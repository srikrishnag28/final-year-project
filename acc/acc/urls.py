"""acc URL Configuration

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
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def viewcriteria(request):
    return render(request, 'criteriapage.html')


@login_required
def viewcriteria1(request):
    return render(request, 'criteria1.html')


@login_required
def viewcriteria2(request):
    return render(request, 'criteria2.html')


@login_required
def viewcriteria3(request):
    return render(request, 'criteria3.html')


@login_required
def viewcriteria4(request):
    return render(request, 'criteria4.html')


@login_required
def viewcriteria5(request):
    return render(request, 'criteria5.html')


@login_required
def viewcriteria6(request):
    return render(request, 'criteria6.html')


@login_required
def viewcriteria7(request):
    return render(request, 'criteria7.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('c1/', include('criteria_1.urls')),
    path('c2/', include('criteria_2.urls')),
    path('c3/', include('criteria_3.urls')),
    path('c4/', include('criteria_4.urls')),
    path('c5/', include('criteria_5.urls')),
    path('c6/', include('criteria_6.urls')),
    path('c7/', include('criteria_7.urls')),
    path('user/', include('user.urls')),

    path('viewcriteria/', viewcriteria, name='viewcriteria'),
    path('viewcriteria1/', viewcriteria1, name='viewcriteria1'),
    path('viewcriteria2/', viewcriteria2, name='viewcriteria2'),
    path('viewcriteria3/', viewcriteria3, name='viewcriteria3'),
    path('viewcriteria4/', viewcriteria4, name='viewcriteria4'),
    path('viewcriteria5/', viewcriteria5, name='viewcriteria5'),
    path('viewcriteria6/', viewcriteria6, name='viewcriteria6'),
    path('viewcriteria7/', viewcriteria7, name='viewcriteria7'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)