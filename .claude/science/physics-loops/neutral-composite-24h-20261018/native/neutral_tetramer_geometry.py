from itertools import combinations,product
from collections import Counter
import json,time

def count(s,p):
 a=set()
 for dx,dy in p:a^={(x-dx,y-dy) for x,y in s}
 return len(a)
box={(0,0),(1,0),(0,1),(1,1)}
patternsA=[[(0,0),(1,0),(2,0)],[(0,0),(0,1),(0,2)],box]
patternsB=[box-{p} for p in box]
patternsD=[[(0,0),(1,1)],[(0,1),(1,0)]]
def energy(s):return 2*(729*sum(count(s,p) for p in patternsA)-405*sum(count(s,p) for p in patternsB)-464*sum(count(s,p) for p in patternsD))
def syn(c):
 s=set()
 for x,y in c:s^={(x,y),(x-1,y),(x,y-1),(x-1,y-1)}
 return s
def cols(s):
 out=set()
 for x in range(min(a for a,b in s),max(a for a,b in s)):
  for y in range(min(b for a,b in s),max(b for a,b in s)):
   if sum(a<=x and b<=y for a,b in s)%2:out.add((x+1,y+1))
 return out
ref=syn({(0,0),(1,0),(10,10),(11,10)});target=energy(ref)
def scan():
 rows=[];negative=[];hist=Counter();tested=0;t=time.time()
 for nr in range(2,5):
  for nc in range(2,5):
   pats=[]
   for C in combinations(range(nr*nc),8):
    P=[divmod(k,nc) for k in C]
    if all(sum(x==i for x,y in P)>0 and sum(x==i for x,y in P)%2==0 for i in range(nr)) and all(sum(y==j for x,y in P)>0 and sum(y==j for x,y in P)%2==0 for j in range(nc)):pats.append(P)
   for P in pats:
    for gaps in product([1,2,3,4],repeat=nr+nc-2):
     xs=[0];ys=[0]
     for g in gaps[:nr-1]:xs.append(xs[-1]+g)
     for g in gaps[nr-1:]:ys.append(ys[-1]+g)
     S={(xs[x],ys[y]) for x,y in P}
     adjacency=sum((x+1,y) in S for x,y in S)+sum((x,y+1) in S for x,y in S)
     if adjacency!=4:continue
     if sum(x*y for x,y in S)%2:continue
     tested+=1;E=energy(S)-target;hist[E]+=1
     if E<0:negative.append(dict(energy=E,syndrome=sorted(S),columns=sorted(cols(S)),gaps=gaps))
     if E==0 and len(rows)<80:rows.append(dict(syndrome=sorted(S),columns=sorted(cols(S)),nr=nr,nc=nc,gaps=gaps))
 return dict(scope='Exposed finite gap-type enumeration; proof of completeness pending; energies integer units JLlambda8/21233664',reference=target,tested=tested,seconds=time.time()-t,histogram=dict(sorted(hist.items())),threshold_examples=rows,negative_examples=negative)

if __name__=='__main__':
 print(json.dumps(scan(),indent=2))
