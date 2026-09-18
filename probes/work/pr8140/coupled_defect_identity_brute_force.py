#!/usr/bin/env python3
"""J:attack:PR8140 - the clock static-charge notes (PR #8140), attack pattern (f) NORMALIZATION on the exact coupled electric/magnetic
defect representation (FINITE_CLOCK_EXACT_COUPLED_ELECTRIC_MAGNETIC_DEFECT_REPRESENTATION note, identity (1)):

  Z_N(j) = N^-r sum_{theta in (2pi/N)Z_N^r} exp[i<j,theta>] prod_p phi_beta((D theta)_p),  phi_beta(u) = sum_k exp[-beta(u-2pi k)^2/2]
         = C_beta sum_{a in Z^r} sum_{[k] in Z^P/K} exp[-<l,Q^-1 l>/(2 beta)] exp[-2 pi^2 beta ||P_perp k||^2] exp[2 pi i <l, Q^-1 D^T k>],
  l = j + N a,  C_beta = (2 pi beta)^(-r/2) (det Q)^(-1/2),

recomputed by brute force with machinery built here from scratch (cubical complexes of boxes with my own orientation convention, a BFS
spanning tree, exact rational Q^-1 and projectors, integer hypotheses checked by Smith normal forms):
  * the single three-cube: Z_N(0) against the runner's direct values at every (N, beta) it records (convention-independent), and the
    plaquette Wilson loop Z_N(D^T e_p)/Z_N(0) against its recorded ratios and the quantized-current note's 0.78930863427393 (N=2, beta=1/2);
  * two three-cubes sharing a face (r = 9, a two-dimensional magnetic lattice, beyond the note's own finite test): direct clock sums over
    N^9 states (N = 2, 3, 4) against the dual double sum (electric points enumerated inside an ellipsoid, magnetic charges in a box, the
    phase and C_beta kept), for j = 0, a plaquette loop and a non-gauge-trivial character; the omissions the note warns against (the phase,
    the aliases a != 0, the magnetic cosets k != 0) as controls;
  * the single four-cube witness in exact rationals: r = 17, P = 24, (P_e)_pp = 17/24 for all 24 plaquettes, <a,Q^-1 a> = 17/24,
    ||P_perp 3e_p||^2 = 9*7/24 = <m,(d_2 d_2^T)^+ m>, the phase exp(2 pi i 51/8) with real part -1/sqrt2, d_2(3e_p) != 0, d_3 d_2 = 0.
HIT if the identity, a stated value or the witness fails.
"""
import itertools
import json
import math
import re
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/clock-static-charge-20260915"
HEAD = "8a71d7fa8a87a451e5c49df31d18986574d73610"
CACHE_X = "logs/runner-cache/finite_clock_exact_coupled_electric_magnetic_defect_representation_2026_09_15.txt"
CACHE_Q = "logs/runner-cache/quantized_current_poisson_identity_centered_gaussian_domination_and_clock_wilson_cosets_2026_09_15.txt"


def show(path):
    r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "-q", "origin", BRANCH], cwd=ROOT, check=True)
        r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True, check=True)
    return r.stdout


def box_complex(n):
    d = len(n)
    cells = {k: [] for k in range(d + 1)}
    for S in itertools.chain.from_iterable(itertools.combinations(range(d), k) for k in range(d + 1)):
        ranges = [range(n[i]) if i in S else range(n[i] + 1) for i in range(d)]
        for v in itertools.product(*ranges):
            cells[len(S)].append((v, S))
    index = {k: {c: i for i, c in enumerate(cells[k])} for k in cells}
    cob = {}
    for k in range(1, d + 1):
        M = np.zeros((len(cells[k]), len(cells[k - 1])), dtype=np.int64)
        for ci, (v, S) in enumerate(cells[k]):
            for t, s in enumerate(S):
                rest = tuple(x for x in S if x != s)
                up = tuple(v[i] + (1 if i == s else 0) for i in range(d))
                sign = (-1) ** t
                M[ci, index[k - 1][(up, rest)]] += sign
                M[ci, index[k - 1][(v, rest)]] -= sign
        cob[k - 1] = M                   # d_{k-1}: (k-1)-cochains -> k-cochains
    return cells, cob


def tree_gauge(cells, d0):
    V = len(cells[0])
    adj = {i: [] for i in range(V)}
    for e in range(d0.shape[0]):
        a, b = np.nonzero(d0[e])[0]
        adj[a].append((b, e))
        adj[b].append((a, e))
    seen, tree, queue = {0}, set(), [0]
    while queue:
        x = queue.pop(0)
        for y, e in adj[x]:
            if y not in seen:
                seen.add(y)
                tree.add(e)
                queue.append(y)
    return [e for e in range(d0.shape[0]) if e not in tree]


class Setup:
    def __init__(self, n):
        self.cells, self.cob = box_complex(n)
        d0, d1 = self.cob[0], self.cob[1]
        self.d2 = self.cob.get(2)
        self.nt = tree_gauge(self.cells, d0)
        self.D = d1[:, self.nt]
        self.r = len(self.nt)
        self.P = d1.shape[0]
        Ds = sp.Matrix(self.D.tolist())
        self.Qs = Ds.T * Ds
        self.Qinv_s = self.Qs.inv()
        self.Pe_s = Ds * self.Qinv_s * Ds.T
        self.detQ = int(self.Qs.det())
        snf = smith_normal_form(Ds, domain=sp.ZZ)
        inv = [abs(snf[i, i]) for i in range(min(snf.shape))]
        rank_d2 = np.linalg.matrix_rank(self.d2) if self.d2 is not None else 0
        self.hyp = {"dd0": not np.any(d1 @ d0), "dd1": self.d2 is None or not np.any(self.d2 @ d1), "rank_D": np.linalg.matrix_rank(self.D) == self.r,
                    "D_primitive": all(x == 1 for x in inv), "K=ker d2": self.P - rank_d2 == self.r}
        self.Qinv = np.array(self.Qinv_s.tolist(), dtype=float)
        self.Pperp = np.eye(self.P) - np.array(self.Pe_s.tolist(), dtype=float)
        # magnetic representatives: a face of each 3-cell that no other 3-cell contains
        self.reps = []
        if self.d2 is not None:
            for c in range(self.d2.shape[0]):
                for p in np.nonzero(self.d2[c])[0]:
                    if np.count_nonzero(self.d2[:, p]) == 1:
                        self.reps.append((p, int(self.d2[c, p])))
                        break
            if len(self.reps) != self.d2.shape[0]:
                self.reps = None                 # no face private to each 3-cell (the four-cube): the dual sum is not run here

    def direct(self, N, beta, j, K=8):
        t = np.array(list(itertools.product(range(N), repeat=self.r)), dtype=float) * (2 * np.pi / N)
        U = t @ self.D.T
        w = np.ones(len(t))
        ks = np.arange(-K, K + 1) * 2 * np.pi
        for p in range(self.P):
            w *= np.exp(-beta * (U[:, p, None] - ks[None, :]) ** 2 / 2).sum(1)
        return np.mean(np.exp(1j * (t @ np.asarray(j, float))) * w)

    def electric_points(self, N, beta, j, R2):
        G = N * N * self.Qinv / (2 * beta)
        Ut = np.linalg.cholesky(G).T                # G = Ut^T Ut, Ut upper triangular
        c = -np.asarray(j, float) / N
        r = self.r
        out = []
        x = np.zeros(r)

        def rec(i, partial):
            if i < 0:
                out.append(x.copy())
                return
            shift = sum(Ut[i, m] * (x[m] - c[m]) for m in range(i + 1, r))
            rem = R2 - partial
            if rem < 0:
                return
            half = math.sqrt(rem) / Ut[i, i]
            centre = c[i] - shift / Ut[i, i]
            for xi in range(math.ceil(centre - half), math.floor(centre + half) + 1):
                x[i] = xi
                val = Ut[i, i] * (xi - c[i]) + shift
                rec(i - 1, partial + val * val)
            x[i] = 0

        rec(r - 1, 0.0)
        return np.array(out)

    def dual(self, N, beta, j, R2=36.0, M=8, keep_phase=True, aliases=True, cosets=True):
        A = self.electric_points(N, beta, j, R2) if aliases else np.zeros((1, self.r))
        L = np.asarray(j, float)[None, :] + N * A
        el = np.exp(-np.einsum("ai,ij,aj->a", L, self.Qinv, L) / (2 * beta))
        ms = list(itertools.product(range(-M, M + 1), repeat=len(self.reps))) if (cosets and self.reps) else [tuple(0 for _ in self.reps)]
        Kmat = np.zeros((len(ms), self.P))
        for i, m in enumerate(ms):
            for (p, s), mc in zip(self.reps, m):
                Kmat[i, p] += s * mc
        Em = np.einsum("mi,ij,mj->m", Kmat, self.Pperp, Kmat)
        wm = np.exp(-2 * np.pi ** 2 * beta * Em)
        W = Kmat @ self.D @ self.Qinv                 # rows: (Q^-1 D^T k)^T
        tot = 0j
        for s in range(0, len(L), 4000):
            ph = np.exp(2j * np.pi * (L[s:s + 4000] @ W.T)) if keep_phase else np.ones((len(L[s:s + 4000]), len(ms)))
            tot += el[s:s + 4000] @ (ph @ wm)
        C = (2 * np.pi * beta) ** (-self.r / 2) / math.sqrt(self.detQ)
        return C * tot, len(L), len(ms)


def main():
    t0 = time.time()
    hits = []
    cx = show(CACHE_X)
    cq = show(CACHE_Q)
    body = cx.split("----- stdout -----", 1)[1]
    rec = json.JSONDecoder().raw_decode(body[body.index("{"):])[0]
    cases = rec["three_cube"]["cases"]
    wq = float(re.search(r'"wilson_direct": ([0-9.]+)', cq).group(1))
    # ---- the three-cube
    c3 = Setup((1, 1, 1))
    print(f"[three-cube] V, E, P, C3 = {len(c3.cells[0])}, {len(c3.cells[1])}, {c3.P}, {len(c3.cells[3])}; r = {c3.r}; det Q = {c3.detQ}; "
          f"hypotheses {c3.hyp}")
    p0 = 0
    jW = c3.D[p0].tolist()
    rows = []
    worst3 = 0.0
    for case in cases:
        N, beta, j = case["N"], case["beta"], case["j"]
        if any(j):
            continue
        z = c3.direct(N, beta, [0] * c3.r).real
        zd = c3.dual(N, beta, [0] * c3.r)[0].real
        zW = c3.direct(N, beta, jW).real
        mate = next((c for c in cases if c["N"] == N and c["beta"] == beta and any(c["j"])), None)
        ratio_rec = mate["direct"] / case["direct"] if mate else float("nan")
        worst3 = max(worst3, abs(z - case["direct"]) / case["direct"], abs(zd - z) / z)
        rows.append(f"N={N} beta={beta}: Z(0) mine {z:.15g} (runner {case['direct']:.15g}, dual {zd:.15g}); plaquette Wilson {zW / z:.12f} "
                    f"(runner's j={mate['j'] if mate else '-'} ratio {ratio_rec:.12f})")
    zq = c3.direct(2, 0.5, jW).real / c3.direct(2, 0.5, [0] * c3.r).real
    print("[three-cube values] " + " | ".join(rows) + f"; plaquette Wilson loop at N=2, beta=1/2: {zq:.14f} (quantized-current note {wq:.14f}); "
          f"largest relative deviation {worst3:.1e}  ({time.time() - t0:.0f}s)")
    if worst3 > 1e-10 or abs(zq - wq) > 1e-11:
        hits.append(f"three-cube values: relative deviation {worst3:.2e}; Wilson {zq} vs {wq}")
    # ---- two cubes sharing a face
    c6 = Setup((2, 1, 1))
    print(f"[two cubes] V, E, P, C3 = {len(c6.cells[0])}, {len(c6.cells[1])}, {c6.P}, {len(c6.cells[3])}; r = {c6.r}; det Q = {c6.detQ}; "
          f"hypotheses {c6.hyp}; magnetic lattice Z^{len(c6.reps)}")
    if not all(c6.hyp.values()) or not all(c3.hyp.values()):
        hits.append(f"integer hypotheses fail on a box: {c3.hyp} {c6.hyp}")
    shared = [p for p in range(c6.P) if np.count_nonzero(c6.d2[:, p]) == 2][0]
    j_loop = c6.D[shared].tolist()
    j_char = [1] + [0] * (c6.r - 1)
    lines, worst6 = [], 0.0
    for N, beta in ((2, 0.25), (3, 0.5), (4, 0.7), (3, 0.25)):
        for name, j in (("0", [0] * c6.r), ("shared-face loop", j_loop), ("e_1", j_char)):
            zd_, na, nm = c6.dual(N, beta, j)
            zdir = c6.direct(N, beta, j)
            err = abs(zd_ - zdir) / abs(zdir)
            worst6 = max(worst6, err)
            ctrl = ""
            if name == "shared-face loop":
                nophase = c6.dual(N, beta, j, keep_phase=False)[0]
                u1 = c6.dual(N, beta, j, aliases=False)[0]
                zero = c6.dual(N, beta, j, cosets=False)[0]
                ctrl = (f"; without the phase {abs(nophase - zdir) / abs(zdir):.1e}, without aliases {abs(u1 - zdir) / abs(zdir):.1e}, "
                        f"zero coset only {abs(zero - zdir) / abs(zdir):.1e} (relative changes)")
            lines.append(f"N={N} beta={beta} j={name}: direct {zdir.real:.13g}{zdir.imag:+.1e}i, dual {zd_.real:.13g}{zd_.imag:+.1e}i "
                         f"({na} electric x {nm} magnetic terms), relative difference {err:.1e}{ctrl}")
    print("[two cubes identity] " + " | ".join(lines) + f"  ({time.time() - t0:.0f}s)")
    if worst6 > 1e-9:
        hits.append(f"identity (1) fails on two cubes: largest relative difference {worst6:.2e}")
    # ---- the four-cube witness, exactly
    c4 = Setup((1, 1, 1, 1))
    diag = [c4.Pe_s[p, p] for p in range(c4.P)]
    p = 0
    Ds = sp.Matrix(c4.D.tolist())
    a = Ds.T * sp.eye(c4.P)[:, p]
    aQa = (a.T * c4.Qinv_s * a)[0]
    k = 3 * sp.eye(c4.P)[:, p]
    Pperp_s = sp.eye(c4.P) - c4.Pe_s
    kk = (k.T * Pperp_s * k)[0]
    d2s = sp.Matrix(c4.d2.tolist())
    m = d2s * k
    mm = (m.T * (d2s * d2s.T).pinv() * m)[0]
    phase_exp = (3 * a).T * c4.Qinv_s * Ds.T * k
    ph = sp.Rational(phase_exp[0]) % 1
    d3d2 = not np.any(c4.cob[3] @ c4.d2)
    print(f"[four-cube] V, E, P, C3, C4 = {len(c4.cells[0])}, {len(c4.cells[1])}, {c4.P}, {len(c4.cells[3])}, {len(c4.cells[4])}; r = {c4.r}; hypotheses "
          f"{c4.hyp}; distinct (P_e)_pp: {sorted(set(diag))}; <a,Q^-1 a> = {aQa}; ||P_perp 3e_p||^2 = {kk} = <m,(d2 d2^T)^+ m> = {mm}; phase exponent "
          f"9 (P_e)_pp = {phase_exp[0]} (fractional part {ph}), real part {sp.nsimplify(sp.cos(2 * sp.pi * ph))}; d_2(3e_p) nonzero: {any(m)}; "
          f"d_3 d_2 = 0: {d3d2}  ({time.time() - t0:.0f}s)")
    ok4 = (c4.r == 17 and c4.P == 24 and set(diag) == {sp.Rational(17, 24)} and aQa == sp.Rational(17, 24) and kk == sp.Rational(63, 24)
           and mm == kk and sp.nsimplify(sp.cos(2 * sp.pi * ph)) == -sp.sqrt(2) / 2 and any(m) and d3d2 and all(c4.hyp.values()))
    if not ok4:
        hits.append("the four-cube witness does not reproduce as stated")
    for h in hits:
        print("HIT: " + h)
    print(f"SUMMARY: attack pattern (f) NORMALIZATION - identity (1) with its phase and C_beta = (2 pi beta)^(-r/2) (det Q)^(-1/2) recomputed "
          f"from complexes built here: the three-cube's recorded Z_N(0) at {sum(1 for c in cases if not any(c['j']))} (N, beta) points and "
          f"the quantized-current note's Wilson value reproduced (largest relative deviation {worst3:.0e}); on two cubes sharing a face "
          f"(r = 9, two magnetic charges) direct clock sums over N^9 states equal the dual double sum at N = 2, 3, 4 for three characters "
          f"(largest relative difference {worst6:.0e}), and dropping the phase, the aliases or the cosets changes them; the four-cube witness "
          f"(17/24, 63/24, exp(2 pi i 51/8)) reproduces exactly; {len(hits)} failures; attack {'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
