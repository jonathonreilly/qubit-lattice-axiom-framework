#!/usr/bin/env python3
"""Refresh selected originals, inspect metadata evidence, and seal once.

Imports only this packet's read-only METADATA verifier, never scientific source.
No Git/integration/publication action. Final verification returns to the caller;
there is no post-seal write or unlisted output file.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

import verify_provenance as verifier

ROOT = Path(__file__).resolve().parent

def info(path):
    raw = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

def new_json(name, value):
    with (ROOT / name).open('x') as f:
        f.write(json.dumps(value, indent=2) + '\n')

def main():
    if (ROOT / 'FREEZE.json').exists():
        raise RuntimeError('Already frozen; refusing mutation')
    initial = verifier.verify(ROOT)
    manifest = json.loads((ROOT / 'SOURCE_MANIFEST.json').read_text())
    refreshed = 0
    for row in manifest['source_closure'] + manifest['history_records']:
        raw = Path(row['original_path']).read_bytes()
        if len(raw) != row['bytes'] or hashlib.sha256(raw).hexdigest() != row['sha256']:
            raise RuntimeError('Original changed: ' + row['original_path'])
        refreshed += 1
    run = ROOT / 'runs/metadata_checks'
    receipt = json.loads((run / 'EXECUTION.json').read_text())
    if not (receipt['observed_expected_exits'] and receipt['inputs_unchanged_after']
            and receipt['executable_source_unchanged_after']):
        raise RuntimeError('Metadata execution did not complete as declared')
    def receipt_file(row):
        path = Path(row['path'])
        if ROOT not in path.resolve().parents:
            raise RuntimeError('Unexpected receipt path')
        raw = path.read_bytes()
        if len(raw) != row['bytes'] or hashlib.sha256(raw).hexdigest() != row['sha256']:
            raise RuntimeError('Metadata receipt identity mismatch')
    for key in ['source', 'launcher']:
        receipt_file(receipt[key])
    if (run / 'SOURCE_AT_LAUNCH.py').read_bytes() != (ROOT / 'verify_provenance.py').read_bytes():
        raise RuntimeError('Executed source changed')
    if (run / 'LAUNCHER_AT_LAUNCH.py').read_bytes() != (ROOT / 'run_metadata_checks.py').read_bytes():
        raise RuntimeError('Executed launcher changed')
    for row in receipt['inputs_at_launch']:
        receipt_file(row['original'])
        receipt_file(row['snapshot'])
        if Path(row['original']['path']).read_bytes() != Path(row['snapshot']['path']).read_bytes():
            raise RuntimeError('Metadata input snapshot mismatch')
    observed = []
    for row in receipt['invocations']:
        receipt_file(row['stdout'])
        receipt_file(row['stderr'])
        stdout = json.loads(Path(row['stdout']['path']).read_text())
        if Path(row['stderr']['path']).read_bytes() != b'':
            raise RuntimeError('Nonempty metadata stderr')
        expected_status = 'UNBOUND' if row['name'] == 'strict_default' else 'SOURCE_CLOSURE_VERIFIED'
        if stdout['status'] != expected_status or row['exit_code'] != row['expected_exit']:
            raise RuntimeError('Unexpected actual metadata result')
        observed.append({'name': row['name'], 'exit_code': row['exit_code'], 'status': stdout['status']})
    new_json('SEAL_VERIFICATION.json', {
        'kind': 'actual_preseal_metadata_and_original_refresh',
        'utc': datetime.now(timezone.utc).isoformat(), 'source_verifier_result': initial,
        'original_files_refreshed': refreshed, 'metadata_receipt': info(run / 'EXECUTION.json'),
        'actual_invocations': observed, 'metadata_input_snapshots_match': True,
        'scientific_executions': 0, 'all_historical_source_bytes_unchanged': True,
        'postseal_result_location': 'Returned by seal_packet.py to caller; no post-seal packet write.'})
    with (ROOT / 'CHECKPOINT.md').open('x') as f:
        f.write('# Final source-packet checkpoint\n\n')
        f.write('The new current wrapper and seven complete immutable bodies are assembled. The mathematical and fixture qualified decisions remain separate. All 131 selected source files plus three history records were rechecked against their originals immediately before sealing. The actual metadata invocations returned default UNBOUND/exit 2 and explicit source-only/exit 0; full sources, input snapshots, argv, limits and streams are retained. No scientific run or saved-matrix reanalysis occurred.\n\n')
        f.write('This checkpoint is written immediately before the final seal; the presence and validity of `FREEZE.json` establishes completion. The final validator requires its member list to equal the entire actual file inventory except the exact root seal itself. The sealer returns the post-seal result without writing an unlisted file.\n\n')
        f.write('Primary status remains UNBOUND. Actual Git base, current canonical parent/binding/acceptance, current wrapper review and publication remain null. Root owns subsequent review and integration. The old draft and every historical pending statement are unchanged. No integration driver, other-chat message, Git/canonical/audit/cache/graph/lock/prompt/axiom mutation is part of this deliverable.\n')
    members = [info(ROOT / rel) for rel in sorted(verifier.inventory(ROOT))]
    new_json('FREEZE.json', {
        'kind': 'source_only_qualified_sparse_publication_freeze',
        'frozen_utc': datetime.now(timezone.utc).isoformat(), 'primary_status': 'UNBOUND',
        'members': members, 'member_count': len(members),
        'exact_excluded_root_paths': ['FREEZE.json'],
        'source_files': len(manifest['source_closure']), 'immutable_bodies': 7,
        'scientific_executions': 0, 'retained_audit': False,
        'actual_git_base': None, 'canonical_parent': None, 'canonical_binding': None,
        'canonical_acceptance': None, 'current_wrapper_review': None, 'publication': None,
        'sealer_argv': sys.argv, 'sealer_cwd': str(Path.cwd()),
        'qualification': 'Byte closure only. Complete current wrapper requires a separate root review; science evidence remains qualified as in unchanged bodies.'})
    final = verifier.verify(ROOT)
    print(json.dumps({'final_freeze': info(ROOT / 'FREEZE.json'), 'final_read_only_verification': final,
                      'postseal_writes': 0, 'source_or_science_replays': 0}, indent=2), flush=True)

if __name__ == '__main__':
    main()
