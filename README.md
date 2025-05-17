# Python to Bash transcompiler
## I was inspired by Dr.Crawley of Lipscomb University to look more into compilers and interpreters.
___
This repo holds the code for a simple transcompiler that will take python code and curn out bash code.
This transcompiler will not handle multi-line strings nor comments, will only handle very simple strings, no functions, no classes,
and only the funtion print is supported. Why was this done in python? For fun? Also add a space between = signs.

To use bash commands or any personal commands, call it like a function and give it the appopropriate parameters. For example,
neofetch() will write neofetch without any other parameters. rm('-r') will run rm with the -r flag. Note that the order of the parameters does matter.