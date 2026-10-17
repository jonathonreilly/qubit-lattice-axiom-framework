"""Exact scalar arithmetic for a proposed structural coefficient box.

No matrix, parameter grid, optimizer or clock dynamics is executed.
The analytical resolvent and packet arguments need their own review.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
start = time.monotonic()
ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / 'SOURCE_PINS.json').read_text())
for row in manifest['files']:
    raw = (ROOT / row['snapshot']).read_bytes()
    assert len(raw) == row['bytes'] and hashlib.sha256(raw).hexdigest() == row['sha256']
source = json.loads((ROOT / 'inputs/CERTIFICATE.json').read_text())
J = F('0.030021107107032')
a = F(1, 10**8)
g = F(9, 50)
b, c = 9*a, 3*a
gap = g-b
kappa = F(1, 7)
eta = b+c+J*J*b/(g*(g-b))
A = F(166)
actual_inverse_bound = A/(1-A*eta)
extra_reflection = 2*J*A*A*eta/(1-A*eta)
assert gap > F(17, 100)
assert 2+F(17, 100)/J > kappa+1/kappa
assert eta < F(1226, 10**10) and A*eta < 1
assert actual_inverse_bound < 167
assert extra_reflection < F(203, 10**6)

inv24 = 2*167+1/J
assert inv24 < 368
LM2 = J*J*(9+4/(1-kappa*kappa)**2)
assert LM2 < F(11, 100)**2
assert 2*(J*368)**2 < 16**2
remainder = F(700, 368)-F(11, 100)*16
assert remainder > 0 and 5*J*J < remainder*remainder

base_ready = F(source['packet']['infinite_finite_preparation_isometry_upper']['rational'])
base_finite = F(source['finite_horizon']['complete_isometry_upper']['rational'])
actual_ready, actual_finite = base_ready+extra_reflection, base_finite+extra_reflection
assert actual_ready < F(112, 10000)
assert actual_finite < F(122, 10000)
assert source['packet']['support_sites'] == 22*10**12
assert source['packet']['all_future_from_elapsed_time'] == 2*10**13
assert source['finite_horizon']['clock_sites'] == 9*10**14
assert source['finite_horizon']['Tobs'] == 4*10**13
Bbound = F(source['finite_horizon']['positive_block_B_upper']['rational'])
Vbound = F(source['finite_horizon']['Vmax']['rational'])
assert Bbound+b < 20
assert Vbound+c < 8
assert F(19, 2)+2*J+8 < 18

parameters = {name: F(value) for name, value in {
    'DeltaA': '2.192035527016003', 'DeltaB': '2.186826508897014',
    'h': '3.999349697888060', 'u': '0.544607276405587',
    'gA': '0.996878563816670', 'gB': '0.599319315560298',
    'lambdaA': '3.801781381581202', 'lambdaB': '2.575033765788497',
    'mu0': '0.321494607058201', 'nu': '1.459892813020969',
}.items()}
assert all(x-a > 0 for x in parameters.values())
assert 2*(parameters['gA']+a) < 2 and 2*(parameters['gB']+a) < 2
assert sum([1, 1, 2, 1, 2, 2])*a == b
assert sum([1, 2, 1, 2, 2])*a == 8*a

# Fixed-nominal-scalar error is an explicitly separate budget, not a
# permitted all-future omission. The crude long-horizon ceiling saturates.
assert a*source['packet']['all_future_from_elapsed_time'] > 2

def scalar(x):
    return {'exact_rational': str(x), 'display_only_float': float(x)}

out = {'scope': 'Exact scalar checks for the proposed structural coefficient box only; analytical proof and independent review remain separate.',
       'parameters': {name: str(x) for name, x in parameters.items()},
       'coefficient_radius': str(a),
       'constants': {name: scalar(x) for name, x in {
           'bulk_norm_radius': b, 'contact_norm_radius': c,
           'remaining_closed_gap': gap, 'matching_norm_radius': eta,
           'physical_inverse_bound': actual_inverse_bound,
           'bridge_inverse_bound': inv24, 'extra_reflection_error': extra_reflection,
           'finite_preparation_all_future_bound': actual_ready,
           'finite_clock_horizon_bound': actual_finite,
           'B_spectral_upper': Bbound+b, 'contact_norm_upper': Vbound+c,
       }.items()},
       'preserved_generic_ceilings': {'root': '1/7', 'root_derivative': '1/24',
           'X0': 16, 'X1': 700, 'C0': 31, 'C1': 2700, 'D': 88000},
       'max_added_incident_load_changes': {'old_each': str(2*a), 'source_each': str(8*a), 'contact_clock_each': str(3*a)},
       'phase_scope': 'Actual nutilde in ten-coefficient comparison; fixed nominal scalar corollary requires nu exact, leaving nine variable coefficients.',
       'limits': {'matrices': 0, 'grid_points': 0, 'time_evolution': False,
           'independent_review': False, 'cpu_cap_seconds': 10,
           'wrapper_wall_cap_seconds': 20},
       'elapsed_seconds': time.monotonic()-start}
(ROOT / 'BOUNDS.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'status': 'exact scalar comparisons completed',
                  'extra_reflection_display': float(extra_reflection),
                  'finite_ready_display': float(actual_ready),
                  'finite_horizon_display': float(actual_finite),
                  'elapsed_seconds': out['elapsed_seconds']}, indent=2))
