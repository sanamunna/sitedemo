from django.shortcuts import render
from django.shortcuts import render
from . models import Place,Review

# Create your views here.
def contact(request):
    obj=Place.objects.all()
    obj2=Review.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})
