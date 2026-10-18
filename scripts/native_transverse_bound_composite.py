from pathlib import Path
import sys,json,numpy as np
from scipy.sparse.linalg import eigsh
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native';sys.path.insert(0,str(P))
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/TRANSVERSE_BOUND_STATE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_transverse_bound_model.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_transverse_physical_control.py']
from neutral_transverse_bound_model import matrix
from neutral_transverse_physical_control import run_checks
physical=run_checks();rows=[]
for L in [30,60]:
 H,s,idx=matrix(L);v=np.zeros(len(s));r=1/np.sqrt(2)
 for x in range(-L,L+1):v[idx[(x,1)]]=.5*r**abs(x)
 for ell in range(2,L+2):v[idx[('y',ell)]]=.5*(-r)**(ell-1)
 residual=np.linalg.norm(H@v+3*np.sqrt(2)*v);assert residual<4*r**L+1e-12
 for b in [0,.001,.005,.01,.02]:
  H,s,idx=matrix(L,b=b);e,U=eigsh(H,k=1,which='SA',tol=1e-12);q=U[:,0];q*=np.sign(q[idx[(0,1)]]);src=-q[idx[(1,0)]]+b*q[idx[(0,1)]]
  if b==0:assert abs(e[0]+3*np.sqrt(2))<1e-8 and abs(src)<1e-9
  if b==.001:
   assert abs(src/b+1.5)<2e-4
   assert abs((e[0]+3*np.sqrt(2))/b**2+25/np.sqrt(2))<.002
  rows.append(dict(L=L,b=b,energy=float(e[0]),source_over_lambda=float(src),analytic_anchor_residual=float(residual)))
# Geometric sums independently evaluate the exact second-order energy input.
n=np.arange(1,101);Spp=np.sum(r**(n[:,None]+n[None,:]+abs(n[:,None]-n[None,:])));n=np.arange(-100,101);Sabs=np.sum(r**(abs(n[:,None])+abs(n[None,:])+abs(n[:,None]-n[None,:])));assert abs(Spp-3)<1e-12 and abs(Sabs-13)<1e-12
out=dict(status='bounded-support',physical_bit_Bloch_controls=physical,fibers=rows,geometric_sums=[float(Spp),float(Sabs)],scope='Complete compact layer-even N4 K1 bound eigenstate and leading original source; supplied H/reference, no full-H or empirical scalar claim')
p=ROOT/'outputs/native_transverse_bound_composite/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
