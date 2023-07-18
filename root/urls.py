from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings

urlpatterns = [
    path("", include('dashboard.urls')),
    path("admin/", admin.site.urls),
    path("api-auth/", include('rest_framework.urls')),
    path("accounts/", include('account.urls')),
]

urlpatterns += [
    path('favicon.ico', RedirectView.as_view(url = settings.STATIC_URL + 'assets/img/favicon.ico')),
]