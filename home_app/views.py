from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'home_app/home.html')

def price_page(request):
    return render(request,'home_app/price.html')

def lesson_schedule_page(request):
    return render(request,'home_app/lesson_schedule.html')

def instructor_page(request):
    return render(request,'home_app/instructor.html')