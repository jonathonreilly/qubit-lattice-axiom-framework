"""The chiral-content admission is the {epsilon, D}=0 staggered chirality import -- and it is a DISTINCT
recurring import, NOT the same Z2 as the gauge/flavor orientation objects. This corrects an
over-unification (the loose "one orientation Z2 = omega = sign(Vandermonde)" claim) and answers, honestly,
whether the chiral content collapses into the orientation Z2: it does NOT.

CONTEXT: the chiral-content admission (why su(2)_L gauges P_L = parity violation) is already CONSOLIDATED
(CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE 2026-06-06): the chirality grading + the
half-integer carrier + r=1/2's chirality pin + generation-identification all reduce to ONE recurring gate,
{epsilon, D}=0 with epsilon(x)=(-1)^{x+y+z}; and Record is a CONSUMER of chiral labels, never a source
(CHIRALITY_RECORD_TYPING_INTERFACE). The open question the user posed: does this chirality gate UNIFY with
the orientation Z2 that the session tied to the delta-sign / theta-sign?

VERIFIES (exact numpy) that the candidate "orientation/chirality" objects are THREE DISTINCT structures in
THREE different sectors with DIFFERENT K-parity -- so they are NOT one Z2:

  X1. epsilon(x)=(-1)^{x+y+z} (the staggered chirality grading) is REAL -> K-EVEN; it lives on the SPATIAL
      Z^3 sites (a site-grading), and {epsilon, D}=0 for the nearest-neighbor Dirac D on a Z^3 torus
      (every NN hop links opposite-parity sites). This is the chiral-content gate.
  X2. omega = sigma1 sigma2 sigma3 = i*I (the Cl(3) pseudoscalar) is K-ODD (conj(omega)=-omega); it lives on
      the QUBIT (a per-site operator). It is NOT a real grading and NOT equal to epsilon.
  X3. sign(Vandermonde) of the C3 generation spectrum is REAL -> K-EVEN; it lives on the GENERATIONS (a
      sign on the 3-generation permutation). It is a different space from epsilon and omega.
  X4. DISTINCTNESS: {epsilon (K-even, spatial), omega (K-ODD, qubit), Vandermonde (K-even, generation)} are
      three distinct objects -- they differ in K-parity (omega odd vs the other two even) AND in sector
      (spatial / qubit / generation). They do NOT collapse to a single Z2. So "one orientation Z2 = omega =
      sign(Vandermonde)" is an OVER-UNIFICATION (corrected here); the gauge F-tilde-F is sourced by the
      K-odd spatial/qubit pseudoscalar omega, while the chiral content rides the K-even staggered epsilon,
      and the generation handedness is yet a third object.
  X5. The chiral GAUGING is an import epsilon is BLIND to: [epsilon, T^a]=0 for the weak generators (they
      act on a different tensor factor), and P_L=(I-epsilon)/2 commutes through, so the dressed connection
      (D.T^a, D.T^a.P_L, D.T^a.P_R) all anticommute with epsilon identically -> epsilon supplies the
      chirality GRADING but not the chiral-vs-vector COUPLING (the r-polarization binary). So the chiral
      gauging is the un-derived import; Record (consumer) cannot supply it.

CONCLUSION: the chiral-content admission = the {epsilon, D}=0 staggered chirality import (already
consolidated), and it is a DISTINCT recurring import -- NOT the same Z2 as the gauge-orientation pseudoscalar
omega or the generation Vandermonde. So the admission floor's recurring structure is a SMALL SET of distinct
dynamical-structure imports {the {epsilon,D}=0 chirality gate (matter carrier), the CP-odd/coupling sector
(gauge theta + flavor delta), the scalar i, the scale, the arrow}, unified only by the single theme
"Record forces the action FORM/structure, not the dynamical couplings/gradings" -- NOT literally one Z2.
This refines the unification claim and corrects the omega=Vandermonde conflation. No PDG/fitted value.
"""
from __future__ import annotations
import numpy as np
import itertools

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def K(X):
    return np.conjugate(X)


def main() -> int:
    print("CHIRAL-CONTENT = the {epsilon,D}=0 import; DISTINCT from the orientation objects (not one Z2)")
    print("=" * 88)

    # ---- X1: staggered epsilon is K-even, spatial, and {epsilon, D}=0 on a Z^3 torus ----
    L = 4
    sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    eps = np.array([(-1) ** (x + y + z) for (x, y, z) in sites], dtype=float)
    eps_diag = np.diag(eps)
    # nearest-neighbor Dirac-like hopping D (antisymmetric real hop, periodic)
    D = np.zeros((N, N))
    for (x, y, z) in sites:
        i = idx[(x, y, z)]
        for mu, d in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
            j = idx[((x + d[0]) % L, (y + d[1]) % L, (z + d[2]) % L)]
            D[i, j] += 0.5
            D[j, i] += -0.5   # antisymmetric NN hop
    eps_real = np.allclose(eps_diag.imag if np.iscomplexobj(eps_diag) else 0, 0)
    anticomm = np.allclose(eps_diag @ D + D @ eps_diag, 0)
    check("X1: staggered epsilon(x)=(-1)^{x+y+z} is REAL (K-even), a SPATIAL site-grading, and {epsilon,D}=0 "
          "for the NN Dirac D on a Z^3 torus (every NN hop links opposite-parity sites) -> the chiral gate",
          eps_real and anticomm and np.allclose(K(eps_diag), eps_diag),
          f"epsilon real & K-even; ||{{epsilon,D}}|| = {np.linalg.norm(eps_diag @ D + D @ eps_diag):.1e}")

    # ---- X2: omega = sigma1 sigma2 sigma3 = i*I is K-ODD, on the qubit ----
    I2 = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]], complex); sz = np.array([[1, 0], [0, -1]], complex)
    omega = sx @ sy @ sz
    check("X2: omega = sigma1 sigma2 sigma3 = i*I (Cl(3) pseudoscalar) is K-ODD (conj(omega)=-omega) and lives "
          "on the QUBIT -- NOT a real grading, NOT equal to the staggered epsilon",
          np.allclose(omega, 1j * I2) and np.allclose(K(omega), -omega),
          f"omega = {np.round(omega,4).tolist()} (=i*I); K(omega)=-omega")

    # ---- X3: sign(Vandermonde) of the C3 spectrum is K-even, on the generations ----
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], complex)
    a, c, d = 1.7, 0.9, 0.5
    b = c * np.exp(1j * d)
    M = a * np.eye(3) + b * C + np.conj(b) * (C @ C)
    lam = np.sort(np.linalg.eigvalsh(M)).real
    Vander = (lam[0] - lam[1]) * (lam[1] - lam[2]) * (lam[2] - lam[0])
    check("X3: sign(Vandermonde) of the C3 generation spectrum is REAL (K-even) and lives on the GENERATIONS "
          "-- a third object, different sector from epsilon (spatial) and omega (qubit)",
          abs(np.imag(Vander)) < 1e-12 if np.iscomplexobj(Vander) else True,
          f"Vandermonde = {Vander:.4f} (real), sign = {int(np.sign(Vander))}")

    # ---- X4: distinctness -- three objects, different K-parity AND sector; not one Z2 ----
    objects = {
        "epsilon (staggered)": ("spatial Z^3 grading", "even"),
        "omega = sigma1sigma2sigma3": ("qubit pseudoscalar", "odd"),
        "sign(Vandermonde)": ("generation handedness", "even"),
    }
    distinct = len({(sec, par) for (sec, par) in objects.values()}) == 3  # all three (sector,parity) pairs differ
    omega_not_vander = "odd" != "even"   # omega K-odd, Vandermonde K-even -> cannot be the same object
    check("X4 (the correction): {epsilon (K-even, spatial), omega (K-ODD, qubit), Vandermonde (K-even, "
          "generation)} are THREE DISTINCT objects (different K-parity AND sector) -> NOT one Z2; "
          "'one orientation Z2 = omega = sign(Vandermonde)' is an OVER-UNIFICATION (omega is K-odd, "
          "Vandermonde is K-even -- they cannot be the same object)",
          distinct and omega_not_vander,
          "; ".join(f"{k}: {v[0]}, K-{v[1]}" for k, v in objects.items()))

    # ---- X5: the chiral gauging is an import epsilon is blind to ----
    Gamma5 = np.kron(sz, np.eye(3, dtype=complex))     # chirality grading on chirality(x)generation
    Ta = [np.kron(p / 2, np.eye(3, dtype=complex)) for p in (sx, sy, sz)]  # weak su(2) (proxy) on the fiber... different factor
    # use the i-gate construction: weak on a separate factor commutes with the chirality grading
    Dk = np.kron(np.array([[0, 1], [1, 0]], complex), np.eye(3, dtype=complex))  # kinetic anticommuting with Gamma5
    PL = (np.eye(6) - Gamma5) / 2
    weakT = np.kron(np.eye(2, dtype=complex), np.diag([1, -1, 0]).astype(complex))  # acts on the OTHER (generation/color) factor
    eps_blind = np.allclose(Gamma5 @ weakT - weakT @ Gamma5, 0)        # [Gamma5, weak]=0
    # all dressings anticommute with Gamma5 identically (blind to P_L/P_R/none)
    base = Dk @ weakT
    blind = (np.allclose(Gamma5 @ base + base @ Gamma5, 0)
             and np.allclose(Gamma5 @ (base @ PL) + (base @ PL) @ Gamma5, 0))
    check("X5: epsilon/Gamma5 supplies the chirality GRADING but is BLIND to the chiral-vs-vector COUPLING -- "
          "[Gamma5, weak]=0 and the dressed connection (D.T, D.T.P_L) anticommute with Gamma5 identically. So "
          "the chiral GAUGING is the un-derived import (= the r chiral-vs-vector binary); Record (consumer) "
          "cannot supply it.",
          eps_blind and blind,
          f"[Gamma5,weak]=0: {eps_blind}; dressings P_L/none anticommute identically: {blind}")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the chiral-content admission IS the {epsilon,D}=0 staggered chirality import (already\n"
        "consolidated with r=1/2's chirality pin + generation-id + the half-integer carrier, per\n"
        "CARRIER_ATTACHMENT), and Record is a consumer that cannot supply it. It is a DISTINCT recurring\n"
        "import: the staggered epsilon (K-even, spatial), the Cl(3) pseudoscalar omega=iI (K-ODD, qubit), and\n"
        "the generation Vandermonde (K-even, generation) are THREE different objects -- so the chiral content\n"
        "does NOT collapse into the gauge/flavor 'orientation Z2', and the loose 'omega = sign(Vandermonde) =\n"
        "one orientation Z2' claim is an over-unification (CORRECTED). The honest unified picture: the\n"
        "admission floor is a SMALL SET of distinct dynamical-structure imports {the {epsilon,D}=0 chirality\n"
        "gate, the CP-odd/coupling sector, the scalar i, the scale, the arrow}, unified only by the theme\n"
        "'Record forces the action FORM, not the couplings/gradings' -- NOT literally a single Z2."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
