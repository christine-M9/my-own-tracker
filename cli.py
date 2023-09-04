# cli.py
import click
from models import Student, Session

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

if __name__ == '__main__':
    cli()



