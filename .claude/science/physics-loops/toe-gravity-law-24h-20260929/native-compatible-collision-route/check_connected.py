#!/usr/bin/env python3
"""Author finite occupation-word control; no imported campaign assembly."""
from itertools import combinations,product
from functools import lru_cache
from collections import defaultdict
import json,time,resource
E=((1,0,0),(0,1,0),(0,0,1));Z=(0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(s,a):return tuple(s*x for x in a)
def sub(a,b):return add(a,scale(-1,b))
G={scale(s*2,e) for e in E for s in (-1,1)}|{add(scale(s,E[i]),scale(t,E[j])) for i in range(3) for j in range(i+1,3) for s,t in product((-1,1),repeat=2)}
def weight(a,b):
 d=sub(b,a)
 if d in (scale(2,E[0]),scale(-2,E[0])):return 1
 if d in (scale(2,E[1]),scale(-2,E[1])):return -1
 return 0
@lru_cache(maxsize=12000)
def haf(S):
 if not S:return 1
 a=S[0];ans=0
 for j,b in enumerate(S[1:],1):
  w=weight(a,b)
  if w:ans+=w*haf(S[1:j]+S[j+1:])
 return ans

def local_words(c,family):
 if family[0]=='a':
  return [(tuple(sorted((sub(c,E[i]),add(c,E[i])))),i) for i in range(3)]
 i,j=family[1:]
 return [(tuple(sorted((add(c,scale(s,E[i])),add(c,scale(t,E[j]))))),s*t) for s,t in product((-1,1),repeat=2)]
def appearances(pair):
 a,b=pair;ans=[]
 for i in range(3):
  for s in (-1,1):
   c=add(a,scale(s,E[i]));u=sub(a,c);v=sub(b,c)
   if v==scale(-1,u):ans.append((c,('a',),i));continue
   for j in range(3):
    if i==j:continue
    for t in (-1,1):
     if v==scale(t,E[j]):ans.append((c,('p',min(i,j),max(i,j)),-s*t))
 return ans

def action12(S,mu=1,tau=1):
 # Literal12H: onsite and all true-neighbor triples, then collective pair words.
 S=set(S);out=defaultdict(int)
 out[tuple(sorted(S))]+=12*mu*(len(S)+sum(sum(sub(y,x) in G for y in S if y!=x)*(sum(sub(y,x) in G for y in S if y!=x)-1)//2 for x in S))
 for pair in combinations(sorted(S),2):
  rem=S-set(pair)
  for c,fam,idx in appearances(pair):
   centers=[(c,6*tau-(2 if fam[0]=='a' else 1)*mu)]+[(add(c,scale(s,e)),-tau) for e in E for s in (-1,1)]
   for target,factor in centers:
    for new,jdx in local_words(target,fam):
     if set(new)&rem:continue
     coeff=factor*((12*(idx==jdx)-4) if fam[0]=='a' else 3*idx*jdx)
     out[tuple(sorted(rem|set(new)))]+=coeff
 return {S:v for S,v in out.items() if v}
@lru_cache(maxsize=4000)
def energy_source(S):return sum(c*haf(T) for T,c in action12(S).items())
@lru_cache(maxsize=4000)
def connected(S):
 # Coefficients of e^(-C) H12 e^C Omega, evaluated on actual distinct-site sets.
 ans=energy_source(S)
 if len(S)<4:return ans
 for m in range(2,len(S),2):
  for I in combinations(range(len(S)),m):
   T=tuple(S[i] for i in I);comp=tuple(x for i,x in enumerate(S) if i not in I)
   h=haf(comp)
   if h:ans-=connected(T)*h
 return ans

def main():
 started=time.monotonic();usage0=resource.getrusage(resource.RUSAGE_SELF)
 # Direct local one-pair zero equation in all nine actual forward orientations.
 forward=[scale(2,e) for e in E]+[add(E[i],scale(s,E[j])) for i in range(3) for j in range(i+1,3) for s in (-1,1)]
 zero=[energy_source(tuple(sorted((Z,d)))) for d in forward];assert zero==[0]*9
 # Fully localized patterns; no finite torus or periodic alias assumption.
 S6=tuple(sorted([(-2,0,0),(0,0,0),(2,0,0),(4,0,0),(0,2,0),(0,4,0)]))
 S8=tuple(sorted([(0,-1,0),(0,1,0),(-1,0,0),(1,0,0),(-1,-2,0),(-1,2,0),(1,-2,0),(1,2,0)]))
 S10=tuple(sorted(S8+((-3,0,0),(3,0,0))))
 samples=[]
 for S in [S6,S8,S10]:
  samples.append({'sites':S,'pairs':len(S)//2,'incoming_hafnian':haf(S),'H12_incoming':energy_source(S),'connected_H12':connected(S)})
 # The exact fifth connected creation source vanishes by the local nilpotence theorem.
 assert samples[-1]['connected_H12']==0
 # Nontrivial literal Hermiticity controls across transitions in all fixtures.
 herm=0
 for S in [S6,S8]:
  items=list(action12(S).items())
  for T,c in items[::max(1,len(items)//12)]:
   assert action12(T).get(S,0)==c;herm+=1
 result={'scope':'exact author occupation controls, not a many-body lower proof','couplings':{'mu':1,'tau':1},'normalization':'H12=12H; raw uniform creator axial weights(1,-1,0), triplet0','one_pair_zero_entries':zero,'samples':samples,'literal_hermiticity_entries':herm,'cache_sizes':{'haf':haf.cache_info()._asdict(),'source':energy_source.cache_info()._asdict(),'connected':connected.cache_info()._asdict()},'resources':{'wall_seconds':time.monotonic()-started,'cpu_seconds':resource.getrusage(resource.RUSAGE_SELF).ru_utime+resource.getrusage(resource.RUSAGE_SELF).ru_stime-usage0.ru_utime-usage0.ru_stime,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}}
 print(json.dumps(result,indent=2));print('TOTAL: PASS=3 FAIL=0')
if __name__=='__main__':main()
