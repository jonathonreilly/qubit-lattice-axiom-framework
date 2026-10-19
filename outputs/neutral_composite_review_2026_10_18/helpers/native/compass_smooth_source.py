"""Smooth-profile response from finite stationary spatial diagnostic; not bulk scaling."""
from pathlib import Path
import json,hashlib
import numpy as np
P=Path(__file__).resolve().parent
s=P.parents[1]/'inputs/stationary_spatial.json';d=json.loads(s.read_text())
x=np.array(d['sites'],float)-1
k=np.array(d['spatial_regularized_inverse_moments']['64']['0.1'])
r2=np.sum(x*x,axis=1)
assert abs(k.sum())<1e-9
lookup={tuple(y):v for y,v in zip(x,k)}
inv=max(abs(v-lookup[tuple(-y)]) for y,v in zip(x,k));assert inv<1e-8
M=np.einsum('n,ni,nj->ij',k,x,x)
rows=[]
for R in [2,4,8,16,32,64]:
 # Gaussian f=exp(-r²/(2R²)); Taylor remainder <= u²/2 for u>=0.
 exact=float(k@np.exp(-r2/(2*R*R)))
 leading=float(-np.trace(M)/(2*R*R))
 bound=float(np.abs(k)@(r2*r2)/(8*R**4)+abs(k.sum()))
 assert abs(exact-leading)<=bound+1e-14
 rows.append(dict(R=R,response=exact,quadratic_term=leading,remainder=exact-leading,absolute_remainder_bound=bound,scaled_response=R*R*exact))
out=dict(source_sha256=hashlib.sha256(s.read_bytes()).hexdigest(),uniform_sum=float(k.sum()),inversion_error=float(inv),second_moment=M.tolist(),rows=rows,scope='Fixed finite27site cube and regularized response eta=.1. Larger R only smooths an externally specified diagnostic profile; no volume extrapolation or matter source derivation.')
(P/'compass_smooth_source.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
