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

PATHS = [
    "GRAPHIC-RESOURCES/",
    "GRAPHIC-RESOURCES/BACKGROUNDS/",
    "GRAPHIC-RESOURCES/CLIPPING-FLOWERS/",
    "GRAPHIC-RESOURCES/CUSTOM-PRODUCTS/",
    "GRAPHIC-RESOURCES/CUSTOMIZABLE-PRODUCTS/",
    "GRAPHIC-RESOURCES/GIFTS/",
    "GRAPHIC-RESOURCES/LINE-PRODUCTS/",
    "GRAPHIC-RESOURCES/RESOURCE-COMPOSITIONS/",
    "GRAPHIC-RESOURCES/VASES-WITH-BACKGROUNDS/",
    "GRAPHIC-RESOURCES/VASES/",
    "GRAPHIC-RESOURCES/WRAPPING-FLOWERS/",
    "EXAMPLE/example.txt",
    "RAW-PICTURES/",
    "RAW-PICTURES/BACKGROUNDS/",
    "RAW-PICTURES/GIFTS/",
    "RAW-PICTURES/PRODUCTS/",
    "RAW-PICTURES/PRODUCTS/CR01/",
    "RAW-PICTURES/PRODUCTS/CR02/",
    "RAW-PICTURES/PRODUCTS/CR03/",
    "RAW-PICTURES/VASES/",
    "RAW-PICTURES/WRAPPING-FLOWERS/",
]


@pytest.fixture(scope='class')
def paths():
    return PATHS
