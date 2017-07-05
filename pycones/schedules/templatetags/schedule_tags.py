from __future__ import unicode_literals

from django import template
import six

register = template.Library()


@register.simple_tag()
def slot_col_size(tracks):
    grid_columns = 12
    return "col-sm-{}".format(int(grid_columns/tracks))


@register.filter()
def comma_list(items):
    return ", ".join(map(lambda s: six.text_type(s), items))
