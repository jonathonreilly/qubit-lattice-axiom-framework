#!/usr/bin/env python3
"""Check native local coefficients and separately labelled partial-model resonances."""
from pathlib import Path
import os,sys,json,hashlib,subprocess
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=300
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bulk_source_check.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bulk_second.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bulk_resonance.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bulk_resonance_dynamic.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bulk_dispersion_check.py']

def main():
 env={**os.environ,'OPENBLAS_NUM_THREADS':'1','VECLIB_MAXIMUM_THREADS':'1'}
 for f in AUDIT_INPUT_PATHS:
  subprocess.run([sys.executable,str(ROOT/f)],env=env,check=True,capture_output=True,text=True,timeout=250)
 def read(name):return json.loads((Path('/private/tmp')/name).read_text())
 source=read('neutral-bulk-source-normalization-independent.json')
 assert max(source['errors'].values())<1e-12 and abs(source['source_norm2']-2)<1e-12
 second=read('neutral_bulk_second.json')
 for row in second:
  assert sorted(F(q['coefficient']) for q in row['rows'])==[F(-5,2),F(-1,8),F(-1,8),F(-1,8),F(-1,8)]
 frozen=read('neutral_bulk_resonance.json');dynamic=read('neutral_bulk_resonance_dynamic.json')
 assert frozen['edge_product']<.074
 assert max(row['residual'] for row in frozen['frozen_boundary_controls'])<1e-10
 assert all(row['converged'] and row['residual']<1e-7 for row in dynamic['rows'])
 assert abs(dynamic['rows'][-1]['width_over_lambda4']-.09857499688)<5e-6
 out=ROOT/'outputs/native_bulk_segment_resonance';out.mkdir(parents=True,exist_ok=True)
 (out/'result.json').write_text(json.dumps(dict(inputs={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in AUDIT_INPUT_PATHS},native_local={'source':source,'second_order':second},conditional_model={'frozen_boundary':frozen,'dynamic_boundary':dynamic,'dispersion':read('neutral-bulk-dispersion-independent.json')},scope='Native finite-order source/channel and K2 checks; resonances and dispersion belong only to partial coefficient model, not a native pole or empirical test'),indent=2)+'\n')
 print('per_site: one physical qubit; bulk segments do not cut column ends')
 print('per_mode: native source and tension motivate conditional outgoing resonance')
 print('per_block: growing length, width and residue remain partial-model results')
 print('lattice_wide: higher-order/uniform native control and scalar identification open')
if __name__=='__main__':main()
