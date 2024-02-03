from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from datetime import datetime
from django.views.generic import TemplateView


class HomePageViews(TemplateView):
    template_name = 'base.html'

def todo_filter_due(request):
    start_date = datetime.strptime(request.GET.get('start_date'), '%d.%m.%Y')
    end_date = datetime.strptime(request.GET.get('end_date'), '%d.%m.%Y')
    todos = Todo.objects.filter(due_date__range=[start_date, end_date], user=request.user)
    return render(request, 'todo_list.html', {'todos': todos})


def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo_list.html', {'todos': todos})


def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_form.html', {'form': form})


def todo_search_title(request):
    query = request.GET.get('q')
    todos = Todo.objects.filter(title__icontains=query, user=request.user)
    return render(request, 'todo_list.html', {'todos': todos})


