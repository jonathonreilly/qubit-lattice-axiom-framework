#!/usr/bin/env python3
"""Small independent controls for the new lift and compact-packet arguments.

No root implementation is imported or executed. General statements are
established by the analytic reconstruction in POST.md, not these samples.
"""
from itertools import product
from pathlib import Path
import hashlib
import json

import mpmath as mp
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parent


def packet_checks():
    mp.mp.dps = 80
    records = []
    for n in (3, 4, 7, 13, 64, 257):
        theta = mp.pi / n
        unnormalized = {j: mp.sin(j * theta)**2 for j in range(1, n)}
        normalization = mp.fsum(v*v for v in unnormalized.values())
        amplitudes = {j: v / mp.sqrt(normalization) for j, v in unnormalized.items()}
        amplitude = lambda j: amplitudes.get(j, mp.mpf(0))
        # After removing the i^x carrier, V/J acts by the real adjacency sum.
        velocity = {j: amplitude(j-1) + amplitude(j+1) for j in range(0, n+1)}
        mean = mp.fsum(amplitude(j) * velocity[j] for j in range(0, n+1))
        variance = mp.fsum((velocity[j]-mean*amplitude(j))**2 for j in range(0, n+1))
        c1 = (2 + mp.cos(2*theta))/3
        predicted_variance = 16*mp.sin(theta)**4*(2*n-3)/(9*n)
        direct_c2 = mp.fsum(amplitude(j)*amplitude(j+2) for j in range(1, n))
        predicted_c2 = (2+mp.cos(4*theta))/3 - 8*mp.sin(theta)**4/(3*n)
        errors = [abs(normalization-mp.mpf(3)*n/8), abs(mean-2*c1),
                  abs(variance-predicted_variance), abs(direct_c2-predicted_c2)]
        assert max(errors) < mp.mpf('1e-70')
        no_exterior_components = mp.fsum((velocity[j]-mean*amplitude(j))**2 for j in range(1, n))
        deleted_boundary_defect = variance-no_exterior_components
        cyclic_c2_defect = (2+mp.cos(4*theta))/3-direct_c2
        assert deleted_boundary_defect > mp.mpf('1e-20')
        assert cyclic_c2_defect > mp.mpf('1e-20')
        records.append({"N": n, "direct_velocity_mean_over_J": mp.nstr(mean, 45),
                        "direct_velocity_variance_over_J_squared": mp.nstr(variance, 45),
                        "largest_identity_error": mp.nstr(max(errors), 8),
                        "deleted_exterior_velocity_components_defect": mp.nstr(deleted_boundary_defect, 35),
                        "cyclic_shift_two_mutation_defect": mp.nstr(cyclic_c2_defect, 35)})
    n, s = sp.symbols('N s', positive=True)
    # Independent recurrence: interior residual (2s/C)(1-4 sin^2/3),
    # plus the two exterior components s/C, where C^2=3N/8.
    recurrence_variance = s*s/(3*n/8) * (4*n/3-2)
    root_expression = 16*s*s*(2*n-3)/(9*n)
    assert sp.simplify(recurrence_variance-root_expression) == 0
    return {"precision_decimal_digits": 80, "direct_velocity_checks": records,
            "symbolic_all_N_recurrence_variance_identity": True,
            "scope": "The finite high-precision checks are not interval certificates; POST supplies the all-N finite-sum argument."}


def exact_lift_checks():
    payload = list(product(range(2), repeat=2))  # (system energy label, flag)
    payload_index = {state: i for i, state in enumerate(payload)}
    unitary = sp.zeros(4)
    for a, f in payload:
        for b, g in payload:
            if f == g and a == b:
                value = sp.Rational(4, 5)
            elif a != b and f == 0 and g == 1:
                value = sp.Rational(3, 5)
            elif a != b and f == 1 and g == 0:
                value = -sp.Rational(3, 5)
            else:
                value = 0
            unitary[payload_index[b, g], payload_index[a, f]] = value
    assert unitary.H*unitary == sp.eye(4)
    assert (unitary-sp.eye(4)).H*(unitary-sp.eye(4)) == sp.Rational(2, 5)*sp.eye(4)
    width = 2
    states = list(product(range(2), range(2), range(width+2)))
    index = {state: i for i, state in enumerate(states)}
    dim = len(states)
    complete = sp.diag(*[int(1 <= a+r <= width+1) for a, f, r in states])
    def lift(operator):
        result = sp.zeros(dim)
        for a, f, r in states:
            total = a+r
            col = index[a, f, r]
            if not 1 <= total <= width+1:
                result[col, col] = 1
                continue
            for b, g in payload:
                destination_r = total-b
                assert 0 <= destination_r <= width+1
                result[index[b, g, destination_r], col] = operator[payload_index[b, g], payload_index[a, f]]
        return result
    lifted = lift(unitary)
    phases = sp.diag(*[1 if a == 0 else sp.I for a, f in payload])
    full_phases = sp.diag(*[1 if a == 0 else sp.I for a, f, r in states])
    conjugated = phases*unitary*phases.H
    second_lift = lift(conjugated)
    free_labels = sp.diag(*[a+r for a, f, r in states])
    identities = {
        "full_unitarity": lifted.H*lifted == sp.eye(dim),
        "free_energy_conservation": free_labels*lifted == lifted*free_labels,
        "global_product_rule": second_lift*lifted == lift(conjugated*unitary),
        "global_phase_conjugation": full_phases*lifted*full_phases.H == second_lift,
        "incomplete_blocks_identity": (sp.eye(dim)-complete)*lifted == sp.eye(dim)-complete,
        "exact_near_identity_metric": (lifted-sp.eye(dim)).H*(lifted-sp.eye(dim)) == sp.Rational(2, 5)*complete,
    }
    assert all(identities.values())
    reflection = sp.diag(*[1 if f == 0 else -1 for a, f in payload])
    wrong_completion = unitary*reflection
    blank = [payload_index[a, 0] for a in range(2)]
    assert wrong_completion[:, blank] == unitary[:, blank]
    assert wrong_completion.H == wrong_completion and wrong_completion**2 == sp.eye(4)
    assert sp.trace(wrong_completion) == 0  # eigenvalues +1 and -1, so distance to I is 2.
    assert 2 > 2*sp.Rational(3, 5)
    return {"dimension": dim, "exact_identities": identities,
            "correct_norm_distance_to_identity": "sqrt(2/5)",
            "wrong_completion_preserves_blank_column": True,
            "wrong_completion_norm_distance_to_identity": "2",
            "wrong_completion_near_identity_bound_rejected": True}


def dimensionless_clock_check():
    tau, n, w = 1e-4, 3, 4
    c1 = (2+np.cos(2*np.pi/(w+1)))/3
    coupling = 1/(2*tau*c1)
    a = n/c1
    buffer = int(np.ceil(8*a))
    size = n+w+2*buffer+1
    adjacency = np.diag(np.ones(size-1), 1)+np.diag(np.ones(size-1), -1)
    ground = 2*coupling*(1-np.cos(np.pi/(size+1)))
    physical = 2*coupling*np.eye(size)-coupling*adjacency-ground*np.eye(size)
    exact_scaled = np.array([float(2*(mp.cos(mp.pi/(size+1))-mp.cos(mp.pi*j/(size+1))))
                             for j in range(1, size+1)])
    scaled_error = float(np.max(np.abs(np.linalg.eigvalsh(physical/coupling)-exact_scaled)))
    mutated_error = float(np.max(np.abs(np.linalg.eigvalsh(physical/coupling-1e-6*np.eye(size))-exact_scaled)))
    assert scaled_error < 2e-12 and mutated_error > 1e-7
    return {"J": coupling, "clock_dimension": size,
            "observed_dimensionful_minimum_eigenvalue": float(np.linalg.eigvalsh(physical)[0]),
            "full_dimensionless_spectrum_error_against_high_precision_formula": scaled_error,
            "wrong_ground_shift_mutation_error": mutated_error,
            "scope": "Reproduces the scale-aware finite diagnostic. Positivity follows from the exact spectrum, not the observed sign of a roundoff-sized eigenvalue."}


def main():
    for name, expected in json.loads((ROOT/'PRE_SEAL.json').read_text())['files'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == expected
    result = {"packet": packet_checks(), "finite_lift": exact_lift_checks(),
              "clock_diagnostic": dimensionless_clock_check(),
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "scope": "Independent small controls; no root source import, no fixed-horizon numerical convergence claim, and no audit verdict."}
    (ROOT/'INDEPENDENT_POST_RESULTS.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
