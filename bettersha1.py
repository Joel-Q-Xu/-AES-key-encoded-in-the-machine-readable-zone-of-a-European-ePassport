import itertools
from hashlib import sha1
s=''
k=[('Q','q'),('W','w'),('%','5'),('(','8'),
          ('=','0'),('I','i'),('*','+'),('N','n')]
for item in itertools.product(k[0],k[1],k[2],k[3],k[4],k[5],k[6],k[7]):
    s=''.join(item)
    for i in itertools.permutations(s):
        key=''.join(i)
        h=sha1(key.encode())
        if h.hexdigest()=='67ae1a64661ac8b4494666f58c4822408dd0a3e4':
            print(key)
            break                                 
        
