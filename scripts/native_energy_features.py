#!/usr/bin/env python3
"""Reproduce scoped native thermal and large-feature calculations."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
AUDIT_TIMEOUT_SEC=600
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_energy_bridge.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_thermal_bridge.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_energy_modes.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/energy_large_feature.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/thermal_dense_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/energy_current_identity.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/independent_thermal_extension.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/independent_energy_modes.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_local_transport.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_scalar.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/independent_transport.py']
PROBES=['compass_energy_bridge', 'compass_thermal_bridge', 'compass_energy_modes', 'energy_large_feature', 'thermal_dense_control', 'energy_current_identity', 'independent_thermal_extension', 'independent_energy_modes']
def main():
 results={}
 for name in PROBES:
  p=subprocess.run([sys.executable,str(PACK/(name+'.py'))],cwd=ROOT,env=dict(os.environ,OPENBLAS_NUM_THREADS='1'),capture_output=True,text=True,timeout=240)
  if p.returncode:raise RuntimeError(name+'\n'+p.stdout+'\n'+p.stderr)
  results[name]=json.loads((PACK/(name+'.json')).read_text())
  print('reproduced',name,flush=True)
 out=ROOT/'outputs/native_energy_features/result.json';out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(dict(scope='Supplied native compass model, conditional thermal large features; no scalar particle or universal matter coupling',empirical_data_used=False,source_hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},results=results),indent=2)+'\n')
 print('per_element: exact native current and independent Pauli coefficients checked')
 print('per_site: actual one-qubit local algebra; no new interaction')
 print('per_mode: mixed response and slow-feature residual checked; particle pole not established')
 print('per_block: Gaussian source profiles are supplied diagnostic preparations')
 print('lattice_wide: uniform finite-temperature conclusion uses cited clustering theorem and explicit source proof, not numerical extrapolation')
if __name__=='__main__':main()
