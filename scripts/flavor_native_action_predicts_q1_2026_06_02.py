"""Action-axis finite scan on the generation factor.

For H = aI + b(C+C^2), five displayed spectral-action cutoffs have their
finite-scan maxima near |b|/a = 1 (r=1, Q=1), not at the charged-lepton point
|b|/a = 1/sqrt2 (r=1/2). The runner also checks that the on-site and hopping
grades are Hilbert-Schmidt orthogonal, so a single HS quadratic norm does not
relate the two amplitudes.

This runner does not prove a theorem for arbitrary monotone cutoffs, Casimir/HK
Brownian time, or Wilson/HK/Manton action-form degeneracy.
"""
from pathlib import Path

import numpy as np

from flavor_occupancy_boundary_checks_2026_06_13 import run_occupancy_boundary_checks

C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def H_real(a, b):
    # delta=0 (Q is delta-independent); real symmetric hopping b(C+C^2).
    return a * I3 + b * (C + C.T)


def spectral_action(a, b, f):
    lam = np.linalg.eigvalsh(H_real(a, b))
    return np.sum(f(lam ** 2))


def critical_bover_a(f, a=1.0):
    # maximize/extremize S(b) = sum f(lam_i^2) over b>=0; report the interior extremum b/a.
    bs = np.linspace(0.0, 2.0, 20001)
    S = np.array([spectral_action(a, b, f) for b in bs])
    # interior extremum = global argmax of S over b (decaying f => Tr f peaks where eigenvalues small)
    return bs[np.argmax(S)] / a


def main():
    passed = []

    # HS block norms: ||aI||^2 = 3a^2, ||b(C+C^2)||^2 = 6 b^2.
    a, b = 1.0, 0.5
    mass_hs = np.real(np.trace((a * I3).conj().T @ (a * I3)))
    hop_hs = np.real(np.trace((b * (C + C.T)).conj().T @ (b * (C + C.T))))
    passed.append(check(
        "HS block norms 3a^2 and 6b^2 (||C+C^2||_F^2 = 6)",
        abs(mass_hs - 3 * a ** 2) < 1e-12 and abs(hop_hs - 6 * b ** 2) < 1e-12,
        f"||mass||^2={mass_hs}, ||hop||^2={hop_hs}"))

    # Equal-block partition 3a^2=6b^2 <=> b/a=1/sqrt2 <=> r=b^2/a^2=1/2.
    passed.append(check(
        "equal-block 3a^2=6b^2  <=>  b/a=1/sqrt2  <=>  r=1/2",
        abs(np.sqrt(0.5) - 1 / np.sqrt(2)) < 1e-12 and abs((1 / np.sqrt(2)) ** 2 - 0.5) < 1e-12,
        f"1/sqrt2 = {1/np.sqrt(2):.6f}, r=1/2"))

    # Spectral-action finite-scan maximum |b|/a across five cutoff functions -> ~1 (r=1),
    # never 1/sqrt2. This is a finite displayed-family scan, not an arbitrary-cutoff theorem.
    cutoffs = {
        "exp(-x)": lambda x: np.exp(-x),
        "exp(-x^2)": lambda x: np.exp(-x ** 2),
        "(1+x)^-2": lambda x: (1 + x) ** -2.0,
        "(1+x)^-4": lambda x: (1 + x) ** -4.0,
        "(1+x)^-8": lambda x: (1 + x) ** -8.0,
    }
    crit = {name: critical_bover_a(f) for name, f in cutoffs.items()}
    all_near_one = all(abs(v - 1.0) < 0.08 for v in crit.values())
    far_from_half = all(abs(v - 1 / np.sqrt(2)) > 0.2 for v in crit.values())
    passed.append(check(
        "five displayed spectral-action cutoffs peak at |b|/a ~ 1 (r=1), never near 1/sqrt2=0.707",
        all_near_one and far_from_half,
        "; ".join(f"{k}:{v:.3f}" for k, v in crit.items())))

    # The extremum at b/a=1 is the [3a,0,0] point (doublet eigenvalue collapses to 0): r=1, Q=1.
    lam_at_1 = np.sort(np.linalg.eigvalsh(H_real(1.0, 1.0)))
    Q_at_1 = (lam_at_1 ** 2).sum() / (lam_at_1.sum() ** 2)
    passed.append(check(
        "at b/a=1 the spectrum is [0,0,3a] (doublet -> 0), r=1, Q=1 (dimension/Plancherel default)",
        np.allclose(lam_at_1, [0, 0, 3], atol=1e-9) and abs(Q_at_1 - 1.0) < 1e-9,
        f"spectrum={lam_at_1}, Q={Q_at_1:.6f}"))

    # Verify the two grades are HS-orthogonal (no cross term => the ratio is not fixed by a single
    # Hilbert-Schmidt quadratic norm on this ansatz).
    cross = np.real(np.trace((a * I3).conj().T @ (b * (C + C.T))))
    passed.append(check(
        "mass grade (I) and hopping grade (C+C^2) are HS-orthogonal => one bi-invariant norm cannot fix the a:|b| ratio",
        abs(cross) < 1e-12, f"<mass,hop>_HS = {cross:.2e}"))

    root = Path(__file__).resolve().parents[1]
    passed.extend(run_occupancy_boundary_checks(root, check, "downstream occupancy atom"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("FINDING: the five displayed spectral-action cutoffs peak near r=1 (Q=1), not r=1/2.")
    print("The mass/hop grades are HS-orthogonal, so one HS quadratic norm on this ansatz")
    print("does not fix their ratio. This is a finite-scan/source-scope certificate, not")
    print("an arbitrary native-action theorem.")
    print("DOWNSTREAM: the residual is the explicit occupancy/slot-degree atom; no")
    print("action-axis selector is introduced or adopted here.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
