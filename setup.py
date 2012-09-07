#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='django-w3cvalidator',
    #version=__import__('').__version__,
    #description=__import__('').__description__,
    #long_description=open('').read(),
    url='http://github.com/akarl818/django-w3cvalidator',
    download_url='http://github.com/akarl818/django-w3cvalidator',
    author='Andreas Karlsson',
    #author_email='',
    #packages=[],
    include_package_data=True,
    install_requires=['django'],
    license='LGPL',
    classifiers=[
        "Framework :: Django",
        "Development Status :: 1 - Alpha",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: System :: Software Distribution",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    ],
)
