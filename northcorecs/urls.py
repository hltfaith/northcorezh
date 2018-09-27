"""northcorecs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path

from asset import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_server_asset_info),
    path('asset/server_info/', views.get_server_asset_info),
    path('asset/idc/add/', views.idc_asset_manage),
    path('asset/idc/list/', views.idc_asset_list),
    path('asset/excel_upload/', views.excel_upload),
    re_path(r'asset/server_info/(\d+)/delete', views.idc_asset_delete),
    re_path(r'asset/server_info/(\d+)/change', views.idc_asset_change),
]
