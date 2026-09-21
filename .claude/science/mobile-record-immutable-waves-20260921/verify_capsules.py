#!/usr/bin/env python3
"""Verify raw independent evidence without relying on original absolute paths."""
from pathlib import Path, PurePosixPath
import hashlib,json,zipfile
HERE=Path(__file__).resolve().parent
sha=lambda data:hashlib.sha256(data).hexdigest()
m=json.loads((HERE/'INDEPENDENT_CAPSULES.json').read_text());files={};seals=[];artifacts=dependencies=0
for item in m['capsules']:
    name=item['name'];archive=HERE/(name+'.zip');assert sha(archive.read_bytes())==item['zip_sha256']
    with zipfile.ZipFile(archive) as z:
        for member in z.namelist():
            path=PurePosixPath(member);assert not path.is_absolute() and '..' not in path.parts
            files[member]=z.read(member)
    sealdata=files[name+'/PRE_SOURCE_SEAL.json'];assert sha(sealdata)==item['seal_sha256']
    assert sha(files[name+'/REPORT.md'])==item['report_sha256']
    assert (HERE/(name+'_REPORT.md')).read_bytes()==files[name+'/REPORT.md']
    seal=json.loads(sealdata);seals.append(seal)
    raw=seal['artifacts'];entries=raw if isinstance(raw,dict) else {a['path']:a for a in raw}
    for path,a in entries.items():
        data=files[name+'/'+path];assert len(data)==a['bytes'] and sha(data)==a['sha256'];artifacts+=1
for seal in seals:
    entries=seal.get('dependency_sha256',{})
    if 'dependencies' in seal: entries={a['path']:a['sha256'] for a in seal['dependencies']}
    for original,digest in entries.items():
        relative=str(PurePosixPath(original).relative_to(m['original_campaign_root']))
        assert sha(files[relative])==digest;dependencies+=1
print(json.dumps({'capsules':len(seals),'sealed_artifacts':artifacts,'dependency_links':dependencies,
                  'result':'all byte identities verified; scientific judgment is not automated'}))
