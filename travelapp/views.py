from django.shortcuts import render

# Create your views here.
def travelhome(request):
    return render(request,'home.html')

