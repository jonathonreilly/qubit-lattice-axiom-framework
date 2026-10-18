#!/usr/bin/env python3
"""Replay native plaquette coefficient, competing parity bands and constraint count."""
from pathlib import Path
import os,sys,json,subprocess,hashlib
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=300
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_column_plaquette.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_column_parity_native.py']
def rank(rows):
 piv={}
 for v in rows:
  while v:
   k=v.bit_length()-1
   if k not in piv:piv[k]=v;break
   v^=piv[k]
 return len(piv)
def main():
 env={**os.environ,'VECLIB_MAXIMUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','NUMBA_NUM_THREADS':'4'}
 for n in ['neutral_column_plaquette','neutral_column_parity_native']:
  subprocess.run([sys.executable,str(PACK/(n+'.py'))],env=env,check=True,capture_output=True,text=True,timeout=250)
 exact=json.loads((PACK/'neutral_column_plaquette.json').read_text());native=json.loads((PACK/'neutral_column_parity_native.json').read_text());checks=[]
 for L in [5,6]:
  for lam in [.1,.2]:
   plus=next(r for r in native if r['L']==L and r['lambda_perp']==lam and r['parity']==0)
   minus=next(r for r in native if r['L']==L and r['lambda_perp']==lam and r['parity']==1)
   ratio=(minus['band_mean']-plus['band_mean'])/lam**4;pred=(L+14)/64
   assert max(plus['residuals']+minus['residuals'])<1e-10
   assert minus['ground']>plus['ground'] and abs(ratio-pred)<.04*lam**2
   c_ratio=(plus['readout_band_mean']-minus['readout_band_mean'])/lam**4;c_pred=-3*(L+13)/64
   assert abs(c_ratio-c_pred)<.3*lam**2
   checks.append(dict(L=L,lam=lam,splitting_over_lambda4=ratio,prediction=pred,readout_difference_over_lambda4=c_ratio,readout_prediction=c_pred))
 counts=[]
 for nx in range(3,8):
  for ny in range(3,8):
   for periodic in [False,True]:
    rows=[]
    for x in range(nx if periodic else nx-1):
     for y in range(ny if periodic else ny-1):
      rows.append(sum(1<<(((x+a)%nx)*ny+(y+b)%ny) for a,b in [(0,0),(1,0),(0,1),(1,1)]))
    r=rank(rows);assert nx*ny-r==nx+ny-1
    counts.append(dict(nx=nx,ny=ny,periodic=periodic,rank=r))
 out=ROOT/'outputs/native_column_plaquette_selection';out.mkdir(parents=True,exist_ok=True)
 (out/'result.json').write_text(json.dumps(dict(inputs={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in AUDIT_INPUT_PATHS},exact=exact,native=native,comparisons=checks,constraint_counts=counts,scope='Fixed-order native interaction and finite-size small-anisotropy parity preference; no uniform 3D phase or empirical claim'),indent=2)+'\n')
 print('per_site: one physical qubit; no additional microscopic interaction')
 print('per_mode: generated four-column plaquette sign checked')
 print('per_block: positive parity preferred at fixed finite size and small ratio')
 print('lattice_wide: subsystem degeneracy remains; no continuum or physical scalar')
if __name__=='__main__':main()
