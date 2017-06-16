import tempfile

SECRET_KEY = 'FALSE-KEY-000'

S3_BUCKET_NAME = 'BucketName'
S3_AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
S3_AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
S3_LOCAL_PATH = tempfile.gettempdir()
S3_UPLOAD_DIR_PATH = tempfile.gettempdir()
S3_AWS_BASE_URL = 'http://s3.amazonaws.com/'
S3_CATEGORY_MAP = {
    'B': 'BACKGROUND',
    'F': 'VASE',
    'CF': 'CLIPPING-FLOWER',
    'WF': 'WRAPPING-FLOWER',
    'CR': 'CATALOGUE-PRODUCT',
    'PP': 'PERSONALIZED-PRODUCT',
    'CM': 'COMPOSITION'
}

INSTALLED_APPS = [
    'django_s3',
]

MIDDLEWARE_CLASSES = (
)
