#!/usr/bin/env python3
"""Read-only packet verifier; no numerical experiment or theorem test."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[6]
LANE=ROOT/'.claude/science/toe-ruleset-20261021/agents/ym4d-proof'
PREFIX='critical_determinant_reader_'
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def check(records):
    for r in records:
        p=ROOT/r['path']
        assert digest(p)==r['sha256'],r['path']
receipt=json.loads((LANE/'checks'/f'{PREFIX}receipt.json').read_text())
manifest=json.loads((LANE/'checks'/f'{PREFIX}read_manifest.json').read_text())
check(receipt['records'])
check(manifest['sources'])
check(manifest['protected_predecessor_files'])
check(manifest['methodology'])
source=LANE/'CRITICAL_DETERMINANT_READER_ASTRA.md'
assert digest(source)==receipt['source_sha256']
assert len(source.read_bytes().splitlines())==receipt['source_lines']
links=re.findall(r'\[[^]\n]*\]\(([^)]+)\)',source.read_text())
for link in links:
    if '://' not in link:
        assert (source.parent/link.split('#',1)[0]).exists(),link
print(json.dumps({'packet_records_verified':len(receipt['records']),
 'input_identities_verified':len(manifest['sources']),
 'protected_predecessor_identities_verified':len(manifest['protected_predecessor_files']),
 'methodology_identities_verified':len(manifest['methodology']),
 'source_local_links_verified':len(links),'files_written':0,
 'scientific_experiments':0,'independent_review':'pending'},indent=2))
