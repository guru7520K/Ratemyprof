from django.shortcuts import render, redirect
from django import forms
from ratings.models import Rating
# Create your views here.
class NewProfForm(forms.Form):
    name = forms.CharField(label="New Professor")
    marks=forms.IntegerField(label="Ratings out of 5")

def index(request):
    return render(request,"ratings/index.html")


def add(request):
    if request.method =="POST":
        form=NewProfForm(request.POST)
        if form.is_valid():
            prof= form.cleaned_data
            name = prof["name"]
            marks = prof["marks"]
            obj = Rating(professor=name, rating=marks)
            obj.save()
            print("redirecting...")
            return redirect("rating")
        else:
            return render(request, "rating/add.html"),{
                "form": form
            }
    return render(request,"ratings/add.html",{
        "form": NewProfForm()
         
    })

def prof(request):
    professors = Rating.objects.all()
    return render(request,"ratings/ratings.html",{
        "professors": professors
    }
    )