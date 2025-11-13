from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import SessionLocal
from app.models import Booking, AvailabilitySlot
from app.schemas import BookingRequest, BookingResponse
import uuid

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/book", response_model=BookingResponse)
def book_appointment(request: BookingRequest, db: Session = Depends(get_db)):
    query_date = request.date
    start_time_obj = datetime.strptime(request.start_time, "%H:%M").time()

    # Find slot_id for that start_time
    slot = db.query(AvailabilitySlot).filter(AvailabilitySlot.start_time == start_time_obj).first()
    if not slot:
        raise HTTPException(status_code=404, detail="Slot not found.")

    # Check if already booked
    existing_booking = (
        db.query(Booking)
        .filter(Booking.slot_id == slot.id, Booking.date == query_date)
        .first()
    )
    if existing_booking:
        return BookingResponse(status="failed", message="Slot is not available.")
    
    booking_id = f"APPT-{request.date.year}-{uuid.uuid4().hex[:4].upper()}"
    confirmation_code = uuid.uuid4().hex[:6].upper()

    # Proceed with booking
    new_booking = Booking(
        booking_id=booking_id,
        appointment_type=request.appointment_type,
        date=request.date,
        slot_id=slot.id,
        patient_name=request.patient.name,
        patient_email=request.patient.email,
        patient_phone=request.patient.phone,
        reason=request.reason,
        status="confirmed",
        confirmation_code=confirmation_code,
    )

    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    return {
        "booking_id": booking_id,
        "status": "confirmed",
        "confirmation_code": confirmation_code,
        "details": {
            "appointment_type": request.appointment_type,
            "date": request.date,
            "start_time": slot.start_time,
            "end_time": slot.end_time,
            "patient": {
                "name": request.patient.name,
                "email": request.patient.email,
                "phone": request.patient.phone,
            },
            "reason": request.reason,
        },
    }