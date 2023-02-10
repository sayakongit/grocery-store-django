from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ProductView(APIView):
    def get(self, request):
        query_set = Product.objects.all()
        serializer = ProductSerializer(query_set, many = True)
        return Response(serializer.data)
    
class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)