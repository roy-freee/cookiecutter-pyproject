#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

REQUIREMENTS = []
SETUP_REQUIREMENTS = []
TEST_REQUIREMENTS = []
DEV_REQUIREMENTS = ["bumpversion", "pre-commit", "tox"]

with open("README.rst") as readme_file:
    README = readme_file.read()


{%- set license_classifiers = {
    "MIT": "License :: OSI Approved :: MIT License",
    "BSD": "License :: OSI Approved :: BSD License",
    "ISC": "License :: OSI Approved :: ISC License (ISCL)"
} %}

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
{%- if cookiecutter.open_source_license in license_classifiers %}
        "{{ license_classifiers[cookiecutter.open_source_license] }}",
{%- endif %}
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="{{ cookiecutter.project_short_description }}",
    {%- if cookiecutter.command_line_interface|lower == 'y' %}
    entry_points={"console_scripts": ["{{ cookiecutter.project_name }}={{ cookiecutter.project_name }}.__main__:main"]},
    {%- endif %}
    install_requires=REQUIREMENTS,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=README,
    include_package_data=True,
    keywords="{{ cookiecutter.project_name }}",
    name="{{ cookiecutter.project_name }}",
    packages=find_packages(include=["{{ cookiecutter.project_name }}"]),
    setup_requires=SETUP_REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    extras_require={"dev": DEV_REQUIREMENTS},
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}",
    version="{{ cookiecutter.version }}",
)
