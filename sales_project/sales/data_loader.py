import pandas as pd
from .models import Customer, Product, Order, OrderItem

def load_data():
    try:

        df = pd.read_csv('sample_sales_data.csv', encoding='ISO-8859-1')

        df.columns = df.columns.str.strip()

        if 'Quantity Sold' not in df.columns or 'Unit Price' not in df.columns or 'Discount' not in df.columns:
            print("Error: Necessary columns for calculating 'Total Amount' are missing.")
            return

        if 'Total Amount' not in df.columns:
            df['Total Amount'] = (df['Quantity Sold'] * (df['Unit Price'] - df['Discount'])) + df['Shipping Cost']
            print("Total Amount calculated and added.")

        for _, row in df[['Customer ID', 'Customer Name', 'Customer Email', 'Customer Address']].drop_duplicates().iterrows():
            customer_id = row['Customer ID']
            Customer.objects.get_or_create(
                customer_id=customer_id,
                name=row['Customer Name'],
                email=row['Customer Email'],
                address=row['Customer Address']
            )


        for _, row in df[['Product ID', 'Product Name', 'Category', 'Unit Price', 'Discount']].drop_duplicates().iterrows():
            product_id = row['Product ID']
            product, created = Product.objects.get_or_create(
                product_id=product_id,
                defaults={
                    'name': row['Product Name'],
                    'category': row['Category'],
                    'unit_price': row['Unit Price'],
                    'discount': row['Discount']
                }
            )
            if not created:
                product.name = row['Product Name']
                product.category = row['Category']
                product.unit_price = row['Unit Price']
                product.discount = row['Discount']
                product.save()

        for _, row in df.iterrows():
            customer = Customer.objects.get(customer_id=row['Customer ID'])


            total_amount = row['Total Amount'] if pd.notnull(row['Total Amount']) else 0.0

            order = Order.objects.create(
                order_id=row['Order ID'],
                customer=customer,
                order_date=row['Date of Sale'],
                payment_method=row['Payment Method'],
                payment_status=row.get('Payment Status', 'Unknown'),  # Default value if missing
                total_amount=total_amount,
                shipping_cost=row['Shipping Cost']
            )
            OrderItem.objects.create(
                order=order,
                product=Product.objects.get(product_id=row['Product ID']),
                quantity_sold=row['Quantity Sold'],
                unit_price=row['Unit Price'],
                discount=row['Discount'],
                total_amount=row['Quantity Sold'] * (row['Unit Price'] - row['Discount'])
            )

    except UnicodeDecodeError:
        print("Error: Unable to decode CSV file with specified encoding.")
    except Exception as e:
        print(f"Error occurred: {e}")
