from pathlib import Path
import datetime, hashlib, json, subprocess

N=Path(__file__).resolve().parents[1]
W=N.parent/'correlation_worktree'
O=N/'bounded_slew_integration_proposal'
D=N/'publication_integration/bounded_slew_compiler'
PACK='.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015'
NOTE='docs/BOUNDED_SLEW_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md'
HELPER='scripts/bounded_slew_positive_time_compiler_2026_10_15.py'
def read(p):return json.loads(p.read_text())
def pin(p):
    b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def git(*args):return subprocess.check_output(['git','-C',str(W),*args],text=True).strip()
assert git('branch','--show-current')=='physics-loop/toe-bounded-slew-compiler-20261015'
assert git('rev-parse','HEAD')=='9ca474a32b3a4799d2d14cfee7580d77750422b4'
prepared=read(D/'PREPARED.json')
for name,row in prepared['canonical_files'].items():
    a=pin(W/name);assert all(a[k]==row[k] for k in ('bytes','sha256')),name
content=read(D/'ROOT_PREPARED_CONTENT_REVIEW.json')
assert content['prepared']==pin(D/'PREPARED.json') and content['diff']==pin(D/'CANONICALIZATION.diff')
integration=read(N/'root_bounded_slew_integration_review/REVIEW.json')
assert integration['common']==pin(O/'bounded_slew_common.py')
review={'kind':'root_installed_canonical_source_review',
        'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'root_read_complete':True,
        'bound_note_sha256':pin(W/NOTE)['sha256'],
        'canonical_body_pins':read(W/PACK/'BODY_MAP.json')['bodies'],
        'parent_binding':read(W/PACK/'PARENT_BINDING.json'),
        'source_draft_freeze_sha256':pin(N/'bounded_slew_publication_draft/FINAL_FREEZE.json')['sha256'],
        'source_draft_review_sha256':pin(N/'root_bounded_slew_publication_review/REVIEW.json')['sha256'],
        'git_base':git('rev-parse','HEAD'),'prebinding_primary':pin(W/HELPER),
        'integration_common':pin(O/'bounded_slew_common.py'),
        'root_integration_review':integration,'prepared_content_review':content,
        'coverage':'Installed files match the reviewed canonical copy exactly. Frozen source wrapper and complete mathematical bodies were reviewed under their original identities; full final active text replacements and changed integrity logic were read, and canonical byte intervals separately checked. Captured historical receipts and literal inventories are byte/schema evidence, not additional scientific verification.',
        'decision':'Accept this exact installed canonical source and the reviewed metadata-only binding step for scoped execution and regular PR publication.',
        'scientific_programs_run':0,'primary_runs_at_review':0,'retained_audit':False,
        'editable_prompt_files_changed':[]}
p=D/'ROOT_INSTALLED_CANONICAL_REVIEW.json';assert not p.exists()
p.write_text(json.dumps(review,indent=2)+'\n')
print(json.dumps({'review':pin(p),'scientific_programs_run':0}))
