Django application for handling graphics resources served  in a S3 Amazon webservice
====================================================================================

Settings
--------

Settings example: 

```python
# Configuration example

S3_BUCKET_NAME = 'bucket-name'                      # The name of the bucket we are working with
S3_AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'          # AWS access key
S3_AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'  # AWS secret access key
S3_LOCAL_PATH = tempfile.gettempdir()               # Path where to put downloaded files.
S3_UPLOAD_DIR_PATH = tempfile.gettempdir()          # Path where to search files for uploading.
S3_AWS_BASE_URL = 'http://s3.amazonaws.com/'        # Base url for Amazon S3 services.
S3_CATEGORY_MAP = {                                 # Map code - category, this is for organizing the 
    'B':  'BACKGROUND',                              # the folders in the bucket.
    'F':  'VASE',
    'CF': 'CLIPPING-FLOWER',
    'WF': 'WRAPPING-FLOWER',
    'CR': 'CATALOGUE-PRODUCT',
    'PP': 'PERSONALIZED-PRODUCT',
    'CM': 'COMPOSITION'
}

INSTALLED_APPS = [
    'django_s3',                                    # Add the app to installed apps.
]
```


Transport
=========

Transport is the class for download and upload resources.


Downloading a resource
----------------------

```python
 from django_s3.transport import Transport
 from django_s3.resource import Resource

 rource = Resource('some_name.jpg')
 transport = Transport()
 filename = transport.download(resource)
 
```

Uploading a resource
--------------------

```python
 from django_s3.transport import Transport
 from django_s3.resource import Resource

 rource = Resource('some_name.jpg')
 transport = Transport()
 filename = transport.upload(resource)
```

Downloading a resource by name
------------------------------

```python
 from django_s3.transport import Transport
 from django_s3.resource import Resource

 filename = transport.download('some_name.jpg')
```


Resource
========

Class for holding information about resources. A resource's name has to 
follow the following name convention:

`<code><serial>_<rest_of_the_resource_name><size>.<extension>`

* <code>: Upper case letters that identify the resource type (Ex. 'BG' for Backgrounds)
* <serial>: A serial number unique for every resource.
* <rest_of_the_resource_name>: String for a name.
* <size>: The size of the image (Ex. 800x600)
* <extension>: The image's extension.

```python
# Example that shows how to get info about a resource.

from django_s3.resource import Resource

 rource = Resource('some_name.jpg')
 code = resource.code               # The code of the type.
 size = resource.size               # The size, as a 2-tuple value.    
 extension = resource.extension     # The extension
 category = resource.category       # The category mapped to the code.
 url = resource.url                 # The url where to find the resource


```

> All this attributes are read-only, and computed at creation time.

Browser
=======

A class for walking through the bucket filesystem.

```python

from django_s3.browser import Browser
from django_s3.browser import FileTreeNode


browser = Browser()
root_node = browser.walk()                  # Returns the whole directory tree. 
node = browser.walk('path/to/some/node')    # Returns the directory tree relative to the path
                                            # passed by parameter
                                            
# You can check for the node type as well
if node.type == FileTreeNode.DIR:
    pass

if node.type == FileTreeNode.File:
    pass
```

Accessing resource info using Resource class. 
---------------------------------------------

Just create a new resource instance and query it for its metadata.

```python

from django_s3.browser import Browser

browser = Browser()
node = browser.walk('path/to/some/node')    # Returns the directory tree relative to the path
                                            # passed by parameter
resource = Resource(node.name)              # Now you can see metadata for resources.                                         
```