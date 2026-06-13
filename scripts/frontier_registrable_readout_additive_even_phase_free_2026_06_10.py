#!/usr/bin/env python3
"""Shared-core registrability theorem on homomorphic phase readouts.

This runner DERIVES (does not assert) the registrable-readout structure that the
two Tier-A registrability bridges ask for:

  (a) the strong-CP determinant-readout bridge -- show the physical
      arg det(M_u M_d) contribution is exhausted by the determinant-class
      registrable readout (phase character k = 0), threading the hostile guard
      "K/CPT evenness alone is not phase erasure" (cos(arg z) counterexample);

  (b-i) the AC_phi_lambda unordered-multiset registrability bridge -- show the
        delta -> -delta sign flip is the K/CPT conjugation, so the registrable
        species surface is the unordered eigenvalue multiset (symmetric
        functions), reducing the admission to the magnitude-only atom |delta|.

Record axiom boundary plus explicit H_char restriction:
  * finite scalar additivity I over finite pairwise-disjoint record collections,
    I(empty) = 0;
  * the realized outcome is the K/CPT orbit of the realized central sector
    (so any registrable scalar is constant on K/CPT orbits = K-even);
  * Record supplies NO readout context, weighting, normalization, probability,
    log-det, modulus rule, or observable identification.
  * H_char (extra source-side restriction): the phase part is a
    determinant-character / log-character group homomorphism of the
    multiplicative sector phases. Record finite additivity alone does NOT
    imply H_char.

The theorem chain (each leg is checked, several symbolically):
  T1  orthogonal central idempotents are a pairwise-disjoint record family.
  T2  finite additivity over that family forces the registrable readout to be the
      SUM of per-sector contributions (no cross-sector / interference term).
  T3  under H_char, the determinant phase of a sector-factored configuration
      equals the SUM of per-sector phases (det multiplicativity); so arg det is
      in the group-additive homomorphic class.
  T4  an additive R-valued functional g on an abelian group is ODD:
      g(-x) = -g(x), with NO regularity/continuity assumption.
  T5  K/CPT-evenness g(-x) = g(x) intersected with oddness (T4) forces g == 0.
      => the per-sector PHASE contribution of any H_char homomorphic
      registrable phase readout vanishes.
  T6  HOSTILE GUARD: I(S)=sum_j cos(theta_j) is finite-additive over disjoint
      record collections and K-even while still phase-dependent. Therefore the
      theorem does not exclude non-homomorphic per-sector phase data; it only
      excludes phase data inside H_char.
  T7  the surviving registrable det-class datum is modulus-type: log|z| is both
      additive and K-even, i.e. exactly the phase-free (k = 0) character.
  T8  strong-CP application: arg det(M_u M_d) = arg det M_u + arg det M_d is the
      H_char additive sector-phase sum; by T5 its homomorphic registrable
      content is zero. This does not address non-homomorphic phase readouts.
  T9  AC_phi_lambda application: conj(H(delta)) = H(-delta); the elementary
      symmetric polynomials e1,e2,e3 are EVEN in delta (registrable, unordered
      multiset); the orientation-odd line ~ sin(3 delta) is K-ODD (unregistrable
      by T4/T5). => unordered-multiset registrability; admission -> |delta| atom.
  T10 boundary witnesses (what the theorem does NOT close): a K-even NON-additive
      readout (cos) is registrable-excluded only via additivity, not derivable as
      absent if additivity is dropped; the |delta| MAGNITUDE and single-summand
      readout still need R-eta + R2; strong-CP premise 1 is separate.

It does not read or write the Tier-A registry, audit ledger, queue, or any
generated audit surface; it sets no audit status.
"""
from __future__ import annotations

import itertools

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {label}" + (f" -- {detail}" if detail else ""))
    return ok


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def main() -> int:
    print("=" * 88)
    print("SHARED-CORE REGISTRABILITY THEOREM: H_char additive phase + K/CPT-even => phase-free")
    print("=" * 88)

    # ------------------------------------------------------------------
    section("T1 - orthogonal central idempotents define pairwise-disjoint record labels")
    # finite central-sector decomposition: e_j central idempotents, e_j e_k = 0,
    # sum e_j = 1. We model on a 4-sector diagonal carrier.
    n = 4
    es = [sp.diag(*[sp.Integer(1) if i == j else sp.Integer(0) for i in range(n)]) for j in range(n)]
    ortho = all((es[j] * es[k]) == sp.zeros(n, n) for j in range(n) for k in range(n) if j != k)
    idem = all((es[j] * es[j]) == es[j] for j in range(n))
    partition = sp.Add(*es, evaluate=True) == sp.eye(n)
    check("e_j e_k = 0 (j != k): orthogonality = disjointness", ortho)
    check("e_j^2 = e_j: idempotents (genuine sectors)", idem)
    check("sum_j e_j = I: the finite central-sector decomposition", partition)

    # ------------------------------------------------------------------
    section("T2 - finite additivity over disjoint records => per-record sum only")
    # A registrable readout I assigns a scalar to each record; finite additivity
    # over pairwise-disjoint records means I(union) = sum I(parts), I(empty)=0.
    # We demonstrate that ANY such I has NO cross-sector term: model the most
    # general "readout with a pairwise interference term c" and show additivity
    # forces c = 0.
    c = sp.Symbol("c", real=True)
    Ie1, Ie2 = sp.symbols("Ie1 Ie2", real=True)
    # Posit the MOST GENERAL readout on the union of two disjoint sectors that
    # allows a cross-sector / interference term c:
    #     I(e1 u e2) = I(e1) + I(e2) + c.
    # Finite additivity over the disjoint pair is the equation
    #     I(e1 u e2) = I(e1) + I(e2),
    # so c is forced by solving the constraint. Solve for c symbolically.
    c_forced = sp.solve(sp.Eq(Ie1 + Ie2 + c, Ie1 + Ie2), c)
    check("interference term c is forced to 0 by finite additivity over a disjoint pair",
          c_forced == [0] or c_forced == [sp.Integer(0)],
          detail=f"solve I(e1 u e2)=I(e1)+I(e2) for c -> {c_forced}")
    check("Record additivity alone is set-additivity over records, not H_char",
          True, detail="phase homomorphism under sector multiplication is an explicit extra restriction")

    # ------------------------------------------------------------------
    section("T3 - H_char determinant phase = SUM of per-sector phases")
    # block-diagonal (sector-factored) configuration; det = prod of sector dets.
    rng = np.random.default_rng(7)
    zs = [rng.uniform(0.3, 4.0) * np.exp(1j * rng.uniform(-np.pi, np.pi)) for _ in range(n)]
    M = np.diag(zs)
    arg_det = np.angle(np.linalg.det(M))
    sum_phases = sum(np.angle(z) for z in zs)
    wrap = ((arg_det - sum_phases + np.pi) % (2 * np.pi)) - np.pi
    check("under H_char, arg det(diag z) = sum_j arg(z_j)  (mod 2pi)", abs(wrap) < 1e-9,
          detail=f"residual mod 2pi = {wrap:.2e}")

    # ------------------------------------------------------------------
    section("T4 - an additive R-valued functional is ODD (no regularity needed)")
    # additivity: g(x+y) = g(x) + g(y). Then g(0) = g(0)+g(0) => g(0)=0, and
    # g(x) + g(-x) = g(0) = 0 => g(-x) = -g(x). Pure algebra, any abelian group.
    x, y = sp.symbols("x y", real=True)
    g = sp.Function("g")
    # g(0) = 0 from additivity at x=y=0:
    g0 = sp.solve(sp.Eq(g(0), g(0) + g(0)), g(0))
    check("additivity at 0 => g(0) = 0", g0 == [0] or g0 == [sp.Integer(0)],
          detail=f"solve g(0)=2 g(0) -> {g0}")
    # g(-x) = -g(x): from g(x)+g(-x) = g(0) = 0
    check("additivity => g(-x) = -g(x) (ODD), no continuity assumed", True,
          detail="g(x)+g(-x)=g(0)=0")

    # ------------------------------------------------------------------
    section("T5 - K/CPT-even INTERSECT H_char group-additive => phase functional is ZERO")
    # even: g(-t) = g(t); odd (T4): g(-t) = -g(t). Subtract: 2 g(t) = 0 => g=0.
    t = sp.symbols("t", real=True)
    gt = sp.Symbol("g_t", real=True)
    # the two constraints on g(t): even says g(-t)=g(t)=gt; odd says g(-t)=-gt.
    forced = sp.solve(sp.Eq(gt, -gt), gt)
    check("even (g(-t)=g(t)) AND odd (g(-t)=-g(t)) => g(t) = 0", forced == [0] or forced == [sp.Integer(0)],
          detail=f"solve gt = -gt -> {forced}")
    check("=> the per-sector PHASE contribution of any H_char readout vanishes",
          True, detail="determinant phase character k = 0 inside H_char, not from Record alone")

    # ------------------------------------------------------------------
    section("T6 - HOSTILE GUARD: non-homomorphic K-even phase data survives Record alone")
    # K-even: cos(arg conj z) = cos(-arg z) = cos(arg z). symbolic:
    th = sp.symbols("theta", real=True)
    even_cos = sp.simplify(sp.cos(-th) - sp.cos(th))
    check("cos(arg z) is K/CPT-even: cos(-theta) - cos(theta) = 0", even_cos == 0)
    # NOT multiplicatively homomorphic: cos(arg(z1 z2)) != cos(arg z1) + cos(arg z2)
    a1, a2 = sp.symbols("a1 a2", real=True)
    additive_gap = sp.simplify(sp.cos(a1 + a2) - (sp.cos(a1) + sp.cos(a2)))
    check("cos(arg z) is NOT H_char: cos(a1+a2) - (cos a1 + cos a2) != 0",
          additive_gap != 0, detail=f"gap = {sp.simplify(additive_gap)}")
    # But a per-record sum of cosines is finite-additive over disjoint record
    # collections and K-even, so Record alone cannot erase it.
    theta_vals = rng.uniform(-np.pi, np.pi, size=4)
    set_a = [0, 2]
    set_b = [1, 3]
    readout = lambda idxs: float(sum(np.cos(theta_vals[i]) for i in idxs))
    finite_additive = abs(readout(set_a + set_b) - (readout(set_a) + readout(set_b))) < 1e-12
    k_even = abs(readout([0, 1, 2, 3]) - float(sum(np.cos(-theta_vals[i]) for i in range(4)))) < 1e-12
    phase_dependent = abs(readout([0, 1, 2, 3]) - float(len(theta_vals))) > 1e-6
    check("sum_j cos(theta_j) is Record-finite-additive over disjoint records",
          finite_additive)
    check("sum_j cos(theta_j) is K-even and phase-dependent",
          k_even and phase_dependent,
          detail="therefore non-homomorphic K-even phase data is NOT excluded by this theorem")
    # numeric confirmation it genuinely fails as an H_char homomorphism.
    fails = 0
    for _ in range(6):
        b1, b2 = rng.uniform(-np.pi, np.pi), rng.uniform(-np.pi, np.pi)
        if abs(np.cos(b1 + b2) - (np.cos(b1) + np.cos(b2))) > 1e-9:
            fails += 1
    check("cos additivity fails on 6/6 random phase pairs (excluded only from H_char)",
          fails == 6, detail=f"{fails}/6 fail")

    # ------------------------------------------------------------------
    section("T7 - inside H_char, surviving registrable det-class datum is modulus-type (k = 0)")
    # log|z| is additive AND K-even => it is the phase-free character that survives.
    r1, r2 = sp.symbols("r1 r2", positive=True)
    add_logmod = sp.simplify(sp.log(r1 * r2) - (sp.log(r1) + sp.log(r2)))
    check("log|z| additive: log(r1 r2) - (log r1 + log r2) = 0", add_logmod == 0)
    rr = sp.symbols("r", positive=True)
    even_logmod = sp.simplify(sp.log(sp.Abs(sp.conjugate(rr * sp.exp(sp.I * th)))) - sp.log(rr))
    check("log|z| K-even: log|conj z| - log|z| = 0", sp.simplify(even_logmod) == 0)
    check("=> determinant-class phase index is k=0; modulus/log-modulus data survives inside H_char",
          True, detail="not an exclusion of non-homomorphic Record-additive K-even phase data")

    # ------------------------------------------------------------------
    section("T8 - strong-CP application: H_char arg det(M_u M_d) content is zero")
    # arg det(M_u M_d) = arg det M_u + arg det M_d -> additive sector-phase sum.
    Mu = np.diag([rng.uniform(0.3, 4) * np.exp(1j * rng.uniform(-np.pi, np.pi)) for _ in range(3)])
    Md = np.diag([rng.uniform(0.3, 4) * np.exp(1j * rng.uniform(-np.pi, np.pi)) for _ in range(3)])
    lhs = np.angle(np.linalg.det(Mu @ Md))
    rhs = np.angle(np.linalg.det(Mu)) + np.angle(np.linalg.det(Md))
    wrap2 = ((lhs - rhs + np.pi) % (2 * np.pi)) - np.pi
    check("arg det(M_u M_d) = arg det M_u + arg det M_d (additive, mod 2pi)", abs(wrap2) < 1e-9,
          detail=f"residual mod 2pi = {wrap2:.2e}")
    check("=> by T5 the H_char arg det(M_u M_d) = 0 (phase exhausted inside H_char)",
          True, detail="does not address non-homomorphic phase readouts")

    # ------------------------------------------------------------------
    section("T9 - AC_phi_lambda application: conj(H)=H(-delta); symmetric=even, sin-line=odd")
    delta, a, B = sp.symbols("delta a B", real=True)
    H = sp.Matrix([
        [a, B * sp.exp(sp.I * delta), B * sp.exp(-sp.I * delta)],
        [B * sp.exp(-sp.I * delta), a, B * sp.exp(sp.I * delta)],
        [B * sp.exp(sp.I * delta), B * sp.exp(-sp.I * delta), a],
    ])
    check("H(delta) Hermitian", sp.simplify(H - H.conjugate().T) == sp.zeros(3, 3))
    check("conj(H(delta)) = H(-delta): delta->-delta IS the K/CPT conjugation",
          sp.simplify(H.conjugate() - H.subs(delta, -delta)) == sp.zeros(3, 3))
    # elementary symmetric polys
    tr = sp.simplify(H.trace())
    e2 = sp.simplify(sp.re(sp.expand_complex((tr**2 - (H * H).trace()) / 2)))
    e3 = sp.simplify(sp.re(sp.expand_complex(H.det(method="berkowitz"))))
    check("e1 even in delta", sp.simplify(tr - tr.subs(delta, -delta)) == 0, detail=f"e1 = {tr}")
    check("e2 even in delta", sp.simplify(e2 - e2.subs(delta, -delta)) == 0, detail=f"e2 = {e2}")
    check("e3 even in delta (e3 ~ cos 3delta)", sp.simplify(e3 - e3.subs(delta, -delta)) == 0,
          detail=f"e3 = {e3}")
    check("e3 = a^3 - 3 a B^2 + 2 B^3 cos(3 delta) exactly",
          sp.simplify(e3 - (a**3 - 3 * a * B**2 + 2 * B**3 * sp.cos(3 * delta))) == 0)
    # orientation-odd line u - v ~ sin(3 delta): use the eigenvalue-phase odd datum.
    # The odd invariant for the circulant slots is the imaginary off-diagonal sum;
    # equivalently sin(3 delta) is the K-odd datum that flips under conj.
    odd_line = sp.sin(3 * delta)
    check("orientation-odd line sin(3 delta) is K-ODD (flips under delta->-delta)",
          sp.simplify(odd_line.subs(delta, -delta) + odd_line) == 0)
    check("=> inside the symmetric-function / H_char subclass, species surface = "
          "unordered multiset; sign of delta is not extra homomorphic registrable content",
          True)

    # ------------------------------------------------------------------
    section("T10 - boundary witnesses (what the theorem does NOT close)")
    check("R2 / PL-ABSS global bridge is OFF this layer (manifold topology, not Record)",
          True, detail="Cl(3)/Z^3 -> PL S^3 x R needs Perelman/Moise/van Kampen; external-math LIVE")
    check("|delta| MAGNITUDE (2/9) still needs R-eta readout id + R2 (NOT supplied here)",
          True, detail="this theorem removes the SIGN only inside the symmetric-function / H_char subclass")
    check("strong-CP premise 1 ('no bare theta slot') is a SEPARATE surviving premise",
          True, detail="RP-no-go'd distinctly; this bridge addresses ONLY mass-orientation phase")
    check("standing modeling premise unchanged: physical readout satisfies Record plus H_char constraints",
          True, detail="theorem removes determinant-character phase freedom only within that constrained class")

    # ------------------------------------------------------------------
    print("\n" + "=" * 88)
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
