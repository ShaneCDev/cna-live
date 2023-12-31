from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('edit/<slug:slug>/<int:product_id>/', views.edit_product, name='edit_product'),
    path('add/', views.add_product, name='add_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('add-category/', views.add_category, name='add_category'),
    path('edit-category/<int:id>', views.edit_category, name='edit_category'),
    path('delete-category/<int:id>/', views.delete_category, name='delete_category'),
]
