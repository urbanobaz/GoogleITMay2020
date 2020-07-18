#!/usr/bin/env python3
import re

with open('receipt.txt') as file:
    
    for line in file:
        pattern = re.search(r"tel: (\(\d{3}\)\s\d{3}-\d{4})",line)
        if pattern != None:
            print(pattern.group(1))
    

