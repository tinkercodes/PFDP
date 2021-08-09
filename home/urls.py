from django.urls import path

from django.views.static import serve
from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about_us'),
    path('demo/', views.demo, name='Try_it_yourself'),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
    # path('vrnForm/', views.vrnForm, name='vrnForm'),
    # path('vrnformsubmit/', views.vrnform_submit, name='vrnform_submit'),
    # # path('challanDetail/', views.challanDetail, name='challandetail'),
]
