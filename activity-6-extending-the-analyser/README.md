# Activity 6: Extending the analyser

File: `log_analyser.py`

The same program, with two functions missing. Operations now want to know which
users are hitting errors, and which of them are hitting more than a few.

This activity is the same shape as this afternoon's assignment task: the
docstrings are the specification, the existing functions are there to be used,
and you are adding to a program that already works rather than starting one.

## Predict

Before writing anything, work out from the log by hand:

- Which users made a request that did not return 200, and how many each?
bob
chen
chen
- Which of them made two or more?
chen
Write both answers down. They are what your code has to produce.

## Run

Run the file as it stands. Both new functions return `None`, so the last two
lines of the report are wrong. That is the starting point, not a fault.

## Investigate

- `errors_by_user` is told to use `failed_requests` rather than walking the log
  again. Why does that matter? What breaks later if you ignore it?
- The docstring says a user with no failures should not appear in the dictionary
  at all. What would you have to do differently to make them appear with a zero?
- `users_at_or_over` says "at or above". Which comparison does that make it, and
  what changes if you pick the other one?

## Modify

Complete both functions.

- `errors_by_user` should give `{'bob': 1, 'chen': 2}`.
- `users_at_or_over` with a threshold of 2 should give `['chen']`.

Check both against what you worked out by hand before you run anything.

## Stretch

Optional, and only if both functions work. Add a function that reports the
busiest hour of the morning. The times are in the log already and you have
everything you need to get at them.
