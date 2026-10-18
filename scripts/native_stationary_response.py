#!/usr/bin/env python3
"""Reproduce full-H finite stationary neutral response diagnostics."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
import numpy,scipy,numba
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native/'
AUDIT_TIMEOUT_SEC=1200
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_basis.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_solve.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_survey.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_stationary_response.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_stationary_mixed.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_stationary_spatial.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_visible_ritz.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_mode_form_factors.py']

def main():
 env={**os.environ,'OPENBLAS_NUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 probes=['compass_sector_control', 'compass_sector_solve', 'compass_sector_survey', 'compass_stationary_response', 'compass_stationary_mixed', 'compass_stationary_spatial', 'compass_visible_ritz', 'compass_mode_form_factors']
 for name in probes:
  subprocess.run([sys.executable,str(PACK/(name+'.py'))],env=env,check=True,capture_output=True,text=True,timeout=650)
  print('reproduced',name,flush=True)
 files=['compass_sector_control','stationary_3x3x3_plus','stationary_sector_survey','stationary_response','stationary_mixed','stationary_spatial','stationary_visible_ritz','stationary_mode_form_factors']
 out=ROOT/'outputs/native_stationary_response';out.mkdir(parents=True,exist_ok=True)
 (out/'result.json').write_text(json.dumps(dict(inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},versions=dict(numpy=numpy.__version__,scipy=scipy.__version__,numba=numba.__version__),results={p:json.loads((PACK/(p+'.json')).read_text()) for p in files},scope='Exact finite sector reduction with numerical full-H responses; no bulk scalar or universal coupling'),indent=2)+'\n')
 print('per_site: one physical qubit; no interaction added')
 print('per_mode: actual finite full-H residuals retained; no bulk pole')
 print('per_block: all32 sectors represented modulo checked unitary equivalence')
 print('lattice_wide: scope is finite open27-site grid, not infinite-volume extrapolation')
if __name__=='__main__':main()
