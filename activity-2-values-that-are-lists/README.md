# Activity 2: When the value is a list

File: `exam_results.py`

The same structure, except each value is a list of three marks rather than a
single number.

## Predict

Five lines of output. Write them all down before running. The fourth and fifth
are the ones to think hardest about.
99 98 95
99
3
98
error/ none

## Run

Execute and compare.

last 2:
true
false

## Investigate

- `exam_results["steve"]` and `exam_results["steve"][0]` differ by four
  characters and return different kinds of thing. Say out loud, left to right,
  what the second one is asking for.
- `len(exam_results["steve"])` gives 3. What would `len(exam_results)` give?
  Predict, then check.
3

- The last two lines both use `in`, and one is True while the other is False.
  What is `in` actually searching, and what would `"steve" in exam_results` do
  instead?
if that value is in the dictionary/  key


## Modify

- Print aqil's second mark.
- Print the total of violet's three marks.
- Add a fourth student with three marks, then print how many students there are.

> Everything you learned about lists yesterday still applies here. The only new
> thing is that you reach the list through a name rather than a position.
