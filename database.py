from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URI = 'sqlite:///student_tracker.db'  # Use SQLite for simplicity, replace with your preferred database

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

# Create the database tables
Base.metadata.create_all(engine)
