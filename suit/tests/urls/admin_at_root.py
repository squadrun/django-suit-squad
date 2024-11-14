from django.urls import include, re_path
from django.conf.urls import patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples for custom menu
    re_path('', include(admin.site.urls)),
)
