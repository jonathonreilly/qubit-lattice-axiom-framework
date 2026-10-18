#!/usr/bin/env python3
"""Native Pauli fluctuation/coupling identities; supplied statistical states."""
from pathlib import Path
import sys,json,numpy as np
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_energy_collective.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_energy_qnorm.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_energy_thermal.py']
sys.path.insert(0,str(ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'))
from neutral_energy_collective import run
from neutral_energy_qnorm import polynomial
from neutral_energy_thermal import run as thermal

def main():
 r=run();p=polynomial();t=thermal();rows=[]
 assert p['at_zero']==5376 and abs(r['conserved_fraction']-4/7)<1e-14
 for q in [.1,.01,.001]:
  h=np.cos(q/2);N=3072+1280*np.cos(q)+1024*h;g=-(32/3)*(2*h+1);m2=64*(1-h);Omega=10*q
  bound=max(0,abs(g)*np.sqrt(3/N)-np.sqrt(m2/(3*Omega**2)))**2
  assert 0<bound<4/7;rows.append(dict(q=q,window=Omega,rigorous_fraction_lower_bound=float(bound)))
 result=dict(status='PASS',native=r,qnorm=p,thermal_control=t,low_window=rows,scope='Exact fluctuation statements in supplied beta0 state; highT finite-volume Taylor control only. No nonzero beta0 retarded response, vacuum particle, physical detector or cosmological identification.')
 out=ROOT/'outputs/native_conserved_scalar/result.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
