from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class AvailabilitySlot(Base):
    __tablename__ = "availability_slots"

    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    bookings = relationship("Booking", back_populates="slot")


class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(String, unique=True, index=True)
    slot_id = Column(Integer, ForeignKey("availability_slots.id"))
    date = Column(Date, nullable=False)
    appointment_type = Column(String, nullable=False)
    patient_name = Column(String, nullable=False)
    patient_email = Column(String, nullable=False)
    patient_phone = Column(String, nullable=False)
    reason = Column(String, nullable=True)
    confirmation_code = Column(String, nullable=False)
    status = Column(String, default="confirmed")

    slot = relationship("AvailabilitySlot", back_populates="bookings")