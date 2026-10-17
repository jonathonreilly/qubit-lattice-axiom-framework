"""Independent implementation of the GENERAL pair test (claim (a) of the
extended C8 note), written before reading the runner.

For a code, a stabilizing rotation v -> M v + t (an involution) and a vertex x:
solve over GF(2), with support in an R-invariant window, for a Pauli S with
  - B_x and B_{Rx} flipped, every other vertex generator unflipped;
  - no plaquette generator flipped unless one of its corners is within
    L-infinity distance 1 of x or Rx;
  - <S, g> = <S^R, g> for every generator g (same syndrome as S^R).
Then O = S^dag S^R commutes with every generator; if it is in +-G (local,
contractible), lambda = sign of O in the signed group G_s.

Contamination probe: lambda is computed for MANY random solutions (particular
solution + random nullspace vectors), so any dependence on the choice of S
(e.g. through extra symmetric local excitations) shows up as a spread.

Usage: python3 general_pair_test.py L [quick]
"""
import itertools
import json
import random
import sys
import time
from collections import Counter

from pauli_bksf import (Code, Lattice, Span, edge_perm, matvec, order_of,
                        permute_pauli, pmul, rotations, sign_vs_canonical, DIRS)
from pair_test import ToricCode, dagger, axis_type

L = int(sys.argv[1]) if len(sys.argv) > 1 else 8
QUICK = len(sys.argv) > 2
lat = Lattice(L)
random.seed(7)
t0 = time.time()


def tdiff(a, b):
    return tuple(((a[i] - b[i] + L // 2) % L) - L // 2 for i in range(3))


def dinf(a, b):
    return max(abs(c) for c in tdiff(a, b))


def mpath(x, y):
    pts = [tuple(c % L for c in x)]
    cur = list(x)
    d = tdiff(y, x)
    for a in range(3):
        st = 1 if d[a] > 0 else -1
        for _ in range(abs(d[a])):
            cur[a] += st
            pts.append(tuple(c % L for c in cur))
    return pts


def solve_gf2(rows, ncols):
    """rows: list of ints with bit ncols = rhs. Returns (particular, nullbasis)
    or (None, None) if inconsistent."""
    piv = {}
    for r in rows:
        for c, (pr) in list(piv.items()):
            pass
        # reduce
        rr = r
        while True:
            low = rr & ((1 << ncols) - 1)
            if low == 0:
                break
            c = low.bit_length() - 1
            if c in piv:
                rr ^= piv[c]
            else:
                piv[c] = rr
                break
        else:
            pass
        if (rr & ((1 << ncols) - 1)) == 0 and (rr >> ncols) & 1:
            return None, None
    # back-substitute to reduced form
    cols = sorted(piv)
    for c in cols:
        for c2 in cols:
            if c2 != c and (piv[c2] >> c) & 1:
                piv[c2] ^= piv[c]
    part = 0
    for c in cols:
        if (piv[c] >> ncols) & 1:
            part |= 1 << c
    free = [c for c in range(ncols) if c not in piv]
    null = []
    for f in free:
        v = 1 << f
        for c in cols:
            if (piv[c] >> f) & 1:
                v |= 1 << c
        null.append(v)
    return part, null


def run_case(code, gens, labels, sp, plaq_c, sectors, M, t, x, nsamples=6):
    perm = edge_perm(lat, M, t)
    Rx = tuple((matvec(M, x)[i] + t[i]) % L for i in range(3))
    x = tuple(c % L for c in x)
    path = mpath(x, Rx)
    Rpath = [tuple((matvec(M, p)[i] + t[i]) % L for i in range(3)) for p in path]
    core = set(path) | set(Rpath)
    Wv = set()
    for p in core:
        for d in itertools.product([-1, 0, 1], repeat=3):
            Wv.add(tuple((p[i] + d[i]) % L for i in range(3)))
    # window edges
    wedges = []
    for v in Wv:
        for a in range(3):
            w = lat.add(v, a)
            if tuple(c % L for c in w) in Wv:
                wedges.append(lat.edge(v, a))
    wedges = sorted(set(wedges))
    assert set(perm[e] for e in wedges) == set(wedges), "window not R-invariant"
    nw = len(wedges)
    col = {e: i for i, e in enumerate(wedges)}
    wmask = 0
    for e in wedges:
        wmask |= 1 << e

    def row_of(g):
        """symplectic row over window vars: S=(sx,sz); <S,g> = sx.gz + sz.gx"""
        r = 0
        gx, gz = g[0] & wmask, g[1] & wmask
        while gz:
            low = gz & -gz; e = low.bit_length() - 1
            r |= 1 << col[e]; gz ^= low
        while gx:
            low = gx & -gx; e = low.bit_length() - 1
            r |= 1 << (nw + col[e]); gx ^= low
        return r

    ncols = 2 * nw
    rows = []
    near = lambda v: dinf(v, x) <= 1 or dinf(v, Rx) <= 1
    for (lab, g) in zip(labels, gens):
        if not ((g[0] | g[1]) & wmask):
            continue
        r = row_of(g)
        if lab[0] == "B":
            v = lab[1]
            rhs = 1 if v in (x, Rx) else 0
            rows.append(r | (rhs << ncols))
        else:
            v, c = lab[1], lab[2]
            a, b = [q for q in range(3) if q != c]
            corners = [v, lat.add(v, a), lat.add(v, b), lat.add(lat.add(v, a), b)]
            corners = [tuple(q % L for q in cc) for cc in corners]
            if not any(near(cc) for cc in corners):
                rows.append(r)
        # symmetry: <S, g> = <S, P g>
        rows.append(r ^ row_of(permute_pauli(g, perm)))
    part, null = solve_gf2(rows, ncols)
    if part is None:
        return None
    lams = {s: Counter() for s in sectors}
    for k in range(nsamples):
        sol = part
        if k > 0:
            for nv in null:
                if random.random() < 0.5:
                    sol ^= nv
        sx = sz = 0
        for i, e in enumerate(wedges):
            if (sol >> i) & 1:
                sx |= 1 << e
            if (sol >> (nw + i)) & 1:
                sz |= 1 << e
        S = (sx, sz, 0)
        SR = permute_pauli(S, perm)
        O = pmul(dagger(S), SR)
        # syndrome check of S
        for (lab, g) in zip(labels, gens):
            com = ((S[0] & g[1]).bit_count() + (S[1] & g[0]).bit_count()) & 1
            if lab[0] == "B":
                assert com == (1 if lab[1] in (x, Rx) else 0)
            comO = ((O[0] & g[1]).bit_count() + (O[1] & g[0]).bit_count()) & 1
            assert comO == 0
        cb = sp.decompose(O)
        for sname, s in sectors.items():
            if cb is None:
                lams[sname]["noncontractible"] += 1
                continue
            prod = sp.product(cb)
            nc = [0, 0, 0]
            j, r = 0, cb
            while r:
                if r & 1 and plaq_c[j] >= 0:
                    nc[plaq_c[j]] += 1
                r >>= 1; j += 1
            sg = sign_vs_canonical(prod) * (-1) ** sum(s[c] * nc[c] for c in range(3))
            lam = sign_vs_canonical(O) / sg
            lams[sname][lam.real if lam.imag == 0 else lam] += 1
    return {k: dict(v) for k, v in lams.items()}, dinf(x, Rx), len(null)


def setup(code):
    G = code.generators((0, 0, 0))
    labels = [l for l, _ in G]
    gens = [g for _, g in G]
    plaq_c = [l[2] if l[0] == "P" else -1 for l in labels]
    sp = Span(gens, lat.n)
    hs = code.hop_signs()
    h = tuple(next(iter(hs[c])) for c in range(3))
    s0 = tuple(0 if h[c] == 1 else 1 for c in range(3))
    spi = tuple(1 - q for q in s0)
    return labels, gens, plaq_c, sp, {"flux0": s0, "fluxpi": spi}


XS_FAR = [(2, 0, 0), (0, 2, 0), (0, 0, 2), (2, 1, 0), (1, 0, 2), (2, 0, 1), (0, 1, 2),
          (3, 0, 0), (0, 3, 0), (0, 0, 3), (3, 1, 1), (1, 3, -1), (2, -1, 2), (3, -1, 0)]
XS_NEAR = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def main():
    ROTS = rotations()
    # --- toric control ---
    tc = ToricCode(lat)
    labels, gens, plaq_c, sp, sectors = setup(tc)
    for M in ROTS:
        if order_of(M) != 2 or not all(abs(M[i][i]) == 1 for i in range(3)):
            continue
        for t in itertools.product([0, 1], repeat=3):
            at = axis_type(M, t)
            if at.startswith("screw"):
                continue
            res = Counter()
            for x in XS_FAR + XS_NEAR:
                out = run_case(tc, gens, labels, sp, plaq_c, sectors, M, t, x)
                if out is None:
                    res["nosol"] += 1; continue
                lam, d, nn = out
                if d < 2:
                    continue
                res[str(lam)] += 1
            print("TORIC", M, t, at, dict(res), flush=True)
        break  # one axis C2 suffices for the control
    # --- BKSF codes ---
    reps = [tuple(r) for r in json.load(open("reps_L4.json"))]
    summary = Counter()
    for ci, r in enumerate(reps):
        code = Code(lat, r)
        labels, gens, plaq_c, sp, sectors = setup(code)
        base = [0, lat.nv, lat.nv + 1, lat.nv + 2]
        for M in ROTS:
            if order_of(M) != 2:
                continue
            perm = edge_perm(lat, M)
            if not all(sp.decompose(permute_pauli(gens[i], perm)) is not None for i in base):
                continue
            kind = "axisC2" if all(abs(M[i][i]) == 1 for i in range(3)) else "edgeC2"
            far = Counter(); near = Counter()
            for x in (XS_FAR[:3] if QUICK else XS_FAR) + XS_NEAR:
                if all((matvec(M, x)[i] - x[i]) % L == 0 for i in range(3)):
                    continue
                if dinf(x, matvec(M, x)) >= L // 2:
                    continue
                out = run_case(code, gens, labels, sp, plaq_c, sectors, M, (0, 0, 0), x)
                if out is None:
                    (far if True else near)["nosol"] += 1; continue
                lam, d, nn = out
                tgt = far if d >= 3 else near
                for sname, cnt in lam.items():
                    for k, v in cnt.items():
                        tgt[(sname, d >= 3 and "sep>=3" or f"sep={d}", k)] += v
            for k, v in far.items():
                summary[(kind,) + (k if isinstance(k, tuple) else (k,))] += v
            for k, v in near.items():
                summary[(kind,) + (k if isinstance(k, tuple) else (k,))] += v
            print(ci, r, kind, M, "far:", dict(far), "near:", dict(near), f"({time.time()-t0:.0f}s)", flush=True)
    print("\nSUMMARY (C2 type, sector, separation, lambda): number of sampled solutions")
    for k, v in sorted(summary.items(), key=str):
        print(" ", k, v)


if __name__ == "__main__":
    main()
