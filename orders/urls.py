from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^search/page_provider/(?P<name>.*)', views.page_provider, name='page_provider'),
    url(r'^search/', views.search, name='search'),
    url(r'^$', views.home, name='home'),

]