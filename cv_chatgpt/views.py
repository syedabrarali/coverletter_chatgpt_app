from django.shortcuts import render

def home(request):
    return render(request, 'cv_chatgpt/home.html')