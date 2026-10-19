"""Exact finite spectral null direction: charges do not fix dynamical source."""
from pathlib import Path
import json,numpy as np
from compass_sector_basis import geometry,dense_terms
sites,bonds=geometry((3,2,1));N=1<<len(sites);terms=[]
for i,j,a in bonds:
 m=(1<<i)|(1<<j);terms.append((m if a!=2 else 0,m if a!=0 else 0,1 if a==1 else -1))
H=dense_terms(terms,N);I=np.eye(N);A=np.zeros_like(H)
for x in range(len(sites)):
 ts=[t for t,(i,j,a) in zip(terms,bonds) if x in (i,j)]
 e=dense_terms(ts,N)/2
 A+=2*e@e-len(ts)*I/2
B=H@(H@A-A@H)-(H@A-A@H)@H
E,U=np.linalg.eigh(H);D=E[:,None]-E[None,:];Be=U.T@B@U;Ae=U.T@A@U
assert np.max(np.abs(Be-D**2*Ae))<1e-11
same=np.abs(D)<1e-9
assert np.max(np.abs(Be[same]))<1e-11
# Entire degenerate blocks vanish, so no arbitrary branch assumption here.
p=np.exp(-.7*(E-E.min()));p/=p.sum();rows=[]
for alpha in [0,.25,1]:
 O=H+alpha*B;Oe=U.T@O@U
 diag_error=float(np.max(np.abs(np.diag(Oe)-E)))
 block_error=float(np.max(np.abs((Oe-np.diag(E))[same])))
 transitions=np.abs(Oe)**2;transitions[same]=0
 weight=float(np.sum(p[:,None]*transitions))
 assert diag_error<1e-11 and block_error<1e-11
 rows.append(dict(alpha=alpha,diagonal_energy_error=diag_error,degenerate_block_error=block_error,thermal_inelastic_weight=weight))
assert rows[0]['thermal_inelastic_weight']<1e-24
assert abs(rows[2]['thermal_inelastic_weight']/rows[1]['thermal_inelastic_weight']-16)<1e-10
out=dict(shape=[3,2,1],beta=.7,native_J=1,commutator_identity_error=float(np.max(np.abs(Be-D**2*Ae))),rows=rows,scope='Constructed observable family, not added interactions, derived scalar or observed coupling. Alpha is an explicit arbitrary probe coefficient.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
