"""Record root's completed content review and verify its source identities."""
from pathlib import Path
import ast
import datetime
import hashlib
import json

D=Path(__file__).resolve().parent
N=D.parent
S=N/'strongly_regular_bus_publication_draft'
PACK='.claude/science/physics-loops/toe-strongly-regular-bus-20261015'
NOTE='docs/STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md'
PRIMARY='scripts/strongly_regular_bus_2026_10_15.py'
FREEZE='71d6aa8f22b83ac1ee6aaac0f6351c58ada14d4cbdc3bf80e44a8d5db719e42f'
def pin(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def read(p):return json.loads(p.read_text())
def write(p,v):
    with p.open('x') as out:json.dump(v,out,indent=2);out.write('\n')
seal=S/'FINAL_FREEZE.json'
assert pin(seal)['sha256']==FREEZE
freeze=read(seal)
for row in freeze['files']:
    actual=pin(S/row['path'])
    assert all(actual[k]==row[k] for k in ('bytes','sha256')),row['path']
assert {p.resolve() for p in S.rglob('*') if p.is_file()}=={(S/r['path']).resolve() for r in freeze['files']}|{seal.resolve()}
reuse=read(S/'REUSE_MAP.json')
for row in reuse['reference_files']:
    got=pin(Path(row['path']))
    assert (got['bytes'],got['sha256'])==(row['bytes'],row['sha256'])
for row in reuse['functions']:
    for side,base in [('reference',Path(reuse['reference_package'])),('current',S)]:
        part=row[side]
        if part is None:continue
        raw=''.join((base/row['script']).read_text().splitlines(keepends=True)[part['line_start']-1:part['line_end']]).encode()
        assert (len(raw),hashlib.sha256(raw).hexdigest())==(part['bytes'],part['sha256'])
    if row['byte_exact_reuse']:
        assert row['reference']['sha256']==row['current']['sha256']
body_map=read(S/'proposal'/PACK/'BODY_MAP.json')
raw=(S/'proposal'/NOTE).read_bytes()
for row in body_map['bodies']:
    b=raw[row['start_byte_inclusive']:row['end_byte_exclusive']]
    assert (len(b),hashlib.sha256(b).hexdigest())==(row['bytes'],row['sha256']) and raw.count(b)==1
parents=read(S/'proposal'/PACK/'PARENT_BINDING.json')
for row in parents['canonical_parents']+parents['transitive_premises']:
    actual=pin(N.parent/'correlation_worktree'/row['path'])
    assert all(actual[k]==row[k] for k in ('bytes','sha256'))
assert len(parents['canonical_parents'])==0 and not parents['transitive_premises']
for row in parents['canonical_parents']:
    raw=(N.parent/'correlation_worktree'/row['path']).read_bytes()
    for part in row['accepted_body_intervals']+row['used_premise_intervals']:
        b=raw[part['start_byte_inclusive']:part['end_byte_exclusive']]
        assert len(b)==part['bytes'] and hashlib.sha256(b).hexdigest()==part['sha256']
for row in read(S/'SOURCE_FRESHNESS.json')['identities']:
    actual=pin(Path(row['original']));assert all(actual[k]==row[k] for k in ('bytes','sha256'))
# Compare the generated primary to the reviewed template after literal substitution.
primary_raw=(S/'proposal'/PRIMARY).read_text()
assign={n.targets[0].id:ast.literal_eval(n.value) for n in ast.parse(primary_raw).body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in {'EXPECTED_PARENTS','EXPECTED_BODIES','MANIFEST_SHA256','AUDIT_INPUT_PATHS'}}
assert assign['EXPECTED_PARENTS']=={r['path']:(r['bytes'],r['sha256'],r['claim_id']) for r in parents['canonical_parents']}
assert set(assign['AUDIT_INPUT_PATHS'])=={r['path'] for r in read(S/'proposal'/PACK/'INPUT_MANIFEST.json')['inputs']}|{PACK+'/INPUT_MANIFEST.json',PACK+'/ACTUAL_BINDING.json'}|set(assign['EXPECTED_PARENTS'])
assert assign['MANIFEST_SHA256']==pin(S/'proposal'/PACK/'INPUT_MANIFEST.json')['sha256']
template=(S/'primary_template.py').read_text()
for key in ('EXPECTED_PARENTS','EXPECTED_BODIES','AUDIT_INPUT_PATHS'):
    template=template.replace('__'+key+'__',repr(assign[key]))
template=template.replace('__MANIFEST_SHA256__',assign['MANIFEST_SHA256'])
assert ast.dump(ast.parse(template),include_attributes=False)==ast.dump(ast.parse(primary_raw),include_attributes=False)
# Confirm new inspector validator is the same fully read executable function.
parts=[]
for name in ('primary_template.py','inspect_proposal.py'):
    text=(S/name).read_text()
    parts.append(next(ast.get_source_segment(text,node) for node in ast.parse(text).body if isinstance(node,ast.FunctionDef) and node.name=='historical_receipt'))
assert parts[0]==parts[1]
assert not parents['preparation_release_intervals']
coverage=D/'READ_COVERAGE.md'
review={'kind':'root_source_publication_review','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'root_read_complete':True,'source_draft_freeze':pin(seal),'note':pin(S/'proposal'/NOTE),
    'primary':pin(S/'proposal'/PRIMARY),'body_pins':body_map['bodies'],'parent_binding':parents,
    'read_coverage':pin(coverage),'reuse_map':pin(S/'REUSE_MAP.json'),
    'verified_function_rows':len(reuse['functions']),'byte_exact_reused_functions':sum(r['byte_exact_reuse'] for r in reuse['functions']),
    'source_acceptance':pin(N/'strongly_regular_bus_root_review/QUALIFIED_ACCEPTANCE.json'),
    'freshness':pin(N/'refresh_before_strongly_regular_bus/BINDING_REFS.json'),
    'decision':'Accept reviewed source-preserving package for root integration as conditional support; canonical review remains separate.',
    'required_canonical_text_correction':{'before':'Unaccepted joint-energy and static-bias continuations are excluded.','after':'Separate joint-energy and static-bias continuations are excluded.','scope':'Later acceptance chronology only; neither continuation is imported.'},
    'scientific_programs_run_this_review':0,'primary_runs':0,'historical_programs_replayed':0,
    'limits':['This root content review is recorded after actual reading; this script validates identity only.',
              'No retained audit, compiler execution, different-model-family replication or physical realization.',
              'Final canonical offsets, metadata edits and actual integration checks require affected-content review.'],
    'editable_prompt_files_changed':[]}
out=D/'REVIEW.json';write(out,review)
sealed=D/'FINAL_FREEZE.json'
write(sealed,{'kind':'root_publication_source_review_freeze','utc':review['utc'],
    'files':[pin(out),pin(coverage)],'scientific_programs_run':0})
print(json.dumps({'review':pin(out),'freeze':pin(sealed),'scientific_programs_run':0}))
