from django.db import models

class Customer(models.Model):
    customer_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()

class Product(models.Model):
    product_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    unit_price = models.FloatField()
    discount = models.FloatField()

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    total_amount = models.FloatField()
    shipping_cost = models.FloatField()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    unit_price = models.FloatField()
    discount = models.FloatField()
    total_amount = models.FloatField()
