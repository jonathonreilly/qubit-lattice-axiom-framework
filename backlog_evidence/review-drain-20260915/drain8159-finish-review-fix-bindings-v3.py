from pathlib import Path
import json,hashlib
b=Path(__file__).resolve().parent;w=b/'review-draft-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p));dp=b/'drain8159-author-canonical-draft-v2.json';d=json.loads(dp.read_text());plan=json.loads((b/'drain8159-author-ownership-plan-v2.json').read_text())
scan=json.loads((b/'drain8159-formula-rewrite-scan-v1.json').read_text());add=json.loads((b/'drain8159-early-affected-review-v1-scope-addendum.json').read_text());changed={x['owner'] for x in scan}|{'scripts/'+s for s in add['replacement_scope']}
for e in d['files']:
 if e['path'] not in changed:assert sha(w/e['path'])==e['sha256'],e['path']
proof=b/'drain8159-author-full-proof-map-v3.json'
for x in json.loads(proof.read_text()):assert sha(w/x['canonical_owner'])==x['canonical_owner_sha256']
deps={plan['owners'][key]['canonical_note']:values for key,values in d['dependencies'].items()};assert len(deps)==25
api=json.loads((b/'drain8159-author-input-discovery-v2.json').read_text())
for x in api['programs']:
 x['closure_scope']='Actual direct and transitive helper file reads; not the complete mathematical premise closure.'
 for e in x['runtime_closure']:e['sha256']=sha(w/e['path'])
math=[]
for p in d['notes']:
 seen=set();pending=list(deps[p])
 while pending:
  q=pending.pop()
  if q in seen:continue
  seen.add(q);pending.extend(deps.get(q,[]))
 assert p not in seen,('cycle',p)
 math.append({'owner':p,'scope':'Transitive internal owner dependencies and their reviewed external canonical parent endpoints; no invented runtime reads.','parents':[{'path':q,'sha256':sha(w/q)} for q in sorted(seen)]})
api['mathematical_premise_closure']=math;api['status']='Separate actual I/O and mathematical premise bindings; nine prior category differences explained, no missing actual runtime read found.'
apip=b/'drain8159-author-input-discovery-v3.json';assert not apip.exists();apip.write_text(json.dumps(api,indent=2)+'\n')
for e in d['files']:e['sha256']=sha(w/e['path'])
for x in d['runtime_plan']:x['canonical_sha256']=sha(w/x['runner'])
d['status']='AUTHOR REVIEW FIXES V3; SAME-SESSION AFFECTED CONFIRMATION PENDING';d['predecessor']=ref(dp);d['resource_plan']='drain8159-author-resource-plan-v3.json';d['dependencies_by_note']=deps
new=b/'drain8159-author-canonical-draft-v3.json';assert not new.exists();new.write_text(json.dumps(d,indent=2)+'\n')
receipt=b/'drain8159-review-fixes-v3.json';assert not receipt.exists();receipt.write_text(json.dumps({'changed_paths':[{'path':p,'sha256':sha(w/p)} for p in sorted(changed)],'draft':ref(new),'patch':ref(b/'drain8159-review-fixes-v3.patch'),'full_proofs':ref(proof),'resource_plan':ref(b/'drain8159-author-resource-plan-v3.json'),'input_discovery':ref(apip),'supersedes':'v2 blanket mathematical preservation assertion was false for six expressions; previous reports and exact affected source copies retained. No primary executed.','binding_script_failure':'Initial fix script restored source and verified all72 bodies, then KeyError because dependencies was indexed by owner number rather than note path. This continuation only completes metadata with explicit numeric-owner mapping; no source change/re-execution. Initial script preserved unchanged.','negative_claim_boundary':'No scientific scope change. Six exact original formulas restored and two companion reporting/cost scopes corrected.','executions':0,'scripts':[ref(b/'drain8159-fix-review-findings-v3.py'),ref(Path(__file__))]},indent=2)+'\n');print(ref(receipt));print(ref(new));print('changed',len(changed),'proofs',len(json.loads(proof.read_text())))
