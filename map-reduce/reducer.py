#!/usr/bin/env python3
import sys

min_year = None
max_year = None
sum_years = 0
count = 0

for line in sys.stdin:
    year = int(line.strip())
    
    if min_year is None or year < min_year:
        min_year = year
    if max_year is None or year > max_year:
        max_year = year
    
    sum_years += year
    count += 1

average = sum_years / count if count != 0 else 0

print(f"Min: {min_year}")
print(f"Max: {max_year}")
print(f"Count: {count}")
print(f"Average: {average:.2f}")

