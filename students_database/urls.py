"""students_database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from students import views as students_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', students_views.students_list, name='students'),
    path('students/add', students_views.students_add, name='students-add'),
    path(r'^students/(?P<sid>\d+)/edit$', students_views.students_edit, name='students-edit'),
    path(r'^students/(?P<sid>\d+)/delete$', students_views.students_delete, name='students-delete'),
    path('visiting/', students_views.visiting_list, name='visiting'),
    path('classes/', students_views.classes_list, name='classes'),
    path('classes/add', students_views.classes_add, name='classes-add'),
    path(r'^classes/(?P<gid>\d+)/edit$', students_views.classes_edit, name='classes-edit'),
    path(r'^classes/(?P<gid>\d+)/delete$', students_views.classes_delete, name='classes-delete'),
]
