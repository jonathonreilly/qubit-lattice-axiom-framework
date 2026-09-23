#!/usr/bin/env python3
"""Secondary exact-certificate validation plus comparison to pinned own prior code."""
from pathlib import Path
import importlib.util,json,hashlib
import numpy as np
import sympy as sp
from cube_point_check import EDGES,CHORDS,A_SITES,state_space,legal_hops
HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'second_event_independent/operators.py'
assert hashlib.sha256(OLD.read_bytes()).hexdigest()=='a152167dff2cfff397397fcc56121cd9b2d79d7f412eb2e134f2f9cbbfa54c95'
spec=importlib.util.spec_from_file_location('prior_independent_operators',OLD)
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
raw=(HERE/'CUBE_POINT_RESULTS.json').read_bytes();data=json.loads(raw)
P,Q=state_space(0),state_space(1)
oldP=old.charge_basis(8,A_SITES,6,4,0);oldQ=old.charge_basis(8,A_SITES,6,4,1)
assert set(oldP)==set(P) and set(oldQ)==set(Q)
row=[oldQ.index(q) for q in Q];col=[oldP.index(q) for q in P]
checks=[]
for theta in [np.zeros(5),np.full(5,np.pi/2),np.array([.31,.57,.93,1.27,1.81])]:
 all_angles=np.array([theta[CHORDS.index(e)] if e in CHORDS else 0. for e in EDGES])
 oldA=old.hopping_matrix(oldP,oldQ,EDGES,all_angles)[np.ix_(row,col)]
 newA=np.zeros((96,36),complex);ix={q:i for i,q in enumerate(Q)}
 for j,q in enumerate(P):
  for out,shift,amp in legal_hops(q):newA[ix[out],j]+=amp*np.exp(1j*np.dot(all_angles,shift))
 error=float(np.max(np.abs(oldA-newA)));assert error<1e-13
 checks.append({'chord_angles':theta.tolist(),'maximum_hopping_matrix_error':error})
# Verify saved Bezout certificate by raw integer coefficient convolution only.
c=data['modular_certificate'];p=c['prime']
f,g=[row['coefficients'] for row in c['fibers']]
s,t=c['bezout_s_coefficients'],c['bezout_t_coefficients']
def mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%p
 return out
sf,tg=mul(s,f),mul(t,g);assert len(sf)==len(tg)
identity=[(a+b)%p for a,b in zip(sf,tg)];assert identity==[0]*(len(identity)-1)+[1]
# Independent graph certificate: number of occupied-neighbor return paths.
row_sums=[]
for q in P:
 count=0
 for mid,_,_ in legal_hops(q):
  count+=sum(out in P for out,_,_ in legal_hops(mid))
 row_sums.append(count)
assert row_sums==[14]*36
# An intentionally insufficient phase pair leaves a common polynomial modulo p.
# This is a retained diagnostic, not evidence for a physical flat band.
x=sp.Symbol('lambda');phase_powers=[0,0,1,1,0]
A=sp.zeros(96,36);ix={q:i for i,q in enumerate(Q)}
for j,q in enumerate(P):
 for out,shift,amp in legal_hops(q):
  exponent=sum(phase_powers[k]*shift[EDGES.index(e)] for k,e in enumerate(CHORDS))
  A[ix[out],j]+=amp*sp.I**exponent
h=-A.conjugate().T*A
p0=sp.Poly.from_list([int(v) for v in data['fibers'][0]['charpoly_coefficients']],x)
p_partial=sp.Poly(h.charpoly(x).as_expr(),x,domain=sp.ZZ)
partial_gcd=sp.gcd(p0,p_partial)
assert partial_gcd.degree()>0
print(json.dumps({'prior_source_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest(),
 'main_results_sha256':hashlib.sha256(raw).hexdigest(),
 'old_builder_comparisons':checks,'saved_modular_bezout_convolution_verified':True,
 'all_36_exact_absolute_path_row_sums':row_sums,
 'inconclusive_phase_pair':{'chord_phase_powers_of_i':phase_powers,'common_exact_polynomial':str(partial_gcd.as_expr()),'degree':partial_gcd.degree(),
 'interpretation':'Two poorly selected fibers can share eigenvalues; this does not establish a band constant on the full five-torus.'}},indent=2))
