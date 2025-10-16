from rest_framework.test import APITestCase
from rest_framework import status
from .models import Airline, Flight


class AirlineAPITestCase(APITestCase):
    def setUp(self):
        self.airline = Airline.objects.create(
            name="LATAM Airlines",
            country="Chile"
        )
    
    def test_list_airlines(self):
        response = self.client.get('/api/airlines/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_airline(self):
        data = {'name': 'Avianca', 'country': 'Colombia'}
        response = self.client.post('/api/airlines/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class FlightAPITestCase(APITestCase):
    def setUp(self):
        self.airline = Airline.objects.create(
            name="LATAM Airlines",
            country="Chile"
        )
        self.flight = Flight.objects.create(
            flight_code="LA2479",
            origin="Lima",
            destination="Santiago",
            airline=self.airline
        )
    
    def test_list_flights(self):
        response = self.client.get('/api/flights/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_search_flights(self):
        response = self.client.get('/api/flights/?search=Lima')
        self.assertEqual(response.status_code, status.HTTP_200_OK)