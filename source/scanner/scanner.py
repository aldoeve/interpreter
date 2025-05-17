#--------------------------------------------------------------------
# This file is the basic scanner code.
#
# Date updated: Sun May 11 04:34:56 PM CDT 2025
#--------------------------------------------------------------------
from util.statusCodes import StatusCodes
from util.myToken import TokenType, Token

from typing import Optional
from io import TextIOWrapper

import re
import keyword

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
        self._discardMode: bool = False
        self._stringMode: bool = False
        self._keywords: list = [kw for kw in keyword.kwlist if len(kw) > 2] +["print"]
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
            '(':      TokenType.LEFT_PAREN,
            ')':      TokenType.RIGHT_PAREN,
            '{':      TokenType.LEFT_BRACE,
            '}':      TokenType.RIGHT_BRACE,
            ',':      TokenType.COMMA,
            '.':      TokenType.DOT,
            '-':      TokenType.MINUS,
            '+':      TokenType.PLUS,
            ';':      TokenType.SEMICOLON,
            ':':      TokenType.COLON,
            '\\':     TokenType.SLASH,
            '*':      TokenType.STAR,
            'is':     TokenType.IS,
            'not':    TokenType.NOT,
            '!=':     TokenType.NOT_EQUAL,
            '=':      TokenType.EQUAL,
            '==':     TokenType.EQUAL_EQUAL,
            '>':      TokenType.GREATER,
            '>=':     TokenType.GREATER_EQUAL,
            '<':      TokenType.LESS,
            '<=':     TokenType.LESS_EQUAL,
            'and':    TokenType.AND,
            'class':  TokenType.CLASS,
            'else':   TokenType.ELSE,
            'False':  TokenType.FALSE,
            'def':    TokenType.DEF,
            'for':    TokenType.FOR,
            'if':     TokenType.IF,
            'None':   TokenType.NONE,
            'or':     TokenType.OR,
            'print':  TokenType.PRINT,
            'return': TokenType.RETURN,
            'self':   TokenType.SELF,
            'True':   TokenType.TRUE,
            'while':  TokenType.WHILE,
            'elif':   TokenType.ELSE_IF,
            '!':      TokenType.BANG,
            '#':      TokenType.COMMENT,
            '\"':     TokenType.QUOTES,
            '\'':     TokenType.QUOTES,
            ' ':      TokenType.SPACE,
        }

    def getStatus(self) -> StatusCodes: return self._status
    def getTokensList(self) -> list[Token]:
        """
        Description:
            Returns a list of tokens if successfully tokenized else returns None.
        Usage:
            scanner.getTokensList()
        """
        return self._tokens if self.getStatus() == StatusCodes.SUCCESS else None
    
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

    def _scanTokenFromWord(self, word: str, atEndOfLine: bool=False) -> None:
        """
        Description:
            Identifies the token and appends it to the list of tokens. Acts as the conventional advance().
        Usage:
            self._scanToken(<str>)
        """
        #tokenType: Optional[TokenType] = self._tokenDict.get(token)
        lookahead1Valid  = lambda i, word, : True if i < len(word) - 1 else False
        isLookAhead1This = lambda i, tokenType, word: tokenType == self._tokenDict.get(word[i + 1])

        var     = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
        number  = r'(?<!\w)(\d+(\.\d+)?)(?!\w)'

        #filter for keywords larger than 2 chars
        keyword = r"\b(" + "|".join(self._keywords) + r")\b"
        isKeyword = False

        i = 0
        #print(f"working with: {word}")
        while i < len(word):
            #print(f"{word[i]}")
            if not self._stringMode and not self._discardMode:
                varNameMatch = re.search(var, word[i:])
                if varNameMatch is None: varNameMatch = re.search(number, word[i:])
                if varNameMatch is None: 
                    varNameMatch = re.search(keyword, word[i:])
                    if varNameMatch: isKeyword = True
                if varNameMatch and varNameMatch.start() <= i <= varNameMatch.end():
                    self._addToken(TokenType.IDENTIFIER if not isKeyword else self._tokenDict.get(word[varNameMatch.start():varNameMatch.end()])\
                                   , word[varNameMatch.start():varNameMatch.end()], word[varNameMatch.start():varNameMatch.end()])
                    i = varNameMatch.end()
    
                if i >= len(word): return

            # Identifies one-two character tokens
            tokenType: Optional[TokenType] = self._tokenDict.get(word[i])

            match tokenType:
                case TokenType.EQUAL:
                    if lookahead1Valid(i, word) and isLookAhead1This(i, TokenType.EQUAL, word): 
                        tokenType = TokenType.EQUAL_EQUAL
                case TokenType.BANG:
                    if lookahead1Valid(i, word) and isLookAhead1This(i, TokenType.EQUAL, word): 
                        tokenType = TokenType.NOT_EQUAL
                    else:
                        self._error(f"Unexpected token {{{word[i]}}}")
                        self._setStatus(StatusCodes.SYNTAX_ERROR)
                case TokenType.GREATER:
                    if lookahead1Valid(i, word) and isLookAhead1This(i, TokenType.EQUAL, word): 
                        tokenType = TokenType.GREATER_EQUAL
                case TokenType.LESS:
                    if lookahead1Valid(i, word) and isLookAhead1This(i, TokenType.EQUAL, word): 
                        tokenType = TokenType.LESS_EQUAL
                case TokenType.SLASH:
                    if not lookahead1Valid(i, word) and not atEndOfLine:
                        tokenType = TokenType.DIVISION
                case TokenType.COMMENT:
                    self._discardMode = not self._stringMode
                    return
                case TokenType.QUOTES:
                    if lookahead1Valid(i, word) and isLookAhead1This(i, TokenType.QUOTES, word) and\
                    lookahead1Valid(i+1, word) and isLookAhead1This(i+1, TokenType.QUOTES, word):
                        self._setStatus(SyntaxError)
                        self._error("Multi line comments and strings are not supported at this moment.")
                        tokenType = None
                    else:
                        self._stringMode = not self._stringMode
                
            #print(f"token: {tokenType}")

            if self._stringMode:
                tokenType = TokenType.STRING
                self._addToken(tokenType, word[i], word[i])
            elif tokenType is None:
                self._error(f"Unexpected token {{{word[i]}}}")
                self._setStatus(StatusCodes.SYNTAX_ERROR)
            else:
                self._addToken(tokenType, word[i], word[i])
            i += 1 

    def _tokenizeLine(self, line:str) -> None:
        """
        Description:
            starts tokenization of a line.
        Usage:
            self._tokenize_line(<str>)
        """
        pattern = r'".*?"|[^"\s]+'
        words:list[str] = re.findall(pattern, line)

        for index, word in enumerate(words):
            self._scanTokenFromWord(word, index == len(words) - 1)
            if self._discardMode:
                self._discardMode = False
                return

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
            self._addToken(TokenType.EOL, '', '')

        if self.getStatus() is not StatusCodes.ERROR:
            self._setStatus(StatusCodes.SUCCESS)

