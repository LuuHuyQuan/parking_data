from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views
from .views import logout_view
urlpatterns = [
    path('', views.home, name ='home'),
    path('register/', views.register, name = 'register'),
    path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name='login'),
    path('logout/', logout_view, name="logout"),
    path('add/', views.add_parkingdata, name = "add"),
    path('show/',views.show_parkingdata, name ="show"),
    path('updateshow/', views.show_update, name="showupdate"),
    path('update/<int:parkingdata_id>/', views.update_parkingdata, name='update'),
    path('delete/<int:parkingdata_id>/', views.delete_product, name='delete'),path('search/', views.search_parking_data, name='search_parking_data'),
]
