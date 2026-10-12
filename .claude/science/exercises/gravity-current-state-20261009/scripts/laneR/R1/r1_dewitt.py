# R1 check: kinetic form E.E - c (tr E)^2 is invariant under the scalar (lapse-type) gauge dE = (q^2 I - q q) beta
# on the vector-Gauss subspace (q_i E_ij = 0) iff c = 1/2 (3D DeWitt value).
import numpy as np
from r1_modes import ops, t2v, phys_basis
rng=np.random.default_rng(3)
for c in [0.0,0.25,0.5,0.75,1.0]:
    worst=0
    for _ in range(5):
        q=2*np.sin(rng.uniform(-np.pi,np.pi,3)/2); o=ops(q)
        trv=t2v(np.eye(3)); K=np.eye(6)-c*np.outer(trv,trv)
        sE=o['S'].T[:,0]                       # scalar-gauge direction in E space
        kerG=phys_basis([o['Gt']])             # E with q_i E_ij = 0 (Gt^T = Gauss operator)
        worst=max(worst,np.abs(sE@K@kerG).max()/np.linalg.norm(sE))
    print('c=%.2f  max |delta K| on Gauss subspace = %.2e'%(c,worst))
