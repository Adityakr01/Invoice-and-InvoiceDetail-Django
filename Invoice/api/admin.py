from django.contrib import admin
from api.models import Invoice, InvoiceDetails

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number','customer_name','date')
    search_fields = ('invoice_number','customer_name')

class InvoiceDetailsAdmin(admin.ModelAdmin):
    list_display = ('description','quantity','line_total','invoice')
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceDetails, InvoiceDetailsAdmin)


# Register your models here.
