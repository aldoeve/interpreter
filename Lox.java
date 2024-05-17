package jlox;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Scanner;

public class Lox {
  static boolean hadError = false;
  public static void main(String[] args) throws IOException {
    if (args.length > 1) {
      System.out.println("Usage: jlox [script]");
      System.exit(64); 
    } else if (args.length == 1) {
      runFile(args[0]);
    } else {
      runPrompt();
    }
  }

  //read from file
  private static void runFile(String path) throws IOException {
    byte[] bytes = Files.readAllBytes(Paths.get(path));
    run(new String(bytes, Charset.defaultCharset()));
    
    if(hadError) System.exit(65);
  }

  //read from stdin
  private static void runPrompt() throws IOException {
    InputStreamReader input = new InputStreamReader(System.in);
    BufferedReader reader   = new BufferedReader(input);

    while (true) {
      System.out.print("> ");
      String line = reader.readLine();
      if (line.compareTo(".quit") == 0) break;
      run(line);
      //point is to keep session going but still report error
      hadError = false;
    }
  }

  //tokenizes output and prints it
  private static void run(String source) {
    Scanner scanner = new Scanner(source);
    List<Token> tokens = scanner.scanTokens();

    for (Token token: tokens) {
      System.out.println(token);
    }
  }

  //quick attempt at error reporting
  static void error(int line, String msg) {
    report(line, "", msg);
  }

  private static void report(int line, String where, String msg){
    System.err.println("[line " + line + "] Error" + where + ": " + msg);
    hadError = true;
  }
}

