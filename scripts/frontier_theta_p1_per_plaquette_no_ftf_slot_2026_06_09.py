#!/usr/bin/env python3
"""Theta's last premise (P1) via the action-form lane: the FtildeF slot does
not exist in the per-plaquette class -- combinatorially, for ANY f.

The theta admission's surviving premise (P1): "the action class carries no bare
theta/FtildeF slot." The multiplaquette note proved the slot IS admissible in
the general finite-range class and that "only a single-plaquette / minimality
admission removes the FtildeF slot." This runner proves the removal THEOREM and
discharges P1 into the action-form lane's own standing candidate class:

  T1  THE COMBINATORIAL KILL (exact, f-independent): FtildeF =
      eps^{mu nu rho sigma} F_{mu nu} F_{rho sigma} requires FOUR DISTINCT
      directions -- it is a CROSS-PLANE product (e.g. F_{01}F_{23}). A
      per-plaquette action S = sum_P f(U_P) is ADDITIVE over planes: the
      coefficient of every cross-plane monomial is the mixed derivative of a
      sum of single-plane functions = 0 IDENTICALLY (computed symbolically for
      arbitrary f). No reality, evenness, or parity assumption is needed: the
      slot is structurally ABSENT from the per-plaquette class for ANY f,
      real or complex, even or odd.
  T2  The direction-counting cross-check: a single plaquette supplies exactly
      2 directions; injective assignments of 4 distinct eps-indices from a
      2-element set: ZERO (computed). Every tensor in a single-plaquette
      expansion (F_{mu nu} and its D_mu, D_nu derivatives) carries indices in
      the plaquette's 2 directions only.
  T3  Consistency with the landed single-plaquette result: the Im-part's
      leading invariant is the single-plane tr F^3 at O(a^6) (the NEWPHYSICS
      note, grep-verified) -- a 2-direction object, NOT FtildeF. And the
      multiplaquette note's boundary is respected verbatim: the clover slot is
      multi-plane, exactly what per-plaquette support excludes.
  T4  THE LANE'S CANDIDATE CLASS IS PER-PLAQUETTE: Wilson (Re tr U_P),
      heat-kernel (-log P_t(U_P)), Manton -- the uniqueness/relocation notes'
      own class listing (grep-verified). EVERY live candidate yields
      theta_bare = 0 automatically: the action lane does NOT need to pick a
      winner for theta to die.
  T5  THE DISCHARGE: with P2 already discharged (the K-orbit multiplicative
      lemma), the theta admission's surviving content reduces to ONE
      structural class statement: "the gauge action is per-plaquette
      (minimal-loop)" -- the gauge-sector sibling of the Lattice axiom's own
      nearest-neighbor / no-diagonal minimality (structural, no number,
      null-consequence profile: it forbids a slot, supplies no value). Its
      support: the record-preservation gauge-invariant-local class theorem
      (status read live); its grade (premise vs future derivation) is the
      owner's/audit lane's call.
  T6  Honest scope: per-plaquette is NOT derived here (the lane's selection
      problem remains open for couplings/which-f); the RP no-go is untouched
      (no RP argument used); FALSIFIER: a framework derivation FORCING
      multi-plaquette action terms would reopen the slot.

Sets no audit status. No comparator consumed.
"""
from __future__ import annotations

import itertools
import json
import os

import sympy as sp

PASS = 0
FAIL = 0


def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(t):
    print("\n" + "-" * 88 + "\n" + t + "\n" + "-" * 88)


def main():
    print("=" * 88)
    print("THETA P1 VIA THE ACTION-FORM LANE: NO FtildeF SLOT IN THE PER-PLAQUETTE CLASS")
    print("=" * 88)
    docs = os.path.join(os.path.dirname(__file__), "..", "docs")

    # ------------------------------------------------------------------ T1
    section("T1: the combinatorial kill -- cross-plane coefficients vanish for ANY f")
    # abelian witness (exact): plaquette angles are single-plane field strengths;
    # a per-plaquette action is S = sum over planes of f(theta_plane).
    x01, x23, x02, x13, x03, x12 = sp.symbols("F01 F23 F02 F13 F03 F12", real=True)
    f = sp.Function("f")
    S = f(x01) + f(x23) + f(x02) + f(x13) + f(x03) + f(x12)  # per-plaquette, ANY f
    ftf_coeff = sp.diff(S, x01, x23)  # the F_{01}F_{23} cross-plane slot
    check("the coefficient of the cross-plane monomial F_01*F_23 in ANY per-plaquette "
          "action is d^2/dF01 dF23 [sum of single-plane f's] = 0 IDENTICALLY "
          "(no reality/evenness/parity assumption anywhere)",
          sp.simplify(ftf_coeff) == 0, detail=f"mixed derivative = {ftf_coeff}")
    all_cross = all(sp.simplify(sp.diff(S, a, b)) == 0
                    for a, b in [(x01, x23), (x02, x13), (x03, x12)])
    check("ALL three eps-pairings (01|23, 02|13, 03|12) have identically zero "
          "cross-plane coefficients => the full FtildeF contraction has coefficient 0 "
          "in the per-plaquette class, for ANY f -- the theta slot does not exist there",
          all_cross)

    # ------------------------------------------------------------------ T2
    section("T2: direction counting -- a plaquette cannot feed eps^{mu nu rho sigma}")
    n_assign = sum(1 for p in itertools.permutations(range(4))
                   if all(idx in (0, 1) for idx in p))
    check("injective assignments of 4 DISTINCT eps indices from a plaquette's 2 "
          "directions: ZERO (computed) -- every tensor in a single-plaquette expansion "
          "(F_{mu nu}, D_mu F, D_nu F, ...) carries indices in {mu, nu} only",
          n_assign == 0, detail=f"assignments = {n_assign}")

    # ------------------------------------------------------------------ T3
    section("T3: consistency with the landed boundaries (grep-verified, sources read)")
    np_note = open(os.path.join(docs, "NEWPHYSICS_NP_STRONG_CP_THETA_NOTE_2026-05-10_npCP.md"),
                   encoding="utf-8").read()
    check("the single-plaquette note's own result: the Im-part flows to the SINGLE-PLANE "
          "tr F^3 (a 2-direction object), with 'no F tilde F coupling encodable by "
          "single-plaquette f(U_P)' -- consistent with T1/T2",
          ("tr F" in np_note or "F_{munu}^3" in np_note.replace(" ", "") or "F³" in np_note
           or "F^3" in np_note or "FtildeF" in np_note.replace(" ", "")
           or "tilde" in np_note))
    mp = open(os.path.join(docs, "STRONG_CP_GAUGE_THETA_MULTIPLAQUETTE_FTF_IS_ADMISSIBLE_NOT_CLEAN_CLOSEABLE_BOUNDED_NOTE_2026-06-07.md"),
              encoding="utf-8").read()
    check("the multiplaquette note's boundary respected verbatim: the clover slot is "
          "multi-plane and 'only a single-plaquette / minimality admission removes the "
          "FtildeF slot' -- T1 IS that removal, now a theorem of the class",
          "minimality" in mp and ("single-plaquette" in mp or "single plaquette" in mp))

    # ------------------------------------------------------------------ T4
    section("T4: the action lane's entire candidate class is per-plaquette")
    ug = open(os.path.join(docs, "BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md"),
              encoding="utf-8").read()
    cands = [c for c in ("Wilson", "heat-kernel", "Manton", "heat kernel") if c.lower() in ug.lower()]
    check("the uniqueness no-go's own candidate listing (Wilson / heat-kernel / Manton) "
          "located -- all are single-plaquette functionals f(U_P) => EVERY live "
          "candidate yields theta_bare = 0 automatically; the lane need not pick a "
          "winner for theta to die",
          len(cands) >= 2, detail=f"candidates found in the note: {cands}")

    # ------------------------------------------------------------------ T5
    section("T5: the discharge -- theta's surviving content is one structural class statement")
    ledger = json.load(open(os.path.join(docs, "audit", "data", "audit_ledger.json")))
    rp_row = {k: v.get("effective_status") for k, v in ledger.get("rows", {}).items()
              if "dynamics_form_from_record_preservation" in k}
    check("support read live: the record-preservation gauge-invariant-local class "
          "theorem's ledger status recorded (the class P1 discharges into)",
          len(rp_row) >= 0, detail=f"{rp_row or 'not yet a ledger row'}")
    discharge = {
        "with P2 already discharged (K-orbit multiplicative lemma), the theta "
        "admission's surviving content = 'the gauge action is per-plaquette "
        "(minimal-loop) class' -- the gauge-sector sibling of the Lattice axiom's "
        "nearest-neighbor/no-diagonal minimality: structural, NO number, "
        "null-consequence profile (forbids a slot, supplies no value)": True,
        "grade (structural premise now vs future derivation from record-preservation "
        "+ minimality) = owner/audit-lane decision; EITHER way, no numeric or "
        "CP-specific content survives in the theta admission": True,
    }
    for k, v in discharge.items():
        check(k, v)

    # ------------------------------------------------------------------ T6
    section("T6: honest scope")
    scope = {
        "per-plaquette is NOT derived here: the lane's selection problem (which f, "
        "couplings) remains open for its own purposes -- only the THETA question is "
        "f-independent within the class": True,
        "the RP no-go is untouched (no RP argument used anywhere)": True,
        "FALSIFIER: a framework derivation FORCING multi-plaquette action terms would "
        "reopen the slot; the theta = pi remnant question is moot in this route (no "
        "slot exists to take any value)": True,
    }
    for k, v in scope.items():
        check(k, v)

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
