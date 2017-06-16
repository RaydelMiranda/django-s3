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

import pytest

from django_s3.resource import Resource


class DUMMYSettings:
    def __init__(self):
        self.S3_BUCKET_NAME = 'BucketName'
        self.S3_AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
        self.S3_AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
        self.S3_LOCAL_PATH = 'S3_LOCAL_PATH'
        self.S3_AWS_BASE_URL = 'http://s3.amazonaws.com/'
        self.S3_DJANGO_S3_CATEGORY_MAPPING = {
            'B': 'BACKGROUND',
            'F': 'VASES',
            'CF': 'CLIPPING-FLOWERS',
            'WF': 'WRAPPING-FLOWERS',
            'CR': 'CATALOGUE-PRODUCTS',
            'PP': 'PERSONALIZED-PRODUCTS',
            'CM': 'COMPOSITIONS'
        }


@pytest.fixture(scope='class')
def settings():
    return DUMMYSettings()


@pytest.fixture(scope='class')
def resource():
    return Resource('F0001-B0001_320x320.SVG')
