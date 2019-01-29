from django.urls import path
from .views import *

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('add/', employee_add, name='employee_add'),
    path('<int:id>/edit/', employee_edit, name='employee_edit'),
    path('<int:id>/delete/', employee_delete, name='employee_delete'),
    path('<int:id>/details/', employee_details, name='employee_details'),
    path('login/', user_login, name="user_login"),
    path('success/', user_success, name="user_success"),
    path('logout/', user_logout, name="user_logout"),
    path('profile/', MyProfile.as_view(), name="my_profile"),
    path('profile/update', ProfileUpdate.as_view(), name="update_profile"),
]