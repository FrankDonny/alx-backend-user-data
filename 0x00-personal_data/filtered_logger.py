#!/usr/bin/env python3
"""module for filter_datum"""
import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:  # type: ignore # noqa
    """function to return obfuscated log message"""
    newDict = {item.split('=')[0]: item.split('=')[1] for item in message.split(separator) if '=' in item}  # noqa
    pattern = r'\b(' + '|'.join([newDict[key] for key in newDict.keys() if key in fields]) + r')\b'  # noqa
    return re.sub(pattern, redaction, message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields) -> None:
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format the record"""
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            message, self.SEPARATOR)


message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
log_record = logging.LogRecord(
    "my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(log_record))
