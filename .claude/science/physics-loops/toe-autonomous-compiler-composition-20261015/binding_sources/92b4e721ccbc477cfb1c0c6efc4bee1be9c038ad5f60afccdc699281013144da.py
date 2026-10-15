"""Record an explicit root source review after, not instead of, reading it."""
from pathlib import Path
import argparse, datetime, hashlib, json

D=Path(__file__).resolve().parent
N=D.parent
S=N/'autonomous_compiler_composition_publication_draft'
PACK='.claude/science/physics-loops/toe-autonomous-compiler-composition-20261015'
NOTE='docs/AUTONOMOUS_COMPILER_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-10-15.md'
PRIMARY='scripts/autonomous_compiler_composition_2026_10_15.py'
def pin(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def read(p):
    return json.loads(p.read_text())
def write(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,indent=2)+'\n')
ap=argparse.ArgumentParser()
ap.add_argument('--freeze-sha',required=True)
ap.add_argument('--coverage-sha',required=True)
a=ap.parse_args()
seal=S/'FINAL_FREEZE.json'
assert pin(seal)['sha256']==a.freeze_sha
freeze=read(seal)
for row in freeze['files']:
    actual=pin(S/row['path'])
    assert all(actual[k]==row[k] for k in ('bytes','sha256')),row['path']
assert {p.resolve() for p in S.rglob('*') if p.is_file()}=={
    (S/row['path']).resolve() for row in freeze['files']}|{seal.resolve()}
coverage=D/'READ_COVERAGE.md'
assert pin(coverage)['sha256']==a.coverage_sha
body_map=read(S/'proposal'/PACK/'BODY_MAP.json')
raw=(S/'proposal'/NOTE).read_bytes()
for row in body_map['bodies']:
    b=raw[row['start_byte_inclusive']:row['end_byte_exclusive']]
    assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
    assert raw.count(b)==1
decision='Accept the reviewed source-preserving publication package for root integration as conditional support; no retained audit or native physical closure.'
review={'kind':'root_source_publication_review',
        'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'root_read_complete':True,'source_draft_freeze':pin(seal),
        'note':pin(S/'proposal'/NOTE),'primary':pin(S/'proposal'/PRIMARY),
        'body_pins':body_map['bodies'],
        'parent_binding':read(S/'proposal'/PACK/'PARENT_BINDING.json'),
        'read_coverage':pin(coverage),'decision':decision,
        'source_recovery':pin(N/'source_recovery/RENEWAL_SOURCE_REUSE.json'),
        'preliminary_review':pin(N/'root_publication_pre_read/PRELIMINARY_REVIEW.json'),
        'scientific_programs_run_this_review':0,'primary_runs':0,'historical_programs_replayed':0,
        'limits':['Root authored this source review. This recording script verifies identities, not mathematics.',
                  'No new protected derivation, independent-model replication, retained audit or physical demonstration.',
                  'Canonical relocation and implementation edits require separate affected-content review.',
                  'Runtime and supplied preparation-to-runtime budgets stay distinct; permanent stopping/reuse remains open.'],
        'editable_prompt_files_changed':[]}
out=D/'REVIEW.json'
write(out,review)
sealed=D/'FINAL_FREEZE.json'
write(sealed,{'kind':'root_publication_source_review_freeze','utc':review['utc'],
              'files':[pin(out),pin(coverage)],'scientific_programs_run':0})
print(json.dumps({'review':pin(out),'freeze':pin(sealed),'scientific_programs_run':0}))
