from django.conf.urls import include, url
import whatsgoingon.views

urlpatterns = [

    url('^', include('django.contrib.auth.urls')),
    url(r'^$', whatsgoingon.views.main, name='main'),


]