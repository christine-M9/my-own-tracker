from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define a many-to-many association table
student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    student_id = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True)  # Add email as an attribute
    
    # Define a many-to-many relationship with Course
    courses = relationship('Course', secondary=student_courses, back_populates='students')

    def get_enrolled_courses(self):
        return [course.name for course in self.courses]

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)  # Add course description as an attribute
    
    # Define a many-to-many relationship with Student
    students = relationship('Student', secondary=student_courses, back_populates='courses')

# Create the database engine and session
DATABASE_URI = 'sqlite:///student_tracker.db'  # Use SQLite for simplicity, replace with your preferred database
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

# Create the database tables
Base.metadata.create_all(engine)
