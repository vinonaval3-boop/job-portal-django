from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import ApplicationForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# 🔹 Job List
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


# 🔹 Job Detail + Apply (🔒 Protected)
@login_required(login_url='login')
def job_detail(request, id):
    job = get_object_or_404(Job, id=id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job

            # 🔥 IMPORTANT (ADD THIS LINE)
            application.user = request.user

            application.save()
            return redirect('job_list')
    else:
        form = ApplicationForm()

    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'form': form
    })


# 🔹 Register
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('job_list')
    else:
        form = UserCreationForm()

    return render(request, 'jobs/register.html', {'form': form}) 
from .models import Application

@login_required(login_url='login')
def dashboard(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'jobs/dashboard.html', {'applications': applications})