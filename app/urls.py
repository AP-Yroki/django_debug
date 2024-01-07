from .views import GetPosts, GetDetailView, CreatePost, UpdatePost, DeletePost, \
    AddToCart, GetOrders, DeleteOrder

from django.urls import path



urlpatterns = [
    path('', GetPosts.as_view(), name='home'),
    path('detail/<int:pk>', GetDetailView.as_view(), name='detail'),
    path('create/', CreatePost.as_view(), name='create'),
    path('update/<int:pk>/', UpdatePost.as_view(), name='update'),
    path('add_to_cart/<int:product_id>/', AddToCart.as_view(), name='add_to_cart'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='delete'),
    path('orders/', GetOrders.as_view(), name='orders'),
    path('delete_order/<int:pk>/', DeleteOrder.as_view(), name='delete_order'),
]

