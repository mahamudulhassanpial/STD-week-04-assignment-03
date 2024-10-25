from django.shortcuts import render, redirect
from . import forms
from . import models
from .models import task



# Create your views here.
def add_Post(request):
    if request.method == 'POST':
        post_form = forms.taskFrom(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_Post')
    else:
        post_form = forms.taskFrom()
    return render(request, 'add_post.html', {'form' : post_form})

def edit_Post(request, id):
    post = models.task.objects.get(pk=id)
    post_form = forms.taskFrom(instance=post)
    if request.method == 'POST':
        post_form = forms.taskFrom(request.POST,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
        
    return render(request, 'add_post.html', {'form' : post_form})

def delete_Post(request, id):
    post = models.task.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

def show_tasks(request):
    tasks = task.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})

def complete_task(request, task_id):
    task = task.objects(task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('show_tasks')
