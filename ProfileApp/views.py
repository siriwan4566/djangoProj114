from django.shortcuts import render,HttpResponse

# Create your views here.

def tests(request):
    return HttpResponse("<H1>Hello Word <br> This is My Word Wide Web </H1>")

def home(request):
    return render(request,'home.html')

def profile(request):
    return render(request, 'profile.html')

def education(request):
    return render(request,'education.html')

def interests(request):
    return render(request,'interests.html')

def dreamJob(request):
    return render(request,'dreamJob.html')

def idol(request):
    return render(request,'idol.html')

def hny (request):
    return render(request,'hny.html')

def myData (request):
    name = "Siriwan"
    surname = "Saengaunurai"
    gender = "G"
    status = "student"
    work = "RMUTI.Khonkean"
    education = "dgree"
    return render(request,'myData.html',
    {'name':name, 'surname':surname,'gender':gender,
     'status':status,'work':work, 'education':education} )



