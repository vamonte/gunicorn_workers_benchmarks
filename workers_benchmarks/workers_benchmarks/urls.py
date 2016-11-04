"""workers_benchmarks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from test_views.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^simple_json', simple_json),
    url(r'^simple_request/(?P<n>\w+)', simple_requests),
    url(r'^create_data/(?P<n>\w+)', create_data),
    url(r'^create_data_in_redis/(?P<n>\w+)', create_data_in_redis),
    url(r'^read_data_in_redis/(?P<k>\w+)', read_data_in_redis),
    url(r'^request_and_read_redis', request_and_read_redis),
    url(r'^request_and_read_redis', request_and_read_redis),
    url(r'^create_data_and_read_redis', create_data_and_read_redis),
    url(r'^read_redis_and_create_data', read_redis_and_create_data),
    url(r'^read_data', read_data)
]
