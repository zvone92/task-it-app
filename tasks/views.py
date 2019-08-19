from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import TaskForm


@login_required
def home(request):
    user = request.user
    # give all objects where this atributte equals this user from request
    tasks = Task.objects.filter(user_profile=user)
    return render(request, 'tasks/home.html', {'tasks':tasks})


@login_required
def add(request):

    form = TaskForm( request.POST or None)

    if form.is_valid():

        task = form.save(commit=False)
         # commit=False tells Django not to send this to database yet.
         # until i make some changes to it
        task.user_profile = request.user # Set the user object
        task.pub_date = timezone.datetime.now() 
        task.save() # Now save it to database
        return redirect('home')

    else:
        return render(request, 'tasks/add.html', {'form':form})


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/detail.html', {'task':task})


def edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    form = TaskForm( request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('home')

    else:
        return render(request, 'tasks/edit.html', {'form':form})




def task_done(request, task_id):

    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    print("product deleted")

    return redirect('home')
