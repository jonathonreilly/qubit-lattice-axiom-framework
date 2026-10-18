#!/usr/bin/env python3
"""Reproduce correlated native trial states and full-H diagnostics."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native/'
AUDIT_TIMEOUT_SEC=600
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_product_state.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_dimer_state.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_dimer_projection.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_full_dimer_map.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_four_site_trial.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_four_site_residual.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_cluster_variational.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_cluster_neutral_acceleration.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_local_transport.py']

def main():
 env={**os.environ,'OPENBLAS_NUM_THREADS':'1'}
 calls=[(name,[]) for name in ['compass_product_state','compass_dimer_state','compass_dimer_projection','compass_full_dimer_map','compass_four_site_trial','compass_four_site_residual']]
 calls += [('compass_cluster_variational',[shape]) for shape in ['2x2x2','3x2x2','4x2x2']]
 calls += [('compass_cluster_variational',['3x3x2','0'])]
 calls += [('compass_cluster_neutral_acceleration',[shape]) for shape in ['2x2x2','3x2x2','4x2x2','3x3x2']]
 for name,args in calls:
  subprocess.run([sys.executable,str(PACK/(name+'.py')),*args],check=True,env=env,capture_output=True,text=True,timeout=240)
  print('reproduced',name,*args,flush=True)
 files=['compass_product_state','compass_dimer_state','compass_dimer_projection','compass_full_dimer_map','compass_four_site_trial','compass_four_site_residual']
 files += ['cluster_'+s for s in ['2x2x2','3x2x2','4x2x2','3x3x2']]
 files += ['cluster_acceleration_'+s for s in ['2x2x2','3x2x2','4x2x2','3x3x2']]
 out=ROOT/'outputs/native_correlated_states';out.mkdir(parents=True,exist_ok=True)
 (out/'result.json').write_text(json.dumps(dict(inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},results={p:json.loads((PACK/(p+'.json')).read_text()) for p in files},scope='Conditional supplied Hamiltonian; no stationary scalar, ground-state selection or empirical validation'),indent=2)+'\n')
 print('per_site: one qubit per original site; exact coordinate regrouping')
 print('per_mode: no equilibrium scalar pole claimed')
 print('per_block: exact variational and leakage identities; numerical cluster trials retain failures')
 print('lattice_wide: exact product-state full-H variance, no finite-torus extrapolation')
if __name__=='__main__':main()
