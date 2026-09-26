"""Author algebra/measure controls for the prepared-state transfer argument."""
from pathlib import Path
from itertools import product,combinations
import hashlib,json
import numpy as np
import scipy.linalg as la
import sympy as sp
HERE=Path(__file__).resolve().parent;ROWS=[]
def check(name,ok,**details):
 row={'name':name,'pass':bool(ok),**details};ROWS.append(row);print(json.dumps(row));assert ok,name

def matrix_controls():
 rows=[];z=sp.symbols('z');c=sp.Rational(3,5)
 for vec in [(1,0,0),(1,2,0),(1,2,3),(-2,1,3)]:
  K=sp.Matrix(vec);r2=(K.T*K)[0];C=sp.Matrix([[0,-K[2],K[1]],[K[2],0,-K[0]],[-K[1],K[0],0]])
  L=K*K.T/r2;T=sp.eye(3)-L;G=sp.I*c*sp.BlockMatrix([[sp.zeros(3),C],[-C,sp.zeros(3)]]).as_explicit()
  assert G.conjugate().T==-G and G.charpoly(z).as_expr().expand()==(z**2*(z**2+c*c*r2)**2).expand()
  for lam in [sp.Rational(0),sp.Rational(1,2),sp.Rational(4)]:
   S=T+L/(1+lam);cov=sp.diag(S,S)
   assert G*cov+cov*G.conjugate().T==sp.zeros(6)
   Gn=np.array(G,dtype=complex);covn=np.array(cov,dtype=complex)
   for dt in [0.,0.17,0.7,2.]:
    U=la.expm(dt*Gn);actual=U@covn;angle=float(c*sp.sqrt(r2))*dt
    diagonal=np.array(L/(1+lam),dtype=complex)+np.cos(angle)*np.array(T,dtype=complex)
    cross=1j*np.sin(angle)*np.array(C,dtype=complex)/float(sp.sqrt(r2))
    residual=max(la.norm(actual[:3,:3]-diagonal),la.norm(actual[:3,3:]-cross),la.norm(U@covn@U.conj().T-covn))
    assert residual<2e-13;rows.append(residual)
 check('exact_wave_spectrum_and_prepared_covariance_invariance',True,wavevectors=4,lambda_values=3,time_differences=4,max_exponential_residual=float(max(rows)))


def gaussian_integrals():
 q=sp.symbols('q',nonnegative=True);rows=[]
 for m in [1,2,3]:
  for lam in [sp.Rational(0),sp.Rational(1,2),sp.Rational(4)]:
   a=2*m;density=q**(a-1)*sp.exp(-q)/sp.factorial(a-1)
   Z=sp.integrate(sp.exp(-lam*q)*density,(q,0,sp.oo))
   mean=sp.integrate(q*sp.exp(-lam*q)*density,(q,0,sp.oo))/Z
   assert Z==(1+lam)**(-a) and mean==a/(1+lam)
   entropy=sp.simplify(-sp.log(Z)-lam*mean)
   assert sp.simplify(entropy-a*(sp.log(1+lam)-lam/(1+lam)))==0
   rows.append({'m':m,'lambda':str(lam),'Z':str(Z),'mean_Q':str(mean),'entropy':str(entropy)})
 check('exact_gamma_integrals_for_preparation_and_entropy',True,cases=rows)


def site_moments():
 rhoA=sp.Rational(1,3);rhoB=sp.Rational(1,2);features=[];prob=[]
 labels=[('vac',(0,0,0))]+[('A',tuple(s if i==j else 0 for i in range(3))) for j in range(3) for s in (-1,1)]+[('B',x) for x in product((-1,1),repeat=3)]
 for kind,tag in labels:
  e=sp.Matrix(tag) if kind=='A' else sp.zeros(3,1);b=sp.Matrix(tag) if kind=='B' else sp.zeros(3,1)
  p=1-rhoA-rhoB if kind=='vac' else rhoA/6 if kind=='A' else rhoB/8;prob.append(p)
  shape=[int(kind=='A'),int(kind=='B'),e[0]**2-e[1]**2,e[0]**2+e[1]**2-2*e[2]**2,b[0]*b[1],b[0]*b[2],b[1]*b[2],b[0]*b[1]*b[2]]
  features.append(list(e/sp.sqrt(rhoA/3))+list(b/sp.sqrt(rhoB))+shape)
 F=sp.Matrix(features);p=sp.Matrix(prob);mean=F.T*p;cov=F.T*sp.diag(*prob)*F-mean*mean.T
 assert cov[:6,:6]==sp.eye(6) and cov[:6,6:]==sp.zeros(6,8)
 assert cov.rank()==14 and cov[6:,6:].rank()==8
 assert all(v>0 for v in cov[6:,6:].eigenvals())
 raw_e=F[:,:3]*sp.sqrt(rhoA/3);raw_b=F[:,3:6]*sp.sqrt(rhoB)
 var_e=sp.trace(raw_e.T*sp.diag(*prob)*raw_e)/2
 var_b=sp.trace(raw_b.T*sp.diag(*prob)*raw_b)/2
 assert var_e==rhoA/2 and var_b==3*rhoB/2
 check('fifteen_label_orthogonality_spectators_and_local_charge',True,covariance_rank=14,spectator_rank=8,spectator_covariance_eigenvalues={str(x):m for x,m in cov[6:,6:].eigenvals().items()},local_centered_divergence_variances=[str(var_e),str(var_b)],expected_variances=[str(rhoA/2),str(3*rhoB/2)])


def finite_path_density_control():
 # Separate four-site reversible chain: validates measure-transfer algebra,
 # not the actual fifteen-label microscopic propagation theorem.
 states=list(combinations(range(4),2));index={frozenset(s):i for i,s in enumerate(states)};L=sp.zeros(6)
 for i,occupied in enumerate(states):
  for x in range(4):
   y=(x+1)%4
   if (x in occupied)==(y in occupied):continue
   new=set(occupied);new.symmetric_difference_update({x,y});L[i,index[frozenset(new)]]+=1
  L[i,i]=-sum(L[i,j] for j in range(6) if j!=i)
 pi=sp.ones(6,1)/6;F=np.array([sum(np.exp(-.5j*np.pi*x) for x in state)/2 for state in states])
 g=sp.Matrix([sp.Rational(1,2) if abs(F[i])>.1 else 1 for i in range(6)]);Z=(pi.T*g)[0];mu=sp.matrix_multiply_elementwise(pi,g)/Z
 assert Z==sp.Rational(2,3) and pi.T*L==sp.zeros(1,6) and mu.T*L!=sp.zeros(1,6)
 rows=[]
 for t in [.03,.2,1.,3.]:
  P=la.expm(float(t)*np.array(L,dtype=float))
  for omega in [0.,.7]:
   error=abs(F[None,:]-np.exp(1j*omega*t)*F[:,None])**2
   reference=float(np.sum(np.array(pi,dtype=float).reshape(-1,1)*P*error))
   prepared=float(np.sum(np.array(mu,dtype=float).reshape(-1,1)*P*error))
   assert prepared<=reference/float(Z)+1e-13
   rows.append({'time':t,'omega':omega,'reference_error':reference,'prepared_error':prepared,'upper_bound':reference/float(Z)})
 check('finite_path_density_bound_without_false_stationarity',True,states=6,Z=str(Z),prepared_stationarity_residual=[str(x) for x in mu.T*L],cases=rows)


def main():
 matrix_controls();gaussian_integrals();site_moments();finite_path_density_control()
 sources={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),HERE/'PREPARED_TRANSVERSE_EULER_STATE.md',HERE.parent/'campaign12h/IMMUTABLE_TRANSVERSE_MAXWELL_CONSTRUCTION.md',HERE.parent/'campaign12h/CONTEXT_EXCHANGE_FLUCTUATION_DERIVATION.md']}
 result={'status':'author checks; reference microscopic theorem imported with its hypotheses; independent review pending','sources_sha256':sources,'rows':ROWS,'all_pass':all(r['pass'] for r in ROWS)}
 (HERE/'PREPARED_TRANSVERSE_STATE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'groups':len(ROWS),'all_pass':result['all_pass'],'sources_sha256':sources},indent=2))
if __name__=='__main__':main()
