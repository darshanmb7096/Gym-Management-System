from email.headerregistry import Address
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact
from authapp.models import MembershipPlan
from authapp.models import Trainer
from authapp.models import Enrollment,Attendance,Gallery
# Create your views here.
def Home(request):
    return render(request,"index.html")


def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
      
        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/signup')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/login')
        
        
    return render(request,"signup.html")




def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
            
        
    return render(request,"handlelogin.html")


def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/login')

def contact(request):
    
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()       
        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
    
    return render(request,"contact.html")

def enroll(request):
        if not request.user.is_authenticated:
            messages.warning(request,"Please Login and Try Again")
            return redirect('/login')
    
        Membership=MembershipPlan.objects.all()
        SelectTrainer=Trainer.objects.all()
        context={"Membership":Membership,"SelectTrainer":SelectTrainer}
        if request.method=="POST":
            fullname=request.POST.get('FullName')
            email=request.POST.get('email')
            gender=request.POST.get('gender')
            number=request.POST.get('PhoneNumber')
            dob=request.POST.get('DOB')
            Membershipplan=request.POST.get('member')
            SelectTrainer=request.POST.get('trainer')
            referedby=request.POST.get('reference')
            address=request.POST.get('address')
            query=Enrollment(FullName=fullname,Email=email,Gender=gender,PhoneNumber=number,DOB=dob,
                            SelectMembershipplan=Membershipplan,SelectTrainer=SelectTrainer,Reference=referedby,Address=address)
            query.save()       
            messages.success(request,"Thanks for Enrolling Welcome to the team")
            return redirect('/join')
        return render(request,"enroll.html",context)
    
def workouts(request):
    return render(request,"workouts.html")

def viewprofile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    user_phone=request.user
    posts=Enrollment.objects.filter(PhoneNumber=user_phone)
    print(posts)
    context={"posts":posts}
    
    return render(request,"viewprofile.html",context)

def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    SelectTrainer=Trainer.objects.all()
    context={"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        phonenumber=request.POST.get('PhoneNumber')
        Login=request.POST.get('logintime')
        Logout=request.POST.get('loginout')
        SelectWorkout=request.POST.get('workout')
        TrainedBy=request.POST.get('trainer')
        query=Attendance(phonenumber=phonenumber,Login=Login,Logout=Logout,SelectWorkout=SelectWorkout,TrainedBy=TrainedBy)
        query.save()
        messages.warning(request,"Attendace Applied Success")
        return redirect('/attendance')
    return render(request,"attendance.html",context)

def checkattendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    user_phone=request.user
    attendance=Attendance.objects.filter(phonenumber=user_phone)
    print(attendance)
    context={"attendance":attendance}
    
    return render(request,"checkattendance.html",context)

def gallery(request):
    posts=Gallery.objects.all()
    context={"posts":posts}
    return render(request,"gallery.html",context)


def gainmuscle(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    return render(request,"gainmuscle.html")

def gainstrength(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    return render(request,"gainstrength.html")

def loseweight(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    return render(request,"loseweight.html")

def getfit(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    return render(request,"getfit.html")

def suggest(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    return render(request,"suggest.html")






