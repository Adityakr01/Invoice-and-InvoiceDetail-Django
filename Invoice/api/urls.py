from django.contrib import admin
from django.urls import path, include
from api.views import InvoiceViewSet, InvoiceDetailsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'InvoiceDetails', InvoiceDetailsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
