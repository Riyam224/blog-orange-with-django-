from django.urls import path 
from . import views 



app_name = 'product'

urlpatterns = [
    path("", views.product, name="product"),
    path('category=<slug:category>/'  , views.product_by_category , name='product_by_category'),

]