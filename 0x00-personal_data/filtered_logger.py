#!/usr/bin/env python3
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.
    
    Args:
    - fields (List[str]): The list of fields to obfuscate.
    - redaction (str): The string to replace the field values with.
    - message (str): The log message containing the fields.
    - separator (str): The character separating the fields in the log message.
    
    Returns:
    - str: The log message with specified fields obfuscated.
    """
    pattern = '|'.join([f'{field}=[^{separator}]*' for field in fields])
    return re.sub(pattern, lambda x: x.group().split('=')[0] + '=' + redaction, message)
