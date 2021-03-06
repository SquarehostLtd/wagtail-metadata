#!/usr/bin/env python
"""
Install wagtail-metadata using setuptools
"""

from setuptools import find_packages, setup

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='wagtail-metadata',
    version='0.4.1',
    description="A tool to assist with metadata for social media.",
    long_description=readme,
    author='Liam Brenner',
    author_email='liam@takeflight.com.au',
    url='https://github.com/takeflight/wagtail-metadata',

    #install_requires=[
    #    'wagtail>=1.12,<=1.9999',
    #],
    zip_safe=False,
    license='BSD License',

    packages=find_packages(exclude=['tests', 'tests*']),

    include_package_data=True,
    package_data={},

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
    ],
)
