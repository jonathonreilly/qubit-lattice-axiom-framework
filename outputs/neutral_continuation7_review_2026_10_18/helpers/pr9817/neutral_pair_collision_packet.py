AUDIT_TIMEOUT_SEC=300
import numpy as np,json,time
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply
from fractions import Fraction as F
rows=[]
for k,R in ((.25,192),(.2,256),(.15,512)):
 st=time.time();T=k**-3;n=R*R;p=2*np.pi*np.fft.fftfreq(R);px,py=np.meshgrid(p,p,indexing='ij');rad=np.sqrt(px*px+py*py)/k
 phi=np.zeros_like(rad);mask=(rad>1)&(rad<1.5);s=(rad[mask]-1)/.5;phi[mask]=np.exp(-1/(s*(1-s)));phi/=np.linalg.norm(phi)
 disp=4-2*np.cos(px)-2*np.cos(py);incoming=np.fft.ifft2(np.exp(1j*T*disp)*phi,norm='ortho').reshape(-1)
 coords=[(i if i<=R//2 else i-R,j if j<=R//2 else j-R) for i in range(R) for j in range(R)]
 core=np.array([abs(x)+abs(y)<=4 and sorted((abs(x),abs(y)))!=[0,4] for x,y in coords]);rr=[];cc=[];vv=[]
 for a,(x,y) in enumerate(coords):
  if core[a]:rr.append(a);cc.append(a);vv.append(16);continue
  ab=tuple(sorted((abs(x),abs(y)),reverse=True));u={(4,0):-8/17,(4,1):-4/17,(3,2):30305/161109}.get(ab,0)
  rr.append(a);cc.append(a);vv.append(4+u)
  i,j=divmod(a,R)
  for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
   b=((i+di)%R)*R+(j+dj)%R
   if not core[b]:rr.append(a);cc.append(b);vv.append(-1)
 H=coo_matrix((vv,(rr,cc)),shape=(n,n)).tocsr();out=expm_multiply((-2j*T)*H,incoming,traceA=(-2j*T)*H.diagonal().sum())
 final=np.exp(1j*T*disp)*np.fft.fft2(out.reshape(R,R),norm='ortho');L=np.zeros_like(disp);L[mask]=np.log(.1502110793901342/disp[mask]);S=np.ones_like(disp,dtype=complex);S[mask]=(L[mask]-1j*np.pi)/(L[mask]+1j*np.pi)
 rows.append(dict(k=k,R=R,T=T,norm_error=float(abs(np.linalg.norm(final)-1)),collision_norm=float(np.linalg.norm(final-phi)),threshold_prediction_norm=float(np.linalg.norm((S-1)*phi)),threshold_difference=float(np.linalg.norm(final-S*phi)),initial_core_weight=float(np.linalg.norm(incoming[core])**2),elapsed=time.time()-st))
 print(json.dumps(rows[-1]),flush=True)
open(__file__.replace('.py','.json'),'w').write(json.dumps(rows,indent=2))
