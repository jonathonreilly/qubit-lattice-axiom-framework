#!/usr/bin/env python3
"""Reproduce symmetry/readout; full native anisotropy solve is a frozen hashed input."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=900
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_discrete_symmetry.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_xy_readout.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_open_xy_comparison.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_anisotropy_comparison.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_model.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_tube_anisotropy.json']
PROBES=['neutral_rung_discrete_symmetry', 'neutral_xy_readout', 'neutral_open_xy_comparison', 'neutral_anisotropy_comparison']

def main():
 env={**os.environ,'OPENBLAS_NUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 for name in PROBES:
  subprocess.run([sys.executable,str(PACK/(name+'.py'))],env=env,check=True,capture_output=True,text=True,timeout=300)
  print('reproduced',name,flush=True)
 out=ROOT/'outputs/native_infrared_readout';out.mkdir(parents=True,exist_ok=True)
 result=dict(inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},results={n:json.loads((PACK/(n+'.json')).read_text()) for n in PROBES},scope='Exact discrete symmetry, leading-theory readout, and frozen full-H finite anisotropy comparison; no bulk phase or physical scalar identification')
 (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 print('per_site: one physical qubit; exact parity coordinates add no degrees of freedom')
 print('per_mode: quadratic original-composite infrared readout derived')
 print('per_block: exact discrete symmetry and conditional infrared route')
 print('lattice_wide: equal coupling, bulk scalar and physical observations remain open')
if __name__=='__main__':main()
