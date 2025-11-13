from sqlalchemy.orm import Session
from app import models
import uuid
from datetime import datetime, timedelta

def create_booking(db: Session, data):
    booking_id = f"APPT-{data.date.year}-{uuid.uuid4().hex[:4].upper()}"
    confirmation_code = uuid.uuid4().hex[:6].upper()

    # Convert start_time string ("10:00") → time object
    start_time_obj = datetime.strptime(data.start_time, "%H:%M").time()
    end_time_obj = (start_time_obj + timedelta(minutes=30)).time()

    appointment = models.Appointment(
        booking_id=booking_id,
        appointment_type=data.appointment_type,
        date=data.date,
        start_time=start_time_obj,
        end_time=None,  # or calculate end time
        patient_name=data.patient.name,
        patient_email=data.patient.email,
        patient_phone=data.patient.phone,
        reason=data.reason,
        status="confirmed",
        confirmation_code=confirmation_code,
    )

    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment
