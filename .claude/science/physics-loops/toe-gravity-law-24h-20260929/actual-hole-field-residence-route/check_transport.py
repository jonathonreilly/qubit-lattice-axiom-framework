#!/usr/bin/env python3
"""Exact finite word control; no imported author action helper."""
import json, os, time
from collections import defaultdict
from pathlib import Path
L=16
D=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
def v(x): return tuple(i%L for i in x)
def add(x,d): return v(tuple(a+b for a,b in zip(x,d)))
def nei(x): return [add(x,d) for d in D]
def dist(x,y): return sum(min((a-b)%L,(b-a)%L) for a,b in zip(x,y))
def parity(x): return sum(x)%2
# A occupancy/charge deviations from +1; B charges; A-to-B fields.
def key(A,B,E): return (tuple(sorted(A.items())),tuple(sorted(B.items())),tuple(sorted(E.items())))
def unpack(s): return [dict(x) for x in s]
def clean(d): return {k:x for k,x in d.items() if x!=0}
def hop(s,a,b,inward=False,S=None):
 A,B,E=unpack(s); qa=A.get(a,1); qb=B.get(b,0)
 if inward:
  if qa!=0 or qb==0: return None
  q=qb; step=q; A[a]=q; B.pop(b)
 else:
  if qa==0 or qb!=0: return None
  q=qa;step=-q;A[a]=0;B[b]=q
 m=E.get((a,b),0)
 if S is not None:
  C=S*(S+1)
  assert abs(m)<=S and abs(m+step)<=S
  assert C-m*(m+step)>0
 E[(a,b)]=m+step
 A={x:q for x,q in A.items() if q!=1}
 return key(A,B,clean(E))
def birth(s,a,b,q,S=None):
 A,B,E=unpack(s)
 if A.get(a,1)!=0 or B.get(b,0)!=0:return None
 m=E.get((a,b),0)
 if S is not None:
  C=S*(S+1);assert abs(m)<=S and abs(m+q)<=S and C-m*(m+q)>0
 A[a]=q;B[b]=-q;E[(a,b)]=m+q
 return key({x:z for x,z in A.items() if z!=1},B,clean(E))
checks=0
def gauss(s,S):
 global checks
 A,B,E=unpack(s);div=defaultdict(int)
 for (a,b),m in E.items():
  assert parity(a)==0 and parity(b)==1 and dist(a,b)==1
  assert abs(m)<=S
  div[a]+=m;div[b]-=m
 verts=set(div)|set(A)|set(B)
 for x in verts:
  rhs=A.get(x,1)-1 if parity(x)==0 else B.get(x,0)
  assert div[x]==rhs,(x,div[x],rhs)
 checks+=1
 return True
def F(s,a,adj=False):
 out=defaultdict(int)
 for b in nei(a):
  t=hop(s,a,b,adj)
  if t is not None:out[t]+=1
 return out
def comp(vec,a,adj=False):
 out=defaultdict(int)
 for s,z in vec.items():
  for t,y in F(s,a,adj).items():out[t]+=z*y
 return dict(out)
def original_label(a,b,coherent):
 for i in range(3):
  if all(a[j]==b[j] for j in range(3) if j!=i):
   if (b[i]-a[i])%L==1:return {'tail':a,'axis':i,**({} if coherent else {'sign':1})}
   if (a[i]-b[i])%L==1:return {'tail':b,'axis':i,**({} if coherent else {'sign':-1})}
 raise AssertionError('not an edge')
def stats(s):
 A,B,E=unpack(s);holes=[a for a,q in A.items() if q==0];assert len(holes)==1
 h=holes[0];q=1+sum(abs(m) for (a,b),m in E.items() if dist(a,h)<=2)
 n3=sum(dist(b,h)<=3 for b in B)
 loss=2*sum(b not in B for b in nei(h))
 return {'hole':h,'W':len(holes),'NB':len(B),'N3':n3,'rotor_loss':loss,'moving_weight':q,'Q1':sum(abs(m) for m in E.values()),'Q2':sum(m*m for m in E.values())}
h,c,b,r=map(v,[(0,0,0),(2,0,0),(1,0,0),(1,1,0)])
a,d,x,y=map(v,[(-2,0,0),(-3,1,0),(-3,0,0),(-2,1,0)])
pairs=[(r,v((0,1,0)),v((2,1,0))),(h,v((-1,0,0)),v((0,-1,0))),(h,v((0,0,1)),v((0,0,-1))),(c,v((3,0,0)),v((2,-1,0))),(c,v((2,0,1)),v((2,0,-1)))]
rows=[]; t0=time.monotonic();cpu=time.process_time()
for m in [0,1,2,4,8]:
 S=max(1,m);s=key({}, {}, {});gauss(s,S)
 for _ in range(m):
  for aa,bb,adj in [(a,x,False),(d,y,False),(d,x,True),(a,y,True)]:
   s=hop(s,aa,bb,adj,S);assert s is not None;gauss(s,S)
 seed=s;vec={s:1};labels=[]
 for aa,u,w in pairs:
  s=hop(s,aa,u,False,S);assert s is not None;gauss(s,S)
  s=birth(s,aa,w,1,S);assert s is not None;gauss(s,S)
  nxt=defaultdict(int)
  for ss,z in vec.items():
   tt=hop(ss,aa,u,False,S);assert tt is not None
   for sign in [1,-1]:
    uu=birth(tt,aa,w,sign,S);assert uu is not None
    gauss(uu,S);nxt[uu]+=z
  vec=dict(nxt);labels.append({'resolved':original_label(aa,w,False),'coherent':original_label(aa,w,True)})
 alpha=hop(s,h,b,False,S);assert alpha is not None;gauss(alpha,S)
 vec={hop(ss,h,b,False,S):z for ss,z in vec.items()};assert None not in vec
 assert len(vec)==32 and vec.get(alpha)==1
 mid=hop(alpha,h,b,True,S);beta=hop(mid,c,b,False,S);gauss(mid,S);gauss(beta,S)
 C=S*(S+1); Ea=dict(alpha[2]);Em=dict(mid[2])
 assert C-Ea[(h,b)]*(Ea[(h,b)]+1)==C
 assert C-Em.get((c,b),0)*(Em.get((c,b),0)-1)==C
 left=comp(F(alpha,h,True),c);right=comp(F(alpha,c),h,True)
 assert left=={beta:1} and right=={}
 sa,sb=stats(alpha),stats(beta)
 assert sa['NB']==sb['NB']==11 and sa['N3']==sb['N3']==11
 assert sa['rotor_loss']==sb['rotor_loss']==0
 assert sa['moving_weight']==12+2*m and sb['moving_weight']==12
 assert sa['Q1']==sb['Q1']==11+4*m and sa['Q2']==sb['Q2']==11+4*m*m
 rows.append({'m':m,'S':S,'alpha':sa,'beta':sb,'actual_cross_coefficient':1,'selected_spin_squared_factors':[1,1],'coherent_component_count':len(vec),'selected_component_coefficient':vec[alpha],'original_birth_labels':labels})
result={'rows':rows,'Gauss_checks':checks,'CPU_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-t0,'threads':{k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']},'scope':'finite exact word identities, not actual trajectory probabilities'}
Path(__file__).with_name('TRANSPORT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'cases':len(rows),'Gauss_checks':checks,'CPU_seconds':result['CPU_seconds'],'wall_seconds':result['wall_seconds']}))
print('TOTAL: PASS=5 FAIL=0')
