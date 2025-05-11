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
        self._status: StatusCodes = StatusCodes.INIT
        self._file: Optional[TextIOWrapper] = None
        try:
            self.file = open(file_name, 'r')
        except Exception as e:
            print(str(e))
            self._status = StatusCodes.ERROR

    def getStatus(self) -> StatusCodes: return self._status
    def _setStatus(self, x: StatusCodes, err:str=None) -> None:
        """
        Description:
            Sets status and rasies exception on any error code.
        Usage:
            scanner._setStatus(<Literal>)
        Exception:
            General exception with an error message.
        """
        if x is not StatusCodes.ERROR:
            self._status = x
        else:
            self._status = x
            raise Exception(err)

    def close(self) -> None:
        """
        Description:
            Frees resources.
        Usage:
            scanner.close()
        """
        if self._file is not None:
            self._file.close()
            self._file = None

    def run(self) -> StatusCodes:
        """
        Description:
            Starts scanning.
        Usage:
            scanner.run()
        Exceptions:
            Raises an exception on any error.
        """
        if self.getStatus() is StatusCodes.ERROR: return StatusCodes.ERROR
        self._setStatus(StatusCodes.RUNNING)
        self._setStatus(StatusCodes.SUCCESS)


