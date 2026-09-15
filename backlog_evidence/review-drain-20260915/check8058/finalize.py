from pathlib import Path
import json,hashlib,subprocess,sys,gzip
from fractions import Fraction as F
r=Path('/private/tmp/review-drain-20260915');q=r/'check8058';w=r/'author-pool/author-backlog';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip();ref=lambda p:{'path':str(p),'sha256':sha(p)}
p=json.loads((r/'review-8058-label-provisional.json').read_text());v=json.loads((r/'8058-unit-label-preexecution-v1.json').read_text());freeze=json.loads((r/'8058-author-final-freeze.json').read_text());outputs={8052:'outputs/native_zero_penalty_l4_delayed_splitting_2026_09_08.json',8053:'outputs/native_weak_electric_spectator_gap_2026_09_08.json',8058:'scripts/native_third_order_star_vertex_2026_09_08.json'}
for n,h in p['final_path_sha256'].items():
 if n not in outputs.values() and not n.startswith('logs/runner-cache/'):assert sha(w/n)==h,n
for entries in v['inputs'].values():
 for x in entries:assert sha(w/x['path'])==x['sha256'],x['path']
def science(x):
 if isinstance(x,dict):return {k:science(v) for k,v in x.items() if k not in {'seconds','elapsed_seconds','peak_rss_mib','rss_mib','rss_bytes','input_sha256','source_sha256'}}
 if isinstance(x,list):return list(map(science,x))
 return x
executions=[];source_inputs={}
for pr,note,count in zip((8052,8053,8058),v['notes'],(93564,7960,40)):
 op=outputs[pr];out=json.loads((w/op).read_text());old=json.loads((q/str(pr)/'original'/op).read_text());assert science(out)==science(old),(pr,'payload');primary=note['primary_runner'];assert out['source_sha256']==sha(w/primary)
 for n,h in out['input_sha256'].items():assert sha(w/n)==h;source_inputs[n]=h
 receipt=r/('8052-label-author-final-execution.json' if pr==8052 else f'{pr}-group-author-final-execution.json');run=json.loads(receipt.read_text());assert run['status']=='ok' and run['exit_code']==0 and not run['stderr'] and run['elapsed_sec']<180;assert json.JSONDecoder().raw_decode(run['stdout'])[0]==out;assert f'TOTAL: PASS={count} FAIL=0' in run['stdout']
 cp='logs/runner-cache/'+Path(primary).stem+'.txt';cache=(w/cp).read_text();assert run['stdout'][-200000:] in cache;finger=hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
 for n in out['input_sha256']:
  a=n.encode();b=(w/n).read_bytes();finger.update(len(a).to_bytes(8,'big'));finger.update(a);finger.update(len(b).to_bytes(8,'big'));finger.update(b)
 assert 'input_fingerprint_sha256: '+finger.hexdigest() in cache and 'runner_sha256: '+sha(w/primary) in cache
 executions.append(dict(pr=pr,receipt=ref(receipt),elapsed_sec=run['elapsed_sec'],cap_sec=180,TOTAL=f'PASS={count} FAIL=0',cache=ref(w/cp),fingerprint_sha256=finger.hexdigest(),scientific_payload_unchanged=True))
 if pr==8053:
  lo,hi=map(F,out['exact_interval']);assert F('370.7628915198')<lo<=hi<F('370.7628915199')
for group in p['constituent_dispositions'].values():
 for x in group:
  if x['final_path']:x['final_sha256']=sha(w/x['final_path'])
  if x['original_path'] in outputs.values():x['disposition']='Actual final regenerated output; full mathematical payload exactly matches the frozen original, with current source/input/runtime identities.'
paths=git('diff','--cached','--name-only').splitlines();final={}
for n in paths:assert subprocess.check_output(['git','-C',str(w),'show',':'+n])==(w/n).read_bytes();final[n]=sha(w/n)
assert all(x.startswith('A\t') for x in git('diff','--cached','--name-status').splitlines())
for args in [('diff','--check'),('diff','--cached','--check'),('diff','HEAD','--check')]:assert not git(*args)
anchors=json.loads((r/'8058-archive-anchor.json').read_text())
for a in anchors.values():
 mp=Path(a['manifest_path']);assert sha(mp)==a['manifest_sha256']
 for x in json.loads(mp.read_text())['entries']:
  b=(mp.parent/x['stored_path']).read_bytes();assert hashlib.sha256(b).hexdigest()==x['stored_sha256'];b=gzip.decompress(b) if x['encoding']=='gzip' else b;assert hashlib.sha256(b).hexdigest()==x['raw_sha256']
p['preserved_initial_8052_capture']=ref(r/'8052-group-author-final-execution.json')
p['late_label_correction']='Exact stdout label separated general cut proof from finite L4 isolation. Initial8052 successful capture retained; only8052 rerun after source-bound refreeze. Unchanged8053/8058 captures reused.'
p.update(status='Final source and actual evidence confirmed',source_verdict='FINAL VERDICT: PASS WITH BOUNDED CLAIMS',candidate=str(w),candidate_HEAD=git('rev-parse','HEAD'),staged_tree=git('write-tree'),final_path_sha256=final,source_inputs=source_inputs,input_categories=v['inputs'],executions=executions,claim_dispositions={'8052':'PASS conditional all-even-torus through-five scalarity; explicit finite L4 isolation and degeneracy, no order-six coefficient or bulk isolation','8053':'PASS complete finite L4 canonical sixth-order quadratic and exact positive interval, physical even-parity unique ground and asymptotic finite small-u gap; no explicit radius or bulk phase','8058':'PASS exact fixed-frame partial star channel/vacuum transition and nonlinear filled-source witness; no full-sixth substitution or universal dressing no-go'},dependency_scope='Actual linked dictionary/instrument/endpoint and constituent theorem sources; proof-identity pins distinguished from candidate data. Old library/runtime manifests remain historical provenance, not live dependencies. Exact current source hashes bound.',external_mathematics='Finite-dimensional CAR/Clifford algebra, graph cuts, square-root concavity, rational residual norm enclosures and isolated finite-dimensional analytic/Riesz perturbation theory were checked in the proofs. No external numerical or physical selection premise imported.',current_main_preservation='All final staged paths are additions. Current corrected parent notes and all bound source/input bytes unchanged after frozen-method replay. No historical generated audit manifest imported as authority.',remaining_findings=[])
assert not (r/'review-8058.json').exists();(r/'review-8058.json').write_text(json.dumps(p,indent=2)+'\n');body=(r/'review-8058-working.md').read_text();body=body.replace('Status: complete original proof/code reading and corrected-source cold confirmation; final verdict pending the three actual bounded executions and final bindings.','FINAL VERDICT: PASS WITH BOUNDED CLAIMS. All three actual executions, final source/input/cache bindings and exact constituent dispositions confirmed.')
(r/'review-8058.md').write_text(body+'\nThe initial8052 capture (93564/0) completed before the final label correction arrived. Its receipt is preserved; only that primary was repeated after the exact label fix and new preflight. The other two completed captures were unchanged and reused.\n\n## Final execution and identities\n\n'+ '\n'.join(f'- PR{x["pr"]}: {x["TOTAL"]}, {x["elapsed_sec"]:.6f}s under180s; unchanged mathematical payload.' for x in executions)+'\n\nFinal tree '+p['staged_tree']+'. All431 constituent paths accounted;395 original historical paths exact. Full identities: review-8058.json. No audit verdict or full pipeline.\n')
newref=ref(r/'review-8058.json');v['reviewer']['report']=newref;v['reviewer']['references'].append(ref(r/'review-8058.md'));v['source']['tree']=p['staged_tree'];v['source']['paths']=[dict(path=n,sha256=h) for n,h in final.items()]
for c in v['constituents']:c['dispositions']=dict(newref,json_pointer=c['dispositions']['json_pointer'])
for n in v['non_science_notes']:n['review_reference']=newref
out=r/'8058-unit-final-v1.json';assert not out.exists();out.write_text(json.dumps(v,indent=2)+'\n');print(p['staged_tree'])
