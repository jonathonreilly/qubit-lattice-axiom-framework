#!/usr/bin/env python3
"""Reproduce conditional neutral source-identification controls."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'outputs/neutral_composite_review_2026_10_18/helpers/native'
AUDIT_TIMEOUT_SEC=900
AUDIT_INPUT_PATHS = ['outputs/neutral_composite_review_2026_10_18/helpers/native/compass_scale_control.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_sector_basis.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_sector_solve.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_smooth_source.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_extra_sector.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_extra_sector_control.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_extra_sector_response.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_ladder_control.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_ladder_probe.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_mode_charges.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_plane_factor.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_source_ambiguity.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_thermal_protocol_control.py', 'outputs/neutral_composite_review_2026_10_18/proofs/native/PROTECTED_PLANE_FACTOR.md', 'outputs/neutral_composite_review_2026_10_18/proofs/native/SOURCE_IDENTIFICATION_NULLSPACE.md', 'outputs/neutral_composite_review_2026_10_18/proofs/native/OVERALL_SCALE_BOUNDARY.md', 'outputs/neutral_composite_review_2026_10_18/proofs/native/SMOOTH_ENERGY_SOURCE.md', 'outputs/neutral_composite_review_2026_10_18/proofs/native/INTERNAL_LADDER.md', 'outputs/neutral_composite_review_2026_10_18/proofs/native/MODE_CHARGE_DIAGNOSTIC.md', 'outputs/neutral_composite_review_2026_10_18/inputs/stationary_spatial.json']
# Spatial response is a frozen prior-milestone numerical input, explicitly hashed.
PROBES=['compass_sector_solve', 'neutral_extra_sector_response', 'compass_scale_control', 'compass_smooth_source', 'neutral_thermal_protocol_control', 'neutral_plane_factor', 'neutral_ladder_control', 'neutral_ladder_probe', 'neutral_mode_charges', 'neutral_source_ambiguity']

def main():
 env={**os.environ,'OPENBLAS_NUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 for name in PROBES:
  subprocess.run([sys.executable,str(PACK/(name+'.py'))],env=env,check=True,timeout=500)
  print('reproduced',name,flush=True)
 out=ROOT/'outputs/native_neutral_source_identification';out.mkdir(parents=True,exist_ok=True)
 result=dict(inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},results={n:json.loads((PACK/(n+'.json')).read_text()) for n in PROBES if n!='compass_sector_solve'},scope='Constructed observable family, protected-factor decomposition and finite conditional diagnostics; negative identification theorems deferred')
 (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 print('per_element: plane symplectic form, double-commutator matrix elements and synthetic ladder controls checked')
 print('per_site: original one-qubit sites and native bond interaction retained throughout these finite controls')
 print('per_mode: finite ladder windows and conditional diagonal expectations are checked at the declared finite state')
 print('per_block: neutral factorization and observable-family matrix blocks checked')
 print('lattice_wide: controls use the stated finite open geometry; bulk persistence and observations remain untested')
if __name__=='__main__':main()
