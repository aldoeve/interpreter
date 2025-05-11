import sys

from util.statusCodes import StatusCodes
from util.settings import Settings
from scanner.startScanner import Scanner

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
    if scanner.getStatus() is StatusCodes.INIT:
        try:
            scanner.run()
        finally:
            scanner.close()
    else:
        return StatusCodes.ERROR.value
    
    processes:StatusCodes = [scanner.getStatus()]

    if StatusCodes.ERROR in processes:
        return StatusCodes.ERROR.value

    return StatusCodes.SUCCESS.value

sys.exit(main())