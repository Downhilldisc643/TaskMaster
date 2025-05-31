from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Case, When, Value, IntegerField
from .models import Task
from .forms import TaskForm

def task_list(request):
    sort_by=request.GET.get('sort_by', 'due_date') 
    tasks=Task.objects.all()
    if sort_by=='priority':
        tasks=tasks.annotate(
            priority_order=Case(
                When(priority='Low', then=Value(1)),
                When(priority='Medium', then=Value(2)),
                When(priority='High', then=Value(3)),
                output_field=IntegerField()
            )
        ).order_by('priority_order')
    elif sort_by=='status':
        tasks=tasks.order_by('status')
    else:
        tasks=tasks.order_by('due_date')
    form=TaskForm()
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            status=form.cleaned_data['status']
            if status=='Completed':
                return redirect('/')
            else:
                form.save()
                return redirect('/')
    context={
        'tasks': tasks,
        'form': form,
        'sort_by': sort_by
    }
    return render(request, 'tasks/task_list.html', context)

def delete_task(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('/')

def update_status(request, pk):
    task=get_object_or_404(Task, pk=pk)
    new_status=request.POST.get('status')

    if new_status in ['Not Started', 'Started', 'Completed']:
        if new_status=='Completed':
            task.delete()
        else:
            task.status=new_status
            task.save()

    return redirect('/')
