#!/usr/bin/env python3
"""
Finite C3 count/readout bookkeeping.

This runner checks the algebraic table relating C3 block weights to Q values,
and the finite spectral-asymmetry identity L_3(1,2)=2/9. It does not derive the
source of the Koide value from the framework, certify phenomenology closure,
or set a verdict.

  F1  THE THREE WEIGHTS. With Q=(1+2r)/3, r=|b|^2/a^2, and block weights (mu,nu) on the
      (singlet, doublet) C3-isotypes giving extremum r*=nu/(2 mu): democratic (1,0)->Q=1/3
      (degenerate/symmetric limit); equal-block (1,1)->Q=2/3 (mass ratio); dimension /
      Plancherel (1,2)->Q=1.
  F2  DIMENSION COUNT AND SPECTRAL ASYMMETRY. The finite Z_N
      equivariant spectral-asymmetry / Lefschetz weight L_N(a) = (1/N) sum_{k=1}^{N-1}
      prod_j 1/(zeta_N^{k a_j} - 1) evaluates to L_3(1,2) = 2/9 exactly, and
      2/9 = (N-1)/N^2 = (doublet dimension 2)/N^2 -- the per-DIMENSION (doublet-counted-
      twice) weight.
  F3  ONE COUNTING FORK, TWO FINITE READOUTS. Count-once (block) gives the
      Q=2/3 readout; count-twice (dimension) gives the L_3(1,2)=2/9 spectral readout.
  F4  SAMPLE VALUES. The runner evaluates Q at the explicit input r=1/2 and
      evaluates L_3(1,2). These are checks of finite readout formulas, not a
      source derivation of r=1/2.
"""

import sys

import sympy as sp

PASSES: list[tuple[str, bool, str]] = []


def record(name, ok, detail=""):
    PASSES.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        for line in detail.split("\n"):
            print(f"       {line}")


def section(t):
    print("\n" + "=" * 88 + f"\n{t}\n" + "=" * 88)


def L_N(a_tuple, N):
    """finite Z_N equivariant spectral-asymmetry / Lefschetz weight (rational value)."""
    zeta = sp.exp(2 * sp.pi * sp.I / N)
    total = 0
    for k in range(1, N):
        prod = 1
        for aj in a_tuple:
            prod *= 1 / (zeta**(k * aj) - 1)
        total += prod
    # the value is a real rational; recover it robustly from the numeric evaluation
    return sp.nsimplify(complex(sp.expand(total / N).evalf()).real, rational=True)


def main():
    section("C3 count readouts: Q table plus spectral asymmetry 2/9")

    # ---- F1: the three weights -> Q=1/3, 2/3, 1 --------------------------------
    section("F1 — the three C3-block weights -> Q = 1/3, 2/3, 1")
    r = sp.Symbol("r", nonnegative=True)
    Q = (1 + 2 * r) / 3
    rows = []
    for name, (mu, nu) in [("democratic (1,0)", (1, 0)), ("equal-block (1,1)", (1, 1)),
                           ("dimension/Plancherel (1,2)", (1, 2))]:
        r_star = sp.Rational(nu, 2 * mu) if mu else sp.Integer(0)
        Qv = Q.subs(r, r_star)
        rows.append((name, r_star, Qv))
    record("F1.1 democratic->Q=1/3, equal-block->Q=2/3, dimension->Q=1 (r*=nu/2mu)",
           rows[0][2] == sp.Rational(1, 3) and rows[1][2] == sp.Rational(2, 3) and rows[2][2] == 1,
           "; ".join(f"{n}: r*={rs}, Q={qv}" for n, rs, qv in rows))

    # ---- F2: the dimension count IS the spectral asymmetry 2/9 -----------------
    section("F2 - dimension count and spectral asymmetry L_3(1,2) = 2/9 = (N-1)/N^2")
    L = L_N((1, 2), 3)
    record("F2.1 L_3(1,2) = 2/9 exactly (finite Z_N spectral-asymmetry formula)",
           sp.simplify(L - sp.Rational(2, 9)) == 0, f"L_3(1,2) = {L}")
    N = 3
    record("F2.2 2/9 = (N-1)/N^2 = (doublet dimension 2)/N^2 (the per-DIMENSION count)",
           sp.Rational(N - 1, N**2) == sp.Rational(2, 9),
           f"(N-1)/N^2 = {sp.Rational(N-1, N**2)}; doublet dim = {N-1} counted over N^2 = {N**2}")

    # ---- F3: one count, two observables ----------------------------------------
    section("F3 - count doublet once/twice -> two finite readouts")
    # block count: doublet weighted 1 -> equal-block -> Q=2/3 (mass ratio)
    Q_block = Q.subs(r, sp.Rational(1, 2))
    # dimension count: doublet weighted 2 -> 2/9 spectral asymmetry
    record("F3.1 count-once (block) -> Q=2/3 readout; count-twice (dimension) -> "
           "spectral-asymmetry 2/9 readout",
           Q_block == sp.Rational(2, 3) and sp.simplify(L - sp.Rational(2, 9)) == 0,
           f"block(1): Q={Q_block} (mass ratio); dimension(2): L_3={L} (spectral asymmetry)")
    record("F3.2 the dimension weight gives Q=1 under the Q-readout and 2/9 under "
           "the spectral-asymmetry readout",
           rows[2][2] == 1 and sp.simplify(L - sp.Rational(2, 9)) == 0,
           "dimension count: Koide-readout Q=1, spectral-readout L_3=2/9 -- same (1,2) weight")

    # ---- F4: both realized -----------------------------------------------------
    section("F4 - sample formula values")
    # mass ratio 2/3 from the signed circulant at r=1/2 (independent re-derivation)
    a_s, x_s = sp.symbols("a x", positive=True)
    import numpy as np
    a_v, b_v = 1.0, 1 / np.sqrt(2)            # r=1/2
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    lam = np.sort(np.linalg.eigvals(a_v * np.eye(3) + b_v * C + b_v * (C @ C)).real)
    Q_phys = sum(lam**2) / (sum(lam))**2
    record("F4.1 Q-readout equals 2/3 at the explicit input r=1/2 (block readout)",
           abs(Q_phys - 2 / 3) < 1e-9, f"Q(r=1/2) = {Q_phys:.6f}")
    record("F4.2 spectral-asymmetry readout: L_3(1,2) = 2/9 (dimension readout)",
           sp.simplify(L - sp.Rational(2, 9)) == 0, f"L_3(1,2) = {L} = 2/9")

    # ---- summary ----------------------------------------------------------------
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    print(f"  {n_pass}/{len(PASSES)} checks passed")
    print()
    print("  The C3 doublet has two finite count readouts:")
    print("    count-once (block)      -> Q-readout 2/3 at r=1/2")
    print("    count-twice (dimension) -> spectral asymmetry 2/9 = (N-1)/N^2")
    print("  This is bookkeeping support, not a derivation of the source of r=1/2.")

    if n_pass == len(PASSES):
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{len(PASSES) - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
