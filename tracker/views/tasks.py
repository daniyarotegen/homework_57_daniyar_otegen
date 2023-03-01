from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from tracker.forms import TaskForm
from tracker.models.status import StatusChoice
from tracker.models.type import TypeChoice


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'task_create.html', context={
            'form': form,
            'choices': StatusChoice.choices,
            'types': TypeChoice.choices
        })
    form = TaskForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'task_create.html', context={
            'form': form,
            'choices': StatusChoice.choices,
            'types': TypeChoice.choices
        })
    else:
        task = form.save()
        return redirect('task_detail', pk=task.pk)

