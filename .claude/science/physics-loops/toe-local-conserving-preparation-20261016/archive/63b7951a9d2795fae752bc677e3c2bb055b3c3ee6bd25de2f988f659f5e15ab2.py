"""Metadata-only capture and exact source verification; no scientific runner."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

OUT = Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_control_author_exposed_check')
N = OUT.parent
SRC = N / 'local_conserving_control_candidate'
sha = lambda b: hashlib.sha256(b).hexdigest()
expected_freeze = '3128a438f020588eb8e8e945b1cbe9f4e6d64f5524831e19e530ff28a1e08c9b'
raw_freeze = (SRC / 'FREEZE.json').read_bytes()
assert sha(raw_freeze) == expected_freeze
freeze = json.loads(raw_freeze)
target = OUT / 'author_source'
target.mkdir(exist_ok=False)
rows = []
all_rows = list(freeze['members']) + [{'path': 'FREEZE.json', 'bytes': len(raw_freeze), 'sha256': expected_freeze}]
for row in all_rows:
    rel = Path(row['path'])
    assert not rel.is_absolute() and '..' not in rel.parts
    raw = (SRC / rel).read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256'], row['path']
    dest = target / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw)
    assert dest.read_bytes() == raw
    rows.append({'original_path': str(SRC / rel), 'capture': str(dest.relative_to(OUT)), 'bytes': len(raw), 'sha256': sha(raw)})
assert sha((target/'DERIVATION.md').read_bytes()) == 'c7f0e58c79b7e05f7fe79374a8bbe52a290c0371392a0b0ddcdb98d3dbb49e60'
assert sha((target/'sources/FINITE_RESERVOIR_PARENT.md').read_bytes()) == 'ee90d960f0db9f30c861d837c53e306a50a855c7af251a748e655749a8a9a195'
assert sha((target/'sources/BAI_MARVIAN_2309.11051v3.pdf').read_bytes()) == 'add4e97c6c0a1939d159924088c45481d54c2c54646d5cfebbbc7faa471154e8'

prior = N / 'local_conserving_control_root_exposed_check'
prior_ids = {
    'REVIEW.md': '70d14b789941483c88d39e582195485f5230528415197ad763183fab6407ebc4',
    'FINAL_FREEZE.json': 'f17710dd8d161053aa6f8168496dc739aeea8488105c422d834e274a2cc043cd',
}
prior_rows = []
for name, expected in prior_ids.items():
    raw = (prior / name).read_bytes()
    assert sha(raw) == expected
    prior_rows.append({'path': str(prior/name), 'bytes': len(raw), 'sha256': expected, 'current_action': 'identity check only; previously read/authored, unchanged'})

a = json.loads((target/'RETRIEVAL.json').read_text())['screen']['argv'][-2]
b = json.loads((target/'SCOPE_SCREEN_CORRECTED.json').read_text())['argv'][-2]
search_finding = {
    'kind': 'comparison_of_saved_metadata_arguments_only',
    'saved_regex_arguments_equal': a == b,
    'first_saved_argument': a,
    'corrected_saved_argument': b,
    'numeric_prefix_codepoints': [ord(c) for c in b.split('|')[0]],
    'interpretation': 'Both saved numeric patterns have one backslash before the period. The separately annotated earlier overescaped argv is not recoverable from these two records. No search was replayed and no undocumented argv reconstructed.',
}
(OUT/'SEARCH_RECEIPT_FINDING.json').write_text(json.dumps(search_finding, indent=2)+'\n')
manifest = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'kind': 'actual_metadata_identity_and_capture',
    'source_records': rows,
    'all_author_freeze_members_verified': True,
    'author_freeze_member_count': len(freeze['members']),
    'prior_root_only_exposure_unchanged': prior_rows,
    'scientific_executions': 0,
    'earlier_root_exposure_precedes_author_exposure': True,
    'no_other_new_root_review_or_worker_results_read': True,
}
(OUT/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest, indent=2)+'\n')
print(json.dumps({'source_records':len(rows), 'author_freeze_members_verified':len(freeze['members']), 'all_identities_match':True, 'prior_root_exposure_unchanged':True, 'search_receipt_finding':search_finding, 'scientific_executions':0},indent=2))
