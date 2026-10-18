#!/usr/bin/env python3
"""Replay short controls; integrity-check explicitly frozen large-grid calculations."""
from pathlib import Path
import os,sys,json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=600
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_four_column_droplet.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_four_column_model_v2.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_four_column_charges.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_four_column_momentum.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_four_column_model.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_four_column_momentum_six.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_four_column_native.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/column_four_results/neutral_four_column_momentum_5x5_t0.8889.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/column_four_results/neutral_four_column_charges_5x6.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/column_four_results/neutral_four_column_5x6.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/column_four_results/neutral_four_column_droplet.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/column_four_results/neutral_four_column_6x6.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/column_four_results/neutral_four_column_momentum_6x6_t0.8889.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/column_four_results/neutral_four_column_momentum_5x5_t4.0000.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/column_four_results/neutral_four_column_native.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/column_four_results/neutral_four_column_charges_5x5.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/column_four_results/neutral_four_column_5x5.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/column_four_results/PROVENANCE.json']

def main():
 frozen=PACK/'column_four_results'; provenance=json.loads((frozen/'PROVENANCE.json').read_text())
 for category,base in [('source_sha256',PACK),('result_sha256',frozen)]:
  for name,digest in provenance[category].items():assert hashlib.sha256((base/name).read_bytes()).hexdigest()==digest,name
 env={**os.environ,'VECLIB_MAXIMUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 for name,args in [('neutral_four_column_droplet',[]),('neutral_four_column_momentum',['5','5']),('neutral_four_column_charges',['5','5']),('neutral_four_column_native',[])]:
  subprocess.run([sys.executable,str(PACK/(name+'.py')),*args],env=env,check=True,capture_output=True,text=True,timeout=500)
 mom=json.loads(Path('/private/tmp/neutral_four_column_momentum_5x5_t0.8889.json').read_text())
 old=json.loads((frozen/'neutral_four_column_momentum_5x5_t0.8889.json').read_text())
 for a,b in zip(mom['rows'],old['rows']):
  assert abs(a['gap']-b['gap'])<1e-8 and abs(a['weight']-b['weight'])<1e-8
  assert a['residual']<1e-8
 charges=json.loads(Path('/private/tmp/neutral_four_column_charges_5x5.json').read_text())
 previous=json.loads((frozen/'neutral_four_column_charges_5x5.json').read_text())
 for a,b in zip(charges['rows'],previous['rows']):
  assert abs(a['gap']-b['gap'])<1e-8 and abs(a['plaquette_difference']-b['plaquette_difference'])<1e-7
  assert a['residual']<1e-8
 native=json.loads(Path('/private/tmp/neutral_four_column_native.json').read_text())
 assert all(row['max_residual']<1e-8 for row in native)
 assert native[0]['H_coefficient_error']<.006 and native[1]['H_coefficient_error']<.023
 assert native[0]['C_coefficient_error']<.028 and native[1]['C_coefficient_error']<.105
 out=ROOT/'outputs/native_four_column_competition';out.mkdir(parents=True,exist_ok=True)
 (out/'result.json').write_text(json.dumps(dict(input_sha256={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in AUDIT_INPUT_PATHS},short_replays={'momentum':mom,'charges':charges,'native':native},large_grid_status='Frozen source-bound development results verified by hash; 5x6 and 6x6 not replayed by this runner',scope='Conditional leading coefficient model and finite native checks; no empirical test or infinite-volume scalar identification'),indent=2)+'\n')
 print('per_site: one physical qubit, supplied directional Hamiltonian')
 print('per_mode: neutral peak and microscopic readout derived in finite leading model')
 print('per_block: short replays pass; large-grid results explicitly frozen')
 print('lattice_wide: open ends and state are premises; no bulk TOE closure')
if __name__=='__main__':main()
