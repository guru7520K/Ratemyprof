from django.shortcuts import render
from django import forms 
# Create your views here.

professors=[]
class NewProfForm(forms.Form):
    name = forms.CharField(label="New Professor")
    marks=forms.IntegerField(label="Ratings out of 5")

def index(request):
    return render(request,"ratings/index.html")


def add(request):
    if request.method =="POST":
        form=NewProfForm(request.POST)
        if form.is_valid():
            prof= form.cleaned_data["prof"]
            professors.append(prof)
        else:
            return render(request, "rating/add.html"),{
                "form": form
            }
    return render(request,"ratings/add.html",{
        "form": NewProfForm()
         
    })

def prof(request):
    return render(request,"ratings/ratings.html",{
        "professors": professors
    }
    )