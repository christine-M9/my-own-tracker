# models.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    student_id = Column(String, nullable=False, unique=True)

# Replace 'sqlite:///student_tracker.db' with your preferred database URI (e.g., PostgreSQL, MySQL).
DATABASE_URI = 'sqlite:///student_tracker.db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

# Create the database tables
Base.metadata.create_all(engine)