from django.urls import path
from products.views import *

urlpatterns = [
    path('', home_view, name='home_view'),
    path('sign-up/', sign_up, name="sign_up"),
    path('sign-in/', sign_in, name='sign_in'),
    path('sign-out/', sign_out, name='sign_out'),
    path('product-list/', product_list, name='product_list'),
    path('add-product/', add_product, name="add_product"),
    path('update-product/<str:p_id>/', update_product, name='update_product'),
    path('delete-product/<str:p_id>/', delete_product, name='delete_product'),
]
