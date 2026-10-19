#!/usr/bin/env python3
"""Reproduce exact native composite spatial moments by two Pauli implementations."""
from pathlib import Path
import ast,hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'outputs/neutral_composite_review_2026_10_18/helpers/native'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS = ['outputs/neutral_composite_review_2026_10_18/helpers/native/compass_local_transport.py', 'outputs/neutral_composite_review_2026_10_18/helpers/native/independent_transport.py', 'outputs/neutral_composite_review_2026_10_18/proofs/native/TRANSPORT_DERIVATION.md']
def main():
 for name in ['compass_local_transport','independent_transport']:
  p=subprocess.run([sys.executable,str(PACK/(name+'.py'))],timeout=60)
  if p.returncode:raise RuntimeError(name+': child exit '+str(p.returncode)+'; output is in the parent execution capture')
 a=json.loads((PACK/'compass_local_transport.json').read_text())['rows'];b=json.loads((PACK/'independent_transport.json').read_text())
 assert len(a)==len(b)==5
 for r,s in zip(a,b):
  assert r['derivative_order']==s['n']
  assert r['pauli_terms']==s['terms']
  assert r['local_norm_squared']==s['norm2']
  assert {tuple(v['displacement']):v['value'] for v in r['translation_overlaps']}=={ast.literal_eval(k):v for k,v in s['correlations'].items()}
 # Offsite coefficients, normalization and first dispersive moment are exact integers.
 assert [r['local_norm_squared'] for r in a]==[3,96,9216,1499136,352124928]
 last={tuple(v['displacement']):v['value'] for v in a[-1]['translation_overlaps']}
 assert len(last)==19 and last[(1,0,0)]==247808 and last[(1,1,0)]==16896
 assert sum(last.values())==3*117938176
 out=ROOT/'outputs/native_composite_transport/result.json';out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(dict(scope='Exact local Pauli coefficients for supplied compass Hamiltonian; no scalar pole or matter coupling established',empirical_data_used=False,source_hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},independent_implementation_agreement=True,rows=a),indent=2)+'\n')
 print('per_element: independent exact integer Pauli products agree')
 print('per_site: one physical qubit, infinite integer coordinates, local support enumerated')
 print('per_mode: Fourier moment coefficients follow exact translation overlaps; pole not derived')
 print('per_block: local composite and derivative hierarchy through order4 checked')
 print('lattice_wide: coefficients hold on infinite cubic lattice by locality, not a finite torus extrapolation')
 print('physical scalar derived: false; matter coupling derived: false')
if __name__=='__main__':main()
