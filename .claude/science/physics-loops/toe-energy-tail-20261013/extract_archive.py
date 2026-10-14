#!/usr/bin/env python3
"""Read-only exact archive extraction to stdout; no filesystem writes or science."""
from pathlib import Path
import argparse,gzip,hashlib,json,sys
MAP_SHA='3e092d68b1be9dc66a70d7ba316550fb0db67bebaf7ee5737920f0799200affe'
def need(ok,message):
    if not ok:raise ValueError(message)
def sha(data):return hashlib.sha256(data).hexdigest()
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list',action='store_true')
    group.add_argument('--suffix')
    args=parser.parse_args();root=Path(__file__).resolve().parent
    data=(root/'EVIDENCE_MAP.json').read_bytes();need(sha(data)==MAP_SHA,'Archive map changed')
    evidence=json.loads(data);aliases={}
    for row in evidence['objects']:
        for alias in row['origins']:
            need(alias not in aliases,'Duplicate archive alias');aliases[alias]=row
    if args.list:
        print('\n'.join(sorted(aliases)));return
    matches=[a for a in aliases if a.endswith(args.suffix)]
    need(matches,'No matching original alias')
    rows={aliases[a]['sha256']:aliases[a] for a in matches}
    need(len(rows)==1,'Ambiguous suffix has different source bytes; use a longer suffix')
    row=next(iter(rows.values()));path=(root/row['path'])
    need(path.resolve().is_relative_to(root) and path.is_file() and not path.is_symlink(),'Invalid archive object path')
    stored=path.read_bytes();need(sha(stored)==row['stored_sha256'] and len(stored)==row['stored_bytes'],'Compressed archive changed')
    raw=gzip.decompress(stored);need(sha(raw)==row['sha256'] and len(raw)==row['bytes'],'Archived source changed')
    sys.stdout.buffer.write(raw)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        print(str(exc),file=sys.stderr);raise SystemExit(1)
