import numpy as np,json,time
from scipy.sparse.linalg import eigsh
from neutral_rect_model import sector,op
from neutral_spacegroup_model import translation_tables,orbits,orbit_op
for L in [2,3]:
 D=sector(L);T,R,C=translation_tables(D);data=orbits(D['dim'],T,R,C);labels,signs,reps,sizes,excluded=data
 H=op(sum(D['H'],[]),D['dim']);h=orbit_op(sum(D['H'],[]),data);v=np.random.default_rng(34).normal(size=len(reps));v/=np.linalg.norm(v)
 full=np.zeros(D['dim']);ok=labels>=0;full[ok]=signs[ok]*v[labels[ok]]/np.sqrt(sizes[labels[ok]]);hv=h@v;expected=np.zeros(D['dim']);expected[ok]=signs[ok]*hv[labels[ok]]/np.sqrt(sizes[labels[ok]])
 err=np.linalg.norm(H@full-expected);print(dict(L=L,reduced=len(reps),excluded=excluded,error=err),flush=True);assert err<1e-11
 print(eigsh(h,k=2,which='SA',tol=1e-10,return_eigenvectors=False),flush=True)
