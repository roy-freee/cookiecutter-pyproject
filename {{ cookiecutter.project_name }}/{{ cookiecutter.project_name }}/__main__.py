{%- if cookiecutter.command_line_interface|lower == 'y' %}
import argparse


def main():
    psr = argparse.ArgumentParser()
    args = psr.parse_args()

{%- endif %}
