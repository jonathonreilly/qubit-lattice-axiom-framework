#!/usr/bin/env python3
"""Exact Gaussian constraint algebra; the ordered conditioning proof is separate."""
from pathlib import Path
import hashlib,json
import sympy as s
checks=[]
def check(name,value):
 assert bool(value),name
 checks.append(dict(name=name,passed=True));print('PASS:',name,flush=True)
k=s.Matrix([1,2,2]);PL=k*k.T/9;PT=s.eye(3)-PL
G=(k.T/3).row_join(s.zeros(1,3)).col_join(s.zeros(1,3).row_join(k.T/3))
conditioned=s.eye(6)-G.T*(G*G.T).inv()*G
check('conditioning_removes_only_longitudinal_variance',conditioned==s.diag(PT,PT))
C=s.Matrix([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]])
D=s.zeros(3).row_join(s.I*C).col_join((-s.I*C).row_join(s.zeros(3)))
check('curl_drift_preserves_Gauss_subspace',G*D==s.zeros(2,6) and D*conditioned==D)
t,st,v0=s.symbols('t s v0',nonnegative=True);beta=s.symbols('beta',positive=True)
rho=lambda u:1-v0*s.exp(-14*beta*u)
noise_integral=s.integrate(8*beta*v0*s.exp(-14*beta*t),(t,st,t))
check('single_birth_longitudinal_noise_after_preparation',s.simplify(noise_integral-s.Rational(4,7)*(rho(t)-rho(st)))==0)
result=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,
 scope='Exact covariance and curl identities. No simultaneous conditioning/lattice limit or microscopic Gauss constraint is inferred.')
(Path(__file__).resolve().parent/'GAUSS_PREPARATION_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print('TOTAL:',len(checks),'PASS',flush=True)
