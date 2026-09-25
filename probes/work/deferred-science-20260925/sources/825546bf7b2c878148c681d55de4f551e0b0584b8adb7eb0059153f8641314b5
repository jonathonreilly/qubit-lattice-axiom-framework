"""One-time evidence closure for this new PRE; writes only its own directory."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import ast
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
KEYS = ('sha256', 'bytes', 'mode', 'dev', 'ino', 'mtime_ns', 'ctime_ns', 'nlink')


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def observation(path):
    s = path.stat()
    return {'sha256': digest(path), 'bytes': s.st_size, 'mode': s.st_mode,
            'dev': s.st_dev, 'ino': s.st_ino, 'mtime_ns': s.st_mtime_ns,
            'ctime_ns': s.st_ctime_ns, 'nlink': s.st_nlink}


def write_new(name, data):
    path = HERE / name
    assert path.is_relative_to(HERE)
    with path.open('x') as stream:
        stream.write(json.dumps(data, indent=2, sort_keys=True) + '\n')


def close_sources(pins):
    observations = []
    for row in pins['sources']:
        snap = HERE / row['snapshot']
        assert digest(snap) == row['sha256'] and snap.stat().st_size == row['bytes']
        if 'origin' in row:
            now = observation(Path(row['origin']))
            assert all(now[key] == row[key] for key in KEYS)
            observations.append({'origin': row['origin'], **now})
        if 'git_revision' in row:
            repository = row.get('git_repository', str(HERE.parent / 'campaign-working'))
            raw = subprocess.check_output(['git', '-C', repository, 'show', row['git_revision'] + ':' + row['git_path']])
            assert raw == snap.read_bytes()
    return observations


def main():
    start = datetime.now(timezone.utc).isoformat(); t0 = time.monotonic()
    assert HERE.name == 'native-charge-finite-time-independent'
    assert not (HERE / 'PRE_SEAL.json').exists()
    pins = json.loads((HERE / 'SOURCE_PINS.json').read_text())
    before_close = close_sources(pins)
    installed = Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md')
    installed_pin = {'origin': str(installed),
                     'snapshot': 'sources/installed_physics_claim_reviewer_SKILL.md',
                     'role': 'Installed procedural distribution copy read earlier; identity matched to repository source at closure.',
                     **observation(installed)}
    raw = installed.read_bytes()
    assert raw == (HERE / 'sources/physics_claim_reviewer_SKILL.md').read_bytes()
    with (HERE / installed_pin['snapshot']).open('xb') as stream:
        stream.write(raw)
    write_new('ADDITIONAL_PROCEDURAL_PIN.json', installed_pin)

    executions = []
    for label in ('capture', 'primitive', 'tree', 'verification'):
        path = HERE / (label + '.execution.json')
        receipt = json.loads(path.read_text())
        assert receipt['exit_code'] == 0
        program = Path(receipt['command'][2]); assert program.parent == HERE
        assert digest(program) == receipt['source_sha256']
        assert digest(HERE / 'record_run.py') == receipt['recorder_sha256']
        for log in receipt['outputs'].values():
            target = HERE / log['path']
            assert digest(target) == log['sha256'] and target.stat().st_size == log['bytes']
        assert receipt['outputs']['stderr.txt']['bytes'] == 0
        executions.append({'receipt': path.name, 'sha256': digest(path), 'exit_code': 0,
                           'elapsed_seconds': receipt['elapsed_seconds']})
    verification = json.loads((HERE / 'verification.stdout.txt').read_text())
    for name, value in verification['result_hashes'].items():
        assert digest(HERE / name) == value
    assert verification['source_origins'] == 9
    assert [row['primitive_rows'] for row in verification['tori']] == [1920, 6480]
    assert len(verification['tree']['finite_time_rows']) == 24
    assert verification['tree']['all_integer_matrices_reconstructed']
    assert verification['all_tree_float_leaves_finite'] == 1628
    assert verification['all_observed_input_files_unchanged'] == 27

    tree = ast.parse((HERE / 'verify_read_only.py').read_text())
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                assert node.func.id not in {'open', 'exec', 'eval', '__import__', 'compile'}
            if isinstance(node.func, ast.Attribute):
                assert node.func.attr not in {'write', 'write_text', 'write_bytes', 'open', 'unlink', 'rename', 'chmod', 'mkdir', 'rmdir', 'system', 'run', 'Popen'}
                if node.func.attr == 'check_output':
                    assert isinstance(node.args[0], ast.List)
                    assert [ast.literal_eval(node.args[0].elts[i]) for i in (0, 1, 3)] == ['git', '-C', 'show']
    assert set(imports) == {'pathlib', 'hashlib', 'collections', 'itertools', 'math', 'json', 'subprocess'}

    write_new('SOURCE_PRESERVATION_AFTER.json', {
        'at_utc': datetime.now(timezone.utc).isoformat(),
        'stat_scope': 'Stable byte/stat identity, excluding access time.',
        'file_origins': before_close, 'additional_procedural_origin': installed_pin,
        'all_source_git_objects_and_snapshots_exact': True,
        'outside_packet_files_written': [],
    })
    write_new('FINAL_BINDINGS.json', {
        'scope': 'Bounded independent PRE47; prior42/43 exposure retained, no author47 release.',
        'report': {'path': 'PRE.md', 'sha256': digest(HERE / 'PRE.md')},
        'source_pins_sha256': digest(HERE / 'SOURCE_PINS.json'),
        'additional_procedural_pin_sha256': digest(HERE / 'ADDITIONAL_PROCEDURAL_PIN.json'),
        'source_preservation_sha256': digest(HERE / 'SOURCE_PRESERVATION_AFTER.json'),
        'verification_source_sha256': digest(HERE / 'verify_read_only.py'),
        'verification_output_sha256': digest(HERE / 'verification.stdout.txt'),
        'scientific_result_hashes': verification['result_hashes'],
        'execution_receipts': executions,
        'artifact_execution_binding_scope': 'Successful writer receipts followed by independent complete stored-evidence reconstruction; artifact hashes are observed at verification and closure, not backdated to execution start.',
        'read_only_verifier_guard': {'imports': sorted(imports), 'no_file_mutation_calls': True,
                                    'only_subprocess_calls': 'git show of pinned sources'},
        'seal_writer_sha256': digest(Path(__file__)),
        'failures_preserved': 'FAILED_ROUTES_AND_SCOPE.md; no scientific execution failed.',
        'new_agents': 0, 'historical_programs_executed': [], 'audit_or_publication_changes': [],
    })

    # Lock only copies and new artifacts in this packet, never any origin or prior packet.
    members = []
    for path in sorted(HERE.rglob('*')):
        assert not path.is_symlink()
        if path.is_file():
            members.append({'path': path.relative_to(HERE).as_posix(),
                            'sha256': digest(path), 'bytes': path.stat().st_size})
    seal = {'created_utc': datetime.now(timezone.utc).isoformat(),
            'phase': 'Independent PRE before author47 disclosure',
            'scope': 'Conditional finite-graph full-process local covariance theorem and bounded new controls; no audit verdict.',
            'member_count': len(members), 'members': members,
            'report_sha256': digest(HERE / 'PRE.md'),
            'source_pins_sha256': digest(HERE / 'SOURCE_PINS.json'),
            'file_mode_after_seal': '0444', 'receipt_outside_manifest': 'PRE_SEAL_RECEIPT.json'}
    write_new('PRE_SEAL.json', seal)
    for member in members:
        (HERE / member['path']).chmod(0o444)
    (HERE / 'PRE_SEAL.json').chmod(0o444)
    for member in members:
        path = HERE / member['path']
        assert digest(path) == member['sha256'] and path.stat().st_size == member['bytes']
        assert path.stat().st_mode & 0o777 == 0o444
    assert close_sources(pins) == before_close
    assert all(observation(installed)[key] == installed_pin[key] for key in KEYS)
    receipt = {'started_utc': start, 'completed_utc': datetime.now(timezone.utc).isoformat(),
               'command': [sys.executable, '-B', str(Path(__file__))],
               'sealer_source_sha256': digest(Path(__file__)),
               'elapsed_seconds_to_receipt': time.monotonic() - t0,
               'report_path': str(HERE / 'PRE.md'), 'report_sha256': seal['report_sha256'],
               'seal_path': str(HERE / 'PRE_SEAL.json'), 'seal_sha256': digest(HERE / 'PRE_SEAL.json'),
               'source_pins_sha256': seal['source_pins_sha256'],
               'member_count': len(members), 'all_members_verified': True,
               'source_records_checked': len(pins['sources']) + 1,
               'all_origin_bytes_and_stable_stats_unchanged': True,
               'stdout_scope': 'This JSON is the complete successful sealing stdout.'}
    write_new('PRE_SEAL_RECEIPT.json', receipt)
    (HERE / 'PRE_SEAL_RECEIPT.json').chmod(0o444)
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
