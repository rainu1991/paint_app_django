from django.conf.urls import patterns, include, url
from views import mainPage,loadPage,d1
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',('^$',mainPage),(r'^([A-Za-z]+)$',loadPage),('^d1$',d1),
    # Examples:
    # url(r'^$', 'paint.views.home', name='home'),
    # url(r'^paint/', include('paint.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
