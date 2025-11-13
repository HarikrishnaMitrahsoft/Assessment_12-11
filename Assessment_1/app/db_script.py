from database import engine, SessionLocal, Base
from models import AvailabilitySlot
from datetime import datetime

def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Check if already initialized
    if db.query(AvailabilitySlot).count() == 0:
        slots = [
            ("09:00", "09:30"),
            ("09:30", "10:00"),
            ("10:00", "10:30"),
            ("10:30", "11:00"),
            ("11:00", "11:30"),
            ("11:30", "12:00"),
        ]
        for start, end in slots:
            db.add(AvailabilitySlot(
                start_time=datetime.strptime(start, "%H:%M").time(),
                end_time=datetime.strptime(end, "%H:%M").time(),
            ))
        db.commit()
        print("Master slots inserted.")
    else:
        print("Slots already exist.")
    db.close()

if __name__ == "__main__":
    init_db()