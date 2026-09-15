from pathlib import Path
import json
import sympy as s
import numpy as np

def exact_models():
 rows=[]
 for label,L,N in [('rectangular',s.Matrix([[1,0],[s.I/2,1],[s.Rational(1,3),-s.I/4]]),s.diag(1,2,3)),('square',s.Matrix([[1,s.I/3],[-s.Rational(1,4),2]]),s.diag(s.Rational(1,2),2))]:
  d=L.cols;q=L.H*N.inv()*L;c0=q.inv()
  for alpha in (s.Rational(1,2),s.Rational(1,5)):
   c=(q+alpha*s.eye(d)).inv();prior=s.diag(alpha**-1*s.eye(d),N);z=(alpha*c).row_join(-c*L.H*N.inv());y=L.row_join(s.eye(L.rows))
   assert s.simplify(z*prior*z.H-c)==s.zeros(d,d);assert s.simplify(z*prior*y.H)==s.zeros(d,L.rows)
   actual_cond=alpha**-1*s.eye(d)-alpha**-2*L.H*(N+alpha**-1*L*L.H).inv()*L
   assert s.simplify(actual_cond-c)==s.zeros(d,d)
   noise=-c0*L.H*N.inv();assert s.simplify(noise*N*noise.H-c0)==s.zeros(d,d)
   if L.rows==L.cols:assert s.simplify(noise+L.inv())==s.zeros(d,d)
   wrong=(-c*L.H*N.inv()).row_join(s.zeros(d,0));missing_prior_cov=wrong*N*wrong.H
   assert s.simplify(c-missing_prior_cov-alpha*c*c)==s.zeros(d,d) and s.simplify(c-missing_prior_cov)!=s.zeros(d,d)
   rows.append(dict(model=label,alpha=str(alpha),source_dimension=d,observation_dimension=L.rows,posterior_det=str(s.factor(c.det())),target_det=str(s.factor(c0.det())),independent_of_observation=True,proper_noise_only=True,omitted_root_covariance_nonzero=True))
 return rows

def local_truncations():
 n=4;shift=s.zeros(n)
 for j in range(n):shift[j,(j+1)%n]=1
 L=s.eye(n)-s.I*shift/3;q=L.H*L;m=s.Rational(4,9);M=s.Rational(16,9);rows=[]
 assert set(q.eigenvals())=={s.Rational(4,9),s.Rational(10,9),s.Rational(16,9)}
 for alpha in (s.Rational(0),s.Rational(1,2)):
  A=q+alpha*s.eye(n);a=m+alpha;b=M+alpha;P=s.eye(n)-A/b;c=A.inv();rho=1-a/b
  for K in (0,1,2,4,8):
   ck=sum((P**j for j in range(K+1)),s.zeros(n))/b;error=s.simplify((c-ck)*A*(c-ck).H);formula=s.simplify(c*P**(2*K+2));assert error==formula
   bound=rho**(2*K+2)/a;ev=np.linalg.eigvalsh(np.array(error).astype(complex));assert max(ev)<=float(bound)+1e-13
   rows.append(dict(alpha=str(alpha),K=K,trace_error=str(s.factor(s.trace(error))),maximum_eigen_error=float(max(ev)),per_component_bound=str(bound),radius_at_most=K))
 return rows

def branch_weights():
 q1=s.eye(2);q2=4*s.eye(2);prior=[s.Rational(1,2)]*2;mass=[q1.det()**-1,q2.det()**-1];weights=[s.factor(x/sum(mass)) for x in mass]
 assert weights==[s.Rational(16,17),s.Rational(1,17)] and weights!=prior
 return dict(prior_weights=[str(x) for x in prior],readout_weights=[str(x) for x in prior],determinant_weights=[str(x) for x in weights])

def run():return dict(exact_gaussian_models=exact_models(),finite_range_truncations=local_truncations(),branch_weight_boundary=branch_weights(),qualification='Personal exact covariance and finite polynomial checks; generic proofs, infinite-volume readout locality and native-observable identification are not established by finite execution.')
if __name__=='__main__':
 rows=run();Path(__file__).with_name('BLOCK20_CHECKS.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
