#!/usr/bin/env python3
"""
Native generation geometry is Hermitian, not Kähler.

The charged-lepton Koide value Q=2/3 (<=> r=|b|^2/a^2 = 1/2) is set by the
doublet FIELD-COUNT of the generation order parameter

    Y = a I + b C + b-bar C^2      (b = x + i y in C, C the Z_3 cyclic shift),

NOT by a choice of readout: the native signed (Brannen/det_R) readout gives
Q=(1+2r)/3 independent of theta=arg(b). Field-count 1 (b one holomorphic mode,
theta = conjugate momentum) gives r=1/2, Q=2/3, b chiral; field-count 2
(Re b, Im b independent) gives r free, Q=1 by the dimension reading.

This runner certifies, symbolically, the six structural facts that localize the
entire pin to one differential-geometric object — the missing symplectic form
omega completing (g, J) to a Kähler triple:

  F1  det M is CONJUGATION-EVEN:  det M(b-bar) = det M(b) identically, with
      det M = a^3 - 3a(x^2+y^2) + 2x^3 - 6 x y^2.  A conjugation-even real
      scalar action carries no first-order (time-antisymmetric) Berry term,
      hence no omega = dRe(b) ^ dIm(b).
  F2  The doublet metric is ISOTROPIC (flat Kähler metric):
      ||M_perp||_F^2 = 6(x^2+y^2) = 6|b|^2.
  F3  J = (C - C^2)/sqrt(3) is a genuine COMPLEX STRUCTURE on the doublet:
      J^2 = -P_doublet, J P_singlet = 0, and J is (proportional to) the
      generator of the theta=arg(b) rotation.
  F4  The signed readout is THETA-INVARIANT at fixed |b|: Q_signed = (1+2r)/3,
      = 2/3 at r=1/2 for every theta.
  F5  At r=1/2 the masses m_k = lambda_k^2 are TWO distinct at theta=0 and
      THREE distinct at theta>0, while Q stays exactly 2/3 — theta is a second,
      independent recorded coordinate (field-count 2), not Q-moving.
  F6  NO native anticommuting grading: B = C + C^2 has spectrum {2,-1,-1},
      not lambda<->-lambda symmetric, so no G with G^2=I and {G,B}=0 exists.
      The count-1 (Kähler) collapse needs exactly such a chiral grading — the
      koide_z3_equivariant_anticommuting_no_go wall at the field-reality level.

Conclusion (positive structural localization, NOT a no-go on Q=2/3): the native
retained Berezin action over the real anti-Hermitian D
(cpt_exact_real_anti_hermitian_d, spin_statistics_berezin_determinant) supplies
the complex structure J and the Kähler metric g, but NOT the symplectic form
omega. The native generation geometry is a Hermitian pair (g, J), not a Kähler
triple (g, J, omega). The missing omega is the single chiral import, shared
identically with the generation-identification chirality gate.

Anchors (all retained on the live ledger): koide_circulant_q_two_thirds_algebraic,
koide_anticommuting_operator_derivation, cpt_exact_real_anti_hermitian_d,
spin_statistics_berezin_determinant, koide_z3_equivariant_anticommuting_no_go,
site_phase_cube_shift_intertwiner.

READ-ONLY structural certificate. Sets no audit status; the audit lane decides
tier and the Hermitian-vs-Kähler convention classification.
"""

import itertools
import sys

import sympy as sp

PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = ""):
    PASSES.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        for line in detail.split("\n"):
            print(f"       {line}")


def section(title: str):
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def main() -> int:
    section("Native generation geometry is Hermitian, not Kähler")

    a, x, y = sp.symbols("a x y", real=True)
    omega = sp.exp(2 * sp.pi * sp.I / 3)

    # Z_3 cyclic shift C (regular rep generator); C^2 = C^T, C^3 = I.
    C = sp.Matrix([[0, 0, 1],
                   [1, 0, 0],
                   [0, 1, 0]])
    I3 = sp.eye(3)
    record("C is the order-3 cyclic shift (C^3 = I, C != I)",
           sp.simplify(C**3 - I3) == sp.zeros(3) and C != I3,
           f"C^3 - I = {sp.simplify(C**3 - I3).tolist()}")

    # Generation order parameter Y = a I + b C + b-bar C^2, b = x + i y.
    b = x + sp.I * y
    bbar = x - sp.I * y
    Y = a * I3 + b * C + bbar * C.T

    # ---- F1: det M conjugation-even -------------------------------------------
    section("F1 — det M is conjugation-even (no first-order Berry term)")
    detY = sp.simplify(Y.det())
    target_det = a**3 - 3 * a * (x**2 + y**2) + 2 * x**3 - 6 * x * y**2
    record("F1.1 det M = a^3 - 3a(x^2+y^2) + 2x^3 - 6xy^2",
           sp.simplify(detY - target_det) == 0,
           f"det M = {sp.expand(detY)}")

    # conjugation b -> b-bar is y -> -y
    det_conj = target_det.subs(y, -y)
    record("F1.2 det M(b-bar) = det M(b) identically (conjugation-EVEN)",
           sp.simplify(det_conj - target_det) == 0,
           f"det M(b-bar) - det M(b) = {sp.simplify(det_conj - target_det)}")

    # ---- F2: isotropic Kähler metric ------------------------------------------
    section("F2 — doublet Frobenius metric is isotropic (flat Kähler metric)")
    # M_perp = Y - (trace/3) I = doublet part = bC + b-bar C^2
    M_perp = b * C + bbar * C.T
    # ||M_perp||_F^2 = sum |entry|^2 = sum Re(entry * conj(entry))
    fro_entries = (M_perp.multiply_elementwise(M_perp.conjugate())).applyfunc(sp.re)
    fro_total = sp.simplify(sum(fro_entries))
    record("F2.1 ||M_perp||_F^2 = 6(x^2+y^2) = 6|b|^2 (isotropic)",
           sp.simplify(fro_total - 6 * (x**2 + y**2)) == 0,
           f"||M_perp||_F^2 = {sp.expand(fro_total)}")
    # isotropy: the Hessian in (x,y) is a scalar multiple of identity
    H = sp.hessian(fro_total, (x, y))
    record("F2.2 metric Hessian = 12 * I_2 (no preferred axis -> only metric, "
           "candidate for omega is unconstrained)",
           sp.simplify(H - 12 * sp.eye(2)) == sp.zeros(2),
           f"Hessian = {H.tolist()}")

    # ---- F3: complex structure J = (C - C^2)/sqrt(3) --------------------------
    section("F3 — J = (C - C^2)/sqrt(3) is a complex structure on the doublet")
    J = (C - C.T) / sp.sqrt(3)
    ones = sp.Matrix([[1, 1, 1]] * 3)
    P_singlet = ones / 3
    P_doublet = I3 - P_singlet
    record("F3.1 J^2 = -P_doublet",
           sp.simplify(J * J - (-P_doublet)) == sp.zeros(3),
           f"J^2 + P_doublet = {sp.simplify(J*J + P_doublet).tolist()}")
    record("F3.2 J annihilates the singlet (J P_singlet = 0)",
           sp.simplify(J * P_singlet) == sp.zeros(3),
           f"J P_singlet = {sp.simplify(J*P_singlet).tolist()}")
    # generator of theta=arg(b) rotation: d/dtheta of (b C + b-bar C^2) at b=|b|
    # b = R e^{i theta}; derivative at theta=0, b real R:  i R (C - C^2) = i R sqrt3 J
    R = sp.symbols("R", positive=True)
    dY_dtheta = sp.I * R * C - sp.I * R * C.T  # d/dtheta[ R e^{i th} C + c.c.] @0
    record("F3.3 theta=arg(b) rotation generator = i*R*sqrt(3)*J (J IS the "
           "phase generator)",
           sp.simplify(dY_dtheta - sp.I * R * sp.sqrt(3) * J) == sp.zeros(3),
           f"dY/dtheta - i R sqrt3 J = "
           f"{sp.simplify(dY_dtheta - sp.I*R*sp.sqrt(3)*J).tolist()}")

    # ---- F4: signed readout theta-invariant -----------------------------------
    section("F4 — signed (Brannen) readout Q=(1+2r)/3 is theta-invariant")
    # eigenvalues of Y (circulant): lam_k = a + b w^k + b-bar w^{2k}
    lams = [sp.simplify(sp.expand_complex(a + b * omega**k + bbar * omega**(2 * k)))
            for k in range(3)]
    lams = [sp.simplify(sp.re(l)) for l in lams]  # all real
    S1 = sp.simplify(sum(lams))           # sum lambda
    S2 = sp.simplify(sum(l**2 for l in lams))  # sum lambda^2
    record("F4.1 sum lambda = 3a (trace), sum lambda^2 = 3a^2 + 6|b|^2",
           sp.simplify(S1 - 3 * a) == 0 and
           sp.simplify(S2 - (3 * a**2 + 6 * (x**2 + y**2))) == 0,
           f"sum lambda = {S1}, sum lambda^2 = {sp.expand(S2)}")
    r = sp.symbols("r", positive=True)
    Q_signed = sp.simplify(S2 / S1**2)  # = (3a^2+6|b|^2)/(9a^2) = (1+2r)/3
    Q_in_r = sp.simplify(Q_signed.subs(x**2 + y**2, r * a**2)
                         .subs(y, 0).subs(x, sp.sqrt(r) * a))
    record("F4.2 Q_signed = (1+2r)/3, theta-free (depends only on |b|^2)",
           sp.simplify(Q_in_r - (1 + 2 * r) / 3) == 0,
           f"Q_signed(r) = {Q_in_r}")
    Q_at_half = Q_in_r.subs(r, sp.Rational(1, 2))
    record("F4.3 Q_signed(r=1/2) = 2/3",
           Q_at_half == sp.Rational(2, 3),
           f"Q_signed(1/2) = {Q_at_half}")

    # ---- F5: masses split with theta, Q fixed ---------------------------------
    section("F5 — at r=1/2 masses are 2 distinct (theta=0) -> 3 distinct "
            "(theta>0); Q stays 2/3")
    Rmag = a / sp.sqrt(2)  # |b| with r=1/2
    # masses m_k = lambda_k^2 with b = Rmag e^{i theta}
    def masses(theta_val):
        xv = Rmag * sp.cos(theta_val)
        yv = Rmag * sp.sin(theta_val)
        ls = [sp.re(sp.expand_complex(
            a + (xv + sp.I * yv) * omega**k + (xv - sp.I * yv) * omega**(2 * k)))
            for k in range(3)]
        return [sp.simplify(l**2) for l in ls]

    m0 = [sp.nsimplify(mm.subs(a, 1)) for mm in masses(0)]
    mth = [sp.nsimplify(mm.subs(a, 1)) for mm in masses(sp.pi / 6)]
    n_distinct_0 = len(set(sp.simplify(v) for v in m0))
    n_distinct_th = len(set(sp.simplify(v) for v in mth))
    record("F5.1 theta=0: exactly 2 distinct masses",
           n_distinct_0 == 2,
           f"masses(theta=0) = {[float(v) for v in m0]}")
    record("F5.2 theta=pi/6: exactly 3 distinct masses",
           n_distinct_th == 3,
           f"masses(theta=pi/6) = {[float(v) for v in mth]}")
    # Q from these masses (signed: sqrt m_k = lambda_k can be negative; use signed)
    def Q_from_b(theta_val):
        xv = Rmag * sp.cos(theta_val)
        yv = Rmag * sp.sin(theta_val)
        ls = [sp.re(sp.expand_complex(
            a + (xv + sp.I * yv) * omega**k + (xv - sp.I * yv) * omega**(2 * k)))
            for k in range(3)]
        return sp.simplify(sum(l**2 for l in ls) / (sum(ls))**2)
    Qs = [sp.simplify(Q_from_b(t)) for t in (0, sp.pi / 6, sp.pi / 4, sp.pi / 3)]
    record("F5.3 Q_signed = 2/3 for theta in {0, pi/6, pi/4, pi/3} (theta-invariant)",
           all(q == sp.Rational(2, 3) for q in Qs),
           f"Q(theta) = {Qs}")

    # ---- F6: no native anticommuting grading ----------------------------------
    section("F6 — no native chiral grading: B=C+C^2 spectrum {2,-1,-1} "
            "(no lambda<->-lambda)")
    B = C + C.T
    spec_B = sorted(int(sp.re(ev)) for ev in B.eigenvals().keys()
                    for _ in range(B.eigenvals()[ev]))
    record("F6.1 spec(B=C+C^2) = {-1,-1,2}",
           spec_B == [-1, -1, 2],
           f"spec(B) = {spec_B}")
    spec_negB = sorted(-v for v in spec_B)
    record("F6.2 spec(B) != spec(-B) -> no G (G^2=I) with {G,B}=0 "
           "(no anticommuting grading)",
           spec_B != spec_negB,
           f"spec(B) = {spec_B}, spec(-B) = {spec_negB}")
    # constructive: search for any signature grading G=diag(+-1) anticommuting w/ B
    found = False
    for signs in itertools.product([1, -1], repeat=3):
        G = sp.diag(*signs)
        if sp.simplify(G * B + B * G) == sp.zeros(3):
            found = True
            break
    record("F6.3 brute force: no diagonal sign grading G anticommutes with B",
           not found,
           "checked all 8 diag(+-1,+-1,+-1); none satisfy {G,B}=0")

    # ---- summary --------------------------------------------------------------
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print(f"  {n_pass}/{n_total} checks passed")
    print()
    print("  Native generation geometry = (g, J) Hermitian PAIR:")
    print("    g  = isotropic Kähler metric 6|b|^2          [F2]   PRESENT")
    print("    J  = (C - C^2)/sqrt(3) complex structure      [F3]   PRESENT")
    print("    omega = dRe(b) ^ dIm(b) symplectic form       [F1]   ABSENT")
    print("           (det M conjugation-even -> no Berry term)")
    print()
    print("  omega ABSENT  =>  theta independent coordinate  [F5]  => count 2 => Q=1")
    print("  omega PRESENT =>  theta = conjugate momentum          => count 1 => Q=2/3")
    print("  supplying omega == native chiral grading, which is non-native [F6]")
    print()
    print("  => the value Q=2/3, the field-count, and the generation chirality")
    print("     are ONE object: the missing symplectic form omega. Not a measure")
    print("     choice — a fact about whether the matter action is Kähler.")

    if n_pass == n_total:
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{n_total - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
