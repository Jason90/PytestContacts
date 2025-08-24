import re  # Add this import at the top

def clean_invalid_chars(text: str) -> str:
    """Remove invalid Unicode characters (like \x80) and non-printable characters
        to fix the issue in pytest-html: UnicodeEncodeError: 'gbk' codec can't encode character '\x80'
    """ 
    # Keep printable ASCII and valid Unicode characters
    pattern = re.compile(r'[^\x20-\x7E\u0100-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]')
    return pattern.sub('', text)