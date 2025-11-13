from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import SessionLocal
from app.models import AvailabilitySlot, Booking
from app.schemas import AvailabilityResponse, Slot

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/availability", response_model=AvailabilityResponse)
def get_availability(
    date: str = Query(...),
    appointment_type: str = Query(..., regex="^(consultation|followup|physical|special)$"),
    db: Session = Depends(get_db)
):
    query_date = datetime.strptime(date, "%Y-%m-%d").date()

    slots = db.query(AvailabilitySlot).all()

    available_slots = []
    for slot in slots:
        booking_exists = (
            db.query(Booking)
            .filter(Booking.date == query_date, Booking.slot_id == slot.id)
            .first()
        )
        available_slots.append({
            "id": slot.id,
            "start_time": slot.start_time.strftime("%H:%M"),
            "end_time": slot.end_time.strftime("%H:%M"),
            "available": booking_exists is None
        })

    return {"date": query_date, "available_slots": available_slots}
