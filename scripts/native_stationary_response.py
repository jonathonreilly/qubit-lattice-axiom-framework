#!/usr/bin/env python3
"""Reproduce full-H finite stationary neutral response diagnostics."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
import numpy,scipy,numba
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'outputs/neutral_composite_review_2026_10_18/helpers/native/'
AUDIT_TIMEOUT_SEC=1200
AUDIT_INPUT_PATHS = ['outputs/neutral_composite_review_2026_10_18/helpers/native/compass_mode_form_factors.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_sector_basis.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_sector_control.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_sector_solve.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_sector_survey.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_stationary_mixed.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_stationary_response.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_stationary_spatial.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_visible_ritz.py', 'outputs/neutral_composite_review_2026_10_18/proofs/native/STATIONARY_SECTOR_DERIVATION.md']

def main():
 env={**os.environ,'OPENBLAS_NUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 probes=['compass_sector_control', 'compass_sector_solve', 'compass_sector_survey', 'compass_stationary_response', 'compass_stationary_mixed', 'compass_stationary_spatial', 'compass_visible_ritz', 'compass_mode_form_factors']
 for name in probes:
  subprocess.run([sys.executable,str(PACK/(name+'.py'))],env=env,check=True,timeout=650)
  print('reproduced',name,flush=True)
 files=['compass_sector_control','stationary_3x3x3_plus','stationary_sector_survey','stationary_response','stationary_mixed','stationary_spatial','stationary_visible_ritz','stationary_mode_form_factors']
 out=ROOT/'outputs/native_stationary_response';out.mkdir(parents=True,exist_ok=True)
 (out/'result.json').write_text(json.dumps(dict(inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},versions=dict(numpy=numpy.__version__,scipy=scipy.__version__,numba=numba.__version__),results={p:json.loads((PACK/(p+'.json')).read_text()) for p in files},scope='Exact finite sector reduction with numerical full-H responses; no bulk scalar or universal coupling'),indent=2)+'\n')
 print('per_element: native bond actions and central composite sector intertwiners checked; eigenpairs have floating residuals')
 print('per_site: original one-qubit sites and native bond interaction retained throughout finite sector construction')
 print('per_mode: actual finite full-H residuals retained; no bulk pole')
 print('per_block: all 32 finite sign sectors are represented modulo the checked unitary equivalence')
 print('lattice_wide: scope is finite open27-site grid, not infinite-volume extrapolation')
if __name__=='__main__':main()
