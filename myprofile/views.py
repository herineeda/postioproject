from django.shortcuts import render, redirect
from .models import Career, License, Portfolio, Profile
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django import forms
from .forms import CareerForm, LicenseForm
from myprofile import views
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator

# 본인 마이페이지 (수정 가능)
def mypage(request):
    careers = Career.objects.all()
    licenses = License.objects.all()
    portfolios = Portfolio.objects.all()
    portfolio_list = Portfolio.objects.all()
    paginator = Paginator(portfolio_list, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    profile = Profile.objects.all()
    return render(request, 'mypage.html', {'careers':careers, 'licenses':licenses, 'portfolios':portfolios, 'profile':profile, 'posts':posts})
    
# 다른사람 프로필 (수정 불가)
def viewprofile(request):
    careers = Career.objects.all()
    licenses = License.objects.all()
    portfolios = Portfolio.objects.all()
    portfolio_list = Portfolio.objects.all()
    paginator = Paginator(portfolio_list, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    profile = Profile.objects.all()
    return render(request, 'viewprofile.html', {'careers':careers, 'licenses':licenses, 'portfolios':portfolios, 'profile':profile, 'posts':posts})

# 프로필 추가하기
class ProfileUploadView(CreateView):
    model = Profile
    fields = ['profile_photo', 'introduction']
    template_name = 'newprofile.html'
    
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/mypage')
        else:
            return self.render_to_response({'form':form})

# 포트폴리오 추가하기        
class PortfolioUploadView(CreateView):
    model = Portfolio
    fields = ['photo', 'title_photo', 'text_photo']
    template_name = 'newportfolio.html'
    
    def form_valid(self, form):
        form.instance.p_author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/mypage')
        else:
            return self.render_to_response({'form':form})

# 경력사항 추가하기
class CareerUploadView(CreateView):
    form_class = CareerForm
    template_name = 'newcareer.html'
    
    def form_valid(self, form):
        form.instance.c_author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/mypage')
        else:
            return self.render_to_response({'form':form})

# 자격사항 추가하기   
class LicenseUploadView(CreateView):
    form_class = LicenseForm
    template_name = 'newlicense.html'
    
    def form_valid(self, form):
        form.instance.l_author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/mypage')
        else:
            return self.render_to_response({'form':form})

# 프로필 수정하기
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['profile_photo', 'introduction']
    template_name = 'updateprofile.html'

# 경력사항 지우기
class CareerDeleteView(DeleteView):
    model = Career
    success_url = '/mypage'
    template_name = 'deletecareer.html'

# 자격사항 지우기
class LicenseDeleteView(DeleteView):
    model = License
    success_url = '/mypage'
    template_name = 'deletelicense.html'
    
# 포트폴리오 지우기
class PortfolioDeleteView(DeleteView):
    model = Portfolio
    success_url = '/mypage'
    template_name = 'deleteportfolio.html'