package lox_j;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import lox_j.TokenType.*;

class Scanner {
    private final String source;
    private final List<TokenType.Token> tokens = new ArrayList<>();

    Scanner(String source) {
        this.source = source;
    }
}