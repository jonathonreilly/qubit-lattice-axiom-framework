"""Seal external referenced evidence, verifying canonical and historical source identities."""
from pathlib import Path
import json,hashlib,sys
R=Path(__file__).resolve().parent
label=sys.argv[1];p=R/(label+'-collected-units.json');d=json.loads(p.read_text());assert len(d['units'])==1
u=d['units'][0];assert u['prs'] and not u.get('procedural_only');inputs=u['inputs'];reports=dict(u['review_evidence_hashes'])
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
recovery=R/'review-loop-efficiency-local-before-recovery-v1.json';old=json.loads(recovery.read_text());oldmap={x['original_path']:x for x in old['files']}
reports[recovery.name]=sha(recovery)
for x in old['files']:
 q=Path(x['path']);assert sha(q)==x['sha256'];reports[q.relative_to(R).as_posix()]=x['sha256']
processed=set();canonical=[]
def walk(x):
 if isinstance(x,dict):
  if isinstance(x.get('path'),str) and isinstance(x.get('sha256'),str) and Path(x['path']).is_absolute():
   q=Path(x['path']);h=x['sha256']
   if str(q) in oldmap:
    recovered=oldmap[str(q)];assert recovered['sha256']==h or (inputs.get('docs/ai_methodology/skills/review-loop/'+q.relative_to(Path('/Users/jonBridger/.codex/skills/review-loop')).as_posix())==h and sha(q)==h)
   elif any(q.is_relative_to(R/slot) for slot in ['review-meta-slot','author-draft-slot','drain-author-slot','review-draft-slot','integration-resume','review-next-slot']):
    slot=next(slot for slot in ['review-meta-slot','author-draft-slot','drain-author-slot','review-draft-slot','integration-resume','review-next-slot'] if q.is_relative_to(R/slot));rel=q.relative_to(R/slot).as_posix();assert inputs.get(rel)==h,(rel,'unbound canonical source reference');assert sha(q)==h;canonical.append(rel)
   else:
    assert q.is_relative_to(R),('external recovery needed',str(q));assert sha(q)==h,(str(q),'evidence drift');name=q.relative_to(R).as_posix();assert name not in reports or reports[name]==h;reports[name]=h
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
while set(reports)-processed:
 for name in list(set(reports)-processed):
  q=R/name;assert sha(q)==reports[name],name;processed.add(name)
  if q.suffix=='.json':walk(json.loads(q.read_text()))
inv=R/sys.argv[2];d['inventory_file']=inv.name;d['inventory_sha256']=sha(inv);u['review_evidence_hashes']=reports;u['reports']=list(reports)
original=R/(label+'-enrolled-units.json');assert not original.exists();original.write_bytes(p.read_bytes());p.write_text(json.dumps(d,indent=2)+'\n')
receipt=R/(label+'-seal.json');assert not receipt.exists();receipt.write_text(json.dumps({'collection':p.name,'sha256':sha(p),'evidence_files':len(reports),'verified_canonical_references':sorted(set(canonical)),'historical_local_recovery':{'path':str(recovery),'sha256':sha(recovery)}},indent=2)+'\n');print('SEALED',len(reports))
