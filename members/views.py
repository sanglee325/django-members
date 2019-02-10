from django.shortcuts import render, get_object_or_404, redirect
from members.models import Person
# Create your views here.

def index(request):
    return redirect('member')

def member(request):
    member = Person.objects.all()
    return render(request, 'members/list.html', {'member': member})