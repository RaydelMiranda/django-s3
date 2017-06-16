import logging
import os

from django.conf import LazyObject
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

logger = logging.getLogger('django-s3')


class DjangoS3SettingError(Exception):
    pass


class DjangoS3Settings(object):
    def __init__(self):

        self.S3_LOCAL_PATH = getattr(settings, 'S3_LOCAL_PATH', None)
        self.S3_UPLOAD_DIR_PATH = getattr(settings, 'S3_UPLOAD_DIR_PATH', None)
        self.S3_BUCKET_NAME = getattr(settings, 'S3_BUCKET_NAME', None)
        self.S3_AWS_ACCESS_KEY_ID = getattr(settings, 'S3_AWS_ACCESS_KEY_ID', None)
        self.S3_AWS_SECRET_ACCESS_KEY = getattr(settings, 'S3_AWS_SECRET_ACCESS_KEY', None)
        self.S3_AWS_BASE_URL = getattr(settings, 'S3_AWS_BASE_URL', None)
        self.S3_CATEGORY_MAP = getattr(settings, 'S3_CATEGORY_MAP', None)

        for setting_name in ['S3_BUCKET_NAME',
                             'S3_AWS_ACCESS_KEY_ID',
                             'S3_AWS_SECRET_ACCESS_KEY',
                             'S3_CATEGORY_MAP',
                             'S3_AWS_BASE_URL',
                             'S3_UPLOAD_DIR_PATH']:
            if getattr(self, setting_name) is None:
                raise DjangoS3SettingError(_("You must to set {} configuration variable".format(setting_name)))

        if not os.path.exists(self.S3_LOCAL_PATH):
            raise DjangoS3SettingError(_("Directory not found: {}".format(self.S3_LOCAL_PATH)))

        if not os.path.exists(self.S3_UPLOAD_DIR_PATH):
            raise DjangoS3SettingError(_("Directory not found: {}".format(self.S3_UPLOAD_DIR_PATH)))


class DjangoS3LazySettings(LazyObject):
    def _setup(self, name=None):
        self._wrapped = DjangoS3Settings()


django_s3_settings = DjangoS3LazySettings()
