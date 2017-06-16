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


class __CategoryDescriptor:
    """
    A descriptor that returns a category name according the mapping defined in settings.
    """

    def __init__(self):
        pass

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass


__category = __CategoryDescriptor()


def Category():
    return __category
