# Activity 1: Looking something up

File: `grades_lookup.py`

A dictionary of names and grades, and four attempts to get something out of it.

## Predict

Write down what each of the four `print` lines produces, in order. One of them
does not produce a line of output at all. Work out which, and what happens
instead.
92
not found
85
none

## Run

Execute it and compare.

## Investigate

- Line 8 and line 9 both ask for something out of the dictionary, and they
  behave completely differently when the name is not there. Describe the
  difference in one sentence.

- `student_grades["Aisha"]` stopped the program. `student_grades.get("Aisha", "Not found")` did not. Which would you want in a program that has to keep running,
  and which would you want while you are still building it?
- Read the error message on the last line properly. What exactly does it tell
  you, and what does it not tell you?
  key error
  that key does not exist

## Modify

- Make the last line report a missing student without stopping the program.
- Add a fifth student, then print their grade.
- Change one of the existing grades. How many lines did you have to touch?
