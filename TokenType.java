package com.craftinginterpreters.lox;

enum TokenType {
    //single-character
    LEFT_PARAN, RIGHT_PARAN,
    LEFT_BRACE, RIGHT_BRACE,
    COMMA, DOT, MINUS, PLUS,
    SEMI, SLASH, STAR,
    
    //one or two character tokens
    BANG, BANG_EQ,
    EQ, EQ_EQ,
    GREATER, GREATER_EQ,
    LESS, LESS_EQ,

    //literals
    ID, STR, NUM,

    //keywords
    AND, CLASS, ELSE, FALSE, FUN, FOR,
    IF, NULL, OR, PRINT, RETURN,
    SUPER, THIS, TRUE, VAR, WHILE,

    EOF
}