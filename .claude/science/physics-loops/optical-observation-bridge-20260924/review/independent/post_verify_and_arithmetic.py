"""Released-source bookkeeping and independently written Decimal arithmetic.

No author module is imported, evaluated, or executed. Finite Fourier values
are compared with the already sealed independent PRE evidence, not rerun.
"""
from pathlib import Path
from decimal import Decimal as D, getcontext
from datetime import datetime, timezone
import copy
import difflib
import hashlib
import json

HERE = Path(__file__).resolve().parent
getcontext().prec = 110


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(rel):
    return json.loads((HERE / rel).read_text())


def atan_small(x):
    # Alternating power series: the first omitted term bounds truncation.
    power = x
    total = x
    n = 1
    while True:
        power *= -x*x
        term = power / D(2*n+1)
        total += term
        if abs(term) < D('1e-108'):
            return total
        n += 1


PI = 16*atan_small(D(1)/5) - 4*atan_small(D(1)/239)


def sin_series(x):
    term = x
    total = x
    n = 1
    while True:
        term *= -x*x / D((2*n)*(2*n+1))
        total += term
        if abs(term) < D('1e-108'):
            return total
        n += 1


def asin_small(x):
    assert abs(x) < D('0.01')
    term = x
    total = x
    n = 0
    while True:
        term *= D((2*n+1)**2)*x*x / D((2*n+2)*(2*n+3))
        total += term
        if abs(term) < D('1e-108'):
            return total
        n += 1


comparisons = []


def compare(label, independent, author_text, tolerance='1e-59'):
    author = D(str(author_text))
    relative = abs(independent-author)/abs(independent)
    assert relative < D(tolerance), (label, relative)
    comparisons.append({
        'quantity': label, 'independent_decimal': str(independent),
        'stored_author_value': str(author), 'relative_difference': str(relative),
        'relative_tolerance': tolerance,
    })


pre_seal_path = HERE / 'PRE_SEAL.json'
assert sha(pre_seal_path) == '0931fe9b88d147fcb9994ea87a0cb48b47cf0215055a8fe9a4780f51ef38666c'
pre = read('PRE_SEAL.json')
for row in pre['members']:
    p = HERE / row['path']
    assert sha(p) == row['sha256'] and p.stat().st_size == row['bytes']

pins = read('POST_SOURCE_PINS_INITIAL.json')
for row in pins['sources']:
    for p in (Path(row['origin']), HERE / row['snapshot']):
        assert sha(p) == row['sha256'] and p.stat().st_size == row['bytes']

pre_pins = read('SOURCE_PINS.json')
for row in pre_pins['sources']:
    assert sha(Path(row['origin'])) == row['sha256']

groups = [
    ('finite-volume-observation-personal', 'finite_volume_units.py', 'FINITE_VOLUME_UNITS.json'),
    ('optical-band-response-personal', 'optical_band_controls.py', 'OPTICAL_BAND_RESULTS.json'),
    ('optical-experiment-scope-personal', 'experiment_units.py', 'EXPERIMENT_UNITS.json'),
]
author_evidence = []
declared_parent_origins = {}
for name, code, result in groups:
    folder = HERE / 'post_sources' / name
    seal = json.loads((folder / 'AUTHOR_SEAL.json').read_text())
    for rel, binding in seal['files'].items():
        assert sha(folder/rel) == binding['sha256']
        assert (folder/rel).stat().st_size == binding['bytes']
    author_pins = json.loads((folder/'SOURCE_PINS.json').read_text())
    for parent in author_pins.get('files', [author_pins]):
        assert sha(Path(parent['path'])) == parent['sha256']
        declared_parent_origins[parent['path']] = parent['sha256']
    receipt = json.loads((folder/'EXECUTION.json').read_text())
    data = json.loads((folder/result).read_text())
    assert receipt['exit_code'] == 0 and receipt['stderr_bytes'] == 0
    assert (folder/'CONTROL.stderr').read_bytes() == b''
    assert (folder/'CONTROL.stdout').read_bytes() == (folder/result).read_bytes()
    assert receipt['stdout_sha256'] == sha(folder/result)
    assert receipt['code_sha256'] == sha(folder/code) == data['source_sha256']
    author_evidence.append({
        'name': name, 'seal_sha256': sha(folder/'AUTHOR_SEAL.json'),
        'member_count': len(seal['files']), 'receipt': receipt,
        'code_and_result_source_match': True, 'stdout_result_byte_identical': True,
        'executed_by_reviewer': False,
    })

current = read('post_sources/optical-band-response-personal/OPTICAL_BAND_RESULTS.json')
old_folder = HERE/'post_sources/optical-band-response-personal/history/hard-band-only'
old = json.loads((old_folder/'OPTICAL_BAND_RESULTS.json').read_text())
old_receipt = json.loads((old_folder/'EXECUTION.json').read_text())
assert old_receipt['exit_code'] == 0 and old_receipt['stderr_bytes'] == 0
assert (old_folder/'CONTROL.stderr').read_bytes() == b''
assert (old_folder/'CONTROL.stdout').read_bytes() == (old_folder/'OPTICAL_BAND_RESULTS.json').read_bytes()
assert old_receipt['code_sha256'] == sha(old_folder/'optical_band_controls.py') == old['source_sha256']
assert old_receipt['stdout_sha256'] == sha(old_folder/'CONTROL.stdout')
reduced = copy.deepcopy(current)
for row in reduced['lattice_rows']:
    del row['w_p']
    del row['w_p_exact']
for row in reduced['SI_rows']:
    del row['mean_energy_limiting_relative_excess_strict_upper']
    row['limiting_relative_probability_excess_strict_upper'] = row.pop('hard_band_limiting_relative_excess_strict_upper')
for field in ('source_sha256', 'elapsed_seconds'):
    reduced.pop(field)
    old.pop(field)
assert reduced == old

diffs = []
for filename in ('OPTICAL_BAND_ORIGINAL_PROBE_RESPONSE_ROOT.md', 'optical_band_controls.py'):
    before = (old_folder/filename).read_text().splitlines(keepends=True)
    after = (old_folder.parent.parent/filename).read_text().splitlines(keepends=True)
    diffs.extend(difflib.unified_diff(before, after, fromfile='hard-band-only/'+filename, tofile='current/'+filename))
(HERE/'POST_HISTORY_DIFF.txt').write_text(''.join(diffs))

own = read('CONTROL_RESULTS.json')
own_spectral = {row['L']: row for row in own['spectral_rows']}
spectral_comparisons = []
empty_rows = []
for row in current['lattice_rows']:
    if row['L'] in own_spectral:
        other = own_spectral[row['L']]
        dv = abs(row['v_p'] - other['v_local'])
        dw = abs(row['w_p'] - other['sum_d_squared_over_s'])
        assert max(dv, dw) < 2e-14
        spectral_comparisons.append({'L': row['L'], 'v_absolute_difference': dv, 'w_absolute_difference': dw})
    for band in row['rows']:
        assert band['normalized_band_packet_available'] == (band['nonzero_momenta_in_band'] > 0)
        if not band['normalized_band_packet_available']:
            assert band['max_eta'] == band['v_low'] == 0
            empty_rows.append({'L': row['L'], 'epsilon': band['epsilon'], 'stored_max_eta': band['max_eta'],
                               'finding': 'Projected weight zero is correct; normalized-band optimum is infeasible, not attained zero.'})

eq = D('6.9e20')
volume = read('post_sources/finite-volume-observation-personal/FINITE_VOLUME_UNITS.json')
for row in volume['fixed_volume_rows']:
    compare('reference gap lower eV L='+str(row['L']), eq*sin_series(PI/D(row['L']))/3,
            row['reference_energy_necessary_lower_eV'])
for row in volume['optical_rows']:
    energy = D(row['supplied_reference_energy_eV'])
    compare('strict L threshold E='+str(energy), PI/asin_small(3*energy/eq), row['necessary_L_strict_lower'])
for row in current['SI_rows']:
    energy = D(row['supplied_E_lab_eV'])
    epsilon = 6*energy/eq
    compare('root27 dimensionless ceiling E='+str(energy), epsilon, row['epsilon_strict_upper'])
    compare('root27 hard-band excess E='+str(energy), 27*D(3).sqrt()*epsilon**4/64,
            row['hard_band_limiting_relative_excess_strict_upper'])
    compare('root27 mean-energy excess E='+str(energy), 2*epsilon/D(3).sqrt(),
            row['mean_energy_limiting_relative_excess_strict_upper'])

experiment = read('post_sources/optical-experiment-scope-personal/EXPERIMENT_UNITS.json')
h = D('6.62607015e-34')
c = D('299792458')
joules_per_eV = D('1.602176634e-19')
for row in experiment['spectral_endpoint_rows']:
    wavelength = D(row['wavelength_nm'])*D('1e-9')
    compare('wavelength endpoint eV '+row['wavelength_nm']+' nm', h*c/(joules_per_eV*wavelength), row['energy_eV'])
compare('root28 supplied 2 eV mean excess', 8*D(3).sqrt()/eq, experiment['mean_energy_limiting_relative_excess_upper'])
tau = 3*h/(PI*joules_per_eV*eq)
compare('root28 conditional clock upper s', tau, experiment['conditional_tau_upper_s'])
compare('root28 1 ns over conditional clock upper', D('1e-9')/tau, experiment['necessary_bin_over_tau_lower'])

# New independent normalization check, not a data fit or digitization. These
# values are direct primary-text/caption inputs. Hypothetical exact zero of
# corrected g2 is used only to illustrate why uncorrected counts are nonzero.
rho = D('.34')
poisson = D(5780)*D(5990)*D('1e-9')*D(11450)
normalization = {
    'scope': 'Primary equations 1/2 and Figure 3 caption arithmetic; no fitted or digitized coincidence count.',
    'rho_definition': 'S/(S+B)', 'rho': str(rho), 'rho_squared': str(rho*rho),
    'estimated_detector_factor': '.7',
    'estimated_overall_per_detector_efficiency': str(D('.08')*D('.2')*D('.25')*D('.5')*D('.7')),
    'N1_N2_bin_T': str(poisson),
    'raw_normalized_coincidence_if_corrected_g2_is_exactly_zero': str(1-rho*rho),
    'raw_count_if_corrected_g2_is_exactly_zero': str(poisson*(1-rho*rho)),
    'interpretation': 'The source background is not the model vacuum; these cannot calibrate an original local-mark probability.',
}

report = {
    'completed_utc': datetime.now(timezone.utc).isoformat(),
    'scope': 'Released-source POST verification, static stored-output comparison, independent Decimal unit/normalization arithmetic.',
    'source_sha256': sha(Path(__file__)), 'author_code_executions_or_imports': 0,
    'PRE_seal_sha256': sha(pre_seal_path), 'PRE_members_unchanged': len(pre['members']),
    'released_origin_and_snapshot_bindings_verified': len(pins['sources']),
    'live_PRE_parent_origins_verified': len(pre_pins['sources']),
    'author_declared_parent_origins_verified': declared_parent_origins,
    'author_evidence': author_evidence,
    'historical_control_receipt': old_receipt,
    'historical_payload_exact_after_explicit_mean_additions_and_runtime_source_removal': True,
    'historical_band_rows_compared': sum(len(row['rows']) for row in current['lattice_rows']),
    'historical_SI_rows_compared': len(current['SI_rows']),
    'stored_PRE_root_spectral_comparisons': spectral_comparisons,
    'empty_band_label_findings': empty_rows,
    'Decimal_precision': getcontext().prec, 'Decimal_arithmetic_comparisons': comparisons,
    'primary_normalization_arithmetic': normalization,
    'limitations': ['No interval certificate for transcendental arithmetic or floating cutoff membership.',
                    'No author or parent runner execution; receipts checked as retained evidence only.',
                    'No source-to-detector theorem, finite-g or volume-uniform dynamics claim, empirical fit or exclusion.'],
}
text = json.dumps(report, indent=2, allow_nan=False)+'\n'
(HERE/'POST_VERIFICATION_REPORT.json').write_text(text)
print(text, end='')
