#!/usr/bin/env python3
"""Check complex endpoint residues, preserving transpose rather than absolute squares."""
from pathlib import Path
import sys,json
import numpy as np
from scipy.linalg import solve_banded
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_range_two_airy.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_host.py']
sys.path.insert(0,str(ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'))
from neutral_range_two_airy import run,alpha
from neutral_slow_host import host

def check(lam,factor=1):
 r=run(lam,factor);N=r['N'];f=lam**2/8;eps=f**(1/3);E=-2+alpha*eps**2+lam**2*complex(*r['coefficient'])
 d=f*(np.arange(N)+3)+lam**2*29/192;h1=-1+lam**2*19/32;h2=-lam**2*13/128
 ab=np.zeros((5,N-1),complex);ab[2]=E-d[1:];ab[1,1:]=-h1;ab[3,:-1]=-h1;ab[0,2:]=-h2;ab[4,:-2]=-h2
 v=np.zeros(N-1,complex);v[:2]=[h1,h2];tail=solve_banded((2,2),ab,v,check_finite=False)
 delta=1e-5;sigmap=(host(E+delta)[0,0]-host(E-delta)[0,0])/(2*delta)
 P11=1/(1+tail@tail-sigmap)
 u=np.array([1.,2.])/np.sqrt(2);G=host(E);coefficient=(u@G[:,0])**2*P11/lam**2
 return dict(lam=lam,N=N,endpoint_residue_over_f=[(P11/f).real,(P11/f).imag],readout_coefficient=[coefficient.real,coefficient.imag],schur_residual=r['schur_residual'])

def main():
 G=host(-2);sigma=G[0,0];u=np.array([1.,2.])/np.sqrt(2);target=(u@G[:,0])**2/(8*(1+sigma)**2);endpoint=1/(1+sigma)**2;rows=[]
 for lam in [.1,.05,.02,.01,.005]:
  r=check(lam);s=check(lam,1.2);diff=float(np.linalg.norm(np.array(r['readout_coefficient'])-s['readout_coefficient']));assert diff<1e-7
  r.update(cutoff_difference=diff,coefficient_error=abs(complex(*r['readout_coefficient'])-target),endpoint_error=abs(complex(*r['endpoint_residue_over_f'])-endpoint));rows.append(r)
 assert rows[-1]['coefficient_error']<rows[0]['coefficient_error']/10
 assert rows[-1]['endpoint_error']<rows[0]['endpoint_error']/10
 result=dict(status='PASS',predicted_coefficient=[target.real,target.imag],predicted_endpoint=[endpoint.real,endpoint.imag],rows=rows,scope='Specified range-two/analytic host numerical controls; full fixed-order leading source and stability are proved separately. Complex residue is not a probability, and no microscopic detector or empirical test is asserted.')
 out=ROOT/'outputs/native_composite_readout/result.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
