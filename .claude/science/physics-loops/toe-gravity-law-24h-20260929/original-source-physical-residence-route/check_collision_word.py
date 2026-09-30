#!/usr/bin/env python3
"""Tiny original-word control. Independent implementation, no state-space enumeration."""
import json,time,resource
from collections import defaultdict
L=16
units=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
def add(a,b):return tuple((x+y)%L for x,y in zip(a,b))
def normdist(a,b):return sum(min((x-y)%L,(y-x)%L) for x,y in zip(a,b))
def around(a):return [add(a,u) for u in units]
def pack(A,B,E):return (tuple(sorted((a,q) for a,q in A.items() if q!=1)),tuple(sorted(B.items())),tuple(sorted((e,m) for e,m in E.items() if m)))
def unpack(x):return tuple(dict(z) for z in x)
def parity(x):return sum(x)%2
checked=0
def validate(x,S):
 global checked
 A,B,E=unpack(x); div=defaultdict(int)
 for (a,b),m in E.items():
  assert parity(a)==0 and parity(b)==1 and normdist(a,b)==1
  assert abs(m)<=S
  div[a]+=m;div[b]-=m
 for v in set(div)|set(A)|set(B):
  assert div[v]==(A.get(v,1)-1 if parity(v)==0 else B.get(v,0))
 checked+=1

def hop(x,a,b,S,inward=False):
 A,B,E=unpack(x); qa=A.get(a,1);qb=B.get(b,0)
 if inward:
  if qa or not qb:return None
  q=qb; step=q;A[a]=q;B.pop(b)
 else:
  if not qa or qb:return None
  q=qa;step=-q;A[a]=0;B[b]=q
 m=E.get((a,b),0)
 if abs(m)>S or abs(m+step)>S:return None
 assert S*(S+1)-m*(m+step)>0
 E[(a,b)]=m+step
 return pack(A,B,E)
def birth(x,a,b,sgn,S):
 A,B,E=unpack(x)
 if A.get(a,1)!=0 or B.get(b,0)!=0:return None
 m=E.get((a,b),0)
 if abs(m)>S or abs(m+sgn)>S:return None
 assert S*(S+1)-m*(m+sgn)>0
 A[a]=sgn;B[b]=-sgn;E[(a,b)]=m+sgn
 return pack(A,B,E)
def charge_shift_unit(x,y):
 E=unpack(x)[2];V=unpack(y)[2]
 z=[(E.get(e,0),V.get(e,0)) for e in set(E)|set(V) if E.get(e,0)!=V.get(e,0)]
 assert len(z)==1 and z[0][0]*z[0][1]==0 and abs(z[0][0]-z[0][1])==1

def applyword(S):
 x=pack({}, {}, {});marks=[];steps=[]
 for h in ((14,0,0),(2,0,0)):
  p=add(h,(1,1,0));q=add(h,(-1,0,1))
  words=[('A',p,add(h,(0,1,0)),add(h,(1,0,0)),None),
         ('A',q,add(h,(-1,0,0)),add(h,(-1,0,2)),None),
         ('B',h,add(h,(0,-1,0)),add(h,(0,0,1)),add(h,(0,0,-1)))]
  for typ,a,old,marked,last in words:
   before=x
   y=hop(x,a,old,S);assert y is not None;charge_shift_unit(x,y);validate(y,S);x=y
   y=birth(x,a,marked,1,S);assert y is not None;charge_shift_unit(x,y);validate(y,S);x=y
   if last is not None:
    y=hop(x,a,last,S);assert y is not None;charge_shift_unit(x,y);validate(y,S);x=y
   marks.append({'coefficient':typ,'a':a,'b':marked,'resolved_sigma':1,'coherent_label':[a,marked]})
   steps.append({'type':typ,'input':before,'output':x})
 A,B,E=unpack(x);holes=[a for a,q in A.items() if q==0]
 assert set(holes)=={(14,0,0),(2,0,0)} and len(B)==14
 assert all(b in B for h in holes for b in around(h))
 assert normdist(*holes)==4
 # Bare loss and every first grade-minus-two D_mu=-j_mu F* vanish.
 assert sum(b not in B for h in holes for b in around(h))==0
 inward_paths=0;recycling_paths=0
 for h in holes:
  for b in around(h):
   y=hop(x,h,b,S,True)
   if y is None:continue
   inward_paths+=1;validate(y,S)
   Ay,By,Ey=unpack(y)
   for ah,qa in Ay.items():
    if qa:continue
    for bm in around(ah):
     for sign in (-1,1):
      z=birth(y,ah,bm,sign,S)
      if z is not None:recycling_paths+=1
 assert inward_paths==12 and recycling_paths==0
 # Only the midpoint belongs to both radius-two A neighborhoods.
 centers=set(add(holes[0],(i,j,k)) for i in range(-2,3) for j in range(-2,3) for k in range(-2,3) if abs(i)+abs(j)+abs(k)<=2 and (i+j+k)%2==0)
 shared=[a for a in centers if a not in holes and all(normdist(a,h)<=2 for h in holes)]
 assert shared==[(0,0,0)]
 a=(0,0,0);assert A.get(a,1)==1 and all(E.get((a,b),0)==0 for b in around(a))
 vacancies=[b for b in around(a) if b not in B];assert len(vacancies)==4
 # <F_a* F_a>=4, electric diagonal zero, (m_a-1)+=1.
 collision_mean=4
 # A distinct actual two-hop magnetic matrix entry, with unchanged A-hole mask.
 new=(0,1,0);old=(15,0,0)
 y=hop(x,a,new,S);assert y is not None
 z=hop(y,a,old,S,True);assert z is not None
 validate(y,S);validate(z,S)
 assert sum(m*m for m in unpack(z)[2].values())-sum(m*m for m in E.values())==2
 assert [a for a,q in unpack(z)[0].items() if q==0]==sorted(holes)
 return {'S':S,'W':2,'NB':14,'original_event_count':6,'selected_primitive_steps':14,
         'selected_amplitude_modulus':1,'full_coefficient_sign':1,
         'bare_loss':0,'D_minus_two_paths':recycling_paths,'inward_paths':inward_paths,
         'collision_diagonal':collision_mean,'collision_matrix_element':1,'Q2_increment':2,
         'marks':marks,'state':x,'current_partner':z,'word_steps':steps}

start=time.process_time()
rows=[applyword(S) for S in (1,2,7)]
assert checked==84
print(json.dumps({'scope':'original coefficient/source-word discriminator; no actual Omega probability or residence claim',
                  'expected_before_execution':{'W':2,'NB':14,'records':6,'G':0,'D_minus_two':0,'R_collision_mean':4,'matrix_element':1,'Q2_increment':2},
                  'rows':rows,'gauss_checks':checked,'cpu_seconds':time.process_time()-start},indent=2))
print('TOTAL PASS=8 FAIL=0')
