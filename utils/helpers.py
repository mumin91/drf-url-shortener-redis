import zlib

from utils.hash import hash_id


def get_short_url_code(long_url: str) -> str:
    crc = zlib.crc32(long_url.encode())
    return hash_id.encode(crc)