from django.shortcuts import render

# Create your views here.
def home(reauest):
    return render(reauest, 'portal/index.html')