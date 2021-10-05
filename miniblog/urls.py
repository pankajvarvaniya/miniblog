from django.contrib import admin
from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.home),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('dashbord/',views.dashbord,name='dashbord'),
    path('signup/',views.user_signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('signup/login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('image/',views.image,name='image'),
    path('image/delete/<int:id>',views.delete_image,name='delete'),
    path('logout/home',views.home),
    path('addpost/',views.add_post,name='addpost'),
    path('updatepost/<int:id>',views.update_post,name='updatepost'),
    path('deletepost/<int:id>',views.delete_post,name='deletepost'),


]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
