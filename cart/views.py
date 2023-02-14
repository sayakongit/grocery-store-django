from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
# Create your views here.
class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user, order=False).first()
        queryset = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        user = request.user
        cart,_ = Cart.objects.get_or_create(user=user, order=False)
        product = Product.objects.get(id = data.get('product'))
        price = product.price
        quantity = data.get('quantity')
        
        print(cart)
        cart_item = CartItem(cart=cart, user=user, product=product, price=price, quantity=quantity)
        cart_item.save()
        
        return Response({'message': 'item added to cart'})
    
    def delete(self, request):
        user = request.user
        data = request.data
        
        cart_item = CartItem.objects.get(id = data.get('id'))
        cart_item.delete()
        #TODO: Update cart total_price after deletion
        cart = Cart.objects.filter(user=user, order=False).first()
        queryset = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
    def put(self, request):
        data = request.data
        cart_item = CartItem.objects.get(id = data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)
    

