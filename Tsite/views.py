from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Student, Submissions, AnswersKey
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.http import JsonResponse
from phase_2.views import level_6
import cv2
import os
# Create your views here.


def index(request):

    if request.user.is_authenticated:
        return redirect("redirect_user")

    return render(request, 'users/index.html')


def home(request):

    if request.user.is_authenticated:
        return redirect("redirect_user")

    return render(request, 'users/home.html')


# Handles sign in 
def sign_in(request):

    if request.user.is_authenticated:
        return redirect("redirect_user")

    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(username=email, password=password)
    if user:
        login(request, user)
        submissions = Submissions.objects.get(name=request.user)
        if submissions.phase_2:
            return redirect("level_6")
        if submissions.l4:
            return redirect("level_5")
        if submissions.l3:
            return redirect("level_4")
        if submissions.l2:
            return redirect("level_3")
        if submissions.l1:
            return redirect("level_2")
        else:
            return redirect("level_1")

    else:
        return render(request, 'users/home.html', {"ERROR": "EMAIL OR PASSWORD IS INCORRECT"})
# Signin ends here

# Registration 
def register(request):

    if request.user.is_authenticated:
        return redirect("redirect_user")


    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data["password1"]
            user = authenticate(username=email, password=password)
            if user:
                subssion = Submissions(name=user)
                subssion.save()
                login(request, user)
                if request.GET.get('next'):
                  return redirect(request.GET['next'])  
                else:
                    return redirect("level_1")
        else:
            return render(request, 'users/home.html', {'form': form})

    form = StudentRegistrationForm()
    return render(request, 'users/home.html', {'form': form})
    
# Registration end here

# For rendiring the level templates 
@login_required(login_url='register')
def level_1(request):
    submissions = Submissions.objects.get(name=request.user)
    if submissions.phase_2:
        return redirect("level_6")
    if submissions.l4:
        return redirect("level_5")
    if submissions.l3:
        return redirect("level_4")
    if submissions.l2:
        return redirect("level_3")
    if submissions.l1:
        return redirect("level_2")
    else:
        return render(request, "users/l1.html")

@login_required(login_url='register')
def level_2(request):
    submissions = Submissions.objects.get(name=request.user)
    if submissions.phase_2:
        return redirect("level_6")
    if submissions.l4:
        return render(request,"users/l2.html", {"again": "Welcome back :)"})
    if submissions.l3:
        return redirect("level_4")
    if submissions.l2:
        return redirect("level_3")
    if submissions.l1:
        return render(request,"users/l2.html")
    else:
        return render(request, "users/cheated_message.html")


@login_required(login_url='register')
def level_3(request):
    submissions = Submissions.objects.get(name=request.user)
    if submissions.phase_2:
        return redirect("level_6")
    if submissions.l4:
        return redirect("level_5")
    if submissions.l3:
        return redirect("level_4")
    if submissions.l2:
        return render(request, "users/l3.html")
    else:
        return render(request, "users/cheated_message.html")


@login_required(login_url='register')
def level_4(request):

    submissions = Submissions.objects.get(name=request.user)
    if request.method == "POST":
        try:
            answer_key = AnswersKey.objects.get(a=3)
            answer = answer_key.lvl_4
            submitted_file = request.FILES['l4_answer']
            submissions.l4 = submitted_file
            submissions.save()
            submitted_image = cv2.imread(submissions.l4.path)
            answer_image = cv2.imread(answer.path)
            difference = cv2.subtract(submitted_image, answer_image)
            b, g, r = cv2.split(difference)
            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                submissions.l4_time = timezone.now()
                submissions.save()
                return redirect("level_5")
            else:
                submissions.l4.delete()
                return render(request, "users/l4.html", {"fail": "try again :) (make sure its in black and white)"})
        except:
            submissions.l4.delete()
            return render(request, "users/l4.html", {"fail": "try again :) (make sure its in black and white)"})
    
    if submissions.phase_2:
        return redirect("level_6")
    if submissions.l4:
        return redirect("level_5")
    if submissions.l3:
        return render(request, "users/l4.html")
    if submissions.l2:
        return redirect("level_3")
    else:
        return render(request, "users/cheated_message.html")

@login_required(login_url="register")
def level_5(request):

    submissions = Submissions.objects.get(name=request.user)
    if submissions.l4:
        return render(request,"users/last_page.html")
    else:
        return render(request, "users/cheated_message.html")
def hidden(request):
    submissions = Submissions.objects.get(name=request.user)
    if submissions.l4:
        return render(request,"users/l5.html")
    else:
        return render(request, "users/cheated_message.html")
# rendering end here


# For checking out the anser with the db
def check_answer(request):

    if request.method == "POST":
        submit = Submissions.objects.get(name=request.user)
        answer = request.POST["l1_answer"]
        answer_key = AnswersKey.objects.get(a=3)
        lvl1_answer = answer_key.lvl_1
        if answer == lvl1_answer:
            submit.l1 = answer
            submit.l1_time = timezone.now()
            submit.save()
            return render(request, "users/l1.html", {"success": "Advanced to the next level congrats :)"})
        else:
            return render(request, "users/l1.html", {"wrong": "Please try Again"})

    if not request.user.is_admin:

        return render(request, "users/cheated_message.html")


# To not let the user go to any page
@login_required(login_url='register')
def redirect_user(request):
    submissions = Submissions.objects.get(name=request.user)
    if submissions.phase_2:
        return redirect("level_6")
    if submissions.l4:
        return redirect("level_5")
    if submissions.l3:
        return redirect("level_4")
    if submissions.l2:
        return redirect("level_3")
    if submissions.l1:
        return redirect("level_2")
    else:
        return redirect("level_1")

@login_required(login_url='register')
def l4(request):
    try:
        flag = request.session["lvl3_done"]
        submissions = Submissions.objects.get(name=request.user)
        submissions.l3 = "Submitted"
        submissions.l3_time = timezone.now()
        submissions.save()
        return redirect("level_4")
    except:
        return render(request, "users/cheated_message.html")


@login_required(login_url='register')
def lv4_check(request):
    request.session["lvl3_done"] = "Yes"
    return JsonResponse({'response': f'success {request.session["lvl3_done"]}'})
