from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MenuItem, Booking

# MenuItem serializer
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']

# Booking serializer
class BookingSerializer(serializers.ModelSerializer):
    # Show the username of the user instead of the ID
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Booking
        fields = ['id','user','booking_date','booking_time','party_size','created_at']

# User serializer (for registration)
class UserSerializer(serializers.ModelSerializer):
    # Make password write-only
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id','username','password','email']

    # Overwrite create to hash password
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
