from django.urls import re_path
from . import consumers

url_patterns = [
    re_path(r'ws/.*', consumers.RequestConsumer.as_asgi())
]
