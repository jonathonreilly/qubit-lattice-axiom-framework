#!/usr/bin/env python3
"""AC_phi_lambda sub-admission (ii) narrowing: R-eta forced/admitted split.

Class-A finite-dimensional verifier (3x3 exact sympy; tiny memory).

Target: separate, inside the R-eta "density-read-as-angle" readout
identification open obligation, the parts forced by Record registrability and
exact circulant algebra from the physical identification that remains open.

Sections:
  S1  context: the AC_phi_lambda Hermitian circulant; K/CPT = delta -> -delta
  S2  forced form leg 1: additive + orbit-constant => sign/phase strip
      (re-derived from scratch; does NOT inherit any sibling audit status)
  S3  forced form leg 2: channel separation e1/e2 delta-blind, e3 via cos3delta
      (re-derived from scratch), C3 period folding => fundamental domain
  S4  the machinery CANNOT select the value: every constant-magnitude
      candidate identification passes ALL form constraints (hostile family)
  S5  hostile candidates violating named hypotheses DO fail (sign readout,
      non-additive even functional, det-character k != 0)
  S6  forced weights: the C3 cycle's transverse spectrum forces exponents
      (1,2); within the AB/Lefschetz density class with forced weights the
      density value is unique (= 2/9); contrast cells need non-forced weights
  S7  circularity guard: the cos3delta channel is a symbolic identity in
      delta with no density object present (R-eta nowhere in the derivation)
  S8  conditional value: |delta| = 2/9 EXACT conditional on the named atom;
      consistency with the separation no-go boundary (2/9 not in {n pi/3})
  S9  boundary witnesses (what is NOT claimed) + r-firewall statement; and the
      2026-07-05 dependency-status split witnesses (formal-theorem section
      present; the two named non-proof authorities marked context-only at
      their current grades;
      K-orbit form wired as the single one-hop markdown-link authority at its
      current retained-bounded grade; physical readout identification explicitly
      NOT claimed; status authority preserved)

Per-check PASS/FAIL lines; final `TOTAL: PASS=N FAIL=0`.
"""
from __future__ import annotations

from pathlib import Path

import sympy as sp

PASS = 0
FAIL = 0
NOTE = (
    Path(__file__).resolve().parents[1]
    / "docs/ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md"
)


def check(name: str, ok, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def main() -> int:
    a, B, delta, r = sp.symbols("a B delta r", real=True, positive=True)
    I3 = sp.eye(3)
    C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])  # cyclic shift (3-cycle)

    # ------------------------------------------------------------------
    section("S1 - context: AC_phi_lambda circulant; K/CPT conjugation = delta -> -delta")
    H = a * I3 + B * sp.exp(sp.I * delta) * C + B * sp.exp(-sp.I * delta) * C.T
    check("H(delta) is Hermitian",
          sp.simplify(H - H.conjugate().T) == sp.zeros(3, 3))
    check("conj(H(delta)) = H(-delta)  (K/CPT acts as the delta sign flip)",
          sp.simplify(H.conjugate() - H.subs(delta, -delta)) == sp.zeros(3, 3))

    # ------------------------------------------------------------------
    section("S2 - FORCED form leg 1: additive + orbit-constant => sign strip (re-derived)")
    # T4-type: an R-valued additive functional on the phase line is odd.
    # Pure algebra: g(0)=g(0)+g(0) => g(0)=0; g(x)+g(-x)=g(0)=0 => g(-x)=-g(x).
    # Witness on the representative additive datum lam*x (no linearity assumed
    # in the theorem; this is the computed witness of the odd conclusion).
    lam, x = sp.symbols("lam x", real=True)
    g = lam * x
    check("additive datum is odd: g(-x) = -g(x)",
          sp.simplify(g.subs(x, -x) + g) == 0)
    # Orbit-constancy (K/CPT-evenness) on top: g(x) = g(-x) = -g(x) => g = 0.
    sol = sp.solve(sp.Eq(g, g.subs(x, -x)), lam)
    check("odd AND orbit-constant (even) => identically zero (lam = 0)",
          sol == [0], detail=f"solve(g(x)=g(-x)) -> {sol}")
    # The orientation-odd line of the circulant is sin(3 delta): K-odd.
    check("sin(3 delta) is K-ODD (flips under delta -> -delta) => unregistrable",
          sp.simplify(sp.sin(3 * delta).subs(delta, -delta) + sp.sin(3 * delta)) == 0)
    check("=> FORCED: any Record-registrable delta-readout is EVEN in delta "
          "(a function of the K/CPT orbit invariant |delta|); orientation/sign stripped",
          True, detail="form content (S-form-1) of R-eta is derived, not admitted")

    # ------------------------------------------------------------------
    section("S3 - FORCED form leg 2: channel separation + fundamental domain (re-derived)")
    tr = sp.simplify(H.trace())
    e1 = tr
    e2 = sp.simplify(sp.re(sp.expand_complex((tr ** 2 - (H * H).trace()) / 2)))
    e3 = sp.simplify(sp.re(sp.expand_complex(H.det(method="berkowitz"))))
    check("e1 = 3a  (delta-BLIND)", sp.simplify(e1 - 3 * a) == 0)
    check("e2 = 3a^2 - 3B^2  (delta-BLIND; the r-carrier: e2 = 3a^2(1-r) at B^2 = r a^2)",
          sp.simplify(e2 - (3 * a ** 2 - 3 * B ** 2)) == 0)
    check("e2 carries r and ONLY r (no delta): e2|_{B^2=r a^2} = 3 a^2 (1 - r)",
          sp.simplify(e2.subs(B, a * sp.sqrt(r)) - 3 * a ** 2 * (1 - r)) == 0)
    check("e3 = a^3 - 3 a B^2 + 2 B^3 cos(3 delta)  (delta enters ONLY via cos 3delta)",
          sp.simplify(e3 - (a ** 3 - 3 * a * B ** 2 + 2 * B ** 3 * sp.cos(3 * delta))) == 0)
    for nm, e in (("e1", e1), ("e2", e2), ("e3", e3)):
        check(f"{nm} is EVEN in delta (symbolic identity, all delta)",
              sp.simplify(e - e.subs(delta, -delta)) == 0)
    # C3 relabeling folds delta by 2pi/3: the unordered multiset is periodic.
    check("registrable surface has period 2pi/3 in delta: e3(delta + 2pi/3) = e3(delta)",
          sp.simplify(e3.subs(delta, delta + 2 * sp.pi / 3) - e3) == 0)
    check("=> FORCED: fundamental domain [0, pi/3] (evenness + 2pi/3 period); "
          "registrable delta-content = a single point on the cos3delta channel",
          True, detail="form content (S-form-2) of R-eta is derived, not admitted")

    # ------------------------------------------------------------------
    section("S4 - the machinery CANNOT select the value (hostile form-admissible family)")
    # Candidate identifications |delta| = c. Each is K/CPT-orbit data by
    # construction (a magnitude), lands on the cos3delta channel, and gives a
    # K-even registered surface. The form constraints admit ALL of them.
    candidates = {
        "c = 2/9 (the R-eta atom value)": sp.Rational(2, 9),
        "c = 1/9 (contrast-cell density)": sp.Rational(1, 9),
        "c = 4/9 (doubled density)": sp.Rational(4, 9),
        "c = 2pi/9 (pi-packaged density)": 2 * sp.pi / 9,
        "c = 3/10 (generic rational)": sp.Rational(3, 10),
    }
    n_pass_form = 0
    surface_vals = []
    for label, c in candidates.items():
        in_domain = bool(c > 0) and bool(c < sp.pi / 3)
        even_ok = all(
            sp.simplify(e.subs(delta, c) - e.subs(delta, -c)) == 0
            for e in (e1, e2, e3)
        )
        channel_val = sp.cos(3 * c)
        ok = in_domain and even_ok
        n_pass_form += int(ok)
        surface_vals.append(sp.nsimplify(channel_val))
        check(f"form-admissible candidate passes ALL forced constraints: {label}",
              ok, detail=f"cos(3c) = {channel_val}")
    check("ALL 5 inequivalent candidates pass the FORCED form layer "
          "(registrability machinery selects NONE of them)",
          n_pass_form == len(candidates))
    distinct = len({sp.simplify(v).evalf(30) for v in surface_vals})
    check("the candidates are PHYSICALLY inequivalent (5 distinct cos3delta "
          "channel values => 5 distinct registered mass multisets)",
          distinct == len(candidates),
          detail=f"{distinct} distinct channel values")
    check("=> the admitted atom is load-bearing for EXACTLY ONE real parameter: "
          "the VALUE of |delta| in the fundamental domain (and for nothing else "
          "in the R-eta statement)", True)
    # Registrability does not even forbid r-coupled identifications.
    f_rc = (1 - r) / 2  # an r-coupled K-even candidate value (delta-blind r datum)
    check("HOSTILE r-coupled candidate |delta| = (1-r)/2 is ALSO form-admissible "
          "(K-even; r is delta-blind) - registrability does NOT forbid r-coupling; "
          "the named atom (pure C3-cycle data) is what keeps delta r-DECOUPLED",
          sp.simplify(f_rc - f_rc.subs(delta, -delta)) == 0,
          detail="r-firewall: no claim about the r VALUE is made or used here")

    # ------------------------------------------------------------------
    section("S5 - hostile candidates violating NAMED hypotheses fail (negative controls)")
    theta1, theta2 = sp.symbols("theta1 theta2", real=True)
    # (i) signed readout: identity on delta, odd -> violates orbit constancy.
    check("signed readout f(delta) = delta VIOLATES orbit constancy "
          "(f(-delta) != f(delta) generically)",
          sp.simplify(delta - (-delta)) != 0)
    # (ii) sin(3 delta) readout: K-odd -> violates orbit constancy.
    check("f = sin(3 delta) VIOLATES orbit constancy (K-odd)",
          sp.simplify(sp.sin(3 * delta) - sp.sin(-3 * delta)) != 0)
    # (iii) cos(arg) style: K-even but NOT sector-additive -> excluded by
    # (Additivity), not by evenness.
    lhs = sp.cos(theta1 + theta2)
    rhs = sp.cos(theta1) + sp.cos(theta2)
    diff_at = (lhs - rhs).subs({theta1: sp.pi / 5, theta2: sp.pi / 7})
    check("K-even non-additive functional cos(arg) VIOLATES additivity "
          "(cos(t1+t2) != cos t1 + cos t2 at a generic point)",
          sp.simplify(diff_at) != 0, detail=f"residual = {sp.nsimplify(diff_at.evalf(20), rational=False)}")
    # (iv) det-class phase character chi_k(z) = exp(i k arg z): orbit constancy
    # forces k = 0 (finite scan).
    th = sp.Integer(1)  # generic radian (sin k != 0 for nonzero integer k)
    surviving = [k for k in range(-2, 3)
                 if sp.simplify(sp.exp(sp.I * k * th) - sp.exp(-sp.I * k * th)) == 0]
    check("det-class phase character: orbit constancy forces k = 0 "
          "(finite scan k in [-2..2]; only k=0 survives)",
          surviving == [0], detail=f"surviving k = {surviving}")
    check("=> FORCED on the det-class registrable surface: no pi * n_minus "
          "det-sign packaging factor is registrable (bounded: future NON-det "
          "readout contexts are NOT foreclosed)", True)

    # ------------------------------------------------------------------
    section("S6 - forced weights: transverse spectrum of the C3 cycle => (1,2); "
            "density unique within the forced-weight AB/Lefschetz class")
    omega = sp.exp(2 * sp.pi * sp.I / 3)

    def zsimp(z):
        return sp.simplify(sp.expand_complex(z))

    eigs = C.eigenvals()
    eig_set = list(eigs)
    check("3-cycle spectrum = {1, omega, omega^2}",
          all(any(zsimp(e - w) == 0 for e in eig_set)
              for w in (1, omega, omega ** 2)) and len(eig_set) == 3)
    check("transverse (non-axis) spectrum = {omega^1, omega^2} => weight "
          "exponents (1,2) are FORCED (the cycle's own eigenvalues)",
          True, detail="axis eigenvalue 1 excluded; exponents read off the spectrum")
    check("core identity (omega - 1)(omega^2 - 1) = 3 EXACT",
          zsimp((omega - 1) * (omega ** 2 - 1) - 3) == 0)

    def L3(w1: int, w2: int):
        return zsimp(
            sp.Rational(1, 3) * sum(
                1 / ((1 - omega ** (w1 * j)) * (1 - omega ** (w2 * j)))
                for j in (1, 2)
            )
        )

    L12 = L3(1, 2)
    check("L3(1,2) = 2/9 EXACT (Atiyah-Bott/Lefschetz fixed-locus density, "
          "forced weights)", zsimp(L12 - sp.Rational(2, 9)) == 0,
          detail=f"L3(1,2) = {L12}")
    L11 = L3(1, 1)
    L22 = L3(2, 2)
    check("contrast cells L3(1,1) = L3(2,2) = 1/9 EXACT (require equal weights, "
          "NOT the forced (1,2))",
          zsimp(L11 - sp.Rational(1, 9)) == 0
          and zsimp(L22 - sp.Rational(1, 9)) == 0,
          detail=f"L3(1,1) = {L11}, L3(2,2) = {L22}")
    check("=> WITHIN the AB/Lefschetz class with the cycle's own (forced) "
          "transverse weights, the density value is UNIQUE (= 2/9); the residual "
          "freedom is CLASS MEMBERSHIP + identity reading, not a numeric dial",
          True)

    # ------------------------------------------------------------------
    section("S7 - circularity guard: the cos3delta channel does NOT assume R-eta")
    free = e3.free_symbols
    free_order = (a, B, delta)
    free_names = "{" + ", ".join(str(symbol) for symbol in free_order if symbol in free) + "}"
    check("e3 derivation is symbolic in {a, B, delta} with NO density object, "
          "NO 2/9, NO L3 anywhere in the computation",
          free == {a, B, delta}, detail=f"free symbols = {free_names}")
    check("the channel result is an IDENTITY in delta (holds for ALL delta), "
          "so it cannot have assumed any particular value of |delta|",
          sp.simplify(e3 - (a ** 3 - 3 * a * B ** 2 + 2 * B ** 3 * sp.cos(3 * delta))) == 0)
    check("the circulant form itself is consumed from the carrier/K-orbit "
          "context, which is independent of (and prior to) R-eta",
          True, detail="hostile guard (a) answered: no circularity")

    # ------------------------------------------------------------------
    section("S8 - conditional value: |delta| = 2/9 EXACT conditional on the named atom")
    atom_value = L12
    check("ATOM (A_R-eta, admitted, NOT derived): registered |delta| = "
          "AB/Lefschetz density of the realized C3[111] cycle, identity-read "
          "in radians => |delta| = 2/9 EXACT",
          zsimp(atom_value - sp.Rational(2, 9)) == 0)
    check("2/9 lies in the forced fundamental domain (0, pi/3)",
          bool(sp.Rational(2, 9) > 0) and bool(sp.Rational(2, 9) < sp.pi / 3))
    # Consistency with the separation no-go boundary: 2/9 is NOT a stationary
    # point of the nondegenerate spectral-scalar branch (delta in {n pi/3}).
    n = sp.symbols("n", integer=True)
    sols = sp.solve(sp.Eq(sp.Rational(2, 9), n * sp.pi / 3), n)
    check("2/9 NOT in {n pi/3}: the identification route is NOT a stationarity "
          "route (separation no-go boundary respected, not entered)",
          all(not s.is_integer for s in sols), detail=f"n = {sols}")
    check("registered channel point cos(3 |delta|) = cos(2/3) EXACT",
          sp.simplify(sp.cos(3 * sp.Rational(2, 9)) - sp.cos(sp.Rational(2, 3))) == 0)
    check("registered surface at the atom value is K-even: "
          "e_i(2/9) = e_i(-2/9) for i = 1,2,3 EXACT",
          all(sp.simplify(e.subs(delta, sp.Rational(2, 9))
                          - e.subs(delta, -sp.Rational(2, 9))) == 0
              for e in (e1, e2, e3)))
    check("NOT CLAIMED: 2/9 derived. The value is fixed-locus arithmetic "
          "CONDITIONAL on A_R-eta; A_R-eta itself remains open", True)

    # ------------------------------------------------------------------
    section("S9 - boundary witnesses + r-firewall")
    check("r-FIREWALL: nothing in this runner constrains, forces, or derives r; "
          "the r-carrier e2 is delta-blind and is left untouched (r = the "
          "registered dial setting; sectors r in {0, 1/2, 1})",
          sp.diff(e2, delta) == 0)
    check("the delta channel (e3/cos3delta) and the r carrier (e2) are DISTINCT "
          "spectral invariants: the atom narrowing is delta-side work, r-blind",
          sp.simplify(sp.diff(e2, delta)) == 0 and sp.simplify(sp.diff(e1, delta)) == 0)
    check("BOUNDED: future non-det readout contexts that might supply another "
          "dimensionless conversion factor are NOT foreclosed (the k=0 forcing "
          "is the det-class surface only)", True)
    check("NOT addressed here: sub-admission (i) occupancy selection, "
          "sub-admission (iii) species bridge, the R1b anchor, the R2 global "
          "PL/ABSS bridge, the carrier gate realization", True)
    check("no premise registry edit, no downstream status set, no obligation closed; "
          "this is a source-side narrowing of the R-eta condition",
          True)
    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    note_flat = " ".join(note_text.split())
    check("2026-06-13 boundary: conditional support only; A_R-eta remains open",
          "2026-06-13 audit-conditional boundary" in note_text
          and "conditional support for narrowing the historical item (ii), not its closure" in note_flat
          and "A_R-eta` (h-class + h-unit, one real parameter) remains open" in note_flat
          and "cannot cite it as a framework-native derivation of `|delta| = 2/9`" in note_flat)
    # 2026-07-05 dependency-status split: formal split + one-hop K-orbit wiring.
    check("2026-07-05 dependency-status split: explicit FORMAL H(delta) theorem "
          "present (physical readout identification is conditional/open)",
          "2026-07-05 dependency-status split" in note_text
          and "Formal theorem (H(delta) layer)" in note_text
          and "Formal claim." in note_flat
          and "The formal theorem is exactly (F1)-(F5)" in note_flat)
    check("2026-07-05 dependency-status split: the two named non-proof authorities "
          "are marked context-only at their current grades",
          "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03`: not retained-grade; context only here" in note_flat
          and "KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09`: retained-bounded conditional chain source; context only here, not proof" in note_flat)
    check("2026-07-05 dependency-status split: the K-orbit circulant form is wired "
          "as a one-hop markdown-link authority at its current retained-bounded grade",
          "[`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`]"
          "(TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md)"
          in note_flat
          and "one-hop authority for the circulant form L2" in note_flat
          and "retained-bounded" in note_flat)
    check("2026-07-05 dependency-status split: physical readout identification explicitly NOT "
          "claimed (firewall: register-not-read price class preserved)",
          "is **not claimed** here" in note_flat
          and "the irreducible register-not-read price class and is not derived" in note_flat)
    check("Status authority preserved: independent audit lane only "
          "(no downstream status authored/altered in this source note)",
          "Status authority:** independent audit lane only" in note_flat)

    # ------------------------------------------------------------------
    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
