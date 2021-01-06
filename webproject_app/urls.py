"""Webproject_app url configuration"""

from django.urls import path

from webproject_app import views


urlpatterns = [

    path('',views.home, name='Home'),
    path('store/',views.store, name='Store'),
    path('blogs/',views.blogs, name='Blogs'),
    path('contact/',views.contact, name='Contact'),
]