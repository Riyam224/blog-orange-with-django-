from django.urls import path
from . import views 



app_name = 'home'


urlpatterns = [
    path("contact_us/", views.contact_us, name="contact_us"),
    path("about_us/", views.about_us , name="about_us"),
    path('' , views.index , name='index'),
    path('<slug:slug>/' , views.post_detail , name='post_detail'),
]
