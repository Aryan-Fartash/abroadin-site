from django.contrib import admin
from django.views.decorators.cache import cache_control
from django.contrib.staticfiles.views import serve
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import *

app_name='blog'

urlpatterns = [
    path('',blog_view,name='blog_index'),
    path('4-challenges-international-students-face-in-the-us',challenges_international_students_view,name='4-challenges-international-students'),
    path('4-sources-to-find-scholarships-in-europe',challenges_international_students_europe_view,name='challenges-international-students-europe'),
    path('5-challenges-of-international-students-in-canada',challenges_international_students_canada_view,name='challenges-international-students-canada'),
    path('best-canadian-universities-for-indian-students',canada_indian_students_view,name='best-canadian-universities-for-indian-students'),
    path('test',test_view), 
    path('masters-programs-in-europe',master_europe_view,name='masters-programs-in-europe'),
    path('working-limits-in-canada-for-international-students',working_limit_international_view,name='working-limits-in-canada-for-international-students'),
    path('working-on-a-student-visa',working_on_a_student_visa_view,name='working-on-a-student-visa'),
    path('how-to-apply-to-us-colleges',apply_us_colleges_view,name='how-to-apply-to-us-colleges'),
    path('scholarships-for-african-students',scholarships_african_view,name='scholarships-for-african-students'),
    path('study-data-science-in-europe',data_europe_view,name='study-data-science-in-europe'),
    path('studying-english-in-the-usa',english_usa_view,name='studying-english-in-the-usa'),
    path('study-abroad-consultant',study_abroad_consultant_view,name='study-abroad-consultant'),
    path('fully-funded-scholarships-for-international-students',fully_funded_scholarships_view,name='fully-funded-scholarships'),
    path('free-consultation',free_consultation_view,name='free-consultation'),   
]
