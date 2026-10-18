#!/usr/bin/env python3
"""Native local/symmetry coefficients and conditional zone-boundary composite controls."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=900
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_zone_boundary.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_zone_local_second.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_zone_exact_math.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_zone_large_feature.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_native_periodic_pi_pole.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_scalar_explicit_basis.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_core.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_model.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_basis.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_solve.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_extra_sector.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_native_periodic_pi_pole.json']
PROBES=['neutral_zone_boundary', 'neutral_zone_local_second', 'neutral_zone_exact_math', 'neutral_zone_large_feature']

def main():
 env={**os.environ,'VECLIB_MAXIMUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 for name in PROBES:
  subprocess.run([sys.executable,str(PACK/(name+'.py'))],env=env,check=True,capture_output=True,text=True,timeout=600)
  print('reproduced',name,flush=True)
 results={n:json.loads((PACK/(n+'.json')).read_text()) for n in PROBES+['neutral_native_periodic_pi_pole']}
 for r in results['neutral_zone_boundary']:
  assert max(r['H1norm'],r['H3norm'],r['reflection_checkerboard_error'])<2e-11
 for r in results['neutral_zone_local_second']:
  for entry in r['kernels']:
   assert F(entry['unnormalized_coefficient']) in [F(1,4),F(-1,8),F(-1,2),F(-2),F(-1)]
 math=results['neutral_zone_exact_math'];assert math['upper_curvature']=='208/27' and math['odd_source_weight_coefficient']=='15/4'
 large=results['neutral_zone_large_feature'];last=large['rows'][-1]
 assert abs(last['residue_times_mean']-float(large['residue_times_mean_limit']))<.0001
 assert last['mean_host_index']>10000
 for r in results['neutral_native_periodic_pi_pole']:
  assert r['ground_residual']<1e-10
  assert all(r['candidates'][i]['residual']<1e-8 for i in [0,2])
  assert all(r['candidates'][i]['residual']>.001 for i in [1,3,4,5])
  lam=r['lambda_perp'];best=r['candidates'][0]
  assert abs(best['energy']-r['prediction_energy'])<.2*lam**4
  assert abs(best['weight_over_lambda2']-r['prediction_weight_coefficient'])<.45*lam**2
 out=ROOT/'outputs/native_zone_boundary_composite';out.mkdir(parents=True,exist_ok=True)
 (out/'result.json').write_text(json.dumps(dict(inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},results=results,frozen_auxiliary=['neutral_native_periodic_pi_pole'],scope='Native formal local coefficients; conditional halfline bound-mode, crossover and size/readout relation; finite full-H evidence; no uniform native or physical scalar theorem'),indent=2)+'\n')
 print('per_site: one physical qubit; original directional Hamiltonian')
 print('per_mode: zone-boundary composite and readout derived')
 print('per_block: conditional crossover and large-feature size/residue law')
 print('lattice_wide: native uniform control and physical observation bridge open')
if __name__=='__main__':main()
