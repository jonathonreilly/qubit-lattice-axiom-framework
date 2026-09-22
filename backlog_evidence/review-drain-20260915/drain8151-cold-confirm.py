import pathlib,json,hashlib,gzip,subprocess,sys,ast
r=pathlib.Path('/private/tmp/review-drain-20260915');w=r/'drain-author-slot';sha=lambda b:hashlib.sha256(b).hexdigest()
def load(n):return json.loads((r/n).read_text())
def git(*a):return subprocess.check_output(['git','-C',str(w),*a])
d=load('drain8151-author-unit-draft-v1.json');h=load('drain8151-author-source-handoff-v1.json');old=load('drain8151-original-review.json');main=git('rev-parse','5418caa').decode().strip()
assert git('write-tree').decode().strip()==d['source']['tree']=='574733a3f7faaeabd237df3d1bdb607c4c64940e';assert not git('diff','--name-only')
for x in d['source']['paths']:assert sha((w/x['path']).read_bytes())==x['sha256']
for entries in d['inputs'].values():
 for x in entries:assert sha((w/x['path']).read_bytes())==x['sha256']
rows=[]
for x in old['original_dispositions']:
 a=next(a for a in h['original_dispositions']if a['original_path']==x['path']);assert sha(gzip.decompress((w/a['final_path']).read_bytes()))==x['sha256']==a['original_sha256'];assert sha((w/a['final_path']).read_bytes())==a['final_sha256'];rows.append(dict(x,**a))
assert len(rows)==22
sys.path[:0]=[str(w/'scripts'),str(w/'docs/audit/scripts')]
import runner_cache as c,build_citation_graph as g,audit_packet_script_deps as p
api=load('drain8151-author-cache-api-v1.json');runner=w/api['primary'];p.SCRIPTS_DIR=w/'scripts'
assert c.declared_timeout_for(runner)==180;assert list(c.declared_input_paths(runner))==api['declared_inputs'];assert c.declared_input_fingerprint(runner)==api['declared_input_fingerprint'];assert not g.resolve_helper_runner_paths(str(runner));assert not p.transitive_helpers(runner.stem)
checks=[n for n in ast.walk(ast.parse(runner.read_text()))if isinstance(n,ast.Call)and isinstance(n.func,ast.Attribute)and n.func.attr=='check'];assert len(checks)==20
for name in api['declared_inputs'][1:]:assert git('show',main+':'+name)==(w/name).read_bytes()
changes=git('diff','--name-status',d['source']['base'],main).decode().splitlines();assert not {x['path']for x in d['source']['paths']}.intersection(x.split('\t')[-1] for x in changes)
assert all(s.startswith('A\t')for s in git('diff','--cached','--name-status').decode().splitlines())
for args in [('diff','--check'),('diff','--cached','--check'),('diff','HEAD','--check')]:git(*args)
refs=[]
for n in ['drain8151-original-review.json','check8151/controls.py','check8151/controls.json','drain8151-author-unit-draft-v1.json','drain8151-author-source-handoff-v1.json','drain8151-author-cache-api-v1.json','drain8151-author-cheap-v1.json']:
 refs.append(dict(path=str(r/n),sha256=sha((r/n).read_bytes())))
o=dict(status='COLD SOURCE PASS FOR POSITIVE IDENTITIES AND EXPLICIT CONDITIONAL IMPLICATIONS; CAPTURE PENDING',reviewer='/root/review_8011',source=d['source'],inputs=d['inputs'],original_dispositions=rows,claim_dispositions=h['claim_dispositions'],actual_api=api,expected_pass_groups=20,resolution='Full revised note and runner delta read. T2 explicitly real; T4 nontrivial p>=m counting and trivial p<m separated. T3 finite inequalities only and exact parity gap stated. T5 requires uniform planar bad-bond estimate for every contour set across tori; no equality epsilon=6m/p asserted. T6 conditional long-distance correlation lower bound passes to torus limits and contradicts unique symmetric tail-trivial state; translated local support is correctly outside conditioning box. T7 uses same explicit unproved planar bound. False orbit/state inference removed. Conditional implications do not constitute a phase verdict or completed negative certificate.',arithmetic='Primary computations and predicates unchanged; only metadata, scope labels and source fences changed. Twenty check calls; root message19 is a planning typo, not source error. Prior independent geometry/group/algebra controls reused.',current_main={'commit':main,'parent_input_bytes_unchanged':True,'changed_paths':changes,'assessment':'New8023 gauge sources are separate supplied-model work; neither static spin event geometry nor any declared premise changes. Proposed26 additions overwrite no current main source. No new scientific dependency imported.'},capture={'owner':'root','count':1,'timeout_seconds':180,'sampled_process_tree_rss_bytes':3221225472,'expected_pass':20,'expected_fail':0,'preserve_attempt':True},scope='Partial positive salvage. Unconditional phase/threshold216 and orbit claims not accepted; preserve original branch and complete proof. No audit verdict. Final execution/cache source binding remains with same reviewer.',references=refs)
f=r/'drain8151-preexecution-review.json';assert not f.exists();f.write_text(json.dumps(o,indent=2)+'\n');(r/'drain8151-preexecution-review.md').write_text('# PR8151 cold confirmation\n\nPASS for positive identities and explicitly conditional contour/limit implications at tree `'+d['source']['tree']+'`. All22 originals verified, all source/input bytes frozen, current-main parent bytes unchanged. Unconditional phase claims and negative certification remain deferred.\n\nRoot may capture once under180seconds/3GiB sampled process-tree RSS. Expected20/0 (not19). Final execution/cache confirmation remains pending.\n');print(sha(f.read_bytes()))
