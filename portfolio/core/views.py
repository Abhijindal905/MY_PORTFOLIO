from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,'about.html')

def projects(request,*args,**kwargs):
    my_context = {
        'project1' : 'My Portfolio',
        'project2' : 'CRude App'
    }
    return render(request,'projects.html',my_context)

def certificates(request):
    certificate =[
        {'name_of_cert' : 'CS50 Certificate'},
        {'Institute_name' : 'CS50x: Introduction to the Intellectual Enterprises of Computer Science and the Art of Programming'},
        {'Issued' : '2024'},
        {'completed' : 'Python'}
        ]
    return render(request,'certificates.html',{"certificate":certificate})

def resume(request):
    return render(request,'resume.html')