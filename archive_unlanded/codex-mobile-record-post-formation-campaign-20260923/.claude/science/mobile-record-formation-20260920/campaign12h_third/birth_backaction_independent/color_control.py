#!/usr/bin/env python3
"""Exact internal-entanglement and nonunique/internal-motion boundary control."""
from pathlib import Path
import json
import sympy as s

HERE = Path(__file__).resolve().parent
I = s.eye(3)
q = s.diag(1, 0, 0)
n = I-q
n0, n1 = s.kronecker_product(n, I), s.kronecker_product(I, n)
empty = s.zeros(9, 1)
empty[0] = 1
bell = s.zeros(9, 1)
bell[4] = bell[8] = 1/s.sqrt(2)
rho = bell*bell.T
J = bell*empty.T
assert (bell.T*bell)[0] == 1
assert J.T*J == s.kronecker_product(q, q)
Hhop = s.zeros(9)
for a in (1, 2):
    Hhop[a, 3*a] = Hhop[3*a, a] = 1
assert Hhop*bell == s.zeros(9, 1)
def dissipator(A, X):
    AA = A.T*A
    return A*X*A.T-(AA*X+X*AA)/2
assert dissipator(J, rho) == s.zeros(9)
assert dissipator(n0, rho) == dissipator(n1, rho) == s.zeros(9)
color_flip = s.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
H0 = s.kronecker_product(color_flip, I)
assert H0*n0-n0*H0 == H0*n1-n1*H0 == s.zeros(9)
internal_derivative = -s.I*(H0*rho-rho*H0)
assert internal_derivative != s.zeros(9)
assert ((n0+n1)*internal_derivative).trace() == 0
assert (s.kronecker_product(n, n)*internal_derivative).trace() == 0
result = {
    'occupied_content_dimension': 2,
    'entangled_born_state': '(|1,1>+|2,2>)/sqrt(2)',
    'birth_JdaggerJ_is_vacant_pair_projector': True,
    'occupation_monitoring_dissipates_no_full_internal_entanglement': True,
    'with_H0_zero_every_full_density_is_stationary': 'Analytic: hops and births vanish, all n_x restrict to identity.',
    'admissible_H0_can_drive_full_internal_unitary_motion': True,
    'nonzero_internal_density_derivative_entries': [[r,c,str(internal_derivative[r,c])] for r in range(9) for c in range(9) if internal_derivative[r,c] != 0],
    'full_occupation_probability_derivative': '0',
    'empty_to_full_survival_for_this_two_site_model': 'exp(-beta*t)',
    'scope': 'Completion does not imply a unique stationary internal state or convergence of the full density matrix.'
}
(HERE/'COLOR_CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
