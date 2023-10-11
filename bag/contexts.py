from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from checkout.models import Order


def bag_contents(request):
    bag_items = []
    total = 0
    total_after_discount = 0
    product_count = 0
    discount_applied = False
    discount_amount = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

            if item_data >= 4:
                discount_applied = True
                discount_amount = 10
    

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    if discount_applied:
        # total_after_discount = total - discount_amount
        grand_total = (delivery + total) - discount_amount

        context = {
            'bag_items': bag_items,
            'total': total,
            'product_count': product_count,
            'delivery': delivery,
            'grand_total': grand_total,
            'discount_applied': discount_applied,
            'total_after_discount': total_after_discount,
            'discount_amount': discount_amount,
        }
    else:
        grand_total = delivery + total
        context = {
            'bag_items': bag_items,
            'total': total,
            'product_count': product_count,
            'delivery': delivery,
            'grand_total': grand_total,
        }

    print(context)

    return context
