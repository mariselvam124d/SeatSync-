from django.shortcuts import render, redirect
from .models import Student, Exam, ExamHall, HallAllocation
from .forms import HallAllocationForm
from .models import Student, HallAllocation
from django.urls import reverse

# Admin page to allocate halls
def admin_allocation(request):
    if request.method == 'POST':
        roll_numbers = request.POST.getlist('roll_number')
        exam_id = request.POST.get('exam_id')
        exam = Exam.objects.get(id=exam_id)
        hall = ExamHall.objects.get(hall_name=request.POST['hall_name'])
        date = request.POST['exam_date']
        time = request.POST['exam_time']
        
        for roll_number in roll_numbers:
            student = Student.objects.get(roll_number=roll_number)
            allocation = HallAllocation(
                student=student, exam=exam, exam_hall=hall, allocation_date=date, allocation_time=time
            )
            allocation.save()

        return redirect('allocation_success')

    exams = Exam.objects.all()
    halls = ExamHall.objects.all()
    students = Student.objects.all()
    return render(request, 'admin_allocation.html', {'exams': exams, 'halls': halls, 'students': students})
def student_allocation(request):
    # Show input form to user
    if request.method == 'POST':
        roll_number = request.POST.get('roll_number')
        year = request.POST.get('year')
        semester = request.POST.get('semester')

        # Validate student existence first
        try:
            student = Student.objects.get(roll_number=roll_number, year=year, semester=semester)
            # Redirect to results page with params in URL
            return redirect(reverse('student_allocation_result') + f'?roll_number={roll_number}&year={year}&semester={semester}')
        except Student.DoesNotExist:
            error = 'No student found with provided details.'
            return render(request, 'student_allocation.html', {'error': error})

    # GET request - show empty form
    return render(request, 'student_allocation.html')

def student_allocation_result(request):
    # Read parameters from GET
    roll_number = request.GET.get('roll_number')
    year = request.GET.get('year')
    semester = request.GET.get('semester')

    if roll_number and year and semester:
        try:
            student = Student.objects.get(roll_number=roll_number, year=year, semester=semester)
            allocations = HallAllocation.objects.filter(student=student)
            return render(request, 'student_allocation_result.html', {
                'student': student,
                'allocations': allocations,
            })
        except Student.DoesNotExist:
            return render(request, 'student_allocation_result.html', {
                'error': 'Student matching query does not exist.'
            })
    else:
        # If any param missing, redirect to form page
        return redirect('student_allocation')
def allocation_success(request):
    return render(request, 'allocation_success.html')
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')