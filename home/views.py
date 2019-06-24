from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'home.html')
def home_view1(request):
    return render(request,'home1.html')
def login_view(request):
    return render(request,'design.html')
def signup_view(request):
    return render(request,'signup.html')
def new_view(request):
    return render(request,'newhome.html')

