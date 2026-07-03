"""Symmetry axis: the qutrit Heisenberg-Weyl / Clifford structure on the generation factor does NOT
force r=1/2. Key disambiguation: the charged-lepton point |b|/a = 1/sqrt2 is the equal-superposition
MAGNITUDE, NOT a Fourier-eigenoperator fixed point -- at r=1/2 the pure-shift mass operator H is not
F-fixed (||F H F^dag - H|| > 0). The genuine F-self-dual operator family carries a FREE parameter
(r free), so 1/sqrt2 is an unmarked member, not the unique self-dual point. HW-covariance forces the
OFF-diagonal balance b=c (equal shift- and clock-weight), never the on-site:hopping ratio r. And the
runner does not use Clifford-intrinsic, Wigner/PSD, or full-orbit value landmarks as selectors.

So the symmetry axis re-confirms, from a new direction, that r=1/2 is unforced by this
HW/Fourier route, not a symmetry fixed point. This runner verifies the qutrit Heisenberg-Weyl
algebra and the scoped facts above. It reports source checks only.
"""
from pathlib import Path

import numpy as np

from flavor_occupancy_boundary_checks_2026_06_13 import run_occupancy_boundary_checks

w = np.exp(2j * np.pi / 3)
# Shift X = C, clock Z, qutrit Fourier F.
X = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
Z = np.diag([1, w, w ** 2])
F = np.array([[w ** (j * k) for k in range(3)] for j in range(3)], dtype=complex) / np.sqrt(3)
I3 = np.eye(3, dtype=complex)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    passed = []

    # Heisenberg-Weyl: Z X = w X Z, F X F^dag = Z.
    passed.append(check(
        "Weyl relation Z X = omega X Z, and Fourier F X F^dag = Z (Clifford normalizer)",
        np.allclose(Z @ X, w * X @ Z) and np.allclose(F @ X @ F.conj().T, Z)))

    # Pure-shift mass operator H = aI + bX + conj(b)X^2 maps under F to the CLOCK line aI+bZ+conj(b)Z^2.
    def Hsh(a, b):
        return a * I3 + b * X + np.conj(b) * X.conj().T

    # At r=1/2 (b/a=1/sqrt2), H is NOT F-fixed: ||F H F^dag - H|| > 0 (word-coincidence, not fixed point).
    a, b = 1.0, 1 / np.sqrt(2)
    H = Hsh(a, b)
    dist_half = np.linalg.norm(F @ H @ F.conj().T - H)
    passed.append(check(
        "at r=1/2, H is NOT a Fourier-eigenoperator: ||F H F^dag - H|| > 0 (=> 1/sqrt2 is not an F fixed point)",
        dist_half > 1.0, f"||FHF^dag - H|| = {dist_half:.3f} (nonzero)"))

    # The pure-shift H is F-fixed only at b=0 (r=0); for all b>0 it moves to the clock line.
    distances = {r: np.linalg.norm(F @ Hsh(1.0, np.sqrt(r)) @ F.conj().T - Hsh(1.0, np.sqrt(r)))
                 for r in (0.0, 0.25, 0.5, 1.0)}
    passed.append(check(
        "pure-shift H is F-fixed only at r=0; nonzero for all r>0 (Fourier self-duality vacuous for the physical operator)",
        distances[0.0] < 1e-9 and all(distances[r] > 0.5 for r in (0.25, 0.5, 1.0)),
        "; ".join(f"r={r}:{d:.3f}" for r, d in distances.items())))

    # The genuine F-self-dual augmented family K = aI + g(X+Z+X^2+Z^2) is F-fixed for ALL g (r free).
    def K(a, g):
        return a * I3 + g * (X + Z + X @ X + Z @ Z)
    fixed_all_g = all(np.linalg.norm(F @ K(1.0, g) @ F.conj().T - K(1.0, g)) < 1e-9
                      for g in (0.1, 0.3, 1 / np.sqrt(2), 1.0, 2.5))
    passed.append(check(
        "the genuine F-self-dual family K=aI+g(X+Z+X^2+Z^2) is F-fixed for ALL g => r=g^2 is a free dial, 1/2 unmarked",
        fixed_all_g))

    # HW-covariance forces the OFF-diagonal balance b=c (shift-weight = clock-weight), NOT the
    # on-site:hopping ratio: G = aI + b(X+X^2) + c(Z+Z^2) is F-fixed iff b=c, with a free.
    def G(a, b, c):
        return a * I3 + b * (X + X @ X) + c * (Z + Z @ Z)
    bc_equal_fixed = np.linalg.norm(F @ G(1.0, 0.4, 0.4) @ F.conj().T - G(1.0, 0.4, 0.4)) < 1e-9
    bc_unequal_notfixed = np.linalg.norm(F @ G(1.0, 0.4, 0.7) @ F.conj().T - G(1.0, 0.4, 0.7)) > 1e-6
    a_free = all(np.linalg.norm(F @ G(aa, 0.4, 0.4) @ F.conj().T - G(aa, 0.4, 0.4)) < 1e-9
                 for aa in (0.2, 1.0, 3.0))
    passed.append(check(
        "F-covariance forces b=c (off-diagonal balance) but leaves the diagonal a FREE => r not fixed",
        bc_equal_fixed and bc_unequal_notfixed and a_free,
        "b=c F-fixed; b!=c not; a free for all values"))

    # The ratio data are invariant under unitary conjugation, but invariance is
    # not selection: it supplies no equation fixing b/a.
    H0 = Hsh(1.3, 0.42)
    HF = F @ H0 @ F.conj().T
    def trace_part(M):
        return np.trace(M) / 3
    def traceless_hs(M):
        T = M - trace_part(M) * I3
        return np.real(np.trace(T.conj().T @ T))
    passed.append(check(
        "trace and traceless-HS ratio are Fourier-conjugation invariant, but this is not value selection",
        np.allclose(trace_part(H0), trace_part(HF)) and np.allclose(traceless_hs(H0), traceless_hs(HF)),
        f"trace={trace_part(H0):.3f}; hs2={traceless_hs(H0):.6f}"))

    root = Path(__file__).resolve().parents[1]
    passed.extend(run_occupancy_boundary_checks(root, check, "downstream occupancy atom"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("FINDING: the tested qutrit Heisenberg-Weyl/Fourier structure does NOT force r=1/2.")
    print("'|b|/a=1/sqrt2 self-dual'")
    print("is a magnitude word-coincidence (H not F-fixed there); the true F-self-dual family has r free;")
    print("F-covariance forces only b=c (off-diagonal), not r. Symmetry axis re-confirms")
    print("r=1/2 is unforced by the scoped HW/Fourier route.")
    print("DOWNSTREAM: the residual is the explicit occupancy/slot-degree atom, not a HW/Fourier equation.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
