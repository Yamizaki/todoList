from django.shortcuts import render
from .models import Task
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def showTasks(request):
    Tasks = Task.objects.all()
    Task_Done = len(Task.objects.filter(status="Culminado"))
    Task_Paused = len(Task.objects.filter(status="Pausado"))
    Task_Register = len(Task.objects.all())

    context = {'tasks': Tasks,
                'tasksDone': Task_Done,
                'tasksPaused': Task_Paused,
                'tasksRegister': Task_Register
        }
    
    return  render(request, 'Task/task.html', context)

def add(request):

    try:
        new_title = request.POST["title"]
        new_description = request.POST["description"]
        new_date = request.POST["date_final"]
        db_data = Task(title=new_title, description=new_description, date_final=new_date)
        db_data.save()
        return HttpResponseRedirect(reverse("showTasks"))
    except ValueError as err:
        print(err)
        return HttpResponseRedirect(reverse("showTasks"))

def delete(request, task_id):
    taskDelete = Task.objects.filter(id=task_id)
    taskDelete.delete()
    return HttpResponseRedirect(reverse("showTasks"))

def done(request, task_id):
    taskDone = Task.objects.get(id=task_id)
    taskDone.status="Culminado"
    taskDone.save()
    print(taskDone.status)
    return HttpResponseRedirect(reverse("showTasks"))

def pause(request, task_id):
    taskDone = Task.objects.get(id=task_id)
    taskDone.status="Pausado"
    taskDone.save()
    print(taskDone.status)
    return HttpResponseRedirect(reverse("showTasks"))

def started(request, task_id):
    taskDone = Task.objects.get(id=task_id)
    taskDone.status="Registrado"
    taskDone.save()
    print(taskDone.status)
    return HttpResponseRedirect(reverse("showTasks"))
