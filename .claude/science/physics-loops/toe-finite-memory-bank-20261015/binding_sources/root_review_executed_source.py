"""Root publication-source decision and exact metadata verification; no science run."""
from pathlib import Path
from datetime import datetime, timezone
import ast, difflib, hashlib, json

N=Path(__file__).resolve().parents[1]
B=N/'finite_bank_publication_draft'
W=N.parent/'correlation_worktree'
R=N/'finite_bank_root_publication_review'
PACK='.claude/science/physics-loops/toe-finite-memory-bank-20261015'
NOTE='docs/FINITE_CONSUMED_MEMORY_BANK_BOUNDED_THEOREM_NOTE_2026-10-15.md'
FREEZE='da49c7c8d76ecd35ac6a02a8cfbb37a263df9f29d11bc5b7aa18369b0426274f'
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):
    b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
def read(p):return json.loads(p.read_bytes())
def verify(p,r):assert (p.stat().st_size,sha(p.read_bytes()))==(r['bytes'],r['sha256']),str(p)
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
assert not R.exists()
assert sha((B/'FINAL_FREEZE.json').read_bytes())==FREEZE
f=read(B/'FINAL_FREEZE.json')
for r in f['files']:verify(Path(r['path']),r)
assert {str(p) for p in B.rglob('*') if p.is_file()}=={r['path'] for r in f['files']}|{str(B/'FINAL_FREEZE.json')}
assert len(f['files'])==180
fresh=read(B/'SOURCE_FRESHNESS.json')
for r in fresh['identities']:verify(Path(r['original']),r)
for r in read(B/'TEMPLATE_MANIFEST.json')['files']:
    verify(B/r['path'],r);verify(Path(r['origin']),r)
changes=read(B/'CHANGED_CODE_MAP.json')
for r in changes['files']:
    a=(B/'template_snapshot'/r['file']).read_text();b=(B/r['file']).read_text()
    assert sha(a.encode())==r['old_sha256'] and sha(b.encode())==r['new_sha256']
    expected=''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='correlated_memory_publication_draft/'+r['file'],tofile='finite_bank_publication_draft/'+r['file']))
    assert (B/r['complete_diff']).read_text()==expected
    if r['file'].endswith('.py'):ast.parse(b)
for p in sorted((B/'packet_text').iterdir()):
    old=B/'template_snapshot/packet_text'/p.name;a=old.read_text() if old.exists() else '';b=p.read_text()
    expected=''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='correlated_memory_publication_draft/packet_text/'+p.name if old.exists() else '/dev/null',tofile='finite_bank_publication_draft/packet_text/'+p.name))
    assert (B/'diffs'/('packet_'+p.name+'.diff')).read_text()==expected
out=B/'proposal';packet=out/PACK;note=(out/NOTE).read_bytes()
for r in read(packet/'BODY_MAP.json')['bodies']:
    body=note[r['start_byte_inclusive']:r['end_byte_exclusive']]
    assert (len(body),sha(body),note.count(body))==(r['bytes'],r['sha256'],1)
sources=read(packet/'SOURCE_MANIFEST.json')['sources']
for r in sources:
    loc=r['recovery']
    if loc['kind']=='blob':b=(out/loc['path']).read_bytes()
    elif loc['kind']=='external_pinned':b=(W/loc['path']).read_bytes()
    else:
        p=out/loc['container']
        if not p.exists():p=W/loc['container']
        b=p.read_bytes()[loc['start_byte_inclusive']:loc['end_byte_exclusive']]
    assert (len(b),sha(b))==(r['bytes'],r['sha256'])
for r in read(packet/'INPUT_MANIFEST.json')['inputs']:verify(out/r['path'],r)
receipts=[]
for label in ('build','inspection'):
    p=B/'metadata_runs'/label;e=read(p/'EXECUTION.json')
    assert e['exit_code']==0 and e['failure'] is None and e['scientific_execution'] is False
    for k in ('child_source_at_launch','stdout','stderr','recorder','recorder_at_launch'):verify(Path(e[k]['path']),e[k])
    launch=read(p/'LAUNCH.json')
    for r in launch['inputs']:
        verify(Path(r['original']['path']),r['original']);verify(Path(r['captured']['path']),r['captured'])
    assert not (p/'stderr').read_bytes()
    receipts.append(pin(p/'EXECUTION.json'))
accept=N/'conditional_sources_root_review/FINITE_BANK_ACCEPTANCE.md'
assert pin(accept)['sha256']=='5bf680ccc41224a0446210d20cbc110ef5ebd63c426ed02de72612148a22e908'
R.mkdir()
review={
 'kind':'root_source_publication_review','utc':datetime.now(timezone.utc).isoformat(),
 'root_read_complete':True,'source_draft_freeze':pin(B/'FINAL_FREEZE.json'),
 'sealed_members_verified':len(f['files']),'source_rows_verified':len(sources),
 'full_current_files_read':[pin(B/x) for x in ('wrapper.md','primary_template.py','build_proposal.py','inspect_proposal.py','record_metadata.py','seal_packet.py')]+[pin(p) for p in sorted((B/'packet_text').iterdir())],
 'reading_scope':'All current changed wrapper, module-level assembly, helper functions, primary and packet text read in full. Complete old-to-new diffs are mechanically verified; the prior correlated template reading is reused by exact identity. The first combined read was truncated at wrapper end and primary start; a second complete primary and wrapper-end read repaired that coverage before this decision.',
 'scientific_source_reading_reused':{'author':'162d7504ad3951ed29add0facefc0bbdb227fcdf582e22250baad04a4f63c521','review':'16f6fbc729dd24fb77df435ecfe86b9545bf875ceec25067893a0ed853f811b6','decision':pin(accept),'actual_root_receipt':pin(N/'runs/conditional_sources_root_acceptance_1726/EXECUTION.json')},
 'existing_source_acceptances':{'finite_bank':pin(accept)},
 'mandatory_current_scope':['Finite supplied bank is consumed, not restored; all records retained.','One global g(delta) replacement; purity only on ideal unused blocks.','Compensation action equals norm(C) times integrated amplitude and is at most B_C times that amplitude.','Guards counted only as H0 aging remain fully compensated; other waits require ordered actual segments or comparison residuals.','Every source, intervening operation and whole bank lifetime has its own control/isolation cost.','The sole direct mathematical parent is correlated-memory canonical12bd18b0; local-bias/rotation and incidental Git ancestry are not imported.'],
 'actual_metadata_receipts':receipts,'scientific_programs_run':0,'historical_programs_replayed':0,
 'decision':'Publication interpretation accepted at existing conditional source scope; actual checkout binding and integration remain pending.',
 'remaining':'Select actual base and bind sources, execute primary/cache/schema mutations/focused checks, preserve graph, review canonical delta, publish regular PR and attach. No retained audit, native supplier or control apparatus is established.'}
write(R/'ROOT_REVIEW.json',review)
write(R/'FINAL_FREEZE.json',{'utc':datetime.now(timezone.utc).isoformat(),'scope':'Root metadata/source publication decision only','files':[pin(R/'ROOT_REVIEW.json')]})
print(json.dumps({'review':pin(R/'ROOT_REVIEW.json'),'freeze':pin(R/'FINAL_FREEZE.json'),'verified_members':len(f['files']),'verified_sources':len(sources),'scientific_programs_run':0}))
