from ..repositories.registration_repository import RegistrationRepository
from ..models.registration import Registration

class RegistrationService:
    def __init__(self):
        self.registration_repo = RegistrationRepository()

    def enroll_student(self, student_id, course_id):
        # Check if already enrolled
        existing_enrollment = self.registration_repo.get_by_student_and_course(student_id, course_id)
        if existing_enrollment:
            raise Exception("Student is already enrolled in this course.")

        registration = Registration(student_id, course_id)
        self.registration_repo.add(registration)

    def get_students_in_course(self, course_id):
        return self.registration_repo.get_students_by_course(course_id)

    def get_courses_for_student(self, student_id):
        return self.registration_repo.get_courses_by_student(student_id)
