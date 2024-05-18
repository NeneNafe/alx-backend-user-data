#!/usr/bin/env python3
"""a function called filter_datum that returns the log
"""

from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated
    fields List[str]: a list of strings representing all fields to obfuscate
    redaction (str): a string representing by what the field will be obfuscated
    message (str): a string representing the log line
    separator (str): a string representing by which character is separating all
                        fields in the log line (message)
    """
    return re.sub(r"(\w+)=([a-zA-Z0-9@\.\-\(\)\ \:\^\<\>\~\$\%\@\?\!\/]*)",
                  lambda match: match.group(1) + "=" + redaction
                  if match.group(1) in fields else match.group(0), message)
