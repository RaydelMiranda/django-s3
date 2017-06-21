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

from django_s3.browser import Browser, FileTreeNode


@pytest.mark.usefixtures('paths')
class TestBrowser:
    def test_build_jason(self, paths):
        expected_structure = {
            'EXAMPLE': {
                'example.txt': {},
                'Example_1': {
                    'example_1.txt': {}
                }
            },
            'GRAPHIC-RESOURCES': {
                'BACKGROUNDS': {},
                'CLIPPING-FLOWERS': {},
                'CUSTOM-PRODUCTS': {},
                'CUSTOMIZABLE-PRODUCTS': {},
                'GIFTS': {},
                'LINE-PRODUCTS': {},
                'RESOURCE-COMPOSITIONS': {},
                'VASES': {},
                'VASES-WITH-BACKGROUNDS': {},
                'WRAPPING-FLOWERS': {}
            },
            'RAW-PICTURES': {
                'BACKGROUNDS': {},
                'GIFTS': {},
                'PRODUCTS': {
                    'CR01': {},
                    'CR02': {},
                    'CR03': {}
                },
                'VASES': {},
                'WRAPPING-FLOWERS': {}
            }
        }
        browser = Browser(paths)
        assert browser.walk() == expected_structure, \
            "The structure for the folders is not correct."

    def test_browser_get_structure_relative(self, paths):
        browser = Browser(paths)
        assert browser.walk('EXAMPLE') == {'example.txt': {}, 'Example_1': {'example_1.txt': {}}}, \
            "walk function with parameter returns the structure relative to the folder"

    def test_file_dir_type(self, paths):
        browser = Browser(paths)

        node = browser.walk('EXAMPLE')
        assert node.type == FileTreeNode.DIR
        assert node['example.txt'].type == FileTreeNode.FILE
        assert node['Example_1'].type == FileTreeNode.DIR

        node = browser.walk('RAW-PICTURES/PRODUCTS/CR01')
        assert node.type == FileTreeNode.DIR

    def test_file_dir_type(self, paths):
        browser = Browser(paths)

        node = browser.walk('EXAMPLE')
        assert node.name == 'EXAMPLE'
        assert node['example.txt'].name == 'example.txt'
