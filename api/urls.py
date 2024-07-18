from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductList.as_view(),name='index'),
    path('create',views.ProductCreate.as_view(),name='create'),
    path('update/<int:pk>/',views.ProductUpdate.as_view(),name='update'),
    path('delete/<int:pk>/',views.ProductDelete.as_view(),name='delete'),
    path('listcreate/',views.ProductListCreate.as_view(),name='listcreate'),
    path('crud/<int:pk>/',views.ProductCrud.as_view(),name='crud'),
]