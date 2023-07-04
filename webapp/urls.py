from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'webapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('reg',views.CustomUserView,name='reg'),
    path('login',views.LoginView,name='login'),
    path('fac/<int:id>',views.Faculty_dashView,name='fac'),
    path('student/<int:id>',views.Student_dashView,name='student'),
    path('logout',views.LogoutView,name='logout'),
    path('student/<int:id>/app',views.ApplicationView,name='app'),
    path('fac/<int:id>/update/<int:app_id>',views.UpdateView,name='update'),
    path('fac/<int:id>/update/change/<int:app_id>',views.ChangeStatus,name='change'),
]