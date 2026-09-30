#!/usr/bin/env python3
"""Exact invariant reduction and positive quartic lower bounds, dimension15."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from datetime import datetime,timezone
import json,time,resource
OUT=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (runtime/'STOP_REQUESTED.json').exists()
assert datetime.now(timezone.utc).timestamp()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
start=time.monotonic();a=json.loads((OUT/'quartic.json').read_text());n=15
mon=[tuple(a['coordinates'].index(x) for x in m) for m in a['monomial_order']];ix={m:i for i,m in enumerate(mon)}
lin=lambda i:tuple(int(j==i) for j in range(5))
u=[lin(0),lin(1),(-1,-1,0,0,0)];v=[lin(4),lin(3),lin(2)] # v_i uses complementary plane
def prod(p,q):
 z=[0]*n
 for i in range(5):
  for j in range(5):z[ix[tuple(sorted((i,j)))]]+=p[i]*q[j]
 return z
def vsum(ps):return [sum(p[i] for p in ps) for i in range(n)]
def mat():return [[F(0) for _ in range(n)] for _ in range(n)]
def outer(p,q=None):
 if q is None:q=p
 return [[F(x*y) for y in q] for x in p]
def reouter(p,q):return [[F(x*y+y2*x2,2) for y,y2 in zip(q,p)] for x,x2 in zip(p,q)]
def add(*Gs):return [[sum(G[i][j] for G in Gs) for j in range(n)] for i in range(n)]
Qe=vsum([prod(x,x) for x in u]);Qt=vsum([prod(x,x) for x in v])
Gs={
 'U2':add(*(outer(prod(x,y)) for x,y in product(u,repeat=2))),
 'Qe2':outer(Qe),
 'p2':add(*(outer(prod(x,y)) for x,y in product(v,repeat=2))),
 'Qt2':outer(Qt),
 'r':add(*(outer(prod(x,x)) for x in v)),
 'Up':add(*(outer(prod(x,y)) for x,y in product(u,v))),
 'J':add(*(outer(prod(x,y)) for x,y in zip(u,v))),
 'QeQt':reouter(Qe,Qt),
 'L':add(*(reouter(prod(x,x),prod(y,y)) for x,y in zip(u,v))),
 'M':add(*(reouter(prod(u[k],v[k]),prod(v[(k+1)%3],v[(k+2)%3])) for k in range(3)))
}
coeff={
 'mu':{'U2':52,'p2':F(700,3),'Qt2':24,'r':F(-124,3),'Up':F(490,3),'J':66,'QeQt':F(22,3),'L':F(4,3),'M':-48},
 'tau':{'U2':120,'p2':632,'Qt2':72,'r':-80,'Up':620,'J':-60,'QeQt':-28,'L':56,'M':-96},
 'number':{'U2':F(-26,9),'Qe2':F(11,9),'p2':F(-16,3),'Qt2':8,'r':F(-28,3),'Up':-16,'J':F(32,3),'QeQt':F(8,3),'L':F(16,3)}
}
keys={'mu':('energy_mu_matrix_numerator',12),'tau':('energy_tau_matrix_numerator',12),'number':('number_quartic_matrix_numerator',3)}
for name,c in coeff.items():
 G=[[sum(v*Gs[k][i][j] for k,v in c.items()) for j in range(n)] for i in range(n)]
 key,den=keys[name]
 assert G==[[F(x,den) for x in row] for row in a[key]],name

# All amplitudes: epsilon4 >= (40 mu+100 tau) (U+2p)^2.
S2=[[Gs['U2'][i][j]+4*Gs['Up'][i][j]+4*Gs['p2'][i][j] for j in range(n)] for i in range(n)]
cert=[]
for name,c in [('mu',40),('tau',100)]:
 key,den=keys[name]
 G=[[F(a[key][i][j],den)-c*S2[i][j] for j in range(n)] for i in range(n)]
 L=[[F(i==j) for j in range(n)] for i in range(n)];D=[]
 for k in range(n):
  d=G[k][k]-sum(L[k][j]**2*D[j] for j in range(k));assert d>0;D.append(d)
  for i in range(k+1,n):L[i][k]=(G[i][k]-sum(L[i][j]*D[j]*L[k][j] for j in range(k)))/d
 assert G==[[sum(L[i][k]*D[k]*L[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
 cert.append({'part':name,'subtracted_s_squared_coefficient':c,'positive_ldl_pivots':[str(d) for d in D],'exact_ldl_reconstruction':True})

# Two complex amplitudes x,y: u=(x,-x,0), v12=y. Freeze complete
# quartic coefficients rather than infer from selected pulse values.
restricted={'mu':{'abs_x4':208,'abs_y4':216,'abs_x2_abs_y2':F(980,3),'Re_xbar2_y2':F(44,3)},
 'tau':{'abs_x4':480,'abs_y4':624,'abs_x2_abs_y2':1240,'Re_xbar2_y2':-56}}
out={'invariant_coefficients':{k:{x:str(y) for x,y in v.items()} for k,v in coeff.items()},
 'full_matrix_identity':True,'positive_bound_certificates':cert,
 'restricted_E_T_coefficients':{k:{x:str(y) for x,y in v.items()} for k,v in restricted.items()},
 'elapsed_s':time.monotonic()-start,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(OUT/'invariant_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
