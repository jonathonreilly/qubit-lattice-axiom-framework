#!/usr/bin/env python3
"""Read-only packet verification; no scientific or numerical theorem test."""
from pathlib import Path
import hashlib, json, re, subprocess
ROOT = Path(__file__).resolve().parents[6]
LANE = Path(__file__).resolve().parent.parent
CHECKS = LANE / 'checks'
PREFIX = 'nonlinear_chart_activity_'
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def resolve(path):
    return ROOT / path
manifest = json.loads((CHECKS / (PREFIX+'read_manifest.json')).read_text())
receipt = json.loads((CHECKS / (PREFIX+'receipt.json')).read_text())
for row in receipt['records']:
    assert digest(resolve(row['path'])) == row['sha256'], row['path']
for row in manifest['sources'] + manifest['protected_ps_pc_fu_files']:
    assert digest(resolve(row['path'])) == row['sha256'], row['path']
for row in manifest['methodology']:
    data = subprocess.check_output(['git', 'show', row['revision']+':'+row['path']], cwd=ROOT)
    assert hashlib.sha256(data).hexdigest() == row['sha256'], row['path']
source = resolve(manifest['mathematical_source_frozen_before_packaging']['path'])
assert digest(source) == '72651905fa554d44e7d42406af199ec0e9a75a88c030009626929f9f77dc1dec'
assert len(source.read_text().splitlines()) == 624
links = re.findall(r'\]\(([^)]+)\)', source.read_text())
for target in links:
    if '://' not in target:
        assert (source.parent / target.split('#',1)[0]).exists(), target
print(json.dumps({'packet_records_matched':len(receipt['records']), 'input_identities_matched':len(manifest['sources']), 'protected_files_matched':len(manifest['protected_ps_pc_fu_files']), 'methodology_identities_matched':len(manifest['methodology']), 'local_links_resolve':len(links), 'files_written':0, 'scientific_experiments':0, 'independent_review':'pending'}, sort_keys=True))
