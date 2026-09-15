#!/usr/bin/env python3
"""Falsifiers for the paired Spin(10) atomic-gap and mirror-spectrum note.
All scientific code is embedded; the general claims rest on the note's proofs.
"""
AUDIT_INPUT_PATHS = (
    "docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md",
)

import itertools
import json
import traceback
from collections import defaultdict
from functools import reduce
from itertools import combinations
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix
from scipy.linalg import null_space
from scipy.optimize import brentq
AUDIT_TIMEOUT_SEC = 90

def fermions(q):
    dim = 1 << q
    ops = []
    for a in range(q):
        rows = []
        cols = []
        data = []
        for n in range(dim):
            if n >> a & 1:
                rows.append(n ^ 1 << a)
                cols.append(n)
                data.append((-1) ** (n & (1 << a) - 1).bit_count())
        ops.append(coo_matrix((data, (rows, cols)), shape=(dim, dim), dtype=float).tocsr())
    return ops

def atomic_checks():
    rows = []
    for q in (4, 6, 8):
        cs = fermions(q)
        D = 1.7
        dim = 1 << q
        s = np.zeros(dim)
        s[0] = s[-1] = 1 / np.sqrt(2)
        H = D * (np.eye(dim) - np.outer(s, s))
        I = np.eye(dim)
        a = cs[0].toarray()
        b = (H @ a - a @ H) / D
        ds = [a, b]
        for z in (0.2 + 0.7j, 1.3 + 0.4j):
            rm = np.linalg.inv(z * I - H)
            rp = np.linalg.inv(z * I + H)
            G = np.array([[s @ A @ rm @ B.T @ s + s @ B.T @ rp @ A @ s for B in ds] for A in ds])
            pred = (z * np.eye(2) - D * np.array([[0, 1], [1, 0]])) / (z * z - D * D)
            assert np.max(abs(G - pred)) < 2e-14
            assert np.max(abs(G @ (z * np.eye(2) + D * np.array([[0, 1], [1, 0]])) - np.eye(2))) < 2e-14
        assert np.linalg.norm(b @ b.T + b.T @ b - I) > 1
        n0 = a.T @ a
        n1 = cs[1].T @ cs[1]
        assert abs(s @ n0 @ n1 @ s - 0.5) < 1e-14
        assert abs(s @ n0 @ s * (s @ n1 @ s) - 0.25) < 1e-14
        a2 = cs[1].toarray()
        pair = a2 @ a @ s
        assert abs(pair @ pair - 0.5) < 1e-14 and np.linalg.norm(H @ pair - D * pair) < 1e-14
        rows.append({'q': q, 'gap': D, 'one_and_two_particle_energy': D, 'composite_not_independent_CAR': True})
    return rows

X = np.array([[0, 1], [1, 0]], complex)

Y = np.array([[0, -1j], [1j, 0]])

Z = np.diag([1, -1])

pauli = [X, Y, Z]

def slab(L, k, offset=0.0):
    b = offset + sum(1 - np.cos(k))
    s = sum((np.sin(k[a]) * pauli[a] for a in range(3)))
    B = b * np.eye(L) - np.eye(L, k=-1)
    H = np.block([[np.kron(np.eye(L), s), np.kron(B, np.eye(2))], [np.kron(B.T, np.eye(2)), -np.kron(np.eye(L), s)]])
    return (H, B, s, b)

def slab_checks():
    rows = []
    for L in (2, 3, 5, 9):
        for k in [np.array(x) * np.pi for x in itertools.product((0, 1), repeat=3)] + [np.array([0.2, 0.7, -1.1]), np.array([1.2, 2.1, 0.4])]:
            H, B, s, b = slab(L, k)
            keep = list(range(4 * L - 2))
            hp = H[np.ix_(keep, keep)]
            v = b ** np.arange(L, dtype=float)
            v /= np.linalg.norm(v)
            V = np.zeros((4 * L - 2, 2), complex)
            V[:2 * L] = np.kron(v[:, None], np.eye(2))
            assert np.max(abs(hp @ V - V @ s)) < 1e-13
            lam = 1 + b * b - 2 * b * np.cos(np.arange(1, L) * np.pi / L)
            sn = np.linalg.norm(np.sin(k))
            expected = [-sn, sn]
            for l in lam:
                expected.extend([-np.sqrt(sn * sn + l)] * 2 + [np.sqrt(sn * sn + l)] * 2)
            assert np.max(abs(np.linalg.eigvalsh(hp) - np.sort(expected))) < 3e-13
            assert min(lam) >= np.sin(np.pi / L) ** 2 - 1e-14
            if sn < 1e-14:
                r = round(b / 2)
                zeros = sum(abs(np.linalg.eigvalsh(hp)) < 1e-11)
                assert zeros == 2
                vel = []
                for axis in range(3):
                    dh = np.zeros_like(hp)
                    dh[:2 * L, :2 * L] = np.kron(np.eye(L), np.cos(k[axis]) * pauli[axis])
                    dh[2 * L:, 2 * L:] = -np.kron(np.eye(L - 1), np.cos(k[axis]) * pauli[axis])
                    vel.append(V.conj().T @ dh @ V)
                sig = (np.trace(vel[0] @ vel[1] @ vel[2]) / 2j).real
                assert abs(sig - (-1) ** r) < 1e-13
                orig_zeros = sum(abs(np.linalg.eigvalsh(H)) < 1e-11)
                assert orig_zeros == (4 if r == 0 else 0)
                short = slab(L - 1, k)[0]
                fullkeep = [i for i in range(4 * L) if i not in (2 * L - 2, 2 * L - 1, 4 * L - 2, 4 * L - 1)]
                assert np.max(abs(H[np.ix_(fullkeep, fullkeep)] - short)) < 1e-14
                rows.append({'L': L, 'corner_pi_count': r, 'projected_zero_modes': int(zeros), 'chirality': int(round(sig)), 'target_end_weight': float(v[0] ** 2), 'mirror_end_weight': float(v[-1] ** 2)})
        h = slab(L, np.zeros(3), offset=0.3)[0]
        assert min(abs(np.linalg.eigvalsh(h))) > 0
    return rows

def gaussian_dilation_checks():
    rows = []
    for L in (2, 4, 7):
        for gap in (0.5, 2.0, 10.0):
            for r in range(4):
                k = np.array([np.pi] * r + [0.0] * (3 - r))
                H, B, s, b = slab(L, k)
                h = np.zeros((4 * L + 2, 4 * L + 2), complex)
                h[:4 * L, :4 * L] = H
                h[4 * L - 2:4 * L, 4 * L:] = gap * np.eye(2)
                h[4 * L:, 4 * L - 2:4 * L] = gap * np.eye(2)
                v = np.r_[b ** np.arange(L), -b ** L / gap]
                v = v / np.linalg.norm(v)
                W = np.zeros((4 * L + 2, 2), complex)
                W[:2 * L] = np.kron(v[:-1, None], np.eye(2))
                W[4 * L:] = v[-1] * np.eye(2)
                assert np.max(abs(h @ W)) < 1e-11
                assert sum(abs(np.linalg.eigvalsh(h)) < 1e-10) == 2
                S = sum((b ** (2 * j) for j in range(L)))
                speed = S / (S + b ** (2 * L) / gap ** 2)
                for a in range(3):
                    dh = np.zeros_like(h)
                    dh[:2 * L, :2 * L] = np.kron(np.eye(L), np.cos(k[a]) * pauli[a])
                    dh[2 * L:4 * L, 2 * L:4 * L] = -np.kron(np.eye(L), np.cos(k[a]) * pauli[a])
                    actual = W.conj().T @ dh @ W
                    assert np.max(abs(actual - speed * np.cos(k[a]) * pauli[a])) < 1e-13
                rows.append({'L': L, 'gap': gap, 'corner_pi_count': r, 'speed': speed, 'chirality': (-1) ** r})
    return rows

def embedding(q, nb):
    P = np.zeros((1 << q + nb, 1 << nb))
    for n in range(1 << nb):
        P[n << q, n] = P[(n << q) + (1 << q) - 1, n] = 1 / np.sqrt(2)
    return P

def fourth_order_checks():
    q = 6
    c = fermions(2 * q)
    P = embedding(q, q)
    V = sum((c[a].T @ c[q + a] + c[q + a].T @ c[a] for a in range(q)))
    V2 = V @ (V @ P)
    A = P.T @ V2
    D4 = P.T @ (V @ (V @ V2))
    n = np.array([x.bit_count() for x in range(1 << q)])
    assert np.max(abs(A - q / 2 * np.eye(1 << q))) < 1e-13
    expected = 3 * (n - q / 2) ** 2 + 3 * q * q / 4 - q
    assert np.max(abs(D4 - np.diag(expected))) < 1e-12
    H4 = 2 * A @ A - D4
    pred = q - q * q / 4 - 3 * (n - q / 2) ** 2
    assert np.max(abs(H4 - np.diag(pred))) < 1e-12
    return {'q': q, 'second_order_scalar': q / 2, 'fourth_order_values_by_number': [float(pred[n == j][0]) for j in range(q + 1)], 'operator_identity_error': float(np.max(abs(H4 - np.diag(pred))))}

def feshbach_checks():
    q = 4
    nb = 2
    c = fermions(q + nb)
    P = embedding(q, nb)
    Q = null_space(P.T)
    H0 = np.eye(len(P)) - P @ P.T
    V = (0.2 * (c[q].T @ c[q + 1] + c[q + 1].T @ c[q]) + 0.3 * (c[0].T @ c[q] + c[q].T @ c[0]) + 0.4 * (c[1].T @ c[q + 1] + c[q + 1].T @ c[1])).toarray()
    v = np.linalg.norm(V, 2)
    A = P.T @ V @ P
    rows = []
    for U in (3.0, 7.0, 15.0):
        assert U > 2 * v
        H = U * H0 + V
        es = np.linalg.eigvalsh(H)
        low = es[:1 << nb]
        assert es[1 << nb] >= U - v - 1e-13
        error = []
        for e in low:
            F = A - P.T @ V @ Q @ np.linalg.solve(Q.T @ H @ Q - e * np.eye(Q.shape[1]), Q.T @ V @ P)
            err = np.linalg.norm(F - A, 2)
            assert err <= v * v / (U - 2 * v)
            assert min(abs(np.linalg.eigvalsh(F) - e)) < 1e-12
            error.append(err)
        rows.append({'U': U, 'V_norm': v, 'bound': v * v / (U - 2 * v), 'largest_Feshbach_error': max(error), 'low_spectrum': low.tolist()})
    return rows

def matrix(L, k, kind, D=1.0):
    H, B, s, b = slab(L, k)
    dhs = []
    for a in range(3):
        ds = np.cos(k[a]) * pauli[a]
        db = np.sin(k[a]) * np.eye(L)
        dhs.append(np.block([[np.kron(np.eye(L), ds), np.kron(db, np.eye(2))], [np.kron(db.T, np.eye(2)), -np.kron(np.eye(L), ds)]]))
    if kind == 'projected':
        return (H[:-2, :-2], [d[:-2, :-2] for d in dhs])
    h = np.zeros((4 * L + 2, 4 * L + 2), complex)
    h[:4 * L, :4 * L] = H
    h[4 * L - 2:4 * L, 4 * L:] = D * np.eye(2)
    h[4 * L:, 4 * L - 2:4 * L] = D * np.eye(2)
    ds = []
    for d in dhs:
        u = np.zeros_like(h)
        u[:4 * L, :4 * L] = d
        ds.append(u)
    return (h, ds)

def optical(kind, L, D, omega):
    zn, zw = np.polynomial.legendre.leggauss(6)
    corners = []
    for bits in itertools.product((0, 1), repeat=3):
        k0 = np.pi * np.array(bits)
        b = 2 * sum(bits)
        S = sum((b ** (2 * j) for j in range(L)))
        v = 1.0 if kind == 'projected' else S / (S + b ** (2 * L) / D ** 2)
        integ = 0.0
        for z, w in zip(zn, zw):
            for phi in np.arange(12) * 2 * np.pi / 12:
                n = np.array([np.sqrt(1 - z * z) * np.cos(phi), np.sqrt(1 - z * z) * np.sin(phi), z])

                def energy(r):
                    vals = np.linalg.eigvalsh(matrix(L, k0 + r * n, kind, D)[0])
                    mid = len(vals) // 2
                    return vals[mid] - vals[mid - 1]
                lo = omega / (4 * v)
                hi = omega / v
                assert energy(lo) < omega < energy(hi)
                radius = brentq(lambda r: energy(r) - omega, lo, hi, xtol=1e-13)
                h, ds = matrix(L, k0 + radius * n, kind, D)
                es, vs = np.linalg.eigh(h)
                mid = len(es) // 2
                minus = vs[:, mid - 1]
                plus = vs[:, mid]
                dr = sum((n[a] * ds[a] for a in range(3)))
                slope = (plus.conj() @ dr @ plus - minus.conj() @ dr @ minus).real
                vertex = abs(plus.conj() @ ds[0] @ minus) ** 2
                integ += w * 2 * np.pi / 12 * radius ** 2 * vertex / slope
        sigma = np.pi / omega / (2 * np.pi) ** 3 * integ
        corners.append({'pi_components': list(bits), 'normalized_slope': float(sigma / omega * 24 * np.pi), 'expected_inverse_speed': v ** (-1)})
    total = sum((x['normalized_slope'] for x in corners))
    expected = sum((x['expected_inverse_speed'] for x in corners))
    assert abs(total / expected - 1) < 0.001
    return {'kind': kind, 'L': L, 'D': D, 'omega': omega, 'sum_normalized_optical_slope': total, 'predicted': expected, 'relative_error': total / expected - 1, 'corners': corners}

def sector(q, n):
    bath = (1 << n) - 1
    mask = (1 << q) - 1
    starts = [bath << q, bath << q | mask]
    states = set(starts)
    todo = starts[:]
    while todo:
        s = todo.pop()
        a = s & mask
        b = s >> q
        moves = []
        if a in (0, mask):
            moves.append(s ^ mask)
        for j in range(q):
            if s >> j & 1 != s >> q + j & 1:
                moves.append(s ^ 1 << j ^ 1 << q + j)
        for z in moves:
            if z not in states:
                states.add(z)
                todo.append(z)
    states = sorted(states)
    ix = {s: i for i, s in enumerate(states)}
    H0 = np.eye(len(states))
    V = np.zeros_like(H0)
    for s in states:
        a = s & mask
        i = ix[s]
        if a in (0, mask):
            H0[i, i] = 0.5
            H0[ix[s ^ mask], i] = -0.5
        for j in range(q):
            f = s >> j & 1
            c = s >> q + j & 1
            if f != c:
                between = s >> j + 1 & (1 << q - 1) - 1
                sign = (-1) ** between.bit_count()
                V[ix[s ^ 1 << j ^ 1 << q + j], i] = sign
    return (H0, V)

def series_checks():
    rows = []
    q = 6
    for n in range(q // 2 + 1):
        H0, V = sector(q, n)
        count = sum(abs(np.linalg.eigvalsh(H0)) < 1e-13)
        assert count == (2 if n == 0 else 1)
        pred4 = q - q * q / 4 - 3 * (n - q / 2) ** 2
        prev = None
        for t in (0.04, 0.025, 0.015):
            low = np.linalg.eigvalsh(H0 + t * V)[:count]
            pred = -q * t * t / 2 + pred4 * t ** 4
            error = max(abs(low - pred))
            assert error < 3000 * t ** 6
            if prev is not None:
                assert error < prev
            prev = error
            rows.append({'n': n, 'sector_dimension': len(H0), 't': t, 'exact_low': low.tolist(), 'fourth_order': pred, 'remainder_over_t6': float(error / t ** 6)})
    return rows

def spin10_checks():
    I = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], complex)
    Y = np.array([[0, -1j], [1j, 0]])
    Z = np.diag([1, -1]).astype(complex)

    def kron(xs):
        return reduce(np.kron, xs)
    gamma = [kron([I] * k + [s] + [Z] * (4 - k)) for k in range(5) for s in (X, Y)]
    P = np.where(np.diag(kron([Z] * 5)).real > 0)[0]
    gen = [(0.5j * gamma[a] @ gamma[b])[np.ix_(P, P)] for a, b in combinations(range(10), 2)]
    C = kron([Y, X, Y, X, Y])
    M = [(C @ g)[np.ix_(P, P)] for g in gamma]
    assert all((np.max(abs(m - m.T)) < 1e-14 for m in M))
    cas = sum((t @ t for t in gen))
    assert np.max(abs(cas - 45 / 4 * np.eye(16))) < 1e-14
    C2 = 2 * np.kron(cas, np.eye(16)) + 2 * sum((np.kron(t, t) for t in gen))
    gram = np.array([[np.trace(a @ b) for b in gen] for a in gen])
    assert np.array_equal(gram, 4 * np.eye(45))
    coef = {}
    for a, c in combinations(range(16), 2):
        for b, d in combinations(range(16), 2):
            v = sum((m[a, b] * m[c, d] - m[a, d] * m[c, b] for m in M))
            if abs(v) > 1e-12:
                coef[a, c, b, d] = v
    intertwiner_error = 0.0
    for (a, b), t in zip(combinations(range(10), 2), gen):
        for c in range(10):
            expected = 1j * ((M[b] if c == a else np.zeros((16, 16))) - (M[a] if c == b else np.zeros((16, 16))))
            err = t.T @ M[c] + M[c] @ t - expected
            assert np.array_equal(err, np.zeros((16, 16)))
            intertwiner_error = max(intertwiner_error, float(np.max(abs(err))))
    C2i = np.rint(C2.real).astype(np.int64)
    assert np.array_equal(C2, C2i)
    I256 = np.eye(256, dtype=np.int64)
    # Integer products are bounded by 256**2 * 50**3 < 2**63.
    assert np.max(abs(C2i)) <= 25
    poly = (C2i - 9 * I256) @ (C2i - 21 * I256) @ (C2i - 25 * I256)
    assert np.array_equal(poly, np.zeros((256, 256), dtype=np.int64))
    swap = I256[np.arange(256).reshape(16, 16).T.ravel()]
    assert np.array_equal((C2i - 21 * I256) @ (I256 - swap), np.zeros((256, 256), dtype=np.int64))
    multiplicities = {}
    for value in (9, 21, 25):
        other = [a for a in (9, 21, 25) if a != value]
        p = (C2i - other[0] * I256) @ (C2i - other[1] * I256)
        num = int(np.trace(p)); den = (value - other[0]) * (value - other[1])
        assert num % den == 0
        multiplicities[value] = num // den
    assert multiplicities == {9: 10, 21: 120, 25: 126}
    g = np.diag([1.0, -1.0] + [0.0] * 14)
    extra = np.kron(g, np.eye(16)) + np.kron(np.eye(16), g)
    assert np.linalg.norm(C2 @ extra - extra @ C2) > 1
    omega = {a: -2 * c for a, c in coef.items()}
    bound = 2 * sum((abs(c) for c in omega.values()))
    assert len(omega) == 240 and bound == 2560 and omega[0, 1, 14, 15] == 8
    omega_create = {(a, c, 16 + b, 16 + d): np.conj(v) for (a, c, b, d), v in omega.items()}
    for t in gen:
        action = defaultdict(complex)
        for ids, value in omega_create.items():
            for slot, src in enumerate(ids):
                block, alpha = divmod(src, 16)
                for beta in np.nonzero(t[:, alpha])[0]:
                    changed = list(ids)
                    changed[slot] = 16 * block + int(beta)
                    if len(set(changed)) < 4:
                        continue
                    inv = sum((changed[a] > changed[b] for a in range(4) for b in range(a + 1, 4)))
                    action[tuple(sorted(changed))] += value * t[beta, alpha] * (-1) ** inv
        assert all((v == 0 for v in action.values()))
    return {'one_particle_Casimir': 45 / 4, 'two_particle_Casimir_multiplicities': multiplicities, 'quartic_coefficient_count': len(omega), 'quartic_norm_bound': float(bound), 'all_45_exterior_actions_zero': True}


def degenerate_sector_check():
    c=fermions(3)
    nf=c[0].T@c[0];nd=c[1].T@c[1]
    hop=(c[0].T@c[2]+c[2].T@c[0]).toarray()
    keep=[n for n in range(8) if not n&2]
    zeros=[n for n in range(8) if not ((n&1) and (n&2))]
    assert np.linalg.norm(c[0].toarray()[np.ix_(zeros,zeros)],2)==1
    for U in (2.,13.,101.):
        H=U*(nf@nd).toarray()+hop
        assert np.array_equal(H[np.ix_(keep,keep)],hop[np.ix_(keep,keep)])
        assert np.max(abs(np.linalg.eigvalsh(H[np.ix_(keep,keep)])-[-1,0,0,1]))<1e-14
    return {'zero_space_dimension':len(zeros),'participating_fermion_survives':True}

def complex_second_order_check():
    q=4;nb=3;c=fermions(q+nb);P=embedding(q,nb)
    rng=np.random.default_rng(6172);T=rng.normal(size=(q,nb))+1j*rng.normal(size=(q,nb))
    V=sum(T[a,b]*(c[a].T@c[q+b])+T[a,b].conjugate()*(c[q+b].T@c[a]) for a in range(q) for b in range(nb))
    A=P.T@(V@(V@P));scalar=np.trace(T.conj().T@T).real/2
    assert np.max(abs(A-scalar*np.eye(1<<nb)))<1e-13
    return {'nonuniform_complex_hopping_scalar':scalar,'bilinear_cancellation_error':float(np.max(abs(A-scalar*np.eye(1<<nb))))}

def check_symmetric_atom_and_spectral_functions():
    print(json.dumps({'Spin10':spin10_checks(),'atomic_spectral_functions':atomic_checks(),'degenerate_hypothesis_guard':degenerate_sector_check()},sort_keys=True))

def check_projected_and_dilated_boundary_spectra():
    print(json.dumps({'projected_slab':slab_checks(),'quadratic_dilation':gaussian_dilation_checks()},sort_keys=True))

def check_induced_terms_and_fixed_box_control():
    print(json.dumps({'second_order':complex_second_order_check(),'fourth_order_operator':fourth_order_checks(),'independent_low_spectrum':series_checks(),'Feshbach':feshbach_checks()},sort_keys=True))

def check_actual_lattice_current_response():
    results=[]
    for kind in ('projected','quadratic_dilation'):
        for omega in (.001,.0005):
            r=optical(kind,3,1.,omega)
            results.append({k:v for k,v in r.items() if k!='corners'})
    print(json.dumps({'actual_interband_Kubo_integrals':results},sort_keys=True))

def main():
    checks=[check_symmetric_atom_and_spectral_functions,check_projected_and_dilated_boundary_spectra,check_induced_terms_and_fixed_box_control,check_actual_lattice_current_response]
    failed=0
    for check in checks:
        try:
            check()
            print('PASS: '+check.__name__,flush=True)
        except Exception:
            failed+=1
            traceback.print_exc()
    print('per_element: exact Clifford, Casimir and fourth exterior-tensor identities test the supplied Spin(10) interaction')
    print('per_site: full atomic Fock spaces challenge the gap, elementary and composite propagators, and non-Gaussianity')
    print('per_mode: complete projected slab spectra and actual velocity matrices detect all eight corner nodes and their handedness')
    print('per_block: full atom-bath operators and a separate reduced-sector spectrum challenge the induced interaction and Schur bound')
    print('lattice_wide: actual-current Kubo surface integrals test the free infrared response; no finite-coupling chiral phase is inferred')
    print('TOTAL: PASS='+str(len(checks)-failed)+' FAIL='+str(failed))
    return int(failed>0)
if __name__=='__main__':raise SystemExit(main())
