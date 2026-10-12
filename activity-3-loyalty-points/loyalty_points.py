"""
Loyalty Points

A coffee shop awards points on every purchase. This program takes a
day's purchases and works out where everybody stands at closing time.
"""

BRONZE_THRESHOLD = 100
SILVER_THRESHOLD = 200
GOLD_THRESHOLD = 250
DOUBLE_POINTS = 2

points = {
    "alice": 220,
    "bob": 40,
    "siobhan": 195
}

purchases = [
    ("alice", 30),
    ("chen", 15),
    ("bob", 60),
    ("alice", 10),
    ("siobhan", 12)
]


tier_members = {
    "Standard": 0,
    "Bronze": 0,
    "Silver": 0,
    "Gold": 0
}

def award_points(points, purchases):
    for name, amount in purchases:
        if amount >= 50:
            points[name] = (points.get(name, 0)) +  DOUBLE_POINTS*amount
        else:
            points[name] = points.get(name, 0) + amount


def tier(total):
    if total >= GOLD_THRESHOLD:
        return "Gold"
    elif total >= SILVER_THRESHOLD:
        return "Silver"
    elif total >= BRONZE_THRESHOLD:
        return "Bronze"
    else:
        return "Standard"







print(f"Customers at open: {len(points)}")

award_points(points, purchases)

print(f"Customers at close: {len(points)}")
print("End of day standings:")
for name, total in points.items():
    print(f"  {name}: {total} points, {tier(total)}")


# for name in points:
#     print(f"  {name}: {points[name]} points, {tier(points[name])}")


# for total in points:


# for points in tier(total):
for total in points.values():
    tier_members[tier(total)] += 1

# for 
#     print(f" {tier_members.keys()}:  {tier_members[]} " [tier])


print("\nCustomers in each tier:")
for tier_member, count in tier_members.items():
    print(f"{tier_member}: {count}")