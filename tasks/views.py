from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Task, TaskList
from .forms import TaskForm, TaskListForm

def home(request):
    task_lists = TaskList.objects.all()
    context = {
        'task_lists': task_lists,
    }
    return render(request, 'tasks/home.html', context)

def task_list(request, pk):
    task_list = get_object_or_404(TaskList, pk=pk)
    tasks = task_list.tasks.all()
    context = {
        'task_list': task_list,
        'tasks': tasks,
    }
    return render(request, 'tasks/task_list.html', context)

def task_create(request, pk):
    task_list = get_object_or_404(TaskList, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_list = task_list
            task.save()
            return redirect('task_list', pk=pk)
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list', pk=task.task_list.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list', pk=task.task_list.pk)
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def task_list_create(request):
    if request.method == 'POST':
        form = TaskListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskListForm()
    return render(request, 'tasks/task_list_form.html', {'form': form})

def task_list_update(request, pk):
    task_list = get_object_or_404(TaskList, pk=pk)
    if request.method == 'POST':
        form = TaskListForm(request.POST, instance=task_list)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskListForm(instance=task_list)
    return render(request, 'tasks/task_list_form.html', {'form': form})

def task_list_delete(request, pk):
    task_list = get_object_or_404(TaskList, pk=pk)
    if request.method == 'POST':
        task_list.delete()
        return redirect('home')
    return render(request, 'tasks/task_list_confirm_delete.html', {'task_list': task_list})

def update_task_category(request, pk, category):
    task = get_object_or_404(Task, pk=pk)
    task.category = category
    task.save()
    return JsonResponse({'status': 'success'})
