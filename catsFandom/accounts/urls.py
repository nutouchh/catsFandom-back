from django.urls import path, include, re_path

accounts_urlpatterns = [
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls.authtoken')),
]
