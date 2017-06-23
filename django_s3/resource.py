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

import re

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from django_s3.exceptions import ResourceError, ResourceNameError, ResourceSizeError
from django_s3.s3_settings import django_s3_settings

url_pattern = re.compile(r'^(?P<folder_name>[A-Z]{1,2}\d+[-A-a0-9]+)_[\w-]+\.(?P<extension>\w{3,4})$')
cat_pattern = re.compile(r'^(?P<category_code>[A-Z]+)\d+.+$')
code_pattern = re.compile(r'^(?P<code>.+)\..+$')
size_pattern = re.compile('(?P<size>\d+x\d+)')


class Resource(object):
    """
    Represents a resource in a bucket
    """

    PUBLIC = 1
    PRIVATE = 2

    def __init__(self, name):
        self.__name = name
        self.__folder_name = None
        self.__category = None
        self.__category_code = None
        self.__url = None
        self.___public_url = None
        self.__code = None
        self.__extension = None
        self.__size = None

        # This is a control for checking the correctness of the file name, according
        # the convention specified by the API.
        self.__compute_url()

    def __compute_url(self, access_level=PRIVATE):
        match = url_pattern.match(self.__name)
        if match is not None:

            BASE_URL = django_s3_settings.S3_AWS_BASE_URL \
                if access_level == Resource.PRIVATE else django_s3_settings.S3_AWS_BASE_PUBLIC_URL
            BASE_URL = BASE_URL[:-1] if BASE_URL.endswith('/') else BASE_URL

            folder = settings.S3_CATEGORY_MAP[self.category_code]

            return "{}/{}/{}/{}/{}".format(
                BASE_URL,
                django_s3_settings.S3_BUCKET_NAME,
                folder,
                self.folder_name,
                self.name
            )
        else:
            raise ResourceNameError()

    @property
    def name(self):
        return self.__name

    @name.getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        raise ResourceError(_("This attribute is readonly, is set at creation time."))

    @property
    def folder_name(self):
        return self.__folder_name

    @folder_name.getter
    def folder_name(self):
        return self.__name.split('_')[0]

    @folder_name.setter
    def folder_name(self, value):
        raise ResourceError(_("This attribute is readonly, is set at creation time."))

    @property
    def category(self):
        return self.__category

    @category.getter
    def category(self):
        match = cat_pattern.match(self.folder_name)
        if match is not None:
            return django_s3_settings.S3_CATEGORY_MAP[match.groupdict()['category_code']]

    @category.setter
    def category(self, value):
        raise ResourceError(_("This attribute is readonly, see S3_CATEGORY_MAP."))

    @property
    def category_code(self):
        return self.__category_code

    @category_code.getter
    def category_code(self):
        match = cat_pattern.match(self.__name)
        if match is not None:
            return match.groupdict()['category_code']

    @category_code.setter
    def category_code(self, value):
        raise ResourceError(_("This attribute is readonly, see S3_CATEGORY_MAP."))

    @property
    def url(self):
        return self.__url

    @url.getter
    def url(self):
        if self.__url is None:
            self.__url = self.__compute_url()
        return self.__url

    @url.setter
    def url(self, value):
        raise ResourceError(_("This attribute readonly, It is calculated using the resource name"))

    @property
    def public_url(self):
        return self.___public_url

    @public_url.getter
    def public_url(self):
        if self.___public_url is None:
            self.___public_url = self.__compute_url(Resource.PUBLIC)
        return self.___public_url

    @public_url.setter
    def public_url(self, value):
        raise ResourceError(_("This attribute readonly, It is calculated using the resource name"))

    @property
    def code(self):
        return self.__code

    @code.getter
    def code(self):
        if self.__code is None:
            match = code_pattern.match(self.__name)
            if match is not None:
                self.__code = match.groupdict()['code']
            else:
                raise ResourceNameError()
        return self.__code

    @code.setter
    def code(self, value):
        raise ResourceError(_("This attribute readonly, It is calculated using the resource name"))

    @property
    def extension(self):
        return self.__extension

    @extension.getter
    def extension(self):
        if self.__extension is None:
            match = url_pattern.match(self.__name)
            if match is not None:
                self.__extension = match.groupdict()['extension']
            else:
                raise ResourceNameError()
        return self.__extension

    @extension.setter
    def extension(self, value):
        raise ResourceError(_("This attribute readonly, It is calculated using the resource name"))

    @property
    def size(self):
        return self.__size

    @size.getter
    def size(self):
        if self.__size is None:
            match = url_pattern.match(self.__name)
            if match is not None:
                try:
                    self.__size = match.groupdict()['size']
                except KeyError:
                    raise ResourceSizeError()
            else:
                raise ResourceNameError()
            # At this moment self.__size is a str object, (Ex. "100x100")
            # we need something like (100, 100)
            self.__size = [int(elem) for elem in self.__size.split('x')]
        return self.__size

    @size.setter
    def size(self, value):
        raise ResourceError(_("This attribute readonly, It is calculated using the resource name"))
