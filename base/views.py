from django.shortcuts import render

def navigation(request):
    return render(request, "navigation.html")
def home(request):
    return render(request, "home.html")

