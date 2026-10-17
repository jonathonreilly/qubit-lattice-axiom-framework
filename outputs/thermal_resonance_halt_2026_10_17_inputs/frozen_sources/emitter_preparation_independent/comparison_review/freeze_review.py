"""Freeze a source-exposed analytical review; no scientific program is run."""
from pathlib import Path
from datetime import datetime, timezone
import ast
import hashlib
import json
import os
import re

D = Path(__file__).resolve().parent
def pin(p):
    raw = p.read_bytes()
    return {'path': str(p.relative_to(D)), 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest()}
def save(name, data):
    with (D/name).open('x') as f:
        f.write(json.dumps(data, indent=2) + '\n')
        f.flush()
        os.fsync(f.fileno())

assert not (D/'ANALYTICAL_FREEZE.json').exists()
exposure = json.loads((D/'SOURCE_EXPOSURE.json').read_text())
rows = []
for row in exposure['source_exposure']:
    copy = (D/row['snapshot']).read_bytes()
    original = Path(row['original']).read_bytes()
    assert hashlib.sha256(copy).hexdigest() == row['sha256']
    assert original == copy
    rows.append({'snapshot': row['snapshot'], 'sha256': row['sha256'],
                 'lines': len(copy.splitlines()), 'original_unchanged': True})
prior = json.loads((D/'EXPOSURE_START.json').read_text())
for key in ['own_candidate', 'own_freeze']:
    row = prior[key]
    assert hashlib.sha256(Path(row['path']).read_bytes()).hexdigest() == row['sha256']
own_manifest = json.loads((D.parent/'FILE_MANIFEST.json').read_text())
for row in own_manifest['members']:
    raw = (D.parent/row['path']).read_bytes()
    assert len(raw) == row['bytes']
    assert hashlib.sha256(raw).hexdigest() == row['sha256']

review = (D/'COMPARISON_REVIEW.md').read_text()
links = re.findall(r'\]\(([^)]+)\)', review)
for link in links:
    assert (D/link).exists(), link
ast.parse(Path(__file__).read_text())
save('STATIC_REVIEW_CHECK.json', {
    'checked_utc': datetime.now(timezone.utc).isoformat(),
    'root_source_pins': rows,
    'own_original_members_verified': len(own_manifest['members']),
    'own_candidate_and_freeze_unchanged': True,
    'complete_review_lines': len(review.splitlines()),
    'review_links_resolve': links,
    'scientific_programs_executed_in_review': 0,
    'root_checker_output_or_receipts_read': False,
    'source_capture_failure_count': 1,
    'dependent_failed_display_count': 1,
    'failure_record': 'CAPTURE_FAILURE_01.json',
    'status': 'Analytical source-exposed check only; no executable-source validation or audit verdict',
    'changed_editable_prompt_files': []})
members = [pin(p) for p in sorted(D.iterdir()) if p.is_file()
           and p.name not in {'REVIEW_MANIFEST.json', 'ANALYTICAL_FREEZE.json'}]
save('REVIEW_MANIFEST.json', {'created_utc': datetime.now(timezone.utc).isoformat(),
                            'members': members})
save('ANALYTICAL_FREEZE.json', {
    'frozen_utc': datetime.now(timezone.utc).isoformat(),
    'status': 'Source-exposed analytical comparison frozen before root checker/output exposure',
    'review': pin(D/'COMPARISON_REVIEW.md'),
    'manifest': pin(D/'REVIEW_MANIFEST.json'),
    'exposure_start': pin(D/'EXPOSURE_START.json'),
    'actual_source_exposure': pin(D/'SOURCE_EXPOSURE.json'),
    'static_check': pin(D/'STATIC_REVIEW_CHECK.json'),
    'member_count_excluding_manifest_and_freeze': len(members),
    'scientific_execution': None,
    'root_checker_output_or_receipts_read': False,
    'disposition': 'No load-bearing failure under stated conditions; clarify D>0 and scaled-isometry wording; no architecture selected',
    'conditional_dependencies': [
        'Exact supplied positive complements and fields',
        'Delivered Gibbs marginal or stated delivery allowance',
        'Exact emitter cancellation throughout early stage',
        'Finite known setup completion time and actual phase areas',
        'Passive retained reference after delivery',
        'Inherited fixed-accuracy finite runtime theorem'],
    'limits': 'Same model and substantial shared inherited-source exposure. This is not root qualification, publication approval, retained audit, native preparation or full-controller realization.',
    'write_boundary': str(D)})
print(json.dumps({'review': pin(D/'COMPARISON_REVIEW.md'),
                  'freeze': pin(D/'ANALYTICAL_FREEZE.json'),
                  'manifest': pin(D/'REVIEW_MANIFEST.json'),
                  'member_count': len(members)}, indent=2))
