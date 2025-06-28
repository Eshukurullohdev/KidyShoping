from django.urls import path
from . import views

app_name = 'controlpanel'  # namespacing

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.product_add, name='product_add'),
    path('edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('users/', views.user_list_view, name='user_list'),
    path('profile/', views.admin_profile_view, name='admin_profile'),
]