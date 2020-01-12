# quizzer
A console-based program to practice with the ISO II questions. It will automatically load the files in the questions dir.
You can also load and specific file with the `-f` option.

Thanks to [Jaime León](https://github.com/jaimelr10) for adding all the questions files. I would like also to thanks [Enrique Cepeda](https://github.com/Equecevi) its contribution adding the questions of the last two units <3. 

To execute it (using preloaded files), in Linux:

```bash
python3 main.py
```

And in Windows:

```bash
py main.py
```

To load a file (only the file name):

```
python3 main.py -f <file>
```

The questions files should follow the next format:

```
Unit 1.1

What is the aim of the information systems?
Support the company business processes
Support computer-based system
Develop software engineering
Discover functional requirements

...
..
.
```
First line of the file the unit, space and then the question itself.
