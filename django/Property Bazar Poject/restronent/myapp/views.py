from django.shortcuts import render
from .models import Bazzar

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')
def home1(request):
    return render(request,'myapp/home.html')


def common(request):
    return render(request,'myapp/common.html')


def menu(request):#selling
    return render(request,'myapp/selling.html')
def menu1(request):
    return render(request,'myapp/selling.html')

def order(request):#purchase
    return render(request,'myapp/purchase.html')
def order1(request):
    return render(request,'myapp/purchase.html')

def deshbord(request):
    return render(request,'myapp/desbord.html')

def trackorder(request):
    return render(request,'myapp/track.html')

def trackorder1(request):
    return render(request,'myapp/track.html')

# for login data 

def ragister(request):
    if request.method=='POST':
        print(request.method)
        print(request.POST)
           
        name = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        state = request.POST.get('state')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        print(name, email, phone, dob, state, gender, password, cpassword)
        user = Bazzar.objects.filter(emp_email=email)
        if user:
            msg = "Already have an account"
            return render(request, 'myapp/Ragister.html', {'msg': msg})
        else:
            if password == cpassword:
                Bazzar.objects.create(emp_name=name,emp_email=email,emp_contact=phone,emp_dob=dob,emp_state=state,emp_gender=gender,emp_password=password)
                msg = "Registration successful"
                return render(request, 'myapp/login.html', {'msg': msg})
            else:
                msg = "Password and Confirm Password do not match"
                userdata = {
                    'username': name,
                    'email': email,
                    'phone': phone,
                    'dob': dob,
                    'state': state,
                    'gender': gender
                }
                return render(request, 'myapp/Ragister.html', {'msg': msg, 'data': userdata})
    else:
        return render(request, 'myapp/Ragister.html')    
    
    # login form filiig process
def login(request):
    if request.method=='POST':
       e=request.POST.get('email')
       p=request.POST.get('password')
       user=Bazzar.objects.filter(emp_email=e)

       if user:
           userdata=Bazzar.objects.get(emp_email=e)
           print(userdata.emp_name)
           print(userdata.emp_email)
           p1=userdata.emp_password
           if p==p1:
               return render(request,'myapp/deshbord.html',{'userdata':userdata})
           else:
               msg="password not match"
               return render(request,'myapp/login.html',{'email':e})
       else:
             msg="email does not exist"
             return render(request,'myappp/ragister.html')
       
    else:
        return render(request,'myapp/login.html')