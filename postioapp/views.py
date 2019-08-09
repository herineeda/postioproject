# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# post 한거 검색해서 나오는 거
from myprofile.models import Profile, Portfolio
from django.db.models import Q

from .forms import ContactForm
from django.template import loader
from django.core.mail import EmailMessage

# Create your views here.

def main(request):
    portfolios = Portfolio.objects.all()
    portfolio_list = Portfolio.objects.all()
    paginator = Paginator(portfolio_list, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    # searchbar -> qs, q
    qs = Portfolio.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(text_photo__icontains=q)
    return render(request, 'main.html', {'portfolios':portfolios, 'posts':posts, 'post_list':qs, 'q':q})
    
    
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
            request.POST['username'], password=request.POST['password1'], email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
            auth.login(request, user)
            return redirect('main')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('main')

def search(request):
    portfolios = Portfolio.objects.all()
    portfolio_list = Portfolio.objects.all()
    paginator = Paginator(portfolio_list, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    # searchbar -> qs, q
    qs = Portfolio.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(text_photo__icontains=q)
    return render(request, 'search.html', {'portfolios':portfolios, 'posts':posts, 'post_list':qs, 'q':q})

def about(request):
    return render(request,'about.html')
    
def Contact(request):
    Contact_form = ContactForm
    
    if request.method == 'POST':
        form = Contact_form(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')
            
            template = loader.get_template('contact_form.txt') 
            
            context = {
            'contact_name' : request.POST.get('contact_name'),
            'contact_email' : request.POST.get('contact_email'),
            'contact_content' : request.POST.get('contact_content'),
           }
           
            content = template.render(context)
        
            email = EmailMessage(
                "New Contact form email",
                content,
                "Postio Project"+'',
                ['ihyelin185@gmail.com'],
                headers = {'Reply to': contact_email},
                )
                
            email.send()
                
        return render(request, 'contact.html', {'form':form })
        
    else:
        form = Contact_form()
        return render(request, 'contact.html', {'form':form })