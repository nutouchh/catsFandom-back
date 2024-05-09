from django.urls import path, include, re_path

from accounts.views import CurrentUserView

accounts_urlpatterns = [
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/auth/users/info', CurrentUserView.as_view(), name='user-me'),
]

