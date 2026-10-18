#!/usr/bin/env python3
"""Finite representation and quadrature controls; not a numerical gap proof."""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import quad
from scipy.special import erfc
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/STATIC_NEUTRAL_RESPONSE_PROOF.md']

def main():
 rows=[]
 for L in [2,4,6]:
  n=2*L-1; D=1<<n
  # Fix last b sign. Flipping a row is a bit flip; last b flip
  # equals all row flips and all other b flips in this gauge.
  generators=[1<<i for i in range(n)]+[D-1]
  ranks={}
  for k in range(D):
   label=tuple((-1)**((k&g).bit_count()) for g in generators)
   assert np.prod(label)==1
   ranks[label]=ranks.get(label,0)+1
  assert len(ranks)==D and set(ranks.values())=={1}
  # Check actual Y-plane phase on every aligned-column pattern.
  for s in range(D):
   a=[(s>>x)&1 for x in range(L)];b=[(s>>(L+y))&1 for y in range(L-1)]+[0]
   for y in range(L):
    down=L*sum(a[x]^b[y] for x in range(L))
    assert (1j)**(L*L)*(-1)**down==1
  rows.append(dict(L=L,characters=D,each_rank=1))
 errors=[]
 for sigma in [.3,1,2]:
  for E in [.1,.7,2,5]:
   value,err=quad(lambda t:erfc(sigma*t/np.sqrt(2))*np.sin(E*t),0,np.inf,epsabs=2e-12,limit=300)
   exact=-np.expm1(-E*E/(2*sigma*sigma))/E
   errors.append(abs(value-exact))
 assert max(errors)<2e-10
 # Filter error bound checked on positive and signed cross spectra.
 rng=np.random.default_rng(875721); maximum=0
 for _ in range(200):
  E=1+rng.random(20)*8; a=rng.normal(size=20)+1j*rng.normal(size=20);a/=np.linalg.norm(a)
  b=rng.normal(size=20)+1j*rng.normal(size=20);b/=np.linalg.norm(b);sigma=.8
  diff=abs(2*np.real(np.sum(a*b*np.exp(-E**2/(2*sigma**2))/E)))
  bound=2*np.exp(-1/(2*sigma**2));assert diff<=bound
  maximum=max(maximum,diff/bound)
 out=dict(status='bounded-support',representation=rows,max_fourier_error=max(errors),cross_spectral_bound_max_ratio=maximum,scope='Finite representation and filter controls only; no numerical microscopic gap or observed-force test')
 p=ROOT/'outputs/native_static_response/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
