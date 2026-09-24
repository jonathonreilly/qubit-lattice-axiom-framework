"""Check selected science and unchanged seals, with explicit procedure omissions."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((HERE/'PUBLICATION_UNIT_MICROSCOPIC_ENERGY.json').read_text())
assert manifest['base_pr']==8898
assert manifest['base_commit']=='99cfdfb105bd2b64715622093b2a7bf7accacaf9'
assert manifest['claim_status']=='provisional review proposal; no audit verdict'
for group in ('artifacts','sources'):
    seen=set()
    for row in manifest[group]:
        assert row['path'] not in seen;seen.add(row['path'])
        p=HERE/row['path']
        assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],row['path']
allowed={
 'microscopic_birth_energy_independent/instructions/'+n for n in
 ('SCIENCE_WORKFLOW.md','SKILL_FRESHNESS_CHECK.md','planning_AGENTS.md','repository_AGENTS.md','workhorse_SKILL.md')
}|{
 'microscopic_electric_robustness_independent/sources/'+n for n in
 ('SCIENCE_WORKFLOW.md','planning_AGENTS.md','repository_AGENTS.md')
}
omitted={x['path']:x for x in manifest['historical_procedure_omissions']}
assert set(omitted)==allowed
for packet,(sealname,pin) in manifest['packets'].items():
    assert sha(HERE/packet/sealname)==pin
    seal=json.loads((HERE/packet/sealname).read_text())
    for row in seal.get('files',seal.get('artifacts',[])):
        name=str(Path(packet)/row['path']);p=HERE/name
        if name in omitted:
            assert not p.exists()
            assert row['sha256']==omitted[name]['sha256'] and row['bytes']==omitted[name]['bytes']
        else:
            assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],name
    for name,pin in seal.get('sources_sha256',{}).items():assert sha(HERE/name)==pin,name
for packet,sealname,pin in (
 ('microscopic_birth_energy_independent','PRE_SEAL.json','82e5b45bc8ecf0aad7deb8f2af8c457062c2bcb860dc83d18c4538a1ac3053d9'),
 ('microscopic_electric_robustness_independent','PRE_SEAL.json','92f534204e822fbbc38f4cfbd8a5f6d1d33f09b727d7bead68fd22dfb4734faa')):
    assert sha(HERE/packet/sealname)==pin
    seal=json.loads((HERE/packet/sealname).read_text())
    for row in seal.get('files',seal.get('artifacts',[])):
        name=str(Path(packet)/row['path'])
        if name in omitted:assert row['sha256']==omitted[name]['sha256']
        else:assert sha(HERE/name)==row['sha256'],name
first=json.loads((HERE/'microscopic_birth_energy_independent/POST_RESULTS_02.json').read_text())
assert first['status']=='completed' and first['summary']['failed']==0
second=json.loads((HERE/'microscopic_electric_robustness_independent/COMPARISON_RESULTS.json').read_text())
assert second['summary']['actual_marks_compared']==9
assert second['summary']['scientific_discrepancies']==[]
print('per_element: all actual local star shifts and marked full-H moments are covered.')
print('per_site: the complete four-site Gauss sector is enumerated; it permits one formation only.')
print('per_mode: microscopic energy bands and no-event modes are covered; spatial or photon modes are not.')
print('per_block: complete N=1/N=3, P/W and gain/loss blocks are included; density and energy limits stay distinct.')
print('lattice_wide: no growing-graph or volume result is executed; the theorem is a fixed physical star.')
print('Selected source/seal closure verified with eight declared historical procedure omissions. No audit verdict.')
