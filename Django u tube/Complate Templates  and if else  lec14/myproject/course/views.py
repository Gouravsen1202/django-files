from django.shortcuts import render
from datetime import datetime # ye time ke liye import kya h
def course(request):
    # dicnary in django
    name="gourav"
    duaration='4 month'
    seats=10
    course_details={'nm':name,'du':duaration,'st':seats}#then isko html file me ja kr so kro
    return render(request,"course/School.html",course_details)
# def Student(request):
#     city='sehore'
#     age=21/

#     job='django'
#     show={'ct':city,'ag':age,'jb':job}
#     d= datetime.now()

#     return render(request,"course/Student.html",show)

# Create your views here.

# exampla 2- if tag 
def Student(request):
    return render(request,"course/Student.html",context={'nm':True})


