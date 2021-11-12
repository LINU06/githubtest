import re

pattern = '^Q...3$'
test_string = 'Qwerty@123'
result = re.match(pattern, test_string)

if result:
  print("True")
else:
  print("False")	