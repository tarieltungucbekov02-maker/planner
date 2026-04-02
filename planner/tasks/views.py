from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task


# -------------------------
# РЕГИСТРАЦИЯ
# -------------------------
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks:list')
    else:
        form = UserCreationForm()

    return render(request, 'tasks/register.html', {'form': form})


# -------------------------
# СПИСОК ЗАДАЧ
# -------------------------
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-id')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# -------------------------
# ДОБАВЛЕНИЕ ЗАДАЧИ
# -------------------------
@login_required
def task_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title:
            Task.objects.create(
                user=request.user,
                title=title,
                description=description
            )

    return redirect('tasks:list')


# -------------------------
# УДАЛЕНИЕ ЗАДАЧИ
# -------------------------
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('tasks:list')


# -------------------------
# ПЕРЕКЛЮЧЕНИЕ ВЫПОЛНЕНИЯ
# -------------------------
@login_required
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('tasks:list')



