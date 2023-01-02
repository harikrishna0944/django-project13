from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name':"hari", "l":[10,20,30]}
    return render(request,"loops.html",d)