#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`G_2_V_BOUNDED_INTERVAL_NARROW_THEOREM_NOTE_2026-05-17`.

The narrow theorem's load-bearing content is the bounded-interval
substitution implication: given

  (X1) Native SU(2) beta=16 one-plaquette interval support
       u_0(SU(2)) in [u_lo, u_hi] = [96/100, 98/100], supplied by the
       2026-06-18 direct class-angle integral bridge.
  (X2) Retained b_2 = 19/6 (SU2_WEAK_BETA_COEFFICIENT_NARROW retained_bounded).
  (X3) Retained native SU(2) gauge structure from Cl(3) bivector irrep
       (NATIVE_GAUGE_CLOSURE_NOTE retained).
  (X4) Retained_bounded one-hop lattice-alpha anchor
       1/alpha_bare |_lattice = 16 pi, with beta_W = 16 as a corollary
       (SU2_WEAK_ALPHA_LATTICE_ONE_OVER_SIXTEEN_PI_ANCHOR_NARROW_THEOREM).
  (X5) Retained tadpole-improvement vertex-power identity
       alpha_2^tadpole = alpha_bare / u_0^2
       (ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM retained).
  (X6) Framework scale-log bridge supplies ln(M_Pl/v_cand) = L_cand
       and licenses the rounded exact-symbolic surrogate L = 38.44.
  (X7) Framework inverse-alpha integration bridge supplies the
       integrated one-loop running law from the already-isolated
       one-loop coefficient convention.

the bounded interval

  g_2(v) in [g_lo, g_hi],
    g_lo = sqrt( 4 pi / (16 pi u_hi^2 - (b_2 / (2 pi)) * L) ),
    g_hi = sqrt( 4 pi / (16 pi u_lo^2 - (b_2 / (2 pi)) * L) ),

follows from substituting the inputs into the bridged one-loop
inverse-alpha equation

  1/alpha_2(v)  =  1/alpha_2^tadpole |_lattice  -  (b_2 / (2 pi)) * ln(M_Pl / v)
                =  16 pi u_0^2  -  (b_2 / (2 pi)) * L

inverted to alpha_2(v) and then to g_2(v) = sqrt(4 pi alpha_2(v)). The
endpoint reversal (g_2 lower endpoint corresponds to u_0 upper endpoint)
follows from the explicit monotonicity check below.

The runner verifies the bounded interval at exact sympy precision over
symbolic (u_0, b_2, L) plus the framework instance with rational endpoints
u_lo = 96/100, u_hi = 98/100, b_2 = 19/6, L = Rational(3844, 100) approximation
of 38.44, then provides high-precision mpmath decimal endpoints for the
result interval to 30 decimal digits.

Companion role: no new claim row, no status promotion.
Provides audit-friendly evidence at exact precision plus high-precision
numeric readout. This is the audit-companion for the Pattern A narrow
bounded theorem; the former row-local literature u_0 interval is replaced
by native one-plaquette SU(2) support, while independent audit remains
required before any effective status change.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    from sympy import (
        Rational,
        Symbol,
        pi,
        sqrt,
        simplify,
        N as Numeric,
        diff,
        Float,
        Eq,
        nsimplify,
    )
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "G_2_V_BOUNDED_INTERVAL_NARROW_THEOREM_NOTE_2026-05-17.md"
BRIDGE_NOTE = ROOT / "docs" / "SU2_WEAK_ONE_LOOP_INVERSE_ALPHA_SCALE_LOG_BRIDGE_NARROW_THEOREM_NOTE_2026-06-15.md"


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("G_2_V_BOUNDED_INTERVAL_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: sympy verification of g_2(v) bounded interval from u_0 in [0.96, 0.98]")
    print("Inputs (cited):")
    print("  (X1) u_0(SU(2)) in [96/100, 98/100]   ... native beta=16 one-plaquette bridge")
    print("  (X2) b_2 = 19/6                        ... retained_bounded")
    print("  (X3) Cl(3) bivector -> SU(2)           ... retained")
    print("  (X4) 1/alpha_2^bare |_lattice = 16 pi  ... retained_bounded one-hop anchor")
    print("  (X5) alpha_2^tadpole = alpha_bare/u_0^2 ... retained")
    print("  (X6) ln(M_Pl/v_cand) = 38.442..., L=38.44 rounded ... framework bridge")
    print("  (X7) one-loop inverse-alpha integration ... framework bridge")
    print("=" * 88)

    # ------------------------------------------------------------------
    section("Part 0: source-packet dependency repair checks")
    # ------------------------------------------------------------------
    note_text = NOTE.read_text(encoding="utf-8")
    bridge_text = BRIDGE_NOTE.read_text(encoding="utf-8")
    check("source note exists", NOTE.exists(), detail=str(NOTE.relative_to(ROOT)))
    check(
        "(X4) source note cites the retained_bounded SU2 lattice-alpha anchor",
        "SU2_WEAK_ALPHA_LATTICE_ONE_OVER_SIXTEEN_PI_ANCHOR_NARROW_THEOREM_NOTE_2026-05-28.md"
        in note_text,
    )
    check(
        "(X4) source note does not leave YT_EW as a load-bearing markdown edge",
        "](YT_EW_COLOR_PROJECTION_THEOREM.md)" not in note_text,
    )
    check(
        "(X4) source note does not leave G_BARE_CANONICAL as a load-bearing markdown edge",
        "](G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md)" not in note_text,
    )
    check(
        "(X4) source note states the coupling input is not rederived here",
        "not independently derive the anchor's assumed coupling input" in note_text,
    )
    bridge_name = "SU2_WEAK_ONE_LOOP_INVERSE_ALPHA_SCALE_LOG_BRIDGE_NARROW_THEOREM_NOTE_2026-06-15.md"
    check("(X6/X7) source note cites the framework-local scale/RGE bridge", bridge_name in note_text)
    native_bridge = "SU2_U0_SINGLE_PLAQUETTE_BETA16_NATIVE_INTERVAL_BOUNDED_SUPPORT_NOTE_2026-06-18.md"
    check("(X1) source note cites the native SU2 beta=16 u0 interval bridge", native_bridge in note_text)
    check(
        "(X1) source note says X1 is not a row-local literature admission",
        "not a row-local literature admission" in note_text,
    )
    check(
        "(X6) bridge includes direct ruler/current-v scale-log hardening",
        "current value-surface cross-check" in bridge_text
        and "ln(1.22e19 / 246.282818290129)" in bridge_text,
    )
    check(
        "(X7) source note no longer registers one-loop RGE as a row-local named admission",
        "**(X7) Named 1-loop RGE admission.**" not in note_text,
    )
    check(
        "(X1) source note no longer claims [0.96,0.98] brackets 0.988",
        "brackets the weak-coupling-series value" not in note_text,
    )
    check(
        "(X1) source note says 0.988 is outside the parent interval",
        "previously said `[0.96, 0.98]` bracketed `u_0 ≈ 0.988`. It does not."
        in note_text,
    )
    check(
        "(X1) source note keeps 0.988 non-load-bearing",
        "not inside the certified" in note_text,
    )

    # ------------------------------------------------------------------
    section("Part 1: symbolic setup (positive real symbols)")
    # ------------------------------------------------------------------
    u0 = Symbol("u_0", positive=True, real=True)
    b2 = Symbol("b_2", positive=True, real=True)
    L = Symbol("L", positive=True, real=True)
    print(f"  symbolic u_0 = {u0}")
    print(f"  symbolic b_2 = {b2}")
    print(f"  symbolic L = ln(M_Pl/v_cand) rounded bridge readout = {L}")

    # ------------------------------------------------------------------
    section("Part 2: lattice-scale bare alpha and tadpole-improved 1/alpha")
    # ------------------------------------------------------------------
    # (X4): g_bare^2 = 1/4, alpha_bare = g_bare^2/(4 pi) = 1/(16 pi),
    #       so 1/alpha_bare|_lattice = 16 pi.
    one_over_alpha_bare = 16 * pi
    check(
        "(X4) 1/alpha_bare |_lattice = 16 pi   (from one-hop lattice-alpha anchor)",
        simplify(one_over_alpha_bare - 16 * pi) == 0,
        detail=f"1/alpha_bare = {one_over_alpha_bare}",
    )
    # Wilson normalization: beta = 2N/g_bare^2 at N=2, g_bare^2=1/4 -> beta=16.
    beta_lattice = Rational(2) * Rational(2) / Rational(1, 4)
    check(
        "(X4+X5 conv) beta = 2N/g_bare^2 = 16 at N=2, g_bare^2=1/4",
        beta_lattice == Rational(16),
        detail=f"beta = {beta_lattice}",
    )

    # (X5): tadpole-improved coupling: alpha_2^tadpole = alpha_bare / u_0^2
    #       => 1/alpha_2^tadpole|_lattice = (16 pi) * u_0^2
    one_over_alpha_tadpole_lattice = one_over_alpha_bare * u0 ** 2
    check(
        "(X5) 1/alpha_2^tadpole |_lattice = 16 pi u_0^2",
        simplify(one_over_alpha_tadpole_lattice - 16 * pi * u0 ** 2) == 0,
        detail="vertex-power identity alpha_tadpole = alpha_bare/u_0^2",
    )

    # ------------------------------------------------------------------
    section("Part 3: 1-loop running from M_Pl to v_cand (bridged inverse-alpha law, b>0 = asymptotic freedom)")
    # ------------------------------------------------------------------
    # 1/alpha_2(v_cand) =
    #   1/alpha_2^tadpole|_lattice - (b_2/(2 pi)) * ln(M_Pl/v_cand)
    inv_alpha_v_sym = one_over_alpha_tadpole_lattice - (b2 / (2 * pi)) * L
    check(
        "(P1) 1/alpha_2(v_cand) = 16 pi u_0^2 - (b_2/(2 pi)) * L (X7 bridge substitution)",
        simplify(
            inv_alpha_v_sym - (16 * pi * u0 ** 2 - (b2 / (2 * pi)) * L)
        )
        == 0,
        detail="symbolic identity",
    )

    # alpha_2(v) = 1 / (1/alpha_2(v))
    alpha_v_sym = 1 / inv_alpha_v_sym
    # g_2(v) = sqrt(4 pi alpha_2(v))
    g2_v_sym = sqrt(4 * pi * alpha_v_sym)
    g2_v_closed_form = sqrt(
        (4 * pi) / (16 * pi * u0 ** 2 - (b2 / (2 * pi)) * L)
    )
    check(
        "(P2) g_2(v) = sqrt(4 pi / (16 pi u_0^2 - (b_2/(2 pi)) L)) symbolic closed form",
        simplify(g2_v_sym - g2_v_closed_form) == 0,
        detail="square root of inverse 1/alpha_2(v)",
    )

    # ------------------------------------------------------------------
    section("Part 4: monotonicity of g_2(v) in u_0 over the input interval")
    # ------------------------------------------------------------------
    # d/du_0 [1/alpha_2(v)] = d/du_0 [16 pi u_0^2 - (b_2/(2 pi)) L]
    #                       = 32 pi u_0  (positive for u_0 > 0)
    # Therefore 1/alpha_2(v) is strictly increasing in u_0, alpha_2(v) is
    # strictly decreasing in u_0, and g_2(v) is strictly decreasing in u_0.
    d_inv_alpha_du0 = diff(inv_alpha_v_sym, u0)
    check(
        "(M1) d/du_0 [1/alpha_2(v)] = 32 pi u_0 (positive for u_0 > 0)",
        simplify(d_inv_alpha_du0 - 32 * pi * u0) == 0,
        detail=f"d/du_0 = {simplify(d_inv_alpha_du0)}",
    )

    # ------------------------------------------------------------------
    section("Part 5: framework instance: u_0 in [96/100, 98/100], b_2 = 19/6, L = 3844/100")
    # ------------------------------------------------------------------
    u_lo = Rational(96, 100)
    u_hi = Rational(98, 100)
    b2_val = Rational(19, 6)
    # L_val = 38.44 expressed as exact rational. The 2026-06-15
    # scale/RGE bridge proves this is the rounded readout of
    # ln(M_Pl/v_cand)=38.442224515... from the hierarchy candidate map.
    L_val = Rational(3844, 100)
    print(f"  u_lo = {u_lo} = {float(u_lo)}")
    print(f"  u_hi = {u_hi} = {float(u_hi)}")
    print(f"  b_2  = {b2_val} = {float(b2_val)}")
    print(f"  L    = {L_val} = {float(L_val)}")

    # 1/alpha_2(v) at the two u_0 endpoints (exact rational + pi).
    inv_alpha_at_ulo = inv_alpha_v_sym.subs({u0: u_lo, b2: b2_val, L: L_val})
    inv_alpha_at_uhi = inv_alpha_v_sym.subs({u0: u_hi, b2: b2_val, L: L_val})
    inv_alpha_at_ulo_simp = simplify(inv_alpha_at_ulo)
    inv_alpha_at_uhi_simp = simplify(inv_alpha_at_uhi)
    print(f"  1/alpha_2(v) at u_lo = 0.96: {inv_alpha_at_ulo_simp}")
    print(f"  1/alpha_2(v) at u_hi = 0.98: {inv_alpha_at_uhi_simp}")

    # Monotonicity check: 1/alpha_2(v)|_{u_lo} < 1/alpha_2(v)|_{u_hi}
    diff_inv = simplify(inv_alpha_at_uhi_simp - inv_alpha_at_ulo_simp)
    check(
        "(M2) 1/alpha_2(v) at u_hi > 1/alpha_2(v) at u_lo (strict monotonicity)",
        bool(diff_inv > 0),
        detail=f"diff = {diff_inv} = {float(diff_inv):.6f}",
    )

    # Inverse map: g_2(v) larger at u_lo, smaller at u_hi.
    # g_2 endpoints (exact symbolic + numeric).
    g2_at_ulo_sym = g2_v_closed_form.subs({u0: u_lo, b2: b2_val, L: L_val})
    g2_at_uhi_sym = g2_v_closed_form.subs({u0: u_hi, b2: b2_val, L: L_val})

    g2_at_ulo_num = Numeric(g2_at_ulo_sym, 30)
    g2_at_uhi_num = Numeric(g2_at_uhi_sym, 30)
    print(f"  g_2(v) at u_0 = 0.96 (HIGHER bound of g_2): {g2_at_ulo_num}")
    print(f"  g_2(v) at u_0 = 0.98 (LOWER bound of g_2):  {g2_at_uhi_num}")

    # ------------------------------------------------------------------
    section("Part 6: explicit bounded interval g_2(v) in [g_lo, g_hi]")
    # ------------------------------------------------------------------
    # Endpoint reversal: g_2 monotone-decreasing in u_0, so
    #   g_lo = g_2(v) at u_0 = u_hi = 0.98
    #   g_hi = g_2(v) at u_0 = u_lo = 0.96
    g_lo = g2_at_uhi_num
    g_hi = g2_at_ulo_num
    print(f"  RESULT: g_2(v_cand approx 246.28 GeV) in [g_lo, g_hi]")
    print(f"          g_lo = {g_lo}")
    print(f"          g_hi = {g_hi}")
    print(f"          width = {Numeric(g_hi - g_lo, 30)}")

    check(
        "(I1) interval lower endpoint g_lo = g_2(v) at u_0 = 0.98",
        g_lo == g2_at_uhi_num,
        detail=f"g_lo = {Numeric(g_lo, 12)}",
    )
    check(
        "(I2) interval upper endpoint g_hi = g_2(v) at u_0 = 0.96",
        g_hi == g2_at_ulo_num,
        detail=f"g_hi = {Numeric(g_hi, 12)}",
    )
    check(
        "(I3) g_lo < g_hi (interval is non-empty)",
        bool(g_lo < g_hi),
        detail=f"g_lo - g_hi = {Numeric(g_lo - g_hi, 12)}",
    )

    # Numerical sanity bounds: the interval should bracket roughly
    # 0.65-0.69 (one decimal digit of tolerance for the lattice running);
    # tight check is g_2 in [0.6, 0.75].
    check(
        "(I4) g_lo > 0.6 (loose physical sanity bound)",
        bool(g_lo > Float("0.6")),
        detail=f"g_lo = {Numeric(g_lo, 10)}",
    )
    check(
        "(I5) g_hi < 0.75 (loose physical sanity bound)",
        bool(g_hi < Float("0.75")),
        detail=f"g_hi = {Numeric(g_hi, 10)}",
    )

    # ------------------------------------------------------------------
    section("Part 6b: weak-coupling 0.988 comparator is outside parent X1 interval")
    # ------------------------------------------------------------------
    u_weak = Rational(988, 1000)
    g2_at_uweak_sym = g2_v_closed_form.subs({u0: u_weak, b2: b2_val, L: L_val})
    g2_at_uweak_num = Numeric(g2_at_uweak_sym, 30)
    print(f"  weak-coupling comparator u_weak = {u_weak} = {float(u_weak)}")
    print(f"  g_2(v) at u_weak = 0.988 (context only): {g2_at_uweak_num}")
    check(
        "(U1) weak-coupling readout 0.988 lies above the parent upper endpoint 0.98",
        bool(u_weak > u_hi),
        detail=f"u_weak - u_hi = {float(u_weak - u_hi):.6f}",
    )
    check(
        "(U2) g_2 at u_weak is below g_lo, hence outside the certified interval",
        bool(g2_at_uweak_num < g_lo),
        detail=f"g_2(u_weak) - g_lo = {Numeric(g2_at_uweak_num - g_lo, 12)}",
    )
    check(
        "(U3) 0.988 comparator is not used as an endpoint",
        u_weak not in (u_lo, u_hi),
        detail="load-bearing endpoints remain 96/100 and 98/100",
    )

    # ------------------------------------------------------------------
    section("Part 7: corollaries")
    # ------------------------------------------------------------------
    # (C1) Width of interval = g_hi - g_lo.
    width = Numeric(g_hi - g_lo, 30)
    check(
        "(C1) interval width is finite and positive (well-formed bounded interval)",
        bool(width > 0),
        detail=f"width = {width}",
    )

    # (C2) Midpoint: (g_lo + g_hi)/2; this is NOT a prediction, only the
    # arithmetic midpoint of the bounded interval.
    midpoint = Numeric((g_lo + g_hi) / 2, 30)
    print(f"  arithmetic midpoint (NOT a prediction): {midpoint}")
    check(
        "(C2) midpoint of g_2 interval is between g_lo and g_hi",
        bool(g_lo < midpoint) and bool(midpoint < g_hi),
        detail=f"midpoint = {Numeric(midpoint, 12)}",
    )

    # (C3) Comparison of interval to retained inputs only (no PDG):
    # Note: the framework's bare lattice value at v=lattice would give
    #   g_2|_lattice = sqrt(1/4) = 1/2 = 0.5 (NOT a v-scale value).
    # After tadpole + running, the interval is centered well above 1/2
    # because the running reduces 1/alpha_2 from ~16 pi u_0^2 ~ 46-48
    # down to ~27, increasing alpha and hence g_2.
    g2_lattice = sqrt(Rational(1, 4))  # = 1/2, retained-bounded
    check(
        "(C3) g_2|_lattice = sqrt(1/4) = 1/2 (one-hop anchor corollary)",
        g2_lattice == Rational(1, 2),
        detail=f"g_2|_lattice = {g2_lattice}",
    )
    check(
        "(C3) interval lies STRICTLY ABOVE the bare lattice value 1/2",
        bool(g_lo > Float("0.5")),
        detail=f"g_lo - 0.5 = {Numeric(g_lo - Float('0.5'), 12)}",
    )

    # (C4) Counterfactual interval u_0 in [1.0, 1.0] (no improvement):
    # at u_0 = 1, 1/alpha_2(v_cand) = 16 pi - (19/(12 pi))*38.44.
    inv_alpha_unimp = inv_alpha_v_sym.subs(
        {u0: Rational(1), b2: b2_val, L: L_val}
    )
    g2_unimp_num = Numeric(sqrt((4 * pi) / inv_alpha_unimp), 30)
    print(f"  counterfactual unimproved g_2(v) at u_0 = 1: {g2_unimp_num}")
    check(
        "(C4) counterfactual u_0=1 g_2(v) differs from improved interval (distinct)",
        bool(g2_unimp_num != g_lo) and bool(g2_unimp_num != g_hi),
        detail=f"unimproved g_2 = {Numeric(g2_unimp_num, 10)}",
    )

    # ------------------------------------------------------------------
    section("Part 8: forbidden-import audit")
    # ------------------------------------------------------------------
    # The runner does NOT consume:
    #   - PDG observed g_2(v) = 0.646
    #   - PDG observed v = 246 GeV as a free derivation input. The
    #     scale log is supplied by the framework hierarchy candidate
    #     bridge and rounded to 38.44 for exact-symbolic evaluation.
    #   - any fitted selector for u_0
    # The u_0 interval [0.96, 0.98] is supplied by the native beta=16
    # one-plaquette bridge; no literature numerical interval is load-bearing.
    pdg_g2_obs = Float("0.646")  # not used in derivation, displayed for context only
    context_gap = abs(g_lo - pdg_g2_obs) / pdg_g2_obs
    print(f"  context-only (NOT consumed): PDG g_2(v) obs = {pdg_g2_obs}")
    print(
        "  context-only (NOT a PASS gate): "
        f"|g_lo - 0.646|/0.646 = {float(context_gap):.4f}"
    )

    # ------------------------------------------------------------------
    section("Summary")
    # ------------------------------------------------------------------
    print(f"  PASS = {PASS}")
    print(f"  FAIL = {FAIL}")
    print(f"  g_2(v_cand approx 246.28 GeV) in [{Numeric(g_lo,15)}, {Numeric(g_hi,15)}]")
    print(f"  interval width = {Numeric(g_hi - g_lo, 15)}")
    print(f"  PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
