from django import template

register = template.Library()

@register.filter
def is_pdf(file_name):
    return file_name.lower().endswith('.pdf')

@register.filter
def is_image(file_name):
    return file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))

@register.filter
def is_word(file_name):
    return file_name.lower().endswith('.word')