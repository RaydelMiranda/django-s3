"""
Copyright (2017) Raydel Miranda Gomez 

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

import boto
from django.conf import settings


class FileTreeNode(dict):
    DIR = 1
    FILE = 0

    def __init__(self, type_=DIR, name='', *args, **kwargs):
        super(FileTreeNode, self).__init__(*args, **kwargs)
        self.type = type_
        self.name = name


def get_file_list():
    conn = boto.connect_s3(
        aws_access_key_id=settings.S3_AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.S3_AWS_SECRET_ACCESS_KEY
    )
    bucket = conn.get_bucket(settings.S3_BUCKET_NAME)
    return list(bucket.list())


class Browser(object):
    def __init__(self, file_list=None):
        self.__structure = FileTreeNode()
        # Connect to the bucket to obtain the file list if is None
        if file_list is None:
            self.__files = get_file_list()
        else:
            self.__files = file_list

        self.__build_structure(self.__files)

    def __build_structure(self, files):

        paths = list(files)
        paths.sort(key=lambda x: len(x.split('/')))

        for path in paths:
            self.__arrange_path_within_structure(path.split('/'), self.__structure)

    def __arrange_path_within_structure(self, path, structure):
        if path == [] or path[0] == '':
            return
        if path[0] not in structure.keys():
            structure[path[0]] = FileTreeNode(type_=FileTreeNode.DIR, name=path[0])
        # Rectify type if is a file.
        if path[-1] != '' and path[-1] == path[0]:
            structure[path[0]].type = FileTreeNode.FILE
        self.__arrange_path_within_structure(path[1:], structure[path[0]])

    def walk(self, relative_to="/"):
        if relative_to == '/':
            return self.__structure
        else:
            parts = relative_to.split('/')
            parts = filter(lambda x: x != '', parts)
            node = self.__structure
            for p in parts:
                node = node[p]
            return node
