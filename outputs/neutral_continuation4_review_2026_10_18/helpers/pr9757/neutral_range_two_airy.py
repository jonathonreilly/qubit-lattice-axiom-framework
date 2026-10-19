"""Specified range-two Airy model: growing cutoff and outgoing host, not full nativeH."""
import sys,json,numpy as np
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from neutral_slow_host import host
from scipy.linalg import solve_banded
from scipy.optimize import root
from scipy.special import ai_zeros
alpha=abs(ai_zeros(1)[0][0]);sigma0=host(-2)[0,0];a0=sigma0/(1+sigma0);pred=109/96+(2+a0)/8

def run(lam,factor=1):
 f=lam**2/8;eps=f**(1/3);N=int(np.ceil(factor*(18+4*np.log(1/lam))/eps));d=f*(np.arange(N)+3)+lam**2*29/192;h1=-1+lam**2*19/32;h2=-lam**2*13/128;v=np.zeros(N-1,complex);v[:2]=[-h1,-h2]
 def eq(b):
  e=-2+alpha*eps**2+lam**2*complex(*b);ab=np.zeros((5,N-1),complex);ab[2]=e-d[1:];ab[1,1:]=-h1;ab[3,:-1]=-h1;ab[0,2:]=-h2;ab[4,:-2]=-h2
  t=solve_banded((2,2),ab,v,overwrite_ab=True,check_finite=False);F=e-d[0]-host(e)[0,0]-v@t;return [F.real,F.imag]
 sol=root(eq,[pred.real,pred.imag],tol=1e-10);b=complex(*sol.x);res=float(np.linalg.norm(eq(sol.x)));assert res<1e-8
 return dict(lam=lam,N=N,coefficient=[b.real,b.imag],predicted=[pred.real,pred.imag],coefficient_error=abs(b-pred),error_over_lambda_two_thirds=abs(b-pred)/lam**(2/3),schur_residual=res,width_coefficient=-2*b.imag,predicted_width=-2*pred.imag)
if __name__=='__main__':
 rows=[]
 for lam in [.2,.1,.05,.02,.01,.005]:
  r=run(lam);s=run(lam,1.2);r['cutoff_coefficient_difference']=float(np.linalg.norm(np.array(r['coefficient'])-s['coefficient']));assert r['cutoff_coefficient_difference']<1e-7;rows.append(r);print(r,flush=True)
 open(__file__.replace('.py','.json'),'w').write(json.dumps(dict(rows=rows,scope='Specified slowK4/analytic outgoinghost model only. Finite cutoff comparisons supplement proof, not independent asymptotic certificate'),indent=2)+'\n')
