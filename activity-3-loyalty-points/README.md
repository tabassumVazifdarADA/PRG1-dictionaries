# Activity 3: Loyalty points

File: `loyalty_points.py`

A working program: a coffee shop takes a day's purchases and works out where
every customer stands at closing time.

## Predict

- How many customers are in the dictionary when the program starts, and how many
3
4
  when it ends?
- What are alice's, bob's and siobhan's totals at the end?

160
100
207
- Which tier does each customer land in?
bronze
bronze
silver




## Run

Execute and compare. Check the totals by hand if any of your predictions were
wrong.

## Investigate

- `points.get(name, 0) + amount` does two different jobs depending on whether
  the customer is already known. Describe both.
- chen was not in the dictionary at the start and is in it at the end. Which
  single line put them there? Nothing in this program explicitly creates a new
  customer, so what did?
  get line
- bob finishes on exactly 100, which is the bronze threshold. Which tier does he
  get, and which character in `tier` decides that? This is the fourth time this
  week you have met a boundary decided by one character.
  >=
- `points.items()` gives you the name and the total together. What would you have
  had to write instead if you only had the names?

  

## Modify

- Award double points on any purchase of 50 or more.
- Report how many customers finished in each tier.
- Add a Gold tier at 250 and predict who moves before you run it.
