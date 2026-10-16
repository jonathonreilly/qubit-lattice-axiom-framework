#!/usr/bin/env python3
"""Write the final controlling metadata once; no science or integration action."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def info(rel):
    raw = (ROOT / rel).read_bytes()
    return {'packet_path': rel, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

def put(name, value):
    with (ROOT / name).open('x') as f:
        f.write(json.dumps(value, indent=2) + '\n')

capture = json.loads((ROOT / 'SOURCE_CAPTURE.json').read_text())
provenance = {
    'kind': 'source_only_qualified_sparse_publication_proposal',
    'primary_status': 'UNBOUND',
    'mathematical_disposition': 'QUALIFIED_CONDITIONAL_ANALYTICAL_SUPPORT',
    'fixture_disposition': 'QUALIFIED_SINGLE_NUMERICAL_FIXTURE_AND_SAVED_ARTIFACT_INSPECTION',
    'actual_git_base': None, 'canonical_parent': None, 'canonical_binding': None,
    'canonical_acceptance': None, 'current_wrapper_review': None, 'publication': None,
    'retained_audit': False, 'rigorous_fixture_residual_certificate': False,
    'independent_fixture_propagation': False,
    'scientific_executions': 0, 'integration_driver': None,
    'editable_prompt_files_changed': [], 'physical_axioms_changed': [],
    'source_decisions': {
        'sparse_acceptance': info('source/sparse_root_decision/QUALIFIED_ACCEPTANCE.json'),
        'sparse_qualifications': info('source/sparse_root_decision/FINAL_QUALIFICATIONS.md'),
        'runtime_acceptance': info('source/control_parent_decision/QUALIFIED_ACCEPTANCE.json'),
        'runtime_qualifications': info('source/control_parent_decision/FINAL_QUALIFICATIONS.md'),
        'fixture_acceptance': info('source/fixture_root_decision/QUALIFIED_ACCEPTANCE.json'),
        'fixture_qualifications': info('source/fixture_root_decision/FINAL_QUALIFICATIONS.md'),
    },
    'historical_wrapper_review_only': info('history/original_publication_review/REVIEW.json'),
    'historical_draft_seal_only': info('history/original_publication_FREEZE.json'),
    'qualification': 'Source decisions authorize only their stated scopes. No current wrapper, canonical, physical, retained or publication acceptance is inferred.',
}
put('PROVENANCE.json', provenance)

evidence = []
for name, base, schema, source, launcher, stdout, stderr, expected in [
    ('sparse_preexec_failure', 'source/sparse_author/runs/exact_sparse_check', 'sparse_flat', 'SOURCE_AT_LAUNCH.py', 'LAUNCHER_AT_LAUNCH.py', 'stdout.txt', 'stderr.txt', None),
    ('sparse_exact_retry', 'source/sparse_author/runs/exact_sparse_check_retry', 'sparse_flat', 'SOURCE_AT_LAUNCH.py', 'LAUNCHER_AT_LAUNCH.py', 'stdout.txt', 'stderr.txt', 0),
    ('emitted_fixture_propagation', 'source/emitted_fixture/runs/attempt_01', 'fixture_nested', 'source_at_launch.py', 'launcher_at_launch.py', 'stdout.txt', 'stderr.txt', 0),
    ('fixture_saved_artifact_inspection', 'source/fixture_exposed_review/runs/artifact_inspection', 'inspection_flat', 'executed_source.py', 'launcher_source.py', 'stdout', 'stderr', 0),
]:
    evidence.append({'id': name, 'schema': schema, 'expected_exit': expected,
                     'receipt': info(base + '/EXECUTION.json'),
                     'source': info(base + '/' + source), 'launcher': info(base + '/' + launcher),
                     'stdout': info(base + '/' + stdout), 'stderr': info(base + '/' + stderr)})
outputs = ['RESULT.json', 'segments.json', 'logical_word.json', 'routed_word.json',
           'mutant_logical_word.json', 'mutant_routed_word.json', 'complete_matrices.npz']
put('EVIDENCE_MAP.json', {
    'actual_historical_executions': evidence,
    'full_fixture_outputs': [info('source/emitted_fixture/runs/attempt_01/output/' + x) for x in outputs],
    'new_scientific_executions': 0,
    'limits': 'One exact algebra retry after a preexec failure; one complex128 compiler propagation; one exact structural inspection plus floating saved-array reanalysis. No independent second propagation or interval certificate.',
})

payload = ['README.md', 'THEOREM_NOTE.md', 'PR_BODY.md', 'EXPOSURE_AND_SCOPE.md',
           'BODY_RECOVERY_MAP.md', 'BODY_RECOVERY_MAP.json', 'SOURCE_CAPTURE.json',
           'PROVENANCE.json', 'EVIDENCE_MAP.json', 'capture_sources.py',
           'make_manifest.py', 'verify_provenance.py', 'run_metadata_checks.py', 'seal_packet.py']
put('SOURCE_MANIFEST.json', {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'kind': 'exact_selected_source_and_current_payload_manifest',
    'closures': capture['closures'], 'source_closure': capture['source_closure'],
    'history_records': capture['history_records'],
    'packet_payload': [info(x) for x in payload],
    'body_recovery_map': 'BODY_RECOVERY_MAP.json',
    'scope': 'Seven immediate source freezes plus three history records; no recursive publication archive or historical citation closure.',
    'final_seal_controls': ['SOURCE_MANIFEST.json', 'runs/metadata_checks/', 'METADATA_CHECKS.md',
                            'SEAL_VERIFICATION.json', 'CHECKPOINT.md'],
    'self_hash_rule': 'Manifest cannot contain its own hash. Final FREEZE.json covers it and every other file except that exact root seal.',
    'primary_status': 'UNBOUND', 'scientific_executions': 0,
})
print(json.dumps({'source_files': len(capture['source_closure']), 'history_records': len(capture['history_records']),
                  'current_payload_files': len(payload), 'controlling_manifest_written_once': True,
                  'primary_status': 'UNBOUND', 'scientific_executions': 0}, indent=2))
