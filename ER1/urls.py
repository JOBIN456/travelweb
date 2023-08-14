from django.urls import path
from .import views
urlpatterns = [
    
    path('',views.dm, name="dm"),
    path('login/',views.dm1,name="dm1"),
    path('welcome/',views.dm3,name="dm3"),
    path('logout',views.logout,name="logout")

]
