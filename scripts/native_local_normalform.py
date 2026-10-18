#!/usr/bin/env python3
"""Finite dense control of exact local-normal-form recursion."""
from pathlib import Path
import sys,json
import numpy as np
from scipy.linalg import eigh,expm
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_local_normalform.py']
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
sys.path.insert(0,str(PACK))
from neutral_local_normalform import model,construct,run

def main():
 rows=run();H0,V=model();h,gens=construct(H0,V,4);lam=.08;U=np.eye(len(H0))
 for k,S in enumerate(gens,1):U=expm(lam**k*S)@U
 H=U@(np.diag(H0)+lam*V)@U.T;B=sum(lam**j*q for j,q in enumerate(h));R=H-B
 E,W=eigh(H);e,w=eigh(B);O=np.diag(1-2*(np.arange(len(H0))&1));time_rows=[]
 for t in [.5,2,8]:
  A=(W*np.exp(-1j*t*E))@W.T;b=(w*np.exp(-1j*t*e))@w.T
  error=float(np.linalg.norm(A.conj().T@O@A-b.conj().T@O@b,2));bound=float(2*t*np.linalg.norm(R,2));assert error<=bound+1e-11
  time_rows.append(dict(t=t,error=error,finite_global_duhamel_bound=bound))
 assert max(r['unitarity'] for r in rows)<1e-12
 Hs,Vs=model(2,1,3);hs,gs=construct(Hs,Vs,4);Us=np.eye(len(Hs))
 for k,S in enumerate(gs,1):Us=expm(lam**k*S)@Us
 Hs=Us@(np.diag(Hs)+lam*Vs)@Us.T;Bs=sum(lam**j*q for j,q in enumerate(hs));states=np.arange(len(Hs))
 C=np.diag(sum(1-2*((states>>a ^ states>>(a+2))&1) for a in [0,3]));Ct=Us@C@Us.T
 Es,Ws=eigh(Hs);es,ws=eigh(Bs);v=Us[:,0];source_rows=[]
 for t in [.5,2,8]:
  a=(Ws*np.exp(-1j*t*Es))@Ws.T;b=(ws*np.exp(-1j*t*es))@ws.T
  error=float(abs(v.conj()@(a.conj().T@Ct@a-b.conj().T@Ct@b)@Ct@v));bound=float(2*t*np.linalg.norm(Hs-Bs,2)*np.linalg.norm(Ct,2)**2);assert error<=bound+1e-11
  source_rows.append(dict(t=t,correlation_error=error,finite_global_bound=bound))
 source=dict(physical_sites=6,dressing_norm=float(np.linalg.norm(Ct-C,2)),correlations=source_rows)
 result=dict(status='PASS',normalform=rows,dynamics=time_rows,dressed_source=source,scope='Finite recursion/sign control only; volume-uniform theorem is analytical, no full native pole or physical state identification')
 out=ROOT/'outputs/native_local_normalform/result.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
