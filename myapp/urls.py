from django.urls import path
from myapp import views
app_name="myapp"
urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('profile/',views.profile,name="profile"),
    path('reset_password/',views.reset_password,name="reset_password"),

]