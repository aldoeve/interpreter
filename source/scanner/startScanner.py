#--------------------------------------------------------------------
# This file is the basic scanner code.
#
# Date updated: Sat May 10 11:56:23 PM CDT 2025
#--------------------------------------------------------------------
from util.statusCodes import StatusCodes

from typing import Optional
from io import TextIOWrapper


class Scanner:
    """
    Description:
        This class scans the python files.
    Usage:
        Scanner(<file_name>) # initalize
        scanner.run()        # starts scanning
    
    """
    def __init__(self, file_name) -> None:
        self.__dict__["status"] = StatusCodes.SUCCESS
        self.file: Optional[TextIOWrapper] = None
        try:
            self.file = open(file_name, 'r')
        except:
            self.__dict__["status"] = StatusCodes.ERROR

    def close(self) -> None:
        """
        Description:
            Frees resources.
        Usage:
            scanner.close()
        """
        if self.file:
            self.file.close()

    def __setattr__(self, name, value):
        if name == 'status':
            if value is StatusCodes.ERROR:
                self.__dict__[name] = StatusCodes.ERROR
                raise Exception("Scanner encountered and issue.")

    def run(self) -> StatusCodes:
        """
        Description:
            Starts scanning.
        Usage:
            scanner.run()
        Exceptions:
            Raises an exception on any error.
        """
        if self.status is StatusCodes.ERROR: return StatusCodes.ERROR


