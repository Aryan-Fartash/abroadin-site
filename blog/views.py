from django.shortcuts import render
from django.http import HttpResponse

def blog_view(request):
    return render(request,'blog/index.html')

def challenges_international_students_view(request):
    return render(request,'blog/4-challenges-international-students-face-in-the-us.html')

def challenges_international_students_europe_view(request):
    return render(request,'blog/4-sources-to-find-scholarships-in-europe.html')

def challenges_international_students_canada_view(request):
    return render(request,'blog/5-challenges-of-international-students-in-canada.html')

def canada_indian_students_view(request):
    return render(request,'blog/best-canadian-universities-for-indian-students.html')

def test_view(request):
    return render(request,'blog/study-data-science-in-europe.html')

def master_europe_view(request):
    return render(request,'blog/masters-programs-in-europe.html')

def working_limit_international_view(request):
    return render(request,'blog/working-limits-in-canada-for-international-students.html')

def working_on_a_student_visa_view(request):
    return render(request,'blog/working-on-a-student-visa.html')

def apply_us_colleges_view(request):
    return render(request,'blog/how-to-apply-to-us-colleges.html')

def scholarships_african_view(request):
    return render(request,'blog/scholarships-for-african-students.html')

def data_europe_view(request):
    return render(request,'blog/study-data-science-in-europe.html')

def english_usa_view(request):
    return render(request,'blog/studying-english-in-the-usa.html')

def study_abroad_consultant_view(request):
    return render(request,'blog/study-abroad-consultant.html')

def fully_funded_scholarships_view(request):
    return render(request,'blog/fully-funded-scholarships-for-international-students.html')

def free_consultation_view(request):
    return render(request,'blog/free-consultation.html')