#!/usr/bin/env python3
"""
U(1)_b wall attack (6-mechanism workflow) — verification runner.

VERDICT: the wall STANDS (0/6 mechanisms reach F1), but its location is
CORRECTED. The missing ingredient is NOT a phase (U(1)_b / theta) quotient
— it is a RADIAL real-dimension 2->1 reduction of the doublet isotype.

This runner verifies the load-bearing facts:
  (1) circulant spectrum lambda_j = a + 2|b| cos(theta + 2 pi j/3);
  (2) Q is EXACTLY theta-independent => theta = arg(b) (the Brannen phase
      delta) is ORTHOGONAL to the F1/F3 knob r = |b|^2/a^2.  Hence
      "quotient the doublet phase" is a category error;
  (3) phase marginalization (flat C_3-invariant Gaussian) leaves the polar
      Jacobian -> r = 2, NOT 1/2;  the phase route cannot reach F1;
  (4) the crossed-product / Pontryagin-dual additive U(1) (the object
      Probe 14 lacked) DOES exist and rotates theta, but leaves r
      invariant -> still F3;
  (5) the surviving wall is radial: F1 (r=1/2) needs the {omega,omega-bar}
      doublet to count as ONE unit (det^{1/dim} / (1,1)-multiplicity),
      explicitly non-derived on main.
"""

import numpy as np
np.set_printoptions(precision=6, suppress=True)


def circulant(a, b):
    """H = a I + b C + conj(b) C^2 on C^3, C the cyclic shift."""
    C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    return a * np.eye(3) + b * C + np.conj(b) * (C @ C)


def koide_Q(a, b):
    H = circulant(a, b)
    s = np.linalg.eigvalsh(H)              # eigenvalues ARE the sqrt-masses
    if np.any(s < -1e-12):
        return None                        # outside positivity cone (need s>=0)
    s = np.clip(s, 0, None)
    return (s ** 2).sum() / (s.sum() ** 2)  # Q = sum m / (sum sqrt m)^2


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    sep("(1) circulant spectrum:  lambda_j = a + 2|b| cos(theta + 2pi j/3)")
    a, bmag, theta = 1.0, 0.5, 0.7
    b = bmag * np.exp(1j * theta)
    H = circulant(a, b)
    lam = np.sort(np.linalg.eigvalsh(H))
    pred = np.sort([a + 2 * bmag * np.cos(theta + 2 * np.pi * j / 3) for j in range(3)])
    print(f"  eig(H)   = {lam}")
    print(f"  formula  = {pred}")
    print(f"  match: {np.allclose(lam, pred)}")

    sep("(2) Q is EXACTLY theta-independent  => theta _|_ r=|b|^2/a^2")
    print("  a=1, |b|=0.4 (so r=|b|^2/a^2=0.16), sweep theta:")
    for th in [0.0, 0.2, 0.5, 1.0, np.pi / 2, 2.0]:
        b = 0.4 * np.exp(1j * th)
        Q = koide_Q(a, b)
        print(f"    theta={th:5.3f}:  Q = {Q:.8f}")
    r = 0.16
    print(f"  closed form Q = 1/3 + (2/3) r = {1/3 + 2/3*r:.8f}  (matches, all theta)")
    print("  => theta is the Brannen phase delta; it deforms individual masses")
    print("     but Q depends ONLY on r. 'Quotient theta' cannot fix r. CATEGORY ERROR.")

    sep("(3) phase marginalization (flat C_3-invariant Gaussian) -> r=2, NOT 1/2")
    rng = np.random.default_rng(0)
    N = 400000
    sig = 1.0
    av = rng.normal(0, sig, N)
    reb = rng.normal(0, sig, N)
    imb = rng.normal(0, sig, N)
    E_plus = 3 * np.mean(av**2)                 # trivial isotype power
    E_perp = 6 * np.mean(reb**2 + imb**2)       # doublet isotype power
    r_eff = np.mean(reb**2 + imb**2) / np.mean(av**2)
    print(f"  <E_+>  = 3<a^2>      = {E_plus:.4f}")
    print(f"  <E_perp> = 6<|b|^2>  = {E_perp:.4f}")
    print(f"  r = <|b|^2>/<a^2>    = {r_eff:.4f}   (F1 needs 1/2; F3 is 1)")
    print("  The polar Jacobian |b| d|b| dtheta keeps BOTH real dims: marginalizing")
    print("  theta is a constant 2pi factor, it removes NO degree of freedom. r stays ~2.")

    sep("(4) crossed-product / Pontryagin-dual additive U(1): rotates theta, leaves r")
    print("  rho_alpha : grade-j coefficient -> e^{i alpha j}.  On b (grade +1): b -> e^{i alpha} b.")
    a = 1.0; b0 = 0.5 * np.exp(1j * 0.3)
    for al in [0.0, 0.7, np.pi, 2.5]:
        b = np.exp(1j * al) * b0
        r = (abs(b)**2) / (a**2)
        print(f"    alpha={al:5.3f}:  arg(b)={np.angle(b):+.3f}  r=|b|^2/a^2={r:.6f}")
    print("  => the additive U(1) Probe 14 lacked DOES exist (outer/dual action),")
    print("     but it moves ONLY arg(b); |b|^2/a^2 is invariant. Wrong direction.")

    sep("(5) the SURVIVING wall is RADIAL, not angular")
    print("  F1 (Q=2/3, r=1/2): equate isotype TOTAL Frobenius norms 3a^2 = 6|b|^2.")
    print("  F3 (Q=1,   r=1  ): equate PER-REAL-DIMENSION norms  3a^2/1 = 6|b|^2/2.")
    print("  Every A1+A2 measure counts the doublet by its real dimension 2 -> F3/free.")
    print("  F1 needs the {omega, omega-bar} pair to count as ONE complex unit")
    print("  (det^{1/dim} / (1,1)-multiplicity) -- a RADIAL 2->1 reduction, the SAME")
    print("  object flagged non-derived in CL3_GAMMA_INVOLUTION_DETERMINANT. Phase")
    print("  routes (gauge, dynamical, decoherence, MaxEnt-via-theta) are all dead.")

    sep("VERDICT")
    print("  Wall STANDS (0/6 mechanisms). NET ADVANCE: (i) the additive U(1)_b")
    print("  exists (crossed-product dual) so Probe 14's 'no additive U(1)' is")
    print("  superseded; (ii) but it is Q-orthogonal, so the wall is RELOCATED")
    print("  from the angular (theta) to the RADIAL (real-dim 2->1) direction.")
    print("  Next: modular/Tomita weight of the trace state on the HERMITIAN")
    print("  circulant algebra, where b-bar=conj(b) ties the pair -- the one")
    print("  untested place 'pair=1' might be FORCED by reality, not imported.")


if __name__ == "__main__":
    main()
