from django.shortcuts import render
from django.http import  JsonResponse, HttpResponse
from django.core import  serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class DefultPagination(PageNumberPagination):
    page_size = 10


class ProductsListAPIView(APIView):
    def get(self, request):
        product = Product.objects.all()
        paginator = DefultPagination()
        paginated_product = paginator.paginate_queryset(product, request)
        serializer = ProductSerializer(paginated_product, many=True)
        return paginator.get_paginated_response(serializer.data)



    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get_object(self, productId):
        return get_object_or_404(Product, pk=productId)

    def get(self, request, productId):
        product = self.get_object(productId)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, productId):
        product = self.get_object(productId)
        if product.author != request.user:
            data = {"error": "본인만 수정 가능합니다"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



    def delete(self, request, productId):
        product = self.get_object(productId)
        if product.author != request.user:
            data = {"error": "본인만 삭제 가능합니다"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        product.delete()
        data = {"delete": f"Comment({productId}) is deleted."}
        return Response(data, status=status.HTTP_200_OK)
