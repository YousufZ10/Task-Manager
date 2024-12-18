from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import TaskForm
from .models import Task

# Create your views here.
def index(request):
    return render(request , 'tasks/index.html' , {
         'tasks': Task.objects.all()
    })

def view_task(request , id):
    task = task.objects.get(pk = id)
    return HttpResponseRedirect(reverse('index')) 

def add(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      new_task_number = form.cleaned_data['task_number']
      new_task_name = form.cleaned_data['task_name']
      new_task_description = form.cleaned_data['task_description']
      new_task_deadline = form.cleaned_data['task_deadline_date']
      new_task_status = form.cleaned_data['task_status']
      

      new_task = Task(
        task_number=new_task_number,
        task_name=new_task_name,
        task_description=new_task_description,
        task_deadline_date=new_task_deadline,
        task_status=new_task_status,
      )
      new_task.save()
      return render(request, 'tasks/add.html', {
        'form': TaskForm(),
        'success': True
      })
  else:
    form = TaskForm()
  return render(request, 'tasks/add.html', {
    'form': TaskForm()
  })

def edit(request, id):
  if request.method == 'POST':
    task = Task.objects.get(pk=id)
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
      form.save()
      return render(request, 'tasks/edit.html', {
        'form': form,
        'success': True
      })
  else:
    task = Task.objects.get(pk=id)
    form = TaskForm(instance=task)
  return render(request, 'tasks/edit.html', {
    'form': form
  })

def delete(request, id):
  if request.method == 'POST':
    task = Task.objects.get(pk=id)
    task.delete()
  return HttpResponseRedirect(reverse('index'))

