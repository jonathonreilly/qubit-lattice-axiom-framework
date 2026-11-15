"""Focused B1 affected review; exact set oracle and frozen-source executions."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations
from pathlib import Path
import inspect
import json
import os
import subprocess
import sys

C = Path(__file__).resolve().parent
ROOT = Path('/Users/jonBridger/Toy Physics/.claude/worktrees/yang-mills-proof-df9972')
assert Path.cwd() == ROOT
PIN = {'fixed': '0bcd86c97aa91b6897241f6998693de15c6131e54785c77a32ee6beb097300b8',
       'original': '63256a04b6d2fc46dad13ee26ae0b0c592e93ac7d271157076ef32d23650fdbc'}
CASES = {
    'baseline': ('fixed', None, None, 0, None),
    'original_active': ('original', 'output_full = norm(grouped, out_labels, allv, allv, 1)',
                        'output_full = norm(grouped, out_labels, lam, lam, 1)', 0, None),
    'both_active': ('fixed', 'return norm(grouped, out_labels, allv, allv, 1)',
                    'return norm(grouped, out_labels, lam, lam, 1)', 1, 'exact_cycle_output_full_norm'),
    'roots_active': ('fixed', 'return norm(grouped, out_labels, allv, allv, 1)',
                     'return norm(grouped, out_labels, lam, allv, 1)', 1, 'exact_inactive_root_output_full_norm'),
    'weight_active': ('fixed', 'return norm(grouped, out_labels, allv, allv, 1)',
                      'return norm(grouped, out_labels, allv, lam, 1)', 1, 'exact_cycle_output_full_norm'),
}


def source(kind):
    p = C / ('lib1_check.py' if kind == 'fixed' else 'lib1_norm_control_original.py')
    b = p.read_bytes()
    assert sha256(b).hexdigest() == PIN[kind]
    return p, b.decode()


def load(case):
    kind, before, after, *_ = CASES[case]
    p, s = source(kind)
    if before is not None:
        assert s.count(before) == 1
        s = s.replace(before, after)
    namespace = {'__name__': 'review_lib1_loaded_checker', '__file__': str(p)}
    exec(compile(s, str(p) + '::review-' + case, 'exec'), namespace)
    return namespace, {'source_path': str(p.relative_to(ROOT)),
                       'base_source_sha256': PIN[kind],
                       'compiled_source_sha256': sha256(s.encode()).hexdigest(),
                       'substitution': None if before is None else {'from': before, 'to': after},
                       'execution': 'Exact function definitions compiled; main() invoked. Only the I/O footer is skipped.'}


def members(mask):
    return frozenset(i for i in range(mask.bit_length()) if mask & (1 << i))


def mask(vertices):
    return sum(1 << i for i in vertices)


def oracle(coefficients, roots, weighted):
    # An independently specified sum at each explicit set-valued root.
    return max((sum((c * 2 ** len(label & weighted)
                     for label, c in coefficients.items() if v in label), Fraction(0))
                for v in roots), default=Fraction(0))


def check_call(function, coefficients, all_vertices, retained):
    by_mask = {mask(s): c for s, c in coefficients.items()}
    got = function(by_mask, {m: m for m in by_mask}, mask(all_vertices), mask(retained))
    expected = oracle(coefficients, all_vertices, all_vertices)
    assert got == expected, ('independent_full_norm', coefficients, all_vertices, retained, got, expected)
    return got


def connected(vertices, adjacency):
    if not vertices:
        return False
    visited = {min(vertices)}
    while True:
        grown = visited | {w for v in visited for w in adjacency[v] if w in vertices}
        if grown == visited:
            return visited == set(vertices)
        visited = grown


def saturate(initial, retained, adjacency):
    current = set(initial)
    while True:
        following = current | {w for v in current for w in adjacency[v] if w not in retained}
        if following == current:
            return frozenset(current)
        current = following


def independent():
    namespace, binding = load('baseline')
    guard = namespace['guard']  # Resource monitor only; graph/norm oracle is independent.
    full = namespace['full_output_norm']
    guard('independent set oracle: start')
    counts = Counter()
    discriminating = Counter()
    for n in range(1, 5):
        universe = frozenset(range(n))
        possible_edges = list(combinations(range(n), 2))
        subsets = [members(s) for s in range(1 << n)]
        for selected in range(1 << len(possible_edges)):
            adjacency = {v: set() for v in universe}
            for i, (v, w) in enumerate(possible_edges):
                if selected & (1 << i):
                    adjacency[v].add(w)
                    adjacency[w].add(v)
            if not connected(universe, adjacency):
                continue
            counts['connected_graphs'] += 1
            if counts['connected_graphs'] % 10 == 0:
                guard('independent graph ' + str(counts['connected_graphs']))
            inputs = [s for s in subsets if connected(s, adjacency)]
            for retained in subsets:
                grouped = {}
                for initial in inputs:
                    if initial & retained:
                        y = saturate(initial, retained, adjacency)
                        coefficient = Fraction(1 + sum(v + 1 for v in initial), 1 + len(initial))
                        grouped[y] = grouped.get(y, Fraction(0)) + coefficient
                        counts['saturated_inputs'] += 1
                value = check_call(full, grouped, universe, retained)
                counts['full_norm_comparisons'] += 1
                discriminating['roots_only'] += value != oracle(grouped, retained, universe)
                discriminating['weight_only'] += value != oracle(grouped, universe, retained)
                discriminating['both_active'] += value != oracle(grouped, retained, retained)
    for order in permutations(range(4)):
        universe = frozenset(order)
        adjacency = {v: {order[(i-1) % 4], order[(i+1) % 4]} for i, v in enumerate(order)}
        retained = frozenset([order[0]])
        y = saturate(retained, retained, adjacency)
        assert y == universe
        for q in [Fraction(1, 3), Fraction(1), Fraction(7, 2)]:
            assert oracle({retained: q}, universe, universe) == 2*q
            assert check_call(full, {y: q}, universe, retained) == 16*q
            assert oracle({y: q}, retained, retained) == 2*q
            counts['cycle_permutation_coefficient_cases'] += 1
    paths = []
    for order in permutations(range(3)):
        left, middle, right = order
        universe = frozenset(order)
        retained = frozenset([left, right])
        adjacency = {left: {middle}, middle: {left, right}, right: {middle}}
        yl = saturate({left}, retained, adjacency)
        yr = saturate({right}, retained, adjacency)
        assert yl == frozenset([left, middle]) and yr == frozenset([middle, right])
        grouped = {yl: Fraction(1, 3), yr: Fraction(2, 5)}
        assert check_call(full, grouped, universe, retained) == Fraction(44, 15)
        assert oracle(grouped, retained, universe) == Fraction(8, 5)
        assert oracle(grouped, retained, retained) == Fraction(4, 5)
        root_values = {v: oracle(grouped, {v}, universe) for v in universe}
        assert root_values[middle] > max(root_values[left], root_values[right])
        paths.append({'order': order, 'root_sums': {v: str(s) for v, s in root_values.items()}})
        counts['path_permutations'] += 1
    guard('independent set oracle: completion')
    return {'binding': binding, 'counts': dict(counts),
            'discriminating_oracle_comparisons': dict(discriminating), 'asymmetric_paths': paths,
            'resources': namespace['REPORT']['resources'],
            'limits': 'Finite implementation checks only; no whole-library theorem rereview.'}


def child(case):
    namespace, binding = load(case)
    calls = Counter()
    if case == 'baseline':
        original = namespace['full_output_norm']
        def traced(coeff, labels, allv, lam):
            value = original(coeff, labels, allv, lam)
            grouped = {}
            for key, coefficient in coeff.items():
                support = members(labels[key])
                grouped[support] = grouped.get(support, Fraction(0)) + coefficient
            assert value == oracle(grouped, members(allv), members(allv)), 'review_runtime_full_norm_oracle'
            caller = inspect.currentframe().f_back.f_code.co_name
            calls[caller] += 1
            return value
        namespace['full_output_norm'] = traced
    status, reason, code = 'completed', None, 0
    try:
        namespace['main']()
        if case == 'baseline':
            assert dict(calls) == {'exercise': 2184, 'mutations': 2}, dict(calls)
    except namespace['ResourceRefusal'] as exc:
        status, reason, code = 'resource_refusal', str(exc), 75
    except Exception as exc:
        status, reason, code = 'failed', repr(exc), 1
    result = {'case': case, 'status': status, 'reason': reason, 'exit_code': code,
              'binding': binding, 'runtime_full_output_calls': dict(calls),
              'author_report': namespace['REPORT']}
    print(json.dumps(result, indent=2))
    return code


def main():
    if len(sys.argv) == 3 and sys.argv[1] == '--child':
        return child(sys.argv[2])
    independent_result = independent()
    env = os.environ.copy()
    settings = {k: '1' for k in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                                 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS', 'PYTHONDONTWRITEBYTECODE']}
    env.update(settings)
    cases = []
    for case, (_kind, _old, _new, expected_code, expected_assertion) in CASES.items():
        command = ['nice', '-n', '10', sys.executable, '-B', str(Path(__file__).resolve()), '--child', case]
        run = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, timeout=70)
        out = C / ('review_lib1_norm_' + case + '_stdout.json')
        err = C / ('review_lib1_norm_' + case + '_stderr.txt')
        with out.open('xb') as f:
            f.write(run.stdout)
        with err.open('xb') as f:
            f.write(run.stderr)
        report = json.loads(run.stdout)
        expected_reason = None if expected_assertion is None else 'AssertionError(' + repr(expected_assertion) + ')'
        observed = run.returncode == expected_code and report['reason'] == expected_reason and not run.stderr
        if case == 'original_active':
            observed = observed and report['author_report']['mutations']['identify_active_and_full_norms'] == 'rejected by exact witness'
        cases.append({'case': case, 'command': command, 'expected_exit': expected_code,
                      'actual_exit': run.returncode, 'expected_assertion': expected_assertion,
                      'actual_reason': report['reason'], 'expected_outcome_observed': observed,
                      'compiled_source_sha256': report['binding']['compiled_source_sha256'],
                      'stdout_sha256': sha256(run.stdout).hexdigest(), 'stderr_sha256': sha256(run.stderr).hexdigest()})
    original_counts = json.loads((C / 'lib1_check_result.json').read_text())['counts']
    corrected_counts = json.loads((C / 'review_lib1_norm_baseline_stdout.json').read_text())['author_report']['counts']
    assert all(corrected_counts.get(k) == v for k, v in original_counts.items()), 'original_count_regression'
    added = {k: v for k, v in corrected_counts.items() if k not in original_counts}
    assert len(added) == 7 and all(v == 1 for v in added.values()), added
    result = {'created_utc': datetime.now(timezone.utc).isoformat(),
              'criteria_sha256': sha256((C / 'review_lib1_norm_criteria.md').read_bytes()).hexdigest(),
              'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'independent_oracle': independent_result, 'source_executions': cases,
              'unchanged_original_predicate_counts': original_counts, 'added_exact_predicates': added,
              'resource_environment': settings, 'all_expected_outcomes': all(x['expected_outcome_observed'] for x in cases)}
    out = C / 'review_lib1_norm_result.json'
    with out.open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps({'oracle_counts': independent_result['counts'],
                      'source_cases': [{k: v for k, v in x.items() if k in ['case', 'actual_exit', 'actual_reason', 'expected_outcome_observed']} for x in cases],
                      'all_expected_outcomes': result['all_expected_outcomes']}, indent=2))
    assert result['all_expected_outcomes'], 'source_execution_outcome'
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
