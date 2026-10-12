"""
Access Log Analyser

Takes a morning's worth of web server log lines and reports on them:
how many requests each page received, which page was busiest, and
which requests failed.

Each line is: time, user, page, status code, separated by spaces.

This program already works. Operations now also want to know which
users are hitting errors, and which of them are hitting more than a
few. That part is not built yet: it is your job to add it, using the
functions already here rather than walking the log again yourself.
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
]


def count_by_page(lines):
    """Return a dictionary of page name to number of requests."""
    counts = {}
    for line in lines:
        page = line.split()[2]
        counts[page] = counts.get(page, 0) + 1
    return counts


def busiest_page(counts):
    """Return the name of the page with the most requests."""
    busiest = ""
    highest = 0
    for page, count in counts.items():
        if count > highest:
            highest = count
            busiest = page
    return busiest


def failed_requests(lines):
    """Return every line whose status code is not 200."""
    failures = []
    for line in lines:
        if line.split()[3] != "200":
            failures.append(line)
    return failures


def errors_by_user(lines):
    """Return a dictionary of user name to the number of requests that
    user made which did not return 200. A user who made no failed
    requests should not appear in the dictionary at all.

    Use failed_requests to get the lines you need; do not walk through
    LOG_LINES again yourself.
    """
    counts = {}
    failures = failed_requests(lines)
    for line in failures:
        user = line.split()[1]
        counts[user] = counts.get(user, 0) + 1
    return counts


def users_at_or_over(counts, threshold):
    """Return a list of every user name in counts whose count is at or
    above threshold."""
    users = []
    for user, count in counts.items():
        if count >= threshold:
            users.append(user)
    return users



page_counts = count_by_page(LOG_LINES)

print(f"{len(LOG_LINES)} requests, across {len(page_counts)} pages")
print("Requests per page:")
for page, count in page_counts.items():
    print(f"  {page}: {count}")

print(f"Busiest page: {busiest_page(page_counts)}")

failures = failed_requests(LOG_LINES)
print(f"Failed requests: {len(failures)}")
for line in failures:
    print(f"  {line}")

print("Errors by user:")
print(errors_by_user(LOG_LINES))

print("Users with two or more failures:")
print(users_at_or_over(errors_by_user(LOG_LINES), 2))
