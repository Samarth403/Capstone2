from django.shortcuts import render , HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'About.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'Contact.html')
def tshirts(request):
    return render(request,'tshirts.html')
def mouses(request):
    return render(request,'mouses.html')
def shirts(request):
    return render(request,'shirts.html')
def monitors(request):
    return render(request,'monitors.html')
                                   