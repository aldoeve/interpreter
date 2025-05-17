#----------------------------------------------------------
# This file is the lexer code.
#
# Date Modified: Sat May 17 12:38:24 AM CDT 2025
#----------------------------------------------------------

from util.myToken import TokenType, Token

class Lexer():
    """This class creates the bash code from a token list."""

    def __init__(self, tokens:list[Token]):
        self._tokens: list[Token] = tokens

    def transcribe(self):
        """
        Description:
            Prints out bash code.
        Usage:
            lexer.transcribe()
        """
        ouput: str = ""
        bashLine: str = ""
        flush: bool = False
        
        for token in self._tokens:

            match token.type:
                case TokenType.EOL:
                    flush = True
                    ouput += "\n"
                case _:
                    continue
            
            if flush: 
                ouput += bashLine
                flush = False

        print(ouput)