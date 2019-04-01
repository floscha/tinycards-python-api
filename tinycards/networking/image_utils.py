from io import BytesIO
from mimetypes import guess_type
import requests


def get_image(url):
    '''
    Get the image at the provided URL and returns a file-like buffer
    containing its bytes, and its MIME type.
    '''
    resp = requests.get(url)
    if not resp.ok:
        raise RuntimeError(
            'Failed to download image from %s: %s - %s'
            % (url, resp.status_code, resp.text)
        )
    img = BytesIO(resp.content)
    mime_type = _mime_type(img, resp.headers, url)
    return img, mime_type


def _mime_type(img, headers, url):
    '''
    Try to get the MIME type of the provided image using either the HTTP
    response's headers, information available via its URL, or by reading the
    beginning of the image's bytes.
    '''
    if ('Content-Type' in headers
            and headers['Content-Type'].startswith('image/')):
        return headers['Content-Type']
    mime_type, _ = guess_type(url)
    if mime_type and mime_type.startswith('image/'):
        return mime_type
    mime_type = mime_type_from_bytes(img.read())
    img.seek(0)  # Reset the BytesIO object, so that it can be read again.
    return mime_type


def mime_type_from_path(img_path):
    ''' Guess the MIME type of the provided image. '''
    mime_type, _ = guess_type(img_path)
    if mime_type and mime_type.startswith('image/'):
        return mime_type
    with open(img_path, 'rb') as img:
        return mime_type_from_bytes(img.read(_LEN_HEADER))


# Only the first 11 bytes of an image are useful to determine its type.
_LEN_HEADER = 11


def mime_type_from_bytes(img_bytes):
    ''' Guess the MIME type of the provided image. '''
    img_bytes = img_bytes[:_LEN_HEADER]
    if img_bytes[:4] == b'\xff\xd8\xff\xe0' and img_bytes[6:] == b'JFIF\0':
        return 'image/jpeg'
    elif img_bytes[1:4] == b'PNG':
        return 'image/png'
    else:
        raise ValueError('Unsupported image type')
