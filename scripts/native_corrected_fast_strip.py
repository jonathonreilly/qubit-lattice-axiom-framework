#!/usr/bin/env python3
"""Numerical controls of the specified coefficient model; not full-H pole proof."""
from pathlib import Path
import sys,json
import numpy as np
from scipy.linalg import eigh
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_corrected_fast_host.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_corrected_fast_boundary.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_native_order4_pole.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_host.py']
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
sys.path.insert(0,str(PACK))
from neutral_corrected_fast_host import host
from neutral_corrected_fast_boundary import arm
from neutral_native_order4_pole import run as pole

def run():
 rows=[]
 n=800;c=np.cos(2*np.pi*(np.arange(n)+.5)/n);x=c[:,None];y=c[None,:];d=x-y;d2=2*(x*x-y*y)
 for lam in [.05,.2]:
  z=-6*lam+.15j;den=z+4*(x+y)+lam*d*d
  direct=np.array([[np.mean(d*d/den),np.mean(d*d2/den)],[np.mean(d*d2/den),np.mean(d2*d2/den)]])
  error=float(np.max(abs(host(z,lam)-direct)));assert error<1e-8
  zz=-6*lam-.06j*lam**3;g=arm(zz,lam);err=float(np.max(abs(g-arm(zz,lam,1.2))));assert err<1e-9
  w=np.array([-2.,-lam/4]);assert np.imag(w@g@w)>0
  N=64;eps=lam/4;f=lam**3/16;T=np.diag(np.ones(N-1),1)+np.diag(np.ones(N-1),-1);v=f*(np.arange(N)+2)-2*lam
  A=np.diag((np.sqrt(1+eps*(v+6*lam))-1)/eps);D=2*np.eye(N)+eps*A;C=D+eps*T;L=T-A;cs,U=eigh(C);sq=(U*np.sqrt(cs))@U.T
  H0=-2*T-eps*T@T+np.diag(v);R=H0+6*lam*np.eye(N)+sq@L@sq;comm=lambda a,b:a@b-b@a
  identity=float(np.linalg.norm(H0+6*lam*np.eye(N)+(C@L+L@C)/2,2));bound=float(np.linalg.norm(comm(C,comm(C,L)),2)/(8*cs[0]));actual=float(np.linalg.norm(R,2))
  assert identity<1e-11 and actual<bound+1e-11
  rows.append(dict(lam=lam,host_error=error,arm_cutoff_error=err,directional_imag=float(np.imag(w@g@w)),identity_error=identity,remainder=actual,functional_bound=bound))
 poles=[pole(lam) for lam in [.1,.05]]
 assert max(r['residual'] for r in poles)<1e-8
 assert abs(poles[-1]['real_lambda4_coefficient']-poles[-1]['predicted_real_lambda4'])<.004
 assert abs(poles[-1]['width_over_lambda4']-poles[-1]['predicted_width'])<.003
 result=dict(status='PASS',controls=rows,poles=poles,scope='Specified projected model only; finite controls do not prove uniform strip or full native resonance')
 out=ROOT/'outputs/native_corrected_fast_strip/result.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':run()
