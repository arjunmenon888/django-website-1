from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegstrationForms, AccountAuthenticationForm, AccountUpdateForm
from blog.models import BlogPost


def registration_view(request):
    context = {}
    if request.POST:
        form = RegstrationForms(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context = {'forms': form}
    else:
        form = RegstrationForms()
        context = {'forms': form}
    return render(request, 'account/registration.html',context)

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST) 
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request,user)
                return redirect('home')
    else:
        form = AccountAuthenticationForm()
    context = {'forms': form}
    return render(request, 'account/login.html', context)

def account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
                initial={
                    'email': request.user.email,
                    'username': request.user.username
                }
            )   
    blog_post = BlogPost.objects.filter(author=request.user)
    print(request.user)
    context = {
        'forms': form,
        'blog_post':blog_post
        }
    return render(request, 'account/account.html', context)

def must_authenticate(request):
    return render(request, 'account/must_authenticate.html')
