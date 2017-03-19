from rest_framework import serializers
from .models import User, Booking, Bus, Route

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'user_name', 'email', 'phone_number', 'password_hash')

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('id', 'user_id', 'destination_id')


class BusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bus
        fields = ('id', 'bus_model', 'passenger_seats', 'name')


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = ('id', 'd_from', 'd_to', 'bus_id')