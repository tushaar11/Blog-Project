from django.shortcuts import render,redirect

# Create your views here.

def landing(request):
    if 'user' in request.session:
        return redirect('blog/home')
    return render(request,'landing.html') 