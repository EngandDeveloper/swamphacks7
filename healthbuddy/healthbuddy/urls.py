"""healthbuddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import include, path
from farms.views import index, loginPage, registerPage, loginUser , registerUser, logoutUser

urlpatterns = [
    path('', index, name='index'),
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('loginUser/', loginUser, name='loginUser'),
    path('logoutUser/', logoutUser, name='logoutUser'),
    path('registerUser/', registerUser, name='registerUser'),
    path('farms/', include('farms.urls')),
    path('admin/', admin.site.urls),
]
