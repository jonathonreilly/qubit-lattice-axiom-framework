#!/usr/bin/env python3
"""The sup-l^1 norm of the linear lift, for Lemma 4.5j (TREE) of parts/hard-core--independent.md.

(TREE) closes with a stable radius only if the linear lift contracts amplitudes:
    P_L := max over level-k links l of sum over coarse bonds c of |a^(c)_l| < 1/4,
where a^(c) is the solution on X-shifted data, Q_str a^(c) = e_c, stationary for d^T d + D Pi_0 D^T, the gauge
term of (CUT) item 1. In the interior one expects P_L of order 1 / L. Near a corner the potential of the lift is more
singular, and nothing has bounded it there except by a sketch.

Model: abelian, one step, torus of side 2 L, patterns of removed blocks.

Pre-registered criteria, written before the first run.
    For each of full, one, diag2, and the snake mask 395 of checks/hard-core--independent_lift_scan.py, at L = 3, 5, 7, 9.
    PASS-PL: P_L decreases with L at each pattern, and P_L(9) <= 0.7 P_L(5).
    FAIL-PL: P_L(9) >= 0.9 P_L(5) at some pattern. Then the radius in (TREE) shrinks per level, and the proof of
    Lemma 4.5j does not close as written, at that pattern.
    Neither: report. The threshold 1/4 is reported as the L at which it would be reached by extrapolation only.

Result of the first run, under a confirmed lock: NEITHER-PL. P_L(9) / P_L(5) = 0.69 (full), 0.78 (one), 0.80 (diag2),
0.81 (snake). P_L = 0.94 to 1.11 at L = 9, P_L * L = 8.5 to 10.0 and still rising, worst link a crossing link.

Note added after the run: the threshold 1/4 and the reading of FAIL above were mine, before the proof of Lemma 4.5k was
written. That proof asks only for an amplitude bound theta <= 1/2, and for a gauge adapted bond by bond (Lemma 4.5j),
since only a gauge invariant functional is composed with the lift. This script computes the Feynman gauge of (CUT) item 1,
so it does not test Lemma 4.5j. It is kept as a record of the size of the unadapted amplitude.

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

HERE = pathlib.Path(__file__)
spec = importlib.util.spec_from_file_location("coer_g", HERE.with_name("hard-core--independent_coer_g.py"))
cg_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cg_mod)

DIM = 4
BLOCKS = list(itertools.product(range(2), repeat=DIM))


def p_l(L, removed):
    Dd, Ds, Q, cross, nl, block_id, site_ok, nsites = cg_mod.build(L, 2, removed)
    pi0, nb, counts = cg_mod.block_proj(block_id, site_ok, nsites)
    nbonds = Q.shape[0]
    if nbonds == 0:
        return None
    QQinv = np.linalg.pinv((Q @ Q.T).toarray())
    Qt = Q.T.tocsr()

    def proj(v):
        return v - Qt @ (QQinv @ (Q @ v))

    def h0(v):
        return Dd.T @ (Dd @ v) + Ds.T @ pi0(Ds @ v)

    op = sl.LinearOperator((nl, nl), matvec=lambda v: proj(h0(proj(v))), dtype=float)
    total = np.zeros(nl)
    for j in range(nbonds):
        e = np.zeros(nbonds)
        e[j] = 1.0
        a_p = Qt @ (QQinv @ e)
        rhs = -proj(h0(a_p))
        x, info = sl.cg(op, rhs, rtol=1e-8, maxiter=4000)
        if info != 0:
            print(f"cg info {info}", flush=True)
        total += np.abs(a_p + proj(x))
    cg_mod.check_rss()
    return float(total.max()), float(cross[np.argmax(total)])


def main():
    pats = cg_mod.patterns(2)
    named = {k: pats[k] for k in ("full", "one", "diag2")}
    mask = 395
    named["snake"] = [BLOCKS[i] for i in range(16) if mask >> i & 1]
    Ls = [int(a) for a in sys.argv[1:]] or [3, 5, 7, 9]
    res = {}
    for name, removed in named.items():
        res[name] = {}
        for L in Ls:
            val = p_l(L, removed)
            res[name][L] = val[0]
            print(f"{name:6s} L={L} P_L={val[0]:.4f} P_L*L={val[0]*L:.3f} worst on crossing link: {bool(val[1])}", flush=True)
    verdict = "PASS-PL"
    for name, r in res.items():
        vals = [r[L] for L in sorted(r)]
        decreasing = all(vals[i + 1] < vals[i] for i in range(len(vals) - 1))
        if 5 in r and 9 in r:
            if r[9] >= 0.9 * r[5]:
                verdict = "FAIL-PL"
            elif not (decreasing and r[9] <= 0.7 * r[5]) and verdict == "PASS-PL":
                verdict = "NEITHER-PL"
    print(verdict)


if __name__ == "__main__":
    main()
