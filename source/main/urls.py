"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import index_view, review_create_view, review_view, \
    review_update_view, review_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('review/<int:pk>/', review_view, name='review_view'),
    path('reviews/add/', review_create_view, name='review_create'),
    path('review/<int:pk>/update/', review_update_view, name='review_update'),
    path('review/<int:pk>/delete/', review_delete_view, name='review_delete')
]
