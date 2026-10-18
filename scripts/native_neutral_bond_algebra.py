#!/usr/bin/env python3
"""Reproduce exact neutral algebra controls and finite collective-source construction."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=600
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_basis.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_solve.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_extra_sector.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_extra_sector_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_extra_sector_response.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_mode_symmetry_labels.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_plane_mobility_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bond_algebra.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_collective_basis.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_quadratic_scalar_basis.py']
PROBES=['compass_sector_solve', 'neutral_extra_sector_control', 'neutral_extra_sector_response', 'neutral_mode_symmetry_labels', 'neutral_plane_mobility_control', 'neutral_bond_algebra', 'neutral_collective_basis', 'neutral_quadratic_scalar_basis']

def main():
 env={**os.environ,'OPENBLAS_NUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 for name in PROBES:
  subprocess.run([sys.executable,str(PACK/(name+'.py'))],env=env,check=True,capture_output=True,text=True,timeout=300)
  print('reproduced',name,flush=True)
 out=ROOT/'outputs/native_neutral_bond_algebra';out.mkdir(parents=True,exist_ok=True)
 result=dict(inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},results={n:json.loads((PACK/(n+'.json')).read_text()) for n in PROBES if n!='compass_sector_solve'},scope='Exact finite neutral algebra; numerical27site source construction, no bulk or physical scalar identification')
 (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 print('per_site: one physical qubit, unchanged native interaction')
 print('per_mode: finite eigenpair residuals and source mixtures recorded')
 print('per_block: complete plane-neutral bond algebra, no dynamical closure implied')
 print('lattice_wide: bulk and observational identification remain open')
if __name__=='__main__':main()
