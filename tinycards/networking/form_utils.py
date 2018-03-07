from uuid import uuid4


def generate_form_boundary():
    """Generate a 16 digit boundary like the one used by Tinycards."""
    boundary = str(uuid4()).replace('-', '')[:16]
    return boundary


def to_multipart_form(data, boundary):
    """Create a multipart form like produced by HTML forms from a dict."""
    form_lines = []
    for k, v in data.items():
        form_lines.append('--' + boundary)
        # Handle special case for imageFile.
        if k == 'imageFile':
            form_lines.append('Content-Disposition: form-data; ' +
                              'name="%s"; filename="cover.jpg"' % k)
            form_lines.append('Content-Type: image/jpeg')
            form_lines.append('')
            form_lines.append('')
        else:
            form_lines.append('Content-Disposition: form-data; name="%s"'
                              % k)
            form_lines.append('')
            # Lowercase bool values to follow JSON standards.
            form_lines.append(str(v) if type(v) is not bool
                              else str(v).lower())
    form_lines.append('--' + boundary + '--')

    joined_form = '\n'.join(form_lines)
    return joined_form
