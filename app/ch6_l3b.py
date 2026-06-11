# ─────────────────────────────────────────────────────────────────────────────
# ch6_l3b — Sorting Algorithms: Ordering Security Data
# Insert into OOSS_CHAPTER["lessons"] between ch6_l3 and ch6_l4
# ─────────────────────────────────────────────────────────────────────────────

CH6_L3B = {
    "id": "ch6_l3b",
    "title": "Sorting Algorithms — Ordering Security Data",
    "duration": "20 min",
    "objectives": [
        "Understand why sorting matters before searching in security tools",
        "Implement bubble sort, merge sort, and quicksort on security data",
        "Know which algorithm fits which job — and why quicksort wins in practice",
    ],
    "sections": [
        {
            "heading": "Why Sorting Matters in Security",
            "body": (
                "Binary search only works on sorted data. "
                "Threat intelligence feeds, blocklists, and log exports "
                "arrive unsorted. Before you can scan 1 million IPs in 20 checks "
                "instead of 1 million, you need to sort them first. "
                "Sorting is also how you surface the worst events fast — "
                "highest severity, most frequent attacker, latest timestamp. "
                "Three algorithms cover everything you'll encounter: "
                "bubble sort (understand it), merge sort (understand recursion in it), "
                "quicksort (use it)."
            ),
            "code": (
                "# unsorted threat feed — useless for binary search\n"
                'threats = ["192.168.1.99", "10.0.0.5", "172.16.0.3", "10.0.0.1"]\n'
                "\n"
                "# sorted — now binary search works in O(log n)\n"
                "threats.sort()\n"
                'print(threats)\n'
                "# [\'10.0.0.1\', \'10.0.0.5\', \'172.16.0.3\', \'192.168.1.99\']"
            ),
            "note": None,
        },
        {
            "heading": "Bubble Sort — Read It, Don't Ship It",
            "body": (
                "Bubble sort compares adjacent items and swaps them if they're out of order, "
                "repeating until the list is sorted. "
                "It's the slowest — O(n²) — but the most readable. "
                "You'll see it in every algorithms course because the logic is transparent. "
                "In security context: sorting a small list of alert severities "
                "to find the worst offender. "
                "Never use it on large datasets — on 10,000 log entries it makes "
                "100 million comparisons."
            ),
            "code": (
                "def bubble_sort(alerts):\n"
                '    """Sort alerts by severity — highest first."""\n'
                "    n = len(alerts)\n"
                "    for i in range(n - 1, 0, -1):\n"
                "        for j in range(i):\n"
                "            if alerts[j]['severity'] < alerts[j + 1]['severity']:\n"
                "                alerts[j], alerts[j + 1] = alerts[j + 1], alerts[j]\n"
                "\n"
                "alerts = [\n"
                '    {"ip": "10.0.0.3", "severity": 3, "event": "port scan"},\n'
                '    {"ip": "10.0.0.1", "severity": 9, "event": "brute force"},\n'
                '    {"ip": "10.0.0.4", "severity": 1, "event": "ping"},\n'
                '    {"ip": "10.0.0.2", "severity": 7, "event": "exploit attempt"},\n'
                "]\n"
                "\n"
                "bubble_sort(alerts)\n"
                "for a in alerts:\n"
                '    print(f"[{a[\'severity\']}] {a[\'ip\']} — {a[\'event\']}")'
            ),
            "note": "Output: severity 9 first, then 7, 3, 1 — worst threats surface to the top.",
        },
        {
            "heading": "Merge Sort — Recursion in Action",
            "body": (
                "Merge sort splits the list in half, sorts each half recursively, "
                "then merges them back in order. "
                "O(n log n) — much faster than bubble sort on large data. "
                "This is the algorithm where recursion actually earns its keep. "
                "Security use case: merging two sorted threat feeds from different sources "
                "into one unified sorted blocklist. "
                "The base case is a list of length 1 — already sorted, nothing to do."
            ),
            "code": (
                "def merge_sort(ip_list):\n"
                '    """Sort a list of IPs — works on any comparable type."""\n'
                "    if len(ip_list) <= 1:\n"
                "        return ip_list          # base case — already sorted\n"
                "\n"
                "    mid = len(ip_list) // 2\n"
                "    left  = merge_sort(ip_list[:mid])   # recursive case\n"
                "    right = merge_sort(ip_list[mid:])\n"
                "\n"
                "    # merge the two sorted halves\n"
                "    merged = []\n"
                "    i = j = 0\n"
                "    while i < len(left) and j < len(right):\n"
                "        if left[i] <= right[j]:\n"
                "            merged.append(left[i]); i += 1\n"
                "        else:\n"
                "            merged.append(right[j]); j += 1\n"
                "    merged.extend(left[i:])\n"
                "    merged.extend(right[j:])\n"
                "    return merged\n"
                "\n"
                "# two threat feeds arriving unsorted\n"
                'feed_a = ["10.0.0.9", "10.0.0.1", "172.16.0.5"]\n'
                'feed_b = ["10.0.0.3", "192.168.1.2", "10.0.0.7"]\n'
                "\n"
                "combined = merge_sort(feed_a + feed_b)\n"
                "print(combined)"
            ),
            "note": None,
        },
        {
            "heading": "Quicksort — The One You Actually Use",
            "body": (
                "Quicksort picks a pivot, moves everything smaller to the left "
                "and everything larger to the right, then recurses on each side. "
                "Average O(n log n) — in practice the fastest of the three. "
                "Python's built-in sorted() and list.sort() use a variant called Timsort "
                "which combines merge sort and insertion sort. "
                "Understanding quicksort tells you why sorted() is fast "
                "and when to reach for it instead of writing your own. "
                "Security use case: sorting a 50,000-entry blocklist before "
                "handing it to binary_search()."
            ),
            "code": (
                "def quicksort(ip_list):\n"
                '    """Sort IPs using quicksort — fast on large blocklists."""\n'
                "    if len(ip_list) <= 1:\n"
                "        return ip_list              # base case\n"
                "\n"
                "    pivot = ip_list[len(ip_list) // 2]\n"
                "    left   = [x for x in ip_list if x < pivot]\n"
                "    middle = [x for x in ip_list if x == pivot]\n"
                "    right  = [x for x in ip_list if x > pivot]\n"
                "\n"
                "    return quicksort(left) + middle + quicksort(right)\n"
                "\n"
                "blocklist = [\n"
                '    "10.0.0.9", "10.0.0.1", "172.16.0.5",\n'
                '    "10.0.0.3", "192.168.1.2", "10.0.0.7"\n'
                "]\n"
                "\n"
                "sorted_blocklist = quicksort(blocklist)\n"
                "print(sorted_blocklist)\n"
                "\n"
                "# now binary search works correctly\n"
                "def binary_search(ip_list, target):\n"
                "    low, high = 0, len(ip_list) - 1\n"
                "    while low <= high:\n"
                "        mid = (low + high) // 2\n"
                "        if ip_list[mid] == target: return True\n"
                "        elif ip_list[mid] < target: low = mid + 1\n"
                "        else: high = mid - 1\n"
                "    return False\n"
                "\n"
                'print(binary_search(sorted_blocklist, "172.16.0.5"))  # True\n'
                'print(binary_search(sorted_blocklist, "10.0.0.99"))   # False'
            ),
            "note": (
                "Real world: use sorted(blocklist) — Python's built-in is faster than "
                "any hand-written quicksort. Learn quicksort to understand why it works, "
                "then use the built-in."
            ),
        },
        {
            "heading": "Checking If Data Is Already Sorted",
            "body": (
                "Before sorting a large feed, check if it's already sorted — "
                "sorting a sorted list wastes time. "
                "is_sorted() scans pairs of adjacent items once — O(n). "
                "In a threat intel pipeline that runs every 5 minutes, "
                "skipping unnecessary sorts adds up."
            ),
            "code": (
                "def is_sorted(ip_list):\n"
                '    """Return True if list is already in ascending order."""\n'
                "    return all(\n"
                "        ip_list[i] <= ip_list[i + 1]\n"
                "        for i in range(len(ip_list) - 1)\n"
                "    )\n"
                "\n"
                'sorted_feed   = ["10.0.0.1", "10.0.0.5", "192.168.1.99"]\n'
                'unsorted_feed = ["10.0.0.5", "10.0.0.1", "192.168.1.99"]\n'
                "\n"
                "print(is_sorted(sorted_feed))    # True  — skip sort\n"
                "print(is_sorted(unsorted_feed))  # False — sort needed\n"
                "\n"
                "def prepare_blocklist(feed):\n"
                '    """Sort only if needed, then return ready for binary search."""\n'
                "    return feed if is_sorted(feed) else sorted(feed)\n"
                "\n"
                "ready = prepare_blocklist(unsorted_feed)\n"
                "print(ready)"
            ),
            "note": None,
        },
    ],
    "exercise": {
        "title": "Sort and Search a Threat Feed",
        "instruction": (
            "You receive an unsorted threat feed. "
            "Use is_sorted() to check if it needs sorting. "
            "If it does, sort it with quicksort(). "
            "Then use binary_search() to check three IPs: "
            "'10.0.0.7', '172.16.0.1', and '192.168.1.5'. "
            "Print BLOCKED or ALLOWED for each."
        ),
        "starter_code": (
            "def is_sorted(ip_list):\n"
            "    return all(\n"
            "        ip_list[i] <= ip_list[i + 1]\n"
            "        for i in range(len(ip_list) - 1)\n"
            "    )\n"
            "\n"
            "def quicksort(ip_list):\n"
            "    if len(ip_list) <= 1:\n"
            "        return ip_list\n"
            "    pivot  = ip_list[len(ip_list) // 2]\n"
            "    left   = [x for x in ip_list if x < pivot]\n"
            "    middle = [x for x in ip_list if x == pivot]\n"
            "    right  = [x for x in ip_list if x > pivot]\n"
            "    return quicksort(left) + middle + quicksort(right)\n"
            "\n"
            "def binary_search(ip_list, target):\n"
            "    low, high = 0, len(ip_list) - 1\n"
            "    while low <= high:\n"
            "        mid = (low + high) // 2\n"
            "        if ip_list[mid] == target: return True\n"
            "        elif ip_list[mid] < target: low = mid + 1\n"
            "        else: high = mid - 1\n"
            "    return False\n"
            "\n"
            "threat_feed = [\n"
            '    "10.0.0.9", "10.0.0.1", "172.16.0.5",\n'
            '    "10.0.0.7", "192.168.1.5", "10.0.0.3"\n'
            "]\n"
            "\n"
            "if not is_sorted(threat_feed):\n"
            "    threat_feed = quicksort(threat_feed)\n"
            "\n"
            'targets = ["10.0.0.7", "172.16.0.1", "192.168.1.5"]\n'
            "for ip in targets:\n"
            '    status = "BLOCKED" if binary_search(threat_feed, ip) else "ALLOWED"\n'
            '    print(f"{ip}: {status}")'
        ),
    },
}
