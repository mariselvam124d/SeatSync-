from django.db import models

# Model for the Admin (User)
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=[('staff', 'Staff'), ('admin', 'Admin')])

    def __str__(self):
        return self.username

# Model for Students
class Student(models.Model):
    roll_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    class_name = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    semester = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"

# Model for Exams
class Exam(models.Model):
    exam_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    exam_date = models.DateField()
    exam_time = models.TimeField()

    def __str__(self):
        return f"{self.exam_name} - {self.subject}"

# Model for Exam Halls
class ExamHall(models.Model):
    hall_name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Hall {self.hall_name}"

# Model for Allocations
class HallAllocation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    exam_hall = models.ForeignKey(ExamHall, on_delete=models.CASCADE)
    allocation_date = models.DateField()
    allocation_time = models.TimeField()

    def __str__(self):
        return f"Roll: {self.student.roll_number} - Hall {self.exam_hall.hall_name} - {self.exam.exam_name}"
