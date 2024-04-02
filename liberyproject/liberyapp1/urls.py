from django.contrib import admin
from django.urls import path, include

from liberyapp import views
app_name="liberyapp"

urlpatterns = [

    path('',views.home,name='home'),
    path('add/',views.add,name="add"),
    path('view/',views.view,name="view"),
    path('detail/<int:n>/',views.detail,name='detail'),
    path('delete/<int:n>/', views.delete, name='delete'),
    path('edit/<int:n>/',views.edit,name='edit'),

]