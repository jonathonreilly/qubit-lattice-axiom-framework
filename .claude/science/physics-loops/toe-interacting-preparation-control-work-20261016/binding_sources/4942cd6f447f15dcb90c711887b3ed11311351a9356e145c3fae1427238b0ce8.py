from pathlib import Path
from datetime import datetime, timezone
import ast, hashlib, json, subprocess
N=Path(__file__).resolve().parents[1]
O=N/'interacting_control_integration_proposal'
S=N/'interacting_control_qualified_publication_draft'
D=N/'publication_integration/interacting_control'
W=N.parent/'correlation_worktree'
R=N/'root_interacting_control_qualified_publication_review'
def read(p): return json.loads(Path(p).read_text())
def pin(p):
    p=Path(p); b=p.read_bytes()
    return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def same(p,r): assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def write(p,v):
    with Path(p).open('x') as f: f.write(json.dumps(v,indent=2)+'\n')
def functions(p):
    s=Path(p).read_text(); lines=s.splitlines(True)
    return {n.name:''.join(lines[n.lineno-1:n.end_lineno]) for n in ast.parse(s).body if isinstance(n,ast.FunctionDef)}
assert pin(O/'FINAL_FREEZE.json')['sha256']=='1f8cb53bc0108c7cdd19a4963d92d7f872eb2cd4d83efa87a4e4a9ef427f0eb6'
f=read(O/'FINAL_FREEZE.json'); assert len(f['files'])==158
assert {str(p.relative_to(O)) for p in O.rglob('*') if p.is_file()}=={r['path'] for r in f['files']}|{'FINAL_FREEZE.json'}
for row in f['files']: same(O/row['path'],row)
sf=read(S/'FREEZE.json'); assert len(sf['members'])==176
assert pin(S/'FREEZE.json')['sha256']=='a82254aa003e3de63109e532adca46c771ec122d910528e9f9ff0f9e2e8996e2'
for row in sf['members']: same(S/row['path'],row)
receipts=[]
for p in sorted((O/'metadata_runs').glob('*/EXECUTION.json')):
    r=read(p); launch=read(p.parent/'LAUNCH.json')
    assert all(r[k]==v for k,v in launch.items())
    assert r['exit_code']==0 and not r['timed_out'] and r['timeout_seconds']==60
    assert r['started_utc']<=r['finished_utc'] and r['scientific_executions']==r['canonical_phases_executed']==0
    keys=('source_and_launcher_at_launch',) if p.parent.name=='seal' else ('source_at_launch','launcher_at_launch')
    for k in (*keys,'stdout','stderr'): same(r[k]['path'],r[k])
    cap=r[keys[0]]
    same(cap['path'],r['original_source'])
    assert r['argv'][1]=='-B' and r['argv'][2]==cap['path'] and cap['path']!=r['original_source']['path']
    assert Path(r['stderr']['path']).read_bytes()==b''
    json.loads(Path(r['stdout']['path']).read_text())
    receipts.append(pin(p))
assert len(receipts)==6
reuse=[]
for g in read(O/'FUNCTION_REUSE_MAP.json')['groups']:
    current=O/('interacting_control_common.py' if g['group']=='common' else 'primary_extension.py')
    ref=O/'reference_sources'/('common.py' if g['group']=='common' else 'extension.py')
    assert pin(current)['sha256']==g['new_sha256'] and pin(ref)['sha256']==g['reference_sha256']
    a,b=functions(ref),functions(current); assert set(a)|set(b)=={r['name'] for r in g['functions']}
    for row in g['functions']:
        name=row['name']; assert row['source_exact']==(a.get(name)==b.get(name))
        assert row['new_sha256']==hashlib.sha256(b[name].encode()).hexdigest()
        assert row['old_sha256']==(hashlib.sha256(a[name].encode()).hexdigest() if name in a else None)
    reuse.append(dict(group=g['group'],exact=sum(r['source_exact'] for r in g['functions']),changed=[r['name'] for r in g['functions'] if not r['source_exact']]))
assert reuse[0]['exact']==26 and reuse[1]['exact']==3
sp=functions(S/'proposal/scripts/interacting_preparation_control_work_2026_10_16.py')
np=functions(O/'proposed_primary_unbound.py')
for name in ('require','digest','identity','disk_read'): assert sp[name]==np[name]
assert sp['verify_payload']==np['verify_payload'].replace('SOURCE_MANIFEST_SHA256','MANIFEST_SHA256').replace('SOURCE_AUDIT_INPUT_PATHS','AUDIT_INPUT_PATHS')
note=(O/'PROPOSED_NOTE.md').read_bytes()
for b in read(O/'PROPOSED_BODY_MAP.json')['bodies']:
    data=note[b['start_byte']:b['end_byte_exclusive']]
    assert len(data)==b['bytes'] and hashlib.sha256(data).hexdigest()==b['sha256']
    same(N/b['source'],b)
parents=read(O/'PARENT_BINDING.json')['direct_canonical_parents']; assert len(parents)==2
for r in parents: same(W/r['path'],r)
for r in read(O/'EXECUTION_TOOL_PINS.json')['files']: same(W/r['path'],r)
observed=read(O/'OBSERVED_SOURCE_REVIEW.json')
for r in observed['aliases']: same(O/r['recovery']['path'],r['original'])
same(R/'REVIEW.json',observed['review'])
assert observed['review']['sha256']=='6359efd97be3f28ed504430a501269027ad279fd2738a258a9d222d801f47f67'
run=N/'runs/interacting_control_source_publication_review_v2'
same(run/'EXECUTION.json',observed['runs'][1])
base=read(O/'BASE_BINDING_INPUT.json')
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=W).decode().strip()==base['base_head']
assert subprocess.check_output(['git','status','--porcelain','-z'],cwd=W)==b''
refresh_receipts=[]
for label in ('source_fetch_1854','open_inventory_1854','interacting_base_refs_1854'):
    p=N/'runs'/label/'EXECUTION.json'; r=read(p); assert r['exit_code']==0
    for k in ('stdout','stderr'): same(r[k]['path'],r[k])
    refresh_receipts.append(pin(p))
lines=(N/'runs/interacting_base_refs_1854/stdout').read_text().splitlines()
assert lines==['7cce8eaa5a72862e0ba884028a21e792c04a6df7','18938dc21fda858a6667ff9e0714818754802a6f','5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2','56c5c0ab64f532c5784e895b2f9aa6894fa334e0']
inventory=read(N/'runs/open_inventory_1854/stdout')
assert {r['number'] for r in inventory}=={9647,9648}
pr=next(r for r in inventory if r['number']==9648)
assert pr['state']=='OPEN' and not pr['isDraft'] and pr['headRefOid']==base['base_head'] and pr['baseRefName']==base['base_parent_branch']
D.mkdir(parents=True,exist_ok=True)
refresh=dict(utc=datetime.now(timezone.utc).isoformat(),refs={'HEAD':lines[0],'origin/main':lines[2],'origin/ai/execution':lines[3]},active_tree=lines[1],inventory=pin(N/'runs/open_inventory_1854/stdout'),actual_receipts=refresh_receipts,scope='Actual current refs and open inventory; authority and main unchanged. Unrelated remote campaign branch advanced; it adds no premise here.')
write(D/'FRESH_REFRESH.json',refresh)
review=dict(utc=datetime.now(timezone.utc).isoformat(),kind='root_integration_source_review',root_read_complete_for_changed_implementation=True,proposal_freeze=pin(O/'FINAL_FREEZE.json'),common=pin(O/'interacting_control_common.py'),primary_unbound=pin(O/'proposed_primary_unbound.py'),source_publication_review=pin(R/'REVIEW.json'),members_verified=158,unchanged_source_members=176,unchanged_mathematical_bodies=9,direct_mathematical_parents=parents,function_reuse=reuse,metadata_receipts=receipts,actual_canonical_acceptance=None,retained_audit=False,scientific_executions=0,editable_prompt_files_changed=[],scope='Complete changed common/extension functions and globals, all new metadata source/recorders, wrapper/certificate/PR text, actual complete six metadata streams and source-review failure recovery inspected. Exact unchanged code and proof bodies reuse recorded prior review, with their identities rechecked. Fixed OPEN parent only; closure requires separate transport review. Canonical, staged and publication actions remain pending. Source-review checkpoint evolution does not imply recovery of unavailable historical bytes. Metadata checks are not mathematical or physical verification.')
write(D/'ROOT_INTEGRATION_REVIEW.json',review)
print(json.dumps(dict(review=pin(D/'ROOT_INTEGRATION_REVIEW.json'),refresh=pin(D/'FRESH_REFRESH.json'),metadata_receipts=len(receipts),canonical_phases_executed=0)))
