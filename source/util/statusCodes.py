#--------------------------------------------------------------------
# This file has status codes that will be used throughout the code.
#
# Date updated: Sun May 11 04:34:56 PM CDT 2025
#--------------------------------------------------------------------

from enum import Enum

class StatusCodes(Enum):
    ERROR    = 1
    SUCCESS  = 0
    INIT     = 2
    RUNNING  = 3
    SYNTAX_ERROR = 4