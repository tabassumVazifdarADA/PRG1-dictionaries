# Activity 4: Broken dictionaries

File: `broken_dictionaries.py`

Three faults. Nothing crashes, and all three outputs look like they could be
right.

## Predict

Work out what each part **should** produce:

- The average grade of the five students on the class list
- Whether Kwame is registered, and whether Aisha is
- The dictionary after Aisha is given 61 and Kai is given 12

## Run

Execute it. All three are wrong.

## Investigate

- The class average comes out at 70.2. Work out the true average of the grades
  that actually exist. Why is the printed figure lower, and which is the correct
  answer to the question the function's name asks?




- `is_registered` returns False for Kwame, who is plainly in the dictionary.
  Read the line carefully. What is it searching, and what did the author think
  it was searching?


  
- Read the docstring on `record_grade`, then look at what happened to Kai. The
  code does something the docstring says it should not.

## Fault log

| # | What you saw | What was wrong | How you fixed it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Modify

Fix all three. You should get the average of the grades that exist, a correct
answer for both registration checks, and Kai's 96 left alone.

> The first fault is the one worth remembering. `.get(name, 0)` never complains,
> which is exactly what you want when a missing value really should count as
> zero, and exactly what you do not want when a missing value means somebody has
> made a mistake. The code cannot tell the difference. You have to.
