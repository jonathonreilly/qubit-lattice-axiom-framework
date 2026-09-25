"""Read-only binding and exact stored-certificate checks for this PRE."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
import difflib
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def main():
    pins = load(HERE/'SOURCE_PINS_INITIAL.json')
    for row in pins['scientific_sources']:
        origin = Path(row['origin'])
        assert sha(origin) == sha(HERE/row['snapshot']) == row['sha256']
        repository = origin.parent.parent
        data = subprocess.check_output(['git', 'show', row['git_revision']+':'+row['git_path']], cwd=repository)
        assert hashlib.sha256(data).hexdigest() == row['sha256']
    for row in pins['instructions']:
        if 'origin' in row:
            data = Path(row['origin']).read_bytes()
        else:
            data = subprocess.check_output(['git', 'show', row['git_revision']+':'+row['git_path']],
                                           cwd=row['origin_git_repository'])
        assert hashlib.sha256(data).hexdigest() == sha(HERE/row['snapshot']) == row['sha256']
    consistency = load(HERE/'INSTRUCTION_SOURCE_CONSISTENCY.json')
    for row in consistency['sources']:
        assert sha(Path(row['origin'])) == sha(HERE/row['snapshot']) == row['sha256']
    evidence = []
    results = []
    for attempt in ('control_attempt01', 'control_attempt02'):
        directory = HERE/attempt
        receipt = load(directory/'EXECUTION.json')
        result = load(directory/'CONTROL_RESULTS.json')
        assert receipt['exit_code'] == 0 and (directory/'stderr.log').read_bytes() == b''
        assert receipt['source_sha256'] == sha(directory/'ground_filling_control.py') == result['source_sha256']
        assert receipt['stdout_sha256'] == sha(directory/'stdout.log') == sha(directory/'CONTROL_RESULTS.json')
        assert result['all_exact_assertions_passed'] is True
        evidence.append({'attempt': attempt, 'execution_sha256': sha(directory/'EXECUTION.json'),
                         'source_sha256': receipt['source_sha256'],
                         'result_sha256': sha(directory/'CONTROL_RESULTS.json'),
                         'exit_code': 0, 'stderr_bytes': 0,
                         'elapsed_seconds': receipt['duration_seconds']})
        results.append(result)
    old, data = results
    assert sha(HERE/'ground_filling_control.py') == data['source_sha256']
    assert sha(HERE/'CONTROL_RESULTS.json') == sha(HERE/'control_attempt02/CONTROL_RESULTS.json')
    for key in ('local_certificates', 'rayleigh_rows', 'geometry_rows'):
        assert old[key] == data[key]
    for before, after in zip(old['physical_rows'], data['physical_rows']):
        assert all(before[key] == after[key] for key in before)
        assert set(after)-set(before) == {'max_cycle_coordinate_displacement_l1', 'three_winding_cycles_exactly_reconstructed'}
        assert after['max_cycle_coordinate_displacement_l1'] <= 4
        assert after['three_winding_cycles_exactly_reconstructed'] is True
    difference = ''.join(difflib.unified_diff(
        (HERE/'control_attempt01/ground_filling_control.py').read_text().splitlines(keepends=True),
        (HERE/'ground_filling_control.py').read_text().splitlines(keepends=True),
        fromfile='successful_attempt01', tofile='successful_attempt02'))
    (HERE/'CONTROL_EXTENSION_DIFF.txt').write_text(difference)
    certificates = data['local_certificates']
    assert len(certificates) == 2
    mask_total = group_total = 0
    for certificate in certificates:
        r = certificate['r']
        expected = {(ua, uc, w) for w in range(r+1)
                    for ua in range(w, w+7-r) for uc in range(w, w+7-r)}
        seen = {(row['ua'], row['uc'], row['w']) for row in certificate['groups']}
        assert seen == expected and len(seen) == len(certificate['groups'])
        assert sum(row['occupancy_masks'] for row in certificate['groups']) == 2**(12-r)
        c, d = F(certificate['sharp_local_low_slope']), F(certificate['sharp_local_hole_slope'])
        assert c == {1: F(69,2), 2: F(37)}[r]
        assert d == {1: F(24), 2: F(23)}[r]
        a = certificate['empty_return_count']
        for row in certificate['groups']:
            occupied = row['ua']+row['uc']
            assert F(row['low_bound_slack']) == a+c*occupied-row['return_count'] >= 0
            assert F(row['hole_bound_slack']) == d*(12-occupied)-row['return_count'] >= 0
        assert certificate['wrong_omitted_common_exclusion_and_exchange_masks_rejected'] > 0
        mask_total += certificate['masks_checked']
        group_total += len(certificate['groups'])
    assert mask_total == 3072 and group_total == 147
    assert len(data['rayleigh_rows']) == 48
    for row in data['rayleigh_rows']:
        assert F(row['ordered_union_rayleigh']) == F(row['independent_row_average'])
        assert F(row['difference']) == 0
    permitted_intervals = []
    for row in data['geometry_rows']:
        M = row['M_A_equals_B']
        low = F(row['weak_limit_lower_filling_from_trial'])*M
        high = F(row['weak_limit_upper_filling_from_trial'])*M
        allowed = [m for m in range(0,M+1,2) if low <= m <= high]
        permitted_intervals.append({'lengths': row['lengths'], 'M': M,
                                    'eventual_even_interval': [min(allowed), max(allowed)],
                                    'meaning': 'Exclusion bounds only; not minimizing sectors computed.'})
    assert [x['eventual_even_interval'] for x in permitted_intervals] == [[6,18],[8,28],[12,44],[18,66],[42,158]]
    ratios = []
    for s in range(4):
        low = F(1263-76*s, 7812-384*s)
        holes = F(1905-110*s, 5040-300*s)
        assert low >= F(23,148) and holes >= F(127,336)
        ratios.append({'short_axes': s, 'coarse_lower_fraction': str(low),
                       'coarse_hole_fraction': str(holes)})
    full = [row for row in data['physical_rows'] if row['m_B'] == row['M']]
    assert len(full) == 2
    assert all(row['gated_D'] == 0 and row['physical_return_paths'] == 0 and row['ungated_sum_E_squared'] > 0 for row in full)
    local_view = ['r\tua\tuc\tw\tR\tmasks\tlow_slack\thole_slack']
    for certificate in certificates:
        for row in certificate['groups']:
            local_view.append('\t'.join(str(row[key]) for key in ['r','ua','uc','w','return_count','occupancy_masks','low_bound_slack','hole_bound_slack']))
    assert (HERE/'LOCAL_CERTIFICATE_REVIEW.tsv').read_text() == '\n'.join(local_view)+'\n'
    ray_view = ['M\tm\tr\tunion_Rayleigh\trow_Rayleigh\tdifference']
    for row in data['rayleigh_rows']:
        ray_view.append('\t'.join(str(row[key]) for key in ['M','m','r','ordered_union_rayleigh','independent_row_average','difference']))
    assert (HERE/'RAYLEIGH_REVIEW.tsv').read_text() == '\n'.join(ray_view)+'\n'
    pins['refreshed_utc'] = datetime.now(timezone.utc).isoformat()
    pins['instruction_consistency'] = consistency
    pins['definition_only_task_supplement'] = {
        'path': 'SUPPLIED_PARAMETERIZATION.md', 'sha256': sha(HERE/'SUPPLIED_PARAMETERIZATION.md'),
        'source': 'Explicit parent task clarification; not a disclosed candidate argument.'}
    pins['control_evidence'] = evidence
    pins['read_coverage'] = 'Both scientific notes complete; all 147 local groups, 48 Rayleigh rows, 5 geometry and 10 final physical rows complete; no author packet or parent runner.'
    (HERE/'SOURCE_PINS.json').write_text(json.dumps(pins, indent=2)+'\n')
    report = {'verified_utc': datetime.now(timezone.utc).isoformat(),
              'verifier_sha256': sha(Path(__file__)), 'PRE_sha256': sha(HERE/'PRE.md'),
              'source_manifest_sha256': sha(HERE/'SOURCE_PINS.json'),
              'scientific_source_origins_verified': 2, 'scientific_Git_objects_verified': 2,
              'local_occupation_masks': mask_total, 'local_group_rows': group_total,
              'exact_Rayleigh_rows': 48, 'geometry_rows': 5, 'physical_rows': 10,
              'control_attempts': evidence, 'eventual_exclusion_intervals': permitted_intervals,
              'coarse_exact_fractions': ratios,
              'full_occupancy_ungated_counterexamples': full,
              'parent_or_author_control_imports_or_executions': 0,
              'other_active_packet_reads_declared': False,
              'limitations': 'Exact certificate and binding verification, not a numerical computation of minimizing sectors or a physical/thermodynamic phase test.'}
    text = json.dumps(report, indent=2)+'\n'
    (HERE/'VERIFICATION_REPORT.json').write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
