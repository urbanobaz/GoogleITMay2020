#!/usr/bin/env python
import re

with open("receipt.txt") as file:
    for line in file:
        pattern = re.search(r"tel:\s(\(\d{3}\)\s\d{3}-\d{4})", line)
        if pattern != None:
            print(pattern.group(1))
