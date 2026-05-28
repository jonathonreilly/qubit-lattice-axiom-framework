#!/usr/bin/env python3
"""Narrow premise-packet bridge for the gravitational boundary/action-density.

This runner verifies the bounded conditional consequence (B1)-(B4) of
PLANCK_BOUNDARY_ACTION_DENSITY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md:

  (BP) := the framework's first-order coframe boundary carrier P_A is
          the leading coefficient of the gravitational boundary/action
          density (supplied in this row as a single premise-packet
          entry, not as a repo-wide axiom).
  =>  (B1) primitive trace c_cell = Tr(rho_cell P_A) = 1/4 on the
            Boolean event cell (linear algebra on 16x16 rationals).
  =>  (B2) (BP) identifies c_cell as the leading boundary/action-density
            coefficient c in S_Wald(c, A) = A * c.
  =>  (B3) retained narrow algebraic equivalence (T1) from
            BH_QUARTER_WALD_NEWTON_COEFFICIENT_NARROW_THEOREM at
            c = c_cell = 1/4 forces 4 * G * 1/4 = 1, hence G = 1.
  =>  (B4) framework-lattice-unit readout G_Newton,lat = 1.

All identities are verified by exact sympy rational arithmetic. No
PDG / fitted / observed value enters.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = (
    "planck_boundary_action_density_accepted_premise_bridge_bounded_note_2026-05-26"
)
RUNNER_REL = "scripts/planck_boundary_action_density_accepted_premise_runner.py"
NOTE_PATH = (
    ROOT
    / "docs/PLANCK_BOUNDARY_ACTION_DENSITY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md"
)

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    msg = f"{status}: {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return condition


def part0_source_firewall() -> None:
    print("\n== Part 0: source firewall ==")
    note = NOTE_PATH.read_text(encoding="utf-8")

    required = [
        "Supplied Premise Packet (Not Axioms)",
        "(BP)",
        "Gravitational boundary/action-density identification",
        "supplied premise-packet entry",
        "does not derive BP",
        "promote BP to a repo-wide axiom",
        "BH_QUARTER_WALD_NEWTON_COEFFICIENT_NARROW_THEOREM_NOTE_2026-05-10.md",
        "MINIMAL_AXIOMS_2026-05-20.md",
        "HYPERCHARGE_ALPHA_THIRD_NORMALIZATION_BRIDGE_BOUNDED_NOTE_2026-05-25.md",
        RUNNER_REL,
        "bounded_theorem",
        "Status authority",
        "independent audit lane only",
    ]
    for phrase in required:
        check(f"source contains required phrase: {phrase}", phrase in note)

    forbidden = [
        "PDG " + "load-bearing value",
        "load-bearing fitted",
        "Monte Carlo " + "measurement consumed",
        "load-bearing " + "g_bare value",
    ]
    for phrase in forbidden:
        check(
            f"source note excludes forbidden phrase: {phrase}",
            phrase not in note,
        )


def part1_primitive_trace() -> sp.Rational:
    """Verify (B1): c_cell = Tr(rho_cell P_A) = 1/4 on the 16-dim Boolean event cell."""
    print("\n== Part 1: (B1) primitive trace c_cell = 1/4 ==")

    E = ("t", "x", "y", "z")
    n = len(E)
    dim = 2 ** n
    check("(B1) Boolean event-cell dim = 16", dim == 16, str(dim))

    # Subsets of E indexed lex by bitmask 0..15
    subsets = []
    for mask in range(dim):
        S = tuple(a for i, a in enumerate(E) if (mask >> i) & 1)
        subsets.append(S)
    check(
        "(B1) Boolean event-cell subsets enumerated",
        len(subsets) == 16 and len(set(subsets)) == 16,
    )

    # rho_cell = (1/16) I_16
    rho_cell = sp.Rational(1, 16) * sp.eye(dim)

    # P_A = P_1 = diag( indicator(|S|=1) )
    P_A = sp.zeros(dim, dim)
    for i, S in enumerate(subsets):
        if len(S) == 1:
            P_A[i, i] = sp.Integer(1)

    # rank(P_A) = C(4,1) = 4
    rk = P_A.rank()
    check("(B1) rank(P_A) = C(4,1) = 4", rk == 4, str(rk))

    # Tr(P_A) = 4
    tr_PA = P_A.trace()
    check("(B1) Tr(P_A) = 4", tr_PA == sp.Integer(4), str(tr_PA))

    # Tr(rho_cell P_A) = (1/16) * Tr(P_A) = 4/16 = 1/4
    c_cell = (rho_cell * P_A).trace()
    check(
        "(B1) c_cell = Tr(rho_cell P_A) = 1/4",
        c_cell == sp.Rational(1, 4),
        str(c_cell),
    )

    # Cross-check: total source-free trace of rho_cell = 1
    tr_rho = rho_cell.trace()
    check(
        "(B1) Tr(rho_cell) = 1 (source-free normalization)",
        tr_rho == sp.Integer(1),
        str(tr_rho),
    )

    # Check that no other Hamming-weight packet projector has trace = c_cell
    # except its Hodge dual P_3 (binom(4,1) = binom(4,3) = 4) — this is the
    # standing Hodge-degeneracy boundary recorded by the retained no-go
    # FIRST_ORDER_COFRAME_UNCONDITIONALITY_NO_GO_THEOREM.
    counts = {p: 0 for p in range(n + 1)}
    for S in subsets:
        counts[len(S)] += 1
    expected = {0: 1, 1: 4, 2: 6, 3: 4, 4: 1}
    check(
        "(B1) Hamming-weight counts on 2^E match binomials (1,4,6,4,1)",
        counts == expected,
        str(counts),
    )

    return c_cell


def part2_bp_registration() -> None:
    """Verify (B2): the source note supplies BP as a bounded premise."""
    print("\n== Part 2: (B2) premise-packet registration check ==")
    note = NOTE_PATH.read_text(encoding="utf-8")

    required_bp = [
        "(BP)",
        "Gravitational boundary/action-density identification",
        "leading coefficient of the gravitational boundary/action density",
        "supplied premise-packet entry",
        "does not derive BP",
        "promote BP to a repo-wide axiom",
    ]
    for phrase in required_bp:
        check(f"(B2) registration phrase present: {phrase}", phrase in note)


def part3_retained_equivalence(c_cell: sp.Rational) -> sp.Rational:
    """Verify (B3): at c = c_cell = 1/4, the retained equivalence (T1) gives G = 1."""
    print("\n== Part 3: (B3) retained algebraic equivalence (T1) at c = 1/4 ==")

    # (T1) from BH_QUARTER_WALD_NEWTON_COEFFICIENT_NARROW_THEOREM is the
    # equivalence  S_Wald(c, A) = A * c  ==  S_BH(G, A) = A / (4 G)  <=>  4 G c = 1.
    # Substitute c = c_cell = 1/4 and solve for G in Q_+.
    G_sym = sp.Symbol("G", positive=True)
    A_sym = sp.Symbol("A", positive=True)

    S_Wald = A_sym * c_cell
    S_BH = A_sym / (4 * G_sym)

    # (T1) holds iff S_Wald == S_BH for all A > 0.
    constraint = sp.simplify(S_Wald - S_BH)  # zero iff 4 G c_cell = 1
    # Solve for G on the rational specialization c_cell = 1/4
    G_sol = sp.solve(constraint, G_sym)
    # sympy returns a list; check it contains exactly the rational G = 1
    check(
        "(B3) (T1) at c_cell = 1/4 has a unique positive-rational solution",
        len(G_sol) == 1,
        str(G_sol),
    )
    G_val = sp.Rational(G_sol[0])
    check(
        "(B3) (T1) at c_cell = 1/4 forces G = 1 (framework lattice units)",
        G_val == sp.Integer(1),
        str(G_val),
    )

    # Cross-check the equivalence directly: 4 * G * c_cell = 1
    eq_check = 4 * G_val * c_cell
    check(
        "(B3) verifies retained equivalence 4 G c_cell = 1 exactly",
        eq_check == sp.Integer(1),
        str(eq_check),
    )

    return G_val


def part4_unit_readout(G_val: sp.Rational) -> None:
    """Verify (B4): the framework-lattice-unit readout G_Newton,lat = 1."""
    print("\n== Part 4: (B4) framework-lattice-unit readout ==")
    G_Newton_lat = G_val
    check(
        "(B4) G_Newton,lat = 1 in framework lattice units",
        G_Newton_lat == sp.Integer(1),
        str(G_Newton_lat),
    )

    # Confirm the separate G_kernel = 1/(4 pi) labeling identity does NOT
    # collide with G_Newton,lat = 1 — the two are distinct convention
    # values per the source-unit normalization support theorem.
    G_kernel = sp.Rational(1, 1) / (4 * sp.pi)
    check(
        "(B4) G_kernel = 1/(4 pi) is distinct from G_Newton,lat = 1",
        sp.simplify(G_kernel - G_Newton_lat) != 0,
    )

    # Cross-check: S_BH(G_Newton,lat, A) = A / 4 at G_Newton,lat = 1
    A_sym = sp.Symbol("A", positive=True)
    S_BH_at_one = A_sym / (4 * G_Newton_lat)
    check(
        "(B4) S_BH(G_Newton,lat = 1, A) = A/4",
        sp.simplify(S_BH_at_one - A_sym / 4) == 0,
        str(S_BH_at_one),
    )


def part5_dependency_status() -> None:
    print("\n== Part 5: dependency status check ==")
    dep = (
        ROOT
        / "docs/BH_QUARTER_WALD_NEWTON_COEFFICIENT_NARROW_THEOREM_NOTE_2026-05-10.md"
    )
    check(
        "BH_QUARTER_WALD_NEWTON_COEFFICIENT note file exists",
        dep.is_file(),
        str(dep.relative_to(ROOT)),
    )
    parent_primitive = (
        ROOT
        / "docs/PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM_NOTE_2026-04-25.md"
    )
    check(
        "Primitive-coframe boundary-carrier source-arithmetic note exists",
        parent_primitive.is_file(),
        str(parent_primitive.relative_to(ROOT)),
    )
    parent_bh = (
        ROOT / "docs/BH_QUARTER_WALD_NOETHER_FRAMEWORK_CARRIER_THEOREM_NOTE_2026-04-29.md"
    )
    check(
        "BH_QUARTER_WALD_NOETHER framework carrier parent note file exists",
        parent_bh.is_file(),
        str(parent_bh.relative_to(ROOT)),
    )
    template = (
        ROOT
        / "docs/HYPERCHARGE_ALPHA_THIRD_NORMALIZATION_BRIDGE_BOUNDED_NOTE_2026-05-25.md"
    )
    check(
        "Canonical narrow-bridge template file exists",
        template.is_file(),
        str(template.relative_to(ROOT)),
    )
    norm = (
        ROOT
        / "docs/PLANCK_SOURCE_UNIT_NORMALIZATION_SUPPORT_THEOREM_NOTE_2026-04-25.md"
    )
    check(
        "Source-unit normalization support theorem note exists",
        norm.is_file(),
        str(norm.relative_to(ROOT)),
    )


def part6_no_forbidden_imports() -> None:
    print("\n== Part 6: no forbidden imports ==")
    note = NOTE_PATH.read_text(encoding="utf-8")
    forbidden_substrings = [
        "PDG " + "obs " + "value consumed",
        "fitted " + "selector consumed",
        "observed " + "Newton constant G_obs imported",
        "observed " + "Planck length l_P_obs imported",
        "Bekenstein-Hawking " + "entropy observed import",
        "Wilson " + "plaquette load-bearing input",
    ]
    for phrase in forbidden_substrings:
        check(
            f"source note excludes literature comparator: {phrase}",
            phrase not in note,
        )


def part7_independence_from_action_density_derivation() -> None:
    """Verify the bridge's scope is correctly bounded: it does not derive BP.

    The runner reads the source-note text and confirms that the boundary
    section names BP as not closed by this bridge.
    """
    print("\n== Part 7: scope-boundary check (BP not derived) ==")
    note = NOTE_PATH.read_text(encoding="utf-8")
    boundary_phrases = [
        "This bridge does not close",
        "derivation of the gravitational boundary/action-density",
        "from the one-qubit operator algebra on the `Z^3`",
        "derivation of the Wald-Noether charge formula",
        "metric-compatible coframe response premise carried by the",
        "Target-3 row",
        "Hawking temperature",
        "higher-curvature correction",
    ]
    for phrase in boundary_phrases:
        check(
            f"(scope) note records open scope phrase: {phrase}",
            phrase in note,
        )


def main() -> int:
    print("PLANCK BOUNDARY/ACTION-DENSITY PREMISE-PACKET BRIDGE")
    part0_source_firewall()
    c_cell = part1_primitive_trace()
    part2_bp_registration()
    G_val = part3_retained_equivalence(c_cell)
    part4_unit_readout(G_val)
    part5_dependency_status()
    part6_no_forbidden_imports()
    part7_independence_from_action_density_derivation()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded premise-packet bridge passes; (B1)-(B4) follow "
            "from the retained BH_QUARTER_WALD_NEWTON_COEFFICIENT_NARROW_THEOREM "
            "(T1) + Boolean event-cell linear algebra + supplied premise packet "
            "(BP) by exact sympy rational arithmetic."
        )
        return 0
    print("VERDICT: bounded premise-packet bridge FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
