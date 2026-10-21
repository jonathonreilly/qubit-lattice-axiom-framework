"""Mathematical strip control; cubic kinetic coefficient is a test choice, not native science."""
import numpy as np,json,time
from scipy.linalg import solve_banded

def green(lam,factor=1.):
 f=lam**3/16;N=int(np.ceil(12*factor/f));z=-6*lam-.06j*lam**3;n=np.arange(N)+1
 diag=f*(n+1)-2*lam-lam/2;diag[0]+=lam/4;diag[-1]+=lam/4
 h1=np.full(N-1,-2+.3*lam**2);h1[0]-=.1*lam**2;h1[-1]-=.1*lam**2
 h2=np.full(N-2,-lam/4);h3=np.full(N-3,.1*lam**2)
 ab=np.zeros((7,N),complex);ab[3]=z-diag
 for k,h in [(1,h1),(2,h2),(3,h3)]:ab[3-k,k:]=-h;ab[3+k,:-k]=-h
 rhs=np.zeros((N,2),complex);rhs[0,0]=1;rhs[1,1]=1
 u=solve_banded((3,3),ab,rhs,overwrite_ab=True,overwrite_b=True,check_finite=False)
 return u[:2].copy(),N
if __name__=='__main__':
 rows=[]
 for lam in [.2,.1,.05]:
  start=time.time();g,N=green(lam);gg,_=green(lam,1.1);err=np.max(abs(g-gg));assert err<1e-8 and g[0,0].imag>0
  row=dict(lam=lam,N=N,g=[[[z.real,z.imag] for z in r] for r in g],cutoff_error=float(err),seconds=time.time()-start);rows.append(row);print(row,flush=True)
 open(__file__.replace('.py','.json'),'w').write(json.dumps(dict(rows=rows,scope='Chosen cubic correction tests general mathematical lemma, not a derived native coefficient'),indent=2)+'\n')
