#!/usr/bin/env python3
"""Reproduce exact internal factorization and finite large-column tunneling."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=900
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_exact_internal_factor.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_strong_tunnel.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_strong_symmetry.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_strong_spectrum.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_model.py']
PROBES=['neutral_exact_internal_factor', 'neutral_strong_tunnel', 'neutral_strong_symmetry', 'neutral_strong_spectrum']

def main():
 env={**os.environ,'OPENBLAS_NUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 for name in PROBES:
  subprocess.run([sys.executable,str(PACK/(name+'.py'))],env=env,check=True,capture_output=True,text=True,timeout=300)
  print('reproduced',name,flush=True)
 out=ROOT/'outputs/native_large_column_dynamics';out.mkdir(parents=True,exist_ok=True)
 result=dict(inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},results={n:json.loads((PACK/(n+'.json')).read_text()) for n in PROBES},scope='Exact coordinate identities, finite strong-column tunneling and scalar-readout selection; no bulk or physical identification')
 (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 print('per_site: one physical qubit; exact parity coordinates add no degrees of freedom')
 print('per_mode: existing internal vertices and large-column tunneling derived')
 print('per_block: exact finite-band scalar-readout selection')
 print('lattice_wide: equal coupling, bulk scalar and physical observations remain open')
if __name__=='__main__':main()
