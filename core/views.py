from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return redirect('add_task')

def add_task(request, task_id=None):
    tasks = Todo.objects.all()
    if task_id:
        task = get_object_or_404(Todo, pk=task_id)
    else:
        task = None
    
    statuses = ['pending', 'in-progress', 'complete']
    
    if request.method == 'POST':
        if task:
            form = TodoForm(request.POST, instance=task)
        else:
            form = TodoForm(request.POST)
        
        if form.is_valid():
            form.save()
            if task:
                messages.success(request, 'Task updated successfully')
            else:
                messages.success(request, 'Task added successfully')
            return redirect('add_task')
        else:
            messages.error(request, 'Invalid Form')
            return redirect('add_task')
    else:
        form = TodoForm(instance=task)
    return render(request, 'core/index.html', {'form': form, 'task': task, 'tasks': tasks, 'statuses': statuses})
    
    # task = Todo.objects.all()
    # statuses = ['pending', 'in-progress', 'complete']
    
    # if request.method == 'POST':
    #     form = TodoForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Added task successfully')
    #         return redirect('add_task')
    #     else:
    #         messages.error(request, 'Invalid Form')
    #         return redirect('add_task')
    # else:
    #     form = TodoForm()
    # return render(request,'core/index.html', {'form': form, 'task': task, 'statuses': statuses})

# def update_task(request, id):
    task = Todo.objects.get(id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated task successfully')
            return redirect('add_task')
        else:
            messages.error(request, 'Invalid Form')
            return redirect('add_task')
    else:
        form = TodoForm(instance=task)
    # return redirect('add_task')
    return render(request,'core/update_task.html', {'form': form, 'task': task})

def delete_task(request, id):
    task = Todo.objects.get(id=id)
    task.delete()
    messages.error(request, 'Deleted task successfully')
    return redirect('add_task')