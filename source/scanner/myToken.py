#--------------------------------------------------------------------
# This file is the tokens enum.
#
# Date updated: Sun May 11 04:34:56 PM CDT 2025
#--------------------------------------------------------------------

from enum import Enum

class TokenType(Enum):
    # Single char
    LEFT_PAREN        = 0
    RIGHT_PAREN       = 1
    LEFT_BRACE        = 2
    RIGHT_BRACE       = 3
    COMMA             = 4
    DOT               = 5
    MINUS             = 6
    PLUS              = 7
    SEMICOLON         = 8
    COLON             = 9
    SLASH             = 10
    STAR              = 11
    # One or two chars
    IS                = 12
    NOT               = 13
    NOT_EQUAL         = 14
    EQUAL             = 15
    EQUAL_EQUAL       = 16
    GREATER           = 17
    GREATER_EQUAL     = 18
    LESS              = 19
    LESS_EQUAL        = 20
    # Literals
    IDENTIFIER        = 21
    STRING            = 22
    NUMBER            = 23
    # Keywords
    AND               = 24
    CLASS             = 25
    ELSE              = 26
    FALSE             = 27
    DEF               = 28
    FOR               = 29
    IF                = 30
    NONE              = 31
    OR                = 32
    PRINT             = 33
    RETURN            = 34
    SELF              = 35
    TRUE              = 36
    VAR               = 37
    WHILE             = 38
    EOF               = 39


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
        