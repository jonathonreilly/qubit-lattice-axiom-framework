#!/usr/bin/env python3
"""Post-seal source/witness comparison without rerunning author controls."""
from pathlib import Path
from decimal import Decimal, localcontext
from datetime import datetime, timezone
import hashlib
import json
import math

OUT = Path(__file__).resolve().parent
RAW = OUT.parent


def identity(p):
    b = p.read_bytes()
    return {'path': str(p), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}


def main():
    pre = json.loads((OUT / 'PRE_COMPARISON_SEAL.json').read_text())
    for r in [pre['primary_source']] + pre['reused_dependencies'] + pre['artifacts']:
        assert identity(Path(r['path'])) == r
    p = RAW / 'dimer_routed_diffusive_gap_checks/RESULTS.json'
    author = json.loads(p.read_text())
    sources = []
    for name, sha in author['sources'].items():
        row = identity(RAW / name)
        assert row['sha256'] == sha
        sources.append(row)
    own = json.loads((OUT / 'INDEPENDENT_RESULTS.json').read_text())
    own_cases = {(r['N'], r['kind']): r for r in own['contracted_paths_and_gap_controls']}
    assert len(author['physical_loads']) == 2
    for r in author['physical_loads']:
        n = r['N']
        assert r['ordered_pairs'] == n ** 6
        assert r['physical_edges'] == 3 * n ** 3
        assert r['exact_load_per_edge'] == n ** 4 // 4
    geometric = []
    assert len(author['contracted_loads']) == 6
    for r in author['contracted_loads']:
        n = r['N']; k = n ** 3 // 2
        assert r['K'] == k and r['unordered_reference_pairs'] == math.comb(k, 2)
        assert r['largest_physical_edge_multiplicity'] <= 2
        assert r['maximum_contracted_path_length'] <= 3 * n // 2
        assert r['maximum_reference_path_load'] <= r['path_load_bound'] == n ** 4 // 2
        assert r['maximum_word_edge_load'] <= r['word_load_bound'] == n ** 4
        assert r['erased_projected_vertices'] == 0
        assert r['all_immutable_endpoint_words_exact'] is True
        assert r['proven_unit_rate_H_gap_lower_bound'] == 1 / (4 * n * (3 * n - 1))
        rec = {'N': n, 'kind': r['kind'], 'saved_bounds_arithmetic_valid': True}
        if r['kind'] != 'irregular':
            ref = own_cases[n, r['kind']]
            assert r['maximum_contracted_path_length'] == ref['maximum_simple_path_length']
            assert r['maximum_reference_path_load'] == ref['maximum_contracted_path_load']
            assert r['maximum_word_edge_load'] == ref['maximum_word_edge_use']
            # Author diagonalizes the unit-rate simple graph; ours used k0/2
            # with k0=1, so the numerical one-marker gaps differ by exactly 2.
            error = abs(r['numerical_one_exceptional_color_gap'] - 2 * ref['numerical_one_marker_simple_gap_k0_one'])
            assert error < 2e-12
            rec.update(shared_fixture_path_counts_exact=True, scaled_gap_error=error)
        else:
            rec['independent_irregular_fixture_differs'] = True
        geometric.append(rec)
    schedules = []
    with localcontext() as ctx:
        ctx.prec = 80
        for r in author['schedule']:
            n = r['N']; k = n ** 3 // 2
            dn = Decimal(n)
            inverse = Decimal(80) * dn * (3 * dn - 1) / 11  # k0=11/10
            # Expanded expression independently fixes the N^5 leading term.
            waiting = ((6 * dn ** 5 - 2 * dn ** 4) * Decimal(14).ln()
                       + 8 * dn * (3 * dn - 1) * (4 * dn.ln() - Decimal(2).ln())) * 10 / 11
            gap = 1 / inverse
            err_t = abs(Decimal(str(r['sufficient_waiting_time'])) - waiting) / waiting
            err_g = abs(Decimal(str(r['gap_lower_bound'])) - gap) / gap
            assert err_t < Decimal('5e-15') and err_g < Decimal('5e-15')
            assert r['K'] == k and r['epsilon'] == n ** -4
            assert r['improvement_factor'] == (k - 1) / (2 * n)
            schedules.append({'N': n, 'waiting_time_relative_error': str(err_t),
                              'gap_relative_error': str(err_g), 'independent_waiting_time_80_digits': str(waiting)})
    log = RAW / 'DIMER_ROUTED_DIFFUSIVE_GAP_RUN.log'
    stderr = RAW / 'DIMER_ROUTED_DIFFUSIVE_GAP_RUN.stderr'
    lines = log.read_text().splitlines()
    assert lines[0] == 'exact all-vertex physical loads passed'
    assert [json.loads(s) for s in lines[1:]] == author['contracted_loads']
    assert not stderr.read_bytes()
    receipt = {
        'created_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Complete author source/evidence read; authentication and selected shared-fixture/arithmetic comparison, not author scientific rerun.',
        'precomparison_artifacts_authenticated': len(pre['artifacts']),
        'reused_dependencies_authenticated': len(pre['reused_dependencies']),
        'author_sources': sources,
        'author_evidence': [identity(p), identity(log), identity(stderr)],
        'geometry_comparison': geometric,
        'schedule_comparison': schedules,
        'author_log_rows_equal_results': True,
        'unresolved_findings': [],
        'author_scientific_suite_rerun': False,
        'dynamic_aggregates_or_finite_wavelength_followup_accessed': False,
    }
    (OUT / 'POST_COMPARISON_RESULTS.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({'status': 'pass', 'source_bindings': len(sources), 'geometry_rows': len(geometric),
                      'high_precision_schedule_rows': len(schedules), 'unresolved_findings': []}))


if __name__ == '__main__':
    main()
