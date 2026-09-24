#!/usr/bin/env python3
"""Read-only POST correspondence; never import or execute author controls."""
from collections import Counter
import cmath
import hashlib
from itertools import product
import json
import math
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
AUTHOR = HERE / 'post_sources' / 'author'
read = lambda p: json.loads(p.read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
checks = []


def check(name, condition, **details):
    row = {'name': name, 'satisfied': bool(condition), **details}
    checks.append(row)
    print(json.dumps(row, sort_keys=True), flush=True)
    if not condition:
        raise AssertionError(name)


pre = read(HERE / 'PRE_SEAL.json')
check('PRE_seal_preserved', sha(HERE / 'PRE_SEAL.json') ==
      '65ef5734192d3ca88511a992fad2b1788582ad8acf632c2b2d33e866d121cff6')
check('all_PRE_members_preserved', all(sha(HERE / member['path']) == member['sha256']
                                     for member in pre['members']), count=len(pre['members']))
pins = read(HERE / 'POST_SOURCE_PINS.json')
check('all_released_frozen_origins_match', all(
    sha(HERE / source['frozen_path']) == sha(Path(source['origin'])) == source['sha256']
    for source in pins['released_author_files']), count=len(pins['released_author_files']))
root_pins = read(AUTHOR / 'SOURCE_PINS.json')
repo = Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth/campaign-working')
origin_rows = []
for source in root_pins['sources']:
    relative = str(Path(source['path']).relative_to(repo))
    data = subprocess.run(['git', 'show', root_pins['main'] + ':' + relative],
                          cwd=repo, capture_output=True, check=True).stdout
    actual = hashlib.sha256(data).hexdigest()
    assert actual == source['sha256'] and len(data) == source['bytes']
    origin_rows.append({'path': relative, 'sha256': actual, 'bytes': len(data),
                        'scope': 'Exact source identity only; no additional theorem imported.'})
check('author_source_pin_git_identities', len(origin_rows) == 5, origins=origin_rows)

main_result = read(AUTHOR / 'READOUT_CONTROL_RESULTS.json')
narrow = read(AUTHOR / 'NARROW_PACKET_RESULTS.json')
check('author_stdout_is_exact_result_bytes',
      (AUTHOR / 'CONTROL.stdout.txt').read_bytes() == (AUTHOR / 'READOUT_CONTROL_RESULTS.json').read_bytes()
      and (AUTHOR / 'NARROW_CONTROL.stdout.txt').read_bytes() == (AUTHOR / 'NARROW_PACKET_RESULTS.json').read_bytes())
check('author_result_source_fingerprints',
      main_result['source_sha256'] == sha(AUTHOR / 'record_photon_readout_controls.py')
      and narrow['source_sha256'] == sha(AUTHOR / 'narrow_packet_control.py'))
metadata = [read(AUTHOR / name) for name in ('CONTROL_EXECUTION.json', 'NARROW_CONTROL_EXECUTION.json')]
check('author_reported_exits_and_empty_stderr', all(row['exit_code'] == 0 for row in metadata)
      and (AUTHOR / 'CONTROL.stderr.txt').stat().st_size == 0
      and (AUTHOR / 'NARROW_CONTROL.stderr.txt').stat().st_size == 0,
      author_metadata=metadata,
      caveat='These are released author execution records, not new independent executions.')

# Independently decode the author's serialized link-index convention. This
# does not import its builder or repeat the primitive dynamics calculation.
vertices = tuple(product(range(6), repeat=3))
index = {v: i for i, v in enumerate(vertices)}


def neighbor(v, axis, sign):
    w = list(v)
    w[axis] = (w[axis] + sign) % 6
    return tuple(w)


edges = []
for a in (i for i, v in enumerate(vertices) if sum(v) % 2 == 0):
    ns = {index[neighbor(vertices[a], axis, sign)] for axis in range(3) for sign in (-1, 1)}
    edges.extend((a, b) for b in sorted(ns))


def convert_shift(items):
    out = {}
    for edge_index, value in items:
        a, b = (vertices[i] for i in edges[edge_index])
        matches = []
        for axis in range(3):
            if b == neighbor(a, axis, 1):
                matches.append(((a, axis), value))
            if b == neighbor(a, axis, -1):
                matches.append(((b, axis), -value))
        assert len(matches) == 1
        key, val = matches[0]
        out[key] = out.get(key, 0) + val
    return tuple(sorted((key, val) for key, val in out.items() if val))


def pre_shift(items):
    return tuple(sorted(((tuple(row['start']), row['axis']), row['value']) for row in items))


own = read(HERE / 'CONTROL_RESULTS.json')
own_cases = {(row['first'], row['second']): row for row in own['paths']}
sign_name = lambda signs: 'coherent' if len(signs) == 2 else ('plus' if signs[0] == 1 else 'minus')
graph = next(g for g in main_result['primitive_graphs'] if g['periods'] == [6, 6, 6])
for row in graph['rows']:
    names = sign_name(row['signs1']), sign_name(row['signs2'])
    expected = own_cases[names]
    poly = Counter({(): row['constant']})
    for shift, coefficient in zip(row['plaquette_shifts'], row['plaquette_coefficients']):
        poly[convert_shift(shift)] += coefficient
    own_poly = Counter({pre_shift(term['translation']): term['coefficient'] for term in expected['effect']})
    check('side_six_effect_correspondence_' + '_'.join(names),
          poly == own_poly and row['second_words'] == expected['path_count']
          and row['after_extra_matter_dephasing_constant'] == expected['dephased_effect'][0]['coefficient'],
          author_joint_words=row['second_words'], own_paths=expected['path_count'],
          caveat='Author joint matter/field words differ from the count of final matter words alone.')
primitive_rows = [row for g in main_result['primitive_graphs'] for row in g['rows']]
check('all_author_primitive_rows_consistent', all(
    row['constant'] == ((g['degree'] - 1) ** 2 - 2) * len(row['signs1']) * len(row['signs2'])
    and row['plaquette_coefficients'] == [len(row['signs1']) * len(row['signs2'])] * 2
    and row['after_extra_matter_dephasing_constant'] == row['constant']
    and row['extra_matter_dephasing_contrast'] == 0
    for g in main_result['primitive_graphs'] for row in g['rows']), rows=len(primitive_rows),
    graph_scopes=[{'periods': g['periods'], 'degree': g['degree']} for g in main_result['primitive_graphs']])

rotors = main_result['separate_rotor_controls'] + [main_result['grid_repeat']]
rotor_rows = [row for control in rotors for row in control['rows']]
all_contrast_consistent = True
for control in rotors:
    cosines = {(row['n'], row['time']): row['actual_cosine'] for row in control['rows']}
    for row in control['contrast_rows']:
        g, t = row['g'], row['time']
        all_contrast_consistent &= abs((cosines[1, t] - cosines[0, t]) / (g * g)
                                      - row['actual_one_minus_vac_over_g2']) < 1e-13
        all_contrast_consistent &= abs(-0.5 * math.exp(-g * g / 4)
                                      - row['harmonic_one_minus_vac_over_g2']) < 1e-14
check('all_author_rotor_output_arithmetic', all_contrast_consistent and all(
    row['observable_error_over_g4'] * row['g'] ** 4 <= row['expectation_error_bound'] + 1e-13
    for row in rotor_rows), rows=len(rotor_rows),
    max_reference_characteristic_error=max(row['reference_characteristic_error'] for row in rotor_rows),
    max_vector_error_over_g2=max(row['vector_error_over_g2'] for row in rotor_rows),
    max_observable_error_over_g4=max(row['observable_error_over_g4'] for row in rotor_rows),
    scope='Arithmetic checks of author results; no rotor evolution reproduced.')
base = next(c for c in main_result['separate_rotor_controls'] if c['rows'][0]['g'] == 0.1)
repeat = main_result['grid_repeat']
grid_diffs = {name: max(abs(a[name] - b[name]) for a, b in zip(base['rows'], repeat['rows']))
              for name in ('actual_cosine', 'vector_error_over_g2', 'observable_error_over_g4')}
check('author_grid_repeat_alignment', all(a['n'] == b['n'] and a['time'] == b['time']
                                        for a, b in zip(base['rows'], repeat['rows'])),
      grid_256_512_max_differences=grid_diffs)

fock_formula_errors = []
for row in narrow['finite_fock_rows']:
    g, t = row['g'], row['time']
    chi = 0.7 * math.sqrt(0.3) * cmath.exp(-0.9j * t) - 0.4j * math.sqrt(0.7) * cmath.exp(-1.7j * t)
    expected = math.exp(-g * g * (0.7 ** 2 + 0.4 ** 2) / 2) * (1 - g * g * abs(chi) ** 2)
    fock_formula_errors.append(abs(expected - row['formula']))
    assert abs(abs(chi) ** 2 - row['chi_abs_squared']) < 1e-14
    assert abs(abs(complex(row['actual_real'], row['actual_imaginary']) - expected)
               - row['absolute_error']) < 2e-14
check('all_author_fock_formula_fields', max(fock_formula_errors) < 2e-14,
      rows=len(narrow['finite_fock_rows']),
      max_closed_formula_correspondence_error=max(fock_formula_errors),
      max_author_matrix_formula_difference=max(row['absolute_error'] for row in narrow['finite_fock_rows']),
      scope='Closed-form/output correspondence; author finite Fock matrix was not executed.')
ks = [2 * math.pi * n / 64 for n in (5, 6, 7)]
omega = [2 * math.sin(k / 2) for k in ks]
vp = 64 * 6 * 6
radius = ks[2] - ks[1]
M = math.pi / (ks[1] - radius)
A = sum(w / math.sqrt(6) * abs(cmath.exp(1j * k) - 1) / math.sqrt(2 * vp * om)
        for w, k, om in zip((1, 2, 1), ks, omega))
parameters = narrow['packet_parameters']
check('author_packet_parameter_correspondence', parameters['V'] == vp
      and abs(parameters['A'] - A) < 1e-15
      and abs(parameters['coarse_Hessian_bound'] - M) < 1e-13
      and abs(parameters['group_velocity_sites_per_time'] - math.cos(ks[1] / 2)) < 1e-14,
      derived_A=A, derived_Hessian_bound=M, band_radius=radius)
for row in narrow['packet_rows']:
    t = row['time']
    check('author_packet_bound_arithmetic_t_' + str(t),
          abs(row['amplitude_bound'] - A * M * t * radius * radius / 2) < 1e-14
          and abs(row['intensity_bound'] - A * A * M * t * radius * radius) < 1e-14
          and row['max_amplitude_error'] <= row['amplitude_bound'] + 1e-16
          and row['max_intensity_error'] <= row['intensity_bound'] + 1e-16,
          row=row)

result = {'scope': __doc__, 'checks': checks, 'check_count': len(checks),
          'all_checks_satisfied': all(row['satisfied'] for row in checks),
          'script_sha256': sha(Path(__file__).resolve()),
          'POST_SOURCE_PINS_sha256': sha(HERE / 'POST_SOURCE_PINS.json'),
          'no_author_code_executed': True}
(HERE / 'POST_CHECK_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'completed': True, 'check_count': len(checks)}, sort_keys=True))
