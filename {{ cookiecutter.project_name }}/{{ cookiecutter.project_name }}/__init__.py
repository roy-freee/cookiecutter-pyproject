{%- if cookiecutter.support_python2 != "n" %}
# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
{% endif %}
from .__version__ import __version__

__all__ = ['__version__']
