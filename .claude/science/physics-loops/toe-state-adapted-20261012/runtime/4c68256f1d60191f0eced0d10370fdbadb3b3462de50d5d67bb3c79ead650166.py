#!/usr/bin/env python3
"""Refresh exact source identities, then seal a completed review without science."""
import datetime
import hashlib
import json
from pathlib import Path

E = Path(__file__).resolve().parent
S = E.parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


rows = []


def check(path, expected, group):
    actual = digest(path)
    rows.append({'group': group, 'path': str(path), 'expected_sha256': expected,
                 'actual_sha256': actual, 'match': actual == expected})


anchors = {
    E / 'NEUTRAL_PLAN.md': '308f4e46581c07a2fedd4cb094c92403211aa61731bdd751f734b7d428b6a728',
    E / 'PRE_EXECUTION_SEAL.json': '5df55a08aa0e8416de0f8f86162034a7dbf63edc59ba54fd1debae6e9c9a75d9',
    E / 'INDEPENDENT_CHECKS_SEAL.json': 'a1fa9a76914840e2acc86f965a76c76e5c37ebfed27292c9bd9fe6df754ef426',
    S / 'STATE_ADAPTED_REFINEMENT_PROBE.md': '459868fcd7f80fa3063c9e7f7a6d62df393eb80f2edc72b221ecda533ba2a971',
    S / 'state_adapted_refinement/final_manifest.json': '8c670592a1dc131492ed0b464c6da23d1cf3da5b51d8ed6855687193af8d783e',
    S / 'state_adapted_control_repair/execution_manifest.json': 'e3a8d8339220c6489c4921b436abddfcfed9cf7ad2b7e3d6c8c6a4ed0aa1bd04',
    E / 'REPAIR_SOURCE_REVIEW.json': 'b0c60e8fb562dc2c6c542d7bc6bb1b0b5bb1987005fa52997e2f1a892ed53190',
    E / 'REPAIR_EVIDENCE_VERIFICATION.json': 'a4bc48ff234556b7f28abc21d6eb0ba4a8d2e67ff19105c959374ba8a233df67',
    E / 'INTEGRITY_EXECUTION_SEAL.json': '5c67601650f2ec1bebc0cd479aafcdbbf1d35956947b2f3e6e5eb475611e4e9d',
    E / 'INTEGRITY_RESULT_SEAL.json': 'a6e1e00b8485aabfab00642095d1dc97d7da6d89a815cd23acd8af48baa6fbf9',
}
for path, expected in anchors.items():
    check(path, expected, 'external_anchor')

for record in json.loads((E / 'SOURCE_READINESS.json').read_text())['sources']:
    path = Path(record['path'])
    if path.name != 'STATE_ADAPTED_REFINEMENT_PROBE.md':
        check(path, record['expected_sha256'], 'current_parent')

for name in ['PRE_EXECUTION_SEAL.json', 'INDEPENDENT_CHECKS_SEAL.json',
             'INTEGRITY_EXECUTION_SEAL.json', 'INTEGRITY_RESULT_SEAL.json']:
    for rel, expected in json.loads((E / name).read_text())['files'].items():
        check(E / rel, expected, name)

for manifest in [S / 'state_adapted_refinement/final_manifest.json',
                 S / 'state_adapted_control_repair/execution_manifest.json']:
    for path, expected in json.loads(manifest.read_text())['files'].items():
        check(Path(path), expected, str(manifest.relative_to(S)))

for rel, expected in json.loads((E / 'REPAIR_EVIDENCE_VERIFICATION.json').read_text())['repair_snapshot_files'].items():
    check(S / 'state_adapted_control_repair' / rel, expected, 'current_repair_evidence')
    check(E / 'repair_final' / rel, expected, 'repair_snapshot')

for record in json.loads((E / 'AUTHOR_FINAL_SOURCE_VERIFICATION.json').read_text())['files']:
    check(E / 'author_final' / record['relative_path'], record['expected_sha256'], 'author_snapshot')

prefix_ok = (S / 'STATE_ADAPTED_REFINEMENT_PROBE.md').read_bytes().startswith((E / 'frozen_sources/STATE_ADAPTED_REFINEMENT_PROBE.md').read_bytes())
refresh = {'checked_utc': utc(), 'all_identities_match': all(x['match'] for x in rows),
           'final_target_has_exact_original_core_prefix': prefix_ok,
           'checks': rows, 'scientific_execution': False}
refresh_path = E / 'FINAL_SOURCE_REFRESH.json'
assert not refresh_path.exists(), 'Preserve prior refresh; use a separately named attempt if needed'
refresh_path.write_text(json.dumps(refresh, indent=2) + '\n')
if not refresh['all_identities_match'] or not prefix_ok:
    raise SystemExit('Final source mismatch; refresh record preserved, no review seal created')

report = S / 'STATE_ADAPTED_REFINEMENT_REVIEW.md'
excluded = {'FINAL_REVIEW_MANIFEST.json', 'FINAL_REVIEW_RECEIPT.json'}
paths = [report] + [p for p in sorted(E.rglob('*')) if p.is_file() and p.name not in excluded]
manifest = {'sealed_utc': utc(), 'scope': 'Completed conditional source review; not a formal retained verdict',
            'excluded_self_reference': sorted(excluded),
            'files': {str(p.relative_to(S)): digest(p) for p in paths}}
manifest_path = E / 'FINAL_REVIEW_MANIFEST.json'
assert not manifest_path.exists()
manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
receipt = {'completed_utc': utc(), 'fixed_deadline_utc': '2026-10-12T16:00:52+00:00',
           'review_path': str(report), 'review_sha256': digest(report),
           'manifest_path': str(manifest_path), 'manifest_sha256': digest(manifest_path),
           'manifest_members': len(paths), 'source_identity_checks': len(rows),
           'source_refresh_path': str(refresh_path), 'source_refresh_sha256': digest(refresh_path),
           'all_source_identities_match': True, 'core_prefix_unchanged': True,
           'material_mathematical_or_scope_findings': 0,
           'recorder_limitation': 'Child exit is recorded but not propagated; copied exit-7 fixture survives outer exit-only inspection.',
           'original_independent_evidence_seal_sha256': anchors[E / 'INDEPENDENT_CHECKS_SEAL.json'],
           'author_original_baseline': {'passed': 85, 'failed': 1, 'exit_code': 1},
           'separate_corrected_baseline': {'passed': 86, 'failed': 0, 'exit_code': 0},
           'formal_retained_verdict': None, 'editable_prompt_files_changed': [],
           'git_or_worktree_mutations': False, 'scientific_reruns_after_original_seal': False,
           'non_scientific_packaging_correction': 'An initial report apply_patch was rejected for duplicate delete/add target; it changed no file. A subsequent update patch succeeded. No scientific source or result was altered.'}
assert datetime.datetime.fromisoformat(receipt['completed_utc']) < datetime.datetime.fromisoformat(receipt['fixed_deadline_utc'])
(E / 'FINAL_REVIEW_RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
