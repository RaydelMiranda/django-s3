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

import os

import boto
from boto.s3.key import Key

from django_s3.s3_settings import django_s3_settings


class Transport(object):
    """
    Upload and download resources.
    """

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
        :return: 
        """
        try:
            key_holder = Key(self.__bucket)
            key_holder.key = resource.name
            key_holder.set_contents_from_filename(os.path.join(django_s3_settings.S3_UPLOAD_DIR_PATH, resource.name))
            key_holder.make_public()
        except Exception as err:
            raise

    def download(self, resource):
        """
        Download a resource.
        
        :param resource: 
        :return: 
        """
        pass
