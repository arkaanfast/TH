from django.shortcuts import render
from Tsite.models import Submissions, AnswersKey
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.

@login_required(login_url='register')
def level_6(request):

    submissions = Submissions.objects.get(name=request.user)
    if submissions.phase_2:
        return render(request, 'users/snowden.html')
    
    else:
        return render(request, "users/cheated_message.html")


@login_required(login_url='register')
def check_lvl6(request):

    if request.method == "POST":
        submit = Submissions.objects.get(name=request.user)
        answer_key = AnswersKey.objects.get(a=3)
        answer = request.POST['contact']
        correct_ans = answer_key.lvl_6
        if answer == correct_ans:
            submit.l6 = answer
            submit.l6_time = timezone.now()
            submit.save()
            return render(request, "users/snowden.html", {"success": "Advanced to the next level congrats :)"})
        else:
            return render(request, "users/snowden.html", {"wrong": "Please try Again"})

    if not request.user.is_admin:
        return render(request, "users/cheated_message.html")
            
