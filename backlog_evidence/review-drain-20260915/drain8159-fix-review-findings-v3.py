from pathlib import Path
import json,hashlib,difflib,re,ast,subprocess
b=Path(__file__).resolve().parent;w=b/'review-draft-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p));dp=b/'drain8159-author-canonical-draft-v2.json';d=json.loads(dp.read_text())
assert not subprocess.check_output(['git','-C',str(w),'diff','--name-only','HEAD'])
for e in d['files']:assert sha(w/e['path'])==e['sha256'],e['path']
scan=json.loads((b/'drain8159-formula-rewrite-scan-v1.json').read_text());assert len(scan)==6
updates={};changes=[]
for x in scan:
 p=x['owner'];old=updates.get(p,(w/p).read_text());m=re.fullmatch(r'\[([^\]]+)\]\(([^)]+)\)',x['matched']);assert m
 broken=m[1]+' (`'+m[2]+'`)';assert old.count(broken)==1,(p,broken);updates[p]=old.replace(broken,x['matched'],1);changes.append({'path':p,'before':broken,'restored':x['matched'],'original':x['original']})
add=json.loads((b/'drain8159-early-affected-review-v1-scope-addendum.json').read_text())
for stem,sc in add['replacement_scope'].items():
 p='scripts/'+stem;s=(w/p).read_text()
 for label in ['per_element','per_site','per_mode','per_block','lattice_wide']:
  pattern=r"^    print\('"+label+r": [^\n]*\)$";assert len(re.findall(pattern,s,re.M))==1,(p,label);s=re.sub(pattern,lambda m:'    print('+repr(label+': '+sc[label])+')',s,flags=re.M)
 ast.parse(s);updates[p]=s
patch=[];originals=b/'drain8159-review-fix-originals-v2';assert not originals.exists();originals.mkdir()
for p,s in updates.items():
 old=(w/p).read_text();(originals/Path(p).name).write_text(old);(w/p).write_text(s);patch.extend(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile=p+' v2',tofile=p+' v3'))
pf=b/'drain8159-review-fixes-v3.patch';assert not pf.exists();pf.write_text(''.join(patch))
# Full body comparison against raw original text, retaining mathematical bracket syntax.
proofrows=[]
for x in d['proof_mapping']+[{'original':'EXTRA_BLOCK27','canonical_owner':next(p for p in d['notes'] if 'FOREST' in p),'original_sha256':'7a0a953deb6b02a4b4c2f78a941013d30a61ad61ef6e5c0c278489c149c1c647'}]:
 raw=(b/'drain8159-block27-original-proof.md').read_text() if x['original']=='EXTRA_BLOCK27' else (b/'drain8159-originals'/x['original']).read_text();assert hashlib.sha256(raw.encode()).hexdigest()==x['original_sha256']
 def actual_target(m):
  target=m[2].split('#',1)[0]
  return m[1]+' (`'+m[2]+'`)' if re.search(r'\.(?:md|py|json|txt|log|yaml|yml|csv|pdf|gz)$',target) else m[0]
 expected=re.sub(r'\[([^\]]+)\]\((?!https?://)([^)]+)\)',actual_target,raw);expected=re.sub(r'^(#{1,6}) ',lambda m:'#'*min(6,len(m[1])+2)+' ',expected,flags=re.M)
 owner=(w/x['canonical_owner']).read_text();assert owner.count(expected)==1,x['original'];proofrows.append(dict(x,verified_complete_body_sha256=hashlib.sha256(expected.encode()).hexdigest(),canonical_owner_sha256=sha(w/x['canonical_owner'])))
proof=b/'drain8159-author-full-proof-map-v3.json';proof.write_text(json.dumps(proofrows,indent=2)+'\n')
cost=json.loads((b/'drain8159-author-resource-plan-v2.json').read_text())
for x in cost:
 if Path(x['runner']).name in add['replacement_scope']:x['basis']=add['replacement_scope'][Path(x['runner']).name]['cost'];x['corrected_family_label']=True
costp=b/'drain8159-author-resource-plan-v3.json';costp.write_text(json.dumps(cost,indent=2)+'\n')
api=json.loads((b/'drain8159-author-input-discovery-v2.json').read_text())
for x in api['programs']:
 x['closure_scope']='Actual direct and transitive helper file reads; not a complete mathematical premise closure.'
 for e in x['runtime_closure']:e['sha256']=sha(w/e['path'])
math=[]
for p in d['notes']:
 seen=set();pending=list(d['dependencies'][p])
 while pending:
  q=pending.pop()
  if q in seen:continue
  seen.add(q);pending.extend(d['dependencies'].get(q,[]))
 math.append({'owner':p,'scope':'Transitive internal owner dependencies and their reviewed external canonical parent endpoints; no invented runtime reads.','parents':[{'path':q,'sha256':sha(w/q)} for q in sorted(seen)]})
api['mathematical_premise_closure']=math;api['status']='Corrected separate actual I/O and mathematical premise bindings; nine previously noted category differences explained, no missing runtime read found.'
apip=b/'drain8159-author-input-discovery-v3.json';apip.write_text(json.dumps(api,indent=2)+'\n')
for e in d['files']:e['sha256']=sha(w/e['path'])
for x in d['runtime_plan']:x['canonical_sha256']=sha(w/x['runner'])
d['status']='AUTHOR REVIEW FIXES V3; SAME-SESSION AFFECTED CONFIRMATION PENDING';d['predecessor']=ref(dp);d['resource_plan']=costp.name
new=b/'drain8159-author-canonical-draft-v3.json';assert not new.exists();new.write_text(json.dumps(d,indent=2)+'\n')
receipt=b/'drain8159-review-fixes-v3.json';receipt.write_text(json.dumps({'source_changes':changes,'changed_paths':[{'path':p,'sha256':sha(w/p)} for p in updates],'draft':ref(new),'patch':ref(pf),'full_proofs':ref(proof),'resource_plan':ref(costp),'input_discovery':ref(apip),'supersedes':'v2 blanket mathematical preservation assertion was false for six expressions; preserved prior files/reports show the defect. No primary was executed on that draft.','negative_claim_boundary':'No scientific scope changes, restored exact original formulas only; same-scope labels corrected for two evidence companions.','executions':0},indent=2)+'\n');print(ref(receipt));print(ref(new));print('changed',len(updates),'proofs',len(proofrows))
