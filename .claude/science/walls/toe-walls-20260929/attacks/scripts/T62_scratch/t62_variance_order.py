"""Control: the SAME rule A={0} (no two adjacent records) with a deterministic raster formation order versus random order.
The formation ORDER (unfixed by the axioms, T01) decides whether the frozen pattern is hyperuniform."""
import numpy as np
from t62_variance import sweep, var_curve, slope
L=64; ws=list(range(1,17))
allowed=np.zeros(7,dtype=np.bool_); allowed[0]=True
for name,perm in (("raster order",np.arange(L**3,dtype=np.int64)),("random order",np.random.default_rng(3).permutation(L**3).astype(np.int64))):
    occ=np.zeros((L,L,L),dtype=np.int8); sweep(occ,allowed,perm,L)
    vc=var_curve(occ,ws); V=vc[:,0]
    print("%-13s density %.3f  Var(w) = %s"%(name,occ.mean(),np.round(V[[0,1,3,7,11,15]],2).tolist()),
          " s(4..16)=%.2f"%slope(ws,np.maximum(V,1e-9)) if V[3]>0 else "")
