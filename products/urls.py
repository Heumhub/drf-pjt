from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "products"
urlpatterns = [
    path('', views.ProductsListAPIView.as_view()),
    path('<int:productId>/', views.ProductDetailAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)