from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Order, Product, OrderItem
from .serializers import OrderSerializer, ProductSerializer
from datetime import datetime
from django.db import models

@api_view(['POST'])
def trigger_data_refresh(request):
    from .tasks import refresh_data
    refresh_data()
    return Response({"message": "Data refresh triggered successfully"})

@api_view(['GET'])
def get_revenue(request):
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

    total_revenue = Order.objects.filter(order_date__range=[start_date, end_date]).aggregate(
        total_revenue=models.Sum('total_amount'))['total_revenue']

    if total_revenue is None:
        total_revenue = 0.0

    return Response({"total_revenue": total_revenue})

@api_view(['GET'])
def get_top_products(request):
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

    top_products = OrderItem.objects.filter(
        order__order_date__range=[start_date, end_date]
    ).values('product__product_id').annotate(
        total_sold=Sum('quantity_sold')
    ).order_by('-total_sold')

    product_data = [
        {
            "product_id": item['product__product_id'],
            "total_sold": item['total_sold']
        }
        for item in top_products
    ]

    return Response({"top_products": product_data})
