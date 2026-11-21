#!/usr/bin/env python3
"""Lemma 4.5h of parts/hard-core--independent.md: is the lift's plaquette small against
the coarse curvature, near a corner of the region, and with what power of L?

In (4.3) the coefficient of the rough cost is phi_* := sup |f_p(V^*)|, with V^* the lift
on a union of whole blocks. Lemma 4.5h says phi_* <= C L^{-sigma} sup |F'|, with sigma > 0
absolute. Expected from the re-entrant edge r^{-1/3}: L^{-5/3}; in the interior, L^{-2}.

Model. Abelian, one step from the Wilson form, periodic 4-torus of side 2 L, patterns of
removed blocks as in checks/hard-core--independent_coer_g.py. For coarse data B' on chart
bonds, a^* minimises ||d a||^2 on R subject to Q_str a = B'. This is solved on X by
conjugate gradients with the form d^T d + D Pi_0 D^T, which does not change d a^*.
With f_p(e_c) the plaquette values for a unit bond, for the plaquettes p with the five
largest sums over c of |f_p(e_c)|, phi(L) is the maximum of f_p(B') over B', by a linear
program, subject to |d_c B'| <= 1 on coarse plaquettes with four chart bonds.

Pre-registered criteria, written before the first run.
    s(pattern) := log( phi(3) / phi(7) ) / log(7 / 3).
    PASS-SIGMA: s >= 1 for every pattern.
    WEAK-SIGMA: 0.3 <= s < 1 for some pattern, with no pattern below 0.3: sigma > 0
    survives, but well below the expected value, and I want to know why.
    FAIL-SIGMA: s < 0.3 for some pattern. Then the loss in (4.3) is not beaten by a
    power of L, and M^4 L^{-sigma} <= c_F / C is in doubt: the text has to change.

Result of the first run: WEAK-SIGMA, s = 0.948 (one), 0.940 (diag4), 1.018 (diag2), others
1.34 to 1.47. But phi L^2 for pattern one was 9.17, 13.86, 22.35, equal to the full torus at
L = 3, 5 and then a jump, which suggests that the choice of the five largest l^1 scores
missed the corner plaquettes at small L, so that phi(3), phi(5) were underestimates.

Follow-up criteria, written before that run. HC_TOP = 400 plaquettes go to the linear
program. Patterns full, one, diag2, diag4, L = 3, 5, 7, 9.
    s2(pattern) := log( phi(5) / phi(9) ) / log(9 / 5), the location of the worst plaquette
    printed as its sup-distance to the removed blocks.
    PASS2-SIGMA: s2 >= 1.2 for all four patterns.
    WEAK2-SIGMA: 0.6 <= s2 < 1.2 for some pattern.
    FAIL2-SIGMA: s2 < 0.6 for some pattern: the corner is worse than r^{-1/3} predicts, by
    more than pre-asymptotics can explain, and Lemma 4.5h must be read again.

Result of the follow-up: WEAK2-SIGMA, s2 = 1.64, 1.18, 0.81, 1.18 (full, one, diag2, diag4), and
the last step of diag2, phi(7) = 0.428 to phi(9) = 0.393, is slow.

Third criteria, written before that run: pattern diag2 only, HC_TOP = 4000, L = 7, 9, 11.
    s3 := log( phi(9) / phi(11) ) / log(11 / 9), s3' := log( phi(7) / phi(9) ) / log(9 / 7).
    If phi(7) moves up with the wider scan, the slow step was a sampling artefact.
    PASS3: s3 >= 0.6. FAIL3: s3 < 0.2, which would suggest that phi does not decay at this
    pattern, against Lemma 4.5h, and it would have to be looked at before anything else.
    Neither: report the numbers.

Run under the numeric lock, BLAS threads 1, nice, RSS checked against 2 GB.
"""
import importlib.util
import itertools
import os
import pathlib
import sys

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import numpy as np
import scipy.sparse.linalg as sl
from scipy.optimize import linprog

spec = importlib.util.spec_from_file_location("coer_g", pathlib.Path(__file__).with_name("hard-core--independent_coer_g.py"))
cg_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cg_mod)

DIM = 4
N_BLOCKS = 2


def chart_bonds(removed):
    n = N_BLOCKS
    bpow = np.array([n**i for i in range(DIM)])
    kept = np.ones(n**DIM, dtype=bool)
    for b in removed:
        kept[np.array(b) @ bpow] = False
    index = {}
    for b in itertools.product(range(n), repeat=DIM):
        arr = np.array(b)
        if not kept[arr @ bpow]:
            continue
        for mu in range(DIM):
            b2 = arr.copy()
            b2[mu] = (b2[mu] + 1) % n
            if kept[b2 @ bpow]:
                index[(b, mu)] = len(index)
    return index


def coarse_d(index):
    """Rows of d_c on coarse plaquettes with four chart bonds."""
    n = N_BLOCKS
    rows = []
    for b in itertools.product(range(n), repeat=DIM):
        arr = np.array(b)
        for mu, nu in itertools.combinations(range(DIM), 2):
            bm = arr.copy()
            bm[mu] = (bm[mu] + 1) % n
            bn = arr.copy()
            bn[nu] = (bn[nu] + 1) % n
            keys = [(b, mu), (tuple(bm), nu), (tuple(bn), mu), (b, nu)]
            if all(k in index for k in keys):
                r = np.zeros(len(index))
                for k, sign in zip(keys, (1.0, 1.0, -1.0, -1.0)):
                    r[index[k]] += sign
                rows.append(r)
    return np.array(rows) if rows else np.zeros((0, len(index)))


def plaquette_sites(L, removed):
    """Base site, mu, nu of each plaquette, in the order of cg_mod.build."""
    n = N_BLOCKS
    N = n * L
    nsites = N**DIM
    powers = np.array([N**i for i in range(DIM)])
    coords = np.array(np.unravel_index(np.arange(nsites), (N,) * DIM, order="F")).T
    blocks = coords // L
    bpowers = np.array([n**i for i in range(DIM)])
    kept = np.ones(n**DIM, dtype=bool)
    for b in removed:
        kept[np.array(b) @ bpowers] = False
    site_ok = kept[blocks @ bpowers]

    def site_index(c):
        return (c % N) @ powers

    link_ok = []
    for mu in range(DIM):
        e = np.zeros(DIM, dtype=int)
        e[mu] = 1
        link_ok.append(site_ok & site_ok[site_index(coords + e)])
    out = []
    for mu, nu in itertools.combinations(range(DIM), 2):
        emu = np.zeros(DIM, dtype=int)
        emu[mu] = 1
        enu = np.zeros(DIM, dtype=int)
        enu[nu] = 1
        good = link_ok[mu] & link_ok[nu][site_index(coords + emu)] & link_ok[mu][site_index(coords + enu)] & link_ok[nu]
        idx = np.where(good)[0]
        out.append((coords[idx], mu, nu))
    return out


def dist_to_removed(x, L, removed):
    n = N_BLOCKS
    N = n * L
    best = 10**9
    for b in removed:
        d = 0
        for i in range(DIM):
            lo, hi = b[i] * L, b[i] * L + L - 1
            di = min(abs((x[i] - lo + N // 2) % N - N // 2), abs((x[i] - hi + N // 2) % N - N // 2))
            if lo <= x[i] <= hi:
                di = 0
            d = max(d, di)
        best = min(best, d)
    return best


def run_pattern(L, removed, name):
    Dd, Ds, Q, cross, nl, block_id, site_ok, nsites = cg_mod.build(L, N_BLOCKS, removed)
    pi0, nb, counts = cg_mod.block_proj(block_id, site_ok, nsites)
    index = chart_bonds(removed)
    nbonds = Q.shape[0]
    if nbonds != len(index):
        raise RuntimeError("bond count mismatch")
    if nbonds == 0:
        print(f"L={L} {name}: no chart bonds, nothing to lift", flush=True)
        return None
    QQinv = np.linalg.pinv((Q @ Q.T).toarray())
    Qt = Q.T.tocsr()

    def proj(v):
        return v - Qt @ (QQinv @ (Q @ v))

    def h0(v):
        return Dd.T @ (Dd @ v) + Ds.T @ pi0(Ds @ v)

    op = sl.LinearOperator((nl, nl), matvec=lambda v: proj(h0(proj(v))), dtype=float)
    fvals = np.zeros((Dd.shape[0], nbonds))
    for j in range(nbonds):
        e = np.zeros(nbonds)
        e[j] = 1.0
        a_p = Qt @ (QQinv @ e)
        rhs = -proj(h0(a_p))
        x, info = sl.cg(op, rhs, rtol=1e-9, maxiter=4000)
        if info != 0:
            print(f"cg info {info} at bond {j}", flush=True)
        fvals[:, j] = Dd @ (a_p + proj(x))
    cg_mod.check_rss()
    D = coarse_d(index)
    if D.shape[0] == 0:
        print(f"L={L} {name}: no coarse plaquette with four chart bonds", flush=True)
        return None
    # components of f_p that vanish on flat B' are harmless: the LP is bounded by the box
    score = np.abs(fvals).sum(axis=1)
    ntop = int(os.environ.get("HC_TOP", "5"))
    top = np.argsort(score)[-ntop:]
    best = 0.0
    best_p = -1
    for p in top:
        c = -fvals[p]
        res = linprog(c, A_ub=np.vstack([D, -D]), b_ub=np.ones(2 * D.shape[0]), bounds=[(-50, 50)] * nbonds, method="highs")
        if res.status != 0:
            print("lp status", res.status, flush=True)
            continue
        if -res.fun > best:
            best = -res.fun
            best_p = int(p)
    where = ""
    if removed and best_p >= 0:
        k = best_p
        for xs, mu, nu in plaquette_sites(L, removed):
            if k < len(xs):
                where = f" worst at x={tuple(int(v) for v in xs[k])} plane=({mu},{nu}) dist={dist_to_removed(xs[k], L, removed)}"
                break
            k -= len(xs)
    print(f"L={L} {name:8s} phi={best:.5f} phi*L^2={best*L**2:.3f} phi*L^(5/3)={best*L**(5/3):.3f} bonds={nbonds} coarse_plaq={D.shape[0]}{where}", flush=True)
    return best


def main():
    pats = cg_mod.patterns(N_BLOCKS)
    names = os.environ.get("HC_NAMES", "full,one,edge2,diag2,diag4,twoslab,neck,slab").split(",")
    Ls = [int(a) for a in sys.argv[1:]] or [3, 5, 7]
    res = {}
    for name in names:
        res[name] = {}
        for L in Ls:
            res[name][L] = run_pattern(L, pats[name], name)
    verdict = "PASS-SIGMA"
    for name in names:
        r = res[name]
        if 3 in r and 7 in r and r[3] and r[7]:
            s = np.log(r[3] / r[7]) / np.log(7 / 3)
            print(f"{name:8s} s = {s:.3f}")
            if s < 0.3:
                verdict = "FAIL-SIGMA"
            elif s < 1 and verdict == "PASS-SIGMA":
                verdict = "WEAK-SIGMA"
    print(verdict)
    if os.environ.get("HC_THIRD"):
        r = res["diag2"]
        s3 = np.log(r[9] / r[11]) / np.log(11 / 9)
        s3p = np.log(r[7] / r[9]) / np.log(9 / 7)
        print(f"s3 = {s3:.3f}, s3' = {s3p:.3f}")
        print("PASS3" if s3 >= 0.6 else ("FAIL3" if s3 < 0.2 else "NEITHER3"))
    elif os.environ.get("HC_TOP"):
        v2 = "PASS2-SIGMA"
        for name in names:
            r = res[name]
            if 5 in r and 9 in r and r[5] and r[9]:
                s2 = np.log(r[5] / r[9]) / np.log(9 / 5)
                print(f"{name:8s} s2 = {s2:.3f}")
                if s2 < 0.6:
                    v2 = "FAIL2-SIGMA"
                elif s2 < 1.2 and v2 == "PASS2-SIGMA":
                    v2 = "WEAK2-SIGMA"
        print(v2)


if __name__ == "__main__":
    main()
