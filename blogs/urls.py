"""Blogs url configuration"""

from django.urls import path

from blogs import views


urlpatterns = [
    
    path('',views.blogs, name='blogs'),
    path('category/<int:category_id>',views.category, name='category'),
   
]
