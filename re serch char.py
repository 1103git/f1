import re
txt ="hi shubhodeep"
x=re.findall("[sh]",txt)
if x:
    print("match found")
