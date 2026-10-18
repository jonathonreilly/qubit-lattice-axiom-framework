"""B16 check, item 1: timing classification of {H_EM(N),H_EM(M)} (own code).

C1a  incidence formula == brute-force dense bracket (random non-uniform timing, L=3, float).
C1b  exact symbolic classification over translation-invariant corner-supported timings
     (per axis (u_t,u_h), per plane 4 corner weights, each normalised to 1), on L=4, built from the
     computed bracket (not hand-derived equations); exact and mod Gauss (E restricted to ker div).
C1c  the 8 solutions; none reflection-symmetric; (mean, four) fails, also mod Gauss.
C1d  STAGGERED (bipartite) timing, outside the B16 class: links timed at their EVEN endpoint, plaquettes
     at the mean of their two ODD corners.  Is the bracket bond-supported?  Point-reflection symmetry about
     an even site?
"""
import sys
from fractions import Fraction as Fr
from itertools import product
import random

import numpy as np
import sympy as sp

from chk_lat import Lat, em_pair_coeffs, uniform_timing, em_quadform, bf_bracket

RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


# ---------------------------------------------------------------- C1a
def c1a():
    lat = Lat(3)
    rng = random.Random(7)
    u = [{x: Fr(rng.randint(-2, 2)), lat.sh(x, j): Fr(rng.randint(-2, 2))} for (x, j) in lat.links]
    w = []
    for p in range(len(lat.plaqs)):
        cs = lat.corners(p)
        w.append({cs[n]: Fr(rng.randint(-2, 2)) for n in cs})
    c, g2 = 1.5, 0.7
    coeffs = em_pair_coeffs(lat, u, w, Fr(3, 2))
    N = np.array([rng.randint(-3, 3) for _ in lat.sites], float)
    Mv = np.array([rng.randint(-3, 3) for _ in lat.sites], float)

    def smear(lapse):
        nl = [sum(float(v) * lapse[lat.sidx[s]] for s, v in u[k].items()) for k in range(len(lat.links))]
        mp = [sum(float(v) * lapse[lat.sidx[s]] for s, v in w[p].items()) for p in range(len(lat.plaqs))]
        return nl, mp
    MN = em_quadform(lat, *smear(N), g2, c)
    MM = em_quadform(lat, *smear(Mv), g2, c)
    B = bf_bracket(MN, MM)  # {H(N),H(M)} = 1/2 z^T B z
    nL = len(lat.links)
    # formula: coefficient of E_k A_a  -> B[nL+k, a] + B[a, nL+k] over 2 = B[nL+k, a]
    Bf = np.zeros((nL, nL))
    for (s, t), d in coeffs.items():
        f = N[lat.sidx[s]] * Mv[lat.sidx[t]]
        for (k, a), v in d.items():
            Bf[k, a] += f * float(v)
    err = np.abs(B[nL:, :nL] - Bf).max()
    other = max(np.abs(B[:nL, :nL]).max(), np.abs(B[nL:, nL:]).max())
    # g-independence: change g2
    B2 = bf_bracket(em_quadform(lat, *smear(N), 3.1, c), em_quadform(lat, *smear(Mv), 3.1, c))
    check("C1a", err < 1e-10 and other < 1e-12 and np.abs(B2 - B).max() < 1e-10,
          f"incidence formula reproduces the brute-force dense bracket (random non-uniform corner timing, L=3): max err {err:.1e}; "
          f"bracket is pure E.A (EE, AA blocks {other:.1e}); g-independent ({np.abs(B2 - B).max():.1e})")


# ---------------------------------------------------------------- C1b/C1c
def classify(L=4):
    lat = Lat(L)
    ut = {j: sp.Symbol(f"u{j}t") for j in range(3)}
    uh = {j: sp.Symbol(f"u{j}h") for j in range(3)}
    wn = {ij: {n: sp.Symbol(f"w{ij[0]}{ij[1]}_{n}") for n in ("00", "10", "01", "11")} for ij in lat.pairs}
    usyms = [ut[j] for j in range(3)] + [uh[j] for j in range(3)]
    wsyms = [wn[ij][n] for ij in lat.pairs for n in ("00", "10", "01", "11")]
    # bracket is bilinear in (u, w): compute coefficient for each basis pair (a, b) numerically-exactly
    origin = (0, 0, 0)
    P = lat.transverse_projector()
    rows_exact, rows_gauss = {}, {}
    for ai, us in enumerate(usyms):
        for bi, ws in enumerate(wsyms):
            lw = {j: (Fr(int(us == ut[j])), Fr(int(us == uh[j]))) for j in range(3)}
            pw = {ij: {n: Fr(int(ws == wn[ij][n])) for n in wn[ij]} for ij in lat.pairs}
            u, w = uniform_timing(lat, lw, pw)
            co = em_pair_coeffs(lat, u, w)
            for (s, t), d in co.items():
                if s != origin or lat.is_bond(s, t) or s == t:
                    continue
                for key, v in d.items():
                    rows_exact.setdefault((t, key), {})[(ai, bi)] = v
                # mod Gauss: project the E-index onto ker(div)
                Y = np.zeros((len(lat.links), len(lat.links)))
                for (k, a), v in d.items():
                    Y[k, a] += float(v)
                PY = P @ Y
                for (k, a) in zip(*np.nonzero(np.abs(PY) > 1e-12)):
                    rows_gauss.setdefault((t, k, a), {})[(ai, bi)] = PY[k, a]
    mons = [(ai, bi) for ai in range(len(usyms)) for bi in range(len(wsyms))]
    mon_expr = [usyms[a] * wsyms[b] for (a, b) in mons]

    def reduce_rows(rows, exact):
        if exact:
            Mx = sp.Matrix([[r.get(m, 0) for m in mons] for r in rows.values()])
            R = Mx.rref()[0]
            eqs = [sum(R[i, j] * mon_expr[j] for j in range(len(mons))) for i in range(R.rows) if any(R[i, j] != 0 for j in range(len(mons)))]
        else:
            Mx = np.array([[r.get(m, 0.0) for m in mons] for r in rows.values()])
            # row space via SVD, then rationalise the rref (entries are small rationals)
            U, S, Vt = np.linalg.svd(Mx, full_matrices=False)
            rk = int((S > 1e-8 * S[0]).sum())
            R = sp.Matrix(Vt[:rk]).applyfunc(lambda z: sp.nsimplify(round(z, 12), rational=True, tolerance=1e-9))
            R = R.rref()[0]
            eqs = [sum(sp.nsimplify(R[i, j], rational=True, tolerance=1e-9) * mon_expr[j] for j in range(len(mons))) for i in range(R.rows)]
        return eqs
    eq_exact = reduce_rows(rows_exact, True)
    eq_gauss = reduce_rows(rows_gauss, False)
    norm = [ut[j] + uh[j] - 1 for j in range(3)] + [sum(wn[ij].values()) - 1 for ij in lat.pairs]
    sol_e = sp.solve(eq_exact + norm, usyms + wsyms, dict=True)
    sol_g = sp.solve(eq_gauss + norm, usyms + wsyms, dict=True)
    return lat, usyms, wsyms, ut, uh, wn, eq_exact, eq_gauss, sol_e, sol_g


def c1bc():
    lat, usyms, wsyms, ut, uh, wn, eq_e, eq_g, sol_e, sol_g = classify(4)
    print(f"  #independent bilinear conditions: exact {len(eq_e)}, mod Gauss {len(eq_g)}")
    full_e = [s for s in sol_e if len(s) == len(usyms) + len(wsyms)]
    full_g = [s for s in sol_g if len(s) == len(usyms) + len(wsyms)]
    print("  exact solutions:")
    for s in sol_e:
        print("   ", {str(k): v for k, v in s.items()})

    def canon(sols):
        return sorted(tuple(sorted((str(k), str(v)) for k, v in s.items())) for s in sols)
    same = canon(sol_e) == canon(sol_g)
    # each solution: every axis at one endpoint, each plane one corner = meeting point
    good = True
    for s in full_e:
        for j in range(3):
            good &= {s[ut[j]], s[uh[j]]} == {0, 1}
        for (i, j) in lat.pairs:
            ci = "0" if s[ut[i]] == 1 else "1"
            cj = "0" if s[ut[j]] == 1 else "1"
            for n in ("00", "10", "01", "11"):
                good &= s[wn[(i, j)][n]] == (1 if n == ci + cj else 0)
    check("C1b", len(sol_e) == 8 and len(full_e) == 8 and good,
          "exact classification over translation-invariant corner-supported timings (L=4, conditions generated from the computed bracket): "
          "exactly 8 solutions, each axis timed at one endpoint and each plaquette at the corner where its axes' chosen endpoints meet")
    check("C1c", same and len(full_g) == 8,
          "mod Gauss (E restricted to ker div, i.e. Gauss terms with arbitrary A-dependent multipliers) gives the SAME 8 solutions; none has u_t = u_h, so no reflection-symmetric timing in this class")
    return lat


def bondsupport(lat, u, w, gauss=False, P=None):
    co = em_pair_coeffs(lat, u, w)
    bad = 0
    for (s, t), d in co.items():
        if s == t or lat.is_bond(s, t):
            continue
        if not gauss:
            bad += 1
            continue
        Y = np.zeros((len(lat.links), len(lat.links)))
        for (k, a), v in d.items():
            Y[k, a] += float(v)
        if np.abs(P @ Y).max() > 1e-10:
            bad += 1
    return bad, co


def staggered(lat, par=0):
    """links timed at the endpoint of parity `par`; plaquettes at the mean of the two corners of opposite parity."""
    def parity(x):
        return sum(x) % 2
    u = []
    for (x, j) in lat.links:
        y = lat.sh(x, j)
        u.append({x: Fr(1)} if parity(x) == par else {y: Fr(1)})
    w = []
    for p in range(len(lat.plaqs)):
        cs = lat.corners(p)
        w.append({s: Fr(1, 2) for s in cs.values() if parity(s) != par})
    return u, w


def c1d():
    lat = Lat(4)
    P = lat.transverse_projector()
    # symmetric reference
    u, w = uniform_timing(lat, {j: (Fr(1, 2), Fr(1, 2)) for j in range(3)}, {ij: {n: Fr(1, 4) for n in ("00", "10", "01", "11")} for ij in lat.pairs})
    nb_sym, _ = bondsupport(lat, u, w)
    nb_sym_g, _ = bondsupport(lat, u, w, True, P)
    print(f"  (mean, four): non-bond antisymmetric lapse pairs (ordered): exact {nb_sym}, mod Gauss {nb_sym_g}")
    check("C1c'", nb_sym > 0 and nb_sym_g == nb_sym, f"reflection-symmetric (mean, four) timing: {nb_sym // 2} unordered non-bond lapse pairs, none removed mod Gauss")
    u, w = staggered(lat, 0)
    nb, co = bondsupport(lat, u, w)
    # point reflection about the even site 0: x -> -x maps link (x,j) to link (-x-e_j, j), plaquette similarly
    def refl(x):
        return tuple((-x[k]) % lat.L for k in range(3))
    sym_ok = True
    for k, (x, j) in enumerate(lat.links):
        x2 = lat.sh(refl(x), j, -1)
        k2 = lat.lidx[(x2, j)]
        sym_ok &= {refl(s): v for s, v in u[k].items()} == u[k2]
    for p, (y, (i, j)) in enumerate(lat.plaqs):
        y2 = lat.sh(lat.sh(refl(y), i, -1), j, -1)
        p2 = lat.pidx[(y2, (i, j))]
        sym_ok &= {refl(s): v for s, v in w[p].items()} == w[p2]
    # also each axis reflection about an even site
    for ax in range(3):
        def ra(x, ax=ax):
            return tuple((-x[k]) % lat.L if k == ax else x[k] for k in range(3))
        for k, (x, j) in enumerate(lat.links):
            x2 = lat.sh(ra(x), j, -1) if j == ax else ra(x)
            sym_ok &= {ra(s): v for s, v in u[k].items()} == u[lat.lidx[(x2, j)]]
        for p, (y, (i, j)) in enumerate(lat.plaqs):
            y2 = ra(y)
            if ax in (i, j):
                y2 = lat.sh(y2, ax, -1)
            sym_ok &= {ra(s): v for s, v in w[p].items()} == w[lat.pidx[(y2, (i, j))]]
    check("C1d", nb == 0 and sym_ok,
          f"STAGGERED timing (links at their even endpoint, plaquettes at the mean of their two odd corners; L=4): "
          f"{{H_EM(N),H_EM(M)}} is EXACTLY bond-supported (non-bond pairs: {nb}), and the timing is invariant under every axis reflection "
          f"and the point reflection about an even site (symmetry check {sym_ok}); it breaks unit translations to the even sublattice")
    return lat, u, w, co


if __name__ == "__main__":
    c1a()
    c1bc()
    c1d()
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
