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
from django.utils.translation import ugettext_lazy as _

from django_s3.exceptions import ResourceError
from django_s3.resource import Resource


@pytest.mark.usefixtures('django_settings', 'resource')
class TestSource:

    def test_resource_creation(self, settings, resource):
        assert isinstance(resource, Resource)

    def test_get_url(self, settings, resource):
        # F0001-B0001_320x320.SVG
        assert resource.url == \
               settings.S3_AWS_BASE_URL + settings.S3_BUCKET_NAME + '/F0001-B0001/' + resource.name

    def test_set_url(self, settings, resource):
        with pytest.raises(ResourceError) as exceinfo:
            resource.url = 'some value'
            assert _("Malformed reource name") == str(exceinfo.value)

    def test_get_name(self, settings, resource):
        assert 'F0001-B0001_320x320.SVG' == resource.name

    def test_set_url(self, settings, resource):
        with pytest.raises(ResourceError) as exceinfo:
            resource.name = 'some value'
            assert _("This attribute is readonly, is set at creation time.") == str(exceinfo.value)

    def test_get_category(self, settings, resource):
        samples = [
            ('B0001_DEFAULT.JPG', 'BACKGROUND'),
            ('F0001_WHITE_DEFAULT.JPG', 'VASE'),
            ('F2344-B0001_DEFAULT.JPG', 'VASE'),
            ('CF0001_WHITE_DEFAULT.JPG', 'CLIPPING-FLOWER'),
            ('WF0001_WHITE_DEFAULT.JPG', 'WRAPPING-FLOWER'),
            ('CR01-047_B0001_320x320.JPG', 'CATALOGUE-PRODUCT'),
            ('PP0001', 'PERSONALIZED-PRODUCT'),
            ('CM991992', 'COMPOSITION')
        ]
        for file_name, expected_category in samples:
            res = Resource(file_name)
            assert res.category == expected_category, \
                _("Expected category {} for the resource with name {}, see the settings "
                  "configuration: S3_CATEGORY_MAP.".format(expected_category, file_name))

    def test_set_catgegory(self, settings, resource):
        with pytest.raises(ResourceError) as exceinfo:
            resource.category = 'some value'
            assert _("This attribute is readonly, see S3_CATEGORY_MAP.") == str(exceinfo.value)
