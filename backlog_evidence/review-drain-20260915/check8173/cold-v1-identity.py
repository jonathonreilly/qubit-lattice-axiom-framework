import pathlib,json,hashlib,subprocess
R=pathlib.Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def git(*a):return subprocess.check_output(['git','-C',str(W),*a])
dp=R/'drain8173-author-unit-draft-v1.json';d=json.loads(dp.read_text());assert sha(dp)=='1fc8ad873caf277a1b1842867730fef0b2a203f6406492260f1edb4b0eade1ca'
assert sha(R/'drain8173-author-cheap-v1.json')=='c53f4fe1866baeefacc158f42118b01a3a718b59644feaffefdb95564b78465c'
base=d['source']['base'];tree=d['source']['tree'];assert git('rev-parse','HEAD').decode().strip()==base
assert git('diff','--cached','--name-only',tree)==b'';assert git('diff','--name-only')==b''
prep=json.loads((R/'drain8173-author-prepared-v3.json').read_text()); pm={e['path']:e for e in prep['source']}
assert set(git('diff','--cached','--name-only',base).decode().splitlines())==set(pm)
rows=[]
for e in d['source']['paths']:
 p=e['path'];assert sha(W/p)==e['sha256']==pm[p]['sha256'];raw=git('show',':'+p);assert hashlib.sha256(raw).hexdigest()==e['sha256'];info=git('ls-files','--stage','--',p).decode().split();assert info[0]==pm[p]['mode'] and info[2]=='0';rows.append(dict(path=p,mode=info[0],blob=info[1],sha256=e['sha256']))
for group,entries in d['inputs'].items():
 for e in entries:assert sha(W/e['path'])==e['sha256'] and hashlib.sha256(git('show',':'+e['path'])).hexdigest()==e['sha256']
for e in d['reviewer']['references']:assert sha(pathlib.Path(e['path']))==e['sha256']
for fn,expected in [('drain8173-build-staged-draft-v1.py','72ce28cba7434db29b79a540c936c383d5e8f830d5c103fd4f804c35d97cd824'),('drain8173-capture-v1.py','53a1d0d1ea346032c8a9855653dc303906cc561553335a2ffbc0921bca047ce5'),('drain8173-mutation-capture-v1.py','3677d329364868e58eccde538d72ed5444d2cea806dadad34488ece912609007')]:assert sha(R/fn)==expected
changed=git('diff','--name-only','8bf464953779b8ada8415208e89a656411f9f525',base).decode().splitlines();bound={e['path'] for es in d['inputs'].values() for e in es};assert not set(changed)&bound
cache=W/'logs/runner-cache/sphere_static_finite_volume_covariance_response_projected_mode_sum_check_2026_09_16.txt';assert not cache.exists()
print(json.dumps(dict(base=base,tree=tree,source_entries=rows,all_record_inputs_index_and_worktree_verified=True,all_reviewer_references_verified=True,current_main_changed_paths=len(changed),changed_bound_inputs=[],cache_absent=True,worktree_delta_empty=True,index_matches_recorded_tree=True,primary_runs=0),indent=2))
