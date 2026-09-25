"""One-time binder for this new publication subpacket only. No scientific execution."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import ast
import json
import os
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
PREVIOUS = HERE.parent
PUB = PREVIOUS.parent / 'local-charge-observation-publication'
STAT_KEYS = ('sha256', 'bytes', 'mode', 'dev', 'ino', 'mtime_ns', 'ctime_ns', 'nlink')


def identity(path):
    s = path.stat()
    return dict(sha256=sha256(path.read_bytes()).hexdigest(), bytes=s.st_size,
                mode=s.st_mode, dev=s.st_dev, ino=s.st_ino, mtime_ns=s.st_mtime_ns,
                ctime_ns=s.st_ctime_ns, nlink=s.st_nlink)


def load(path):
    return json.loads(path.read_text())


def write_new(name, value):
    with (HERE / name).open('x') as stream:
        stream.write(json.dumps(value, indent=2) + '\n')


def verify(pins, prior):
    records = []
    for row in prior:
        path = Path(row['path']); now = identity(path)
        assert all(now[k] == row[k] for k in STAT_KEYS), str(path)
        records.append(dict(path=str(path), role='Protected prior PRE/POST file', **now))
    for row in pins['sources']:
        path = Path(row['origin']); now = identity(path)
        assert all(now[k] == row[k] for k in STAT_KEYS), str(path)
        records.append(dict(path=str(path), role='Live source origin', **now))
        snapshot = HERE / row['snapshot']; now = identity(snapshot)
        assert now['sha256'] == row['sha256'] and now['bytes'] == row['bytes']
        records.append(dict(path=str(snapshot), role='New snapshot', **now))
    path = HERE / pins['base_graph']['snapshot']; now = identity(path)
    assert now['sha256'] == pins['base_graph']['sha256'] and now['bytes'] == pins['base_graph']['bytes']
    records.append(dict(path=str(path), role='Base git manifest snapshot', **now))
    assert len(records) == len({r['path'] for r in records}) == 174
    return records


def main():
    started = datetime.now(timezone.utc).isoformat(); tick = time.monotonic()
    seal_name = 'PUBLICATION_COMPARISON_SEAL.json'
    receipt_name = 'PUBLICATION_COMPARISON_SEAL_RECEIPT.json'
    assert not (HERE / seal_name).exists() and not (HERE / receipt_name).exists()
    pins = load(HERE / 'SOURCE_PINS.json')
    prior = load(HERE / 'PRIOR_PRESERVATION_BEFORE.json')['files']
    assert len(pins['sources']) == 44 and len(prior) == 85
    verify(pins, prior)
    for filename, expected in [('PRE_SEAL.json', '2e45743285afecd1b294017ab085c965d96007872193dd9822b4b76976072255'),
                               ('POST_SEAL.json', '2ce94c18e4e8ff9d0a0e14b0e2925e65b41aa7f02f4016530d07fb20325af7a6')]:
        assert identity(PREVIOUS / filename)['sha256'] == expected
        for row in load(PREVIOUS / filename)['members']:
            now = identity(PREVIOUS / row['path'])
            assert now['sha256'] == row['sha256'] and now['bytes'] == row['bytes']
    executions = []
    for label in ('capture', 'comparison'):
        receipt = load(HERE / (label + '.execution.json'))
        assert receipt['exit_code'] == 0
        program = Path(receipt['command'][2])
        assert program.parent == HERE and identity(program)['sha256'] == receipt['source_sha256']
        assert identity(HERE / 'record_run.py')['sha256'] == receipt['recorder_sha256']
        for kind, row in receipt['outputs'].items():
            now = identity(HERE / row['path'])
            assert now['sha256'] == row['sha256'] and now['bytes'] == row['bytes']
            if kind == 'stderr.txt':
                assert now['bytes'] == 0
        executions.append(dict(receipt=label + '.execution.json',
                               receipt_sha256=identity(HERE / (label + '.execution.json'))['sha256'],
                               source_sha256=receipt['source_sha256'],
                               elapsed_seconds=receipt['elapsed_seconds'], outputs=receipt['outputs']))
    code = HERE / 'compare_read_only.py'
    assert identity(code)['sha256'] == '21f9438cb2850335c82a71492ce0ffcba6d4c9f35559374e7ab7242beb76efd9'
    forbidden_methods = {'write_text', 'write_bytes', 'open', 'chmod', 'unlink', 'mkdir',
                         'rename', 'touch', 'rmdir', 'symlink_to', 'hardlink_to'}
    imports = []
    for node in ast.walk(ast.parse(code.read_text())):
        if isinstance(node, ast.Import):
            imports.extend(a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                assert node.func.id not in {'open', 'exec', 'eval', 'compile', '__import__'}
            elif isinstance(node.func, ast.Attribute):
                assert node.func.attr not in forbidden_methods
    assert set(imports) == {'pathlib', 'hashlib', 'collections', 'ast', 'difflib', 'json',
                           'math', 'os', 're', 'stat', 'subprocess'}
    result = load(HERE / 'comparison.stdout.txt')
    assert result['observed_paths_unchanged'] == 174 and result['protected_prior_files'] == 85
    assert [r['non_timing_leaf_count'] for r in result['comparisons']] == [177399, 249500]
    assert result['exact_full_cache_reconstruction'] is True
    assert result['graph']['old_nodes'] == 6667 and result['graph']['new_nodes'] == 6668
    assert result['graph']['new_edges'] - result['graph']['old_edges'] == 3
    env = dict(os.environ, GIT_OPTIONAL_LOCKS='0')
    final_git = []
    for args, expected in [(['rev-parse', '--verify', 'HEAD'], result['base']),
                           (['branch', '--show-current'], result['branch'])]:
        run = subprocess.run(['git', *args], cwd=PUB, env=env, capture_output=True)
        assert run.returncode == 0 and run.stderr == b'' and run.stdout.decode().strip() == expected
        final_git.append(dict(command=['git', *args], exit_code=run.returncode, stdout=run.stdout.decode(), stderr=''))

    names = {r['snapshot'] for r in pins['sources']}
    names.add(pins['base_graph']['snapshot'])
    names.update({'capture_sources.py', 'record_run.py', 'compare_read_only.py', 'seal_packet.py',
                  'SOURCE_PINS.json', 'PRIOR_PRESERVATION_BEFORE.json', 'GIT_SOURCE_EVIDENCE.json',
                  'PUBLICATION_COMPARISON.md', 'PROCESS_LOG.md'})
    for label in ('capture', 'comparison'):
        names.update(label + suffix for suffix in ('.execution.json', '.stdout.txt', '.stderr.txt'))
    actual = {str(p.relative_to(HERE)) for p in HERE.rglob('*') if p.is_file()}
    assert actual == names and len(names) == 60, {'extra': sorted(actual - names), 'missing': sorted(names - actual)}
    for name in sorted(names):
        (HERE / name).chmod(0o444)
    after = verify(pins, prior)
    write_new('PRESERVATION_AFTER.json', dict(at_utc=datetime.now(timezone.utc).isoformat(),
        prior_files_unchanged=85, live_origins_unchanged=44, snapshots_bound=45,
        original_and_prior_bytes_and_metadata_unchanged=True,
        snapshot_permission_change='Only new subpacket copies were made read-only.', files=after))
    write_new('FINAL_BINDINGS.json', dict(at_utc=datetime.now(timezone.utc).isoformat(),
        executions=executions, final_git=final_git,
        frozen_manifest_sha256=pins['frozen_manifest_sha256'],
        report_sha256=identity(HERE / 'PUBLICATION_COMPARISON.md')['sha256'],
        readonly_comparator=dict(source_sha256=identity(code)['sha256'], imports=sorted(set(imports)),
            inspected_no_file_writes=True, subprocess_scope='Six explicitly restricted read-only git commands with optional locks disabled.',
            static_check_limit='Interface guard plus complete source read, not a general security proof.'),
        scientific_reruns=[], source_edits=[], new_execution_failures=[],
        interruption=pins['interruption'], applies_audit_verdict=False))
    names.update({'PRESERVATION_AFTER.json', 'FINAL_BINDINGS.json'})
    for name in ('PRESERVATION_AFTER.json', 'FINAL_BINDINGS.json'):
        (HERE / name).chmod(0o444)
    members = [dict(path=name, sha256=identity(HERE / name)['sha256'], bytes=(HERE / name).stat().st_size)
               for name in sorted(names)]
    assert len(members) == 62
    write_new(seal_name, dict(sealed_utc=datetime.now(timezone.utc).isoformat(),
        phase='Final released-source publication correspondence for Part II and stated joins',
        members=members, member_count=len(members),
        PRE_seal_sha256=identity(PREVIOUS / 'PRE_SEAL.json')['sha256'],
        POST_seal_sha256=identity(PREVIOUS / 'POST_SEAL.json')['sha256'],
        audit_verdict_applied=False, receipt_outside_manifest=True))
    (HERE / seal_name).chmod(0o444)
    for row in members:
        now = identity(HERE / row['path'])
        assert now['sha256'] == row['sha256'] and now['bytes'] == row['bytes']
        assert now['mode'] & 0o777 == 0o444
    verify(pins, prior)
    receipt = dict(started_utc=started, completed_utc=datetime.now(timezone.utc).isoformat(),
        elapsed_seconds=time.monotonic() - tick, binder_source_sha256=identity(Path(__file__))['sha256'],
        command=[sys.executable, '-B', str(Path(__file__).resolve())],
        report_sha256=identity(HERE / 'PUBLICATION_COMPARISON.md')['sha256'],
        seal_sha256=identity(HERE / seal_name)['sha256'], members_verified=len(members),
        prior_files_unchanged=85, live_origins_unchanged=44, all_members_read_only=True)
    write_new(receipt_name, receipt)
    (HERE / receipt_name).chmod(0o444)
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
