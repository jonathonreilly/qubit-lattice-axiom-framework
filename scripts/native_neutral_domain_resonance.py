#!/usr/bin/env python3
"""Reproduce native finite coefficients and conditional expanded-domain resonance."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=900
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_physical_q_source.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_full_third_check.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_q_certificate.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_source_dressing.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_fourth_rational.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_dark_rational.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_dark_third.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_dark_fourth_diagonal.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_dark_bound_math.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_dark_resonance.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_fourth_overlap.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_dark_fourth_action.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_core.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_model.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_fourth_overlap.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_dark_fourth_action.json']
PROBES=['neutral_kink_physical_q_source', 'neutral_kink_full_third_check', 'neutral_kink_q_certificate', 'neutral_kink_source_dressing', 'neutral_kink_fourth_rational', 'neutral_kink_dark_rational', 'neutral_kink_dark_third', 'neutral_kink_dark_fourth_diagonal', 'neutral_dark_bound_math', 'neutral_kink_dark_resonance']
FROZEN=['neutral_kink_fourth_overlap', 'neutral_kink_dark_fourth_action']

def main():
 env={**os.environ,'VECLIB_MAXIMUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 for name in PROBES:
  subprocess.run([sys.executable,str(PACK/(name+'.py'))],env=env,check=True,capture_output=True,text=True,timeout=300)
  print('reproduced',name,flush=True)
 results={n:json.loads((PACK/(n+'.json')).read_text()) for n in PROBES+FROZEN}
 for row in results['neutral_kink_source_dressing']:assert row['second_source_identity_residual']<1e-10
 for row in results['neutral_kink_dark_third']:
  if row['ell']>=4 and row['ell']%2==0:
   assert max(row['H3norm'],row['H1norm'],row['H2res'],abs(row['H2mean']+2))<1e-10
 from fractions import Fraction as F
 for row in results['neutral_kink_dark_rational']:
  L=row['L']
  for name,values in row['kernels'].items():
   expected=[F(0)]*L
   if name=='4_4':expected[0]=F(-13,96)
   else:expected[0]=expected[2]=F(-3,64)
   assert list(map(F,values))==expected
 for row in results['neutral_kink_physical_q_source']:
  assert max(row['first_identity_error'],row['second_identity_error'])<1e-10
 for row in results['neutral_kink_dark_resonance']['rows']:
  if row['ratio']==.01:
   assert abs(row['shift_coefficient']-row['predicted_shift'])<.001
   assert abs(row['width_coefficient']-row['predicted_width'])<.004
   assert abs(row['source_residue_coefficient']-row['predicted_source'])<.005
 for row in results['neutral_kink_fourth_overlap']:
  power=sum(re*re+im*im for ell,re,im in row['overlaps'])
  assert abs(power-row['outside']**2)<1e-10
 for row in results['neutral_kink_dark_fourth_action']:
  power=sum(re*re+im*im for ell,re,im in row['overlaps'])
  assert abs(power-row['outside']**2)<1e-10
 out=ROOT/'outputs/native_neutral_domain_resonance';out.mkdir(parents=True,exist_ok=True)
 (out/'result.json').write_text(json.dumps(dict(inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},results=results,frozen_auxiliary=FROZEN,scope='Finite native coefficient certificates and conditional dark-chain resonance; no all-L closure, physical scalar or empirical test'),indent=2)+'\n')
 print('per_site: one physical qubit; no added interaction')
 print('per_mode: finite native neutral domains and original composite source')
 print('per_block: conditional expanded-chain resonance; isolated-state truncation corrected')
 print('lattice_wide: all-length control, equal coupling, physical scalar and observations open')
if __name__=='__main__':main()
