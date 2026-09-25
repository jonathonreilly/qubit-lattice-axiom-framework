"""Read-only generation02 link, complete payload, recovery and cache binding.

No scientific runner or cache helper is imported or executed. All output is
JSON on stdout; the caller records it outside the publication worktree.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import ast
import difflib
import hashlib
import json
import re
import stat
import subprocess

HERE = Path(__file__).resolve().parent
OLD = HERE / 'publication_frozen'
NEW = HERE / 'publication_revision_frozen' / 'generation02'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(path.read_text())


def match(path, row):
    data = path.read_bytes()
    assert len(data) == row['bytes'] and sha(data) == row['sha256'], str(path)


def compare(a, b, path, counts, times):
    assert type(a) is type(b), path
    if isinstance(a, dict):
        assert list(a) == list(b), path
        for key in a:
            if key == 'elapsed_seconds' and path in {'root_generic', 'independent_native'}:
                times.append({'path': path + '/' + key, 'generation01': a[key], 'generation02': b[key]})
            else:
                compare(a[key], b[key], path + '/' + key, counts, times)
    elif isinstance(a, list):
        assert len(a) == len(b), path
        for index, (x, y) in enumerate(zip(a, b)):
            compare(x, y, path + '/' + str(index), counts, times)
    else:
        assert a == b, (path, a, b)
        counts[type(a).__name__] += 1


def main():
    pins = load(HERE / 'PUBLICATION_REVISION_SOURCE_PINS.json')
    work = Path(pins['publication_root'])
    history = Path(pins['generation01_history'])
    old_commit = pins['generation01_commit']
    assert len(pins['origins']) == 14
    for row in pins['origins']:
        match(HERE / row['frozen'], row)
        match(Path(row['origin']), row)
    seals = {
        'PRE_SEAL.json': ('75bdc5d36dad74adf96285cefb0896539466f4e14c179cecc30f9afe5dbbf4ca', 25),
        'POST_SEAL.json': ('5c8cf25f153a2e8d2ece143e22afa95242c93e1ebfe137efa005809c2617b6a0', 20),
        'PUBLICATION_COMPARISON_SEAL.json': ('dbe7b8e5f0ba94c1aea2dad3ebfccb77e77d30fbd65213e1609b91eac761cdf0', 27)
    }
    for name, (expected, count) in seals.items():
        assert sha((HERE / name).read_bytes()) == expected
        seal = load(HERE / name)
        assert seal['member_count'] == len(seal['members']) == count
        for member in seal['members']:
            match(HERE / member['path'], member)

    manifest_name = 'FINITE_WINDOW_ENERGY_PUBLICATION_FROZEN_SOURCES.json'
    old_manifest = load(OLD / 'metadata' / manifest_name)
    manifest = load(NEW / 'metadata' / manifest_name)
    assert sha((NEW / 'metadata' / manifest_name).read_bytes()) == '8ec03d41266350e7f73b3e1ea38665ed77fe01f91a53fbee7f9424fcd823335b'
    assert manifest['generation'] == 2 and manifest['previous_generation_commit'] == old_commit
    assert manifest['base_revision'] == old_manifest['base_revision']
    assert list(manifest['files_sha256']) == list(old_manifest['files_sha256'])
    changed_members = []
    recovery = []
    for rel, expected in manifest['files_sha256'].items():
        current = (NEW / 'worktree' / rel).read_bytes()
        old = (OLD / 'worktree' / rel).read_bytes()
        assert sha(current) == expected
        git = subprocess.run(['git', '-C', str(work), 'show', old_commit + ':' + rel],
                             capture_output=True, check=True).stdout
        assert git == old, rel
        archived = history / 'worktree' / rel
        if archived.is_file():
            assert archived.read_bytes() == old
        recovery.append({'path': rel, 'generation01_sha256': sha(old),
                         'git_commit_bytes_match': True, 'separate_history_copy_exists_and_matches': archived.is_file()})
        if old != current:
            changed_members.append(rel)
    assert changed_members == [manifest['note'], manifest['result'], manifest['cache']]
    recovered_metadata = []
    for row in load(HERE / 'PUBLICATION_SOURCE_PINS.json')['origins']:
        if row['type'] == 'external process metadata':
            archived = history / Path(row['origin']).name
            match(archived, row)
            assert archived.read_bytes() == (HERE / row['frozen']).read_bytes()
            recovered_metadata.append({'path': str(archived), 'sha256': row['sha256']})
    assert len(recovered_metadata) == 4
    helper = OLD / 'tooling' / 'runner_cache.py'
    assert helper.read_bytes() == (work / 'scripts/runner_cache.py').read_bytes()
    assert subprocess.run(['git', '-C', str(work), 'show', old_commit + ':scripts/runner_cache.py'],
                          capture_output=True, check=True).stdout == helper.read_bytes()

    note = (NEW / 'worktree' / manifest['note']).read_text()
    old_note = (OLD / 'worktree' / manifest['note']).read_text()
    diff = ''.join(difflib.unified_diff(old_note.splitlines(keepends=True), note.splitlines(keepends=True),
                                      fromfile='generation01', tofile='generation02'))
    assert diff == (NEW / 'metadata' / 'FINITE_WINDOW_ENERGY_PUBLICATION_LINK_REPAIR.diff').read_text()
    heading = '## Evidence and remaining physical obligations'
    assert note[:note.index(heading)] == old_note[:old_note.index(heading)]
    old_paragraph, old_footer = old_note[old_note.index(heading):].split('\n\nAn energy distribution', 1)
    paragraph, footer = note[note.index(heading):].split('\n\nAn energy distribution', 1)
    assert footer == old_footer
    old_links = re.findall(r'\[([^]]+)\]\(([^)]+)\)', old_note)
    new_links = re.findall(r'\[([^]]+)\]\(([^)]+)\)', note)
    assert len(old_links) == len(new_links)
    changed_links = [(a, b) for a, b in zip(old_links, new_links) if a != b]
    assert len(changed_links) == 4
    link_rows = []
    for old_link, new_link in changed_links:
        assert old_link[0] == new_link[0]
        old_target = Path(old_link[1])
        assert old_target.suffix == '.md'
        assert new_link[1] == old_target.parent.as_posix() + '/'
        assert '`' + old_target.name + '`' in paragraph
        directory = (work / manifest['note']).parent / new_link[1]
        assert directory.is_dir() and (directory / old_target.name).is_file()
        link_rows.append({'label': old_link[0], 'old_target': old_link[1], 'new_target': new_link[1],
                          'named_historical_file': old_target.name, 'directory_and_named_file_exist': True,
                          'linked_historical_contents_reaudited': False})
    reason = load(NEW / 'metadata' / 'FINITE_WINDOW_ENERGY_PUBLICATION_LINK_REPAIR.json')
    assert reason['old_note'] == sha(old_note.encode()) and reason['new_note'] == sha(note.encode())
    assert reason['new_note'] == 'f950ff0435287ce4be95d278422319d398d5969676299211e12b5478e42bdfbb'

    tree = ast.parse((NEW / 'worktree' / manifest['runner']).read_text())
    declaration = next(n for n in tree.body if isinstance(n, ast.Assign)
                       and any(isinstance(t, ast.Name) and t.id == 'AUDIT_INPUT_PATHS' for t in n.targets))
    inputs = ast.literal_eval(declaration.value)
    assert inputs == (manifest['note'], *manifest['parent_paths'], *manifest['runtime'])
    fingerprint = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
    for rel in inputs:
        assert not Path(rel).is_absolute() and '..' not in Path(rel).parts and Path(rel).as_posix() == rel
        component = work
        for part in Path(rel).parts:
            component /= part
            assert not stat.S_ISLNK(component.lstat().st_mode)
        body = (NEW / 'worktree' / rel).read_bytes()
        label = rel.encode()
        fingerprint.update(len(label).to_bytes(8, 'big')); fingerprint.update(label)
        fingerprint.update(len(body).to_bytes(8, 'big')); fingerprint.update(body)
    fp = fingerprint.hexdigest()
    assert fp == '18fc944893cea337313ad993f2ac65027120c4ae043285c289d3b1f6fefa42cc'
    result_bytes = (NEW / 'worktree' / manifest['result']).read_bytes()
    result = json.loads(result_bytes)
    old_result = load(OLD / 'worktree' / old_manifest['result'])
    assert list(result) == list(old_result)
    assert list(result['payload']) == list(old_result['payload']) == ['root_generic', 'independent_native']
    assert len(result['stages']) == len(old_result['stages']) == 2
    counts, timers = Counter(), []
    for key in ('root_generic', 'independent_native'):
        compare(old_result['payload'][key], result['payload'][key], key, counts, timers)
    assert dict(counts) == {'str': 464, 'int': 232, 'bool': 8, 'float': 410}
    assert len(timers) == 2
    for key, stage, source in zip(('root_generic', 'independent_native'), result['stages'], manifest['runtime']):
        stdout = (json.dumps(result['payload'][key], indent=2, allow_nan=False) + '\n').encode()
        assert sha(stdout) == stage['stdout_sha256'] and len(stdout) == stage['stdout_bytes']
        assert stage['exit_code'] == stage['stderr_bytes'] == 0
        assert stage['program'] == Path(source).name
        assert stage['code_sha256'] == result['payload'][key]['source_sha256'] == sha((NEW / 'worktree' / source).read_bytes())
    wrapper_sha = sha((NEW / 'worktree' / manifest['runner']).read_bytes())
    assert wrapper_sha == result['source_sha256'] == old_result['source_sha256']
    assert result['scope'] == old_result['scope'] and result['all_assertions_passed'] is True
    execution = load(NEW / 'metadata' / 'FINITE_WINDOW_ENERGY_PUBLICATION_CACHE_EXECUTION.json')
    assert execution['stdout'].encode() == result_bytes + b'TOTAL_PASS: 2\n'
    assert len(execution['stdout']) < 200000
    assert execution['status'] == 'ok' and execution['exit_code'] == 0 and execution['stderr'] == ''
    assert execution['runner'] == manifest['runner'] and execution['timeout_sec'] == 120
    header = ('===== runner cache v1 =====\n' + f"runner: {manifest['runner']}\n"
              + f'runner_sha256: {wrapper_sha}\ninput_fingerprint_sha256: {fp}\n'
              + f"timeout_sec: {execution['timeout_sec']}\nexit_code: {execution['exit_code']}\n"
              + f"elapsed_sec: {execution['elapsed_sec']:.2f}\nstatus: {execution['status']}\n----- stdout -----\n")
    cache = (header + execution['stdout'] + '\n----- stderr -----\n' + execution['stderr'] + '\n').encode()
    assert cache == (NEW / 'worktree' / manifest['cache']).read_bytes()
    print(json.dumps({
        'checked_utc': datetime.now(timezone.utc).isoformat(), 'scope': __doc__,
        'source_sha256': sha(Path(__file__).read_bytes()),
        'source_pins_sha256': sha((HERE / 'PUBLICATION_REVISION_SOURCE_PINS.json').read_bytes()),
        'current_origins_verified': 14, 'preserved_seals': {k: {'sha256': v[0], 'members': v[1]} for k,v in seals.items()},
        'changed_nine_manifest_members': changed_members,
        'generation01_commit': old_commit, 'generation01_nine_member_recovery': recovery,
        'generation01_external_metadata_recovery': recovered_metadata,
        'unchanged_helper_git_and_live_bytes_verified': True,
        'full_actual_diff_equals_supplied_diff': True, 'complete_diff': diff,
        'complete_revised_evidence_paragraph': paragraph,
        'science_canonical_citations_and_final_physical_obligations_byte_unchanged': True,
        'provenance_links': link_rows, 'recorded_mechanical_failure_and_repair': reason,
        'new_note_sha256': sha(note.encode()), 'new_manifest_sha256': sha((NEW/'metadata'/manifest_name).read_bytes()),
        'new_input_fingerprint_sha256': fp, 'declared_inputs': list(inputs),
        'full_scientific_payload_leaf_counts': dict(counts), 'scientific_differences': [],
        'only_excluded_payload_fields': timers, 'new_stage_records': result['stages'],
        'new_result_sha256': sha(result_bytes), 'new_result_bytes': len(result_bytes),
        'new_cache_sha256': sha(cache), 'new_cache_bytes': len(cache),
        'full_result_execution_stdout_cache_exact': True,
        'external_run_seconds': execution['elapsed_sec'], 'wrapper_seconds': result['elapsed_seconds'],
        'programs_or_cache_helpers_imported_or_executed': [], 'other_active_packets_opened': [],
        'scope_limits': ['No scientific rerun or new independent reconstruction.',
                         'No mechanical gate execution or retained audit; root separately checks the full evidence package and allowlist.',
                         'Recovery checked for prior pinned sources, not an inventory audit of all 65 publication files.',
                         'Earlier live origins intentionally changed; earlier frozen snapshots and seals remain unchanged.'],
        'check_failures': []
    }, indent=2))


if __name__ == '__main__':
    main()
