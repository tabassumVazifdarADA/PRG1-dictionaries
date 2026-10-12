"""
Access Log Analyser

Takes a morning's worth of web server log lines and reports on them:
how many requests each page received, which page was busiest, and
which requests failed.

Each line is: time, user, page, status code, separated by spaces.
"""

LOG_LINES = [
    "09:02 alice /home 200",
    "09:04 bob /home 200",
    "09:05 alice /basket 200",
    "09:07 chen /home 200",
    "09:11 bob /checkout 500",
    "09:14 alice /checkout 200",
    "09:15 chen /basket 404",
    "09:19 dara /home 200",
    "09:21 bob /home 200",
    "09:24 chen /checkout 500"
    "10:45 bob/checkout 200"

]


def count_by_page(lines):
    """Return a dictionary of page name to number of requests."""
    counts = {}
    for line in lines:
        page = line.split()[2]
        counts[page] = counts.get(page, 0) + 1
    return counts



def count_by_user(lines):
    """Return a dictionary of number of users to number of requests."""
    counts = {}
    for line in lines:
        user = line.split()[1]
        counts[user] = counts.get(user, 0) + 1
    return counts

def busiest_page(counts):
    """Return the name of the page with the most requests."""
    busiest = ""
    highest = 0
    for page, count in counts.items():
        if count > highest:
            highest = count
            busiest = page
    return busiest, highest


def quitest_page(counts):
    quitest = ""
    
    lowest = 0

    for page, count in counts.items():
            if lowest is 0  or count < lowest:
                lowest = count
                quietest = page
    return quietest
    

    

def failed_requests(lines):
    """Return every line whose status code is not 200."""
    failures = []
    for line in lines:
        if line.split()[3] != "200":
            failures.append(line)
    return failures

# def count_users(lines, counts):
   
#     for line in lines:
#         page = lines.split()[1]
#         if lines [page] = lines.get(page, 0 )
#         num_page = len(counts)
#     return (lines.get()), num_page
    

page_counts = count_by_page(LOG_LINES)

print(f"{len(LOG_LINES)} requests, across {len(page_counts)} pages")
print("Requests per page:")
for page, count in page_counts.items():
    print(f"  {page}: {count}")

print(f"Busiest page: {busiest_page(page_counts)}")

print(f"Quietest page: {quitest_page(page_counts)}")

failures = failed_requests(LOG_LINES)
print(f"Failed requests: {len(failures)}")
for line in failures:
    print(f"  {line}")

users = count_by_user(LOG_LINES)
print(users)
print(f"Number of users: {len(users)}")
# for line in users:
#     print(f"  {line}: {count}")
