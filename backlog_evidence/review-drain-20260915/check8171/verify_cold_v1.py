import pathlib,hashlib,json,subprocess
R=pathlib.Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot';h=lambda b:hashlib.sha256(b).hexdigest()
def g(*a):return subprocess.check_output(['git','-C',str(W),*a])
expected={'drain8171-author-unit-draft-v1.json':'823b3e2e86efde22d13af579073b1bed92c847a33409975ee326d9ca30101cc9','drain8171-capture-v1.py':'3ac252adfb2c0eced1b93eb071649e86fc1e581fb07019d5dc99707e5c38c588','drain8171-mutation-capture-v1.py':'76041434c6e8f7cf393e4a06cf667e94a10a8ede8191395d24ba8290fd1c1f9f','drain8171-capture-plan-v1.json':'12b72e616fd0579db2e76fbe74c8b18884db853416da60a460bca3662d68b352'}
for p,d in expected.items():assert h((R/p).read_bytes())==d
record=json.loads((R/'drain8171-author-unit-draft-v1.json').read_text());base=record['source']['base'];tree=record['source']['tree']
assert g('write-tree').decode().strip()==tree=='6630433b9aa6b17b66a64466a7484563b4fb61ef'
assert g('rev-parse','HEAD').decode().strip()==base
assert not g('diff','--name-only')
ps={e['path'] for e in record['source']['paths']};assert set(g('diff','--cached','--name-only','--no-renames',base).decode().splitlines())==ps
assert not g('diff','--cached','--name-only','--diff-filter=MD',base)
for e in record['source']['paths']+sum(record['inputs'].values(),[]):
 assert h((W/e['path']).read_bytes())==e['sha256']
 assert h(g('show',':'+e['path']))==e['sha256']
prepared=json.loads((R/'drain8171-author-prepared-v2.json').read_text())
assert {e['path']:e['sha256'] for e in prepared['source']}=={e['path']:e['sha256'] for e in record['source']['paths']}
for e in prepared['source']:
 mode=g('ls-files','-s','--',e['path']).decode().split()[0];assert mode==e['mode']
candidate='a0f8dbe92d402e4aacfa523023690a10c2c6770d';assert g('rev-parse',candidate+'^{tree}').decode().strip()=='2ab5e0ff2f8a8188572ffe402f0ded5f9433b214'
changes=set(g('diff','--name-only',base,candidate).decode().splitlines());assert not ps&changes
inputs={e['path'] for e in sum(record['inputs'].values(),[])}-ps;assert not inputs&changes
path='docs/SPHERE_LEVEL_KERNEL_MOMENTS_WALK_LOCAL_LIMIT_AND_FINITE_PLANE_MIXING_BOUNDED_THEOREM_NOTE_2026-09-16.md';b=g('show',candidate+':'+path)
(R/'check8171/train84-sphere8170-context.txt').write_bytes(b)
print(json.dumps(dict(source_tree=tree,source_paths=23,source_modes_match_prepared=True,all_inputs_match_disk_and_index=True,unstaged_changes=False,source_changes_since_early=False,candidate_commit=candidate,candidate_tree='2ab5e0ff2f8a8188572ffe402f0ded5f9433b214',candidate_changed_paths=len(changes),source_overlap=[],input_overlap=[],candidate_sphere_context_sha256=h(b),cheap_receipt_read=False,primary_executed=False),indent=2))
