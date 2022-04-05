import re
txt='''hi shubhodeep 1103'''
mail='''shubho1103@gmail.com
shubho1103git@gmail.com
sarkar.shubhodeep09@gmail.com'''

x=re.compile(r'([a-zA-Z0-9]+)@([a-zA-Z]+)(\.\w+)')
matches=x.finditer(mail)
for i in matches:
    print("DNS:",i.group(1),"   host:",i.group(2))
  
