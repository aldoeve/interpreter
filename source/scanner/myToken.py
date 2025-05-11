#--------------------------------------------------------------------
# This file is the tokens enum.
#
# Date updated: Sun May 11 04:34:56 PM CDT 2025
#--------------------------------------------------------------------

from enum import Enum

class TokenType(Enum):
    # Single char
    LEFT_PARAM        = 0
    RIGHT_PARAM       = 1
    LEFT_BRACE        = 2
    RIGHT_BRACE       = 3
    COMMA             = 4
    DOT               = 5
    MINUS             = 6
    PLUS              = 7
    SEMICOLON         = 8
    SLASH             = 9
    STAR              = 10
    # One or two chars
    BANG              = 11
    BANG_EQUAL        = 12
    EQUAL             = 13
    EQUAL_EQUAL       = 14
    GREATER           = 15
    GREATER_EQUAL     = 16
    LESS              = 17
    LESS_EQUAL        = 18
    # Literals
    IDENTIFIER        = 19
    STRING            = 20
    NUMBER            = 21
    # Keywords
    AND               = 22
    CLASS             = 23
    ELSE              = 24
    FALSE             = 25
    DEF               = 26
    FOR               = 27
    IF                = 28
    NONE              = 29
    OR                = 30
    PRINT             = 31
    RETURN            = 32
    SELF              = 33
    TRUE              = 34
    VAR               = 35
    WHILE             = 37
    EOF               = 38


class Token():
    """
    Description:
        This class make a simple object to store token information.
    """
    def __init__(self, tokenType: TokenType, lexeme: str, literal: object, line:int):
        self.type: TokenType = tokenType
        self.lexeme: str = lexeme
        self.literal: object = literal
        self.line: int = line

    def dump(self) -> str:
        """
        Description:
            Dumps a tokens information as a string.
        Usage:
            stringy = self.dump()
        """
        return f"{self.type.value} {self.lexeme} {self.literal} {self.line}"
        