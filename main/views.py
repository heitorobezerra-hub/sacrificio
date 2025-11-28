from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from main.models import Task

class TaskList(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tarefas'