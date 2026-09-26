"""Primary finite-support integer words on Z^3. No rotor truncation.
Projected off-diagonal paths only; scalar vacuum subtraction is separate.
"""
from collections import Counter
from functools import lru_cache
from itertools import product

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def even(a):return sum(a)%2==0
DIRS=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
@lru_cache(None)
def nb(a):return tuple(add(a,x) for x in DIRS)
@lru_cache(None)
def partners(a):return tuple(sorted({c for b in nb(a) for c in nb(b) if c!=a}))
def default(v):return int(even(v))
def charge(q,v):return q.get(v,default(v))
def pack(q,e):return tuple(sorted((v,x) for v,x in q.items() if x!=default(v))),tuple(sorted((ab,x) for ab,x in e.items() if x))
def unpack(s):return dict(s[0]),dict(s[1])
OMEGA=((),())
def gauss(s):
 q,e=unpack(s);d=Counter()
 for (a,b),x in e.items():d[a]+=x;d[b]-=x
 return all(d[v]==charge(q,v)-default(v) for v in set(q)|set(d))
def cost(s):
 q,e=unpack(s)
 return sum(x*(x-charge(q,a)) for (a,b),x in e.items() if charge(q,b)==0)
def outgoing(s,a):
 q,e=unpack(s);qa=charge(q,a)
 if not qa:return []
 out=[]
 for b in nb(a):
  if charge(q,b):continue
  qq=q.copy();ee=e.copy();qq[a]=0;qq[b]=qa;ee[a,b]=ee.get((a,b),0)-qa
  out.append((pack(qq,ee),(a,b,qa)))
 return out

def incoming(s,a):
 q,e=unpack(s)
 if charge(q,a):return []
 out=[]
 for b in nb(a):
  qb=charge(q,b)
  if not qb:continue
  qq=q.copy();ee=e.copy();qq[a]=qb;qq[b]=0;ee[a,b]=ee.get((a,b),0)+qb
  out.append((pack(qq,ee),(a,b,qb)))
 return out

def born(s,a,b,sig):
 q,e=unpack(s)
 if charge(q,a) or charge(q,b):return None
 qq=q.copy();ee=e.copy();qq[a]=sig;qq[b]=-sig;ee[a,b]=ee.get((a,b),0)+sig
 return pack(qq,ee)
def jump(s,a,b,sig):
 out=Counter()
 for t,_ in outgoing(s,a):
  y=born(t,a,b,sig)
  if y is not None:out[y]+=1
 return out

def relevant_pairs(s):
 q,e=unpack(s);verts=set(q)|{v for ab in e for v in ab};aa={v for v in verts if even(v)}
 for b in verts:
  if not even(b):aa.update(nb(b))
 return tuple(sorted({tuple(sorted((a,c))) for a in aa for c in partners(a)}))

def projected_offdiag(s,target=None,one_witness=False):
 out=Counter();witness={}
 for a,c in relevant_pairs(s):
  for t,p1 in outgoing(s,a):
   for u,p2 in outgoing(t,c):
    for v,p3 in incoming(u,c):
     for w,p4 in incoming(v,a):
      if w==s or (target is not None and w!=target) or cost(w):continue
      out[w]-=2
      if w not in witness:witness[w]=(a,c,p1,p2,p3,p4)
      if one_witness:return out,witness
 return out,witness

def translate(s,d):
 q,e=unpack(s)
 assert even(d)
 return pack({add(v,d):x for v,x in q.items()},{(add(a,d),add(b,d)):x for (a,b),x in e.items()})
def star_state(a,b,c):
 return pack({a:-1,b:1,c:1},{(a,b):-1,(a,c):-1})
