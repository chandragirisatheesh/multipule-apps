from django.shortcuts import render

# Create your views here.
def a1_frist(request):
    d={'a':100,'b':200}
    return render(request,'a1_frist.html',d)


def a1_second(request):
    d={'a':123,'b':234,'c':2343}
    return render(request,'a1_second.html',d)