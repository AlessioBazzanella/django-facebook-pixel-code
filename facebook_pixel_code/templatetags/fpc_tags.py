from django.template import Library
from django.conf import settings

register = Library()

@register.inclusion_tag("fpc/fpc.html")
def fpc(facebook_pixel_code_tag_id=None):
    if facebook_pixel_code_tag_id is None:
        facebook_pixel_code_tag_id = getattr(settings, 'FACEBOOK_PIXEL_CODE_ID', None)
    return {
        'facebook_pixel_code_tag_id': facebook_pixel_code_tag_id
    }
