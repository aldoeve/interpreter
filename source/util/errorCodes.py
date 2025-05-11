from enum import Enum

class ErrorCodes(Enum):
    ERROR = 1
    SUCCESS = 0
    TRANSLATION_ERROR = 2
    SYNTAX_ERROR = 3

class Settings(Enum):
    ARGS = 1
