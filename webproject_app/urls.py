"""Main_app url configuration"""

from django.urls import path

from webproject_app import views


urlpatterns = [

    path('',views.home, name='Home'),
    path('services/',views.services, name='Services'),
    path('store/',views.store, name='Store'),
    path('blogs/',views.blogs, name='Blogs'),
    path('contact/',views.contact, name='Contact'),
]