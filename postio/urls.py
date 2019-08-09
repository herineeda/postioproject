
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
import myprofile.views
import postioapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mypage/', include('myprofile.urls')),
    path('', postioapp.views.main, name="main"),
    path('postio/', include('postioapp.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)