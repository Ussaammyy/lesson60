from django.shortcuts import render
from . models import mystudents
# Create your views here.
def index(response):
    students=mystudents.objects.all()
    context={"students":students}
    return render(response, "index.html", context)