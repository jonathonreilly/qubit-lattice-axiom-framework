#!/usr/bin/env python3
"""Verify portable review bytes, distinguishing the unbundled reference PDF."""
from pathlib import Path, PurePosixPath
import hashlib, json, zipfile

HERE=Path(__file__).resolve().parent
sha=lambda data:hashlib.sha256(data).hexdigest()

def rows(obj):
    if isinstance(obj,dict):
        if isinstance(obj.get('path'),str) and 'sha256' in obj:yield obj
        for value in obj.values():yield from rows(value)
    elif isinstance(obj,list):
        for value in obj:yield from rows(value)

manifest=json.loads((HERE/'INDEPENDENT_CAPSULES.json').read_text())
members=bindings=seal_rows=0
external=[]
for capsule in manifest['capsules']:
    archive=HERE/capsule['archive'];assert sha(archive.read_bytes())==capsule['zip_sha256']
    with zipfile.ZipFile(archive) as z:
        assert len(z.namelist())==len(set(z.namelist()))
        data={name:z.read(name) for name in z.namelist()}
    assert set(data)=={row['path'] for row in capsule['members']}
    for row in capsule['members']:
        path=PurePosixPath(row['path']);assert not path.is_absolute() and '..' not in path.parts
        assert len(data[row['path']])==row['bytes'] and sha(data[row['path']])==row['sha256']
        members+=1
    assert data['review/REPORT.md']==(HERE/capsule['report']).read_bytes()
    assert sha(data['review/REPORT.md'])==capsule['report_sha256']
    lookup={(row['original_path'],row['sha256']):row for row in capsule['bindings']}
    for row in capsule['bindings']:
        if row['disposition']=='bundled':
            assert sha(data[row['member']])==row['sha256'] and len(data[row['member']])==row['bytes']
            bindings+=1
        else:
            assert row['disposition']=='external_reference_not_bundled'
            assert row['sha256']=='c919dec4d75cafd53138a9ec64d09d344ce520caadb5a85a77f7561faa70106d'
            assert row['url']=='https://arxiv.org/pdf/1010.5064v1'
            external.append(dict(capsule=capsule['name'],**row))
    for key in capsule['seal_members']:
        for row in rows(json.loads(data[key])):
            bound=lookup[row['path'],row['sha256']]
            if 'bytes' in row:assert bound['bytes']==row['bytes']
            seal_rows+=1
print(json.dumps(dict(capsules=len(manifest['capsules']),bundled_members=members,
                     bundled_source_bindings=bindings,seal_rows=seal_rows,
                     external_reference_exclusions=external,
                     scope='Bundled bytes authenticated. External PDF not fetched or verified by this portable check; its original local verification is recorded. No scientific correctness or audit status inferred.')))
