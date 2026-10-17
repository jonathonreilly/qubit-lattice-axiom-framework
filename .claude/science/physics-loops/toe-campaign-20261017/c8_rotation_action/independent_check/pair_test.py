"""Independent probe of item 5 (fractionalization) by a method different from
the note's: the C2 eigenvalue of a two-fermion state with the fermions at
C2-swapped positions x, Rx (off the axis).

For a realization U_R = P_R that maps the signed group G_s to itself,
  P_R S|GS> = S^R P_R|GS> = lambda * S P_R|GS>,   S^R := P_R S P_R^{-1},
where S is a product of edge operators from x to Rx and lambda is the sign of
S^dag S^R inside G_s.  lambda is independent of the path and (for pairs far
from the axis) of x; spin-statistics for point particles gives
lambda = theta_f * eta_f(C2,C2) with theta_f = -1 for the BKSF charge, so
eta_f = -lambda.  (Control: 3D toric code, boson, expect lambda = +1.)

We test vertex-axis C2's (the note's case) and translated C2's v -> M v + t
whose axis contains no vertex (rotations about edge midpoints, plaquette
centres, cube centres), which are equally symmetries of the code.

Also: dressing by a logical straight fermion string W along a lattice C2 axis
and by a logical membrane, U = P_R F, and what U^2 is.

Usage: python3 pair_test.py L
"""
import itertools
import json
import sys
import time
from collections import Counter, defaultdict

from pauli_bksf import (Code, Lattice, Span, canonical, edge_perm, matvec,
                        order_of, permute_pauli, pmul, rotations,
                        sign_vs_canonical, DIRS)

L = int(sys.argv[1]) if len(sys.argv) > 1 else 6
lat = Lattice(L)
ROTS = rotations()
t0 = time.time()


def dagger(P):
    x, z, p = P
    return (x, z, (-p + 2 * (x & z).bit_count()) % 4)


class ToricCode(Code):
    """Control: 3D toric code. A(v,a) = Z on the edge (charge hop),
    B_v = X on the six edges, plaquette = product of 4 Z."""

    def __init__(self, lat):
        self.lat = lat
        self.order = ("toric",)
        self._A = {}

    def A(self, v, a):
        return (0, 1 << self.lat.edge(v, a), 0)

    def B(self, v):
        x = 0
        for d in DIRS:
            x ^= 1 << self.lat.edge_at(v, d)
        return (x, 0, 0)


def path_ops(code, x, y):
    """Product of A's along a Manhattan path x -> y (axis order 0,1,2), using
    shortest torus displacement. Returns Pauli (ordered product)."""
    P = (0, 0, 0)
    cur = list(x)
    for a in range(3):
        d = (y[a] - cur[a]) % L
        if d > L // 2:
            d -= L
        step = 1 if d > 0 else -1
        for _ in range(abs(d)):
            if step == 1:
                op = code.A(tuple(cur), a)
            else:
                w = list(cur)
                w[a] -= 1
                op = code.A(tuple(w), a)
            P = pmul(P, op)
            cur[a] += step
    assert all((cur[i] - y[i]) % L == 0 for i in range(3))
    return P


def plaq_counts(combo, plaq_c):
    nc = [0, 0, 0]
    j = 0
    while combo:
        if combo & 1 and plaq_c[j] >= 0:
            nc[plaq_c[j]] += 1
        combo >>= 1
        j += 1
    return nc


def signed_sign(sp, combo, plaq_c, s):
    prod = sp.product(combo)
    nc = plaq_counts(combo, plaq_c)
    return sign_vs_canonical(prod) * (-1) ** sum(s[c] * nc[c] for c in range(3)), prod


_AXIS_CACHE = {}


def axis_type(M, t):
    """Classify the fixed line of v -> M v + t: which lattice objects it meets
    (vertex, edge midpoint, plaquette centre, cube centre)."""
    import fractions
    key = (M, t)
    if key in _AXIS_CACHE:
        return _AXIS_CACHE[key]
    types = set()
    rng = range(-4, 5)
    for v in itertools.product(rng, repeat=3):
        vv = tuple(fractions.Fraction(c, 2) for c in v)
        Mv = matvec(M, vv)
        if all(Mv[i] + t[i] == vv[i] for i in range(3)):
            nint = sum(1 for c in vv if c.denominator == 1)
            types.add({3: "vertex", 2: "edge-mid", 1: "plaq-centre", 0: "cube-centre"}[nint])
    out = "+".join(sorted(types)) if types else "screw(no fixed pt)"
    _AXIS_CACHE[key] = out
    return out


def main():
    reps = [tuple(r) for r in json.load(open("reps_L4.json"))]
    codes = [("toric", ToricCode(lat))] + [(str(r), Code(lat, r)) for r in reps]
    perm_cache = {}
    summary = defaultdict(Counter)
    for name, code in codes:
        gens0 = code.generators((0, 0, 0))
        labels = [lab for lab, _ in gens0]
        paulis0 = [g for _, g in gens0]
        plaq_c = [lab[2] if lab[0] == "P" else -1 for lab in labels]
        sp = Span(paulis0, lat.n)
        hs = code.hop_signs()
        h = tuple(next(iter(hs[c])) for c in range(3))
        s0 = tuple(0 if h[c] == 1 else 1 for c in range(3))
        spi = tuple(1 - s0[c] for c in range(3))
        base = [i for i, lab in enumerate(labels) if lab[1] == (0, 0, 0)]
        # stabilizing rotations (unsigned) -- test translation reps only (L-torus,
        # translation covariance makes this sufficient)
        stab = []
        for ri, M in enumerate(ROTS):
            key = (ri, (0, 0, 0))
            if key not in perm_cache:
                perm_cache[key] = edge_perm(lat, M)
            perm = perm_cache[key]
            if all(sp.decompose(permute_pauli(paulis0[i], perm)) is not None for i in base):
                stab.append(ri)
        c2s = [ri for ri in stab if order_of(ROTS[ri]) == 2]
        line = [name, "stab", len(stab)]
        for sector_name, s in (("flux0", s0), ("fluxpi", spi)):
            for ri in c2s:
                M = ROTS[ri]
                # translations t with |t_i|<=1 giving pure rotations, one per axis type
                seen = {}
                for t in itertools.product([0, 1], repeat=3):
                    at = axis_type(M, t)
                    if at.startswith("screw"):
                        continue
                    if at not in seen:
                        seen[at] = t
                for at, t in sorted(seen.items()):
                    key = (ri, t)
                    if key not in perm_cache:
                        perm_cache[key] = edge_perm(lat, M, t)
                    perm = perm_cache[key]
                    # signed invariance under this rotation (bare perm)
                    ok = True
                    for i in base:
                        img = permute_pauli(paulis0[i], perm)
                        cb = sp.decompose(img)
                        sg, _ = signed_sign(sp, cb, plaq_c, s)
                        sgen = (-1) ** s[plaq_c[i]] if plaq_c[i] >= 0 else 1
                        if sg != sign_vs_canonical(img) * sgen:
                            ok = False
                    lams = []
                    # is the stabilizer Hamiltonian -sum B - sum P^sigma itself
                    # P_R-symmetric (plaquette supports map to plaquette supports)?
                    supp = set((g[0], g[1]) for g in paulis0)
                    hsym = all((lambda im: (im[0], im[1]) in supp)(permute_pauli(paulis0[i], perm)) for i in base)
                    if not hsym:
                        summary[(sector_name, at)][("H_sigma not symmetric", ok)] += 1
                        line.append(f"{sector_name} C2{M} t={t} [{at}] Pok={ok} H_sigma-not-symmetric")
                        continue
                    # vertices x near the axis, not fixed
                    for x in itertools.product(range(-2, 3), repeat=3):
                        Rx = tuple((matvec(M, x)[i] + t[i]) for i in range(3))
                        if all((Rx[i] - x[i]) % L == 0 for i in range(3)):
                            continue
                        # keep displacements small so paths stay local
                        if max(abs(((Rx[i] - x[i]) + L // 2) % L - L // 2) for i in range(3)) > 2:
                            continue
                        S = path_ops(code, x, Rx)
                        SR = permute_pauli(S, perm)
                        O = pmul(dagger(S), SR)
                        cb = sp.decompose(O)
                        assert cb is not None, (name, at, x)
                        sg, prod = signed_sign(sp, cb, plaq_c, s)
                        # O = c * (signed group element) ; signed elt = sg*canonical
                        lam = sign_vs_canonical(O) / sg
                        lams.append(lam)
                    lamset = sorted(set(complex(l).real if complex(l).imag == 0 else l for l in lams), key=str)
                    summary[(sector_name, at)][(str(lamset), ok)] += 1
                    line.append(f"{sector_name} C2{M} t={t} [{at}] Pok={ok} lambda={lamset} (n={len(lams)})")
        print(" | ".join(map(str, line)), f"({time.time()-t0:.0f}s)", flush=True)
    print()
    print("SUMMARY: (sector, axis type) -> {(lambda values, bare-perm preserves signed group): count of (code, C2)}")
    for k in sorted(summary):
        print(" ", k, dict(summary[k]))


if __name__ == "__main__":
    main()
