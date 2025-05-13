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
    DIVISION          = 12
    BANG              = 13
    # One or two chars
    IS                = 14
    NOT               = 15
    NOT_EQUAL         = 16
    EQUAL             = 17
    EQUAL_EQUAL       = 18
    GREATER           = 19
    GREATER_EQUAL     = 20
    LESS              = 21
    LESS_EQUAL        = 22
    # Literals
    IDENTIFIER        = 23
    STRING            = 24
    NUMBER            = 25
    # Keywords
    AND               = 26
    CLASS             = 27
    ELSE              = 28
    FALSE             = 29
    DEF               = 30
    FOR               = 31
    IF                = 32
    NONE              = 33
    OR                = 34
    PRINT             = 35
    RETURN            = 36
    SELF              = 37
    TRUE              = 38
    WHILE             = 39
    EOF               = 40
    ELSE_IF           = 41
    QUOTES            = 42
    COMMENT           = 43
    LONG_COMMENT      = 44


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
        