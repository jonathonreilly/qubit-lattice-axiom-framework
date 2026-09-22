import pathlib,json,hashlib,gzip,subprocess,sys
r=pathlib.Path('/private/tmp/review-drain-20260915');w=r/'drain-author-slot';main='0ee1a0396c2160605397ecf42f3602215a572c67'
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.check_output(['git','-C',str(w),*a])
def read(n):return json.loads((r/n).read_text())
d=read('drain8150-author-unit-draft-v1.json');h=read('drain8150-author-source-handoff-v1.json');orig=read('drain8150-original-review.json');inventory=read('drain8150-original-inventory.json')
assert git('write-tree').decode().strip()==d['source']['tree']==h['tree']
assert not git('diff','--name-only')
for args in [('diff','--check'),('diff','--cached','--check'),('diff',d['source']['base'],'--check')]:git(*args)
for x in d['source']['paths']:assert sha((w/x['path']).read_bytes())==x['sha256']
assert all(x.split('\t')[0]=='A' for x in git('diff','--cached','--name-status').decode().splitlines())
rows=[]
for u in inventory:
 for x in u['original_paths']:
  a=next(z for z in h['original_dispositions'][str(u['number'])] if z['original_path']==x['path'])
  assert sha(gzip.decompress((w/a['final_path']).read_bytes()))==a['original_sha256']==x['sha256']
  assert sha((w/a['final_path']).read_bytes())==a['final_sha256']
  rows.append(dict(pr=u['number'],**x,**a))
assert len(rows)==66
for group,inputs in d['inputs'].items():
 for x in inputs:assert sha((w/x['path']).read_bytes())==x['sha256']
for x in d['inputs']['parents']:assert sha(git('show',main+':'+x['path']))==x['sha256']
sys.path[:0]=[str(w/'scripts'),str(w/'docs/audit/scripts')]
import runner_cache as c,build_citation_graph as g,audit_packet_script_deps as p
p.SCRIPTS_DIR=w/'scripts';apis=[]
for a in read('drain8150-author-cache-api-v1.json'):
 f=w/a['primary']; inputs=list(c.declared_input_paths(f));assert inputs==a['declared_inputs'];assert c.declared_timeout_for(f)==300
 gh=list(g.resolve_helper_runner_paths(str(f)));ph=sorted(p.transitive_helpers(f.stem));assert not gh and not ph
 apis.append(dict(primary=a['primary'],timeout=300,graph_helpers=gh,packet_helpers=ph,inputs=[dict(path=v,sha256=sha((w/v).read_bytes())) for v in inputs],type=g.extract_claim_type_hint((w/inputs[0]).read_text())))
changes=git('diff','--name-status',d['source']['base'],main).decode().splitlines();contexts=[]
for line in changes:
 status,path=line.split('\t')
 if path.startswith('docs/') and '/work_history/' not in path and path.endswith('.md'):
  contexts.append(dict(path=path,sha256=sha(git('show',main+':'+path)),read_scope='claim scope, result and potentially interacting boundary/mixture assertions'))
newset={v['path'] for v in d['source']['paths']};assert not newset.intersection(line.split('\t')[-1] for line in changes)
refs=[]
for n in ['drain8150-original-review.json','drain8150-original-inventory.json','drain8150-independent-controls.py','drain8150-independent-controls.json','drain8150-author-unit-draft-v1.json','drain8150-author-source-handoff-v1.json','drain8150-author-cache-api-v1.json','drain8150-author-cheap-v1.json']:
 refs.append(dict(path=str(r/n),sha256=sha((r/n).read_bytes())))
out=dict(status='COLD SOURCE PASS WITH BOUNDED POSITIVE CLAIMS; EXECUTION AND FINAL CACHE CONFIRMATION PENDING',reviewer_session='/root/review_8011',source=d['source'],original_dispositions=rows,claim_dispositions=h['claim_dispositions'],inputs=d['inputs'],actual_api_closure=apis,findings_resolution={'8149_fixed_boundary':'Only sufficiency retained for arbitrary fixed exterior; unsupported converse explicitly deferred.','model_axiom_boundary':'Supplied sequential/joint/clock conventions distinguished from axioms; no realized-state statistical grant.','8148_scope':'Positive total rate, value-blind mixing, causal weight versus posterior, seeded trees, finite plaquette scope corrected.','gravity':'No gravity/static equivalence imported.','8149_coverage':'Five canonical star classes and two plus three environment orders stated; historical seven-class controls distinct.','negative_gate':'No negative-certification PASS. Universal exclusions deferred; original proofs and branch recovery preserved.'},mathematical_change='No computation/predicate/formula changes in the three runner diffs; metadata, scope labels and source text fences changed. Complete revised notes read; previous independent 5436 rational controls reused without rerun.',current_main=dict(commit=main,declared_parent_bytes_unchanged=True,new_context=contexts,assessment='New formation-suite notes retain supplied finite recorded-set/monotone models, conditional infinite-law regions and explicit negative deferrals. They neither select clocks/units nor repair the deferred arbitrary-boundary converse. Pair-additive exceptional points concern log K3 decomposition, not constancy of Kk in a recorded argument. No new dependency imported, no existing main source replaced, and no proposed source path collides with the added suite.'),allowed_capture=dict(runners=3,concurrency=1,timeout_seconds_each=300,rss_limit_bytes=3221225472,expected_pass_counts=[22,18,17],owner='root',preserve_all_attempts=True,no_scientific_execution_by_reviewer=True),references=refs,final_scope='Positive identities/sufficient constructions and exact finite witnesses only; no audit or universal negative certification. Final source/output/cache confirmation remains with this original reviewer after captures.')
p=r/'drain8150-preexecution-review.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
m=r/'drain8150-preexecution-review.md';assert not m.exists();m.write_text('# PR8148–8150 cold source confirmation\n\nPASS for the narrowed positive identities, sufficient constructions and finite witnesses at tree `'+d['source']['tree']+'`. All six original finding groups are addressed. Universal negative certification and arbitrary fixed-boundary necessity remain deferred; the 66 original versions are preserved exactly.\n\nAll source/input hashes, three actual four-input closures, empty helper closures and main `'+main+'` interactions were checked. The three arithmetic implementations are unchanged; the prior independent 5,436-check control is reused.\n\nRoot may capture each primary once, sequentially, under 300 seconds and 3 GiB process-tree RSS (expected 22/18/17 PASS groups). No primary was executed by this review. Final source/output/cache confirmation remains pending in this session.\n')
print(json.dumps({'report':str(p),'sha256':sha(p.read_bytes()),'tree':d['source']['tree'],'original_count':len(rows),'source_count':len(d['source']['paths'])}))
