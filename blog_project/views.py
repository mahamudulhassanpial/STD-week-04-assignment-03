from django.shortcuts import render
from task.models import task

def home(request):
    data = task.objects.all()
    print(data)
    # for i in data:
    #     print(i.title, i.catagory)
    return render(request, 'home.html', {'data' : data})