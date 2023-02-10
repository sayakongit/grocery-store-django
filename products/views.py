from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class ProductView(APIView):
    def get(self, request):
        query_set = Product.objects.all()
        serializer = ProductSerializer(query_set, many = True)
        return Response(serializer.data)