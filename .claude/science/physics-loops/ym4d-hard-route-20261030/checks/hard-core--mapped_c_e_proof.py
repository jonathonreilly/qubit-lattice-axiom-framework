#!/usr/bin/env python3
"""Test of the closed proof that g(P) - 1 >= (1 - B^-2) |P-hat|^2 / (6 d), `library/sector-values.md`, Lemma 3.3-bis.

Criteria, written before any run.
 C1. S_4(P) := sum_{m in Z_B} D_B((P + 2 pi m)/B)^4 equals (2 B^2 + 1 + (B^2 - 1) cos P) / (3 B^2), to 1e-10.
 C2. Sum over aliases of prod_rho D^2 equals 1, to 1e-10 (the Parseval step).
 C3. H_n := |P-hat|^2 / (B^2 |k-hat_n|^2) <= sum_rho y_rho x_{n rho}, on every alias, to 1e-12.
 C4. Gamma_mu := G_mu_mu |P-hat|^2 / B^4 <= 1 - (1 - B^-2) sum_rho P-hat_rho^4 / (6 |P-hat|^2), for all mu, to 1e-12.
 C5. Control against the existing check's direct form: the least eigenvalue of Min at d = 4, L = 3, 5 is at least
     B^(d-4) (1 + (1 - B^-2) |P-hat|^2 / (6 d)), at random P and on the grid, to 1e-10.
 C6. The bound is not vacuous: the least value of (g - 1) / |P-hat|^2 found is within a factor 4 of the bound's constant at d = 4.
PASS if all hold. A FAIL of C1 to C4 refutes the proof as written. Limits: finite samples; the proof itself is algebra.
"""
import importlib.util
import itertools
import os
import resource
import sys

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def guard():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    gb = r / 1024**3 if sys.platform == "darwin" else r / 1024**2
    if gb > 2:
        raise SystemExit("RSS above 2 GB")


def dirichlet(q, B):
    s = np.sin(q / 2)
    out = np.ones_like(q, dtype=float)
    mask = np.abs(s) > 1e-12
    out[mask] = np.sin(B * q[mask] / 2) / (B * s[mask])
    # at s = 0, D = +-1 by the limit; sign is irrelevant since only squares are used.
    return out


def aliases(P, B, d):
    ms = np.array(list(itertools.product(range(B), repeat=d)), dtype=float)
    return (P[None, :] + 2 * np.pi * ms) / B


def gammas(P, B, d):
    Phat = 2 * np.sin(P / 2)
    P2 = float(np.sum(Phat**2))
    y = Phat**2 / P2
    k = aliases(P, B, d)
    khat = 2 * np.sin(k / 2)
    k2 = np.sum(khat**2, axis=1)
    x = dirichlet(k, B) ** 2
    w = np.prod(x, axis=1)
    keep = k2 > 1e-20
    H = np.zeros_like(k2)
    H[keep] = P2 / (B**2 * k2[keep])
    Gamma = np.array([np.sum(w[keep] * x[keep, mu] * H[keep]) for mu in range(d)])
    return Gamma, H[keep], x[keep], y, w, P2, Phat


def main():
    fails = []
    rng = np.random.default_rng(20261101)
    worst_c1 = worst_c2 = 0.0
    worst_c3 = worst_c4 = -1.0
    for d, Bs in ((2, (3, 5, 9, 27)), (3, (3, 5, 9)), (4, (3, 5, 7, 9))):
        for B in Bs:
            n_p = 60 if d < 4 else (40 if B <= 5 else 12)
            pts = [rng.uniform(-np.pi, np.pi, size=d) for _ in range(n_p)]
            pts += [np.array(t) for t in itertools.product((0.0, 0.05, np.pi / 2, np.pi), repeat=d) if max(t) > 0][:40]
            for P in pts:
                guard()
                for rho in range(d):
                    q = (P[rho] + 2 * np.pi * np.arange(B)) / B
                    S4 = float(np.sum(dirichlet(q, B) ** 4))
                    worst_c1 = max(worst_c1, abs(S4 - (2 * B**2 + 1 + (B**2 - 1) * np.cos(P[rho])) / (3 * B**2)))
                Gamma, H, x, y, w, P2, Phat = gammas(P, B, d)
                k_all = aliases(P, B, d)
                w_all = np.prod(dirichlet(k_all, B) ** 2, axis=1)
                worst_c2 = max(worst_c2, abs(float(np.sum(w_all)) - 1.0))
                worst_c3 = max(worst_c3, float(np.max(H - x @ y)))
                bound = 1 - (1 - B**-2) * float(np.sum(Phat**4)) / (6 * P2)
                worst_c4 = max(worst_c4, float(np.max(Gamma) - bound))
    print(f"C1 max |S4 - formula| = {worst_c1:.2e}")
    print(f"C2 max |Parseval - 1| = {worst_c2:.2e}")
    print(f"C3 max H_n - sum y x  = {worst_c3:.2e}")
    print(f"C4 max Gamma - bound  = {worst_c4:.2e}")
    if worst_c1 > 1e-10:
        fails.append("C1")
    if worst_c2 > 1e-10:
        fails.append("C2")
    if worst_c3 > 1e-12:
        fails.append("C3")
    if worst_c4 > 1e-12:
        fails.append("C4")

    spec = importlib.util.spec_from_file_location("ex", os.path.join(HERE, "hard-core--mapped_excess.py"))
    ex = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ex)
    d = 4
    best = {}
    worst_c5 = -1.0
    for L in (3, 5):
        pts = list(ex.grid(d)) + [tuple(rng.uniform(-np.pi, np.pi, size=d)) for _ in range(150)]
        pts += [(0.02, 0.02, 0.02, 0.0), (0.02, 0.02, 0.02, 0.02)]
        vals = []
        for P in pts:
            guard()
            Min, _, P2 = ex.forms(P, L, 1, d)
            ev = float(np.linalg.eigvalsh(0.5 * (Min + Min.T))[0])
            floor = 1 + (1 - L**-2) * P2 / (6 * d)
            worst_c5 = max(worst_c5, floor - ev)
            vals.append((ev - 1) / P2)
        best[L] = min(vals)
        print(f"L = {L}: min (g-1)/|P-hat|^2 = {best[L]:.5f}, bound's constant {(1 - L**-2) / (6 * d):.5f}, ratio {best[L] / ((1 - L**-2) / (6 * d)):.3f}")
    print(f"C5 max floor - least eigenvalue = {worst_c5:.2e}")
    if worst_c5 > 1e-10:
        fails.append("C5")
    if any(best[L] / ((1 - L**-2) / (6 * d)) > 4 for L in best):
        fails.append("C6")
    print("PASS" if not fails else "FAIL " + " ".join(fails))


if __name__ == "__main__":
    main()
