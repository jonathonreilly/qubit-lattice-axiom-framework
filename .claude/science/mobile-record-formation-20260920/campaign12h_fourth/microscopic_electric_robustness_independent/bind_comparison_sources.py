#!/usr/bin/env python3
"""Freeze comparison sources without changing any PRE-bound byte.
Scientific source names are campaign-relative aliases; SHA256 is authoritative.
A relocated archive can use --campaign-fourth PATH at the initial bind step.
"""
from pathlib import Path
import argparse,hashlib,json,datetime
HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--campaign-fourth',type=Path,default=HERE.parent)
a=p.parse_args();ROOT=a.campaign_fourth.resolve()
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def bind_assert(path,wanted):
 got=sha(path)
 assert got==wanted,(str(path),got,wanted)
 return path.read_bytes()
def new(path,data):
 path.parent.mkdir(parents=True,exist_ok=True)
 if path.exists():assert path.read_bytes()==data,('refusing to overwrite changed comparison file',str(path))
 else:path.write_bytes(data)
pre_hash='92f534204e822fbbc38f4cfbd8a5f6d1d33f09b727d7bead68fd22dfb4734faa'
bind_assert(HERE/'PRE_SEAL.json',pre_hash)
pre=json.loads((HERE/'PRE_SEAL.json').read_text())
for row in pre['files']:
 path=HERE/row['path'];bind_assert(path,row['sha256']);assert path.stat().st_size==row['bytes']
author=ROOT/'microscopic_electric_robustness_author'
author_seal_hash='fe08f9e62cfc1278cf659127e23989435cb6f0dcc39942a1e6cbef7eec0b1b21'
bind_assert(author/'AUTHOR_SEAL.json',author_seal_hash)
author_seal=json.loads((author/'AUTHOR_SEAL.json').read_text())
rows=[]
def snapshot(relative,wanted,role):
 src=ROOT/relative;data=bind_assert(src,wanted)
 dst=HERE/'comparison_sources'/'campaign12h_fourth'/relative
 new(dst,data)
 rows.append({'campaign_relative_path':'campaign12h_fourth/'+relative,'snapshot_path':dst.relative_to(HERE).as_posix(),'bytes':len(data),'sha256':wanted,'role':role})
snapshot('microscopic_electric_robustness_author/AUTHOR_SEAL.json',author_seal_hash,'released author seal')
for row in author_seal['files']:
 snapshot('microscopic_electric_robustness_author/'+row['path'],row['sha256'],'released author artifact')
 assert rows[-1]['bytes']==row['bytes']
for path,wanted in author_seal['sources_sha256'].items():snapshot(path,wanted,'released author dependency')
manifest={'stage':'post-PRE source comparison','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'PRE_seal_sha256':pre_hash,'PRE_bound_files_authenticated':len(pre['files']),'author_seal_sha256':author_seal_hash,'path_policy':'All scientific aliases are campaign-relative; relocated snapshots are matched by SHA256. No absolute private path is required by comparison controls.','sources':rows}
new(HERE/'COMPARISON_SOURCE_BINDINGS.json',(json.dumps(manifest,indent=2)+'\n').encode())
print(json.dumps({'PRE_seal_sha256':pre_hash,'PRE_bound_files_unchanged':len(pre['files']),'released_sources_authenticated_and_snapshotted':len(rows),'author_seal_sha256':author_seal_hash},indent=2))
