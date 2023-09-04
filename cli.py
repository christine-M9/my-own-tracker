import click
from models import Student
from database import Session

@click.command
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

if __name__ == '__main__':
    add_student()

