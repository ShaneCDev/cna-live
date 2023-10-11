from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

# @register.filter(name='apply_discount')
# def apply_discount(price, quantity, discount_amount):
#     return (price * quantity) - discount_amount
