from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def calc_total(cart_items):
    total = sum(item.quantity * item.book.price for item in cart_items)
    return round(total, 2)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

