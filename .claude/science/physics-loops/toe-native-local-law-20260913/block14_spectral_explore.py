from pathlib import Path
from itertools import combinations
import numpy as np,json
from scipy.linalg import eigh_tridiagonal
from scipy import sparse as sp
from scipy.sparse.linalg import eigsh
from scipy.special import hyp1f1
from scipy.optimize import brentq
P=Path(__file__).resolve().parent

def box_energy(s):
 fun=lambda E:hyp1f1((1-E)/4,.5,2*s*s)
 lo=1.;f0=fun(lo)
 for hi in np.linspace(1.00001,1+np.pi*np.pi/(2*s*s)+2*s*s,200):
  if fun(hi)*f0<0:return brentq(fun,lo,hi,xtol=1e-13)
 raise RuntimeError(s)
def pure(g,S,step=1,k=4):
 n=np.arange(-S,S+1);H=sp.diags(2*g*g*n*n+1/(g*g),format='csr');off=-np.ones(len(n)-step)/(2*g*g);H+=sp.diags([off,off],[-step,step],format='csr');return eigsh(H,k=k,which='SA',return_eigenvectors=False,tol=1e-11)[::-1]
# Four-site cycle, one orbital/site, integer staggered background, two particles.
eta=np.array([0,1,0,1]);states=[sum(1<<i for i in pair) for pair in combinations(range(4),2)];fi={s:i for i,s in enumerate(states)};ons=np.array([.17,-.31,.26,-.12]);hops=[1.,.7,1.2,.9]
E0=[]
for state in states:
 rho=np.array([(state>>j)&1 for j in range(4)])-eta;E0.append(np.array([rho[0],rho[0]+rho[1],sum(rho[:3]),0]))
def fermion_move(state,x,y):
 if not(state>>y&1) or state>>x&1:return None
 sign=(-1)**((state&((1<<y)-1)).bit_count());s=state^(1<<y);sign*=(-1)**((s&((1<<x)-1)).bit_count());return s|(1<<x),sign
free=np.diag([sum(ons[j] for j in range(4) if state>>j&1) for state in states]).astype(float)
for f,state in enumerate(states):
 for edge,hop in enumerate(hops):
  move=fermion_move(state,edge,(edge+1)%4)
  if move is not None:
   target,sign=move;ff=fi[target];free[ff,f]+=hop*sign;free[f,ff]+=hop*sign
free_e=np.linalg.eigvalsh(free)
def coupled(g,S):
 basis=[]
 for f in range(6):
  for n in range(-S-int(min(E0[f])),S-int(max(E0[f]))+1):basis.append((f,n))
 ix={v:j for j,v in enumerate(basis)};rr=[];cc=[];vv=[]
 for col,(f,n) in enumerate(basis):
  rr.append(col);cc.append(col);vv.append(float(2*g*g*n*n+g*g*n*sum(E0[f])+.5*g*g*np.dot(E0[f],E0[f])+1/g**2+free[f,f]))
  if (f,n+1) in ix:
   row=ix[(f,n+1)];rr.extend([row,col]);cc.extend([col,row]);vv.extend([-1/(2*g*g)]*2)
  state=states[f]
  for edge,hop in enumerate(hops):
   move=fermion_move(state,edge,(edge+1)%4)
   if move is not None:
    target,sign=move;ff=fi[target];nn=n+(edge==3)
    if (ff,nn) in ix:
     row=ix[(ff,nn)];rr.extend([row,col]);cc.extend([col,row]);vv.extend([hop*sign]*2)
 H=sp.csr_matrix((vv,(rr,cc)),shape=(len(basis),len(basis)));return np.sort(eigsh(H,k=4,which='SA',return_eigenvectors=False,tol=1e-11))
records=[]
for s in [1.,2.,3.]:
 limit=box_energy(s)
 for S in [20,40,80]:
  g=s/(S+1);e=pure(g,S);ec=coupled(g,S)
  records.append(dict(s=s,S=S,g=g,pure=e.tolist(),coupled=ec.tolist(),box_ground=limit,coupled_limit_ground=limit+float(free_e[0])))
full=[]
for g in [.4,.2,.1,.05]:
 S=int(np.ceil(np.log(1/g)/g));e=coupled(g,S);full.append(dict(g=g,S=S,scaled_cutoff=g*S,coupled=e.tolist(),target_ground=1+float(free_e[0])))
double=[]
for g in [.2,.1,.05]:double.append(dict(g=g,eigenvalues=pure(g,int(np.ceil(4/g)),step=2).tolist()))
result=dict(free_matter_spectrum=free_e.tolist(),fixed_box=records,full_line=full,nonprimitive_double_copy=double)
(P/'BLOCK14_SPECTRAL_EXPLORATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
