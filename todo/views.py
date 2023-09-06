from django.http import HttpResponse
from django.shortcuts import redirect, render
from todo.models import Todo
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def list(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        context = {
            "todos":todos,
        }
        return render(request, "list.html", context)
    
    
def read(request, todo_id):
    if request.method == "GET":
        todo = Todo.objects.get(id=todo_id)
        context = {
            "todo":todo,
        }
        return render(request, "detail.html", context)

@login_required(login_url='/user/login/')
@csrf_exempt    
def create(request):
    if request.method == "GET":
       return render(request, "create.html")
    elif request.method == "POST":
        Todo.objects.create(
            title = request.POST["title"],
            content = request.POST["content"],
            user = request.user,
        )
        return redirect("/todo/")
    
@login_required(login_url='/user/login/')    
@csrf_exempt 
def mytodo(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        todos_list = todos.filter(user_id=request.user.id)
        context = {
            "todos_list":todos_list,
        }
        return render(request, "mytodo.html", context)
    
    
    
@login_required(login_url='/user/login/')    
@csrf_exempt 
def update(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        todo.title = request.POST["title"]
        todo.content = request.POST["content"]
        todo.save()
        return redirect(f"/todo/{todo_id}")
    elif request.method == "GET":
        todo = Todo.objects.get(id=todo_id)
        context = {
            "todo":todo
        }
        return render(request, "update.html", context)
    else :
        return HttpResponse("You are not allowed to delete this todo", status=403)
    
    
