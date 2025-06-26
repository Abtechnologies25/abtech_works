from django import template

register = template.Library()

@register.simple_tag
def monthly_total(monthly_totals, branch, year, month):
    return monthly_totals.get((branch, int(year), month), 0)
