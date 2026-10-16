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


AUDIT_TIMEOUT_SEC = 60
MANIFEST_SHA256 = '42f7dfb1174388dc8db6f6527eff107b4272439ce3ef2d280955cccac45727b3'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-local-conserving-sparse-20261016/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/ACTUAL_REFRESH_PROVENANCE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/BODY_MAP.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/CANONICAL_BINDING.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/INPUT_MANIFEST.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/PARENT_BINDING.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/PR_TITLE.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/README.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/0c87d3be9af2418d0de0175251998f83dbc1a3cd46a2b943640410dd81990394.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/0da27d48c154171d0fd975bcf554d3f10862c9414925157481ae26fbc2b02433.blob', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/1921469ba53746b85df3d36febffd3f1213f5c66cf59514825c065232ecbf4b7.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/2fc15f9c50e73fd70c433bdebb56a427ade2d7501fbbe50d9ce731d7a43b926f.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/350ade715db5d1e9069c3d962943dd2c8154280b1d4ed32da400dc55e881d273.blob', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/354a3b8a1605759b74708a45c33aafe27fdb622ad7b402c0efaa6c29330f9606.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/3719075eb69419159544c969409a7bba3045f2e321609f2f044df6f209e7c3dd.blob', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/3d5604eab20b799db4862ce095a23dbf5b2816f2f48b77692919afcfc5acc6f4.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/3da24ce3e7c2af1db5160917d51e06931493b97f0826d3ea158124430a997e1a.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/4d0d6b112e46ec0a20b4aad89637f7245aea141d6420bb6a4d781220a644f9c6.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/4db683d3c480902089122fdd83c2365ecf5fe43d72bc4aabc9c76c9ff006e81b.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/4ed7f802f5edf2b7b3ba8dcfc13decac3d07bd2285be11c635e62d4f440b180e.blob', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/60bb5adbcb8f346d870cc555bacf3f236b0c2af0c0d5b9eceb5f3f311bff70d0.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/61a639668b2e4e1b98234a6ac2cf9ab9cc2c5c152444315554c6db948ee2c050.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/73955dc152767970334aef68853915fb28d1fb4b0570033f3850e5652b13e3d7.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/7d8b52e99b020407bd908ca63e7a4d43fcaa965e10805be47d1adf8848036d94.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/8628a1a473daf3c17bae6f48ed1dfd528e3d81a482162218f3bb1345fcf6f989.blob', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/862eb8f25be5297707badc5c1b056f1bb4da5e98b52c8827f9ee1e7afe97d468.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/8efb46edb72d27350474575a9123325593d686bc7045ed5c0396270fa6ac97ae.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/8f59a94d8583f02f04b1df7824a47496de789e12d8a4094affc54a38da0b954c.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/962d832756b0a7bd27b7a364cc389edf8ace7af33236041f6e424c90cf273881.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/9927849edd289e7ce206e0abb06d0908a9cc760d0b3dc749c7961c096e607f18.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/9b40206f122539c7865c3cb2ff1bd808a7a358d00a62774f1528ccd646a1d527.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/a407e2abef03167078857852ef67877be31f1cb1bdf2f4195acb7b26fac9bb4d.blob', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/a66128973140423a4a080e08411dfbb450ee8f1145e7b9342473609d4b5ec299.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/b2161150997749c72ad1e0867a4fcf519ebdbfa07bd526d1faa552eb1f567428.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/b2e9392fd3b68228839cf8959b72abc792474c0515e3e8881a0593946dcae942.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/c2510e4226688cc63bc6ce741c3fd36e65c83b327f65818374bd90f40ce537c6.blob', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/dd59be3c8ef03e98c2078d3c1f3cfcc9d1f511c045a1719a129d3a5f35c03975.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/df8bd6dd8f87540792026dab56ed07c8a77c0b7ec2af1b16c2e821742c6b7b0b.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/e9b2412cae7d2bfaa34a0c33d7d0c693b8fd93435a5caf16c0be6672f485514f.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/ef66b9de63abdb41c735e3f26e17f05a77f92d9c2fd43dc0e9abe85b540340e4.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/f38656fd0e2834d73a86a31606e3285f2c1ac59f5966c9ad1d790e9f5e336702.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/binding_sources/f8d88e1bd0581d28e1d2298bba63499f33fe57f3be0000b8ca66636e72771fe8.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/BODY_RECOVERY_MAP.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/BODY_RECOVERY_MAP.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/CHECKPOINT.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/EVIDENCE_MAP.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/EXPOSURE_AND_SCOPE.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/FREEZE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/METADATA_CHECKS.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/PROVENANCE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/PR_BODY.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/README.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/SEAL_VERIFICATION.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/SOURCE_CAPTURE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/THEOREM_NOTE.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/capture_sources.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/history/original_publication_FREEZE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/history/original_publication_review/REVIEW.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/history/original_publication_review/REVIEW.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/make_manifest.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/run_metadata_checks.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/runs/metadata_checks/EXECUTION.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/runs/metadata_checks/INPUTS_AT_LAUNCH/BODY_RECOVERY_MAP.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/runs/metadata_checks/INPUTS_AT_LAUNCH/EVIDENCE_MAP.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/runs/metadata_checks/INPUTS_AT_LAUNCH/PROVENANCE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/runs/metadata_checks/INPUTS_AT_LAUNCH/SOURCE_CAPTURE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/runs/metadata_checks/INPUTS_AT_LAUNCH/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/runs/metadata_checks/LAUNCHER_AT_LAUNCH.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/runs/metadata_checks/SOURCE_AT_LAUNCH.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/runs/metadata_checks/explicit_source_only.stderr.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/runs/metadata_checks/explicit_source_only.stdout.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/runs/metadata_checks/strict_default.stderr.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/runs/metadata_checks/strict_default.stdout.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/seal_packet.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/control_parent_decision/FINAL_QUALIFICATIONS.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/control_parent_decision/FREEZE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/control_parent_decision/QUALIFIED_ACCEPTANCE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/EXPOSURE.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/FREEZE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/LAUNCH_CONTEXT.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/REVIEW.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/emitted_word_fixture.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/run_fixture.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/runs/attempt_01/EXECUTION.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/runs/attempt_01/launcher_at_launch.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/runs/attempt_01/output/RESULT.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/runs/attempt_01/output/complete_matrices.npz', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/runs/attempt_01/output/logical_word.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/runs/attempt_01/output/mutant_logical_word.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/runs/attempt_01/output/mutant_routed_word.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/runs/attempt_01/output/routed_word.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/runs/attempt_01/output/segments.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/runs/attempt_01/source_at_launch.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/runs/attempt_01/stderr.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/runs/attempt_01/stdout.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/seal_packet.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/sources/control_DERIVATION.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/sources/sparse_DERIVATION.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/emitted_fixture/sources/sparse_FREEZE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/ARTIFACT_INSPECTION.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/CHECKPOINT.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/FREEZE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/REVIEW.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/SEAL_VERIFICATION.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/SOURCE_COVERAGE.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/EXPOSURE.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/FREEZE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/LAUNCH_CONTEXT.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/REVIEW.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/emitted_word_fixture.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/run_fixture.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/runs/attempt_01/EXECUTION.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/runs/attempt_01/launcher_at_launch.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/runs/attempt_01/output/RESULT.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/runs/attempt_01/output/complete_matrices.npz', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/runs/attempt_01/output/logical_word.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/runs/attempt_01/output/mutant_logical_word.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/runs/attempt_01/output/mutant_routed_word.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/runs/attempt_01/output/routed_word.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/runs/attempt_01/output/segments.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/runs/attempt_01/source_at_launch.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/runs/attempt_01/stderr.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/runs/attempt_01/stdout.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/seal_packet.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/sources/control_DERIVATION.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/sources/sparse_DERIVATION.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/fixture_source/sources/sparse_FREEZE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/inspect_artifacts.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/prior_review/FREEZE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/prior_review/REVIEW.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/run_inspection.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/runs/artifact_inspection/EXECUTION.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/runs/artifact_inspection/executed_source.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/runs/artifact_inspection/launcher_source.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/runs/artifact_inspection/stderr', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/runs/artifact_inspection/stdout', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_exposed_review/seal_review.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_root_decision/FINAL_QUALIFICATIONS.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_root_decision/FREEZE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/fixture_root_decision/QUALIFIED_ACCEPTANCE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/AUTHOR_CHECK_AND_EXPOSURE.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/CHECKPOINT.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/DERIVATION.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/FREEZE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/PRECHECK_FINDINGS.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/SOURCE_MANIFEST_INITIAL.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/exact_sparse_check.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/run_exact_check.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/run_exact_check_retry.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/runs/exact_sparse_check/EXECUTION.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/runs/exact_sparse_check/LAUNCHER_AT_LAUNCH.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/runs/exact_sparse_check/SOURCE_AT_LAUNCH.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/runs/exact_sparse_check/stderr.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/runs/exact_sparse_check/stdout.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/runs/exact_sparse_check_retry/EXECUTION.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/runs/exact_sparse_check_retry/LAUNCHER_AT_LAUNCH.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/runs/exact_sparse_check_retry/SOURCE_AT_LAUNCH.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/runs/exact_sparse_check_retry/stderr.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/runs/exact_sparse_check_retry/stdout.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/sources/BAI_MARVIAN_2309.11051v3.pdf', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_author/sources/LOCAL_CONTROL_PARENT.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/CHECKPOINT.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/FREEZE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/PRIMARY_SCOPE.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/REVIEW.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/SEAL_VERIFICATION.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/SOURCE_COVERAGE.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/AUTHOR_CHECK_AND_EXPOSURE.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/CHECKPOINT.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/DERIVATION.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/FREEZE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/PRECHECK_FINDINGS.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/SOURCE_MANIFEST_INITIAL.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/exact_sparse_check.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/run_exact_check.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/run_exact_check_retry.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/runs/exact_sparse_check/EXECUTION.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/runs/exact_sparse_check/LAUNCHER_AT_LAUNCH.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/runs/exact_sparse_check/SOURCE_AT_LAUNCH.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/runs/exact_sparse_check/stderr.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/runs/exact_sparse_check/stdout.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/runs/exact_sparse_check_retry/EXECUTION.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/runs/exact_sparse_check_retry/LAUNCHER_AT_LAUNCH.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/runs/exact_sparse_check_retry/SOURCE_AT_LAUNCH.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/runs/exact_sparse_check_retry/stderr.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/runs/exact_sparse_check_retry/stdout.txt', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/sources/BAI_MARVIAN_2309.11051v3.pdf', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/author_source/sources/LOCAL_CONTROL_PARENT.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/capture_sources.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/run_metadata_capture.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/runs/source_capture/EXECUTION.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/runs/source_capture/executed_source.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/runs/source_capture/launcher_source.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/runs/source_capture/stderr', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/runs/source_capture/stdout', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_exposed_review/seal_packet.py', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_root_decision/FINAL_QUALIFICATIONS.md', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_root_decision/FREEZE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/source/sparse_root_decision/QUALIFIED_ACCEPTANCE.json', '.claude/science/physics-loops/toe-local-conserving-sparse-20261016/frozen_source/verify_provenance.py', 'docs/LOCAL_CONSERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md', 'docs/LOCAL_CONSERVING_SPARSE_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-16.md')
EXPECTED_CANONICAL_REVIEW_SHA = '60bb5adbcb8f346d870cc555bacf3f236b0c2af0c0d5b9eceb5f3f311bff70d0'
EXPECTED_CANONICAL_REVIEW_COMMAND = ('python3', '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/bootstrap/record_sparse_canonical_review_path_recovery.py', 'installed')
EXPECTED_CANONICAL_EXECUTION_SHA = '1921469ba53746b85df3d36febffd3f1213f5c66cf59514825c065232ecbf4b7'
EXPECTED_PREBINDING_PRIMARY = {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/scripts/local_conserving_sparse_2026_10_16.py', 'bytes': 55166, 'sha256': 'c0592bd09d493675515ae478d0ff4ec238646b139afd7d786cfd0e2624ed8738'}
EXPECTED_INTEGRATION_COMMON = {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_sparse_parent_refresh_recovery/local_conserving_sparse_common.py', 'bytes': 56255, 'sha256': '9b40206f122539c7865c3cb2ff1bd808a7a358d00a62774f1528ccd646a1d527'}
PACK = '.claude/science/physics-loops/toe-local-conserving-sparse-20261016'
NOTE = 'docs/LOCAL_CONSERVING_SPARSE_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-16.md'
PRIMARY = 'scripts/local_conserving_sparse_2026_10_16.py'
EXPECTED_GIT_BASE = '98c9eaf1702d74f5f19649f8140e9fbdc83a2345'
EXPECTED_BASE_PR = 9645
EXPECTED_BASE_BRANCH = 'physics-loop/toe-local-conserving-preparation-20261016'
EXPECTED_BASE_PARENT_BRANCH = 'main'
EXPECTED_ROOT_REVIEW_SHA = '9927849edd289e7ce206e0abb06d0908a9cc760d0b3dc749c7961c096e607f18'
EXPECTED_ROOT_REVIEW_COMMAND = ('python3', '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/bootstrap/record_qualified_sparse_source_review.py')
EXPECTED_ROOT_EXECUTION_SHA = '8efb46edb72d27350474575a9123325593d686bc7045ed5c0396270fa6ac97ae'
EXPECTED_ROOT_RECORDER_SHA = 'b2161150997749c72ad1e0867a4fcf519ebdbfa07bd526d1faa552eb1f567428'
EXPECTED_REVIEW_CWD = '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009'
EXPECTED_WORKTREE = '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree'
EXPECTED_REPOSITORY = 'jonathonreilly/qubit-lattice-axiom-framework'
EXPECTED_SOURCE_BODY_PINS = [{'body_id': 'sparse_derivation', 'original_path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_sparse_compiler_candidate/DERIVATION.md', 'packet_path': 'source/sparse_author/DERIVATION.md', 'bytes': 30201, 'sha256': '6b1e1ecd6afcf53dd05411493c18ceb9db258fcc279dc3c24072a516a5a76c3b'}, {'body_id': 'sparse_analytical_review', 'original_path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_sparse_compiler_exposed_check/REVIEW.md', 'packet_path': 'source/sparse_exposed_review/REVIEW.md', 'bytes': 25079, 'sha256': '2af89ecefd2d682259e967cc96ef1f5965c37500de4d3cc9261cb39d50254a2a'}, {'body_id': 'sparse_qualifications', 'original_path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_sparse_compiler_root_review/FINAL_QUALIFICATIONS.md', 'packet_path': 'source/sparse_root_decision/FINAL_QUALIFICATIONS.md', 'bytes': 8609, 'sha256': '83b913c6b47ee8625cc15914759886e642515d02f284dc84a6b92d8e3ed54d3e'}, {'body_id': 'runtime_qualifications', 'original_path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_control_root_review/FINAL_QUALIFICATIONS.md', 'packet_path': 'source/control_parent_decision/FINAL_QUALIFICATIONS.md', 'bytes': 11037, 'sha256': '9fb1514db57464c15de3156916922f405e80e3dc56b6d7624d2e9531b011f305'}, {'body_id': 'fixture_report', 'original_path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_sparse_compiler_fixture/REVIEW.md', 'packet_path': 'source/emitted_fixture/REVIEW.md', 'bytes': 12442, 'sha256': 'c9e99e725b3efd8dabbf551c315e983113129de0ed12d5f9028c207f93fe9649'}, {'body_id': 'fixture_exposed_review', 'original_path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_sparse_fixture_exposed_check/REVIEW.md', 'packet_path': 'source/fixture_exposed_review/REVIEW.md', 'bytes': 21515, 'sha256': 'c1f7a257fbb824d868c3ca25c7ba9fc8d7504f2e532ca83b8851427afdae305d'}, {'body_id': 'fixture_qualifications', 'original_path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_sparse_fixture_root_review/FINAL_QUALIFICATIONS.md', 'packet_path': 'source/fixture_root_decision/FINAL_QUALIFICATIONS.md', 'bytes': 4390, 'sha256': 'e2bf8af1a8c90068c33d833604717762cb1207e008ad52b3c330986cd470a4bc'}]
EXPECTED_PARENT_BINDING = {'kind': 'exact_direct_mathematical_parent_binding', 'direct_canonical_parents': [{'path': 'docs/LOCAL_CONSERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md', 'bytes': 170504, 'sha256': '6db93809f12315668f720006c6a443301ad682381ce5629c173b1ff1c6d66a7f'}], 'git_base': None, 'scope': 'The author fixed-duration local-control argument and its qualifications are in this parent. Existing finite-lift core is transitive; no preparation/runtime composition is newly claimed.'}
EXPECTED_SOURCE_FREEZE = '8f59a94d8583f02f04b1df7824a47496de789e12d8a4094affc54a38da0b954c'
EXPECTED_SOURCE_MAP_SHA = 'ef66b9de63abdb41c735e3f26e17f05a77f92d9c2fd43dc0e9abe85b540340e4'
EXPECTED_SOURCE_MANIFEST_SHA = '0c87d3be9af2418d0de0175251998f83dbc1a3cd46a2b943640410dd81990394'
EXPECTED_SOURCE_VALIDATOR_SHA = 'cd890636262655c771d56dde5273dc8993adafdb2408dd784fbeb611255d97c7'
EXPECTED_CANONICAL_CERTIFICATE_SHA = 'faa9644175e8d1352455317ac82ffa2160891aa988c6f494e29264dd386c0bf9'
EXPECTED_PUBLICATION_STATE_SHA = '1144cfc8580ba543d66b516959404a851437535cf668e1a9b1d04ed46015096c'
EXPECTED_CANONICAL_TRAILER_SHA = 'baf72fc74ff1ff812261324f92da50a6006d9b3d443071b1dc5c56ef9585fbdb'

def verify_bytes(data,row,label):
    require(len(data)==row['bytes'] and sha(data)==row['sha256'],label)

def bound_blob(root,row):
    path=Path(row['path'])
    require(not path.is_absolute() and '..' not in path.parts,'Safe relative evidence path')
    data=(root/path).read_bytes();verify_bytes(data,row,'Input identity mismatch: '+str(path));return data

def execution_evidence(root,evidence,command,source_required):
    receipt=json.loads(bound_blob(root,evidence['execution']))
    require(receipt['exit_code']==0,'Successful captured execution required')
    require(receipt['argv']==list(command),'Actual base observation command' if not source_required else 'Exact review command')
    require(receipt['cwd']==EXPECTED_REVIEW_CWD if source_required else receipt['cwd']==EXPECTED_WORKTREE,'Actual execution cwd')
    require(receipt['start_utc']<=receipt['end_utc'] if 'end_utc' in receipt else receipt['start_utc']<=receipt['finished_utc'],'Actual execution timestamps')
    for field in ['stdout','stderr','recorder']:
        data=bound_blob(root,evidence[field]);verify_bytes(data,receipt[field],'Input identity mismatch: '+field)
    require(bound_blob(root,evidence['stderr'])==b'','Empty captured stderr')
    if source_required:
        data=bound_blob(root,evidence['source'])
        verify_bytes(data,receipt['child_source_at_launch'],'Input identity mismatch: source-at-launch')
        require('source_capture' in receipt,'Explicit captured source required')
        verify_bytes(data,receipt['source_capture'],'Input identity mismatch: captured source')
        require(receipt['argv'][1]==receipt['child_source_at_launch']['path'],'Actual review executable')
        require(receipt['source_capture']['path']!=receipt['child_source_at_launch']['path'],'Distinct original and captured source')
    return json.loads(bound_blob(root,evidence['stdout'])) if command[0]!='git' else bound_blob(root,evidence['stdout']).decode().strip()

def canonical_validate(root):
    require(isinstance(EXPECTED_CANONICAL_REVIEW_SHA,str),'Canonical review is not bound')
    manifest_data=(root/PACK/'INPUT_MANIFEST.json').read_bytes()
    require(sha(manifest_data)==MANIFEST_SHA256,'Input manifest identity')
    manifest=json.loads(manifest_data);rows=manifest['inputs']
    require(len(rows)==len({r['path'] for r in rows}),'Unique input membership')
    require(set(AUDIT_INPUT_PATHS)=={r['path'] for r in rows}|{PACK+'/INPUT_MANIFEST.json'},'Declared audit input membership')
    for row in rows:bound_blob(root,row)
    load=lambda name:json.loads((root/PACK/name).read_bytes())
    actual=load('ACTUAL_BINDING.json');note=(root/NOTE).read_bytes();mapping=load('BODY_MAP.json')
    require(actual['root_read_complete'] is True and actual['canonical_parent_binding_complete'] is True,'Actual canonical review required')
    require(actual['note_sha256']==sha(note) and actual['git_base']==EXPECTED_GIT_BASE,'Actual note/base linkage')
    require(actual['new_scientific_execution'] is False and actual['retained_audit'] is False,'No scientific status promotion')
    require(load('PARENT_BINDING.json')==EXPECTED_PARENT_BINDING==actual['parent_binding'],'Exact parent binding')
    for parent in EXPECTED_PARENT_BINDING['direct_canonical_parents']:bound_blob(root,parent)
    require(actual['source_body_pins']==EXPECTED_SOURCE_BODY_PINS,'Original body-map identity')
    require(actual['raw_bodies']==mapping['bodies'],'Canonical body identity')
    require(len(mapping['bodies'])==7,'Seven canonical bodies')
    for row,old in zip(mapping['bodies'],EXPECTED_SOURCE_BODY_PINS):
        require(row['body_id']==old['body_id'] and row['sha256']==old['sha256'],'Canonical body identity')
        body=note[row['start_byte']:row['end_byte_exclusive']]
        require(len(body)==row['bytes'] and sha(body)==row['sha256'] and note.count(body)==1,'Canonical body identity')
    trailer=mapping['trailer'];tail=note[trailer['start_byte']:trailer['end_byte_exclusive']]
    require(trailer['start_byte']==mapping['bodies'][-1]['end_byte_exclusive'] and trailer['end_byte_exclusive']==len(note),'Canonical closing wrapper interval')
    require(len(tail)==trailer['bytes'] and sha(tail)==trailer['sha256']==EXPECTED_CANONICAL_TRAILER_SHA,'Canonical closing wrapper identity')
    require(actual['source_proposal_freeze']['sha256']==EXPECTED_SOURCE_FREEZE,'Exact source proposal freeze')
    freeze=json.loads(bound_blob(root,actual['source_proposal_freeze']))
    require(freeze['scientific_executions']==0 and freeze['canonical_binding'] is None,'Original source-only scope')
    require(sha((root/PACK/'frozen_source/FREEZE.json').read_bytes())==EXPECTED_SOURCE_FREEZE,'Exact frozen source inventory')
    original_note=bound_blob(root,actual['source_draft_note'])
    original_map=bound_blob(root,actual['source_draft_body_map'])
    require(sha(original_map)==EXPECTED_SOURCE_MAP_SHA,'Exact source body-map identity')
    require(json.loads(original_map)['immutable_bodies']==EXPECTED_SOURCE_BODY_PINS,'Original body-map identity')
    original_manifest=bound_blob(root,actual['source_draft_manifest'])
    require(sha(original_manifest)==EXPECTED_SOURCE_MANIFEST_SHA,'Exact source manifest identity')
    expected_manifest={'kind':'canonical_body_recovery','source_packet_freeze':EXPECTED_SOURCE_FREEZE,
        'current_body_recovery_intervals':[dict(note=NOTE,**row) for row in mapping['bodies']]}
    require(load('SOURCE_MANIFEST.json')==expected_manifest,'Canonical recovery interval')
    require(sha((root/PACK/'CLAIM_STATUS_CERTIFICATE.md').read_bytes())==EXPECTED_CANONICAL_CERTIFICATE_SHA,'Canonical certificate identity')
    require(sha((root/PACK/'PUBLICATION_STATE.json').read_bytes())==EXPECTED_PUBLICATION_STATE_SHA,'Historical publication state')
    original_provenance=bound_blob(root,actual['source_draft_provenance'])
    require(original_provenance==(root/PACK/'frozen_source/PROVENANCE.json').read_bytes(),'Original source provenance')
    verify(root/PACK/'frozen_source')
    review_bytes=bound_blob(root,actual['root_review_evidence']['review'])
    require(sha(review_bytes)==EXPECTED_ROOT_REVIEW_SHA,'Exact root review identity');review=json.loads(review_bytes)
    require(review['source_freeze']['sha256']==EXPECTED_SOURCE_FREEZE and review['immutable_bodies']==7,'Actual source-review linkage')
    require(review['root_read_complete'] is True and review['source_manifest']['sha256']==EXPECTED_SOURCE_MANIFEST_SHA,'Actual source-review body/manifest linkage')
    require(review['source_validator']['sha256']==EXPECTED_SOURCE_VALIDATOR_SHA,'Actual source-review validator linkage')
    verify_bytes(original_note,review['source_note'],'Reviewed source note')
    require(review['scientific_executions']==0 and review['actual_canonical_acceptance'] is None and review['retained_audit'] is False,'Original source-review scope')
    observed=execution_evidence(root,actual['root_review_evidence'],EXPECTED_ROOT_REVIEW_COMMAND,True)
    require(observed['review']['sha256']==EXPECTED_ROOT_REVIEW_SHA and observed['review']['bytes']==len(review_bytes),'Actual review output linkage')
    verify_bytes(bound_blob(root,actual['root_review_evidence']['freeze']),observed['freeze'],'Actual review freeze linkage')
    verify_bytes(bound_blob(root,actual['root_review_evidence']['review_text']),review['review'],'Actual review prose linkage')
    require(sha(bound_blob(root,actual['root_review_evidence']['execution']))==EXPECTED_ROOT_EXECUTION_SHA,'Exact source-review execution identity')
    require(sha(bound_blob(root,actual['root_review_evidence']['recorder']))==EXPECTED_ROOT_RECORDER_SHA,'Exact source-review recorder identity')
    evidence=actual['canonical_review_evidence'];raw=bound_blob(root,evidence['review'])
    require(sha(raw)==EXPECTED_CANONICAL_REVIEW_SHA,'Exact canonical review identity');canonical=json.loads(raw)
    require(canonical['root_read_complete'] is True and canonical['bound_note_sha256']==sha(note),'Actual canonical note review')
    require(canonical['canonical_body_pins']==mapping['bodies'] and canonical['parent_binding']==EXPECTED_PARENT_BINDING,'Actual canonical body/parent review')
    require(canonical['source_draft_freeze_sha256']==EXPECTED_SOURCE_FREEZE and canonical['source_draft_review_sha256']==EXPECTED_ROOT_REVIEW_SHA,'Canonical source linkage')
    require(canonical['git_base']==EXPECTED_GIT_BASE and canonical['prebinding_primary']==EXPECTED_PREBINDING_PRIMARY and canonical['integration_common']==EXPECTED_INTEGRATION_COMMON,'Canonical implementation linkage')
    observed=execution_evidence(root,evidence,EXPECTED_CANONICAL_REVIEW_COMMAND,True)
    require(observed['review']['sha256']==EXPECTED_CANONICAL_REVIEW_SHA,'Canonical review operation linkage')
    require(sha(bound_blob(root,evidence['execution']))==EXPECTED_CANONICAL_EXECUTION_SHA,'Exact canonical execution identity')
    local=json.loads(bound_blob(root,actual['base_observation']))
    require(local['observed_commit']==EXPECTED_GIT_BASE and local['source_revision_verified'] is True,'Actual local base identity')
    require(execution_evidence(root,local['execution_evidence'],('git','rev-parse','HEAD'),False)==EXPECTED_GIT_BASE,'Actual local HEAD linkage')
    command=('gh','pr','view',str(EXPECTED_BASE_PR),'--repo',EXPECTED_REPOSITORY,'--json','number,state,isDraft,headRefOid,headRefName,baseRefName,url')
    base=execution_evidence(root,actual['parent_pr_observation'],command,False)
    require(base['number']==EXPECTED_BASE_PR and base['headRefOid']==EXPECTED_GIT_BASE and base['headRefName']==EXPECTED_BASE_BRANCH and base['baseRefName']==EXPECTED_BASE_PARENT_BRANCH,'Actual base PR identity')
    require(base['state'] in ('OPEN','MERGED') and base['isDraft'] is False,'Regular actual base PR')
    paths={actual[k]['path'] for k in ['source_proposal_freeze','source_draft_body_map','source_draft_note','source_draft_manifest','source_draft_provenance','base_observation']}
    for group in ['root_review_evidence','canonical_review_evidence','parent_pr_observation']:
        paths.update(r['path'] for r in actual[group].values())
    paths.update(r['path'] for r in local['execution_evidence'].values())
    require(set(actual['receipt_paths'])==paths and len(actual['receipt_paths'])==len(paths),'Exact binding evidence membership')
    return {'result':'source_integrity_verified','scope':'Exact source/body/review/base/receipt provenance only',
            'scientific_programs_run_this_primary':0,'historical_programs_replayed':0,'mathematics_or_retention_certified':False}

def main():
    parser=argparse.ArgumentParser(description='Sparse compiler provenance primary; no scientific execution')
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--source-only',action='store_true')
    args=parser.parse_args();root=args.root.resolve()
    if args.source_only:
        print(json.dumps({'source_only':verify(root),'canonical_certification':False},sort_keys=True));return 0
    report=canonical_validate(root);print(json.dumps(report,sort_keys=True))
    print('per_element: positive reserves, full SWAP and actual phase corrections remain supplied')
    print('per_site: literal equal-gap old K and all-site connected-path access remain explicit')
    print('per_mode: fixed-q laboratory count does not bound classical compiler time or memory')
    print('per_block: complete complement, determinant phase, ancilla and reference outputs retained')
    print('lattice_wide: one qualified floating fixture; no interval certificate, physical test or retained audit')
    return 0

if __name__ == "__main__":sys.exit(main())
