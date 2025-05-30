from urllib.parse import urlparse


def extract_salon_name_from_url(url):
    """
    Extracts the salon name from a Google Maps URL by parsing the /place/<name>/... pattern.
    Returns a human-readable name.
    """
    try:
        path_parts = urlparse(url).path.split("/")
        if "place" in path_parts:
            raw_name = path_parts[path_parts.index("place") + 1]
            return raw_name.replace("+", " ")
    except Exception:
        pass
    return "Unknown Salon"
