from django.shortcuts import render, redirect
from .models import ToDo
# Create your views here.

def todo_list(request):
    todos = ToDo.objects.order_by('-id')
    return render(request, 'todo/index.html', {'todos':todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        ToDo.objects.create(title=title, description=description)
        
        # return redirect('todo_list')

# import requests

def complete_todo(request, home_id):
    tod = ToDo.objects.get(id = home_id)
    ToDo.completed = True
    ToDo.save()
    return redirect('todo_list')
    

def delete_todo(request, home_id):
    tod = ToDo.objects.get(id = home_id)
    ToDo.delete()
    return redirect('todo_list') 