#!/usr/bin/env python3
"""Portable byte verification of inherited and new independent evidence."""
from pathlib import Path,PurePosixPath
import hashlib,json,zipfile
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
sha=lambda data:hashlib.sha256(data).hexdigest()
new=json.loads((HERE/'INDEPENDENT_CAPSULES.json').read_text())
basepath=(HERE/new['base_capsule_manifest']).resolve();old=json.loads(basepath.read_text())
files={};seals=[];artifacts=dependencies=instructions=0
for directory,manifest in [(basepath.parent,old),(HERE,new)]:
 for item in manifest['capsules']:
  name=item['name'];archive=directory/(name+'.zip');assert sha(archive.read_bytes())==item['zip_sha256']
  with zipfile.ZipFile(archive) as z:
   for member in z.namelist():
    key=PurePosixPath(member);assert not key.is_absolute() and '..' not in key.parts
    data=z.read(member)
    if member in files:assert files[member]==data
    files[member]=data
  sealbytes=files[name+'/PRE_SOURCE_SEAL.json'];assert sha(sealbytes)==item['seal_sha256']
  assert sha(files[name+'/REPORT.md'])==item['report_sha256']
  assert files[name+'/REPORT.md']==(directory/(name+'_REPORT.md')).read_bytes()
  seal=json.loads(sealbytes);seals.append(seal)
  entries=seal['artifacts'];entries=entries if isinstance(entries,list) else [dict(path=k,**v) for k,v in entries.items()]
  for row in entries:
   data=files[name+'/'+row['path']]
   assert sha(data)==row['sha256'] and len(data)==row['bytes'];artifacts+=1

def resolve(original):
 p=PurePosixPath(original)
 try:return files[str(p.relative_to(new['original_campaign_root']))]
 except ValueError:pass
 rel=p.relative_to(new['original_repository_root'])
 return (ROOT/str(rel)).read_bytes()

for seal in seals:
 entries=[]
 entries.extend(dict(path=k,sha256=v) for k,v in seal.get('dependency_sha256',{}).items())
 entries.extend(seal.get('dependencies',[]));entries.extend(seal.get('source_identities',[]))
 for row in entries:
  data=resolve(row['path']);assert sha(data)==row['sha256'],row['path']
  if 'bytes' in row:assert len(data)==row['bytes']
  dependencies+=1
 instruction_rows=list(seal.get('instruction_identities',[]))
 instruction_rows.extend(dict(path=k,sha256=v) for k,v in seal.get('instruction_sha256',{}).items())
 for row in instruction_rows:
  data=resolve(row['path']);assert sha(data)==row['sha256']
  if 'bytes' in row:assert len(data)==row['bytes']
  instructions+=1
print(json.dumps(dict(capsules=len(seals),sealed_artifacts=artifacts,source_links=dependencies,instruction_snapshots=instructions,
 result='All byte identities verified. Scientific correctness and audit status are not inferred from hashes.')))
