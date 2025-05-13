#--------------------------------------------------------------------
# This kicks off the transcribing of the python code.
#
# Date updated: Sun May 11 04:34:56 PM CDT 2025
#--------------------------------------------------------------------

import sys

from util.statusCodes import StatusCodes
from util.settings import Settings
from scanner.scanner import Scanner

def help():
    usageAndDetails: str = \
    """
Usage: python3 run.py <input_file> [options]

Arguements:
    <input_file>    Path to file to py script turn to bash

Options:
    -h, --help          Show this message

Example:
    python3 run.py test.py 
    """
    print(usageAndDetails)

def main():
    listArgs: list[str] = sys.argv[1:]
    num_args: int = len(listArgs)
    
    if "--help" in listArgs or "-h" in listArgs:
        help()
        return StatusCodes.SUCCESS.value
    elif num_args != Settings.EXPECTED_ARGS.value:
        help()
        return StatusCodes.ERROR.value

    fileToTranslate: str = sys.argv[1]
    scanner = Scanner(fileToTranslate)
    runtimeStatus: StatusCodes = StatusCodes.SUCCESS

    if scanner.getStatus() is StatusCodes.INIT:
        try:
            scanner.run()
            runtimeStatus = scanner.getStatus()
        finally:
            scanner.close()
    else:
        runtimeStatus = StatusCodes.ERROR
    
    return (StatusCodes.SUCCESS.value if runtimeStatus is not StatusCodes.ERROR else StatusCodes.ERROR.value)

sys.exit(main())