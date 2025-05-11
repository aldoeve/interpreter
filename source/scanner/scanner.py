#--------------------------------------------------------------------
# This file is the basic scanner code.
#
# Date updated: Sun May 11 04:34:56 PM CDT 2025
#--------------------------------------------------------------------
from util.statusCodes import StatusCodes
from .myToken import TokenType, Token

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
        self._line: int = 0
        self._tokens: list[Token] = list
        try:
            self._file = open(file_name, 'r')
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
    
    def _error(self, msg: str) -> None:
        """
        Description:
            Prints debug lines for transcompiling errors.
        Usage:
            self._error(<'str'>)
        """
        print(f"Line {self._line}: {msg}")

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

    def _consumeLine(self) -> str:
        """
        Description:
            Reads next line using readline().
        Usage:
            line = self._consumeLine()
        """
        self._line += 1
        return self._file.readline()
    
    def _scanToken(token: str) -> None:
        """
        Description:
            Identifies the token and appends it to the list of tokens.
        Usage:
            self._scanToken(<str>)
        """

    def _tokenizeLine(self, line:str) -> None:
        """
        Description:
            starts tokenization of a line.
        Usage:
            self._tokenize_line(<str>)
        """
        strArry:list[str] = line.split()

        for token in strArry:
            self._scanToken(token)
        self._tokens.append(Token(TokenType.EOF, "", None, self._line))


    def run(self) -> StatusCodes:
        """
        Description:
            Starts scanning.
        Usage:
            scanner.run()
        Exceptions:
            Raises an exception on any error.
        """
        if self.getStatus() is not StatusCodes.INIT: return StatusCodes.ERROR

        self._setStatus(StatusCodes.RUNNING)

        line = self._consumeLine()
        while line:
            self._tokenizeLine(line)
            line = self._consumeLine()

        self._setStatus(StatusCodes.SUCCESS)


