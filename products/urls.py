from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "products"
urlpatterns = [
    path('', views.ProductAPIView.as_view(), name='product'),
    path('<int:productId>/', views.ProductDetailAPIView.as_view(), name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)