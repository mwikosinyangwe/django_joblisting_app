from django.shortcuts import render, redirect, get_object_or_404
from .models import *

from .forms import *

def create(request):
    if request.method == "POST":
        form = CreateJobForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreateJobForm()
            return redirect("/")
    else:
        form = CreateJobForm()

    jobs = Job.objects.all()
    context = {'form':form, 'jobs':jobs}
    return render(request, "create_view.html", context)


def home(request):
    jobs = Job.objects.all()
    context = { 'jobs':jobs}
    
    return render(request, 'home.html', context)

def detail(request, pk):
    
    jobs = Job.objects.get(pk = pk)
    context = {'jobs':jobs}
         
    return render(request, "detail.html", context)


def DeleteJob(request, pk):

    
    jobs = Job.objects.get(pk=pk)
    if request.method =="POST":

        jobs.delete()
        return redirect("/")
        
    return render(request, "delete.html", {'jobs':jobs})
