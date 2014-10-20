#!/usr/bin/python3
import jinja2
from collections import OrderedDict


class ConfigObject():
    '''
    Represents a Shinken configuration object.
    '''
    TEMPLATE = jinja2.Template('''define {{ o.type }} {
{% for key, value in o.properties.items() -%}
    {{ key }}        {{ value }}
{% endfor -%}
}''')

    def __init__(self, type):
        self.type = type
        self.properties = OrderedDict()

    def __str__(self):
        '''
        Print a representation of this object in shinken config format
        '''
        return ConfigObject.TEMPLATE.render(o=self)
