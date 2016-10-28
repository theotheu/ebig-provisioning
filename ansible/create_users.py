import string
import random
import crypt
char_set = string.ascii_lowercase +string.ascii_uppercase + string.digits

users=["user1","user2","user3","...","usern"]

password=[]

print ">>>> BEGIN Python script"

for user in users:
    pwd=''.join(random.sample(char_set*16, 16))
    password.append(pwd)
    ansiblePwd=crypt.crypt(pwd, "$1$SomeSalt$")
    print "- user: name=%s password=%s state=present shell=/bin/bash" % (user, ansiblePwd)

print "<<<<< End Python script"


i=0
for user in users:
    print user, password[i]
    i=i+1
