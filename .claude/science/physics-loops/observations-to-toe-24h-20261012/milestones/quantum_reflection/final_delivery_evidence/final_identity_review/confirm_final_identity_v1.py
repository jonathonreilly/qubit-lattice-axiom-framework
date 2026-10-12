#!/usr/bin/env python3
"""Read-only Git/file identity checks; no scientific code or pipeline execution."""
import base64
import datetime as dt
import difflib
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path('/Users/jonBridger/.codex/worktrees/quantum-reflection-20261012/New Axioms Lets Go')
PACK = ROOT / '.claude/science/physics-loops/quantum-reflection-milestone-20261012'
OUT = Path(__file__).resolve().parent
BASE = '516cb69d8487ff04f8a48e065d3dcbe71d7dd237'
ORIGINAL = '0a2ce9ac6d0d1647c24b54bcb95e23136ff6c0f6'
FINAL = '8148be1c698f7c9b3bee8a6a659ec352adbbbdbb'
TREE = 'db5bdc4b10aeb285c0576df770948e4e8c9ad460'


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha(path):
    return sha_bytes(Path(path).read_bytes())


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def reference(path):
    path = Path(path)
    return {'path': str(path.resolve()), 'sha256': sha(path)}


def main():
    assert git('rev-parse', 'HEAD').decode().strip() == FINAL
    assert git('rev-parse', FINAL + '^{tree}').decode().strip() == TREE
    subprocess.run(['git', 'merge-base', '--is-ancestor', BASE, ORIGINAL], cwd=ROOT, check=True)
    subprocess.run(['git', 'merge-base', '--is-ancestor', ORIGINAL, FINAL], cwd=ROOT, check=True)
    old_report = PACK / 'independent_review/REVIEW.md'
    old_receipt = PACK / 'independent_review/REVIEW_RECEIPT_v1.json'
    assert sha(old_report) == 'fcf18ec44654fe4483ea852fc73f7b1f817e5efda4f9454f4d2b3e8d1077d80c'
    assert sha(old_receipt) == '3492f3b9b1a01c48f029231a82985dcb8a642ad5970fdbe508075fc44c713b57'
    previous = json.loads(old_receipt.read_text())
    assert previous['constituent']['head'] == ORIGINAL
    scientific = previous['source_identities']
    assert len(scientific) == 4
    for row in scientific:
        path, digest = row['path'], row['sha256']
        original_bytes = git('show', ORIGINAL + ':' + path)
        final_bytes = git('show', FINAL + ':' + path)
        assert original_bytes == final_bytes == (ROOT / path).read_bytes()
        assert sha_bytes(final_bytes) == digest

    final_delta = []
    for line in git('diff', '--name-status', '--no-renames', BASE, FINAL).decode().splitlines():
        status, path = line.split('\t')
        data = git('show', FINAL + ':' + path)
        assert data == (ROOT / path).read_bytes()
        final_delta.append({'path': path, 'sha256': sha_bytes(data), 'change': status})
    added = git('diff', '--name-status', '--no-renames', ORIGINAL, FINAL).decode().splitlines()
    assert len(final_delta) == 28 and len(added) == 24
    for line in added:
        status, path = line.split('\t')
        assert status == 'A' and path.startswith(str(PACK.relative_to(ROOT)) + '/')

    metadata = []
    deltas = []
    changed_names = {'CLAIM_STATUS_CERTIFICATE.md', 'HANDOFF.md', 'REVIEW_HISTORY.md'}
    for row in previous['metadata_read']:
        old_path = Path(row['path'])
        current = PACK / old_path.name
        if current.name in changed_names:
            recovery = PACK / 'evidence' / ('SOURCE_FREEZE_' + current.name)
            assert sha(recovery) == row['sha256']
            delta = ''.join(difflib.unified_diff(
                recovery.read_text().splitlines(keepends=True),
                current.read_text().splitlines(keepends=True),
                fromfile=str(recovery.relative_to(ROOT)),
                tofile=str(current.relative_to(ROOT))))
            assert delta
            deltas.append(delta)
        else:
            recovery = current
            assert sha(current) == row['sha256']
        metadata.append({'original_path': str(old_path), 'original_sha256': row['sha256'],
                         'preserved_snapshot': reference(recovery),
                         'current_path': str(current.relative_to(ROOT)),
                         'current_sha256': sha(current),
                         'semantic_disposition': 'No changed scientific premise or claim; current review/validation status or unchanged task context.'})

    # Validate all immutable current-review execution/evidence references without running them.
    for row in previous['review_references']:
        assert sha(row['path']) == row['sha256']

    archive_path = PACK / 'evidence/ARCHIVAL_CACHE_v1.json'
    archive = json.loads(archive_path.read_text())
    decoded = base64.b64decode(archive['base64'], validate=True)
    raw_path = Path(archive['original_local_path'])
    assert archive['format'] == 'base64_exact_original_bytes_v1'
    assert archive['sha256'] == '29db3aee21fdde48149f1384d1666744371a89784a858e5bb2601272c4ecad62'
    assert sha_bytes(decoded) == archive['sha256']
    assert decoded == raw_path.read_bytes() and len(decoded) == 3622
    assert decoded.endswith(b'\n\n')
    assert any(row['path'] == str(raw_path) and row['sha256'] == archive['sha256']
               for row in previous['review_references'])
    assert not git('ls-tree', '-r', '--name-only', FINAL, str(raw_path.relative_to(ROOT))).strip()
    cache_mapping = {'archive': reference(archive_path), 'original_path': str(raw_path),
                     'original_sha256': archive['sha256'], 'decoded_sha256': sha_bytes(decoded),
                     'decoded_bytes': len(decoded), 'decoded_equals_original_local_bytes': True,
                     'terminal_blank_line_preserved': True, 'raw_txt_in_final_tree': False,
                     'recovery': 'Strict base64 decoding of ARCHIVAL_CACHE_v1.json field base64 restores the exact historical bytes. It is not the current canonical cache.'}

    validation_path = PACK / 'evidence/validation_science_v1/RESULTS_v1.json'
    validation = json.loads(validation_path.read_text())
    assert validation['base'] == BASE and validation['commit'] == ORIGINAL
    assert validation['tree'] == '8069c8dfe91c5ce189373c22c5bbcf90e3e498de'
    validation_refs = [reference(validation_path)]
    for row in validation['results']:
        local = validation_path.parent / Path(row['log']).name
        assert row['exit'] == 0
        assert sha(local) == sha(row['log']) == row['sha256']
        validation_refs.append(reference(local))
    logs = [(validation_path.parent / ('gate-' + str(i) + '_v1.log')).read_text()
            for i in (1, 2, 3)]
    assert 'Pipeline complete.' in logs[0]
    assert 'OK: no errors' in logs[0] and 'OK: no errors' in logs[1]
    evidence = json.loads(logs[2])
    assert not evidence['failures'] and not evidence['control_failures']
    assert len(evidence['checked']) == 1 and evidence['checked'][0]['forensic_evidence_ready']

    assert git('rev-parse', 'HEAD').decode().strip() == FINAL
    for row in final_delta:
        assert sha(ROOT / row['path']) == row['sha256']
    result = {
        'schema': 'same_session_final_identity_confirmation_v1',
        'at': dt.datetime.now(dt.timezone.utc).isoformat(),
        'reviewer_session': '/root/direct_quantum_visibility_review',
        'confirmation': 'PASS_identity_and_metadata_scope',
        'base': BASE, 'original_scientific_commit': ORIGINAL,
        'final_commit': FINAL, 'final_tree': TREE,
        'scientific_sources_unchanged': scientific,
        'final_source_refs': final_delta,
        'original_dispositions': previous['original_dispositions'],
        'prior_source_report': reference(old_report), 'prior_source_receipt': reference(old_receipt),
        'metadata_mappings': metadata, 'complete_metadata_delta': deltas,
        'archival_cache_mapping': cache_mapping,
        'validation_evidence': validation_refs,
        'validation_scope': validation['scope'],
        'saved_scientific_tree_gate_exits': [row['exit'] for row in validation['results']],
        'saved_logs_include_nonfatal_warnings_and_notices': True,
        'material_semantic_issues': [],
        'limits': ['Same-session source judgment carries forward because the four scientific files are byte-identical.',
                   'Existing saved validation concerns scientific tree 8069c8dfe91c5ce189373c22c5bbcf90e3e498de, not final evidence tree.',
                   'Final evidence-package mechanical validation remains parent-owned and pending this confirmation.',
                   'Metadata storage/PR references designate delivery locations; this confirmation does not assert a PR or later validation already exists.',
                   'No scientific runner, pipeline, strict lint or formal audit was rerun. No retained status or landing is granted.'],
        'checker': reference(__file__), 'science_rerun': False, 'pipeline_rerun': False,
        'tracked_files_edited': False, 'formal_audit': False, 'landing_authorized': False
    }
    target = OUT / 'SOURCE_REFS_v1.json'
    assert not target.exists()
    target.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'confirmation': result['confirmation'], 'source_refs': reference(target),
                      'final_delta_count': len(final_delta), 'added_evidence_paths': len(added),
                      'archival_bytes': len(decoded), 'material_semantic_issues': []}, indent=2))


if __name__ == '__main__':
    main()
