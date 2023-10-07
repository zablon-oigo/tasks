from django.shortcuts import render,redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'task/land.html')


@login_required
def list_task(request):
    tasks=Task.objects.filter(created_by=request.user).order_by('-created_at')[:6]
    context={'tasks':tasks}
    return render(request, 'task/list.html',context)

def detail_task(request, id, slug):
    task=get_object_or_404(Task, id=id, slug=slug, created_by=request.user)
    context={'task':task}
    return render(request, 'task/detail.html', context)
@login_required
def create_task(request):
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.created_by=request.user
            task.status='Pending'
            task.save()
            return redirect('list')
    else:
        form=TaskForm()
    return render(request, 'task/create.html',{'form':form})

@login_required      
def update_task(request, id):
    task=get_object_or_404(Task, id=id , created_by=request.user)
    if request.method == 'POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('list' )
    else:
        form=TaskForm(instance=task)    
    return render(request, 'task/create.html',{'task':task,'id':id,'form':form})
@login_required
def delete_task(request, id):
    task=get_object_or_404(Task, created_by=request.user, id=id )
    if request.method == 'POST':
        task.delete()
        return redirect('list')
    return render(request, 'task/delete.html',{'task':task})

def task_complete(request,pk):
    task=Task.objects.get(pk=pk)
    task.created_by=request.user
    task.status='Completed'
    task.save()
    return redirect('list')

