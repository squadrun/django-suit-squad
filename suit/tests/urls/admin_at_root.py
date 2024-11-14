from django.urls import include, path
from django.conf.urls import patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples for custom menu
    path('', include(admin.site.urls)),
)
