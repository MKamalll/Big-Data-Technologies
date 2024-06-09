## Task 1 Description
Write a program task1_c1.py using mrjob, which applies a function f of your choice to a
small input file of your choice without using a combiner. Also, write a program
task1_c2.py using mrjob, which applies f to the same input file and it uses a combiner. f
must be inappropriate for being used with a combiner.
Please comment your code appropriately to explain what each step does.
Provide the output of both programs and explain why the output of the second program
is incorrect. Your explanation should be detailed, taking into account the properties of
functions that can be used in a combiner.
Note: You can use redirection (e.g., python3 myprogram.py > myoutput.txt) to get the
output. You can execute the program in local mode (i.e., without -r hadoop).

## Task 1 Solution
Using _mrjob_ we created a program takes text file as an input and calculated avarage grade for each student. 
Currently program does not handle any errors.
The first version of the program is using mapper and reducer functions only. To test it works 

# Program not using combiner 
Program without the combiner is using mapper and reducer functions.
To execute the progrem run:
```python
python3 task1_c1.py student_grades.txt
```
The output of the program is:
![Alt text](output_c1.png)

If we use exceel sheet to validate the avarge was correctly calculated we can see it is the same:
![Alt text](check.png)

# Program using combiner
Program with the combiner is using mapper, combiner and reducer functions.

To execute the progrem run:
```python
python3 task1_c2.py student_grades.txt
```

The output of the program is:
![Alt text](output_c2.png)

Program with the combiner did not calculate the avarage correctly. 



