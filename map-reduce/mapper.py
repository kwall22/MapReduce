#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Strip any whitespace and split the line into words (years)
    years = line.strip().split()
    
    # Output each year
    for year in years:
        print(year)

