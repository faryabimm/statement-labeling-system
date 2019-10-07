"""crowd_labeling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView

from register import views as register_views
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('register/', register_views.register, name='register'),
    path('label/', views.label, name='label'),
    path('', RedirectView.as_view(pattern_name='label', permanent=False)),

    # temporary todo delete for production
    path('complete/', views.complete, name='complete')

]
