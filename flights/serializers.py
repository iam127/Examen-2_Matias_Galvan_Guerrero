from rest_framework import serializers
from .models import Airline, Flight


class AirlineSerializer(serializers.ModelSerializer):
    """Serializer para Aerolíneas"""
    flights_count = serializers.IntegerField(source='flights.count', read_only=True)
    
    class Meta:
        model = Airline
        fields = ['id', 'name', 'country', 'flights_count', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class AirlineDetailSerializer(serializers.ModelSerializer):
    """Serializer detallado para Aerolíneas con sus vuelos"""
    flights = serializers.SerializerMethodField()
    
    class Meta:
        model = Airline
        fields = ['id', 'name', 'country', 'flights', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    
    def get_flights(self, obj):
        flights = obj.flights.all()
        return FlightSimpleSerializer(flights, many=True).data


class FlightSimpleSerializer(serializers.ModelSerializer):
    """Serializer simple para Vuelos (sin datos anidados)"""
    class Meta:
        model = Flight
        fields = ['id', 'flight_code', 'origin', 'destination']


class FlightSerializer(serializers.ModelSerializer):
    """Serializer para Vuelos con información de aerolínea"""
    airline_name = serializers.CharField(source='airline.name', read_only=True)
    airline_country = serializers.CharField(source='airline.country', read_only=True)
    
    class Meta:
        model = Flight
        fields = [
            'id', 'flight_code', 'origin', 'destination', 
            'airline', 'airline_name', 'airline_country',
            'departure_time', 'arrival_time', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
    
    def validate_flight_code(self, value):
        """Validar que el código de vuelo esté en mayúsculas"""
        return value.upper()