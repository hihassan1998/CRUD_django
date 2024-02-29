# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

<<<<<<< HEAD
from crud.models import *
from datetime import date


# Code starts from here:
def write_instructors():
    # Add instructors
    # Create a user
    user_john = User(first_name='John', last_name='Doe', dob=date(1962, 7, 16))
    user_john.save()
    instructor_john = Instructor(full_time=True, total_learners=30050)
    # Update the user reference of instructor_john to be user_john
    instructor_john.user = user_john
    instructor_john.save()
    
    instructor_yan = Instructor(first_name='Yan', last_name='Luo', dob=date(1962, 7, 16), full_time=True, total_learners=30050)
    instructor_yan.save()

    instructor_joy = Instructor(first_name='Joy', last_name='Li', dob=date(1992, 1, 2), full_time=False, total_learners=10040)
    instructor_joy.save()
    instructor_peter = Instructor(first_name='Peter', last_name='Chen', dob=date(1982, 5, 2), full_time=True, total_learners=2002)
    instructor_peter.save()
    print("Instructor objects all saved... ")

def write_courses():
    # Add Courses
    course_cloud_app = Course(name="Cloud Application Development with Database",
                              description="Develop and deploy application on cloud")
    course_cloud_app.save()
    course_python = Course(name="Introduction to Python",
                           description="Learn core concepts of Python and obtain hands-on "
                                       "experience via a capstone project")
    course_python.save()

    print("Course objects all saved... ")

def write_lessons():
    # Add lessons
    lession1 = Lesson(title='Lesson 1', content="Object-relational mapping project")
    lession1.save()
    lession2 = Lesson(title='Lesson 2', content="Django full stack project")
    lession2.save()
    print("Lesson objects all saved... ")

def clean_data():
    # Delete all data to start from fresh
    Enrollment.objects.all().delete()
    User.objects.all().delete()
    Learner.objects.all().delete()
    Instructor.objects.all().delete()
    Course.objects.all().delete()
    Lesson.objects.all().delete()

# Clean any existing data first
clean_data()
write_courses()
write_instructors()
write_lessons()

def write_learners():
=======
from related_objects.models import *
from datetime import date


# My code starts from here:
def populate_instructors():
    # Add instructors
    user_john = User(first_name='John', last_name='Doe', dob=date(1962, 7, 16))
    user_john.save()
    instructor_john = Instructor(full_time=True,
                                total_learners=30050)
    instructor_john.user = user_john
    instructor_john.save()

    instructor_yan = Instructor(first_name='Yan', last_name='Luo', dob=date(1962, 7, 16),
                                full_time=True,
                                total_learners=30050)
    instructor_yan.save()

    instructor_joy = Instructor(first_name='Joy', last_name='Li', dob=date(1992, 1, 2),
                                full_time=False,
                                total_learners=10040)
    instructor_joy.save()
    instructor_peter = Instructor(first_name='Peter', last_name='Chen', dob=date(1982, 5, 2),
                                  full_time=True,
                                  total_learners=2002)
    instructor_peter.save()
    print("Instructors objects saved... ")


def populate_learners():
>>>>>>> 47a491c (Query Spanning Relationships checking from cloud ide)
    # Add Learners
    learner_james = Learner(first_name='James', last_name='Smith', dob=date(1982, 7, 16),
                            occupation='data_scientist',
                            social_link='https://www.linkedin.com/james/')
    learner_james.save()
<<<<<<< HEAD
=======

>>>>>>> 47a491c (Query Spanning Relationships checking from cloud ide)
    learner_mary = Learner(first_name='Mary', last_name='Smith', dob=date(1991, 6, 12), occupation='dba',
                           social_link='https://www.facebook.com/mary/')
    learner_mary.save()
    learner_robert = Learner(first_name='Robert', last_name='Lee', dob=date(1999, 1, 2), occupation='student',
                             social_link='https://www.facebook.com/robert/')
    learner_robert.save()
    learner_david = Learner(first_name='David', last_name='Smith', dob=date(1983, 7, 16),
                            occupation='developer',
                            social_link='https://www.linkedin.com/david/')
    learner_david.save()
<<<<<<< HEAD
=======

>>>>>>> 47a491c (Query Spanning Relationships checking from cloud ide)
    learner_john = Learner(first_name='John', last_name='Smith', dob=date(1986, 3, 16),
                           occupation='developer',
                           social_link='https://www.linkedin.com/john/')
    learner_john.save()
<<<<<<< HEAD
    print("Learner objects all saved... ")
    #<HINT> Add more learners objects#
    #...

    # Clean any existing data first
clean_data()
write_courses()
write_instructors()
write_lessons()
write_learners()
=======
    print("Learners objects saved... ")


def populate_lessons():
    # Add lessons
    lession1 = Lesson(title='Lesson 1', content="Object-relational mapping project")
    lession1.save()
    lession2 = Lesson(title='Lesson 2', content="Django full stack project")
    lession2.save()
    print("Lessons objects saved... ")


def clean_data():
    # Delete all data to start from fresh
    Enrollment.objects.all().delete()
    User.objects.all().delete()
    Learner.objects.all().delete()
    Instructor.objects.all().delete()
    Course.objects.all().delete()
    Lesson.objects.all().delete()

def populate_courses():
    # Add Courses
    course_cloud_app = Course(name="Cloud Application Development with Database",
                              description="Develop and deploy application on cloud")
    course_cloud_app.save()
    course_python = Course(name="Introduction to Python",
                           description="Learn core concepts of Python and obtain hands-on "
                                       "experience via a capstone project")
    course_python.save()
    print("Course objects saved... ")

def populate_course_instructor_relationships():
    # Get related instructors
    instructor_yan = Instructor.objects.get(first_name='Yan')
    instructor_joy = Instructor.objects.get(first_name='Joy')
    instructor_peter = Instructor.objects.get(first_name='Peter')

    # Get related courses
    course_cloud_app = Course.objects.get(name__contains='Cloud')
    course_python = Course.objects.get(name__contains='Python')

    # Add instructors to courses
    course_cloud_app.instructors.add(instructor_yan)
    course_cloud_app.instructors.add(instructor_joy)
    course_python.instructors.add(instructor_peter)
    
    print("Course-instructor relationships saved... ")


def populate_course_enrollment_relationships():

    # Get related courses
    course_cloud_app = Course.objects.get(name__contains='Cloud')
    course_python = Course.objects.get(name__contains='Python')

    # Get related learners
    learner_james = Learner.objects.get(first_name='James')
    learner_mary = Learner.objects.get(first_name='Mary')
    learner_david = Learner.objects.get(first_name='David')
    learner_john = Learner.objects.get(first_name='John')
    learner_robert = Learner.objects.get(first_name='Robert')

    # Add enrollments
    james_cloud = Enrollment.objects.create(learner=learner_james, date_enrolled=date(2020, 8, 1),
                                            course=course_cloud_app, mode='audit')
    james_cloud.save()
    mary_cloud = Enrollment.objects.create(learner=learner_mary, date_enrolled=date(2020, 8, 2),
                                         course=course_cloud_app, mode='honor')
    mary_cloud.save()
    david_cloud = Enrollment.objects.create(learner=learner_david, date_enrolled=date(2020, 8, 5),
                                            course=course_cloud_app, mode='honor')
    david_cloud.save()
    david_cloud = Enrollment.objects.create(learner=learner_john, date_enrolled=date(2020, 8, 5),
                                           course=course_cloud_app, mode='audit')
    david_cloud.save()
    robert_python = Enrollment.objects.create(learner=learner_robert, date_enrolled=date(2020, 9, 2),
                                              course=course_python, mode='honor')
    robert_python.save()
    print("Course-learner relationships saved... ")

def create_dummy_data():
    # Create a dummy learner
    dummy_learner = Learner(first_name='Dummy', last_name='Learner', dob=date(2000, 1, 1),
                            occupation='student', social_link='https://www.exDummy.com/dummy/')
    dummy_learner.save()

    # Create a dummy instructor
    dummy_instructor = Instructor(first_name='Dummy', last_name='Instructor', dob=date(1980, 1, 1),
                                  full_time=True, total_learners=100)
    dummy_instructor.save()

    # Create a dummy course
    dummy_course = Course(name='Dummy Course', description='A dummy course for testing purposes')
    dummy_course.save()

    # Establish relationships
    dummy_course.instructors.add(dummy_instructor)
    Enrollment.objects.create(learner=dummy_learner, date_enrolled=date(2022, 1, 1),
                              course=dummy_course, mode='audit')

    print("Dummy data and relationships created...")

# Clean data before populating
clean_data()

# Populate data
populate_courses()
populate_instructors()
populate_learners()
populate_lessons()
populate_course_instructor_relationships()
populate_course_enrollment_relationships()

# Create dummy data and relationships
create_dummy_data()
populate_courses()
populate_instructors()
populate_learners()
populate_lessons()

#Populate relationships
populate_course_instructor_relationships()
populate_course_enrollment_relationships()
>>>>>>> 47a491c (Query Spanning Relationships checking from cloud ide)
