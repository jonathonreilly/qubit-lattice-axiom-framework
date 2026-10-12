#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path

def digest(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def verify(root, expected_manifest_sha):
    root=Path(root).resolve(); manifest=root/'FROZEN_EXECUTION_MANIFEST.json'
    got=digest(manifest)
    if got!=expected_manifest_sha:
        raise RuntimeError('MANIFEST_PIN_MISMATCH expected='+expected_manifest_sha+' actual='+got)
    data=json.loads(manifest.read_text())
    checked=[]
    for item in data['files']:
        q=(root/item['path']).resolve()
        if not q.is_relative_to(root):raise RuntimeError('PATH_ESCAPE '+item['path'])
        h=digest(q)
        if h!=item['sha256']:raise RuntimeError('SOURCE_PIN_MISMATCH '+item['path']+' expected='+item['sha256']+' actual='+h)
        checked.append({'path':item['path'],'sha256':h})
    return {'manifest_sha256':got,'files':checked}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--expected',required=True);a=p.parse_args()
    try:
        result=verify(a.root,a.expected)
        print(json.dumps({'guard':'accepted','manifest_sha256':result['manifest_sha256'],'files_checked':len(result['files'])}))
    except Exception as e:
        print(json.dumps({'guard':'rejected','reason':str(e)}))
        raise SystemExit(3)
