import re
txt="the sun and moon"
x=re.search("\s",txt)
print("first whitw space after ",x.start())
