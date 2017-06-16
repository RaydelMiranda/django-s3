"""
Copyright (2017) Raydel Miranda 

This file is part of Dajngo-S3.

    Dajngo-S3 is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Dajngo-S3 is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Dajngo-S3.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.utils.translation import ugettext_lazy as _


class ResourceError(Exception):
    def __init__(self, message):
        super(ResourceError, self).__init__(message)


class ResourceNameError(ResourceError):
    def __init__(self, message=_("Malformed reource name")):
        super(ResourceError, self).__init__(message)
