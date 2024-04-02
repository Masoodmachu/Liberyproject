
from django.urls import path, include

from student import views
app_name="student"

urlpatterns = [

    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    # path('login/',views.user_login,name='login'),
    path('details/',views.details,name='details'),
    path('add/',views.add,name="add"),
    path('teacher/',views.teacher,name='teacher'),
    path('viewteacher',views.viewteacher,name='viewteacher'),
    path('tdetail/<int:n>/',views.tdetail,name='tdetail'),
    path('deleteteacher/<int:n>/',views.deleteteacher,name='delete'),
    path('editteacher/<int:n>/',views.editteacher,name='editteacher'),
    path("logout/",views.userlogout,name='logout'),
    # path('logout/',views.logout,name='logout'),



]