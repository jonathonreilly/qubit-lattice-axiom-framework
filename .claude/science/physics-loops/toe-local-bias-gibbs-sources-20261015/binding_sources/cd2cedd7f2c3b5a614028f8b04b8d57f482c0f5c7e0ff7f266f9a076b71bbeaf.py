from pathlib import Path
import ast,datetime,difflib,hashlib,json,re,shutil,sys
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261014_214309');O=N/'local_bias_integration_proposal';D=N/'publication_integration/local_bias';S=D/'canonical_source';OLD=N/'local_bias_publication_draft/proposal';P='.claude/science/physics-loops/toe-local-bias-gibbs-sources-20261015';H='scripts/local_conditional_bias_and_rotated_gibbs_2026_10_15.py'
def pin(p):
 p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def read(p):return json.loads(Path(p).read_text())
def write(p,v):Path(p).write_text(json.dumps(v,indent=2)+'\n')
assert datetime.datetime.now(datetime.timezone.utc)<datetime.datetime(2026,10,15,21,43,9,tzinfo=datetime.timezone.utc)
R=D/'recovery_offset_repair';R.mkdir(exist_ok=False)
before=read(D/'PREPARED.json')
for rel,row in before['canonical_files'].items():assert pin(S/rel)['sha256']==row['sha256']
for name in ('PREPARED.json','CANONICALIZATION.diff'):shutil.copyfile(D/name,R/name)
selection=read(S/P/'RECOVERY_SELECTION.json');mapping={r['name']:r for r in read(S/P/'BODY_MAP.json')['bodies']};count=0
for row in selection['members']:
 loc=row.get('recovery') or {}
 if loc.get('kind')=='body_interval':
  bound=mapping[loc['body_name']];assert row['sha256']==bound['sha256'] and row['bytes']==bound['bytes']
  for key in ('container','start_byte_inclusive','end_byte_exclusive'):loc[key]=bound[key]
  count+=1
assert count==15;write(S/P/'RECOVERY_SELECTION.json',selection)
path=S/H;text=path.read_text();needle='    state=read_json(PACKET+"/PUBLICATION_STATE.json")\n'
check='''    selection=read_json(PACKET+"/RECOVERY_SELECTION.json")
    for member in selection["members"]:
        recovery=member.get("recovery")
        if recovery is not None:
            require(any(member["bytes"]==row["bytes"] and member["sha256"]==row["sha256"] and recovery==row["recovery"] for row in sources),"Recovery selection linkage")
'''
assert text.count(needle)==1;path.write_text(text.replace(needle,check+needle));ast.parse(path.read_bytes())
evidence={}
paths=[Path(__file__),D/'ROOT_INTEGRATION_SOURCE_REVIEW.json']
for label in ('local_bias_integration_review_1855','local_bias_integration_review_1855_recovery','local_bias_integration_review_1855_final'):
 paths.extend(p for p in (N/'runs'/label).iterdir() if p.is_file())
for p in paths:
 row=pin(p);rel=P+'/binding_sources/'+row['sha256']+(p.suffix or '.blob');q=S/rel
 if q.exists():assert q.read_bytes()==p.read_bytes()
 else:q.write_bytes(p.read_bytes())
 evidence[str(p)]={**row,'path':rel}
write(S/P/'CANONICAL_RECOVERY.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Root found RECOVERY_SELECTION retained fifteen original note offsets after wrapper relocation. Relocate those exact body rows and add a semantic source-manifest linkage check. Frozen proposal, all scientific bodies, historical nulls and mathematical parent unchanged. Initial root preflight detected this omission; second preflight hit null recovery metadata; both failed receipts and original helper sources retained. Third preflight accepted only prepare plus mandatory repair.','relocated_rows':count,'original_prepared':pin(R/'PREPARED.json'),'original_diff':pin(R/'CANONICALIZATION.diff'),'evidence':evidence,'science_runs':0,'planned_check':'Actual baseline and a repinned stale-offset mutation before publication.'})
manifest=S/P/'INPUT_MANIFEST.json';value=read(manifest);known={r['path'] for r in value['inputs']}
for p in sorted(S.rglob('*')):
 if not p.is_file():continue
 rel=str(p.relative_to(S))
 if rel not in known and rel not in (H,P+'/INPUT_MANIFEST.json'):value['inputs'].append({**pin(p),'path':rel})
for row in value['inputs']:
 p=S/row['path']
 if p.exists():row.update({k:pin(p)[k] for k in ('bytes','sha256')})
write(manifest,value)
text=path.read_text();text,n=re.subn(r'^AUDIT_INPUT_PATHS\s*=.*$','AUDIT_INPUT_PATHS = '+repr(tuple(sorted({r['path'] for r in value['inputs']}|{P+'/INPUT_MANIFEST.json'}))),text,flags=re.M);assert n==1
text,n=re.subn(r'^MANIFEST_SHA256\s*=.*$','MANIFEST_SHA256 = '+repr(pin(manifest)['sha256']),text,flags=re.M);assert n==1;path.write_text(text);ast.parse(text)
changed=[str(p.relative_to(S)) for p in sorted(S.rglob('*')) if p.is_file() and (not (OLD/p.relative_to(S)).exists() or p.read_bytes()!=(OLD/p.relative_to(S)).read_bytes())]
delta=''
for rel in changed:
 old=OLD/rel;prior=old.read_text().splitlines(True) if old.exists() else []
 delta+=''.join(difflib.unified_diff(prior,(S/rel).read_text().splitlines(True),fromfile='draft/'+rel,tofile='canonical/'+rel))
(D/'CANONICALIZATION.diff').write_text(delta)
before['canonical_files']={str(p.relative_to(S)):pin(p) for p in sorted(S.rglob('*')) if p.is_file()};before['diff']=pin(D/'CANONICALIZATION.diff');before['root_recovery']=pin(S/P/'CANONICAL_RECOVERY.json');before['utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();write(D/'PREPARED.json',before)
print(json.dumps({'prepared':pin(D/'PREPARED.json'),'diff':pin(D/'CANONICALIZATION.diff'),'recovery':pin(S/P/'CANONICAL_RECOVERY.json'),'relocated_rows':count}))
