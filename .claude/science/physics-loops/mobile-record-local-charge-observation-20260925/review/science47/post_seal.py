"""New POST-only binder. Writes only new POST artifacts; no scientific execution."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import ast
import json

HERE = Path(__file__).resolve().parent
STAT_KEYS = ('sha256', 'bytes', 'mode', 'dev', 'ino', 'mtime_ns', 'ctime_ns', 'nlink')


def identity(path):
    st = path.stat()
    return {'sha256': sha256(path.read_bytes()).hexdigest(), 'bytes': st.st_size,
            'mode': st.st_mode, 'dev': st.st_dev, 'ino': st.st_ino,
            'mtime_ns': st.st_mtime_ns, 'ctime_ns': st.st_ctime_ns, 'nlink': st.st_nlink}


def load(path):
    return json.loads(path.read_text())


def write_new(name, value):
    with (HERE / name).open('x') as stream:
        stream.write(json.dumps(value, indent=2) + '\n')


def verify_prior_and_sources(pins, previous):
    records = []
    for row in previous:
        path = Path(row['path'])
        now = identity(path)
        assert all(now[key] == row[key] for key in STAT_KEYS), str(path)
        records.append({'path': str(path), 'role': 'Protected prior PRE file', **now})
    for row in pins['sources']:
        origin = Path(row['origin'])
        now = identity(origin)
        assert all(now[key] == row[key] for key in STAT_KEYS), str(origin)
        records.append({'path': str(origin), 'role': 'Pinned released origin', **now})
        snap = HERE / row['snapshot']
        now = identity(snap)
        assert now['sha256'] == row['sha256'] and now['bytes'] == row['bytes']
        records.append({'path': str(snap), 'role': 'New POST snapshot', **now})
    assert len(records) == len({r['path'] for r in records}) == 91
    return records


def main():
    assert not (HERE / 'POST_SEAL.json').exists()
    assert not (HERE / 'POST_SEAL_RECEIPT.json').exists()
    pins = load(HERE / 'POST_SOURCE_PINS.json')
    previous = load(HERE / 'POST_PRE_PRESERVATION_BEFORE.json')['files']
    assert len(previous) == 41 and len(pins['sources']) == 25
    before = verify_prior_and_sources(pins, previous)
    prior_paths = {Path(row['path']).relative_to(HERE).as_posix() for row in previous}
    old_seal = load(HERE / 'PRE_SEAL.json')
    assert len(old_seal['members']) == 39
    for member in old_seal['members']:
        now = identity(HERE / member['path'])
        assert now['sha256'] == member['sha256']
        assert now['bytes'] == member['bytes']

    executions = []
    for prefix in ('post_capture', 'post_comparison'):
        receipt = load(HERE / (prefix + '.execution.json'))
        assert receipt['exit_code'] == 0
        program = Path(receipt['command'][2])
        assert program.parent == HERE
        assert identity(program)['sha256'] == receipt['source_sha256']
        assert identity(HERE / 'post_record_run.py')['sha256'] == receipt['recorder_sha256']
        for kind, row in receipt['outputs'].items():
            output = HERE / row['path']
            assert identity(output)['sha256'] == row['sha256']
            assert output.stat().st_size == row['bytes']
            if kind == 'stderr.txt':
                assert row['bytes'] == 0
        executions.append({'receipt': prefix + '.execution.json',
                           'sha256': identity(HERE / (prefix + '.execution.json'))['sha256'],
                           'program': program.name, 'source_sha256': receipt['source_sha256'],
                           'started_utc': receipt['started_utc'],
                           'elapsed_seconds': receipt['elapsed_seconds'],
                           'exit_code': receipt['exit_code'], 'outputs': receipt['outputs']})

    comparator = HERE / 'post_compare_read_only.py'
    tree = ast.parse(comparator.read_text())
    modules = []
    forbidden_attributes = {'write_text', 'write_bytes', 'open', 'chmod', 'unlink',
                            'mkdir', 'rename', 'touch', 'rmdir', 'symlink_to', 'hardlink_to'}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            modules.append(node.module)
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                assert node.func.id not in {'open', 'exec', 'eval', 'compile', '__import__'}
            elif isinstance(node.func, ast.Attribute):
                assert node.func.attr not in forbidden_attributes
    assert set(modules) == {'pathlib', 'hashlib', 'fractions', 'itertools', 'math', 'ast', 'json'}
    result = load(HERE / 'post_comparison.stdout.txt')
    assert result['prior_PRE_files_unchanged'] == 41
    assert result['source_origins'] == 25
    assert result['all_observed_sources_and_copies_unchanged'] == 91
    assert [row['L'] for row in result['graphs']] == [4, 6, 8, 12, 16, 20]
    assert sum(row['complete_stored_atoms_compared'] for row in result['graphs']) == 14916
    assert sum(row['complete_stored_groups_compared'] for row in result['graphs']) == 23487

    skill = Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md')
    write_new('POST_PROCESS_INSTRUCTIONS.json', {
        'created_utc': datetime.now(timezone.utc).isoformat(),
        'skill_read_as_process_guidance': {'path': str(skill), **identity(skill)},
        'application': 'Bounded proof, premise and evidence review only; explicit task scope controls. No audit, publication, delegation or model change.',
        'unchanged_repository_instruction_copies': [row for row in pins['sources']
                                                     if row['snapshot'].endswith(('5_AGENTS.md', '6_SCIENCE_WORKFLOW.md'))],
        'editable_prompts_modified': [], 'model_or_effort_changed': False,
        'author_programs_or_old_writers_executed': []})

    names = {Path(row['snapshot']).as_posix() for row in pins['sources']}
    names.update({'capture_post_sources.py', 'post_record_run.py', 'post_compare_read_only.py',
                  'post_seal.py', 'POST_SOURCE_PINS.json', 'POST_PRE_PRESERVATION_BEFORE.json',
                  'POST_PROCESS_INSTRUCTIONS.json', 'POST.md', 'POST_PROCESS_LOG.md'})
    for prefix in ('post_capture', 'post_comparison'):
        names.update(prefix + suffix for suffix in ('.execution.json', '.stdout.txt', '.stderr.txt'))
    expected_current = prior_paths | names
    actual_current = {p.relative_to(HERE).as_posix() for p in HERE.rglob('*') if p.is_file()}
    assert actual_current == expected_current, {'unexpected': sorted(actual_current - expected_current),
                                                'missing': sorted(expected_current - actual_current)}
    assert not (names & prior_paths)
    # Only new POST files are chmodded. Prior sources retain their metadata.
    for name in sorted(names):
        (HERE / name).chmod(0o444)
    after = verify_prior_and_sources(pins, previous)
    for initial in before:
        current = identity(Path(initial['path']))
        if initial['role'] != 'New POST snapshot':
            assert all(current[k] == initial[k] for k in STAT_KEYS)
        else:
            assert current['sha256'] == initial['sha256'] and current['bytes'] == initial['bytes']

    write_new('POST_PRESERVATION_AFTER.json', {
        'at_utc': datetime.now(timezone.utc).isoformat(),
        'protected_PRE_and_live_source_bytes_and_metadata_unchanged': True,
        'prior_PRE_files': 41, 'live_origins': 25, 'new_snapshots': 25,
        'new_snapshot_mode_change': 'Only new POST copies were set read-only; original and PRE metadata unchanged.',
        'files': after})
    write_new('POST_FINAL_BINDINGS.json', {
        'at_utc': datetime.now(timezone.utc).isoformat(),
        'PRE_seal_sha256': identity(HERE / 'PRE_SEAL.json')['sha256'],
        'author47_seal_sha256': pins['author47_seal_sha256'],
        'actual_new_executions': executions,
        'readonly_comparator_review': {'sha256': identity(comparator)['sha256'],
                                       'import_modules': sorted(set(modules)),
                                       'no_write_or_dynamic_execution_calls_in_inspected_source': True,
                                       'scope': 'Static interface check plus complete source read, not a general Python security proof.'},
        'complete_comparison_counts': {'volumes': 6, 'local_tests': 18,
                                        'stored_atom_occurrences': 14916,
                                        'stored_group_occurrences': 23487},
        'scientific_failures_in_POST': [], 'packaging_failures_in_POST': [],
        'report_sha256': identity(HERE / 'POST.md')['sha256']})
    names.update({'POST_PRESERVATION_AFTER.json', 'POST_FINAL_BINDINGS.json'})
    for name in ('POST_PRESERVATION_AFTER.json', 'POST_FINAL_BINDINGS.json'):
        (HERE / name).chmod(0o444)
    members = [{'path': name, 'sha256': identity(HERE / name)['sha256'],
                'bytes': (HERE / name).stat().st_size} for name in sorted(names)]
    write_new('POST_SEAL.json', {
        'sealed_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Released-source POST47; no audit verdict, author execution or source mutation.',
        'prior_PRE_seal_sha256': identity(HERE / 'PRE_SEAL.json')['sha256'],
        'members': members})
    (HERE / 'POST_SEAL.json').chmod(0o444)
    for member in members:
        current = identity(HERE / member['path'])
        assert current['sha256'] == member['sha256'] and current['bytes'] == member['bytes']
        assert current['mode'] & 0o777 == 0o444
    verify_prior_and_sources(pins, previous)
    receipt = {'verified_utc': datetime.now(timezone.utc).isoformat(),
               'POST_seal_sha256': identity(HERE / 'POST_SEAL.json')['sha256'],
               'POST_report_sha256': identity(HERE / 'POST.md')['sha256'],
               'members_verified': len(members), 'prior_PRE_files_unchanged': 41,
               'live_origins_unchanged': 25, 'sealed_files_read_only': True,
               'seal_and_receipt_are_outside_manifest': True}
    write_new('POST_SEAL_RECEIPT.json', receipt)
    (HERE / 'POST_SEAL_RECEIPT.json').chmod(0o444)
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
