{%- if cookiecutter.command_line_interface|lower == 'y' %}
{%- if cookiecutter.support_python2 != "n" %}
# coding: utf-8
{%- endif %}
"""Command line interface"""
{%- if cookiecutter.support_python2 != "n" %}
from __future__ import absolute_import, division, print_function, unicode_literals
{%- endif %}

import argparse


def main():
    """CLI entrypoint"""
    psr = argparse.ArgumentParser()
    args = psr.parse_args()
    #
    print(args)

{%- endif %}
