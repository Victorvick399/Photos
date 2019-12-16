from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.home_page,name='home'),
    url(r'^about/$',views.about_page,name='about'),
    url(r'^search/', views.search_results, name='search_results')
    ]