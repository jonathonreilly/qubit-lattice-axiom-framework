#!/usr/bin/env python3
"""Reproduce exact neutral algebra controls and finite collective-source construction."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'outputs/neutral_composite_review_2026_10_18/helpers/native'
AUDIT_TIMEOUT_SEC=600
AUDIT_INPUT_PATHS = ['outputs/neutral_composite_review_2026_10_18/helpers/native/compass_sector_basis.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_sector_solve.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_bond_algebra.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_collective_basis.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_extra_sector.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_extra_sector_control.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_extra_sector_response.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_mode_symmetry_labels.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_plane_mobility_control.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/neutral_quadratic_scalar_basis.py', 'outputs/neutral_composite_review_2026_10_18/proofs/native/NEUTRAL_BOND_ALGEBRA.md', 'outputs/neutral_composite_review_2026_10_18/proofs/native/PLANE_MOBILITY.md']
PROBES=['compass_sector_solve', 'neutral_extra_sector_control', 'neutral_extra_sector_response', 'neutral_mode_symmetry_labels', 'neutral_plane_mobility_control', 'neutral_bond_algebra', 'neutral_collective_basis', 'neutral_quadratic_scalar_basis']

def main():
 env={**os.environ,'OPENBLAS_NUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 for name in PROBES:
  subprocess.run([sys.executable,str(PACK/(name+'.py'))],env=env,check=True,timeout=300)
  print('reproduced',name,flush=True)
 out=ROOT/'outputs/native_neutral_bond_algebra';out.mkdir(parents=True,exist_ok=True)
 result=dict(inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},results={n:json.loads((PACK/(n+'.json')).read_text()) for n in PROBES if n!='compass_sector_solve'},scope='Exact finite neutral algebra; numerical27site source construction, no bulk or physical scalar identification')
 (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 print('per_element: binary Pauli commutation, signed orbit actions and source covariance entries checked')
 print('per_site: original one-qubit sites and native bond interaction retained throughout these finite controls')
 print('per_mode: floating full-H eigenpair residuals and finite source mixtures are recorded without bulk extrapolation')
 print('per_block: complete plane-neutral bond algebra, no dynamical closure implied')
 print('lattice_wide: controls use the stated finite open geometry; bulk persistence and observational identification remain open')
if __name__=='__main__':main()
