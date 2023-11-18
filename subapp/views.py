from django.shortcuts import render

# Create your views here.

def form(request):
    diction = {}
    return render(request, 'subapp/form.html', context = diction)