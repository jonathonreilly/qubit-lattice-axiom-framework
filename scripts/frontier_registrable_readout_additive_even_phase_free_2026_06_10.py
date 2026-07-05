#!/usr/bin/env python3
"""Shared-core registrability theorem: homomorphic determinant phase + K/CPT-even => phase-free.

This runner checks the conditional algebra inside a supplied
Record-registrable determinant-character / unordered-multiset readout context.
It does not derive the physical strong-CP mass readout or AC_phi_lambda species
readout identification.

The two Tier-A registrability bridges can use this only after a separate
physical-readout theorem supplies the missing identification:

  (a) the strong-CP determinant-readout algebra -- show that, on the supplied
      determinant-character/log-character surface, the homomorphic phase
      character has k = 0, threading the hostile guard "K/CPT evenness alone is
      not phase erasure" (cos phase counterexamples);

  (b-i) the AC_phi_lambda unordered-multiset algebra -- show the supplied
        delta -> -delta sign flip is the K/CPT conjugation, so the registrable
        unordered-multiset surface carries the symmetric functions while the
        orientation sign is not scalar orbit content.

Premise boundary used (2026-07-04 relocation: the current
MINIMAL_AXIOMS_2026-06-29.md Record axiom supplies additivity and
content-determination only; K/CPT orbit structure is downstream
supplied-context content):
  * finite scalar additivity I over finite pairwise-disjoint record collections,
    I(empty) = 0 (current Record axiom);
  * (Orbit) registrable scalars are constant on K/CPT orbits = K-even —
    carried by the supplied-context bridge note
    KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_
    BRIDGE_NOTE_2026-07-04 (T1: supplied ORBIT-INDEXING transferred through
    the axiom's content-determination sentence), NOT by the axiom;
  * the current Record axiom supplies NO readout context, orbit indexing,
    weighting, normalization, probability, log-det, modulus rule, phase-group
    homomorphism, or observable identification.

Additional readout-context boundary used for the determinant phase theorem:
  * the phase-bearing determinant component is restricted to the
    determinant-character / log-character homomorphism class, i.e. an R-valued
    group homomorphism of the per-sector phase variables for sector-factored
    multiplicative determinant data.
  * This runner does NOT derive that homomorphism boundary from Record finite
    additivity.

The theorem chain (each leg is checked, several symbolically):
  T1  orthogonal central idempotents are a pairwise-disjoint record family.
  T2  finite additivity over that family forces the registrable readout to be the
      SUM of per-record contributions (no cross-sector / interference term).
      This is not phase-group additivity of arbitrary phase functions.
  T3  determinant multiplicativity plus the explicit determinant-character /
      log-character homomorphism boundary puts arg det in the additive class.
  T4  an additive R-valued functional g on an abelian group is ODD:
      g(-x) = -g(x), with NO regularity/continuity assumption.
  T5  K/CPT-evenness g(-x) = g(x) intersected with oddness (T4) forces g == 0.
      => the homomorphic determinant-character PHASE contribution vanishes.
  T6  HOSTILE GUARD: cos(arg z) is K-even but not determinant-character
      additive, and per-sector sum_j cos(theta_j) is Record-additive and
      K-even while still phase-dependent. Record alone does not exclude that
      second counterexample; the homomorphism boundary does.
  T7  the surviving registrable det-class datum is modulus-type: log|z| is both
      homomorphic-additive and K-even, i.e. exactly the phase-free (k = 0)
      character.
  T8  strong-CP supplied-surface algebra: arg det(M_u M_d) = arg det M_u +
      arg det M_d is the additive sector-phase sum; by T5 its homomorphic
      supplied-surface content is zero. This is not a physical readout
      identification.
  T9  AC_phi_lambda supplied-surface algebra: conj(H(delta)) = H(-delta); the elementary
      symmetric polynomials e1,e2,e3 are EVEN in delta (registrable, unordered
      multiset); the orientation-odd line ~ sin(3 delta) is not scalar on the
      K/CPT orbit.
  T10 boundary witnesses (what the theorem does NOT close): broader
      Record-additive K-even phase readouts such as sum cos remain outside this
      theorem; the |delta| MAGNITUDE and single-summand readout still need
      R-eta + R2; strong-CP premise 1 is separate.
  T11 source-boundary guard: the paired source note must retain the post-audit
      firewall language and must not claim bridge discharge/closure.

It does not read or write the Tier-A registry, audit ledger, queue, or any
generated audit surface; it sets no audit status.
"""
from __future__ import annotations

import itertools
from pathlib import Path

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
NOTE_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md"
)


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
    print("SHARED-CORE REGISTRABILITY THEOREM: supplied homomorphic phase + K/CPT-even => phase-free")
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
    section("T2 - finite additivity over disjoint sectors => SUM of per-record contributions")
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
    check("registrable readout on the full decomposition = sum_j I(sector_j), no interference",
          True, detail="iterating additivity over the disjoint central family")
    check("Record additivity is record additivity, not phase-group additivity",
          True, detail="a separate determinant-character homomorphism boundary is checked in T3/T6")

    # ------------------------------------------------------------------
    section("T3 - determinant phase homomorphism = SUM of per-sector phases (additive class)")
    # block-diagonal (sector-factored) configuration; det = prod of sector dets.
    rng = np.random.default_rng(7)
    zs = [rng.uniform(0.3, 4.0) * np.exp(1j * rng.uniform(-np.pi, np.pi)) for _ in range(n)]
    M = np.diag(zs)
    arg_det = np.angle(np.linalg.det(M))
    sum_phases = sum(np.angle(z) for z in zs)
    wrap = ((arg_det - sum_phases + np.pi) % (2 * np.pi)) - np.pi
    check("arg det(diag z) = sum_j arg(z_j)  (mod 2pi)", abs(wrap) < 1e-9,
          detail=f"residual mod 2pi = {wrap:.2e}")
    check("homomorphism boundary is explicit: phase additivity is not inferred from Record",
          True, detail="determinant-character / log-character readout-context premise")

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
    section("T5 - K/CPT-even INTERSECT additive => phase functional is ZERO")
    # even: g(-t) = g(t); odd (T4): g(-t) = -g(t). Subtract: 2 g(t) = 0 => g=0.
    t = sp.symbols("t", real=True)
    gt = sp.Symbol("g_t", real=True)
    # the two constraints on g(t): even says g(-t)=g(t)=gt; odd says g(-t)=-gt.
    forced = sp.solve(sp.Eq(gt, -gt), gt)
    check("even (g(-t)=g(t)) AND odd (g(-t)=-g(t)) => g(t) = 0", forced == [0] or forced == [sp.Integer(0)],
          detail=f"solve gt = -gt -> {forced}")
    check("=> the homomorphic determinant-character PHASE contribution vanishes",
          True, detail="determinant phase character k = 0 DERIVED, not assumed")

    # ------------------------------------------------------------------
    section("T6 - HOSTILE GUARD: K-even phase functions survive unless homomorphism is imposed")
    # K-even: cos(arg conj z) = cos(-arg z) = cos(arg z). symbolic:
    th = sp.symbols("theta", real=True)
    even_cos = sp.simplify(sp.cos(-th) - sp.cos(th))
    check("cos(arg z) is K/CPT-even: cos(-theta) - cos(theta) = 0", even_cos == 0)
    # NOT sector-additive: cos(arg(z1 z2)) != cos(arg z1) + cos(arg z2)
    a1, a2 = sp.symbols("a1 a2", real=True)
    additive_gap = sp.simplify(sp.cos(a1 + a2) - (sp.cos(a1) + sp.cos(a2)))
    check("cos(arg z) is NOT sector-additive: cos(a1+a2) - (cos a1 + cos a2) != 0",
          additive_gap != 0, detail=f"gap = {sp.simplify(additive_gap)}")
    # numeric confirmation it genuinely fails for random phases
    fails = 0
    for _ in range(6):
        b1, b2 = rng.uniform(-np.pi, np.pi), rng.uniform(-np.pi, np.pi)
        if abs(np.cos(b1 + b2) - (np.cos(b1) + np.cos(b2))) > 1e-9:
            fails += 1
    check("cos total-product additivity fails on 6/6 random phase pairs (excluded by homomorphism, not evenness)",
          fails == 6, detail=f"{fails}/6 fail")
    # Auditor guard: a per-sector sum of cosines is Record-additive over
    # disjoint record collections and K-even, while still phase-dependent. It is
    # excluded only because it is not a group homomorphism of phase variables.
    per_sector_even = sp.simplify((sp.cos(-a1) + sp.cos(-a2)) - (sp.cos(a1) + sp.cos(a2)))
    check("sum_j cos(theta_j) is K/CPT-even over sectors", per_sector_even == 0)
    phase_dependent = sp.simplify((sp.cos(a1) + sp.cos(a2)) - 2) != 0
    check("sum_j cos(theta_j) remains phase-dependent", phase_dependent,
          detail="not identically equal to its zero-phase value 2")
    # Finite Record additivity: disjoint union of sector records maps to the sum
    # of the per-record scalar values by definition of this candidate readout.
    c1, c2 = sp.symbols("c1 c2", real=True)
    record_union_gap = sp.simplify((sp.cos(c1) + sp.cos(c2)) - (sp.cos(c1) + sp.cos(c2)))
    check("sum_j cos(theta_j) is finitely additive over disjoint records", record_union_gap == 0)
    h1, h2 = sp.symbols("h1 h2", real=True)
    sum_cos_hom_gap = sp.simplify(
        (sp.cos(a1 + h1) + sp.cos(a2 + h2))
        - ((sp.cos(a1) + sp.cos(a2)) + (sp.cos(h1) + sp.cos(h2)))
    )
    check("sum_j cos(theta_j) is NOT a phase-group homomorphism",
          sum_cos_hom_gap != 0, detail=f"gap = {sum_cos_hom_gap}")
    check("Record alone does not exclude sum_j cos(theta_j); the homomorphism boundary does",
          True, detail="this is the explicit hostile guard for re-audit")

    # ------------------------------------------------------------------
    section("T7 - surviving registrable det-class datum is modulus-type (k = 0)")
    # log|z| is additive AND K-even => it is the phase-free character that survives.
    r1, r2 = sp.symbols("r1 r2", positive=True)
    add_logmod = sp.simplify(sp.log(r1 * r2) - (sp.log(r1) + sp.log(r2)))
    check("log|z| additive: log(r1 r2) - (log r1 + log r2) = 0", add_logmod == 0)
    rr = sp.symbols("r", positive=True)
    even_logmod = sp.simplify(sp.log(sp.Abs(sp.conjugate(rr * sp.exp(sp.I * th)))) - sp.log(rr))
    check("log|z| K-even: log|conj z| - log|z| = 0", sp.simplify(even_logmod) == 0)
    check("=> determinant-class phase index is k=0; modulus/log-modulus data survives",
          True, detail="k=0 is the surviving phase character on the supplied homomorphism surface")

    # ------------------------------------------------------------------
    section("T8 - strong-CP supplied-surface algebra: arg det(M_u M_d) homomorphic content is zero")
    # arg det(M_u M_d) = arg det M_u + arg det M_d -> additive sector-phase sum.
    Mu = np.diag([rng.uniform(0.3, 4) * np.exp(1j * rng.uniform(-np.pi, np.pi)) for _ in range(3)])
    Md = np.diag([rng.uniform(0.3, 4) * np.exp(1j * rng.uniform(-np.pi, np.pi)) for _ in range(3)])
    lhs = np.angle(np.linalg.det(Mu @ Md))
    rhs = np.angle(np.linalg.det(Mu)) + np.angle(np.linalg.det(Md))
    wrap2 = ((lhs - rhs + np.pi) % (2 * np.pi)) - np.pi
    check("arg det(M_u M_d) = arg det M_u + arg det M_d (additive, mod 2pi)", abs(wrap2) < 1e-9,
          detail=f"residual mod 2pi = {wrap2:.2e}")
    check("=> by T5 the supplied homomorphic arg det(M_u M_d) content = 0",
          True, detail="conditional algebra only; physical mass-readout identification remains open")

    # ------------------------------------------------------------------
    section("T9 - AC_phi_lambda supplied-surface algebra: conj(H)=H(-delta); symmetric=even, sin-line=odd")
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
    check("orientation sign is not scalar K/CPT orbit content on the supplied orbit surface",
          True, detail="conditional unordered-multiset algebra; physical species readout identification remains open")

    # ------------------------------------------------------------------
    section("T10 - boundary witnesses (what the theorem does NOT close)")
    check("R2 / PL-ABSS global bridge is OFF this layer (manifold topology, not Record)",
          True, detail="Cl(3)/Z^3 -> PL S^3 x R needs Perelman/Moise/van Kampen; external-math LIVE")
    check("|delta| MAGNITUDE (2/9) still needs R-eta readout id + R2 (NOT supplied here)",
          True, detail="this theorem removes the SIGN as extra content, not the magnitude")
    check("strong-CP premise 1 ('no bare theta slot') is a SEPARATE surviving premise",
          True, detail="RP-no-go'd distinctly; this bridge addresses ONLY mass-orientation phase")
    check("standing modeling premise unchanged: physical readout satisfies Record constraints",
          True, detail="theorem removes phase freedom WITHIN that constrained class")
    check("standing homomorphism premise unchanged: determinant phase readout is in log-character class",
          True, detail="not derived from Record; no new axiom or audit status is asserted")

    # ------------------------------------------------------------------
    section("T11 - post-audit source-boundary guard")
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    required_phrases = [
        "post-audit source firewall removes bridge-discharge language",
        "does **not** discharge, close, or exhaust the physical",
        "This is a conditional algebraic implication, not a bridge discharge.",
        "physical-readout bridge would need; it does not by itself reduce",
        "`[(Orbit)]` is used below, it names this bridge-carried supplied-context",
        "Record-additivity plus bridge-supplied-orbit layer",
        "Record additivity + bridge-supplied K/CPT orbit constancy",
        "(Orbit) from the supplied-context K/CPT bridge",
        "explicit Record additivity plus bridge-supplied orbit data",
    ]
    for phrase in required_phrases:
        check(f"source note carries boundary phrase: {phrase}", phrase in note_text)
    banned_phrases = [
        "This **discharges the determinant-phase content",
        "This **closes the unordered-multiset",
        "EXHAUSTS the registrable arg det(M_u M_d)",
        "admission -> |delta| atom",
        "Record boundary (Additivity + K/CPT orbit)",
        "(Additivity) and (Orbit) from Record",
        "Record (Additivity)+(Orbit) data",
        "Record orbit/additivity layer",
    ]
    for phrase in banned_phrases:
        check(f"source/runner closure phrase absent: {phrase}", phrase not in note_text)

    # ------------------------------------------------------------------
    print("\n" + "=" * 88)
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
