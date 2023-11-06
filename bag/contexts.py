from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Category
from checkout.models import Order


def bag_contents(request):
    bag_items = []
    total = 0
    total_after_discount = 0
    product_count = 0
    discount_amount = 0
    bag = request.session.get('bag', {})
    product = None

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            discount_applied = False
            total += item_data * product.price
            product_count += item_data

            discount = 0

            match product.category.name:
                case 'hhc-carts':
                    if item_data == 4:
                        discount_applied = True
                        discount = 19.97
                    elif item_data == 10:
                        discount_applied = True
                        discount = 100
                    elif item_data == 25:
                        discount_applied = True
                        discount = 299.97
                    elif item_data == 50:
                        discount_applied = True
                        discount = 699.51
                case 'hhc-disposables':
                    if item_data == 4:
                        discount_applied = True
                        discount = 39.97
                    elif item_data == 10:
                        discount_applied = True
                        discount = 149.91
                    elif item_data == 25:
                        discount_applied = True
                        discount = 449.97
                    elif item_data == 50:
                        discount_applied = True
                        discount = 949.51
                case 'concentrates-shatter':
                    if item_data == 4:
                        discount_applied = True
                        discount = 39.97
                    elif item_data == 10:
                        discount_applied = True
                        discount = 149.91
                    elif item_data == 25:
                        discount_applied = True
                        discount = 449.97
                    elif item_data == 50:
                        discount_applied = True
                        discount = 949.51
                case 'concentrates-distillate':
                    if item_data == 2:
                        discount_applied = True
                        discount = 99.99
                    elif item_data == 4:
                        discount_applied = True
                        discount = 299.97
                    elif item_data == 10:
                        discount_applied = True
                        discount = 1399.91
                    elif item_data == 20:
                        discount_applied = True
                        discount = 2999.81
                    elif item_data == 40:
                        discount_applied = True
                        discount_amount = 6999.61
                case 'hhc-o-carts':
                    if item_data == 5:
                        discount_applied = True
                        discount = 24.96
                    elif item_data == 10:
                        discount_applied = True
                        discount = 69.91
                case 'hhc-o-disposables':
                    if item_data == 5:
                        discount_applied = True
                        discount = 54.96
                    elif item_data == 10:
                        discount_applied = True
                        discount = 129.91

            discount_amount += discount

            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

    if bag.items():
        delivery = 5
    else:
        delivery = 0

    if product and discount_applied:
        dec_discount_amount = Decimal(discount_amount)
        grand_total = (delivery + total) - dec_discount_amount
        discounted_price = total - dec_discount_amount

        context = {
            'bag_items': bag_items,
            'total': total,
            'product_count': product_count,
            'delivery': delivery,
            'grand_total': grand_total,
            'discount_applied': discount_applied,
            'discounted_price': discounted_price,
            'total_after_discount': total_after_discount,
            'discount_amount': dec_discount_amount,
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

    return context
