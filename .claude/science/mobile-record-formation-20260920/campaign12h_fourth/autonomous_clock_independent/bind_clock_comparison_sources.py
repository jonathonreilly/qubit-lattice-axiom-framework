#!/usr/bin/env python3
"""Authenticate the frozen spin-clock PRE and released traveling-clock packet."""
from pathlib import Path
import datetime,hashlib,json
HERE=Path(__file__).resolve().parent;CAMPAIGN=HERE.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
pre_hash='d015c9245087ce39c102c61d859171c58ccd5b4a2ea4d25ea2b9bc37a61493ad'
assert sha(HERE/'PRE_SEAL.json')==pre_hash
pre=json.loads((HERE/'PRE_SEAL.json').read_text())
for r in pre['files']:
 p=HERE/r['path'];assert sha(p)==r['sha256'] and p.stat().st_size==r['bytes'],r['path']
author=CAMPAIGN/'autonomous_clock_author'
seal_hash='dcff32f98d26b2cddfdcfa8feeb4dc8907b9174f54f0b51f3ec0cda0a9fa6c4e'
assert sha(author/'AUTHOR_SEAL.json')==seal_hash
seal=json.loads((author/'AUTHOR_SEAL.json').read_text());rows=[]
def bind(alias,expected,role):
 src=CAMPAIGN/alias;assert sha(src)==expected,(alias,sha(src),expected)
 dest=HERE/'comparison_sources'/alias;dest.parent.mkdir(parents=True,exist_ok=True)
 data=src.read_bytes()
 if dest.exists():assert dest.read_bytes()==data
 else:dest.write_bytes(data)
 rows.append({'campaign_relative_alias':alias,'snapshot_path':str(dest.relative_to(HERE)),'sha256':expected,'bytes':len(data),'role':role})
bind('autonomous_clock_author/AUTHOR_SEAL.json',seal_hash,'released target seal')
for r in seal['artifacts']:
 bind('autonomous_clock_author/'+r['path'],r['sha256'],'released target artifact');assert rows[-1]['bytes']==r['bytes']
for alias,digest in seal['sources_sha256'].items():bind(alias,digest,'released target dependency')
bind('microscopic_electric_robustness_independent/EXACT_STAR_MATRIX_RESULTS.json','8b26fca39e618219ed263cdd4e15ebac084a22359abeb62144c67e41b359922f','own previously sealed independent full local matrices; no root builder imported')
bind('microscopic_electric_robustness_independent/star_local_matrix_control.py','1d99b207b028f191961331b0c79662f9fe13e93dc145ce53c38da00deed81254','own local-construction source identity; comparison reconstructs from frozen matrix data')
result={'stage':'post-PRE source comparison','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'PRE_seal_sha256':pre_hash,'PRE_files_authenticated_unchanged':len(pre['files']),'released_author_seal_sha256':seal_hash,'sources':rows,'portability':'Relative aliases and exact hashes are authoritative. Public projections may omit historical instruction provenance with an explicit omission manifest. No third-party paper/content is copied here; a released dependency seal may retain its bibliographic hash metadata.'}
(HERE/'COMPARISON_SOURCE_BINDINGS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'PRE_files_unchanged':len(pre['files']),'comparison_sources':len(rows),'author_seal_sha256':seal_hash},indent=2))
