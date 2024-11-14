from rest_framework import serializers
from api.models import Invoice, InvoiceDetails

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    
    id=serializers.ReadOnlyField()
    class Meta:
        model=Invoice
        fields="__all__"
    def create(self, validated_data):
        details_data = validated_data.pop('details')
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in details_data:
            InvoiceDetails.objects.create(invoice=invoice, **detail_data)
        return invoice 


    def update(self, instance, validated_data):

        details_data = validated_data.pop('details')
        instance.invoice_number = validated_data.get('invoice_number', instance.invoice_number)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        # Update existing details and create new ones
        existing_details = instance.details.all()
        existing_ids = [detail.id for detail in existing_details]
        for detail_data in details_data:
            if 'id' in detail_data:
                detail_id = detail_data.pop('id')
                if detail_id in existing_ids:
                    detail = existing_details.get(id=detail_id)
                    for key, value in detail_data.items():
                        setattr(detail, key, value)
                    detail.save()
                    existing_ids.remove(detail_id)
            else:
                InvoiceDetails.objects.create(invoice=instance, **detail_data)

        # Delete remaining existing details
        for detail_id in existing_ids:
            InvoiceDetails.objects.get(id=detail_id).delete()

        return instance
        
        
class InvoiceDetailsSerializer(serializers.HyperlinkedModelSerializer):
    
    id=serializers.ReadOnlyField()    
    class Meta:
        model=InvoiceDetails
        fields="__all__"
        
    def create(self, validated_data):

        validated_data['line_total'] = validated_data['quantity'] * validated_data['price']
        return super().create(validated_data)
    
    
    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.price = validated_data.get('price', instance.price)

        instance.line_total = instance.quantity * instance.price
        instance.save()
        return instance
