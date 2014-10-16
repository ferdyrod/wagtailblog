from django import template

from blog.models import Anuncio

register = template.Library()

# Advert snippets
@register.inclusion_tag('blog/anuncios.html', takes_context=True)
def anuncios(context):
    return {
        'anuncios': Anuncio.objects.all(),
        'request': context['request'],
    }