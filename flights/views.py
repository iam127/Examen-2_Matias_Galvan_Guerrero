from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Airline, Flight
from .serializers import (
    AirlineSerializer, 
    AirlineDetailSerializer,
    FlightSerializer
)


class AirlineViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD de Aerolíneas
    
    Endpoints:
    - GET /api/airlines/ - Listar todas las aerolíneas
    - POST /api/airlines/ - Crear nueva aerolínea
    - GET /api/airlines/{id}/ - Detalle de aerolínea
    - PUT /api/airlines/{id}/ - Actualizar aerolínea
    - PATCH /api/airlines/{id}/ - Actualizar parcialmente
    - DELETE /api/airlines/{id}/ - Eliminar aerolínea
    """
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'country']
    ordering_fields = ['name', 'country', 'created_at']
    
    def get_serializer_class(self):
        """Usar serializer detallado para retrieve"""
        if self.action == 'retrieve':
            return AirlineDetailSerializer
        return AirlineSerializer


class FlightViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD de Vuelos
    
    Endpoints:
    - GET /api/flights/ - Listar todos los vuelos
    - POST /api/flights/ - Crear nuevo vuelo
    - GET /api/flights/{id}/ - Detalle de vuelo
    - PUT /api/flights/{id}/ - Actualizar vuelo
    - PATCH /api/flights/{id}/ - Actualizar parcialmente
    - DELETE /api/flights/{id}/ - Eliminar vuelo
    - GET /api/flights/?search=lima - Búsqueda
    """
    queryset = Flight.objects.select_related('airline').all()
    serializer_class = FlightSerializer
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]
    filterset_fields = ['airline', 'origin', 'destination']
    search_fields = ['flight_code', 'origin', 'destination', 'airline__name']
    ordering_fields = ['flight_code', 'origin', 'destination', 'created_at']
    
    @action(detail=False, methods=['get'])
    def by_airline(self, request):
        """Endpoint personalizado: filtrar vuelos por aerolínea"""
        airline_id = request.query_params.get('airline_id')
        if airline_id:
            flights = self.queryset.filter(airline_id=airline_id)
            serializer = self.get_serializer(flights, many=True)
            return Response(serializer.data)
        return Response({'error': 'airline_id parameter is required'}, status=400)