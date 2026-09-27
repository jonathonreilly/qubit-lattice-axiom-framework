"""Toy zero-offset isolated-square calibration tangent; no device inference."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json
from scipy.linalg import eigh_tridiagonal
for delta in (1.,10.,31.607246,100.):
    K=1.;n=np.arange(-100,101,dtype=float)
    e,v=eigh_tridiagonal(4*K*n*n-4*delta,np.full(200,-2*delta),select='i',select_range=(0,6),tol=1e-12)
    dhk=(4*n[:,None]**2*v*v).sum(axis=0)
    dhd=-4*np.ones(7)-4*(v[:-1]*v[1:]).sum(axis=0)
    c=((8*delta-8*K*n*n)[:,None]*v*v).sum(axis=0)+2*((4*delta+4*K*n[:-1]*(n[:-1]+1))[:,None]*v[:-1]*v[1:]).sum(axis=0)
    J=np.column_stack((dhk[1:]-dhk[0],dhd[1:]-dhd[0]));cg=c[1:]-c[0]
    adjustment=np.linalg.solve(J[:2],-cg[:2]);remaining=cg+J@adjustment
    print(json.dumps(dict(delta_over_K=delta,parameter_adjustment_per_x=adjustment.tolist(),unadjusted_gap_shift_per_x=cg.tolist(),calibrated_gap_shift_per_x=remaining.tolist(),scope='Fix two model gaps by K and delta shifts; higher-gap derivatives only. No data, cavity, offset or fixed microscopic x.')))
