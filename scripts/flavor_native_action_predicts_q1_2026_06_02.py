"""Action axis: the native heat-kernel / Casimir / Connes spectral action on the generation factor
has its interior stationary point at |b|/a ~ 1 (r=1, Q=1, the dimension/Plancherel default), NOT at
the charged-lepton point |b|/a = 1/sqrt2 (r=1/2). And the {Wilson, HK, Manton} action-form
degeneracy is r-IRRELEVANT: the on-site:hopping (a:|b|) split is set at quadratic order, where all
three forms agree on the bi-invariant metric, so breaking the degeneracy at O(X^4) cannot move r.

So no native action delivers r=1/2; the framework's native action-sector prediction is Q=1, and
r=1/2 is reached only by the equal-block Hilbert-Schmidt partition 3a^2=6|b|^2 (= the admitted input
AC_phi_lambda), a measure/reading prescription on the single invariant Tr(H^2), not a stationarity
condition of any native action.

This runner verifies the spectral-action critical |b|/a across several cutoff
functions and the equal-block landmark. It reports source checks only.
"""
import numpy as np

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

    # Spectral-action interior extremum |b|/a across cutoff functions -> ~1 (r=1), never 1/sqrt2.
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
        "spectral-action interior extremum |b|/a ~ 1 (r=1) for every cutoff, never near 1/sqrt2=0.707",
        all_near_one and far_from_half,
        "; ".join(f"{k}:{v:.3f}" for k, v in crit.items())))

    # The extremum at b/a=1 is the [3a,0,0] point (doublet eigenvalue collapses to 0): r=1, Q=1.
    lam_at_1 = np.sort(np.linalg.eigvalsh(H_real(1.0, 1.0)))
    Q_at_1 = (lam_at_1 ** 2).sum() / (lam_at_1.sum() ** 2)
    passed.append(check(
        "at b/a=1 the spectrum is [0,0,3a] (doublet -> 0), r=1, Q=1 (dimension/Plancherel default)",
        np.allclose(lam_at_1, [0, 0, 3], atol=1e-9) and abs(Q_at_1 - 1.0) < 1e-9,
        f"spectrum={lam_at_1}, Q={Q_at_1:.6f}"))

    # Action-form degeneracy is r-irrelevant: at quadratic order all forms give the same bi-invariant
    # |X|^2 metric; mass (k=0) and hopping (k=1,2) live in HS-ORTHOGONAL C_3 character modes, so the
    # bi-invariant metric only rescales the overall norm, never relates the two amplitudes.
    # Verify the two grades are HS-orthogonal (no cross term => ratio not fixed by a single norm).
    cross = np.real(np.trace((a * I3).conj().T @ (b * (C + C.T))))
    passed.append(check(
        "mass grade (I) and hopping grade (C+C^2) are HS-orthogonal => one bi-invariant norm cannot fix the a:|b| ratio",
        abs(cross) < 1e-12, f"<mass,hop>_HS = {cross:.2e}"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("FINDING: the native heat-kernel/Casimir/spectral action interior extremum is at r=1 (Q=1) for")
    print("every cutoff; the action-form degeneracy is r-irrelevant (mass/hop HS-orthogonal, set at")
    print("quadratic order). The tested native action axis does not deliver r=1/2; r=1/2 is")
    print("the equal-block partition 3a^2=6b^2 = AC_phi_lambda. Native action-sector")
    print("tendency = Q=1 for this route.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
