#!/usr/bin/env python3
"""Reproduce conditional neutral source-identification controls."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=900
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_scale_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_basis.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_solve.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_smooth_source.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_extra_sector.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_extra_sector_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_extra_sector_response.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_ladder_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_ladder_probe.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_mode_charges.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_plane_factor.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_source_ambiguity.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_thermal_protocol_control.py']
# Spatial response is a frozen prior-milestone numerical input, explicitly hashed.
AUDIT_INPUT_PATHS.append('.claude/science/physics-loops/neutral-composite-24h-20261018/native/stationary_spatial.json')
PROBES=['compass_sector_solve', 'neutral_extra_sector_response', 'compass_scale_control', 'compass_smooth_source', 'neutral_thermal_protocol_control', 'neutral_plane_factor', 'neutral_ladder_control', 'neutral_ladder_probe', 'neutral_mode_charges', 'neutral_source_ambiguity']

def main():
 env={**os.environ,'OPENBLAS_NUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 for name in PROBES:
  subprocess.run([sys.executable,str(PACK/(name+'.py'))],env=env,check=True,capture_output=True,text=True,timeout=500)
  print('reproduced',name,flush=True)
 out=ROOT/'outputs/native_neutral_source_identification';out.mkdir(parents=True,exist_ok=True)
 result=dict(inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},results={n:json.loads((PACK/(n+'.json')).read_text()) for n in PROBES if n!='compass_sector_solve'},scope='Exact source nonuniqueness and protected-state reduction; finite conditional model diagnostics, no physical scalar coupling derived')
 (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 print('per_site: one physical qubit, unchanged native interaction')
 print('per_mode: finite ladder and conditional diagonal expectations')
 print('per_block: neutral protected-factor removal and source nonuniqueness')
 print('lattice_wide: bulk identification and observations remain open')
if __name__=='__main__':main()
