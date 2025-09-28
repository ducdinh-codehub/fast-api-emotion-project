''' SHARING METHODS TO ALL THE PROJECT '''
import base64
import time

def crc32_custom(data):
    crc = 0xFFFFFFFF
    polynomial = 0x04C11DB7
    if isinstance(data, str):
        data = data.encode('utf-8')
    for byte in data:
        crc ^= byte << 24
        for _ in range(8):
            crc = (crc << 1) ^ polynomial if crc & 0x80000000 else crc << 1
            crc &= 0xFFFFFFFF
    return crc

def map_to_range(hash_value, max_value=100000000):
    return (hash_value % max_value) + 1

async def hash_email_value(data: str):
    hash_value = crc32_custom(data)
    return map_to_range(hash_value)