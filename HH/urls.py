"""HH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path

from label_ListPage.views import dashBourd, ticketDetail, FormTicketCreate, FormTicketDelete, FormTicketUpdate
from login.views import Login, Logout

urlpatterns = [
    re_path(r'^logout/', Logout.as_view(), name="logout"),
    path('dasboard/', dashBourd.as_view(), name="dashBourdPage"),
    re_path(r'^dasboard/(?P<pk>\d+)/', ticketDetail.as_view(), name='ticketDetail'),
    re_path(r'^formticket/add/$', FormTicketCreate.as_view(), name='ticketForm_create'),
    re_path(r'formticket/(?P<pk>\d+)/$', FormTicketUpdate.as_view(), name='ticketForm_update'),
    re_path(r'formticket/(?P<pk>\d+)/delete/$', FormTicketDelete.as_view(), name='ticketForm_delete'),

    path('', Login.as_view(), name="login"),
    re_path(r'^admin/', admin.site.urls, name="admin"),
]
