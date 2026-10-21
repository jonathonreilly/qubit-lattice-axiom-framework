import numpy as np
from neutral_transverse_bound_model import matrix
from scipy.sparse.linalg import eigsh
def run_checks():
 L=100;b=.1;h=1e-4
 H,st,idx=matrix(L,b=b);e,v=eigsh(H,k=1,which='SA',tol=1e-12);E=e[0];u=v[[idx[(1,0)],idx[(0,1)]],0];u2=u@u;W=(-u[0]+b*u[1])**2;pred=2*u2/np.sqrt(E*E-16)
 em=eigsh(matrix(L,b=b,c=1-h)[0],k=1,which='SA',tol=1e-12,return_eigenvectors=False)[0];ep=eigsh(matrix(L,b=b,c=1+h)[0],k=1,which='SA',tol=1e-12,return_eigenvectors=False)[0];fd=-(ep-em)/(8*h)
 assert abs(fd-pred)<1e-6
 return dict(energy=float(E),predicted_curvature=float(pred),finite_difference_curvature=float(fd),error=float(fd-pred),source_weight=float(W))
