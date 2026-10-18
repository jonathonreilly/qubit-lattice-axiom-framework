#!/usr/bin/env python3
"""Finite algebra replay supporting the separately stated local normal-form proof."""
from pathlib import Path
import os,sys,json,subprocess,hashlib
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_local_normal_form.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_packet_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_model.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_core.py']
def main():
 env={**os.environ,'VECLIB_MAXIMUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 for n in ['neutral_local_normal_form','neutral_packet_control']:
  subprocess.run([sys.executable,str(PACK/(n+'.py'))],check=True,env=env,capture_output=True,text=True)
 r=json.loads((PACK/'neutral_local_normal_form.json').read_text());p=json.loads((PACK/'neutral_packet_control.json').read_text())
 assert r['cancellation_error']==r['K2_match_error']==r['uniform_annihilation_error']==0
 assert abs(p['modes'][0]['source_coefficient']-15/4)<1e-12
 assert all(abs(x['moment']-x['exact_moment'])<2e-15 for x in p['packet'])
 out=ROOT/'outputs/native_local_normal_form';out.mkdir(parents=True,exist_ok=True)
 (out/'result.json').write_text(json.dumps(dict(inputs={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in AUDIT_INPUT_PATHS},local_algebra=r,packet=p,scope='Finite algebra and leading packet checks; uniform proof is in note; no exact native pole or empirical test'),indent=2)+'\n')
 print('per_site: one physical qubit; supplied directional interaction')
 print('per_mode: native local inversion matches canonical second order')
 print('per_block: explicit packet and conditional leading readout checks')
 print('lattice_wide: finite checks do not establish the separate uniform proof')
if __name__=='__main__':main()
