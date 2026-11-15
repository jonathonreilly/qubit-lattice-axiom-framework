#!/usr/bin/env python3
"""Read-only identity checks; no scientific computation or author mutation."""
from pathlib import Path
import ast
import hashlib
import json
import re
from datetime import datetime, timezone

ROOT = Path.cwd()
L = ROOT / '.claude/science/toe-ruleset-20261021/agents/ym4d-proof'
C = L / 'checks'
EXPECTED_SOURCE = 'f8e5ac755f106cf9419f81d3d3f683949c59abfe4f8ad1a250795fa6ec1c58d4'
EXPECTED_REPORT = '0d039b6cc62fa8fe285342d08b4bc95a88fbd942c719d219dc5795f97f10248f'
EXPECTED_AUTHOR_RECEIPT = '5de6261b7d9aa257802878a5c71c8909b69d5ba7f6ecf61da51472d76e35ff64'


def digest(path):
    path = Path(path)
    if not path.is_absolute():
        path = ROOT / path
    raw = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
            'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def verify(record):
    actual = digest(record['path'])
    assert actual['sha256'] == record['sha256'], (record['path'], 'hash mismatch')
    if 'bytes' in record:
        assert actual['bytes'] == record['bytes'], (record['path'], 'byte mismatch')
    return actual


def read_json(name):
    return json.loads((C / name).read_text())


source = digest(L / 'OUTSIDE_CHART_RETURN_ASTRA.md')
report = digest(L / 'REVIEW_OUTSIDE_CHART_RETURN_ASTRA.md')
author_receipt_pin = digest(C / 'outside_chart_return_receipt.json')
assert source['sha256'] == EXPECTED_SOURCE
assert report['sha256'] == EXPECTED_REPORT
assert author_receipt_pin['sha256'] == EXPECTED_AUTHOR_RECEIPT
receipt = read_json('outside_chart_return_receipt.json')
manifest = read_json('outside_chart_return_read_manifest.json')
source_freeze = read_json('outside_chart_return_source_freeze.json')
assert receipt['author_source'] == source
assert manifest['author_source'] == source
verify(source_freeze['source'])
assert len((L / 'OUTSIDE_CHART_RETURN_ASTRA.md').read_text().splitlines()) == source_freeze['source']['lines'] == 641
owned = [verify(x) for x in receipt['owned_files']]
current_inputs = [verify(x) for x in receipt['input_pins']]
methodology = [verify(x) for x in manifest['reused_methodology_reads']]
assert len(owned) == 7 and len(current_inputs) == 23 and len(methodology) == 27
actual_author_set = {str(p.relative_to(ROOT)) for p in C.glob('outside_chart_return_*')}
actual_author_set.add(source['path'])
expected_author_set = {x['path'] for x in owned} | {author_receipt_pin['path']}
assert actual_author_set == expected_author_set
assert receipt['input_pins'] == manifest['source_inputs']

predecessor_records = []
for packet in manifest['immutable_CC_CS_packets']:
    verify(packet['receipt'])
    data = json.loads((ROOT / packet['receipt']['path']).read_text())
    rows = data['owned_files'] if 'owned_files' in data else data['artifacts']
    assert len(rows) == packet['owned_records_verified']
    predecessor_records.extend(verify(x) for x in rows)
assert len(predecessor_records) == 64
for pin in receipt['predecessor_receipt_pins']:
    verify(pin)

binding = receipt['GC_binding']
verify(binding['current_source'])
verify(binding['coordinator_correction'])
verify(binding['affected_confirmation'])
verify(binding['historical_author_receipt'])
verify(binding['independent_review_receipt'])
for pin in binding['historical_author_non_source_files']:
    verify(pin)
correction = json.loads((ROOT / binding['coordinator_correction']['path']).read_text())
gc_text = (ROOT / binding['current_source']['path']).read_text()
change = correction['exact_change']
assert gc_text.count(change['after']) == 1
old_bytes = gc_text.replace(change['after'], change['before'], 1).encode()
assert hashlib.sha256(old_bytes).hexdigest() == binding['historical_author_source']['sha256'] == correction['source_before_sha256']
assert len(old_bytes) == binding['historical_author_source']['bytes']
gc_review = json.loads((ROOT / binding['independent_review_receipt']['path']).read_text())
gc_review_records = [verify(x) for x in gc_review['owned_files']]
assert len(gc_review_records) == binding['independent_review_owned_records_verified'] == 8

source_text = (L / 'OUTSIDE_CHART_RETURN_ASTRA.md').read_text()
labels = [int(x) for x in re.findall(r'^\s+.*\(OC(\d+)\)\s*$', source_text, flags=re.M)]
assert labels == list(range(1, 33))
local_links = []
for file in (L / 'OUTSIDE_CHART_RETURN_ASTRA.md', C / 'outside_chart_return_routes.md',
             L / 'REVIEW_OUTSIDE_CHART_RETURN_ASTRA.md'):
    in_fence = False
    for line_no, line in enumerate(file.read_text().splitlines(), 1):
        if line.startswith('```'):
            in_fence = not in_fence
        if in_fence or line.startswith('    '):
            continue
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', line):
            if '://' in target or target.startswith('#'):
                continue
            path = (file.parent / target.split('#', 1)[0]).resolve()
            assert path.is_file(), (str(file), line_no, target)
            local_links.append({'path': str(file.relative_to(ROOT)), 'line': line_no, 'target': target})

for file in (C / 'outside_chart_return_freeze.py', Path(__file__)):
    ast.parse(file.read_text(), filename=str(file))

result = {
    'checked_utc': datetime.now(timezone.utc).isoformat(),
    'scope': 'Mechanical identities, JSON records, Python syntax and local links only; not mathematical proof or audit.',
    'source': source, 'source_lines': 641, 'mathematical_report': report,
    'author_receipt': author_receipt_pin,
    'author_files_including_receipt': len(expected_author_set),
    'author_owned_hashes_verified': owned,
    'author_current_inputs_verified': current_inputs,
    'author_reused_methodology_pin_count': len(methodology),
    'predecessor_owned_pin_count': len(predecessor_records),
    'GC_historical_source_reconstructed_without_writing': True,
    'GC_review_owned_pin_count': len(gc_review_records),
    'equation_labels': labels, 'local_links': local_links,
    'scientific_numerical_runs': 0,
    'author_script_executed': False,
    'source_or_author_package_mutated': False,
    'prior_operational_observation': 'A read attempted before packaging completed found outside_chart_return_receipt.json absent; author announced completion before this verification. Not a science failure.'
}
print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
