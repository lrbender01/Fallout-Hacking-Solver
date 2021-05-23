# Fallout-Hacking-Solver

Python script to solve the hacking minigame in Fallout 3, Fallout New Vegas, Fallout 4, and Fallout 76 given file with all possible choices as argument. I haven't been able to find a single instance of the minigame for which this solver does not work, please let me know if you do.

Invocation:
```
solver.py <FILE>
```

I've also included a sample .bat file for windows users. Simply replace all of the fields inside the file with the appropriate absolute file paths on your machine and double click to run. This lets you reuse the same input file every time rather than reinvoking the script with a new one each time. 

The examples folder contains 12 example input files with the file name indicating the "correct" answer. The bash script test.sh will test all of them one at a time using solver.py and user input.

Written by Luke Bender (lrbender01@gmail.com) in January 2021.