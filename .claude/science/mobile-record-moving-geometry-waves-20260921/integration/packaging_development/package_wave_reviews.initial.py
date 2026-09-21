from pathlib import Path
import hashlib,json,shutil,zipfile

R=Path('/Users/jonreilly/Documents/Codex/mobile-record-wave-publication-20260921')
P=Path('/Users/jonreilly/Documents/Codex/mobile-record-all-stage-publication-20260921')
A=Path('/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920/.claude/science/mobile-record-formation-20260920/campaign12h_second')
E=R/'.claude/science/mobile-record-moving-geometry-waves-20260921'
EXPECTED={
 'dimer_routed_transport_independent':('c1b5de01666b73c5300dec08338d3c8a524922a2c71fd9073b1c2441d607b31f','c27fc4e70c4761b554474c3ebcfbfacd700f60bf830c5f508c61bcd1f08c0ae2'),
 'dimer_routed_preparation_independent':('b84a18b6c3f3f5dbd738c80faa2667cd719490d70b9c4ee038b3851e2c521d2e','4935850f9abb022390e789a1a06c068b53067926790ebd64fe23ee009b09cc60'),
 'dimer_routed_moving_geometry_independent':('9b71bc822000865f2c4c7dbc927b3a8909cef51df61cdb7d73c13db4a09a055f','33b64b45806608385c28bbc14548c0dca647eca46e5b9e2adfd14cb36aeacdf7'),
 'dimer_routed_diffusive_gap_independent':('79350876fd7ae23580fe4ee9de82c4a559ceba61830a4afa259d018a4b1a25e9','ddde213c0b33f2f1e6ece1bba622335955c87d3efdea9c8138048e61c66552c2'),
}
ALIASES={
 '5fd0f707110dba04fbebb01a64d3fc1925fca6358c6245cc57f7dfe6e691f479':A/'dimer_routed_f1_fix/DIMER_ROUTED_RECORD_TRANSPORT.before.md',
 'd7e0ed4f6dfc8ef8e5ccd6c9382643a2df5013ba4cb9c73f47bcb23b40dbade3':A/'dimer_routed_moving_geometry_f1_fix/DIMER_ROUTED_MOVING_GEOMETRY_EXTENSION.before.md',
}
sha=lambda data:hashlib.sha256(data).hexdigest()
def rows(obj):
 if isinstance(obj,dict):
  if isinstance(obj.get('path'),str) and isinstance(obj.get('sha256'),str):yield obj
  for value in obj.values():yield from rows(value)
 elif isinstance(obj,list):
  for value in obj:yield from rows(value)
def resolve(row,folder):
 p=Path(row['path']);p=p if p.is_absolute() else folder/p
 if not p.is_file() or sha(p.read_bytes())!=row['sha256']:
  p=ALIASES[row['sha256']]
 data=p.read_bytes();assert sha(data)==row['sha256'],str(p)
 if 'bytes' in row:assert len(data)==row['bytes'],str(p)
 assert p.suffix.lower() not in ('.pdf','.ps','.pyc','.csv','.npz','.state','.bin')
 assert len(data)<10_000_000
 return p,data

capsules=[]
for name,(report_sha,seal_sha) in EXPECTED.items():
 folder=A/name
 assert sha((folder/'REPORT.md').read_bytes())==report_sha
 assert sha((folder/'FINAL_SEAL.json').read_bytes())==seal_sha
 contents={};bindings={};manifests=[];pending=[];processed=set()
 for p in sorted(folder.rglob('*')):
  if not p.is_file() or '__pycache__' in p.parts:continue
  assert p.suffix.lower() not in ('.pdf','.ps','.pyc','.csv','.npz','.state','.bin')
  member='review/'+str(p.relative_to(folder));contents[member]=p.read_bytes()
  if p.suffix=='.json':pending.append((member,p.parent))
 # The routed correction lives outside its original sealed report folder.
 if name=='dimer_routed_transport_independent':
  for p in sorted((A/'dimer_routed_f1_fix').glob('*')):
   if not p.is_file():continue
   member='correction/'+p.name;contents[member]=p.read_bytes()
   if p.suffix=='.json':pending.append((member,p.parent))
 while pending:
  member,relative=pending.pop()
  if member in processed:continue
  processed.add(member);manifests.append(member)
  for row in rows(json.loads(contents[member])):
   key=row['path'],row['sha256']
   if key in bindings:continue
   p,data=resolve(row,relative);digest=sha(data)
   source_member='bound_sources/'+digest+'/'+p.name
   contents[source_member]=data
   bindings[key]=dict(original_path=row['path'],sha256=digest,bytes=len(data),
                     disposition='bundled',member=source_member)
   # Seal and source-manifest dependencies can themselves bind sources.
   if p.suffix=='.json' and ('SEAL' in p.name or 'SOURCES' in p.name):
    pending.append((source_member,p.parent))
 archive=E/'independent'/(name+'.zip')
 with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for member,data in sorted(contents.items()):
   info=zipfile.ZipInfo(member,date_time=(2026,9,21,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
   z.writestr(info,data)
 report=E/'independent'/(name+'_REPORT.md');shutil.copy2(folder/'REPORT.md',report)
 capsules.append(dict(name=name,archive='independent/'+archive.name,zip_sha256=sha(archive.read_bytes()),
  report='independent/'+report.name,report_sha256=report_sha,
  seal_members=sorted(manifests),
  manifest_coverage='All review JSON identity rows plus recursively bound seal/source manifests and the separately sealed routed F1 correction.',
  bindings=list(bindings.values()),
  members=[dict(path=k,bytes=len(v),sha256=sha(v)) for k,v in sorted(contents.items())]))
(E/'INDEPENDENT_CAPSULES.json').write_text(json.dumps(dict(capsules=capsules,external_reference_identities={}),indent=2)+'\n')
shutil.copy2(P/'.claude/science/mobile-record-all-stage-formation-20260921/verify_evidence.py',E/'verify_evidence.py')
print(json.dumps({'capsules':len(capsules),'members':sum(len(x['members']) for x in capsules),
                  'bindings':sum(len(x['bindings']) for x in capsules),
                  'manifest_members':sum(len(x['seal_members']) for x in capsules)}))
