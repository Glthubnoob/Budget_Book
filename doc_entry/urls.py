from django.urls import path
from . import views


urlpatterns = [
    path('', views.DocumentListView.as_view(), name='home'),
    # path('<int:doc_id>/', views.doc_create, name='doc_create'),
    path('<int:doc_id>/', views.index, name='index'),
    path('document/create/', views.DocumentCreateView.as_view(), name='document_create'),
    path('location/create/', views.LocationCreateView.as_view(), name='location_create'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('unit/create/', views.UnitCreateView.as_view(), name='unit_create'),
    
]
