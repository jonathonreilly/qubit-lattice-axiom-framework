import sys,json,numpy as np
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from scipy.optimize import root
from scipy.special import ai_zeros
from neutral_slow_host import host
from neutral_corrected_fast_boundary import resolvent

def run(lam):
 f=lam**2/8;N=int(20*f**(-1/3));h1=-1+lam**2*19/32;h2=-lam**2*13/128
 H=np.diag(f*(np.arange(N)+3)+lam**2*29/192)+np.diag(np.full(N-1,h1),1)+np.diag(np.full(N-1,h1),-1)+np.diag(np.full(N-2,h2),2)+np.diag(np.full(N-2,h2),-2)
 a=host(-2)[0,0];a=a/(1+a);alpha=abs(ai_zeros(1)[0][0]);pred=-2+alpha*f**(2/3)+f*(2+a)+lam**2*109/96
 def equation(e):
  R,_,_=resolvent(lam*(e-4),lam);V=np.array([[0.,0.],[-1.,0.],[-1.,-2.],[0.,0.]]);M=V.T@R@V;g=host(e);G=np.linalg.solve(np.eye(2)-g@(lam*M),g)
  # Schur complement of tail avoids tiny determinant and preserves boundarycondition.
  hh=e*np.eye(N)-H;tail=np.linalg.solve(hh[1:,1:],hh[1:,0]);return hh[0,0]-hh[0,1:]@tail-G[0,0]
 sol=root(lambda v:[equation(complex(*v)).real,equation(complex(*v)).imag],[pred.real,pred.imag],tol=1e-10);e=complex(*sol.x)
 return dict(lam=lam,e=[e.real,e.imag],residual=abs(equation(e)),success=bool(sol.success),real_lambda4_coefficient=(e.real+2-alpha*f**(2/3))/lam**2,width_over_lambda4=-2*e.imag/lam**2,predicted_real_lambda4=109/96+(2+a.real)/8,predicted_width=-a.imag/4)
if __name__=='__main__':
 rows=[]
 for lam in [.2,.1,.05,.025,.02]:
  row=run(lam);rows.append(row);print(row,flush=True)
 open('/private/tmp/neutral_native_order4_pole.json','w').write(json.dumps(dict(rows=rows,scope='Specifiedmodel includesnative longslowK4 andcompletefastK2; finiteboundaryhighertermsandfullSWremainderabsent'),indent=2)+'\n')
