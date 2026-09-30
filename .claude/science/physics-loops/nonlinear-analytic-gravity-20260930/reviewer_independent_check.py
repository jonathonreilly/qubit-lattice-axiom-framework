"""Independent review checks; imports no author implementation. Estimated <10 CPU s, <150 MB."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'): os.environ[key]='1'
import resource,time,json
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
start=time.monotonic()
import sympy as s
import numpy as np
x=s.symbols('x:3'); psi=s.Function('psi')(*x)
g=s.eye(3)*psi**4; iv=s.eye(3)/psi**4
Gamma=[[[s.simplify(sum(iv[k,l]*(s.diff(g[j,l],x[i])+s.diff(g[i,l],x[j])-s.diff(g[i,j],x[l])) for l in range(3))/2) for j in range(3)]for i in range(3)]for k in range(3)]
Ric=[[sum(s.diff(Gamma[k][i][j],x[k])-s.diff(Gamma[k][i][k],x[j])+sum(Gamma[k][k][l]*Gamma[l][i][j]-Gamma[k][j][l]*Gamma[l][i][k] for l in range(3)) for k in range(3)) for j in range(3)]for i in range(3)]
R=s.simplify(sum(iv[i,j]*Ric[i][j] for i in range(3) for j in range(3)))
assert s.simplify(R+8*sum(s.diff(psi,t,2) for t in x)/psi**5)==0
# Dense nodal cotangent bracket, with derivative made by FFT of basis vectors.
n=7; xx=2*np.pi*np.arange(n)/n; modes=np.fft.fftfreq(n)*n
D=np.fft.ifft(1j*modes[:,None]*np.fft.fft(np.eye(n),axis=0),axis=0).real
q=np.cos(xx);p=np.cos(3*xx);X=np.ones(n);Y=np.cos(3*xx)
def grad(Z): return D.T@(p*Z),Z*(D@q)
qx,px=grad(X);qy,py=grad(Y)
bracket=np.mean(qx*py-px*qy)
shift=X*(D@Y)-Y*(D@X)
defect=bracket-np.mean(p*shift*(D@q))
assert abs(defect-1.75)<1e-12
# Wrong sign and wrong derivative scale decisively change the result.
assert abs((-bracket-np.mean(p*shift*(D@q)))-1.75)>.1
# Scalar metric derivative using an independent real central finite difference.
rng=np.random.default_rng(937);errors=[];wrong=[]
for _ in range(5):
 a=rng.normal(size=(3,3));g=np.eye(3)+.02*(a+a.T);v=rng.normal(size=3);w=.7;coef=1.9
 inv=np.linalg.inv(g);root=np.sqrt(np.linalg.det(g));z=inv@v
 stress=-w*w*inv/(4*root)+coef*root*(v@z)*inv/4-coef*root*np.outer(z,z)/2
 def energy(G):return w*w/(2*np.sqrt(np.linalg.det(G)))+coef*np.sqrt(np.linalg.det(G))*(v@np.linalg.solve(G,v))/2
 for i in range(3):
  for j in range(i,3):
   E=np.zeros((3,3));E[i,j]=E[j,i]=1;d=1e-5
   fd=(energy(g+d*E)-energy(g-d*E))/(2*d)
   expected=np.sum(stress*E);errors.append(abs(fd-expected))
   if i!=j:wrong.append(abs(fd-stress[i,j]))
assert max(errors)<1e-7
assert max(wrong)>1e-3
print(json.dumps({'conformal_scalar_curvature':str(R),'dense_nodal_GG_defect':float(defect),'scalar_real_difference_max_error':max(errors),'offdiagonal_half_factor_wrong_max_error':max(wrong),'cpu_seconds':time.process_time(),'wall_seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Independent symbolic conformal and dense nodal bracket checks; scalar real FD check. No universal theorem inferred from samples.'},indent=2))
