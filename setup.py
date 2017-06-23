"""
Copyright (2017) Raydel Miranda 

This file is part of Django-S3.

    Django-S3 is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Django-S3 is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Django-S3.  If not, see <http://www.gnu.org/licenses/>.
"""

from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

long_description = ''

try:
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = ''

setup(
    name='real-django-s3',

    version='1.2.6',
    description='A simple API for download and upload graphics resources to/from a Amazon S3 bucket',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/RaydelMiranda/django-s3',

    # Author details
    author='Raydel Miranda',
    author_email='raydel.miranda.gomez@gmail.com',

    license='GPL',
    data_files=[('', ['README.md'])],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='development web django amazon s3',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=[
        'django_s3'
    ],

    include_package_data=True,

    install_requires=['boto==2.38.0', 'pytest', 'mock'],
)
