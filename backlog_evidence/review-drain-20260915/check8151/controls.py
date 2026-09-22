import itertools,json,time
from fractions import Fraction as F
from pathlib import Path
t=time.monotonic();out={}
for d in [2,3]:
 n=4;edge=frozenset([tuple([0]*d),tuple([1]+[0]*(d-1))]);seen={edge};todo=[edge]
 while todo:
  e=todo.pop()
  for axis in range(d):
   for k in range(n):
    f=frozenset(tuple((2*k-v[i])%n if i==axis else v[i] for i in range(d))for v in e)
    if f not in seen:seen.add(f);todo.append(f)
 assert len(seen)==n**d//2**(d-1)
 assert all(all(v[i]%2==0 for i in range(1,d))for e in seen for v in e)
 out[str(d)+'d_reflected_edge_orbit']={'distinct_edges':len(seen),'all_direction_edges':n**d,'transverse_coordinates':'even only'}
Z=6**4;bad=sum(all(v[i]!=v[(i+1)%4]for i in range(4)) for v in itertools.product(range(6),repeat=4));assert F(bad,Z)==F(35,72)
out['independent_spin_4x4']={'site_reflected_event_probability':str(F(bad,Z)**2),'claimed_all_direction_probability':str(F(bad,Z)**4),'equal':False}
perms=[]
for p in itertools.permutations(range(3)):
 for swaps in itertools.product(range(2),repeat=3):
  perms.append(tuple(2*p[i//2]+((i%2)^swaps[i//2])for i in range(6)))
prob=tuple(F(i,21)for i in range(1,7));orbit={tuple(prob[g[i]] for i in range(6))for g in perms};assert len(orbit)==48
out['nonuniform_one_site_orbit']={'distribution':[str(x)for x in prob],'orbit_size':len(orbit),'refutes_claimed_upper_bound_six':True}
# direct operator action on invariant basis, separate from symbolic eigenvalue routine
for p,q,r in [(3,1,2),(5,2,4),(432,1,2)]:
 mat=[[p if a==b else q if a//2==b//2 else r for b in range(6)]for a in range(6)]
 bases=[([1]*6,p+q+4*r)]+[([int(i==2*j)-int(i==2*j+1)for i in range(6)],p-q)for j in range(3)]+[([1,1,-1,-1,0,0],p+q-2*r),([1,1,0,0,-1,-1],p+q-2*r)]
 for v,l in bases:assert [sum(a*b for a,b in zip(row,v))for row in mat]==[l*x for x in v]
out['spectrum_controls']=18
out['contour_arithmetic']={'series':str(F(1,2)**4*(4-3*F(1,2))/(1-F(1,2))**2),'sum':str(F(5,24)+F(180,1024))};assert F(5,24)+F(180,1024)==F(295,768)
out['elapsed_seconds']=time.monotonic()-t;print(json.dumps(out,indent=2));Path('/private/tmp/review-drain-20260915/check8151/controls.json').write_text(json.dumps(out,indent=2)+'\n')
