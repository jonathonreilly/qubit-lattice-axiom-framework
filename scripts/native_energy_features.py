#!/usr/bin/env python3
"""Reproduce scoped native thermal and large-feature calculations."""
from pathlib import Path
import hashlib,json,os,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'outputs/neutral_composite_review_2026_10_18/helpers/native'
AUDIT_TIMEOUT_SEC=600
AUDIT_INPUT_PATHS = ['outputs/neutral_composite_review_2026_10_18/helpers/native/compass_energy_bridge.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_energy_modes.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_local_transport.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_scalar.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/compass_thermal_bridge.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/energy_current_identity.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/energy_large_feature.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/independent_energy_modes.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/independent_thermal_extension.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/independent_transport.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/thermal_dense_control.py', 'outputs/neutral_composite_review_2026_10_18/proofs/native/THERMAL_BRIDGE_DERIVATION.md', 'outputs/neutral_composite_review_2026_10_18/proofs/native/ENERGY_FEATURE_DERIVATION.md', 'outputs/neutral_composite_review_2026_10_18/proofs/native/FINITE_BETA_FEATURE_DERIVATION.md']
PROBES=['compass_energy_bridge', 'compass_thermal_bridge', 'compass_energy_modes', 'energy_large_feature', 'thermal_dense_control', 'energy_current_identity', 'independent_thermal_extension', 'independent_energy_modes']
def main():
 results={}
 for name in PROBES:
  p=subprocess.run([sys.executable,str(PACK/(name+'.py'))],cwd=ROOT,env=dict(os.environ,OPENBLAS_NUM_THREADS='1'),timeout=240)
  if p.returncode:raise RuntimeError(name+': child exit '+str(p.returncode)+'; output is in the parent execution capture')
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
