from django.shortcuts import render

# Create your views here.
def a2_frist(request):
    d={'a':100,'b':500,'c':9000}
    return render(request,'a2_frist.html',d)

def a2_second(request):
    d={'name':'TEJA'}
    return render(request,'a2_second.html',d)
