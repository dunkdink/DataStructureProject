"""DataStructProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from classRoomCheck import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.information,name='UserContact'),
    path('classStatus/',views.allStudentName,name='ClassStatus'),
    path('dataStructlogin/',views.dataStructlogin,name='DataStructMember'),
    path('comNetlogin/',views.comNetlogin,name='ComnetMember'),
    path('comOrglogin/',views.comOrglogin,name='ComOrgMember'),
    path('epplogin/',views.ePPlogin,name='EppMember'),
    path('problogin/',views.problogin,name='Probmember'),
    path('dataStructlogin/addIDNameDatastruct',views.dataStructloginAddIDandName),
    path('dataStructlogin/dataStructlogout',views.dataStructlogout),
    path('dataStructlogin/registerIDdata',views.registerIDdata),
    path('comNetlogin/addIDNameComNet',views.comNetloginAddIDandName),
    path('comNetlogin/comNetlogout',views.comNetlogout),
    path('comNetlogin/registerIDcomNet',views.registerIDcomNet),
    path('comOrglogin/addIDNameComOrg',views.comOrgloginAddIDandName),
    path('comOrglogin/comOrglogout',views.comOrglogout),
    path('comOrglogin/registerIDcomOrg',views.registerIDcomOrg),
    path('epplogin/addIDNameEpp',views.ePPloginAddIDandName),
    path('epplogin/ePPlogout',views.ePPlogout),
    path('epplogin/registerIDePP',views.registerIDePP),
    path('problogin/addIDNameProb',views.probloginAddIDandName),
    path('problogin/problogout',views.problogout),
    path('problogin/registerIDprob',views.registerIDprob),
    path('', views.helloUser)
]

