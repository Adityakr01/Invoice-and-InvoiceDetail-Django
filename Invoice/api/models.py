from django.db import models

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    
    def date_field(self):
        return self.date.date()
    
    def __str__(self):
        return self.customer_name
    

    
class InvoiceDetails(models.Model):
    
    id = models.AutoField(primary_key=True)
    description = models.CharField( max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    invoice = models.ForeignKey(Invoice, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.description
    