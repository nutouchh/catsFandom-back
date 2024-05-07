"""
URL configuration for catsFandom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from accounts.urls import accounts_urlpatterns
from cat.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cat-auth/', include('rest_framework.urls')),
    path('api/v1/cat/', CatAPIList.as_view()),
    path('api/v1/cat/<slug:slug>/', CatAPIUpdate.as_view()),
    path('api/v1/catdelete/<slug:slug>/', CatAPIDestroy.as_view()),
    # path('api/v1/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('api/v1/auth/', include('djoser.urls')),  # new
    # re_path(r'^auth/', include('djoser.urls.authtoken')),  # new
    # path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += accounts_urlpatterns # add URLs for authentication
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MTA4NjA1LCJpYXQiOjE3MTUwMjIyMDUsImp0aSI6IjhiZDllOGNhMDgwZTRlMmE4NTdjMjQ2MmRmNWMwNTYyIiwidXNlcl9pZCI6MX0.tBCctWXCgtMoEtJfEl119WEn8Iasg__tHjUju7IgVB8