from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status

# MenuItem API — public
class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.AllowAny]  # anyone can view

# Booking API — secure
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]  # only authenticated users

    # Assign the logged-in user automatically when creating a booking
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# User registration API
class RegisterViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # anyone can register

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'username': user.username, 'token': token.key}, status=status.HTTP_201_CREATED)
