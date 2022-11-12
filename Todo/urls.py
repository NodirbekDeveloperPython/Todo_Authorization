"""Todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from plan.views import *
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('plans/', AllPlanAPIView.as_view()),
    path('plan/<int:pk>/', PlanAPIView.as_view()),
    path('get_token/', obtain_auth_token, name='api_token_auth'),
]
    # path('get_token/',TokenObtainPairView.as_view()),
    # path('token_refresh/',TokenRefreshView.as_view()),
