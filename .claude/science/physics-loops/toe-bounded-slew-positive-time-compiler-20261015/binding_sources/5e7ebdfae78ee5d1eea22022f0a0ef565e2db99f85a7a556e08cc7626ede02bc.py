"""Record root's completed content review and verify its source identities."""
from pathlib import Path
import ast
import datetime
import hashlib
import json

D=Path(__file__).resolve().parent
N=D.parent
S=N/'bounded_slew_publication_draft'
PACK='.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015'
NOTE='docs/BOUNDED_SLEW_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md'
PRIMARY='scripts/bounded_slew_positive_time_compiler_2026_10_15.py'
FREEZE='0add271622a6912ce736e43f106f90a4c40e09ab3115cdc0ec0ea6b7a10fd06f'
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
coverage=D/'READ_COVERAGE.md'
review={'kind':'root_source_publication_review','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'root_read_complete':True,'source_draft_freeze':pin(seal),'note':pin(S/'proposal'/NOTE),
    'primary':pin(S/'proposal'/PRIMARY),'body_pins':body_map['bodies'],'parent_binding':parents,
    'read_coverage':pin(coverage),'reuse_map':pin(S/'REUSE_MAP.json'),
    'verified_function_rows':len(reuse['functions']),'byte_exact_reused_functions':sum(r['byte_exact_reuse'] for r in reuse['functions']),
    'source_acceptance':pin(N/'bounded_slew_root_candidate/QUALIFIED_ACCEPTANCE.json'),
    'freshness':pin(N/'refresh_before_bounded_slew/REFS.json'),
    'decision':'Accept reviewed source-preserving package for root integration as conditional support; canonical review remains separate.',
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
