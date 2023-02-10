from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import IntegrityError

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        
        try:
            user = User(username=username)
            user.set_password(password)
            user.save()
        except IntegrityError as e:
            return Response({'status': 'username already exists'})
        refresh = RefreshToken.for_user(user)
        
        response = {
            'status': 'user registered successfully',
            'user_id': user.id,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return Response(response)
        
