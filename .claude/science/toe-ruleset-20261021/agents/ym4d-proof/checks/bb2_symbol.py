"""bb2: the level-1 Hessian symbol at small momentum vs the Wilson symbol (BFT_B.md §5.1, Theorem BB-4♮ at k = 1).
Criteria: checks/bb2_criteria.md (written first). Usage: python3 bb2_symbol.py"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bb1_decay as BB1  # noqa: E402  (build: the bb1 fibre model)
import c37_kcurv as K37  # noqa: E402  (d1c, d0c, say)

say = K37.say
DIRS = [np.array(v, float) / np.linalg.norm(v) for v in ((1, 0, 0, 0), (1, 1, 0, 0), (1, 1, 1, 1), (1, 2, 0, 3))]
TS = (0.4, 0.2, 0.1, 0.05, 0.025)


def H1(F, Kv, kap):
    """Exactly bb1_decay.hats' formula at one (off-grid) momentum, complex128."""
    Ok = F.Ot(Kv, kap); Dk = F.d(Kv); Qk = F.Q(Kv)
    rhs = np.hstack([Dk.conj().T @ F.iota, Qk.conj().T])
    X = np.linalg.solve(Ok, rhs)
    Cg = X - F.onemPi @ rhs
    x = -Cg[:, :6]
    return -kap * (Qk @ x) @ K37.d1c(Kv)


def transverse(g):
    """Two orthonormal vectors orthogonal to g (complex Gram-Schmidt from the real basis)."""
    out = []
    u0 = g / np.linalg.norm(g)
    for b in np.eye(4):
        v = b.astype(complex) - u0 * (u0.conj() @ b)
        for w in out:
            v = v - w * (w.conj() @ v)
        if np.linalg.norm(v) > 1e-3:
            out.append(v / np.linalg.norm(v))
        if len(out) == 2:
            break
    return out


def run(F, kap):
    gauge = herm = 0.0
    beta = {}
    rho = {t: 0.0 for t in TS}
    for t in TS:
        for i, n in enumerate(DIRS):
            Kv = t * n
            H = H1(F, Kv, kap)
            d1 = K37.d1c(Kv); HW = d1.conj().T @ d1
            g = K37.d0c(Kv).ravel()
            nh = np.linalg.norm(H, 2)
            gauge = max(gauge, np.linalg.norm(H @ g) / (nh * np.linalg.norm(g)))
            herm = max(herm, np.linalg.norm(H - H.conj().T, 2) / nh)
            for j, e in enumerate(transverse(g)):
                beta[(t, i, j)] = float(np.real(e.conj() @ H @ e) / np.real(e.conj() @ HW @ e))
            rho[t] = max(rho[t], np.linalg.norm(H - HW, 2) / t ** 4)
    return gauge, herm, beta, rho


def main():
    F = BB1.build(); say("bb2: fibres built")
    ok = {}
    for kap in (1.0, 0.25, 4.0):
        gauge, herm, beta, rho = run(F, kap)
        b25 = [beta[(0.025, i, j)] - 1 for i in range(4) for j in range(2)]
        b05 = [beta[(0.05, i, j)] - 1 for i in range(4) for j in range(2)]
        ratios = [abs(a) / abs(b) for a, b in zip(b05, b25) if abs(a) > 1e-9]
        rr = (rho[0.05] / rho[0.1], rho[0.025] / rho[0.05])
        say(f"kappa={kap}: gauge defect {gauge:.2e}; hermiticity defect {herm:.2e}")
        for t in TS:
            say(f"kappa={kap} t={t}: beta-1 = " + ", ".join(f"{beta[(t, i, j)] - 1:+.3e}" for i in range(4) for j in range(2))
                + f"; rho(t) = {rho[t]:.6e}")
        say(f"kappa={kap}: max|beta(0.025)-1| = {max(map(abs, b25)):.3e}; ratios |b(0.05)-1|/|b(0.025)-1| = "
            + ", ".join(f"{r:.3f}" for r in ratios) + f"; rho ratios {rr[0]:.4f}, {rr[1]:.4f}")
        if kap == 1.0:
            ok["B2-1"] = gauge <= 1e-8
            ok["B2-2"] = max(map(abs, b25)) <= 1e-3 and all(2.5 <= r <= 6 for r in ratios)
            ok["B2-3"] = all(0.8 <= r <= 1.25 for r in rr)
    print(f"bb2: {'PASS' if all(ok.values()) else 'FAIL'} {ok}", flush=True)


if __name__ == "__main__":
    main()
