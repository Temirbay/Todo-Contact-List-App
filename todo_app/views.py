from django.shortcuts import render, redirect

from todo_app.models import Todo, Contact

def index (request):
    return render(request, 'index.html')

def todo_list (request):
    todos = Todo.objects.all().order_by('-created_at')
    return render (request, 'todo/todo_list.html', {"todos": todos, "active_menu": "todo"}) 

def todo_detail (request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    return render (request, 'todo/todo_detail.html', {"todo": todo, "active_menu": "todo"}) 

def todo_add (request):
    if (request.method == 'POST'):
        title = request.POST['title']
        priority = request.POST['priority']
        todo = Todo (title=title, priority=priority)
        todo.save()
        return redirect('/todos')
    else:
        return render(request, "todo/todo_add.html", {"active_menu": "todo"})

def todo_complete (request, todo_id):
    todo = Todo.objects.get (pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('/todos')

def todo_delete (request, todo_id):
    todo = Todo.objects.get (pk=todo_id)
    todo.delete()
    return redirect('/todos')

def todo_update (request, todo_id):
    todo = Todo.objects.get (pk=todo_id)
    if (request.method == 'POST'):
        todo.title = request.POST['title']
        todo.priority = request.POST['priority']
        todo.save()
        return redirect('/todos')
    else:
        return render(request, "todo/todo_update.html", {"active_menu": "todo", "todo": todo})

def todo_sort (request, sort_id):
    if sort_id == 1:
        todos = Todo.objects.all().order_by('-created_at')
    elif sort_id == 2:
        todos = Todo.objects.all().order_by('-updated_at')
    elif sort_id == 3:
        todos = Todo.objects.all().order_by('title')
    elif sort_id == 4:
        todos = Todo.objects.all().order_by('-priority')
    return render (request, 'todo/todo_list.html', {"todos": todos, "active_menu": "todo"}) 
    

def contact_list (request):
    contacts = Contact.objects.all().order_by('created_at')
    return render (request, 'contact/contact_list.html', {"contacts": contacts, "active_menu": "contact"})

def contact_detail (request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    return render (request, 'contact/contact_detail.html', {"contact": contact, "active_menu": "contact"}) 

def contact_add (request):
    if (request.method == 'POST'):
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        contact = Contact (name=name, phone_number=phone_number)
        contact.save()
        return redirect('/contacts')
    else:
        return render(request, "contact/contact_add.html", {"active_menu": "contact"})

def contact_delete (request, contact_id):
    contact = Contact.objects.get (pk=contact_id)
    contact.delete()
    return redirect('/contacts')

def contact_sort (request, sort_id):
    if sort_id == 1:
        contacts = Contact.objects.all().order_by('-created_at')
    if sort_id == 2:
        contacts = Contact.objects.all().order_by('-updated_at')
    elif sort_id == 3:
        contacts = Contact.objects.all().order_by('phone_number')
    elif sort_id == 4:
        contacts = Contact.objects.all().order_by('name')
    return render (request, 'contact/contact_list.html', {"contacts": contacts, "active_menu": "contact"}) 


def contact_update (request, contact_id):
    contact = Contact.objects.get (pk=contact_id)
    if (request.method == 'POST'):
        contact.name = request.POST['name']
        contact.phone_number = request.POST['phone_number']
        contact.save()
        return redirect('/contacts')
    else:
        return render(request, "contact/contact_update.html", {"active_menu": "contact", "contact": contact})
