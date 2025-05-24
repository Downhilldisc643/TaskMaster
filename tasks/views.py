from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks=Task.objects.all().order_by('-priority', 'due_date') 
    form=TaskForm()

    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'tasks': tasks, 'form': form}
    return render(request, 'tasks/task_list.html', context)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('/')