from fastapi import FastAPI
from app.database import Base, engine
from app.routes import availability, booking

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Doctor Appointment API")

app.include_router(availability.router, prefix="/api/calendly", tags=["availability"])
app.include_router(booking.router, prefix="/api/calendly", tags=["booking"])