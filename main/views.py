from django.shortcuts import render, redirect
from .models import Queue

def home(request):
    queues = Queue.objects.all()
    return render(request, 'home.html', {'queues': queues})

def add_queue(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        phone = request.POST['phone']
        address = request.POST['address']
        reason = request.POST['reason']
        Queue.objects.create(name=name, surname=surname, phone=phone, address=address, reason=reason)
        return redirect('home')
    return render(request, 'add_queue.html')
