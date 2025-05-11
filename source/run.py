import sys
from util.errorCodes import ( 
    ErrorCodes, Settings
)

def help():
    print("help")

def main():
    num_args: int = len(sys.argv) - 1
    if num_args != Settings.ARGS.value:
        help()
        return ErrorCodes.ERROR.value

main()
