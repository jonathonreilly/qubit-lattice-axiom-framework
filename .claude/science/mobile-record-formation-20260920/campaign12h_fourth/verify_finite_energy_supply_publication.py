"""Verify selected scientific bytes with explicit historical/external omissions."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
j=json.loads((HERE/'PUBLICATION_UNIT_FINITE_ENERGY_SUPPLY.json').read_text())
assert j['base_pr']==8923 and j['base_commit']=='191ad04ad48d64c55d31c34521caec68444bfa64'
assert j['claim_status']=='provisional review proposal; no audit verdict'
for group in ('artifacts','sources'):
    seen=set()
    for row in j[group]:
        assert row['path'] not in seen;seen.add(row['path'])
        p=HERE/row['path'];assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],str(p)
omissions={r['path']:r for r in j['explicit_omissions']}
assert len(omissions)==8
assert sum('/instructions/' in p for p in omissions)==7
assert 'full_instrument_energy_supply_independent/sources/Aberg_1304.1060v3.pdf' in omissions
for entry in j['seals']:
    p=HERE/entry['path'];assert sha(p)==entry['sha256']
    record=json.loads(p.read_text())
    for row in record.get('files',record.get('artifacts',[])):
        q=p.parent/row['path'];name=str(q.relative_to(HERE))
        if name in omissions:
            assert not q.exists() and row['sha256']==omissions[name]['sha256']
            assert row['bytes']==omissions[name]['bytes']
        else:
            assert q.stat().st_size==row['bytes'] and sha(q)==row['sha256'],name
    for name,pin in record.get('sources_sha256',{}).items():assert sha(HERE/name)==pin,name
assert json.loads((HERE/'coherent_energy_supply_independent/POST_RESULTS_02.json').read_text())['summary']['failed']==0
assert json.loads((HERE/'full_instrument_energy_supply_independent/COMPARISON_CONTROL_RESULTS.json').read_text())['all_assertions_passed']
print('per_element: exact local star matrices and all nine normalized actual marks are covered.')
print('per_site: complete four-site physical star; no second formation on this graph.')
print('per_mode: microscopic energy bands and battery charge blocks, not spatial photon modes.')
print('per_block: complete finite conserving unitary blocks, CP collision and signed energy accounting.')
print('lattice_wide: no growing-graph claim; generic finite-spectrum construction is conditional on its resources.')
print('Selected source/seal closure verified; seven procedural and one external bibliographic omission. No audit verdict.')
