"""Exact author arithmetic for the proposed weighted emitter estimates.

The analytical integral bounds and provisional installed theorem need their
own separate checks. No matrix, quadrature, parameter search or dynamics runs.
"""
from pathlib import Path
from fractions import Fraction as F
import datetime
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
started = time.monotonic()
ROOT = Path(__file__).resolve().parent
for row in json.loads((ROOT/'SOURCE_PINS.json').read_text())['files']:
    raw = (ROOT/row['snapshot']).read_bytes()
    assert len(raw) == row['bytes']
    assert hashlib.sha256(raw).hexdigest() == row['sha256']
src = json.loads((ROOT/'inputs/INSTALLED_CERTIFICATE.json').read_text())
k = F(src['parameters']['coupling'])
sigma = F(src['parameters']['half_width'])
assert k == F(1, 10**12) and sigma == F(1, 10**6)
v, d, F0 = F(1, 40), F(61, 1000), F(1, 500)
assert 560*k*k < v/2
assert 8/(19*v) < 17
assert 4/(361*v) < F(1, 2)
assert 34*sigma < 1

# The residual inverse is a separate closed summand plus one block rank-one
# term; this exact factor is the source Schur estimate used in the note.
xi = F(src['uniform_schur']['relative_resonant_denominator_error']['exact_rational'])
delta = F(src['uniform_schur']['closed_tail_factor']['exact_rational'])
spq, sqp = 2*sigma*206*delta, delta*206*2
inverse_rank_factor = (1+6*k*k*spq)*(1+6*k*k*sqp)/(1-xi)
assert inverse_rank_factor < 2

a1 = 2/sigma+13
f1 = a1+17*d/k
phase_weight = 2*F0+48960*k+320*d/k
assert f1 < 2/k
assert f1+F(5, 2)*F0 < 3/k
assert f1+phase_weight+F(5, 2)*F0 < 23/k
assert 3*d*36+180 < 187
assert 3*d*24+60 < 65
assert 3*d*4 < 1
assert 1+20000*k < 2 and 36*k < 1
assert 374*k+18*10**6*k*k < 1
assert 6*10**6*k*k < k

Dj = 236*a1+5518+544*d/k+(6*d+1)/(k*k)
assert Dj < F(3, 2)/(k*k)
D = 3/(k*k)
assert 2*Dj*Dj < D*D
A0, B0 = 3/k, 23/k
T = 10**36
sqrt_lower = 27*10**16
assert sqrt_lower*sqrt_lower < 3*v*T
assert v*T > 1 and B0/sqrt_lower < F(1, 2)
escape = (A0+B0)/sqrt_lower+D/(F(12, 5)*v*T)
complete = F(3, 1000)+F(714, 10**6)+escape
assert escape < F(97, 10**6)
assert complete < F(4, 1000)
Tobs, M = 2*T, 5*10**37
distance = M-src['parameters']['L']-1
assert distance > 19*Tobs*F(6, 5)+9
assert complete+F(1, 1000) < F(5, 1000)

def scalar(q):
    return {'exact_rational': str(q), 'display_only_float': float(q)}

out = {
    'scope': 'Author scalar checks only. Weighted integral proof and installed theorem remain provisional pending separate review.',
    'weighted_constants': {key: scalar(value) for key, value in {
        'resonant_rank_factor': inverse_rank_factor, 'F1_upper': f1,
        'weighted_phase_derivative_upper': phase_weight,
        'localized_column_upper': Dj, 'grouped_D': D,
        'A0': A0, 'B0': B0, 'escape_at_onset': escape,
        'complete_isometry_at_onset': complete,
        'finite_complete_isometry_upper': complete+F(1, 1000),
    }.items()},
    'time_and_clock': {'onset': T, 'Tobs': Tobs, 'M': M, 'first_omitted_distance': distance},
    'unchanged_comparator': 'Same f, rho, beta, zeta, actual scalar nu+2kappa and total old aging as the installed source.',
    'limits': {'cpu_cap_seconds': 5, 'wrapper_wall_cap_seconds': 10,
               'matrices': 0, 'quadrature': False, 'parameter_search': False,
               'time_evolution': False, 'independent_review': False},
    'elapsed_seconds': time.monotonic()-started,
}
(ROOT/'BOUNDS.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'status': 'exact scalar comparisons completed',
                  'onset': T, 'complete_error_display': float(complete),
                  'elapsed_seconds': out['elapsed_seconds']}, indent=2))
