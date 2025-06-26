from django import template

register = template.Library()

@register.filter
def get_total(total_dict, key_string):
    return total_dict.get(tuple(key_string.split('|')), 0)
