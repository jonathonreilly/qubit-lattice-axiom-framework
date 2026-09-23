"""Freeze the bounded comparison, preserving and reauthenticating PRE."""
import datetime
import hashlib
import json
from pathlib import Path
import sys

base = Path(__file__).resolve().parent
author = base.parent/'compensated_volume_author'
target = base/'FINAL_SEAL.json'
if target.exists():
    raise FileExistsError(target)


def binding(path):
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


pre_path = base/'PRE_COMPARISON_SEAL.json'
assert binding(pre_path)['sha256'] == '6e8bae143d8ee1e0c77c57461c8025143b660709ff89e42c5c072a38d2164d0f'
pre = json.loads(pre_path.read_text())
for row in pre['sources'] + pre['artifacts']:
    assert binding(Path(row['path'])) == row
author_seal_path = author/'AUTHOR_SEAL.json'
assert binding(author_seal_path)['sha256'] == '5da6ab8a81e7f6442a3c63ece190e9119b3c2cdd00c9960465bc01cc963d1f7f'
author_seal = json.loads(author_seal_path.read_text())
source_map = {}
for row in pre['sources'] + author_seal['sources'] + author_seal['artifacts']:
    assert binding(Path(row['path'])) == row
    source_map[row['path']] = row
source_map[str(author_seal_path)] = binding(author_seal_path)
clarification = author/'ROOT_TIME_TOPOLOGY_CLARIFICATION.md'
assert binding(clarification)['sha256'] == '256c6243b7f0c4d7208dd8b2ced8971b9f843bb8a9a715e36be05ce10e932fdd'
source_map[str(clarification)] = binding(clarification)

for name in ('comparison_check_run', 'clarification_ack_run'):
    receipt = json.loads((base/f'{name}.receipt.json').read_text())
    assert receipt['exit_code'] == 0
    assert binding(Path(receipt['command_argv'][1]))['sha256'] == receipt['source_sha256']
    for suffix in ('stdout', 'stderr'):
        assert binding(base/f'{name}.{suffix}')['sha256'] == receipt[f'{suffix}_sha256']
ack = json.loads((base/'F1_CLARIFICATION_ACK.json').read_text())
assert ack['disposition'].startswith('Resolved')
for row in ack['bindings']:
    assert binding(Path(row['path'])) == row

sources = [source_map[key] for key in sorted(source_map)]
artifacts = [binding(p) for p in sorted(base.iterdir()) if p.is_file() and p != target]
seal = {
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'procedure_argv': [sys.executable, str(Path(__file__).resolve())],
    'scope': 'Bounded authorized post-PRE scientific comparison of the compensated rotor target local-volume theorem.',
    'PRE_preserved': binding(pre_path),
    'author_packet': binding(author_seal_path),
    'separate_source_clarification': binding(clarification),
    'disposition': 'F1 topology wording resolved by the explicit separate clarification. No remaining mathematical finding in the reviewed target-volume claim. Not a formal audit/publication verdict.',
    'read_scope': 'Complete new author argument, control interpretation, scientific runner, all result fields and bound receipt/seal metadata; unchanged checked premises reused by identity.',
    'execution_scope': 'Own symbolic physical phase and off-diagonal field Gram check; two selected independently rebuilt overlap geometries; identity/receipt authentication. Author scientific runner not reexecuted.',
    'independent_additions_preserved': ['bounded-electric-cutoff proof in PRE',
                                       'global-folium counterexample in PRE',
                                       'PRE amplified local-map normality and state/boundary extensions'],
    'scope_limits': ['No numerical proof of infinite-volume dynamics.',
                     'No microscopic volume-uniform scaling or interchange of limits.',
                     'No phase/native/resource claim or unrelated frontier review.'],
    'sources': sources, 'artifacts': artifacts,
}
target.write_text(json.dumps(seal, indent=2)+'\n')
for row in sources + artifacts:
    assert binding(Path(row['path'])) == row
print(json.dumps({'FINAL_SEAL': binding(target), 'COMPARISON': binding(base/'COMPARISON.md'),
                  'verified_sources': len(sources), 'verified_artifacts': len(artifacts),
                  'F1': 'resolved by separate clarification', 'PRE_unchanged': True}, indent=2))
