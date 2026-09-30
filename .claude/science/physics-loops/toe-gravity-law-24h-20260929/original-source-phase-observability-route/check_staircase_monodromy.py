#!/usr/bin/env python3
"""Formal-charge certificate for the actual rotor two-hop staircase monodromy."""
import json


def check(L):
    assert L >= 8 and L % 2 == 0
    length, charges = 2*L, 2*L-1
    h = [(0, (-j) % L, j % L) for j in range(L)]
    b = [(0, (-j) % L, (j+1) % L) for j in range(L)]
    vertices = [v for pair in zip(h, b) for v in pair]
    assert len(set(vertices)) == length
    assert all(sum(v) % 2 == 0 for v in h)
    assert all(sum(v) % 2 == 1 for v in b)
    current = [None] + list(range(charges))
    original = current.copy()
    fields = {}
    divergence = [[0]*charges for _ in vertices]
    pi_sign, endpoint_checks = 1, 0
    def qvector(label):
        return [int(label == i) for i in range(charges)]
    def transfer(donor, hole, edge_A, edge_B, electric_sign):
        nonlocal pi_sign, endpoint_checks
        assert current[hole] is None and current[donor] is not None
        label = current[donor]
        assert vertices[edge_A] in h and vertices[edge_B] in b
        av, bv = vertices[edge_A], vertices[edge_B]
        assert sum(min((av[i]-bv[i]) % L, (bv[i]-av[i]) % L) for i in range(3)) == 1
        edge = (edge_A, edge_B)
        fields.setdefault(edge, [0]*charges)[label] += electric_sign
        divergence[edge_A][label] += electric_sign
        divergence[edge_B][label] -= electric_sign
        current[hole], current[donor] = label, None
        # These are coefficient identities in independent symbols q_i.
        # Each q_i is later either +1 or -1; no substituted rotor law is used.
        for v in (donor, hole):
            expected = [a-c for a, c in zip(qvector(current[v]), qvector(original[v]))]
            assert divergence[v] == expected
            endpoint_checks += 1
        if {av[2], bv[2]} == {0, L-1}:
            pi_sign = -pi_sign  # (-1)^q_i=-1 for both actual charges
    rounds = 2*L-1
    for circuit in range(rounds):
        for j in range(L):
            ah, bj, anext = 2*j, 2*j+1, (2*j+2) % length
            # F_h^*: occupied B -> empty A, electric +q_B.
            transfer(bj, ah, ah, bj, +1)
            # F_(hnext): occupied A -> now-empty B, electric -q_A.
            transfer(anext, bj, anext, bj, -1)
        expected_rotation = (circuit+1) % charges
        assert current[0] is None
        assert current[1:] == list(range(expected_rotation, charges)) + list(range(expected_rotation))
    assert current == original and pi_sign == -1
    assert all(all(c == 0 for c in row) for row in divergence)
    assert len(fields) == length
    for j in range(L):
        assert fields[(2*j, 2*j+1)] == [1]*charges
        assert fields[((2*j+2) % length, 2*j+1)] == [-1]*charges
    n = L**3//2
    global_negative = (n-2)//2
    # Every local sign assignment extends to the actual k=n-1 physical sector.
    assert global_negative >= charges
    assert (2*n-2)-charges >= global_negative
    return {'L':L, 'primitive_vertices':length, 'occupied_loop_charges':charges,
            'two_hop_steps':L*(2*L-1), 'primitive_hops':2*L*(2*L-1),
            'endpoint_Gauss_coefficient_checks':endpoint_checks,
            'restored_charge_permutation':True, 'electric_cycle_coefficients':'all +1/-1 times sum of every original q_i',
            'pi_z_holonomy_sign':pi_sign,
            'scope':'all formal charge assignments by exact coefficient identity; no source probability, full observability rank or spin truncation'}


if __name__ == '__main__':
    print(json.dumps({'cases':[check(L) for L in (8,16,24,32)]},indent=2))
    print('TOTAL PASS=4 FAIL=0')
