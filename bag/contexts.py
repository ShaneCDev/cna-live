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
    product_discounts = {}

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            discount_applied = False
            print(discount_applied)
            total += item_data * product.price
            product_count += item_data

            discount = 0

            match product.category.name:
                case 'hhc-carts':
                    if item_data == 4:
                        discount_applied = True
                        discount = 19.97
                    elif item_data == 10:
                        product.discount_applied = True
                        discount = 100
                    elif item_data == 25:
                        product.discount_applied = True
                        discount = 299.97
                    elif item_data == 50:
                        product.discount_applied = True
                        discount = 699.51
                case 'hhc-disposables':
                    if item_data == 4:
                        product.discount_applied = True
                        discount = 40
                    elif item_data == 10:
                        product.discount_applied = True
                        discount = 150
                    elif item_data == 25:
                        product.discount_applied = True
                        discount = 450
                    elif item_data == 50:
                        product.discount_applied = True
                        discount = 950
                case 'concentrates-shatter':
                    if item_data == 4:
                        product.discount_applied = True
                        discount = 40
                    elif item_data == 10:
                        product.discount_applied = True
                        discount = 150
                    elif item_data == 25:
                        product.discount_applied = True
                        discount = 450
                    elif item_data == 50:
                        product.discount_applied = True
                        discount = 950
                case 'concentrates-distillate':
                    if item_data == 5:
                        product.discount_applied = True
                        discount = 50
                    elif item_data == 10:
                        product.discount_applied = True
                        discount = 250
                    elif item_data == 25:
                        product.discount_applied = True
                        discount = 1100
                    elif item_data == 50:
                        product.discount_applied = True
                        discount = 2500
                    elif item_data == 1000:
                        product.discount_applied = True
                        discount_amount = 5500
                case 'hhc-o-carts':
                    if item_data == 5:
                        product.discount_applied = True
                        discount = 25
                    elif item_data == 10:
                        product.discount_applied = True
                        discount = 70
                case 'hhc-o-disposables':
                    if item_data == 5:
                        product.discount_applied = True
                        discount = 55
                    elif item_data == 10:
                        product.discount_applied = True
                        discount = 130

            discount_amount += discount

            product_discounts[product.slug] = discount_applied
            
            print('Product discounts dictionary:', product_discounts)

            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

    if bag.items():
        delivery = 5
    else:
        delivery = 0

    #print(product.discount_applied)

    if product and discount_applied:
        dec_discount_amount = Decimal(discount_amount)
        grand_total = (delivery + total) - dec_discount_amount
        discounted_price = total - dec_discount_amount
        print('discounted price:', discounted_price)
        print('discount applied:', product_discounts[product.slug])
        print('dictionary:', product_discounts)

        context = {
            'bag_items': bag_items,
            'total': total,
            'product_count': product_count,
            'delivery': delivery,
            'grand_total': grand_total,
            'discount_applied': product_discounts,
            'discounted_price': discounted_price,
            'total_after_discount': total_after_discount,
            'discount_amount': dec_discount_amount,
        }
        print(context)
    else:
        grand_total = delivery + total
        print('Grand total before delivery charge:', grand_total)
        context = {
            'bag_items': bag_items,
            'total': total,
            'product_count': product_count,
            'delivery': delivery,
            'grand_total': grand_total,
        }

    return context
