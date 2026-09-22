import pathlib,json,hashlib,gzip,subprocess
R=pathlib.Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot'; sha=lambda b:hashlib.sha256(b).hexdigest()
x=json.load(open(R/'drain8023-author-unit-draft-v1.json'));h=json.load(open(R/'drain8023-author-source-handoff-v1.json')); o=json.load(open(R/'drain8023-original-review.json'))
assert subprocess.check_output(['git','write-tree'],cwd=W,text=True).strip()==x['source']['tree']
for a in x['source']['paths']:
 assert sha((W/a['path']).read_bytes())==a['sha256'];assert sha(subprocess.check_output(['git','show',':'+a['path']],cwd=W))==a['sha256']
for cat, rows in x['inputs'].items():
 for a in rows:assert sha((W/a['path']).read_bytes())==a['sha256']
orig={a['original_path']:a for a in o['original_dispositions']}; mapped=[]
for a in h['original_dispositions']:
 assert a['original_sha256']==orig[a['original_path']]['original_sha256']
 b=(W/a['final_path']).read_bytes();assert sha(b)==a['final_sha256'];assert sha(gzip.decompress(b))==a['original_sha256']
 z=dict(orig[a['original_path']]);z.update(final_path=a['final_path'],final_sha256=a['final_sha256']);z['disposition']+=' Exact original recovered in verified gzip, including inherited/audit/process material solely as history.';mapped.append(z)
assert len(mapped)==407
existing=subprocess.check_output(['git','diff','--cached','--name-status'],cwd=W,text=True).splitlines();assert all(a.startswith('A\t') for a in existing)
changed_context=[]
for p,s in o['source_input_context_hashes'].items():
 if (W/p).is_file() and sha((W/p).read_bytes())!=s:changed_context.append(p)
assert not changed_context,changed_context
out=dict(status='COLD SOURCE CONFIRMED WITH BOUNDED CLAIMS; CAPTURE PENDING',reviewer='/root/review_8012',base=x['source']['base'],tree=x['source']['tree'],original_dispositions=mapped,source_hashes={a['path']:a['sha256'] for a in x['source']['paths']},inputs=x['inputs'],archive_occurrences_verified=407,archive_unique_objects=384,current_main_preservation='All390 staged paths are additions; no preexisting file changed. All previously bound authority/premise/tool context hashes equal reviewer snapshot.',affected_review='Full four-file original-to-corrected diff read. Added proof identity inputs/canonical cache links/footer and removed live historical execution prose. Computation/proof unchanged.',no_go_scope='No N1 packet PASS; valid finite approximation, quantitative spectral count/enclosure and explicit adverse witnesses do not establish broader compiler or physical-route exclusions. All historical claims retained without authority adoption.',references={n:sha((R/n).read_bytes()) for n in ['drain8023-original-review.json','drain8023-author-unit-draft-v1.json','drain8023-author-source-handoff-v1.json','drain8023-author-cache-api-v1.json']},capture_permission='After root-owned actual cheap preflight PASS, root may perform exactly one capture per primary under180s/180MiB. Preserve failures; no inherited rerun. Final evidence confirmation pending.')
p=R/'drain8023-cold-confirmation-v1.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(str(p),sha(p.read_bytes()))
