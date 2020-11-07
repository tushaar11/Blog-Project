from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog
# Create your views here.

def home(request):
    if 'user' not in request.session:
        return redirect('/')
    username=request.session['user']
    blogs = Blog.objects.all()
    print(username)
    return render(request, 'home.html', {
        'blogs': blogs,
        'user': username
    })

def profile(request):
    if 'user' not in request.session:
        return redirect('/')
    username=request.session['user']
    blogs=Blog.objects.filter(username=username)
    return render(request, 'profile.html', {
        'blogs': blogs,
        'user': username
    })

def addblogs(request):
    if 'user' not in request.session:
        return redirect('/')
    username=request.session['user']
    if request.method=='POST':
        title=request.POST['title']
        description=request.POST['description']
        blog=Blog(username=username,title=title,description=description)
        blog.save()
        return redirect('profile')
    else:
        return render(request,'addblog.html',{
            'user': username
        })

def blogPage(request,id):
    if 'user' not in request.session:
        return redirect('/')
    username=request.session['user']
    blog=Blog.objects.get(id=id)
    return render(request,'BlogPage.html',{ 'blog': blog , 'user':username })

def editBlog(request,id):
    if 'user' not in request.session:
        return redirect('/')
    
    if request.method == 'POST':
        title=request.POST['title']
        description=request.POST['description']
        Blog.objects.filter(id=id).update(title=title,description=description)
        return redirect('home')

    blog=Blog.objects.get(id=id)
    return render(request,'editBlog.html',{ 'blog': blog })

def deleteBlog(request,id):
    if 'user' not in request.session:
            return redirect('/')
    
    if request.method == 'POST':
        blog=Blog.objects.get(id=id)
        blog.delete()
        return redirect('home')
