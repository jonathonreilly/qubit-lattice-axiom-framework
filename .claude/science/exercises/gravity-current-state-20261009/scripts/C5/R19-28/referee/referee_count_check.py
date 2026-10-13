"""Independent exact check of the R19-28 invariant and Ward counts.

This deliberately does not import or reuse scripts/r1928_count_z4.py.  It uses
(i) exact character averages for finite signed-permutation groups and
(ii) integer tensor-orbit bases plus exact SymPy ranks for the Ward map.
O(4) invariant tensors are generated independently from Kronecker-delta
pairings.
"""

from itertools import permutations, product
from math import factorial

import numpy as np
from sympy import Matrix


D = 4


def compose(g, h):
    """Signed permutations acting as e_i -> sign[i] e_perm[i]."""
    pg, sg = g
    ph, sh = h
    return (
        tuple(pg[ph[i]] for i in range(D)),
        tuple(sh[i] * sg[ph[i]] for i in range(D)),
    )


def power(g, n):
    out = (tuple(range(D)), (1,) * D)
    for _ in range(n):
        out = compose(g, out)
    return out


def trace_v(g):
    p, s = g
    return sum(s[i] for i in range(D) if p[i] == i)


def det_perm(p):
    inversions = sum(p[i] > p[j] for i in range(D) for j in range(i + 1, D))
    return -1 if inversions % 2 else 1


def full_signed_group(proper_only=False):
    out = []
    for p in permutations(range(D)):
        for s in product((-1, 1), repeat=D):
            if proper_only and det_perm(p) * np.prod(s) != 1:
                continue
            out.append((p, s))
    return out


def oht_group():
    out = []
    for ps in permutations((1, 2, 3)):
        for signs in product((-1, 1), repeat=4):
            p = (0,) + ps
            out.append((p, signs))
    return out


def character_counts(group):
    sums = np.zeros(3, dtype=object)
    for g in group:
        v1 = trace_v(g)
        v2 = trace_v(power(g, 2))
        v4 = trace_v(power(g, 4))
        sym2 = (v1 * v1 + v2) // 2
        sym2_g2 = (v2 * v2 + v4) // 2
        pair_pair = (sym2 * sym2 + sym2_g2) // 2
        sums += np.array((sym2, pair_pair, pair_pair * sym2), dtype=object)
    assert all(x % len(group) == 0 for x in sums)
    return tuple(int(x // len(group)) for x in sums)


def intrinsic_group(n):
    generators = []
    pair_swaps = [(0, 1)]
    if n >= 4:
        pair_swaps.append((2, 3))
    if n == 6:
        pair_swaps.append((4, 5))
    for a, b in pair_swaps:
        p = list(range(n))
        p[a], p[b] = p[b], p[a]
        generators.append(tuple(p))
    if n >= 4:
        p = list(range(n))
        p[0], p[2] = p[2], p[0]
        p[1], p[3] = p[3], p[1]
        generators.append(tuple(p))
    group = {tuple(range(n))}
    frontier = list(group)
    while frontier:
        old = frontier.pop()
        for gen in generators:
            new = tuple(old[gen[i]] for i in range(n))
            if new not in group:
                group.add(new)
                frontier.append(new)
    return tuple(group)


def canonical_coordinate_pattern(t, kind):
    counts = [t.count(i) for i in range(D)]
    if any(c % 2 for c in counts):
        return None
    if kind == "wb4":
        remap = {}
        nxt = 0
        out = []
        for x in t:
            if x not in remap:
                remap[x] = nxt
                nxt += 1
            out.append(remap[x])
        return tuple(out)
    if kind == "oht":
        remap = {}
        nxt = 1
        out = []
        for x in t:
            if x == 0:
                out.append(0)
            else:
                if x not in remap:
                    remap[x] = nxt
                    nxt += 1
                out.append(remap[x])
        return tuple(out)
    raise ValueError(kind)


def orbit_key(t, kind, slot_group):
    variants = []
    for p in slot_group:
        u = tuple(t[p[i]] for i in range(len(t)))
        c = canonical_coordinate_pattern(u, kind)
        if c is not None:
            variants.append(c)
    return min(variants) if variants else None


def orbit_basis(n, kind):
    slots = intrinsic_group(n)
    keys = sorted(
        {
            key
            for t in product(range(D), repeat=n)
            if (key := orbit_key(t, kind, slots)) is not None
        }
    )
    columns = []
    for key in keys:
        arr = np.zeros((D,) * n, dtype=int)
        for t in product(range(D), repeat=n):
            if orbit_key(t, kind, slots) == key:
                arr[t] = 1
        columns.append(arr)
    return columns


def all_pairings(items):
    if not items:
        yield ()
        return
    first = items[0]
    for i in range(1, len(items)):
        second = items[i]
        rest = items[1:i] + items[i + 1 :]
        for tail in all_pairings(rest):
            yield ((first, second),) + tail


def o4_pairing_basis(n):
    slots = intrinsic_group(n)
    raw = []
    for pairing in all_pairings(tuple(range(n))):
        arr = np.zeros((D,) * n, dtype=int)
        for t in product(range(D), repeat=n):
            if all(t[i] == t[j] for i, j in pairing):
                for p in slots:
                    arr[tuple(t[p[i]] for i in range(n))] += 1
        raw.append(arr.reshape(-1))
    mat = Matrix(np.stack(raw, axis=1))
    pivots = mat.rref()[1]
    return [raw[i].reshape((D,) * n) for i in pivots]


def ward_rank(columns):
    monomials = list(product(range(D), repeat=3))
    monomials = sorted(set(tuple(sorted(x)) for x in monomials))
    rows = [(n, r, s, mono) for n in range(D) for r in range(D) for s in range(D) for mono in monomials]
    lookup = {row: i for i, row in enumerate(rows)}
    mat = np.zeros((len(rows), len(columns)), dtype=int)
    for j, tensor in enumerate(columns):
        for m, n, r, s, a, b in product(range(D), repeat=6):
            mat[lookup[(n, r, s, tuple(sorted((m, a, b))))], j] += tensor[m, n, r, s, a, b]
    return Matrix(mat).rank()


def ward_image(tensor):
    monomials = sorted(set(tuple(sorted(x)) for x in product(range(D), repeat=3)))
    rows = [(n, r, s, mono) for n in range(D) for r in range(D) for s in range(D) for mono in monomials]
    lookup = {row: i for i, row in enumerate(rows)}
    out = np.zeros(len(rows), dtype=int)
    for m, n, r, s, a, b in product(range(D), repeat=6):
        out[lookup[(n, r, s, tuple(sorted((m, a, b))))]] += tensor[m, n, r, s, a, b]
    return out


def four_times_einstein_tensor():
    """Coefficient tensor for 4 times the standard linearized EH kernel."""
    delta = lambda i, j: int(i == j)
    out = np.zeros((D,) * 6, dtype=int)
    for m, n, r, s, a, b in product(range(D), repeat=6):
        p2 = 2 * (
            delta(m, r) * delta(n, s)
            + delta(m, s) * delta(n, r)
            - 2 * delta(m, n) * delta(r, s)
        ) * delta(a, b)
        cross = -(
            delta(m, r) * (delta(a, n) * delta(b, s) + delta(a, s) * delta(b, n))
            + delta(m, s) * (delta(a, n) * delta(b, r) + delta(a, r) * delta(b, n))
            + delta(n, r) * (delta(a, m) * delta(b, s) + delta(a, s) * delta(b, m))
            + delta(n, s) * (delta(a, m) * delta(b, r) + delta(a, r) * delta(b, m))
        )
        traces = 2 * (
            delta(m, n) * (delta(a, r) * delta(b, s) + delta(a, s) * delta(b, r))
            + delta(r, s) * (delta(a, m) * delta(b, n) + delta(a, n) * delta(b, m))
        )
        out[m, n, r, s, a, b] = p2 + cross + traces
    return out


def report_finite(name, group, kind):
    chars = character_counts(group)
    direct = tuple(len(orbit_basis(n, kind)) for n in (2, 4, 6))
    assert chars == direct
    wrank = ward_rank(orbit_basis(6, kind))
    print(f"{name}: one={chars[0]} deg0={chars[1]} deg2={chars[2]} total={sum(chars)} ward2_null={chars[2]-wrank}")


def report_o4():
    dims = tuple(len(o4_pairing_basis(n)) for n in (2, 4, 6))
    wrank = ward_rank(o4_pairing_basis(6))
    print(f"O(4): one={dims[0]} deg0={dims[1]} deg2={dims[2]} total={sum(dims)} ward2_null={dims[2]-wrank}")


if __name__ == "__main__":
    report_finite("W(B4)", full_signed_group(), "wb4")
    report_finite("O_h x T", oht_group(), "oht")
    # Proper B4+ has the same character counts here; direct orbit construction
    # above targets W(B4), the group actually asked for in section 3.1.
    print("B4+ character counts:", character_counts(full_signed_group(proper_only=True)))
    report_o4()
    eh = four_times_einstein_tensor()
    assert not np.any(ward_image(eh))
    wb4 = orbit_basis(6, "wb4")
    coeffs = Matrix(np.stack([x.reshape(-1) for x in wb4], axis=1)).gauss_jordan_solve(Matrix(eh.reshape(-1)))[0]
    assert any(c != 0 for c in coeffs)
    print("EH check: W(B4)-invariant, Ward-exact, and nonzero; uniqueness follows from ward2_null=1")
