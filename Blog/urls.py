"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from post.views import index, about, show_post,add_post, update_post, delete_post, search_post, add_comment, like, add_review
from user.views import user_register,user_login, user_logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('post/show/<int:id>/', show_post, name = 'show_post'),
    path('post/add/', add_post, name = 'add_post'),
    path('post/update/<int:id>/', update_post, name = 'update_post'),
    path('post/delete/<int:id>/', delete_post, name = 'delete_post'),
    path('post/search/', search_post, name='search_post'),
    path('comment/add/<int:id>/', add_comment, name='add_comment'),
    path('review/add/', add_review, name='add_review'),
    path('like/add/<int:id>/', like, name='like'),
    path('user/register/', user_register, name='register'),
    path('user/login/',user_login, name='login'),
    path('user/logout/',user_logout, name='logout'),
]

from Blog import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)