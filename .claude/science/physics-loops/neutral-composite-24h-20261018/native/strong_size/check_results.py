"""Cross-check independently computed data; does not certify a stable feature."""
from pathlib import Path
import json,numpy as np
P=Path(__file__).resolve().parent
load=lambda f:json.loads((P/f).read_text())
a=load('algebra_control.json');b=load('compact_patch_control.json');assert a['all_pass'] and b['all_pass']
ends={r['L']:r for r in load('endcap_control.json')['rows']}
mx=0
for r in load('mps_size.json')['rows']:
 # The expectation identity is state-independent, so numerical mismatch directly tests implementation.
 actual=r.get('raw_string_energy',r.get('raw_energy'))
 if actual is None: print('Keys',r.keys());raise KeyError('raw energy key')
 expected=[x['endcap_energy'] for x in ends[r['L']]['lengths']]
 mx=max(mx,float(np.max(abs(np.array(actual)-expected))))
assert mx<1e-8
exact={r['L']:r for r in load('periodic_exact.json')}
r=exact[8];spread=max(x['energy'] for x in r['raw'])-min(x['energy'] for x in r['raw']);assert spread<1e-7 and r['residual']<1e-8
# MPS does not fix the global X-pair character, so this is a numerical comparison, not a cross-sector variational theorem.
m=load('periodic_mps.json')['rows'][0];error=m['stages'][-1]['energy']-r['energy']
result=dict(endcap_identity_max_error=mx,periodic_ED_length_spread=spread,periodic_ED_residual=r['residual'],periodic_MPS_minus_ED_energy=error,algebra_cases=a['cases'],compact_patch_cases=b['cases'],scope='Author consistency checks only; independent review pending; no stable-size certificate')
(P/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
