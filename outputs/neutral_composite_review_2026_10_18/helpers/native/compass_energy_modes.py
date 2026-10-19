"""Exact energy-feature norm and residual kernels in the HS state, K=1.
Uses E_x=2e_x/K: divide kernels by4 for physical e at K=1.
"""
from pathlib import Path
import json
from compass_local_transport import shift,word,derivative,correlations
P=Path(__file__).resolve().parent
A={word([((0,0,0),a),(shift((0,0,0),a,s),a)]):1 for a in range(3) for s in [-1,1]}
rows=[]
for n in range(3):
 cr=correlations(A);row=dict(n=n,terms=len(A),kernel=[dict(r=list(r),value=v) for r,v in sorted(cr.items())]);rows.append(row);print(row)
 assert sum(cr.values())==(12 if n==0 else 0)
 if n<2:A=derivative(A)
(P/'compass_energy_modes.json').write_text(json.dumps(dict(scope='HS energy wavepacket residual, not a propagating scalar-particle identification',rows=rows),indent=2)+'\n')
