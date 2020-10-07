#Manuel Duran 1584885
password = input("")
new_password = ""

for c in password:
   if c == 'i':
       new_password = new_password + '!'

   elif c == 'a':
       new_password = new_password + '@'

   elif c == 'm':
       new_password = new_password + 'M'

   elif c == 'B':
       new_password = new_password + '8'

   elif c == 'o':
       new_password = new_password + '.'

   else:
       new_password = new_password + c

new_password = new_password + "q*s"
print("" + new_password + "")