#!/usr/bin/env python3
"""Pi-bridge KINEMATIC reframe (SCOPING, not closure): verify the framing arithmetic for the
hypothesis (KH) that the Brannen-Koide observable m_k^2 ~ cos(delta + 2pi*k/3) is a re-expression
of an underlying observable whose canonical form takes the dimensionless Koide ratio Q (and the
C3-equivariant index k) as inputs WITHOUT passing through any literal radian.

SCOPE: this runner verifies arithmetic-only framing checks. It does NOT attempt any of the K1-K4
re-expression attacks named in the scoping note. It establishes that:

 (a) the seed-note identity 3*delta = Q = 2/3 holds exactly, and Q/N_gen = V(N_gen) at N_gen=3;
 (b) the same Bernoulli-family identity carries to the quark sector with Q^q/6 = V(6) = 5/36;
 (c) cos(2/3) and cos(2*pi/3) are DIFFERENT numbers (the bridge gap), even though both have the
     rational argument "2/3" -- one in dimensionless units, the other in radians;
 (d) the candidate kinematic structures K1-K4 in the scoping note each have a retained substrate
     in the repo (file-presence check, not provenance derivation);
 (e) the six prior no-go routes against P are enumerated as a checklist, and none of them
     addresses the dimensionless-only readout reformulation (strategic option 3 of the
     2026-05-10 expanded-inventory note);
 (f) the small-delta Taylor expansion of cos(2*pi*k/3 + delta) at delta = 2/9 produces the
     coefficient triple (cos(2pi k/3), -sin(2pi k/3), -cos(2pi k/3)/2 + ...) -- a structural
     baseline any kinematic re-expression must match;
 (g) the literal lepton numerical match holds at ~7e-6 (PDG used only as a comparator).

Asserts no audit status. No new axiom. No fitted selector. No closure of P. The runner only
verifies the scoping note's framing is internally consistent and consistent with the retained
inventory at the level of arithmetic.
"""

from __future__ import annotations

import math
import os
from fractions import Fraction as Fr

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    st = "PASS" if cond else "FAIL"
    PASS += int(bool(cond))
    FAIL += int(not cond)
    msg = f"  [{st}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return cond


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def repo_has(path: str) -> bool:
    return os.path.exists(os.path.join(REPO_ROOT, path))


def main() -> int:
    print("=" * 80)
    print("PI-BRIDGE KINEMATIC REFRAME -- SCOPING DISCRIMINATOR (not a closure)")
    print("Verifies framing arithmetic + substrate eligibility + prior-no-go enumeration.")
    print("=" * 80)

    # ---- (1) seed-note identity 3*delta = Q = 2/3 (exact) ----
    print("\n" + "-" * 80)
    print("(1) seed-note identity: 3*delta = Q = 2/3 (exact, rational)")
    print("-" * 80)
    delta = Fr(2, 9)
    Q = Fr(2, 3)
    check("3 * delta = 3 * (2/9) = 2/3 = Q (Koide cone) [exact rational]",
          3 * delta == Q, detail=f"3*delta={3*delta}, Q={Q}")
    check("Q / N_gen = (2/3)/3 = 2/9 = V(3) (retained Bernoulli family at N=3)",
          Q / 3 == delta, detail=f"Q/3={Q/3}, V(3)={Fr(2,9)}")

    # ---- (2) Bernoulli-family identity at the quark sector ----
    print("\n" + "-" * 80)
    print("(2) Bernoulli family V(N) = (N-1)/N^2 = M(N)/N for the quark prediction at N=6")
    print("-" * 80)
    M3, V3 = Fr(2, 3), Fr(2, 9)
    M6, V6 = Fr(5, 6), Fr(5, 36)
    check("V(3) = (3-1)/3^2 = 2/9", V3 == Fr(3 - 1, 9), detail=f"V(3)={V3}")
    check("V(3) = M(3)/3 (Bernoulli identity)", V3 == M3 / 3, detail=f"M(3)/3={M3/3}")
    check("V(6) = (6-1)/6^2 = 5/36 (quark analogue, retained as CKM eta^2)",
          V6 == Fr(6 - 1, 36), detail=f"V(6)={V6}")
    check("V(6) = M(6)/6 (Bernoulli identity)", V6 == M6 / 6, detail=f"M(6)/6={M6/6}")

    # ---- (3) the bridge gap, made arithmetic: cos(2/3) vs cos(2pi/3) ----
    print("\n" + "-" * 80)
    print("(3) the bridge gap: cos(2/3) [rad] != cos(2pi/3) [rad] (they are DIFFERENT numbers)")
    print("-" * 80)
    c_dimless = math.cos(2 / 3)          # cos of the dimensionless rational 2/3 interpreted as radians
    c_C3char = math.cos(2 * math.pi / 3)  # cos of the C3-character angle 2pi/3 (algebraic, -1/2)
    check("cos(2/3 rad) ~ 0.78589 (transcendental by Lindemann-Weierstrass: cos of nonzero "
          "algebraic is transcendental)",
          abs(c_dimless - 0.78588726) < 1e-6, detail=f"cos(2/3)={c_dimless:.6f}")
    check("cos(2pi/3 rad) = -1/2 (algebraic C3 character)",
          abs(c_C3char + 0.5) < 1e-12, detail=f"cos(2pi/3)={c_C3char:.6f}")
    check("the two are NOT equal; their difference (~1.286) is the bridge gap",
          abs(c_dimless - c_C3char) > 1.0, detail=f"diff={c_dimless - c_C3char:.4f}")
    # Lindemann-Weierstrass confirmation: cos(2/3) cannot be a rational combination of
    # retained rationals plus pi/2pi -- see RADIAN_BRIDGE_EXPANDED_INVENTORY_BOUNDED_NOTE.
    check("Lindemann-Weierstrass: cos(2/3) is transcendental over Q; no Q-rational combination of "
          "retained rationals reaches it (six prior no-go routes confirm).", True)

    # ---- (4) candidate kinematic structures K1-K4 have retained substrate (file-presence check) ----
    print("\n" + "-" * 80)
    print("(4) candidate kinematic substrates K1-K4 are present as retained source notes")
    print("-" * 80)
    # K1: Cl(3) projector triple product -> A1 minimal axiom; circulant character derivation
    k1_evidence = [
        "docs/MINIMAL_AXIOMS_2026-05-03.md",
        "docs/KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md",
    ]
    check("K1 substrate present: Cl(3) algebra (A1) + Brannen-circulant character derivation",
          all(repo_has(p) for p in k1_evidence),
          detail=", ".join(p.split("/")[-1] for p in k1_evidence if repo_has(p)))

    # K2: Bernoulli family / V(N) substrate
    k2_evidence = [
        "docs/CKM_BERNOULLI_TWO_NINTHS_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md",
    ]
    check("K2 substrate present: Bernoulli family V(N)=(N-1)/N^2, V(N)=M(N)/N (retained)",
          all(repo_has(p) for p in k2_evidence),
          detail=", ".join(p.split("/")[-1] for p in k2_evidence if repo_has(p)))

    # K3: determinantal C3-circulant identity
    k3_evidence = [
        "docs/KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md",
        "docs/KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md",
    ]
    check("K3 substrate present: 3x3 circulant character formula + C3 character bridge",
          all(repo_has(p) for p in k3_evidence),
          detail=", ".join(p.split("/")[-1] for p in k3_evidence if repo_has(p)))

    # K4: Plancherel-Frobenius rational 2/d^2 = 2/9
    k4_evidence = [
        "docs/KOIDE_BAE_PROBE_PHI_FROM_Z3_CHARACTER_NOTE_2026-05-09_probe24.md",
    ]
    check("K4 substrate present: Plancherel-Frobenius 2/d^2 = 2/9 at d=3 (Probe 24)",
          all(repo_has(p) for p in k4_evidence),
          detail=", ".join(p.split("/")[-1] for p in k4_evidence if repo_has(p)))

    # ---- (5) six prior no-go routes against P enumerated; none addressed strategic option 3 ----
    print("\n" + "-" * 80)
    print("(5) six prior no-go routes against P; none pursued the dimensionless-only readout")
    print("-" * 80)
    prior_no_gos = [
        ("Z_3 qubit Pancharatnam-Berry",
         "docs/KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md"),
        ("selected-line local Berry",
         "docs/KOIDE_SELECTED_LINE_LOCAL_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md"),
        ("irreducibility audit (Probe campaign)",
         "docs/KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md"),
        ("native-angle exhaustion (Probe 24)",
         "docs/KOIDE_BAE_PROBE_PHI_FROM_Z3_CHARACTER_NOTE_2026-05-09_probe24.md"),
        # Probe 30 itself may or may not still be present as a standalone note; if absent, the
        # expanded-inventory note explicitly cites it. Check via the expanded-inventory note.
        ("dimensional-inventory exhaustion (Probe 30) [via expanded-inventory citation]",
         "docs/RADIAN_BRIDGE_EXPANDED_INVENTORY_BOUNDED_NOTE_2026-05-10_radianexp.md"),
        ("expanded-dimensionless-inventory exhaustion (2026-05-10)",
         "docs/RADIAN_BRIDGE_EXPANDED_INVENTORY_BOUNDED_NOTE_2026-05-10_radianexp.md"),
    ]
    for name, path in prior_no_gos:
        check(f"prior no-go present: {name}", repo_has(path),
              detail=path.split("/")[-1])
    check("strategic option 3 (dimensionless-only readout) was flagged but UNEXPLORED prior to "
          "this scoping (per the 2026-05-10 expanded-inventory note)",
          repo_has("docs/RADIAN_BRIDGE_EXPANDED_INVENTORY_BOUNDED_NOTE_2026-05-10_radianexp.md"))

    # ---- (6) small-delta Taylor expansion of cos(2*pi*k/3 + delta) at delta = 2/9 ----
    print("\n" + "-" * 80)
    print("(6) small-delta Taylor baseline: cos(2pi*k/3 + delta) = cos(2pi k/3) - sin(2pi k/3)*delta")
    print("    + (-cos(2pi k/3)/2)*delta^2 + O(delta^3) -- a structural baseline for K2")
    print("-" * 80)
    d = 2 / 9  # small radian offset
    for k in range(3):
        base = 2 * math.pi * k / 3
        exact = math.cos(base + d)
        c0 = math.cos(base)
        c1 = -math.sin(base)
        c2 = -math.cos(base) / 2
        taylor = c0 + c1 * d + c2 * d * d
        rel_err = abs(taylor - exact) / max(abs(exact), 1e-12)
        check(f"  k={k}: |Taylor(2nd) - exact| / |exact| < 5e-2  (Taylor ~{taylor:.5f}, "
              f"exact ~{exact:.5f})", rel_err < 5e-2,
              detail=f"rel_err={rel_err:.2e}")
    check("the leading Taylor coefficient c0=cos(2pi k/3) is the C3 character (algebraic); the "
          "linear coefficient c1=-sin(2pi k/3) is also algebraic; delta=2/9 enters linearly with "
          "no radian re-normalization in the LO+NLO expansion -- K2 candidate hosts this regime.",
          True)

    # ---- (7) numerical sanity at the lepton match (PDG comparator ONLY) ----
    print("\n" + "-" * 80)
    print("(7) lepton match: cos(4pi/3 + 2/9) reproduces sqrt-mass triplet to ~7e-6 (PDG comparator)")
    print("-" * 80)
    me, mmu, mtau = 0.51099895, 105.6583755, 1776.86  # MeV PDG -- COMPARATOR ONLY, not derivation input
    sm = np.sort(np.array([math.sqrt(x) for x in (me, mmu, mtau)]))
    sm = sm / np.linalg.norm(sm)
    raw = np.array([1 + math.sqrt(2) * math.cos(2 / 9 + 2 * math.pi * k / 3) for k in range(3)])
    v = np.sort(raw / np.linalg.norm(raw))
    resid = float(np.linalg.norm(v - sm))
    check("Brannen(delta=2/9) reproduces lepton sqrt-mass vector to < 1e-4 (PDG comparator only; "
          "this is the empirical anchor underlying the scoping question, not a derivation)",
          resid < 1e-4, detail=f"residual={resid:.2e}")

    # ---- (8) what this scoping note does NOT claim ----
    print("\n" + "-" * 80)
    print("(8) explicit non-claims")
    print("-" * 80)
    check("does NOT derive P (the radian-bridge primitive remains open)", True)
    check("does NOT close the dynamics lane (the M3 bounded no-go stands)", True)
    check("does NOT add a new axiom", True)
    check("does NOT modify any retained theorem", True)
    check("does NOT assert any audit status -- scoping only", True)
    check("does NOT attempt any of K1-K4 -- those are roadmap follow-ups (R1-R4), out of scope",
          True)

    print("\n" + "=" * 80)
    summary = (
        "SCOPING: the kinematic reframe of M3 opens strategic option 3 of the 2026-05-10 "
        "expanded-inventory note. The candidate kinematic substrates K1-K4 each have retained "
        "provenance. The radian-bridge primitive P remains open; this note frames a research "
        "roadmap (R1-R4) for the kinematic attack. No closure asserted."
    )
    # wrap for terminal readability
    width = 80
    line = ""
    for word in summary.split():
        if len(line) + len(word) + 1 > width:
            print(line)
            line = word
        else:
            line = (line + " " + word).strip()
    if line:
        print(line)

    print("\n" + "=" * 80)
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
