#!/usr/bin/env python3
"""Read-only byte/receipt verifier, with default primary outcome UNBOUND.

No captured science imports, matrix propagation, integration, Git inspection,
external requests, binding acceptance or writes. SHA256 identity is not a
signature or mathematical proof. A separately supplied seal pins these bytes.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

BODY_PINS = {
    'sparse_derivation': '6b1e1ecd6afcf53dd05411493c18ceb9db258fcc279dc3c24072a516a5a76c3b',
    'sparse_analytical_review': '2af89ecefd2d682259e967cc96ef1f5965c37500de4d3cc9261cb39d50254a2a',
    'sparse_qualifications': '83b913c6b47ee8625cc15914759886e642515d02f284dc84a6b92d8e3ed54d3e',
    'runtime_qualifications': '9fb1514db57464c15de3156916922f405e80e3dc56b6d7624d2e9531b011f305',
    'fixture_report': 'c9e99e725b3efd8dabbf551c315e983113129de0ed12d5f9028c207f93fe9649',
    'fixture_exposed_review': 'c1f7a257fbb824d868c3ca25c7ba9fc8d7504f2e532ca83b8851427afdae305d',
    'fixture_qualifications': 'e2bf8af1a8c90068c33d833604717762cb1207e008ad52b3c330986cd470a4bc',
}
DECISION_PINS = {
    'sparse_acceptance': '999446a20afe1516069bdd7abebba103e5cd16be70762c85b221e5d2e75d4cda',
    'sparse_qualifications': BODY_PINS['sparse_qualifications'],
    'runtime_acceptance': '7a696aff18e51fd5d83548a49944a95ab3ccb180a6daf01b8629d8cad5578509',
    'runtime_qualifications': BODY_PINS['runtime_qualifications'],
    'fixture_acceptance': '449fed271fe190a1065c25c0fdf94fc75992e2a0511f35e258a7c6bd95b86021',
    'fixture_qualifications': BODY_PINS['fixture_qualifications'],
}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def member(root, row):
    name = row.get('packet_path', row.get('path'))
    rel = Path(name)
    require(not rel.is_absolute() and '..' not in rel.parts, 'Unsafe member: ' + name)
    path = root / rel
    require(path.is_file() and not path.is_symlink() and root in path.resolve().parents,
            'Missing or unsafe file: ' + name)
    raw = path.read_bytes()
    require(len(raw) == row['bytes'] and sha(raw) == row['sha256'], 'Identity mismatch: ' + name)
    return name

def inventory(root, under=None):
    start = root if under is None else root / under
    result = set()
    for path in start.rglob('*'):
        require(not path.is_symlink(), 'Symlink forbidden: ' + str(path))
        if path.is_file():
            result.add(str(path.relative_to(root)))
    return result

def load(root, name):
    return json.loads((root / name).read_text())

def verify(root):
    manifest = load(root, 'SOURCE_MANIFEST.json')
    rows = manifest['source_closure'] + manifest['history_records'] + manifest['packet_payload']
    names = [member(root, row) for row in rows]
    require(len(names) == len(set(names)), 'Duplicate manifest paths')
    source_by_path = {row['packet_path']: row for row in manifest['source_closure']}
    require(inventory(root, 'source') == set(source_by_path), 'Source closure has missing/extra files')
    require(inventory(root, 'history') == {r['packet_path'] for r in manifest['history_records']},
            'History inventory has missing/extra files')
    require(len(manifest['closures']) == 7, 'Expected seven selected immediate closures')
    for closure in manifest['closures']:
        seal = load(root, member(root, closure['freeze']))
        entries = seal.get('members', seal.get('files'))
        require(isinstance(entries, list) and len(entries) == closure['member_count'], 'Invalid source seal')
        expected = set()
        for item in entries:
            rel = Path(item['path'])
            if rel.is_absolute():
                rel = rel.relative_to(Path(closure['original_root']))
            packet = str(Path(closure['packet_root']) / rel)
            member(root, {'packet_path': packet, 'bytes': item['bytes'], 'sha256': item['sha256']})
            expected.add(packet)
        require(len(expected) == len(entries), 'Duplicate source-seal members')
        expected.add(closure['freeze']['packet_path'])
        require(inventory(root, closure['packet_root']) == expected, 'Incomplete immediate closure')
    bodies = load(root, 'BODY_RECOVERY_MAP.json')['immutable_bodies']
    require(len(bodies) == 7 and {r['body_id'] for r in bodies} == set(BODY_PINS), 'Incomplete body map')
    for row in bodies:
        member(root, row)
        require(row['sha256'] == BODY_PINS[row['body_id']], 'Body pin mismatch')
        require(all(row[k] == source_by_path[row['packet_path']][k]
                    for k in ['original_path', 'packet_path', 'bytes', 'sha256']), 'Body map recovery mismatch')
    provenance = load(root, 'PROVENANCE.json')
    nulls = ['actual_git_base', 'canonical_parent', 'canonical_binding', 'canonical_acceptance',
             'current_wrapper_review', 'publication', 'integration_driver']
    require(provenance['primary_status'] == 'UNBOUND' and all(provenance[k] is None for k in nulls),
            'Source-only checker refuses a primary/canonical/integration binding')
    require(provenance['fixture_disposition'] == 'QUALIFIED_SINGLE_NUMERICAL_FIXTURE_AND_SAVED_ARTIFACT_INSPECTION',
            'Wrong current fixture disposition')
    require(provenance['retained_audit'] is False and provenance['scientific_executions'] == 0,
            'Unsupported execution/audit status')
    require(provenance['rigorous_fixture_residual_certificate'] is False
            and provenance['independent_fixture_propagation'] is False, 'Overstated fixture evidence')
    require(set(provenance['source_decisions']) == set(DECISION_PINS), 'Missing source decisions')
    for key, expected in DECISION_PINS.items():
        row = provenance['source_decisions'][key]
        member(root, row)
        require(row['sha256'] == expected, 'Decision pin mismatch: ' + key)
    require(provenance['historical_wrapper_review_only']['sha256'] ==
            'a33ef4f684fc567544a36da12d87a69588de29b10fc6815b6f1a26801b6e19fc', 'Wrong historical review')
    require(provenance['historical_draft_seal_only']['sha256'] ==
            '0903d917f7fffcde78c432acfe7ba11dae9c7bfd917c9f08f09a50293db67b72', 'Wrong historical seal')
    member(root, provenance['historical_wrapper_review_only'])
    member(root, provenance['historical_draft_seal_only'])
    evidence = load(root, 'EVIDENCE_MAP.json')
    histories = evidence['actual_historical_executions']
    require(len(histories) == 4, 'Missing execution history')
    original_map = {r['original_path']: r for r in manifest['source_closure']}
    for item in histories:
        receipt = load(root, member(root, item['receipt']))
        for role in ['source', 'launcher', 'stdout', 'stderr']:
            member(root, item[role])
            if item['schema'] == 'fixture_nested':
                observed = receipt[role]
                require(observed['sha256'] == item[role]['sha256'] and observed['bytes'] == item[role]['bytes'],
                        'Nested receipt binding mismatch')
                require(original_map[observed['path']]['packet_path'] == item[role]['packet_path'],
                        'Nested receipt recovery mismatch')
            else:
                require(receipt[role + '_sha256'] == item[role]['sha256'], 'Flat receipt binding mismatch')
                if item['schema'] == 'inspection_flat' and role in ['stdout', 'stderr']:
                    require(receipt[role + '_bytes'] == item[role]['bytes'], 'Stream size mismatch')
        exit_code = receipt.get('returncode', receipt.get('exit_code'))
        require(exit_code == item['expected_exit'], 'Historical exit changed')
        require(isinstance(receipt['argv'], list) and isinstance(receipt['cwd'], str), 'Missing actual launch data')
    for row in evidence['full_fixture_outputs']:
        member(root, row)
    result = load(root, 'source/emitted_fixture/runs/attempt_01/output/RESULT.json')
    for row in result['words'].values():
        member(root, {'packet_path': 'source/emitted_fixture/runs/attempt_01/output/' + row['path'],
                      'bytes': row['bytes'], 'sha256': row['sha256']})
    sealed_count = None
    if (root / 'FREEZE.json').exists():
        seal = load(root, 'FREEZE.json')
        sealed_names = [member(root, row) for row in seal['members']]
        require(len(sealed_names) == len(set(sealed_names)), 'Duplicate final-seal members')
        require('FREEZE.json' not in sealed_names, 'Self-including final seal')
        require(inventory(root) - {'FREEZE.json'} == set(sealed_names),
                'Final packet inventory has missing or extra files')
        sealed_count = len(sealed_names)
    return {'kind': 'read_only_metadata_verification', 'primary_status': 'UNBOUND',
            'source_files': len(manifest['source_closure']), 'immediate_closures': 7,
            'history_records': len(manifest['history_records']), 'immutable_bodies': 7,
            'current_payload_files': len(manifest['packet_payload']), 'historical_receipts_bound': 4,
            'fixture_disposition': provenance['fixture_disposition'],
            'exact_final_inventory_members': sealed_count,
            'exact_final_inventory_checked': sealed_count is not None,
            'scientific_executions': 0, 'null_bindings': nulls,
            'meaning': 'Selected byte closure and receipt bindings only; no mathematical, interval, physical, canonical or publication certification.'}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--packet-root', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--source-only', action='store_true')
    args = parser.parse_args()
    result = verify(args.packet_root.resolve())
    result['status'] = 'SOURCE_CLOSURE_VERIFIED' if args.source_only else 'UNBOUND'
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    return 0 if args.source_only else 2

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        print(json.dumps({'status': 'INVALID_SOURCE_CLOSURE', 'error': str(exc)}, indent=2), file=sys.stderr)
        sys.exit(1)
