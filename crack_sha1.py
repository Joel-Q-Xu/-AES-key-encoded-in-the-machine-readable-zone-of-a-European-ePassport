import itertools
from hashlib import sha1
s=''
k=[('Q','q'),('W','w'),('%','5'),('(','8'),
          ('=','0'),('I','i'),('*','+'),('N','n')]
for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
            for d in range(0,2):
                for e in range(0,2):
                    for f in range(0,2):
                        for g in range(0,2):
                            for h in range(0,2):
                                s=k[0][a]+k[1][b]+k[2][c]+k[3][d]+k[4][e]+k[5][f]+k[6][g]+k[7][h]
                                for i in itertools.permutations(s):
                                    key=''.join(i)
                                    h=sha1(key.encode())
                                    if h.hexdigest()=='67ae1a64661ac8b4494666f58c4822408dd0a3e4':
                                        print(key)
                                        break
        
