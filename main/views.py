from django.shortcuts import render
from .models import Student

def home_view(request):
    # 1. MODEL: Retrieve all student records from the database
    students = Student.objects.all()
    
    # 2. Prepare the data to be sent to the template
    context = {
        'students': students
    }
    
    # 3. TEMPLATE: Render the HTML template and pass the context
    return render(request, 'main/home.html', context)

# Create your views here.
