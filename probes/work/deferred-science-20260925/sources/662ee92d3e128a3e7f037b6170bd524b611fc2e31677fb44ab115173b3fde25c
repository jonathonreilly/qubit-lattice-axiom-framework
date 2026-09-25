"""Close this new comparison packet; never write any prior or public source."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import ast
import json
import sys
import time

HERE = Path(__file__).resolve().parent
KEYS = ('sha256', 'bytes', 'mode', 'dev', 'ino', 'mtime_ns', 'ctime_ns', 'nlink')
START = datetime.now(timezone.utc).isoformat()
T0 = time.monotonic()


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def observed(path):
    stat = path.stat()
    return {
        'sha256': digest(path), 'bytes': stat.st_size, 'mode': stat.st_mode,
        'dev': stat.st_dev, 'ino': stat.st_ino, 'mtime_ns': stat.st_mtime_ns,
        'ctime_ns': stat.st_ctime_ns, 'nlink': stat.st_nlink,
    }


def read_json(name):
    return json.loads((HERE / name).read_text())


def write_new(name, obj):
    path = HERE / name
    assert path.parent == HERE
    with path.open('x') as stream:
        stream.write(json.dumps(obj, indent=2, sort_keys=True) + '\n')


def check_origins(sources, own):
    current_sources, current_own = [], []
    for row in sources:
        path = Path(row['origin'])
        now = observed(path)
        assert all(now[key] == row[key] for key in KEYS), str(path)
        snap = HERE / row['snapshot']
        assert snap.is_relative_to(HERE)
        assert digest(snap) == row['sha256']
        assert snap.stat().st_size == row['bytes']
        current_sources.append({'origin': str(path), 'snapshot': row['snapshot'], **now})
    for row in own:
        path = Path(row['path'])
        now = observed(path)
        assert all(now[key] == row[key] for key in KEYS), str(path)
        current_own.append({'path': str(path), **now})
    return current_sources, current_own


def main():
    assert HERE.name == 'publication_comparison_42_43'
    assert HERE.parent.name == 'native-birth-cluster-transport-independent'
    for name in ('PRESERVATION_AFTER.json', 'FINAL_BINDINGS.json',
                 'SEAL_PREPARATION.log', 'PUBLICATION_COMPARISON_SEAL.json',
                 'PUBLICATION_COMPARISON_SEAL_RECEIPT.json'):
        assert not (HERE / name).exists(), name
    pins = read_json('SOURCE_PINS.json')
    sources = pins['sources'] + read_json('MECHANICAL_SOURCE_PINS.json')['sources']
    own = read_json('OWN_43_PRESERVATION_BEFORE.json')['files']
    assert len(sources) == 104 and len(own) == 80
    current_sources, current_own = check_origins(sources, own)
    base = pins['git_context']
    assert digest(HERE / base['base_graph_snapshot']) == base['base_graph_sha256']

    receipts = []
    recorder_hash = digest(HERE / 'record_run.py')
    for label in ('capture', 'capture_mechanics', 'comparison'):
        receipt = read_json(label + '.execution.json')
        script = Path(receipt['command'][-1])
        assert script.parent == HERE
        assert digest(script) == receipt['source_sha256']
        assert receipt['recorder_sha256'] == recorder_hash
        assert receipt['exit_code'] == 0
        for log in receipt['outputs'].values():
            path = HERE / log['path']
            assert path.parent == HERE
            assert digest(path) == log['sha256']
            assert path.stat().st_size == log['bytes']
        assert receipt['outputs']['stderr.txt']['bytes'] == 0
        receipts.append({'path': label + '.execution.json',
                         'sha256': digest(HERE / (label + '.execution.json')),
                         'execution': receipt})
    comparison = receipts[-1]['execution']
    expected_console = json.dumps(comparison, indent=2) + '\n' + (HERE / 'comparison.stdout.txt').read_text()
    assert (HERE / 'comparison.console.txt').read_text() == expected_console
    assert (HERE / 'comparison.console.stderr.txt').read_bytes() == b''
    assert digest(HERE / 'comparison.stdout.txt') == 'c127b1f8bb4829321bdf1a3f3c725bf33dd8bf551657a96f63856666b69142a3'
    output = read_json('comparison.stdout.txt')
    assert output['source_origins_checked'] == 104
    assert output['own43_files_unchanged'] == 80
    assert [row['exact_nontiming_scalar_leaves'] for row in output['complete_fresh_scientific_payload_comparisons']] == [186008, 17758]
    assert output['input_fingerprint_sha256'] == 'deaba64df4916d8b08e577bb8105a0d9373a6a6fbdd01cc7250ed42c43c12fbd'
    assert output['exact_cache_bytes_reconstructed'] is True
    assert output['graph_manifest_delta']['old_nodes_unchanged'] == 6667
    assert output['graph_manifest_delta']['added_edges'] == 3

    # A conservative supplementary guard, not a replacement for the complete code read.
    tree = ast.parse((HERE / 'compare_read_only.py').read_text())
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
                assert node.func.attr not in {'write', 'write_text', 'write_bytes', 'open', 'unlink', 'rename', 'replace', 'chmod', 'mkdir', 'rmdir', 'system', 'run', 'Popen'} or (
                    node.func.attr == 'replace' and isinstance(node.func.value, ast.Name) and node.func.value.id == 'presented'
                )
    assert set(imports) == {'pathlib', 'hashlib', 'collections', 'ast', 'json', 're', 'stat'}

    write_new('PRESERVATION_AFTER.json', {
        'at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Closing source and prior-file observations before local packet locking.',
        'stat_scope': 'Bytes, mode, device, inode, mtime_ns, ctime_ns and nlink; access time excluded.',
        'sources': current_sources, 'own43_files': current_own,
        'all_before_after_identities_equal': True,
        'public_author_independent_sources_written': False,
    })
    bindings = {
        'scope': 'Released-source final publication correspondence42+43; no retained or audit verdict.',
        'report': {'path': 'PUBLICATION_COMPARISON.md', 'sha256': digest(HERE / 'PUBLICATION_COMPARISON.md')},
        'source_pins_sha256': digest(HERE / 'SOURCE_PINS.json'),
        'mechanical_source_pins_sha256': digest(HERE / 'MECHANICAL_SOURCE_PINS.json'),
        'closing_preservation_sha256': digest(HERE / 'PRESERVATION_AFTER.json'),
        'origin_count': 104, 'prior_own43_file_count': 80,
        'complete_comparison_output_sha256': digest(HERE / 'comparison.stdout.txt'),
        'complete_result_leaves': [186008, 17758],
        'cache_sha256': output['cache_sha256'],
        'input_fingerprint_sha256': output['input_fingerprint_sha256'],
        'publication_result_sha256': output['publication_result_sha256'],
        'graph_manifest_delta': output['graph_manifest_delta'],
        'recorded_new_script_executions': receipts,
        'local_report_tool_parse_failure': {'path': 'REPORT_WRITE_FAILURE.md',
                                           'sha256': digest(HERE / 'REPORT_WRITE_FAILURE.md'),
                                           'filesystem_mutation_before_failure': False},
        'scientific_programs_executed': [], 'historical_writers_executed': [],
        'fresh_comparator_read_only_ast_guard': {'imports': sorted(imports), 'checked': True},
        'complete_code_read_and_scientific_exposure': 'See PUBLICATION_COMPARISON.md and PROCESS_LOG.md.',
        'sealing_program': {'path': Path(__file__).name, 'sha256': digest(Path(__file__))},
    }
    write_new('FINAL_BINDINGS.json', bindings)
    log = [
        'Final binding checks completed without rerunning the primary or any scientific program.',
        '104 source origins and snapshots match their initial bytes and stable stats.',
        '80 previous independent43 files match their initial bytes and stable stats.',
        'Three new capture/comparison execution receipts and full logs match their current code.',
        'The complete comparison output, graph base snapshot, exact cache and fingerprint claims are bound.',
        'All historical files are read only; only this new subdirectory is written or locked.',
        'The sealing receipt is outside the seal to avoid a self-referential hash.',
    ]
    with (HERE / 'SEAL_PREPARATION.log').open('x') as stream:
        stream.write('\n'.join(log) + '\n')

    members = []
    for path in sorted(HERE.rglob('*')):
        assert not path.is_symlink(), str(path)
        if path.is_file():
            members.append({'path': path.relative_to(HERE).as_posix(),
                            'sha256': digest(path), 'bytes': path.stat().st_size})
    seal = {
        'created_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Immutable released-source publication comparison42+43; no publication edits or audit verdict.',
        'members': members,
        'member_count': len(members),
        'report_sha256': bindings['report']['sha256'],
        'source_pins_sha256': bindings['source_pins_sha256'],
        'prior_own43_preserved': True,
        'source_origins_unchanged': True,
        'files_locked_mode': '0444',
        'receipt_outside_manifest': 'PUBLICATION_COMPARISON_SEAL_RECEIPT.json',
    }
    write_new('PUBLICATION_COMPARISON_SEAL.json', seal)
    for row in members:
        path = HERE / row['path']
        assert digest(path) == row['sha256'] and path.stat().st_size == row['bytes']
        path.chmod(0o444)
    (HERE / 'PUBLICATION_COMPARISON_SEAL.json').chmod(0o444)
    for row in members:
        path = HERE / row['path']
        assert digest(path) == row['sha256'] and path.stat().st_size == row['bytes']
        assert path.stat().st_mode & 0o777 == 0o444
    check_origins(sources, own)
    receipt = {
        'completed_utc': datetime.now(timezone.utc).isoformat(),
        'started_utc': START,
        'command': [sys.executable, '-B', str(Path(__file__))],
        'source_sha256': digest(Path(__file__)),
        'elapsed_seconds_to_receipt': time.monotonic() - T0,
        'report_path': str(HERE / 'PUBLICATION_COMPARISON.md'),
        'report_sha256': bindings['report']['sha256'],
        'seal_path': str(HERE / 'PUBLICATION_COMPARISON_SEAL.json'),
        'seal_sha256': digest(HERE / 'PUBLICATION_COMPARISON_SEAL.json'),
        'source_pins_sha256': bindings['source_pins_sha256'],
        'member_count': len(members),
        'all_seal_members_verified': True,
        'source_origins_checked_unchanged': 104,
        'prior_own43_files_checked_unchanged': 80,
        'no_scientific_rerun': True,
        'required_mathematical_repair_found': False,
        'stdout_scope': 'This JSON receipt is the complete successful sealing stdout.',
    }
    write_new('PUBLICATION_COMPARISON_SEAL_RECEIPT.json', receipt)
    (HERE / 'PUBLICATION_COMPARISON_SEAL_RECEIPT.json').chmod(0o444)
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
