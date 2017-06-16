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

import logging
import os

import boto
from boto.s3.key import Key
from django.utils.translation import ugettext_lazy as _

from django_s3.s3_settings import django_s3_settings


class Transport(object):
    """
    Upload and download resources.
    """

    logger = logging.getLogger('django-s3-transport')

    def __init__(self, aws_key, aws_secret, bucket_name):
        """
        Initializes the connection to the service.       
        """
        # connect to the bucket
        self.__conn = boto.connect_s3(aws_access_key_id=aws_key, aws_secret_access_key=aws_secret)
        self.__bucket = self.__conn.get_bucket(bucket_name)

    def upload(self, resource):
        """
        Upload a resource.
        
        :param resource: An instance of `django_s3.resource.Resource`
        """
        try:
            key_holder = Key(self.__bucket)
            key_holder.key = resource.name
            key_holder.set_contents_from_filename(os.path.join(django_s3_settings.S3_UPLOAD_DIR_PATH, resource.name))
            key_holder.make_public()
        except Exception as err:
            Transport.logger(_("Error uploading file: {}. Error: {}".format(resource.name, err)))
            # Right now we don't know what exceptions are expected here, we propagate the error
            # up. If we found some exception then we'll add the proper handler.
            raise

    def download(self, resource):
        """
        Download a resource.
        
        :param resource: An instance of `django_s3.resource.Resource`
        """

        files = self.__bucket.list()
        filename = os.path.join(django_s3_settings.S3_LOCAL_PATH, resource.name)

        # If the file exists do not download again.
        if not os.path.exists(filename):
            Transport.logger(_('Downloading {} to {}.'.format(resource.name, filename)))
            try:
                files.get_contents_to_filename(filename)
            except Exception as err:
                Transport.logger(_("Error downloading file: {}. Error: {}".format(resource.name, err)))
                # Right now we don't know what exceptions are expected here, we propagate the error
                # up. If we found some exception then we'll add the proper handler.
                raise
        else:
            Transport.logger(_('File already exists, skipping download: {}'.format(filename)))
