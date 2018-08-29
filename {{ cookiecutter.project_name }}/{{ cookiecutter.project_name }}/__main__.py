{%- if cookiecutter.command_line_interface|lower == 'y' %}
"""Command line interface"""
import argparse


def main():
    """CLI entrypoint"""
    psr = argparse.ArgumentParser()
    args = psr.parse_args()
    #
    print(args)

{%- endif %}
