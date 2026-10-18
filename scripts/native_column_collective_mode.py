#!/usr/bin/env python3
"""Replay competing native column interactions and the conditional visible mode."""
from pathlib import Path
import os,sys,json,subprocess,hashlib
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=300
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rectangle_six.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_column_source_derivative.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_column_six_mode.py']
def main():
 env={**os.environ,'VECLIB_MAXIMUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 results={}
 for name in ['neutral_rectangle_six','neutral_column_source_derivative','neutral_column_six_mode']:
  subprocess.run([sys.executable,str(PACK/(name+'.py'))],env=env,check=True,capture_output=True,text=True,timeout=250)
  results[name]=json.loads((PACK/(name+'.json')).read_text())
 exact=results['neutral_rectangle_six']; assert len(exact)==128
 for r in exact:assert F(r['coefficient'])==-F(3,256 if r['cost']==2 else 8192)*r['corner_parity']
 source=next(r for r in results['neutral_column_source_derivative'] if r['L']==6)
 assert F(source['t_log_source_derivative'])==6 and F(source['total_source_over_t'])==F(-63,20)
 mode=results['neutral_column_six_mode']; assert mode['delta']>mode['lower_threshold'] and mode['upper_binding']>0
 assert mode['upper_q_squared_curvature']<0
 last=mode['rows'][-1]
 assert abs(last['upper']-mode['upper'])<5e-6
 assert abs(last['upper_weight']-mode['source_weight'])<1e-5
 assert last['lower']>-4 and abs(last['lower']+4)<.021
 for r in mode['momentum_checks']:assert abs(r['native_coefficient_finite']-r['halfline_prediction'])<2e-5
 assert abs(mode['physical_readout_weight_over_t_squared']-float(F(63,20)**2)*mode['source_weight'])<1e-12
 out=ROOT/'outputs/native_column_collective_mode';out.mkdir(parents=True,exist_ok=True)
 (out/'result.json').write_text(json.dumps(dict(inputs={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in AUDIT_INPUT_PATHS},results=results,scope='Derived order-six coefficient operator for open length-six columns; no exact native pole, physical identification or empirical validation'),indent=2)+'\n')
 print('per_site: one physical qubit; no additional microscopic interaction')
 print('per_mode: upper neutral composite and original-readout weight derived at order six')
 print('per_block: competing native interaction removes naive lower bound mode')
 print('lattice_wide: negative curvature at zero momentum; no relativistic scalar or TOE closure')
if __name__=='__main__':main()
