"""Reviewer-only checks. No import from primary; < 60 CPU s / 300 MB, BLAS1."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'): os.environ[k]='1'
import numpy as np
from scipy.linalg import expm
import json,time,resource
from pathlib import Path
start=time.process_time()
# Solve the characteristic two-state differential equation directly in position.
# Compare its Fourier coefficients with a finite Toeplitz exponential.
q=256; y=2*np.pi*np.arange(q)/q; t=.6; k0=2; K=10
v=np.zeros((q,2),complex);v[:,0]=1
h=np.diag([0.,2.]); G=np.array([[1.,-1.],[-1.,1.]])
def rhs(s,w):return -1j*(w@h+(.5-.5*np.cos(y+s))[:,None]*(w@G))
steps=2400;dt=t/steps
for j in range(steps):
 a=rhs(j*dt,v);b=rhs((j+.5)*dt,v+dt*a/2);c=rhs((j+.5)*dt,v+dt*b/2);d=rhs((j+1)*dt,v+dt*c)
 v+=dt*(a+2*b+2*c+d)/6
beta=sum(np.exp(1j*m*y) for m in range(-k0,k0+1))/np.sqrt(2*k0+1)
field=beta[:,None]*v
modes=np.arange(-K,K+1)
expected=np.array([np.mean(np.exp(-1j*m*(y+t))[:,None]*field,axis=0) for m in modes]).reshape(-1)
f=np.fromfunction(lambda i,j: .5*(i==j)-.25*(abs(i-j)==1),(2*K+1,2*K+1))
H=np.kron(np.diag(modes),np.eye(2))+np.kron(np.eye(len(modes)),h)+np.kron(f,G)
ready=np.zeros((len(modes),2),complex);ready[abs(modes)<=k0,0]=1/np.sqrt(2*k0+1)
actual=expm(-1j*t*H)@ready.reshape(-1)
error=float(np.linalg.norm(actual-expected));assert error<1e-9
# Julia dilation checked through singular vectors, with genuinely rectangular R.
rng=np.random.default_rng(49271);R=(rng.normal(size=(6,3))+1j*rng.normal(size=(6,3)))/10
u,s,vh=np.linalg.svd(R,full_matrices=True)
left=vh.conj().T@np.diag(np.sqrt(1-s*s))@vh
right=u@np.diag(np.r_[np.sqrt(1-s*s),np.ones(3)])@u.conj().T
J=np.block([[left,-R.conj().T],[R,right]])
defect=float(np.linalg.norm(J.conj().T@J-np.eye(9)));assert defect<1e-12
# Exact independent occupancy-layer incidence bound, rather than full word walker.
Fbounds=[(6-o)*(o+1) for o in range(7)]
Bbounds=[(5-o)*(o+1) for o in range(6)]
center=[2*(5-o)*Fbounds[o] for o in range(6)]
assert max(Fbounds)==12 and max(Bbounds)==9 and max(center)==80
# Re-derive current weight: jump changes radial sum by 2 (5 bands),
# loss by 4 (9 bands). 2*5*3^2 + 1 + 9*5^2 =316.
current_coefficient=2*5*3**2+1+9*5**2;assert current_coefficient==316
out={'characteristic_RK4_vs_Toeplitz_expm_error':error,'position_points':q,'RK4_steps':steps,'Julia_rectangular_unitarity_defect':defect,'incidence_F_squared':Fbounds,'incidence_B_squared':Bbounds,'center_loss_bounds':center,'current_electric_weight_coefficient':current_coefficient,'cpu_seconds':time.process_time()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Finite diagnostics, not interval proof; independent analytic review supplies general quantifiers.'}
Path(__file__).with_name('REVIEWER_INDEPENDENT_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
