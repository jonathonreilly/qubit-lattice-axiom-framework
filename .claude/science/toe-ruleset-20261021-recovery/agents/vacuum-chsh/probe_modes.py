#!/usr/bin/env python3
"""Stage 2 (added after stage-1 results, see LOG.md): mode-optimised CHSH lower bounds.

Local observables of a region include those of any mode inside it.  For regions A, B
too large for the full Fock state, pick modes a in span(A), b in span(B) and evaluate
CHSH on the reduced Gaussian state of those modes: a LOWER bound on the region's CHSH.
  noSSR, 1+1 modes: closed form (2-mode number-conserving Gaussian + Horodecki),
      CHSH = 2 sqrt(4|g|^2 + max(4|g|^2, T_zz^2)), T_zz = (1-2n_a)(1-2n_b) - 4|g|^2.
  SSR, 2+2 modes: isometries V_A, V_B optimised with an inner see-saw (lower bound).
"""
import os
for v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
          "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import sys
import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import probe as P  # noqa: E402

RNG = np.random.default_rng(7)


def chsh_pair(C, nA, a, b):
    a = a / np.linalg.norm(a)
    b = b / np.linalg.norm(b)
    na = np.real(a.conj() @ C[:nA, :nA] @ a)
    nb = np.real(b.conj() @ C[nA:, nA:] @ b)
    g2 = abs(a.conj() @ C[:nA, nA:] @ b) ** 2
    tzz = (1 - 2 * na) * (1 - 2 * nb) - 4 * g2
    return 2 * np.sqrt(4 * g2 + max(4 * g2, tzz * tzz))


def best_pair(C, nA, restarts=24):
    nB = C.shape[0] - nA
    def unpack(x):
        a = x[:nA] + 1j * x[nA:2 * nA]
        b = x[2 * nA:2 * nA + nB] + 1j * x[2 * nA + nB:]
        return a, b
    f = lambda x: -chsh_pair(C, nA, *unpack(x))
    wa, Va = np.linalg.eigh(C[:nA, :nA])
    wb, Vb = np.linalg.eigh(C[nA:, nA:])
    starts = []
    for i in (0, 1, nA - 2, nA - 1):
        for j in (0, 1, nB - 2, nB - 1):
            a, b = Va[:, i % nA], Vb[:, j % nB]
            starts.append(np.concatenate([a.real, a.imag, b.real, b.imag]))
    while len(starts) < restarts:
        starts.append(RNG.normal(size=2 * (nA + nB)))
    vals = [-minimize(f, x0, method="BFGS", options={"gtol": 1e-10}).fun for x0 in starts]
    vals = np.array(vals)
    return max(2.0, vals.max()), vals.max(), vals.max() - np.median(vals)


def ssr_22(C, nA, restarts=3, maxfev=600):
    nB = C.shape[0] - nA
    def iso(x, n):
        M = (x[:2 * n] + 1j * x[2 * n:]).reshape(n, 2)
        q, _ = np.linalg.qr(M)
        return q
    def val(x):
        VA = iso(x[:4 * nA], nA)
        VB = iso(x[4 * nA:], nB)
        W = np.zeros((nA + nB, 4), complex)
        W[:nA, :2] = VA
        W[nA:, 2:] = VB
        rho, _, _ = P.gaussian_rho(W.conj().T @ C @ W)
        return P.seesaw(rho, 2, 2, ssr=True, restarts=3, iters=60)[0]
    best = []
    wa, Va = np.linalg.eigh(C[:nA, :nA])
    wb, Vb = np.linalg.eigh(C[nA:, nA:])
    for k in range(restarts):
        if k == 0:  # one nearly-filled + one nearly-empty mode per side
            MA, MB = Va[:, [0, nA - 1]], Vb[:, [0, nB - 1]]
            x0 = np.concatenate([MA.real.ravel(), MA.imag.ravel(),
                                 MB.real.ravel(), MB.imag.ravel()])
        else:
            x0 = RNG.normal(size=4 * (nA + nB))
        r = minimize(lambda x: -val(x), x0, method="Powell",
                     options={"maxfev": maxfev, "xtol": 1e-4, "ftol": 1e-9})
        best.append(-r.fun)
    best = np.array(best)
    return best.max(), best.max() - np.median(best)


def main(stage):
    if stage == "pairs":
        for m in (0.0, 0.1, 0.3, 1.0):
            sea = P.Sea(P.L_MAIN, m)
            print(f"\n== m={m}  noSSR 1+1 mode-optimised (floor 2; raw Horodecki; spread)")
            for dname, n in P.DIRS.items():
                for sh in ("s4", "cube", "p3x3", "p4x4"):
                    A = P.shapes(dname)[sh]
                    row = []
                    for r in range(1, 9):
                        B = P.shift(A, r, n)
                        if not P.disjoint(A, B):
                            continue
                        C = sea.C(A + B)
                        v, raw, sp = best_pair(C, len(A))
                        row.append(f"{r}:{raw:.4f}")
                    print(f"-- {dname} {sh}: " + " ".join(row))
                sys.stdout.flush()
    else:
        m = float(stage)
        sea = P.Sea(P.L_MAIN, m)
        print(f"\n== m={m}  SSR 2+2 mode-optimised lower bound (best, spread)")
        for dname, n, sh, rs in (("axis", (1, 0, 0), "cube", (2,)),
                                 ("axis", (1, 0, 0), "p3x3", (1,))):
            A = P.shapes(dname)[sh]
            for r in rs:
                B = P.shift(A, r, n)
                b, sp = ssr_22(sea.C(A + B), len(A))
                print(f"-- {dname} {sh} r={r}: {b:.9f} spread {sp:.1e}")
                sys.stdout.flush()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "pairs")
