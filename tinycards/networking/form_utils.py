import json
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder
from .image_utils import get_image, mime_type_from_path


CARDS = 'cards'
IMAGE_FILE = 'imageFile'
BLACKLISTED_QUESTION_TYPES = 'blacklistedQuestionTypes'
GRADING_MODES = 'gradingModes'
TTS_LANGUAGES = 'ttsLanguages'
# Keys for which the data needs to be JSON-encoded:
JSON_KEYS = set([CARDS, BLACKLISTED_QUESTION_TYPES, GRADING_MODES, TTS_LANGUAGES])
# Keys for which the data needs to be encoded in special ways:
SPECIAL_KEYS = set([IMAGE_FILE]).union(JSON_KEYS)


def to_multipart_form(data, boundary=None):
    """Create a multipart form like produced by HTML forms from a dict."""
    fields = {}
    for k, v in data.items():
        if k not in SPECIAL_KEYS:
            fields[k] = str(v) if not isinstance(v, bool) else str(v).lower()
        if k in JSON_KEYS:
            fields[k] = json.dumps(data[k])
    if _has_image_file(data):
        fields[IMAGE_FILE] = _get_image(data[IMAGE_FILE])
    return MultipartEncoder(fields=fields, boundary=boundary)


def _has_image_file(data):
    return IMAGE_FILE in data and data[IMAGE_FILE]


# The name seems irrelevant to Tinycards as it isn't used anywhere, doesn't
# appear in the URL, and is always this regardless of the type of the image.
_FILENAME = 'cover.jpg'


def _get_image(path_or_url):
    '''
    Returns a tuple (filename, file, MIME type) compliant with requests_toolbelt's MultipartEncoder.
    See also: https://toolbelt.readthedocs.io/en/latest/uploading-data.html#uploading-data
    '''
    if os.path.exists(path_or_url):
        mime_type = mime_type_from_path(path_or_url)
        return (_FILENAME, open(path_or_url, 'rb'), mime_type)
    elif path_or_url.startswith('http'):
        img, mime_type = get_image(path_or_url)
        return (_FILENAME, img, mime_type)
    else:
        raise ValueError('Unknown image: %s' % path_or_url)
