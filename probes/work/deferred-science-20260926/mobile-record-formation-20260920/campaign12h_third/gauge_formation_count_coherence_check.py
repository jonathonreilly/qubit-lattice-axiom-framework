#!/usr/bin/env python3
"""Exact physical-ring operators and conserved/eigenobservable controls."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent


def simplify_zero(A):
    return all(s.expand(value) == 0 for value in A.todok().values())


def check_ring(K):
    assert K >= 4 and K % 2 == 0
    D = 1 << K
    mask = D-1
    bit = lambda b, i: (b >> (i % K)) & 1
    charges = [[bit(b, i)-bit(b, i-1) for i in range(K)] for b in range(D)]
    occ = [[int(q != 0) for q in row] for row in charges]
    number = [sum(row) for row in occ]
    assert all(n % 2 == 0 for n in number)
    T = s.SparseMatrix(D, D, {(b ^ mask, b): 1 for b in range(D)})
    N = s.SparseMatrix(s.diag(*number))
    chi = s.symbols('chi', real=True)
    O = s.SparseMatrix(D, D, {(b ^ mask, b): chi**((K-number[b])//2) for b in range(D)})
    assert T*T == s.eye(D) and N*T == T*N
    occupations = [s.SparseMatrix(s.diag(*[row[i] for row in occ])) for i in range(K)]
    H = s.SparseMatrix(D, D, {})
    H_inhomogeneous = s.SparseMatrix(D, D, {})
    births = []
    gamma = s.SparseMatrix(D, D, {})
    graph = {}
    fiber = {}
    for b in range(D):
        pattern = sum(x << i for i, x in enumerate(occ[b]))
        fiber.setdefault(pattern, []).append(b)
        graph.setdefault(pattern, set())
    assert len(fiber) == 2**(K-1) and all(len(v) == 2 for v in fiber.values())
    channels = []
    for i in range(K):
        vp = {}; vm = {}; hop = {}
        for b in range(D):
            target = b ^ (1 << i)
            if bit(b, i-1) != bit(b, i+1):
                hop[(target, b)] = 1
                assert number[target] == number[b]
                # Exactly one existing charge moves across this edge.
                assert sorted(charges[b]) == sorted(charges[target])
                changed = [j for j in range(K) if occ[b][j] != occ[target][j]]
                assert set(changed) == {i, (i+1) % K}
                p = sum(x << j for j, x in enumerate(occ[b]))
                q = sum(x << j for j, x in enumerate(occ[target]))
                graph[p].add(q)
            elif bit(b, i-1) == bit(b, i) == bit(b, i+1):
                (vp if bit(b, i) == 0 else vm)[(target, b)] = 1
                assert number[target] == number[b]+2
                assert sum(q == 1 for q in charges[target]) == sum(q == 1 for q in charges[b])+1
                assert sum(q == -1 for q in charges[target]) == sum(q == -1 for q in charges[b])+1
        Vp = s.SparseMatrix(D, D, vp); Vm = s.SparseMatrix(D, D, vm)
        hop_matrix = s.SparseMatrix(D, D, hop)
        assert hop_matrix == hop_matrix.T
        H += hop_matrix
        H_inhomogeneous += (i+1)*hop_matrix
        assert hop_matrix*T == T*hop_matrix
        assert T*Vp*T == Vm
        assert Vp.T*Vm == s.zeros(D)
        P = Vp.T*Vp+Vm.T*Vm
        expected_P = s.SparseMatrix(s.diag(*[int(not row[i] and not row[(i+1) % K]) for row in occ]))
        assert P == expected_P and T*P == P*T
        gamma += P
        assert N*Vp-Vp*N == 2*Vp and N*Vm-Vm*N == 2*Vm
        dual = Vp.T*O*Vp+Vm.T*O*Vm+chi*(Vp.T*O*Vm+Vm.T*O*Vp)-(P*O+O*P)/2
        assert simplify_zero(dual)
        for pattern, states in fiber.items():
            outputs = [b ^ (1 << i) for b in states if bit(b, i-1) != bit(b, i+1)]
            if outputs:
                assert len(outputs) == 2
                out_pattern = sum(x << j for j, x in enumerate(occ[outputs[0]]))
                assert set(outputs) == set(fiber[out_pattern])
        births.append((Vp, Vm, P))
        channels.append({'edge': i, 'forward_births': len(vp), 'reverse_orientation_births': len(vm), 'hopping_matrix_entries': len(hop)})
    assert simplify_zero(H*O-O*H)
    assert simplify_zero(H_inhomogeneous*O-O*H_inhomogeneous)
    orientation_swap = s.Matrix([[0, 1], [1, 0]])
    coefficient = s.Matrix([[1, chi], [chi, 1]])
    assert orientation_swap*coefficient*orientation_swap == coefficient
    for nx in occupations:
        assert nx*O == O*nx
    # A diagonal, charge-conjugation-even electric interaction is an allowed
    # occupation-preserving H0; it need not be linear in total record number.
    H0 = s.SparseMatrix(s.diag(*[sum((2*bit(b, i)-1)*(2*bit(b, i+2)-1) for i in range(K)) for b in range(D)]))
    assert simplify_zero(H0*O-O*H0)
    # Exact electric-monitoring eigenobservable, independently assembled.
    field_dual = s.SparseMatrix(D, D, {})
    for i in range(K):
        E = s.SparseMatrix(s.diag(*[s.Rational(2*bit(b, i)-1, 2) for b in range(D)]))
        field_dual += E*O*E-(E*E*O+O*E*E)/2
    assert simplify_zero(field_dual+s.Rational(K, 2)*O)
    # This diagonal H0 still commutes with all occupations, but breaks T.
    Z0 = s.SparseMatrix(s.diag(*[2*bit(b, 0)-1 for b in range(D)]))
    assert all(Z0*nx == nx*Z0 for nx in occupations)
    assert not simplify_zero(Z0*T-T*Z0)
    # Enumerate occupation-pattern hopping components, not a classical
    # substitute for the separate whole-fiber quantum proof.
    unseen = set(graph); components = []
    while unseen:
        first = min(unseen); seen = {first}; stack = [first]; unseen.remove(first)
        while stack:
            x = stack.pop()
            for y in graph[x]:
                if y not in seen:
                    seen.add(y); unseen.remove(y); stack.append(y)
        n = first.bit_count()
        assert all(x.bit_count() == n for x in seen)
        contact = [p for p in seen if any(not ((p >> i) & 1) and not ((p >> ((i+1) % K)) & 1) for i in range(K))]
        assert n == K or contact
        components.append({'record_number': n, 'occupation_patterns': len(seen), 'birth_contact_patterns': len(contact)})
    assert len(components) == K//2+1
    full = [b for b, n in enumerate(number) if n == K]
    assert len(full) == 2 and full[0] ^ full[1] == mask
    rhoF = s.SparseMatrix(D, D, {(full[0], full[0]): s.Rational(1, 2), (full[1], full[1]): s.Rational(1, 2),
                                (full[0], full[1]): chi**(K//2)/2, (full[1], full[0]): chi**(K//2)/2})
    assert simplify_zero((H+H0)*rhoF-rhoF*(H+H0))
    assert simplify_zero((H_inhomogeneous+H0)*rhoF-rhoF*(H_inhomogeneous+H0))
    translation = s.SparseMatrix(D, D, {(((b << 1) & mask) | (b >> (K-1)), b): 1 for b in range(D)})
    assert not simplify_zero(translation*H_inhomogeneous-H_inhomogeneous*translation)
    for vp, vm, P in births:
        assert vp*rhoF == s.zeros(D) and vm*rhoF == s.zeros(D) and P*rhoF == s.zeros(D)
    assert s.expand(s.trace(T*rhoF)-chi**(K//2)) == 0
    assert s.expand(s.trace(rhoF*rhoF)-(1+chi**K)/2) == 0
    initial = s.SparseMatrix(D, D, {(0, 0): s.Rational(1, 2), (mask, mask): s.Rational(1, 2),
                                   (0, mask): s.Rational(1, 2), (mask, 0): s.Rational(1, 2)})
    assert s.expand(s.trace(O*initial)-chi**(K//2)) == 0
    assert T*initial*T == initial and T*rhoF*T == rhoF
    return {'K': K, 'physical_dimension': D, 'occupation_fiber_dimension': 2,
            'all_local_Gauss_charge_and_record_rules_checked': True,
            'every_hop_identifies_entire_occupation_fibers_unitarily': True,
            'each_birth_dual_annihilates_O_for_symbolic_real_chi': True,
            'H_and_occupation_monitoring_preserve_O': True,
            'diagonal_even_H0_preserves_O': True,
            'diagonal_odd_H0_countercontrol_breaks_T': True,
            'unit_electric_monitoring_dual_eigenvalue': str(-s.Rational(K, 2)),
            'occupation_hopping_components': sorted(components, key=lambda x: x['record_number']),
            'channels': channels, 'full_basis_indices': full,
            'terminal_coherence': str(chi**(K//2)), 'terminal_purity': str((1+chi**K)/2),
            'orientation_coefficient_matrix_is_charge_conjugation_covariant': True,
            'translation_breaking_hopping_preserves_invariant_and_terminal_density': True,
            'initial_and_terminal_densities_charge_conjugation_invariant': True,
            'complete_symbolic_terminal_stationarity_checked': True}


if __name__ == '__main__':
    out = {'created_utc': datetime.now(timezone.utc).isoformat(),
           'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'cases': [check_ring(K) for K in (4, 6, 8)],
           'limits': 'Exact finite controls. General even-cycle completion uses the supplied monitoring/fiber theorem; the all-size count identity is proved analytically. No simulation or proof of three-dimensional photon physics.'}
    text = json.dumps(out, indent=2)+'\n'
    (HERE/'GAUGE_FORMATION_COUNT_COHERENCE_RESULTS.json').write_text(text)
    print(text, end='')
