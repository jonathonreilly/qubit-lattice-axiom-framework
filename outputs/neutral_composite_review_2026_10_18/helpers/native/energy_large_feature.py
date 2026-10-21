"""Normalizable large energy features; exact kernels, converged Gaussian sums."""
from pathlib import Path
import json,numpy as np
P=Path(__file__).resolve().parent
kernels=json.loads((P/'compass_energy_modes.json').read_text())['rows']
def sums(R,cut):
 x=np.arange(-int(np.ceil(cut*R))-4,int(np.ceil(cut*R))+5,dtype=float)
 f=np.exp(-x*x/(2*R*R));s={r:float(f@np.exp(-(x+r)**2/(2*R*R))) for r in range(-3,4)}
 return [sum(v['value']*np.prod([s[r] for r in v['r']]) for v in k['kernel'])/4 for k in kernels]
rows=[]
for R in [1.,2.,4.,8.,16.,32.]:
 a=sums(R,8);b=sums(R,10);assert np.allclose(a,b,rtol=1e-9,atol=1e-9)
 row=dict(R=R,energy_norm_squared=a[0],residual_squared=a[1]/a[0],fourth_moment=a[2]/a[0],R_squared_residual=R*R*a[1]/a[0],R_squared_fourth_moment=R*R*a[2]/a[0]);rows.append(row);print(row)
assert abs(rows[-1]['R_squared_residual']-4)<.01
assert abs(rows[-1]['R_squared_fourth_moment']-96)<.2
(P/'energy_large_feature.json').write_text(json.dumps(dict(scope='HS norm large energy features in supplied Hamiltonian; K=1; numerical Gaussian sums, exact local kernels; not propagating particle',rows=rows),indent=2)+'\n')
