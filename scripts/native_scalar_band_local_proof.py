#!/usr/bin/env python3
"""Local coefficient and complete scalar-band controls; finite native output declared frozen."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=900
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_wall_connected.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_wall_full_kernel.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_domain_boundary_local.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_band_scalar_reflection_sector.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_scalar_explicit_basis.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_native_periodic_pole.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_core.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_model.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_basis.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_solve.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_extra_sector.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_native_periodic_pole.json']
PROBES=['neutral_wall_connected', 'neutral_wall_full_kernel', 'neutral_domain_boundary_local', 'neutral_band_scalar_reflection_sector', 'neutral_scalar_explicit_basis']

def main():
 env={**os.environ,'VECLIB_MAXIMUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 for name in PROBES:
  subprocess.run([sys.executable,str(PACK/(name+'.py'))],env=env,check=True,capture_output=True,text=True,timeout=300)
  print('reproduced',name,flush=True)
 results={n:json.loads((PACK/(n+'.json')).read_text()) for n in PROBES+['neutral_native_periodic_pole']}
 connected={r['name']:r for r in results['neutral_wall_connected']}
 assert F(connected['wall']['excess_vs_vac'])==F(-13,192)
 assert F(connected['domain3']['excess_vs_vac'])==F(-13,96)
 # This preserved failed shortcut is explicitly NOT the canonical boundary result.
 assert F(connected['domain2']['excess_vs_vac'])!=F(-73,192)
 for r in results['neutral_domain_boundary_local']:
  assert r['canonical_boundary_matrix']==[['47/192','-5/8'],['-5/8','47/192']]
 for r in results['neutral_band_scalar_reflection_sector']:
  assert r['scalar_q0_dimension']==r['predicted_bright_plus_even_dark']
 for r in results['neutral_scalar_explicit_basis']:
  assert max(r['closure_errors']+r['symmetry_errors']+[r['orthogonality_error'],r['K1_formula_error']])<2e-11
 for r in results['neutral_native_periodic_pole']:
  assert r['ground_residual']<1e-10
  assert all(x['residual']<1e-8 for x in r['candidates'][:2])
  assert all(x['residual']>.01 for x in r['candidates'][2:])
  lam=r['lambda_perp'];best=r['candidates'][0]
  assert abs(best['energy']-r['prediction_energy'])<1.7*lam**6
  assert abs(best['weight_over_lambda4']-r['prediction_weight_coefficient'])<2.5*lam**2
 out=ROOT/'outputs/native_scalar_band_local_proof';out.mkdir(parents=True,exist_ok=True)
 (out/'result.json').write_text(json.dumps(dict(inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},results=results,frozen_auxiliary=['neutral_native_periodic_pole'],scope='Exact scalar finite-band completeness and formal local coefficients; finite native residual tests; no infinite native pole or physical scalar'),indent=2)+'\n')
 print('per_site: one physical qubit; no added interaction')
 print('per_mode: complete scalar E8 basis and local native coefficients')
 print('per_block: exact-support formal math; frozen finite full-H bounded-support')
 print('lattice_wide: uniform limit and observational identification remain open')
if __name__=='__main__':main()
