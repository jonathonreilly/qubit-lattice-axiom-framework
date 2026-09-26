#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
import sympy as s
import mpmath as mp
HERE=Path(__file__).resolve().parent
q=s.Matrix([1,2,3]);P=s.eye(3)-q*q.T/(q.T*q)[0]
assert P*P==P and s.trace(P)==2 and P*q==s.zeros(3,1)
mp.mp.dps=100
results=[]
for value in ['0.2','1','6','18']:
 sig=mp.mpf(value)
 direct_weights=[mp.exp(-mp.mpf(n*n)/(2*sig)) for n in range(-150,151)]
 direct=sum(mp.mpf(n*n)*w for n,w in zip(range(-150,151),direct_weights))/sum(direct_weights)/sig
 dual_weights=[mp.exp(-2*mp.pi**2*sig*n*n) for n in range(-100,101)]
 dual=1-4*mp.pi**2*sig*sum(mp.mpf(n*n)*w for n,w in zip(range(-100,101),dual_weights))/sum(dual_weights)
 assert abs(direct-dual)<mp.mpf('1e-90')
 r=mp.exp(-2*mp.pi**2*sig);bound=8*mp.pi**2*sig*r*(1+r)/(1-r)**3
 assert 1-dual<=bound+mp.mpf('1e-95')
 results.append({'sigma_squared':value,'ratio':mp.nstr(direct,90),'one_minus_ratio_upper_bound':mp.nstr(bound,20),'direct_dual_error':mp.nstr(abs(direct-dual),10)})
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'transverse_projector_trace':2,'zero_mode_components':3,'discrete_Gaussian':results,'scope':'Added Gaussian benchmark only; no record-ensemble or confidence-coverage theorem.'}
(HERE/'BENCHMARK_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
