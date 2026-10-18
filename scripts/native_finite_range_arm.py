#!/usr/bin/env python3
"""Finite controls of a general arm lemma, not a native coefficient fit."""
from pathlib import Path
import sys,json
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_general_band_control.py']
sys.path.insert(0,str(ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'))
from neutral_general_band_control import green

def main():
 rows=[]
 for lam in [.2,.1,.05]:
  g,N=green(lam);h,_=green(lam,1.1);err=float(np.max(abs(g-h)))
  assert err<1e-8 and g[0,0].imag>.3 and np.max(abs(g))<2
  rows.append(dict(lam=lam,N=N,cutoff_error=err,endpoint_imag=float(g[0,0].imag),max_entry=float(np.max(abs(g)))))
 # Polynomial/Toeplitz equality away from endpoints, fixed cubic test.
 N=40;T=np.diag(np.ones(N-1),1)+np.diag(np.ones(N-1),-1);P=-2*T-.03*T@T+.004*T@T@T
 A=np.diag(np.full(N,-.06))+np.diag(np.full(N-1,-1.988),1)+np.diag(np.full(N-1,-1.988),-1)+np.diag(np.full(N-2,-.03),2)+np.diag(np.full(N-2,-.03),-2)+np.diag(np.full(N-3,.004),3)+np.diag(np.full(N-3,.004),-3)
 assert np.max(abs((A-P)[3:-3]))<1e-14
 result=dict(status='PASS',controls=rows,scope='Chosen cubic correction is a mathematical test, not a native coefficient. Uniform strip and native structural statements are analytical; no full microscopic pole.')
 out=ROOT/'outputs/native_finite_range_arm/result.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
