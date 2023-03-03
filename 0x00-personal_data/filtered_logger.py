#!/usr/bin/env python3
"""module for filter_datum"""
import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:  # type: ignore # noqa
    """function to return obfuscated log message"""
    newDict = {item.split('=')[0]: item.split('=')[1] for item in message.split(separator)}  # noqa
    pattern = r'\b(' + '|'.join([newDict[key] for key in newDict.keys() if key in fields]) + r')\b'  # noqa
    return re.sub(pattern, redaction, message)
