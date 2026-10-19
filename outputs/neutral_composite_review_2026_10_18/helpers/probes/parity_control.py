"""Uniform bound on even-parity projection corrections to offdiagonal bilinear weights."""
from pathlib import Path
import numpy as np,itertools,json
from scipy.special import expit
R=Path(__file__).resolve().parents[4];d=json.loads((R/'data/collective_corner_response/candidate.json').read_text());sh=np.array(d['shifts']);bl=np.array(d['blocks']['real'])+1j*np.array(d['blocks']['imag']);mu=d['chemical_potential_development_value'];rows=[]
for N in [4,8,12,24]:
 k=2*np.pi/N*(np.array(list(itertools.product(range(N),repeat=3)))+.5);E=np.linalg.eigvalsh(np.einsum('ks,sij->kij',np.exp(1j*k@sh.T),bl)).ravel()
 for T in [.03,.01]:
  logs=np.sort(np.log(np.maximum(abs(np.tanh((E-mu)/(2*T))),np.finfo(float).tiny)))
  logr=logs.sum();logrest=logs[2:].sum();rbound=np.exp(logr);eps=(np.exp(logr)+np.exp(logrest))/(1-rbound)
  row={'N':N,'T':T,'log_abs_parity_expectation':float(logr),'worst_log_abs_parity_excluding_two_modes':float(logrest),'uniform_relative_weight_error_bound':float(eps) if eps>0 else None,'log_relative_weight_error_bound':float(np.logaddexp(logr,logrest)-np.log1p(-rbound))};rows.append(row);print(row)
# Independent brute-force four-mode occupation sum validates exact pair formula.
f=np.array([.17,.32,.61,.83]);r=np.prod(1-2*f);checks=[]
for a in range(4):
 for b in range(4):
  if a==b:continue
  z=w=0.
  for bits in itertools.product([0,1],repeat=4):
   if sum(bits)%2:continue
   pr=np.prod([f[i] if n else 1-f[i] for i,n in enumerate(bits)]);z+=pr;w+=pr*bits[a]*(1-bits[b])
  rest=np.prod([1-2*f[i] for i in range(4) if i not in [a,b]])
  pred=f[a]*(1-f[b])*(1-rest)/(1+r);checks.append(abs(w/z-pred)<1e-14)
assert all(checks)
Path(__file__).with_name('parity_control.json').write_text(json.dumps({'scope':'Even total fermion parity only, one fixed gauge/holonomy sector; thermal mu,T remain supplied. Excludes diagonal density operators. Tiny products may underflow; log values preserved.','rows':rows,'brute_force_pair_controls':len(checks),'passed':int(sum(checks))},indent=2)+'\n')
