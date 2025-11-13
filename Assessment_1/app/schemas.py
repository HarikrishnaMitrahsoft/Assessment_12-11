from pydantic import BaseModel
from datetime import date, time
from typing import Optional, Dict, Any

class Slot(BaseModel):
    id: int
    start_time: str
    end_time: str
    available: bool

    class Config:
        from_attributes = True


class AvailabilityResponse(BaseModel):
    date: date
    available_slots: list[Slot]


class Patient(BaseModel):
    name: str
    email: str
    phone: str


class BookingRequest(BaseModel):
    appointment_type: str
    date: date
    start_time: str
    patient: Patient
    reason: str

class BookingDetails(BaseModel):
    appointment_type: str
    date: date
    start_time: time
    end_time: time | None = None
    patient: Patient
    reason: str

class BookingResponse(BaseModel):
    booking_id: Optional[str] = None
    status: str
    confirmation_code: Optional[str] = None
    details: Optional[Dict[str, Any]] = None

    class Config:
        from_attributes = True
