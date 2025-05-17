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
        self._vars: dict[Token] = {}

    def transcribe(self):
        """
        Description:
            Prints out bash code.
        Usage:
            lexer.transcribe()
        """
        output: str = ""
        bashLine: str = ""
        flush: bool = False
        totalListSize: int = len(self._tokens)
        next = lambda i: i + 1 
        fetchNextTokenType = lambda: self._tokens[next(i)].type

        for i, token in enumerate(self._tokens):
            match token.type:
                case TokenType.EOL:
                    flush = True
                    output += "\n"
                case TokenType.IDENTIFIER:
                    if i + 1 < totalListSize:
                        peek: TokenType = fetchNextTokenType()
                        if peek == TokenType.LEFT_BRACE: 
                            output += f"{token.literal}"
                

                case _:
                    continue
            
            if flush: 
                output += bashLine
                flush = False

        print(output)