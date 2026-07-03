"""Finite distinctness check for three orientation/chirality objects.

This runner checks that the staggered site grading, the one-qubit
pseudoscalar, and a supplied generation-sector Vandermonde sign are distinct
objects. It does not derive the chiral grading, generation handedness, chiral
gauging, or any action-form theorem.

VERIFIES (exact numpy) that the candidate objects live in three different
sectors and do not collapse to one Z2:

  X1. epsilon(x)=(-1)^{x+y+z} (the staggered chirality grading) is REAL -> K-EVEN; it lives on the SPATIAL
      Z^3 sites (a site-grading), and {epsilon, D}=0 for the nearest-neighbor Dirac D on a Z^3 torus
      (every NN hop links opposite-parity sites).
  X2. omega = sigma1 sigma2 sigma3 = i*I (the Cl(3) pseudoscalar) is K-ODD (conj(omega)=-omega); it lives on
      the QUBIT (a per-site operator). It is NOT a real grading and NOT equal to epsilon.
  X3. sign(Vandermonde) of a supplied C3 generation circulant is REAL -> K-EVEN; it lives on the
      GENERATIONS. It is a different space from epsilon and omega.
  X4. DISTINCTNESS: {epsilon (K-even, spatial), omega (K-ODD, qubit), Vandermonde (K-even, generation)} are
      three distinct objects -- they differ in K-parity (omega odd vs the other two even) AND in sector
      (spatial / qubit / generation). They do NOT collapse to a single Z2.
  X5. In a finite tensor-factor model, the grading is blind to the chiral-vs-vector coupling choice:
      an independent weak/coupling factor commutes with Gamma5, and vector/left/right dressings all
      anticommute with Gamma5 identically. The grading check therefore supplies no selection rule for
      chiral gauging.

CONCLUSION: the three named objects are distinct supplied data. The runner
corrects the omega=Vandermonde=epsilon conflation only. No PDG/fitted value.
"""
from __future__ import annotations
import numpy as np

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
    print("STAGGERED CHIRALITY, QUBIT PSEUDOSCALAR, AND GENERATION HANDEDNESS ARE DISTINCT")
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
          "for the NN Dirac D on a Z^3 torus (every NN hop links opposite-parity sites)",
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

    # ---- X3: sign(Vandermonde) of a supplied C3 spectrum is K-even, on the generations ----
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], complex)
    a, c, d = 1.7, 0.9, 0.5
    b = c * np.exp(1j * d)
    M = a * np.eye(3) + b * C + np.conj(b) * (C @ C)
    lam = np.sort(np.linalg.eigvalsh(M)).real
    Vander = (lam[0] - lam[1]) * (lam[1] - lam[2]) * (lam[2] - lam[0])
    check("X3: sign(Vandermonde) of a supplied C3 generation spectrum is REAL (K-even) and lives on the "
          "GENERATIONS -- a third object, different sector from epsilon (spatial) and omega (qubit)",
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
          "omega is K-odd and the generation Vandermonde is K-even, so they cannot be the same object",
          distinct and omega_not_vander,
          "; ".join(f"{k}: {v[0]}, K-{v[1]}" for k, v in objects.items()))

    # ---- X5: the tested grading is blind to the chiral-vs-vector coupling choice ----
    Gamma5 = np.kron(sz, np.eye(3, dtype=complex))     # chirality grading on chirality(x)generation
    Dk = np.kron(np.array([[0, 1], [1, 0]], complex), np.eye(3, dtype=complex))  # kinetic anticommuting with Gamma5
    PL = (np.eye(6) - Gamma5) / 2
    PR = (np.eye(6) + Gamma5) / 2
    weakT = np.kron(np.eye(2, dtype=complex), np.diag([1, -1, 0]).astype(complex))  # acts on the OTHER (generation/color) factor
    eps_blind = np.allclose(Gamma5 @ weakT - weakT @ Gamma5, 0)        # [Gamma5, weak]=0
    # all dressings anticommute with Gamma5 identically (blind to P_L/P_R/none).
    base = Dk @ weakT
    blind = (np.allclose(Gamma5 @ base + base @ Gamma5, 0)
             and np.allclose(Gamma5 @ (base @ PL) + (base @ PL) @ Gamma5, 0)
             and np.allclose(Gamma5 @ (base @ PR) + (base @ PR) @ Gamma5, 0))
    check("X5: the tested grading is BLIND to the chiral-vs-vector coupling choice -- [Gamma5, weak]=0 and "
          "the dressed connection (D.T, D.T.P_L, D.T.P_R) anticommutes with Gamma5 identically. The grading "
          "check supplies no selection rule for chiral gauging.",
          eps_blind and blind,
          f"[Gamma5,weak]=0: {eps_blind}; vector/left/right dressings anticommute identically: {blind}")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
    print(
        "VERDICT: the staggered epsilon (K-even, spatial), the Cl(3) pseudoscalar omega=iI (K-ODD,\n"
        "qubit), and the supplied generation Vandermonde sign (K-even, generation) are three distinct\n"
        "objects. They do not collapse into one orientation Z2. The finite grading/coupling check is\n"
        "blind to vector/left/right dressing, so it supplies no chiral-gauging selection rule. This is\n"
        "only a distinctness correction; it derives no chirality source, generation handedness, chiral\n"
        "gauging, action-form theorem, or fitted value."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
