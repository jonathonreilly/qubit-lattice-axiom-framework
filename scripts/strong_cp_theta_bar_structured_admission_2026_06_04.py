"""Strong-CP theta_bar = theta_QCD + arg det(M) is a GENUINE ADMISSION in this framework (not forced;
honestly shared with the Standard Model), but it sharpens into a precisely-structured two-prong admission
with TWO verified sub-results where the framework does modestly better than the SM:

 PRONG A (gauge): form-degree DERIVES 'no bare F^F (4-form) slot at the fundamental dim-3 level'
   (C(3,4)=0; a 4-form has zero components on Z^3 SPACE). NEW vs the bare admission. Does NOT force
   theta_QCD=0: the canonical pi_3 large-gauge-winding theta-vacuum lives on the 3-space and survives,
   the Z^3 instanton sector is unsettled, and the emergent-level kill needs an undelivered 'O_h-even
   gauge measure' premise (the O_h pseudoscalar det(R) loophole: odd measure x odd slot = even).
 PRONG B (mass): K-reality collapses arg det M from a continuous O(1) phase to a discrete {0,pi}
   (the C_3 conjugate-symmetric circulant H=aI+bC+conj(b)C^2 has REAL det). NEW vs the SM continuum.
   But this is only the chiral-REMOVABLE part: arg det M is chiral-basis-dependent (axial rotation shifts
   it), only theta_bar is invariant, and the joint-basis bridge (gauge-OS reflection == generation
   conjugation-parity) is UNBUILT; {0,pi}->0 rests on a sign convention; lepton->quark transport is asserted.

 CONNECTION: the arg-det-M half REDUCES to AC_phi_lambda (same C_3 circulant); theta_QCD does not. So a
 (currently unaudited-tier) reduction would shrink the genuine Tier-A count from 2 to (1 shared mass-
 orientation == AC_phi_lambda) + (1 residual theta_QCD).

Sets no audit status (independent audit lane owns that); edits/re-cites no existing row.
"""
import numpy as np
import itertools

w = np.exp(2j * np.pi / 3)
C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    passed = []

    # PRONG A.1 — form degree: a 4-form (Tr F^F) has C(3,4)=0 components on dim-3 SPACE; C(4,4)=1 on dim-4.
    from math import comb
    passed.append(check(
        "PRONG A: no bare F^F (4-form) slot at fundamental dim-3 (C(3,4)=0); the slot exists only on dim-4 (C(4,4)=1)",
        comb(3, 4) == 0 and comb(4, 4) == 1,
        "the theta term's Euclidean 4-form writing has no components on Z^3 space"))

    # PRONG A.2 — O_h pseudoscalar character: R R R eps = det(R) eps for all 48 signed permutations.
    eps = np.zeros((3, 3, 3))
    for i, j, k in itertools.permutations(range(3)):
        s = np.sign((j - i) * (k - i) * (k - j))
        eps[i, j, k] = s
    oh = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            R = np.zeros((3, 3))
            for a in range(3):
                R[a, perm[a]] = signs[a]
            oh.append(R)
    def transform(R):
        return np.einsum('ai,bj,ck,ijk->abc', R, R, R, eps)
    ok = all(np.allclose(transform(R), np.linalg.det(R) * eps) for R in oh)
    passed.append(check(
        "PRONG A: O_h pseudoscalar law R R R eps = det(R) eps on all 48 signed perms => theta-slot is O_h-ODD (an O_h-EVEN measure forbids it)",
        ok and len(oh) == 48,
        f"verified on {len(oh)} O_h elements; but 'measure is O_h-even' is the undelivered premise (pseudoscalar loophole)"))

    # PRONG B.1 — K-reality: the C_3 conjugate-symmetric circulant has REAL det => arg det in {0,pi}.
    max_im = 0.0
    for a, b in [(1.3, 0.5 + 0.4j), (0.7, 0.9 - 0.2j), (2.0, 0.3 + 1.1j)]:
        M = a * I3 + b * C + np.conj(b) * C.conj().T
        max_im = max(max_im, abs(np.imag(np.linalg.det(M))))
    passed.append(check(
        "PRONG B: K-real C_3 circulant H=aI+bC+conj(b)C^2 has REAL det => arg det M in {0,pi} (continuous O(1) -> discrete Z_2)",
        max_im < 1e-12, f"max|Im det| = {max_im:.2e} over sampled (a,b)"))

    # PRONG B.2 — the decisive subtlety: arg det M is chiral-basis-dependent (vacuous removable part).
    # Axial rotation M -> e^{2i alpha} M shifts arg det by 2*n*alpha (n=3) and breaks Hermiticity.
    a, b = 1.3, 0.5  # real b => M Hermitian, arg det = 0
    M = a * I3 + b * (C + C.conj().T)
    alpha = 0.31
    Mrot = np.exp(2j * alpha) * M
    shift = np.angle(np.linalg.det(Mrot)) - np.angle(np.linalg.det(M))
    passed.append(check(
        "PRONG B subtlety: axial rotation shifts arg det by 2*n*alpha=6*alpha and breaks Hermiticity => arg det M is chiral-basis-dependent; only theta_bar is invariant",
        abs(((shift - 6 * alpha + np.pi) % (2 * np.pi)) - np.pi) < 1e-9
        and not np.allclose(Mrot, Mrot.conj().T),
        f"shift={shift:.4f} = 6*alpha={6*alpha:.4f}; Mrot non-Hermitian => 'arg det=0' is the removable part"))

    # CONNECTION — the arg-det-M object IS the AC_phi_lambda C_3 circulant (Im det = 0 around the b-circle).
    ims = [abs(np.imag(np.linalg.det(a * I3 + (r * np.exp(1j * t)) * C + np.conj(r * np.exp(1j * t)) * C.conj().T)))
           for a in (1.0,) for r in (0.6,) for t in np.linspace(0, 2 * np.pi, 24)]
    passed.append(check(
        "CONNECTION: arg det M reduces to AC_phi_lambda (same C_3 circulant); Im det = 0 around the full coupling circle",
        max(ims) < 1e-12, f"max|Im det| over circle = {max(ims):.2e}; theta's mass half == AC_phi_lambda's gate"))

    # A genuinely complex coupling c != conj(b) breaks it: arg det != 0 (so the reduction needs the
    # conjugate-symmetry, i.e. AC_phi_lambda's holomorphic/BAE gate -- NOT free).
    Mc = 1.0 * I3 + (0.5 + 0.4j) * C + (0.5 + 0.7j) * C.conj().T  # c != conj(b)
    passed.append(check(
        "the reduction NEEDS conjugate-symmetry: a complex c != conj(b) gives surviving arg det != 0 (AC_phi_lambda's open BAE gate)",
        abs(np.imag(np.linalg.det(Mc))) > 1e-3,
        f"Im det = {np.imag(np.linalg.det(Mc)):.4f} != 0 when c != conj(b)"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("FINDING: theta_bar=0 is a GENUINE ADMISSION (not forced; shared with the SM), sharpened into a")
    print("two-prong admission. NEW verified sub-results: (A) form-degree 'no bare 4-form slot at dim-3';")
    print("(B) K-reality collapses arg det M to discrete {0,pi}. But A doesn't kill the canonical pi_3")
    print("theta-vacuum and B is only the chiral-removable part (joint-basis bridge unbuilt). The arg-det-M")
    print("half REDUCES to AC_phi_lambda (partial Tier-A consolidation, pending audit). No audit status.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
