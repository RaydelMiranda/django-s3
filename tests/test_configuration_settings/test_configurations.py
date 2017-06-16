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

import tempfile

import mock
import pytest

from django_s3.s3_settings import DjangoS3SettingError


class TestSettings:
    @mock.patch('django_s3.s3_settings.settings', spec_set={})
    def test_missing_settings_error(self, mock_settings):
        with pytest.raises(DjangoS3SettingError):
            django_s3 = __import__('django_s3')
            # Accessing some configuration variable
            dir(django_s3.s3_settings.django_s3_settings)

    @mock.patch('django_s3.s3_settings.settings', autospec=True)
    def test_wrong_local_path_settings_error(self, mock_settings):
        mock_settings.S3_LOCAL_PATH = tempfile.mktemp()

        with pytest.raises(DjangoS3SettingError):
            django_s3 = __import__('django_s3')
            # Accessing some configuration variable
            dir(django_s3.s3_settings.django_s3_settings)

    @mock.patch('django_s3.s3_settings.settings', autospec=True)
    def test_wrong_upload_dir_path_settings_error(self, mock_settings):
        # We need an existing file name here in order to hit
        # the checkpoint for S3_UPLOAD_DIR_PATH.
        mock_settings.S3_LOCAL_PATH = '/'
        mock_settings.S3_UPLOAD_DIR_PATH = tempfile.mktemp()

        with pytest.raises(DjangoS3SettingError):
            django_s3 = __import__('django_s3')
            # Accessing some configuration variable
            dir(django_s3.s3_settings.django_s3_settings)
