import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['VECLIB_MAXIMUM_THREADS']='1'
import numpy as np,json,math
from scipy.linalg import eigh
from neutral_four_layer_geometry import geometry,diagonal
h=4;g=5;m=2*h/(math.sqrt((16*g)**2+4*h*h)+16*g);a=2*h*m*(8-4*h/g)**2;b=9003008
rows=[]
for R in [3,4]:
 _,_,edges,flips=geometry(R,True);n=1<<((R-1)**2);s=np.arange(n,dtype=np.int64);E=-diagonal(s,edges)/5
 K=np.diag(-g*E)
 for f in flips:K[s,s^f]-=h
 ev,U=eigh(K);ground=U[:,0];ground*=np.sign(ground.sum());assert min(ground)>0
 ratio=min(np.min(ground[s^f]/ground) for f in flips)
 q=(E-ground@(E*ground))*ground;weight=(U.T@q)**2;omega=ev-ev[0]
 M=[float(weight@omega**j) for j in [0,1,3]]
 direct1=h/2*sum(float(np.sum(ground*ground[s^f]*(E[s^f]-E)**2)) for f in flips)
 A=1j*(K*E[None,:]-E[:,None]*K);ag=A@ground;direct3=float(np.vdot(ag,K@ag-ev[0]*ag).real)
 assert ratio>=m and M[1]>=a*R*R and M[2]<=b*R*R
 assert abs(M[1]-direct1)<1e-8 and abs(M[2]-direct3)<1e-5
 assert M[0]>=M[1]**1.5/math.sqrt(M[2])
 rows.append(dict(R=R,min_amplitude_ratio=float(ratio),ratio_lower=m,moments=M,M1_direct=direct1,M3_direct=direct3,variance_density=M[0]/R**2,first_moment_density=M[1]/R**2))
print(json.dumps(dict(checks=rows,scope='Finite coefficient-model identity controls; analytic locality argument supplies arbitrary-area bounds')))
