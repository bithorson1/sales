from rest_framework import serializers
from .models import Order, OrderItem, Product, Customer

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'customer', 'order_date', 'payment_method', 'payment_status', 'total_amount', 'shipping_cost']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity_sold', 'unit_price', 'discount', 'total_amount']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'category', 'unit_price', 'discount']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'name', 'email', 'address']
