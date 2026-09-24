#!/usr/bin/env python3
"""Released-source and stored-toy record consistency; no science-runner execution."""
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE / 'released_sources'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    pins = json.loads((HERE / 'POST_SOURCE_PINS.json').read_text())
    assert sha(HERE / 'PRE_SEAL.json') == pins['pre_seal_sha256']
    pre = json.loads((HERE / 'PRE_SEAL.json').read_text())
    for name, want in pre['files'].items():
        assert sha(HERE / name) == want, name
    for row in pins['sources']:
        for path in [Path(row['source']), HERE / row['snapshot']]:
            assert path.stat().st_size == row['bytes'] and sha(path) == row['sha256'], str(path)
    for name in ('AUTHOR_SEAL.json', 'CONTROL_SEAL.json'):
        seal = json.loads((ROOT / name).read_text())
        for member, want in seal['files'].items():
            assert sha(ROOT / member) == want, member

    result = json.loads((ROOT / 'RECENT_BIRTH_CONTROL_RESULTS.json').read_text())
    assert (ROOT / 'RECENT_BIRTH_CONTROL_RESULTS.json').read_bytes() == (ROOT / 'CONTROL.stdout.txt').read_bytes()
    assert (ROOT / 'CONTROL.stderr.txt').read_bytes() == b''
    execution = json.loads((ROOT / 'CONTROL_EXECUTION.json').read_text())
    assert execution['exit_code'] == 0
    runner_hash = sha(ROOT / 'recent_birth_controls.py')
    assert result['source_sha256'] == execution['script_sha256'] == runner_hash
    par = result['parameters']
    delta, kappa, g, b, r = (par[x] for x in ('delta', 'kappa', 'g', 'b', 'r'))
    omega = delta*g
    # Hand-derived solution: X_22=1/(2kappa), X_11=X_22+kappa/(2omega^2),
    # X_12=i/(2omega). No numerical Lyapunov solver is imported or executed.
    integral_formula = 1/kappa + kappa/(2*omega*omega)
    integral_error = abs(integral_formula-result['fast_integral_infinite'])
    assert integral_error < 3e-14
    Iinf, IA = result['fast_integral_infinite'], result['fast_integral_capped']
    assert 0 < IA < Iinf
    residuals = []
    for row in result['rows']:
        eps, t = row['epsilon'], row['t']
        lam = kappa*(b+eps*eps*r)
        q = math.exp(-lam*t)
        q0 = math.exp(-kappa*b*t)
        comparisons = {
            'initial_probability': (row['initial_sector_probability'], q),
            'born_low_probability': (row['born_low_probability'], kappa*b*(-math.expm1(-lam*t))/lam),
            'limiting_mean': (row['limiting_mean'], kappa*delta*r*q0*Iinf),
            'limiting_scaled_variance': (row['limiting_eps4_variance'], kappa*delta*delta*r*q0*Iinf),
            'recent_high_target': (row['recent_high_probability_target'], kappa*r*q0*IA),
            'recent_mean_target': (row['recent_mean_target'], kappa*delta*r*q0*IA),
            'recent_variance_target': (row['recent_variance_target'], kappa*delta*delta*r*q0*IA),
            'Fisher_ratio': (row['Fisher_over_four_variance'], row['full_Fisher']*eps**4/(4*row['eps4_full_variance']))
        }
        errors = {name: abs(a-c) for name, (a, c) in comparisons.items()}
        errors['total_probability'] = abs(sum(row[name] for name in (
            'initial_sector_probability', 'born_low_probability', 'born_high_probability', 'terminal_probability'))-1)
        assert max(errors.values()) < 3e-14, errors
        assert row['eps4_recent_within_path_variance'] <= row['eps4_full_variance']+1e-10
        assert row['recent_high_probability_over_eps4'] > 0
        assert row['field_only_mutant_high_probability'] == 0
        assert row['born_density_min_eigenvalue'] > -1e-13
        residuals.append({'t': t, 'epsilon': eps, 'maximum_stored_scalar_consistency_error': max(errors.values())})
    report = {
        'status': 'PASS-evidence-correspondence-and-stored-scalar-consistency',
        'checker_sha256': sha(__file__),
        'pre_seal_sha256': pins['pre_seal_sha256'],
        'pre_members_unchanged': len(pre['files']),
        'original_snapshot_pairs_verified': len(pins['sources']),
        'root_runner_sha256': runner_hash,
        'complete_stdout_equals_complete_result_bytes': True,
        'stderr_empty': True,
        'recorded_exit_code': execution['exit_code'],
        'recorded_wall_seconds': execution['seconds'],
        'recorded_internal_seconds': result['elapsed_seconds'],
        'toy_infinite_integral_from_explicit_2x2_Lyapunov_solution': integral_formula,
        'toy_infinite_integral_formula_discrepancy': integral_error,
        'rows_checked': residuals,
        'mutant_scope': 'field_only_mutant_high_probability is a stored literal zero comparator, not a separately executed mutation.',
        'root_toy_imported_or_executed': False,
        'independent_full_cube_numerical_replication': False,
        'scope': 'Frozen identities, full output correspondence and arithmetic consistency only. Toy formulas were analytically compared in POST; these checks do not prove the cube limit or establish interval enclosures.'
    }
    (HERE / 'POST_EVIDENCE_CHECK.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
