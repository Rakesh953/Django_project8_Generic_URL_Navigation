from django.shortcuts import render

# Create your views here.
def url_navigation1(request):
    return render(request,'url_navigation1.html')

def url_navigation2(request):
    return render(request,'url_navigation2.html')