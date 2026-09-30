#!/usr/bin/env python3
"""Direct central occupation t^4 coefficient on a finite hard-core patch.

Only four-particle words containing the central site are constructed. No
translation-count, cycle-expansion, or defect builder is imported. Price
<100MB,<30s. This is a second author derivation, not independent review.
"""
from pathlib import Path
from itertools import product,combinations
from datetime import datetime,timezone
import json,time,resource
OUT=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (runtime/'STOP_REQUESTED.json').exists()
assert datetime.now(timezone.utc).timestamp()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
start=time.monotonic();a=json.loads((OUT/'quartic.json').read_text());O=(0,0,0)
def weight(p,q,z):
 d=[q[i]-p[i] for i in range(3)];nz=[i for i in range(3) if d[i]]
 if len(nz)==1 and abs(d[nz[0]])==2:return [z[0],z[1],-z[0]-z[1]][nz[0]]
 if len(nz)==2 and all(abs(d[i])==1 for i in nz):return -d[nz[0]]*d[nz[1]]*z[{(0,1):2,(0,2):3,(1,2):4}[tuple(nz)]]
 return 0j
norm=lambda z:int((z.conjugate()*z).real)
D=[d for d in product(range(-2,3),repeat=3) if weight(O,d,[1,1,1,1,1])]
sites={O}|set(D)|{tuple(x+y for x,y in zip(d,e)) for d,e in product(D,repeat=2)}
mon=[tuple(a['coordinates'].index(x) for x in m) for m in a['monomial_order']]
directions=[('E',[1,-1,0,0,0]),('E_complex',[1,1j,0,0,0]),('T_phase',[0,0,1,1j,0]),
 ('general',[1+1j,-2+1j,2-1j,1j,-1])]
rows=[]
for name,z in directions:
 z=list(map(complex,z));edges={p:weight(*p,z) for p in combinations(sorted(sites),2) if weight(*p,z)}
 central={p:w for p,w in edges.items() if O in p}
 s=sum(norm(w) for w in edges.values());s0=sum(norm(w) for w in central.values())
 four={}
 def amp(S):
  if S not in four:
   x,y,v,w=S
   four[S]=2*(weight(x,y,z)*weight(v,w,z)+weight(x,v,z)*weight(y,w,z)+weight(x,w,z)*weight(y,v,z))
  return four[S]
 ell=0j
 for e,w in central.items():
  for f,v in edges.items():
   S=tuple(sorted(set(e)|set(f)))
   if len(S)==4:ell+=w.conjugate()*v.conjugate()*amp(S)
 r0=sum(norm(w) for w in four.values())
 # 12 times n4 = 3 r0-4(ell+s*s0), avoiding rational arithmetic.
 assert ell.imag==0 and ell.real==int(ell.real)
 lhs=3*r0-4*(int(ell.real)+s*s0)
 m=[z[i]*z[j] for i,j in mon];G=a['number_quartic_matrix_numerator']
 rhs=sum(m[i].conjugate()*G[i][j]*m[j] for i in range(15) for j in range(15))
 assert rhs.imag==0 and lhs==4*rhs.real,(name,lhs,rhs)
 assert max(abs(lhs),abs(ell.real),r0,s*s0)<2**52
 rows.append({'direction':name,'sites':len(sites),'edges':len(edges),'central_four_particle_words':len(four),'number_t4_numerator_over_12':lhs,'exact_match':True})
out={'checks':rows,'elapsed_s':time.monotonic()-start,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 'coverage':'Actual central number Taylor coefficient through N4 on the complete radius-two pair graph patch. This independently checks volume/root normalization of the connected number polynomial.'}
(OUT/'local_number_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
