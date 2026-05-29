#!/usr/bin/env python3
"""
DECIDING runner for the charged-lepton Koide program: does A1's quantum
Kahler structure (i = omega) force F1 (Q=2/3), or does the framework
natively give F3 (Q=1)?  Verdict (4-angle workflow, 0 F1 / 4 F3): F3-NO-GO.

The clean decisive argument (the whole ballgame):
  E_+ = 3 a^2  (trivial isotype: 1 real dim = 1/2 complex dim)
  E_perp = 6 |b|^2  (doublet isotype: 2 real dim = 1 complex dim)
ANY CONSISTENT counting gives the 2:1 ratio -> F3 (r=1, Q=1):
  - count BOTH by real dimension: weights (1,2) -> r=1
  - count BOTH by complex dimension (a real line is HALF a complex line):
    weights (1/2, 1) -> r=1
Only the INCONSISTENT ASYMMETRIC count (doublet by complex dim = 1, singlet
by real dim = 1) gives F1 (r=1/2). That asymmetry is the tuned isotype
weight kappa = 2 mu/nu; it is NOT forced by A1's omega=i, which is CENTRAL
and acts as the UNIFORM i*Id_3 on grade-1 (complexifies singlet AND doublet
equally -> ratio preserved -> F3). The F1-giving structure J (rotation about
the body diagonal, fixes the singlet, pairs only the doublet) is sourced by
C_3, not A1, so polarizing w.r.t. J is a free choice / import.
"""

import numpy as np
np.set_printoptions(precision=6, suppress=True)


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def r_from_weights(w_plus, w_perp):
    """Equate per-weight energy: (3 a^2)/w_plus = (6 |b|^2)/w_perp.
    Returns r = |b|^2/a^2 at the balance point."""
    # 3 a^2 / w_plus = 6 |b|^2 / w_perp  =>  |b|^2/a^2 = (3 w_perp)/(6 w_plus)
    return (3 * w_perp) / (6 * w_plus)


def Q_of_r(r):
    return 1/3 + (2/3) * r


def main():
    sep("(1) THE DECISIVE ARITHMETIC: consistent counting -> F3 either way")
    print("  E_+ = 3a^2 (trivial: 1 real dim = 1/2 complex dim)")
    print("  E_perp = 6|b|^2 (doublet: 2 real dim = 1 complex dim)")
    print()
    rows = [
        ("REAL dims both       (w_+, w_perp) = (1, 2)", 1, 2),
        ("COMPLEX dims both    (w_+, w_perp) = (1/2, 1)", 0.5, 1),
        ("ASYMMETRIC (F1)      (w_+, w_perp) = (1, 1)", 1, 1),
    ]
    for label, wp, wpp in rows:
        r = r_from_weights(wp, wpp)
        tag = "F1 (inconsistent!)" if abs(r - 0.5) < 1e-9 else "F3 (consistent)"
        print(f"  {label}: r={r:.4f}  Q={Q_of_r(r):.4f}  -> {tag}")
    print("  => BOTH consistent countings (real-both, complex-both) give r=1=F3.")
    print("     Only the ASYMMETRIC (doublet complex, singlet real) gives F1.")
    print("     F1 = the tuned weight kappa=2mu/nu, NOT a consistent count.")

    sep("(2) omega (Cl(3,0) pseudoscalar = the QM i) is CENTRAL -> uniform i*Id")
    # Pauli realization: e_i -> sigma_i ; omega = sigma1 sigma2 sigma3 = i*I_2
    s1 = np.array([[0, 1], [1, 0]], complex)
    s2 = np.array([[0, -1j], [1j, 0]], complex)
    s3 = np.array([[1, 0], [0, -1]], complex)
    omega = s1 @ s2 @ s3
    print(f"  omega = s1 s2 s3 = {omega.diagonal()}  (= i * I_2, central, omega^2=-1)")
    for nm, s in [("e1", s1), ("e2", s2), ("e3", s3)]:
        comm = omega @ s - s @ omega
        print(f"    [omega, {nm}] = {np.max(np.abs(comm)):.1e}  (commutes => central)")
    print("  => omega acts as the SAME scalar i on every grade-1 axis; it")
    print("     complexifies the singlet a and the doublet b UNIFORMLY, so it")
    print("     cannot supply the asymmetric (doublet-only) complex count. -> F3.")

    sep("(3) the F1-giving J (rotation about body diagonal) is C_3-sourced, != omega")
    n = np.array([1.0, 1, 1]) / np.sqrt(3)
    # J = generator of rotation about n by 90 deg: J v = n x v  (then exp)
    Nmat = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    J = np.eye(3) + Nmat * np.sin(np.pi / 2) + (Nmat @ Nmat) * (1 - np.cos(np.pi / 2))
    print(f"  J fixes the singlet axis n?  J n = {np.round(J @ n,4)}  (= n: {np.allclose(J@n,n)})")
    # doublet vectors (orthogonal to n)
    d1 = np.array([1.0, -1, 0]) / np.sqrt(2)
    Jd1 = J @ d1
    print(f"  J acts on doublet: J d1 . d1 = {np.dot(Jd1,d1):.3f} (=0 => 90deg rotation in plane)")
    print(f"  J^2 on doublet = -Id?  J@J@d1 = {np.round(J@J@d1,4)} vs -d1 = {np.round(-d1,4)}")
    print("  => J fixes the singlet and pairs ONLY the doublet (the asymmetric")
    print("     structure F1 needs). It is sourced by C_3 generation symmetry,")
    print("     NOT by A1. omega (uniform i*Id_3) is a DIFFERENT operator. So")
    print("     'polarize w.r.t. J' is a free choice / import, not forced by A1.")

    sep("(4) packet parameter space {(a,b): a in R, b in C} = R^3 is ODD-dim")
    print("  dim_R = 1 (a) + 2 (b) = 3 (ODD) -> admits NO global complex")
    print("  structure. There is no canonical holomorphic polarization of the")
    print("  mass-operator packet itself; omega=i lives in the qubit state")
    print("  space, not on this R^3 parameter space.")

    sep("VERDICT: F3-NO-GO. Framework predicts Q=1; Q=2/3 needs an import.")
    print("  A1+A2+retained natively select F3 (r=1, Q=1) for the charged-lepton")
    print("  generation carrier, on EVERY consistent channel: classical/real")
    print("  measures, the perturbative+nonperturbative dynamical channel, AND")
    print("  the genuinely quantum/Kahler measure built from A1's own omega=i.")
    print("  Q=2/3 (F1) requires the ASYMMETRIC isotype weight (doublet counted")
    print("  as 1 complex unit, singlet as 1 real unit) = the tuned kappa=2mu/nu")
    print("  = polarizing w.r.t. the C_3-sourced J instead of A1's omega. That")
    print("  is an unflagged IMPORT, not forced by A1. The equipartition")
    print("  derivation rests on exactly this asymmetric (inconsistent) count.")
    print("  CONCLUSION: the framework, taken honestly with a consistent")
    print("  measure, predicts Q=1 -- NOT the observed 2/3. Deriving 2/3 needs")
    print("  new structure (a forced complex structure pairing ONLY the")
    print("  generation doublet) that A1+A2+retained do not supply.")


if __name__ == "__main__":
    main()
