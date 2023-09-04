# cli.py
import click
from models import Student, Course, Session

@click.group()
def cli():
    """Student Tracker CLI"""

@cli.command()
@click.option('--name', prompt='Student Name', help='Name of the student')
@click.option('--student-id', prompt='Student ID', help='Student ID')
def add_student(name, student_id):
    """Add a new student"""
    session = Session()
    student = Student(name=name, student_id=student_id)
    session.add(student)
    session.commit()
    session.close()
    click.echo(f'Student "{name}" with ID "{student_id}" added successfully.')

@cli.command()
def list_students():
    """List all students"""
    session = Session()
    students = session.query(Student).all()
    session.close()
    if students:
        click.echo("List of Students:")
        for student in students:
            click.echo(f'Student ID: {student.student_id}, Name: {student.name}')
    else:
        click.echo('No students found.')

@cli.command()
@click.option('--name', prompt='Course Name', help='Name of the course')
def add_course(name):
    """Add a new course"""
    session = Session()
    course = Course(name=name)
    session.add(course)
    session.commit()
    session.close()
    click.echo(f'Course "{name}" added successfully.')

@cli.command()
def list_courses():
    """List all courses"""
    session = Session()
    courses = session.query(Course).all()
    session.close()
    if courses:
        click.echo("List of Courses:")
        for course in courses:
            click.echo(f'Course ID: {course.id}, Name: {course.name}')
    else:
        click.echo('No courses found.')

@cli.command()
@click.option('--student-id', prompt='Student ID', help='Student ID')
@click.option('--course-id', prompt='Course ID', help='Course ID')
def enrol_student(student_id, course_id):
    """Enroll a student in a course"""
    session = Session()

    # Fetch the student and course within the same session
    student = session.query(Student).filter_by(student_id=student_id).first()
    course = session.query(Course).filter_by(id=course_id).first()

    if not student:
        click.echo(f'Student with ID "{student_id}" not found.')
        session.close()
        return

    if not course:
        click.echo(f'Course with ID "{course_id}" not found.')
        session.close()
        return

    student.courses.append(course)
    session.commit()
    click.echo(f'Student "{student.name}" with ID "{student.student_id}" enrolled in course "{course.name}" successfully.')

    # Close the session after the operation
    session.close()

if __name__ == '__main__':
    cli()


