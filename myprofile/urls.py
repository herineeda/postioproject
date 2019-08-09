from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.detail import DetailView
from .models import Portfolio, Profile

urlpatterns = [
    # 본인 마이페이지
    path('', mypage, name="mypage"),
    # 다른사람 프로필
    path('viewprofile/', viewprofile, name="viewprofile"),
    # 경력, 자격, 프로필, 포트폴리오 추가
    path('newcareer/', CareerUploadView.as_view(), name="newcareer"),
    path('newlicense/', LicenseUploadView.as_view(), name="newlicense"),
    path('newprofile/', ProfileUploadView.as_view(), name="newprofile"),
    path('newportfolio/', PortfolioUploadView.as_view(), name="newportfolio"),
    # 프로필 수정
    path('updateprofile/<int:pk>/', ProfileUpdateView.as_view(), name="updateprofile"),
    # 경력, 자격, 포트폴리오 삭제
    path('deletecareer/<int:pk>/', CareerDeleteView.as_view(), name="deletecareer"),
    path('deletelicense/<int:pk>/', LicenseDeleteView.as_view(), name="deletelicense"),
    path('deleteportfolio/<int:pk>/', PortfolioDeleteView.as_view(), name="deleteportfolio"),
    # 포트폴리오 자세히보기
    path('detailportfolio/<int:pk>/', DetailView.as_view(model=Portfolio, template_name='detailportfolio.html'), name="detailportfolio"),
    # 프로필 자세히보기
    path('detailprofile/<int:pk>/', DetailView.as_view(model=Profile, template_name='detailprofile.html'), name="detailprofile"),
]