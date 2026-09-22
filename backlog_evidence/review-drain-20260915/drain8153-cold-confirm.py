import pathlib,json,hashlib,gzip,subprocess,sys
r=pathlib.Path('/private/tmp/review-drain-20260915');w=r/'drain-author-slot';sha=lambda b:hashlib.sha256(b).hexdigest();load=lambda n:json.loads((r/n).read_text())
d=load('drain8153-author-unit-draft-v1.json');h=load('drain8153-author-source-handoff-v1.json');orig=load('drain8153-original-review.json');latest='19b73e32772a990f4d9d0792013347943bc80818'
def git(*a):return subprocess.check_output(['git','-C',str(w),*a])
assert git('write-tree').decode().strip()==d['source']['tree']=='047bbca99bc5025c0c7cf932471178beca032911'
assert not git('diff','--name-only');assert len(h['original_dispositions'])==22
for x in d['source']['paths']:
 b=(w/x['path']).read_bytes();assert sha(b)==x['sha256'];assert git('show',':'+x['path'])==b
for group,rows in d['inputs'].items():
 for x in rows: assert sha((w/x['path']).read_bytes())==x['sha256']
original={x['path']:x for x in orig['original_dispositions']}
for x in h['original_dispositions']:
 assert sha(gzip.decompress((w/x['final_path']).read_bytes()))==x['original_sha256']==original[x['original_path']]['sha256']
changes=git('diff','--cached','--name-status').decode().splitlines();assert all(x.startswith('A\t')for x in changes)
current=[]
for x in orig['context']+d['inputs']['parents']:
 b=git('show',latest+':'+x['path']);assert b==(w/x['path']).read_bytes();current.append(dict(path=x['path'],sha256=sha(b)))
for x in d['source']['paths']:
 exists=subprocess.run(['git','-C',str(w),'cat-file','-e',latest+':'+x['path']],capture_output=True).returncode==0
 assert not exists
sys.path[:0]=[str(w/'scripts'),str(w/'docs/audit/scripts')]
import runner_cache as c,build_citation_graph as g,audit_packet_script_deps as p
runner=w/d['inputs']['runtime'][0]['path'];note=w/d['source']['paths'][0]['path'];p.SCRIPTS_DIR=w/'scripts'
api=dict(type=g.extract_claim_type_hint(note.read_text()),timeout=c.declared_timeout_for(runner),runtime_scientific_inputs=[dict(path=x,sha256=sha((w/x).read_bytes()))for x in c.declared_input_paths(runner)],graph_helpers=list(g.resolve_helper_runner_paths(str(runner))),packet_helpers=sorted(p.transitive_helpers(runner.stem)))
assert api['timeout']==180 and not api['graph_helpers'] and not api['packet_helpers']
refs=[dict(path=str(r/x),sha256=sha((r/x).read_bytes()))for x in ['drain8153-original-review.json','drain8153-author-unit-draft-v1.json','drain8153-author-source-handoff-v1.json','drain8153-author-cache-api-v1.json','check8153/controls.py','check8153/controls.json','check8153/control-attempt1.json']]
o=dict(status='COLD SOURCE PASS — POSITIVE BOUNDED MATHEMATICS; EXECUTION PENDING',reviewer='/root/review_8011',source=d['source'],inputs=d['inputs'],actual_api=api,original_dispositions=h['original_dispositions'],original_identity=dict(head=orig['head'],delta_base=orig['delta_base']),affected_confirmation='Complete revised note and complete runner correction diff read. All six material findings resolved: real reflection form; explicit Gaussian-domination import with ordered NN normalization; self-inverse Fourier proof; shell control of singular Riemann sum; all-N liminf proof; zero-field component scope and withdrawal of comparative physical/negative classifications. Runner arithmetic unchanged; evidence labels/fences/input path and180sec cap changed. No source self-certification.',mathematical_import=orig['external_methods'],independent_controls_reused=orig['independent_controls'],current_main=dict(revision=latest,identical_authorities_and_parents=current,preservation='26 additions only, no proposed source path exists on latestmain; all existing sources untouched. Newly landed8151 conditional phase and8152 finite conditional representation results are not mathematical premises for this self-contained defined-model proof; no original universal conclusion imported.'),allowed_capture=dict(count_expected=17,timeout_seconds=180,process_tree_rss_limit_bytes=1073741824,concurrency=1,scope='Single root-owned primary capture after matching cheap receipt; no rerun independent controls.'),deferred='No negative certificate, selected extremal transverse state, real-space decay or physical candidate selection. Complete original branch remains preserved for unlanded claims.',final_pending='Fresh cache/output and unchanged input confirmation in this original reviewer session.',references=refs)
out=r/'drain8153-preexecution-review.json';assert not out.exists();out.write_text(json.dumps(o,indent=2)+'\n');print(sha(out.read_bytes()))
