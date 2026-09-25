"""Read-only released-source correspondence; no author/runtime imports or writes.

Checks exact stored bytes and arithmetic already present in recorded rows. The
only subprocess is git show of the four explicitly released parent paths.
"""
from __future__ import annotations
import argparse
import ast
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import re
import stat
import subprocess

HERE = Path(__file__).resolve().parent
EXT = Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth')
PUB = EXT / 'native-charge-threshold-publication'

def sha(body):
    return hashlib.sha256(body).hexdigest()

def stats(path):
    s = path.stat()
    return {k: getattr(s, 'st_' + k) for k in ('mode', 'dev', 'ino', 'size', 'mtime_ns', 'ctime_ns')}

def read(rel):
    return (HERE / rel).read_bytes()

def data(rel):
    return json.loads(read(rel))

def literal(tree, name):
    nodes = [n for n in tree.body if isinstance(n, ast.Assign)
             and any(isinstance(t, ast.Name) and t.id == name for t in n.targets)]
    assert len(nodes) == 1, name
    return ast.literal_eval(nodes[0].value)

def require_equal_payload(left, right, excluded=()):
    counts = Counter()
    timings = []
    def visit(a, b, path):
        assert type(a) is type(b), (path, type(a).__name__, type(b).__name__)
        if path in excluded:
            assert isinstance(a, float) and math.isfinite(a) and a > 0
            assert math.isfinite(b) and b > 0
            timings.append({'path': path, 'author': a, 'public': b})
        elif isinstance(a, dict):
            assert a.keys() == b.keys(), path
            for k in a:
                visit(a[k], b[k], path + '/' + k)
        elif isinstance(a, list):
            assert len(a) == len(b), path
            for i, (x, y) in enumerate(zip(a, b)):
                visit(x, y, path + '/' + str(i))
        else:
            assert a == b, (path, a, b)
            counts[type(a).__name__] += 1
    visit(left, right, '')
    return {'equal_nontiming_leaves': sum(counts.values()), 'equal_leaf_types': dict(counts),
            'permitted_timing_fields': timings, 'other_differences': []}

def verify_seal(snapshot_root, name):
    seal = data(snapshot_root + '/' + name)
    for item in seal['members']:
        p = Path(item['path'])
        assert not p.is_absolute() and '..' not in p.parts
        body = read(snapshot_root + '/' + item['path'])
        assert sha(body) == item['sha256'] and len(body) == item['bytes'], item['path']
    return {'sha256': sha(read(snapshot_root + '/' + name)), 'members': len(seal['members'])}

def main(check_own_seal=False):
    pins = data('SOURCE_PINS.json')
    for row in pins['members']:
        body = read(row['snapshot'])
        assert sha(body) == row['sha256'] and len(body) == row['bytes'], row['snapshot']
        origin = Path(row['origin'])
        assert origin.read_bytes() == body, row['origin']
        assert stats(origin) == row['original_stat'], ('original stat changed', row['origin'])
    seals = {
        'author': verify_seal('frozen/author', 'AUTHOR_SEAL.json'),
        'prior_PRE': verify_seal('frozen/prior_checker', 'PRE_SEAL.json'),
        'prior_POST': verify_seal('frozen/prior_checker', 'POST_SEAL.json'),
    }
    manifest = data('frozen/process/NATIVE_CHARGE_THRESHOLD_FROZEN_SOURCES.json')
    working = data('frozen/process/NATIVE_CHARGE_THRESHOLD_PUBLICATION_WORKING_SOURCES.json')
    assert all(manifest[k] == v for k, v in working.items())
    pfx = 'frozen/publication/'
    for path, expected in manifest['files_sha256'].items():
        assert sha(read(pfx + path)) == expected, path
    for path, expected in manifest['source_files_sha256'].items():
        assert sha(read(pfx + path)) == expected, path
    git_parents = []
    for path in manifest['parent_paths']:
        args = ['git', '-C', str(PUB), 'show', manifest['base_revision'] + ':' + path]
        result = subprocess.run(args, capture_output=True,
                                env=dict(os.environ, GIT_OPTIONAL_LOCKS='0'))
        assert result.returncode == 0 and not result.stderr, (args, result.stderr)
        assert result.stdout == read(pfx + path)
        git_parents.append({'revision': manifest['base_revision'], 'path': path,
                            'sha256': sha(result.stdout), 'bytes': len(result.stdout)})

    # Parse the generation script as inert source, not executable Python.
    builder = ast.parse(read('frozen/process/build_native_charge_threshold_publication.py'))
    author_note = read('frozen/author/FIRST_BIRTH_CHARGE_AND_SEPARATED_THRESHOLD_ROOT.md').decode()
    transformed = author_note
    for replacement in manifest['presentation_replacements']:
        assert transformed.count(replacement['old']) == 1
        transformed = transformed.replace(replacement['old'], replacement['new'])
    increment = manifest['heading_level_increment']
    assert increment == 2
    transformed = re.sub(r'^(#{1,6}) ', lambda m: '#' * (len(m[1]) + increment) + ' ',
                         transformed, flags=re.M)
    canonical = read(pfx + manifest['note']).decode()
    embedded = canonical.split('## Complete personal argument\n\n', 1)[1].split(
        '\n## Reproduction and observation boundary\n', 1)[0]
    assert embedded == transformed
    parents = manifest['parent_paths']
    header = ('---\nclaim_id: ' + Path(manifest['note']).stem.lower() + '\nclaim_type: bounded_theorem\n'
              'claim_scope: "Conditional global flat separated threshold, ordered weak-coupling energy limit, '
              'and actual-birth charge/comparison-projector distinctions; no physical mass, finite-coupling '
              'binding exclusion or selected particle."\nupstream_dependencies:\n')
    header += ''.join('  - ' + Path(p).stem.lower() + '\n' for p in parents)
    header += 'runner: ' + manifest['runner'] + '\n---\n\n'
    front = literal(builder, 'front')
    footer_node = next(n for n in builder.body if isinstance(n, ast.Assign)
                       and any(isinstance(t, ast.Name) and t.id == 'footer' for t in n.targets))
    assert isinstance(footer_node.value, ast.BinOp) and isinstance(footer_node.value.left, ast.Constant)
    footer = ast.literal_eval(footer_node.value.left)
    footer += ''.join('- [' + Path(p).stem + '](' + Path(p).name + ').\n' for p in parents)
    assert canonical == header + front + transformed + footer

    runtime_rel = manifest['runtime'][0]
    runtime = read(pfx + runtime_rel)
    assert runtime == read('frozen/author/two_record_threshold_and_charge_controls.py')
    assert runtime == read('frozen/author/attempt05/two_record_threshold_and_charge_controls.py')
    wrapper = read(pfx + manifest['runner'])
    tree = ast.parse(wrapper)
    declared = literal(tree, 'AUDIT_INPUT_PATHS')
    expected_inputs = tuple([manifest['note'], *parents, runtime_rel])
    assert declared == expected_inputs and len(declared) == 6
    assert literal(tree, 'AUDIT_TIMEOUT_SEC') == 120
    assert literal(tree, 'OUTPUT_DIRECTORY') == manifest['output_directory']
    assert literal(tree, 'RUNTIME') == runtime_rel
    base_wrapper = literal(builder, 'wrapper')
    template = [n.value.value for n in builder.body if isinstance(n, ast.AugAssign)
                and isinstance(n.target, ast.Name) and n.target.id == 'wrapper'
                and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str)]
    assert len(template) == 1
    rebuilt_wrapper = base_wrapper + 'AUDIT_TIMEOUT_SEC = 120\nAUDIT_INPUT_PATHS = ' + repr(declared) + '\n'
    rebuilt_wrapper += 'OUTPUT_DIRECTORY = ' + repr(manifest['output_directory']) + '\nRUNTIME = ' + repr(runtime_rel) + '\n'
    rebuilt_wrapper += template[0]
    rebuilt_wrapper = rebuilt_wrapper.replace("+'\\\\n'", "+'\\n'")
    assert rebuilt_wrapper.encode() == wrapper

    # Reimplement the documented v1 digest; do not import runner_cache.py.
    fingerprint = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
    input_rows = []
    for relative in declared:
        path = Path(relative)
        assert not path.is_absolute() and '..' not in path.parts and path.as_posix() == relative
        component = PUB
        for part in path.parts:
            component /= part
            assert not stat.S_ISLNK(component.lstat().st_mode), relative
        body = read(pfx + relative)
        encoded = relative.encode()
        fingerprint.update(len(encoded).to_bytes(8, 'big')); fingerprint.update(encoded)
        fingerprint.update(len(body).to_bytes(8, 'big')); fingerprint.update(body)
        input_rows.append({'path': relative, 'sha256': sha(body), 'bytes': len(body)})
    fingerprint = fingerprint.hexdigest()
    assert fingerprint == 'e79582accb27009c3fdf50430f9b51e79c7f8f9d15e9532d98c4c79fea8da46c'

    out = pfx + manifest['output_directory'] + '/'
    full_bytes = read(out + 'CHARGE_THRESHOLD_RESULTS.json')
    full = json.loads(full_bytes)
    original = data('frozen/author/attempt05/RESULT.json')
    payload = require_equal_payload(original, full, ('/elapsed_seconds',))
    assert payload['equal_nontiming_leaves'] == 6714
    assert len(payload['permitted_timing_fields']) == 1
    public = data(pfx + manifest['result'])
    stdout = read(out + 'charge_control.stdout.txt')
    stderr = read(out + 'charge_control.stderr.txt')
    assert not stderr
    omitted = {'unwrapped_rows', 'periodic_controls', 'reciprocity_controls', 'auxiliary_one_occupancy_kernel'}
    assert json.loads(stdout) == {k: v for k, v in full.items() if k not in omitted}
    assert full['source_sha256'] == public['runtime_source_sha256'] == sha(runtime)
    assert public['source_sha256'] == sha(wrapper)
    assert public['exit_code'] == 0 and public['stderr_bytes'] == 0
    assert public['stdout_bytes'] == len(stdout) and public['stdout_sha256'] == sha(stdout)
    assert public['all_assertions_passed'] is True
    assert public['complete_scientific_artifact'] == {
        'path': manifest['output_directory'] + '/CHARGE_THRESHOLD_RESULTS.json',
        'sha256': sha(full_bytes), 'bytes': len(full_bytes)}
    execution = data('frozen/process/NATIVE_CHARGE_THRESHOLD_PRIMARY_EXECUTION.json')
    assert execution['status'] == 'ok' and execution['exit_code'] == 0 and execution['stderr'] == ''
    assert execution['timeout_sec'] == 120
    assert execution['stdout'] == read(pfx + manifest['result']).decode() + 'TOTAL_PASS: 1\n'
    expected_cache = (
        '===== runner cache v1 =====\nrunner: ' + manifest['runner'] + '\nrunner_sha256: ' + sha(wrapper)
        + '\ninput_fingerprint_sha256: ' + fingerprint
        + '\ntimeout_sec: 120\nexit_code: 0\nelapsed_sec: ' + format(execution['elapsed_sec'], '.2f')
        + '\nstatus: ok\n----- stdout -----\n' + execution['stdout'][-200000:]
        + '\n----- stderr -----\n' + execution['stderr'][-50000:] + '\n')
    assert read(pfx + manifest['cache']).decode() == expected_cache

    # Arithmetic correspondence from complete saved rows; no primitive builder replay.
    denominator = full['denominator']
    deficits = {tuple(k): v for k, v in full['deficits']}
    assert denominator == 10**9 and len(deficits) == 13
    assert all(0 <= v < denominator for v in deficits.values())
    compact_rows = []
    for row in full['unwrapped_rows']:
        group = dict((tuple(k), v) for k, v in row['grouped_integer_row'])
        kind = tuple(row['type'])
        assert len(group) == len(row['grouped_integer_row'])
        assert sum(group.values()) == row['row_sum']
        residual = sum(c * (denominator - deficits.get(k, 0)) for k, c in group.items())
        residual -= 12096 * (denominator - deficits.get(kind, 0))
        assert residual == row['trial_residual_numerator'] and residual <= 0
        compact_rows.append({'type': row['type'], 'row_sum': row['row_sum'], 'grouped_entries': len(group),
                             'target_count': row['target_count'], 'residual_numerator': residual})
    old_rows = []
    for attempt, key in [('attempt01/stdout.json', 'classes'), ('attempt02/RESULT.json', 'rows'), ('attempt03/RESULT.json', 'rows')]:
        old = data('frozen/author/' + attempt)
        lookup = {tuple(x['type']): x for x in full['unwrapped_rows']}
        for row in old[key]:
            now = lookup[tuple(row['displacement_type'])]
            assert row['grouped_exact_row'] == now['grouped_integer_row']
            assert row['row_sum'] == now['row_sum']
        old_rows.append({'artifact': attempt, 'row_groups': len(old[key]),
                         'grouped_entries': sum(len(x['grouped_exact_row']) for x in old[key]),
                         'lp_success': old['lp_success'], 'message': old['lp_message']})
    short = data('frozen/author/attempt04/RESULT.json')
    assert short['denominator'] == denominator
    assert [(x['type'], x['numerator']) for x in short['deficit_numerators']] == [(x, y) for x, y in full['deficits']]
    assert [(x['type'], x['numerator_at_common_denominator']) for x in short['residuals']] == [
        (x['type'], x['trial_residual_numerator']) for x in full['unwrapped_rows']]
    kernel = full['auxiliary_one_occupancy_kernel']
    assert len(kernel) == 85 and sum(c for _, c in kernel) == 6048
    second = [[sum(c * p[i] * p[j] for p, c in kernel) for j in range(3)] for i in range(3)]
    assert second == full['auxiliary_kernel_second_moment'] == [[7392,0,0],[0,7392,0],[0,0,7392]]
    assert sum(c * sum(x*x for x in p)**2 for p,c in kernel) == 93696
    assert len(full['unwrapped_rows']) == 37 and len(full['periodic_controls']) == 68
    assert len(full['reciprocity_controls']) == 43 and full['near_total_row_defect'] == -1548
    for row in full['periodic_controls']:
        assert row['trial_residual_numerator'] <= 0
    charge_counts = Counter()
    for row in full['charge_controls']:
        m = row['occupied_sites_after_one_birth']
        assert Fraction(row['resolved_first_birth_color_line_weight']) == Fraction(1,m)
        assert Fraction(row['flat_coherent_first_birth_color_line_weight']) == Fraction(2,m)
        assert Fraction(row['uniform_minus_probability_minus_on_B']) == Fraction(2,m)
        charge_counts.update(row['counts'])
    assert charge_counts['resolved_primitive_outputs'] == 8448
    assert charge_counts['resolved_edge_sign_marks'] == 1704
    assert charge_counts['flat_coherent_edge_controls'] == 852
    assert sum(len(x['test_charge_rows']) for x in full['charge_controls']) == 15
    # Recheck every original after the complete pass, including the prior seals.
    for row in pins['members']:
        origin = Path(row['origin'])
        assert sha(origin.read_bytes()) == row['sha256']
        assert stats(origin) == row['original_stat'], row['origin']
    own_seal = verify_seal('.', 'PUBLICATION_COMPARISON_SEAL.json') if check_own_seal else None
    result = {
        'verified_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Read-only final correspondence by a newly exposed checker, not a blind reconstruction or scientific primary rerun.',
        'observed_origins_unchanged': len(pins['members']), 'prior_seals': seals,
        'frozen_publication_files': len(manifest['files_sha256']),
        'base_parent_origins': git_parents,
        'body_replacements': manifest['presentation_replacements'],
        'heading_increment': increment, 'complete_note_exact_builder_presentation': True,
        'wrapper_exact_builder_presentation': True, 'runtime_exact_author_source': True,
        'declared_inputs': input_rows, 'input_fingerprint_sha256': fingerprint,
        'cache_sha256': sha(read(pfx + manifest['cache'])),
        'cache_exact_execution_serialization': True,
        'execution_elapsed_sec': execution['elapsed_sec'],
        'primary_wrapper_elapsed_sec': public['elapsed_seconds'],
        'payload_comparison': payload,
        'full_artifact_sha256': sha(full_bytes), 'wrapper_result_sha256': sha(read(pfx + manifest['result'])),
        'stdout_projection_exact': True, 'empty_stderr': True,
        'stored_arithmetic_scope': 'Recomputed arithmetic of already recorded grouped rows and kernel; no primitive graph reconstruction or scientific code execution.',
        'all_37_stored_row_arithmetic': compact_rows, 'historical_row_correspondence': old_rows,
        'short_certificate_correspondence': True,
        'periodic_rows': 68, 'reciprocity_rows': 43, 'kernel_entries': 85,
        'charge_aggregate_counts': dict(charge_counts), 'charge_moment_rows': 15,
        'charge_raw_word_artifacts_available': False,
        'preserved_history_gap': 'attempt04 has saved result only; its original heredoc writer and separate execution receipt are absent from the author seal.',
        'own_seal': own_seal, 'all_checks_passed': True,
    }
    print(json.dumps(result, indent=2, allow_nan=False))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--seal', action='store_true')
    main(parser.parse_args().seal)
