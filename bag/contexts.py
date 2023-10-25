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

            print('Product:', type(product.category.name))
            
            print('Item Data:', item_data)

            all_categories = Category.objects.all()

            print('All Categories:', all_categories)
            print('List of all categories:', list(all_categories))
            # if product.category.name == 'hhc-carts':
            #     if item_data >= 4:
            #         discount_applied = True
            #         discount_amount = 20

            discount = 0

            match product.category.name:
                case 'hhc-carts':
                    if item_data == 4:
                        discount_applied = True
                        discount = 20
                    elif item_data == 10:
                        discount_applied = True
                        discount = 100
                    elif item_data == 25:
                        discount_applied = True
                        discount = 300
                    elif item_data == 50:
                        discount_applied = True
                        discount = 700
                case 'hhc-disposables':
                    if item_data == 4:
                        discount_applied = True
                        discount = 40
                    elif item_data == 10:
                        discount_applied = True
                        discount = 150
                    elif item_data == 25:
                        discount_applied = True
                        discount = 450
                    elif item_data == 50:
                        discount_applied = True
                        discount = 950
                case 'concentrates-shatter':
                    if item_data == 4:
                        discount_applied = True
                        discount = 40
                    elif item_data == 10:
                        discount_applied = True
                        discount = 150
                    elif item_data == 25:
                        discount_applied = True
                        discount = 450
                    elif item_data == 50:
                        discount_applied = True
                        discount = 950
                case 'concentrates-distillate':
                    if item_data == 5:
                        discount_applied = True
                        discount = 50
                    elif item_data == 10:
                        discount_applied = True
                        discount = 250
                    elif item_data == 25:
                        discount_applied = True
                        discount = 1100
                    elif item_data == 50:
                        discount_applied = True
                        discount = 2500
                    elif item_data == 1000:
                        discount_applied = True
                        discount_amount = 5500
                case 'hhc-o-carts':
                    if item_data == 5:
                        discount_applied = True
                        discount = 25
                    elif item_data == 10:
                        discount_applied = True
                        discount = 70
                case 'hhc-o-disposables':
                    if item_data == 5:
                        discount_applied = True
                        discount = 55
                    elif item_data == 10:
                        discount_applied = True
                        discount = 130

            discount_amount += discount
    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    print('Discount applied:', discount_applied)

    if discount_applied:
        print('Bag:', bag)
        print('Bag Items:', bag_items)
        grand_total = (delivery + total) - discount_amount
        #total_after_discount += discount_amount
        print('Grand total before delivery charge inside discount applied statement:', grand_total)
        print('Total After Discount (should be 90):', discount_amount)
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
        print('Grand total before delivery charge:', grand_total)
        context = {
            'bag_items': bag_items,
            'total': total,
            'product_count': product_count,
            'delivery': delivery,
            'grand_total': grand_total,
        }

    return context
