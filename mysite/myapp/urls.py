
from os import name
from django.urls import  path

from myapp import views
app_name='myapp'
urlpatterns = [
    path('',views.index),
    path('contact/', views.contact),
    path('show_product/<int:prod_id>',views.show_product, name='show_product' )
]