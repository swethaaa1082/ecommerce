from django.urls import path
from ecommerce_app import views
# app_name='ecommerce_app'
urlpatterns = [
    path('',views.home,name='home'),
    path('allProdCat',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProdCatDetail, name='ProdCatDetail')
]
