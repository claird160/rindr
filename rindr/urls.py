"""rindr URL Configuration

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
from django.urls import path,include
from ticket import views as ticket_views
from type import views as type_views
urlpatterns = [
    path('login/',ticket_views.login),
    path('login/action',ticket_views.login_action),
    path('new',ticket_views.new),
    path('new/create',ticket_views.new_action),
    path('type/new',type_views.new),
    path('type/new/create',type_views.new_action),
    path('type/<int:type>',type_views.type),    
    path('type/export/tickets_type-<int:type>.json',type_views.type_export),
    path('type/export/all_types.json',type_views.type_export_all),
    path('table',ticket_views.table),
    path('',ticket_views.home),
    path('ticket/<int:ticket>',ticket_views.ticket),
    path('ticket/export/ticket_<int:ticket>.json',ticket_views.ticket_export),
    path('ticket/export/all_tickets.json',ticket_views.ticket_export_all),
    path('type',type_views.table),
    path('chart/type/top',type_views.type_chart_data),
    path('chart/ticket/times',ticket_views.ticket_response_chart_data),
    path('admin/', admin.site.urls)
]

