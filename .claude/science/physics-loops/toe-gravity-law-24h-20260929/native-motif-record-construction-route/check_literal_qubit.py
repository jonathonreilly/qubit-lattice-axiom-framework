"""Exact finite-support native-qubit controls; no imported operator builder."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from pathlib import Path
import hashlib,json,time,resource
started=time.process_time(); here=Path(__file__).resolve().parent
axes=((1,0,0),(0,1,0),(0,0,1))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(a,s):return tuple(s*x for x in a)
def dist(a,b):return max(abs(x-y) for x,y in zip(a,b))
D=set()
for e in axes:
 for s in (-1,1):D.add(scale(e,2*s))
for i in range(3):
 for j in range(i+1,3):
  for s,t in product((-1,1),repeat=2):D.add(add(scale(axes[i],s),scale(axes[j],t)))
def families(c):
 ep=[frozenset((add(c,e),add(c,scale(e,-1)))) for e in axes]
 out=[(ep,[[F(int(i==j))-F(1,3) for j in range(3)] for i in range(3)],2)]
 for i in range(3):
  for j in range(i+1,3):
   st=list(product((-1,1),repeat=2)); ps=[frozenset((add(c,scale(axes[i],s)),add(c,scale(axes[j],t)))) for s,t in st]
   out.append((ps,[[F(s*t*u*v,4) for u,v in st] for s,t in st],1))
 return out
def action(word,mu,tau):
 out=defaultdict(F);n=len(word)
 out[word]+=mu*n
 for x in word:
  m=sum(add(x,d) in word for d in D);out[word]+=mu*m*(m-1)//2
 centers={add(x,scale(e,s)) for x in word for e in axes for s in (-1,1)}
 for c in centers:
  cf=families(c)
  for group,(ann,G,attr) in enumerate(cf):
   for i,p in enumerate(ann):
    if not p<=word:continue
    rem=word-p
    choices=[(c,6*tau-attr*mu)]+[(add(c,scale(e,s)),-tau) for e in axes for s in (-1,1)]
    for y,coef in choices:
     if not coef:continue
     create=families(y)[group][0]
     for j,q in enumerate(create):
      if q & rem:continue
      out[frozenset(rem|q)]+=coef*G[j][i]
 return {w:v for w,v in out.items() if v}
def markers(word):return frozenset(x for x in word if all(x==y or dist(x,y)>2 for y in word))
def pinched(word,mu,tau):return {w:a for w,a in action(word,mu,tau).items() if markers(w)==markers(word)}
def linear_action(psi,mu,tau,changed=False):
 out=defaultdict(F)
 for w,a in psi.items():
  for z,b in (pinched if changed else action)(w,mu,tau).items():out[z]+=a*b
 return {w:a for w,a in out.items() if a}
def birth(word,x):
 if any(dist(x,y)<=2 for y in word):return None
 return frozenset(word|{x})
I=frozenset(((0,0,0),(2,0,0),(4,0,0)));O=frozenset(((0,0,0),(3,0,0),(5,0,0)))
assert action(I,1,0).get(O,F(0))==0
assert action(I,0,1)[O]==F(-2,3)
assert O not in pinched(I,0,1)
assert markers(I)==frozenset() and markers(O)==frozenset(((0,0,0),))
psi=defaultdict(int)
for x in product((-1,0,1),repeat=3):
 weight=1
 for z in x:weight*=2 if z==0 else 1
 for i,sgn in ((0,1),(1,-1)):
  q=frozenset((add(x,axes[i]),add(x,scale(axes[i],-1))))
  psi[q]+=sgn*weight
psi={w:a for w,a in psi.items() if a};norm=sum(a*a for a in psi.values())
assert norm==432
assert linear_action(psi,1,0)=={}
tauvec=linear_action(psi,0,1)
energy=sum(F(a)*tauvec.get(w,0) for w,a in psi.items())
assert energy==864 and energy/norm==2
assert tauvec==linear_action(psi,0,1,changed=True)
assert all(not markers(w) for w in psi)
old=frozenset(((0,0,0),))
assert action(old,1,0)=={old:F(1)} and action(old,0,1)=={}
for x in ((1,0,0),(2,2,2)):
 assert birth(old,x) is None
new=birth(old,(3,0,0));assert new is not None and markers(new)==new
assert len(new)-len(markers(new))==len(old)-len(markers(old))
for m in range(19):assert F((m-1)*(m-2),2)+F(m,3)>=F(1,3)
result={'controls':[{'name':'literal changed-law four-flip','mu':0,'tau':'-2/3','pinched':0,'original_output_terms':len(action(I,0,1)),'preserved_output_terms':len(pinched(I,0,1))},{'name':'actual hard-core pair packet','states':len(psi),'norm_squared':norm,'mu_action_zero':True,'tau_numerator':str(energy),'tau_energy':str(energy/norm),'full_output_terms':len(tauvec),'new_law_same_action':True},{'name':'overlapping-collar original birth','blocked_distances':[1,2],'allowed_distance':3,'old_markers_preserved':True},{'name':'diagonal quantum discriminator','integer_degrees':19,'minimum':'1/3'}],'TOTAL':{'PASS':4,'FAIL':0},'scope':'Finite exact controls only. No all-volume proof, dynamical simulation, phase or framework-law claim.','cpu_seconds':time.process_time()-started,'peak_RSS_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(here/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
