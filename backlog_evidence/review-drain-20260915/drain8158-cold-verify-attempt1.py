import json,pathlib,hashlib,gzip,subprocess,sys
r=pathlib.Path('/private/tmp/review-drain-20260915');w=r/'drain-author-slot';sha=lambda b:hashlib.sha256(b).hexdigest();load=lambda n:json.loads((r/n).read_text());git=lambda *a:subprocess.check_output(['git','-C',str(w),*a])
d=load('drain8158-author-unit-draft-v1.json');h=load('drain8158-author-source-handoff-v1.json');old=load('drain8158-original-review.json');inv=load('drain8158-original-inventory.json')[0]
assert git('write-tree').decode().strip()==d['source']['tree'];assert git('rev-parse','HEAD').decode().strip()==d['source']['base']
for row in d['source']['paths']:
 b=(w/row['path']).read_bytes();assert sha(b)==row['sha256'];assert git('show',':'+row['path'])==b
for group,rows in d['inputs'].items():
 for row in rows:assert sha((w/row['path']).read_bytes())==row['sha256'],row
assert set(git('diff','--cached','--name-only').decode().splitlines())=={x['path']for x in d['source']['paths']}
for row in inv['original_paths']:
 p=w/'docs/work_history/review_loop/pr8158/objects'/(row['sha256']+'.gz');assert sha(gzip.decompress(p.read_bytes()))==row['sha256']
assert len(h['original_dispositions'])==22
for x in old['current_main_collisions']:assert sha((w/x['path']).read_bytes())==x['current_sha256'],x
sys.path[:0]=[str(w/'scripts'),str(w/'docs/audit/scripts')]
import runner_cache as c,build_citation_graph as g,audit_packet_script_deps as a
n=d['notes'][0];p=w/n['primary_runner'];assert c.declared_timeout_for(p)==180;assert g.extract_claim_type_hint((w/n['path']).read_text())[1]=='bounded_theorem';assert not g.resolve_helper_runner_paths(str(p));assert not a.transitive_helpers(p.stem)
for args in [('diff','--check'),('diff','--cached','--check'),('diff',d['source']['base'],'--check')]:subprocess.run(['git','-C',str(w),*args],check=True)
out={'status':'COLD SOURCE PASS WITH BOUNDED POSITIVE CLAIMS; CAPTURE AND FINAL EVIDENCE CONFIRMATION PENDING','reviewer':'/root/review_8011','source':d['source'],'inputs':d['inputs'],'original_dispositions':h['original_dispositions'],'original_claim_dispositions':old['claim_dispositions'],'affected_confirmation':'Full narrowed note and runner diff read. F1-F5 reconciled: positive factorization, at-most-one attachment sufficiency, scoped spectral/path factors and finite witnesses; abstract triangle diagnostic labeled; general topology converse and all-axiom-model certification deferred. Uniform linear averaging only. All22 archived originals decoded SHA verified; existing11 main collision bytes preserved.','current_context':'Actual parents and six authorities unchanged from original review. Updated tooling bindings verified at current49777 base; actual helper APIs both empty and Type bounded_theorem. No new scientific dependence on subsequently landed gauge packets.','runtime_scientific_inputs':[{'path':x,'sha256':sha((w/x).read_bytes())}for x in c.declared_input_paths(p)],'input_fingerprint':c.declared_input_fingerprint(p),'permitted_capture':{'count':1,'timeout_seconds':180,'sampled_process_tree_rss_limit_bytes':1073741824,'expected_checks':20,'owner':'root'},'branch_preservation':'Preserve original branch for deferred universal/physical claims. No negative certificate or audit verdict granted.','independent_controls':'Original20/0 controls reused unchanged; no primary or mutation executed in this confirmation.','references':[{'path':str(r/f),'sha256':sha((r/f).read_bytes())}for f in ['drain8158-author-unit-draft-v1.json','drain8158-author-source-handoff-v1.json','drain8158-author-cache-api-v1.json','drain8158-original-review.json','check8158/controls.py','check8158/controls.json']]}
f=r/'drain8158-cold-confirmation-v1.json';f.open('x').write(json.dumps(out,indent=2)+'\n');print(sha(f.read_bytes()))
