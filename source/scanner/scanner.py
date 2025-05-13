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
        self._tokens: list[Token] = list()
        self._tokenDict: dict = self._loadDict()
        try:
            self._file = open(file_name, 'r')
        except Exception as e:
            print(str(e))
            self._status = StatusCodes.ERROR

    def _loadDict(self)-> dict:
        """
        Description:
            Creates the static map that hold token info to match to.
        Usage:
            self._loadMap()
        """
        return {
            '(': TokenType.LEFT_PAREN,
            ')': TokenType.RIGHT_PAREN,
            '{': TokenType.LEFT_BRACE,
            '}': TokenType.RIGHT_BRACE,
            ',': TokenType.COMMA,
            '.': TokenType.DOT,
            '-': TokenType.MINUS,
            '+': TokenType.PLUS,
            ';': TokenType.SEMICOLON,
            ':': TokenType.COLON,
            '\\': TokenType.SLASH,
            '*': TokenType.STAR,
            'is': TokenType.IS,
            'not': TokenType.NOT,
            '!=': TokenType.NOT_EQUAL,
            '=': TokenType.EQUAL,
            
        }

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
    
    def _addToken(self, token: TokenType, lexeme: str, literal: object) -> None:
        """
        Descripition:
            Appends a line aware token to the tokens list.
        Usage:
            self._addToken(<TokenType>, <str>, <object>)
        """
        self._tokens.append(Token(token, lexeme, literal, self._line))

    def _scanToken(self, token: str) -> None:
        """
        Description:
            Identifies the token and appends it to the list of tokens.
        Usage:
            self._scanToken(<str>)
        """
        tokenType: Optional[TokenType] = self._tokenDict.get(token)
        if tokenType is None:
            self._setStatus(StatusCodes.SYNTAX_ERROR)
            self._error(f"Unexpected character: {token}")            


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
        self._addToken(TokenType.EOF, '', None)


    def run(self):
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

        line:str = self._consumeLine()
        while line:
            self._tokenizeLine(line)
            line = self._consumeLine()

        if self.getStatus() is not StatusCodes.ERROR:
            self._setStatus(StatusCodes.SUCCESS)

