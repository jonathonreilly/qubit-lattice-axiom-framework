#!/usr/bin/env python3
"""Native coefficients and explicitly scoped projected-model resonance checks."""
from pathlib import Path
import os,sys,json,hashlib,subprocess
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=300
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bulk_second_other.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bulk_second_boundary.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_source_check.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_host.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_dispersion.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_resonance.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_response.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_confined_fast_source.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_coupled_slow_pole.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_outgoing_host.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bulk_source_check.py']
RUN_NAMES=['neutral_bulk_second_other', 'neutral_bulk_second_boundary', 'neutral_slow_source_check', 'neutral_slow_host', 'neutral_slow_dispersion', 'neutral_slow_resonance', 'neutral_slow_response', 'neutral_confined_fast_source', 'neutral_coupled_slow_pole']
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
def main():
 env={**os.environ,'OPENBLAS_NUM_THREADS':'1','VECLIB_MAXIMUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 data={}
 for name in RUN_NAMES:
  subprocess.run([sys.executable,str(PACK/(name+'.py'))],env=env,check=True,capture_output=True,text=True,timeout=250)
  path=Path('/private/tmp')/(name+'.json') if name.startswith('neutral_bulk_second') else PACK/(name+'.json')
  data[name]=json.loads(path.read_text())
 other=data['neutral_bulk_second_other']
 axial=next(r for r in other if (r['ell'],r['rx'],r['ry'])==(4,2,0))
 assert sorted(F(x['coefficient']) for x in axial['rows'])==[F(-4),F(-1,2),F(-1,2),F(-1,2),F(-1,2)]
 for r in other:
  if r['ell']==4 and r['ry']==1:assert [F(x['coefficient']) for x in r['rows']]==[F(-4)]
 src=data['neutral_slow_source_check'];assert src['direct_second_order_source_support_absent']
 assert max(abs(src[k]-v) for k,v in [('A_to_e',-1),('A_to_d2',-1),('D_to_e',-2),('D_to_d2',0)])<1e-10
 h=data['neutral_slow_host'];assert abs(h['width_coefficient']-.1136079122)<1e-9
 poles=data['neutral_slow_resonance']['rows'];assert all(r['success'] and r['residual']<1e-8 for r in poles)
 assert data['neutral_slow_response']['minimum_spectral']>0
 assert all(r['physical_curvature_over_lambda4']>0 for r in data['neutral_slow_dispersion'])
 coupled=data['neutral_coupled_slow_pole']['rows'];assert all(r['success'] and r['residual']<1e-8 for r in coupled)
 assert all(r['physical_shift_over_lambda5_log']<.15 for r in coupled)
 out=ROOT/'outputs/native_slow_bulk_composite/result.json'
 out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(dict(source_hashes={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in AUDIT_INPUT_PATHS},checks=data,scope='Native finite-order coefficients; explicit projected-model pole and readout. No full native pole, physical scalar or empirical test.'),indent=2)+'\n')
 print('per_site: one physical qubit, supplied directional Hamiltonian')
 print('per_mode: native vertices induce conditional slow-composite readout')
 print('per_block: coupled projected-model resonance survives; native remainder open')
 print('lattice_wide: cosmological state, isotropy and measured coupling not derived')
if __name__=='__main__':main()
