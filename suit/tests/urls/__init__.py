import django
from django.contrib import admin
from django.conf.urls import include

admin.autodiscover()

try:
    # Django 2.0+
    from django.urls import re_path

    urlpatterns = [
        re_path(r'^admin/', admin.site.urls),
    ]
except ImportError:
    try:
        from django.conf.urls import patterns, url
        urlpatterns = patterns(
            '',
            # Examples for custom menu
            url('admin/', include(admin.site.urls)),
        )
    except ImportError:  # Django 1.10+
        from django.conf.urls import url
        urlpatterns = [
            url('admin/', include(admin.site.urls)),
        ]
