"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.http import request
from django.urls import path
from django.urls.conf import include
from portfolioapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('who/',views.who, name="who"),
    path('hobby/',views.hobby, name="hobby"),
    path('place/',views.place, name="place"),
    path('music/',views.music, name="music"),
    path('photo/',views.photo, name="photo"),
    path('visit/',views.visit, name="visit"),
    path('<str:id>',views.visit_detail, name="visit_detail"),
    path('new/',views.new, name="new"),
    path('create/',views.create, name="create"),
    path('edit/<str:id>',views.edit, name="edit"),
    path('update/<str:id>',views.update, name="update"),
    path('delete/<str:id>',views.delete, name="delete"),
    path('accounts/',include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)