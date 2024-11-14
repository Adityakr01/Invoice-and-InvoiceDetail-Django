from django.shortcuts import render
from rest_framework import viewsets
from api.models import Invoice, InvoiceDetails
from api.serializers import InvoiceSerializer, InvoiceDetailsSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    
    
    
class InvoiceDetailsViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetails.objects.all()
    serializer_class = InvoiceDetailsSerializer