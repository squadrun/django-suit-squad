from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = i18n_patterns('',
    # Examples for custom menu
    path('admin/', include(admin.site.urls)),
)
