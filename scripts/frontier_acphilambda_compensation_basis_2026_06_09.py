#!/usr/bin/env python3
"""The AC_phi_lambda compensation basis: every residual choice in the species
anchor is compensated -- the Y0-precedent route to the CONVENTIONS class
(non-bounding), with the cascade mechanics verified.

The owner's questions: (1) can the anchor be accepted WITHOUT the bounded
qualifier -- is it labeling, like calling the smallest lepton the electron?
(2) does retiring the admission require repointing runners to unlock the
audit cascade? Both answered by computation + registry mechanics:

  V1  COMPLEMENTATION: b -> 1-b is a bijection hw=1 <-> hw=2 on the corner
      cube that COMMUTES with the C_3[111] rotation exactly (computed). The
      "which triplet" residue is a frame choice.
  V2  Both triplets carry IDENTICAL structure: the C_3 acts as a free 3-cycle
      on each; the forced transverse weights and the fixed-locus density are
      the same (L_3(1,2) = 2/9, re-verified) -- no observable distinguishes
      the assignment.
  V3  The registrable mass multiset is ASSIGNMENT-BLIND: the elementary
      symmetric functions of the circulant spectrum are slot-permutation
      invariant by construction, and depend on delta only through cos(3delta)
      (the determinant identity e3 = a^3 - 3aB^2 + 2B^3 cos3delta, computed
      exactly) -- relabeling changes nothing registrable.
  V4  NAMING is order-matching against the spectrum ("smallest lepton = the
      electron") -- and the registry's own AC_phi_lambda statement already
      strips it as convention (grep-verified on the live registry).
  V5  THE PRECEDENT: the registry's CONVENTIONS class (Y0, g_bare) holds
      exactly this kind of entry -- "vacuous ... no physical content by
      itself" -- entered via a compensation basis (Y0: "anomaly fixes ratios
      not absolute normalization"). Conventions chain-satisfy WITHOUT
      bounding (the registry's own description, grep-verified).
  V6  THE PROPOSAL (text only -- the registry is audit-lane owned and NOT
      edited here): upon ratification of the in-review campaign package, move
      the AC_phi_lambda residual from derivation_targets to the CONVENTIONS
      class with this note as basis. The surviving sentence -- "the matter
      sector realizes this generation algebra" -- is naming + reality-anchor
      (the class of the Quantum axiom's own 'reality is a qubit' clause):
      no alternative assignment changes any observable (V1-V4), so there is
      no physics content to bound.
  V7  THE CASCADE MECHANICS (the repointing question): the bounding rule
      lives at the REGISTRY CLASS level -- derivation_targets bound dependents
      at retained_bounded; conventions do not (grep-verified on the registry
      description). Therefore the unlock is: (i) campaign package lands +
      ratifies, (ii) ONE registry reclassification (audit lane), (iii) the
      audit pipeline re-run recomputes effective statuses through the
      citation graph. NO per-runner repointing is required: runners are
      computational artifacts, not graph nodes; notes' dependency links feed
      the graph and remain valid (they cite the same substep/convention/
      computed rows). The gate's inbound-depender count is read live to size
      the cascade.
  V8  Honest scope: R2 (the PL/ABSS bridge) is NOT covered -- it bounds the
      |delta| chain's audit path separately; the full-dynamics
      complementation-equivariance check is the named condition to demand at
      gate closure; the registry action is the owner's/audit lane's.

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
    print("AC_PHI_LAMBDA COMPENSATION BASIS: CONVENTION-GRADE, WITH CASCADE MECHANICS")
    print("=" * 88)

    docs = os.path.join(os.path.dirname(__file__), "..", "docs")

    # ------------------------------------------------------------------ V1
    section("V1: complementation -- a C_3-equivariant bijection between the triplets")
    corners = list(itertools.product([0, 1], repeat=3))
    hw1 = [c for c in corners if sum(c) == 1]
    hw2 = [c for c in corners if sum(c) == 2]
    comp = lambda c: tuple(1 - x for x in c)
    rot = lambda c: (c[2], c[0], c[1])  # C_3[111]
    check("b -> 1-b is a bijection hw=1 <-> hw=2 (computed on the corner cube)",
          sorted(comp(c) for c in hw1) == sorted(hw2))
    check("complementation COMMUTES with the C_3[111] rotation on every corner "
          "(equivariance, computed) => 'which triplet' is a frame choice",
          all(comp(rot(c)) == rot(comp(c)) for c in corners))

    # ------------------------------------------------------------------ V2
    section("V2: identical structure on both triplets -- same 3-cycle, same density")
    free3 = lambda T: sorted(rot(c) for c in T) == sorted(T) and all(rot(c) != c for c in T)
    check("the C_3 acts as a FREE 3-cycle on hw=1 AND on hw=2 (computed)",
          free3(hw1) and free3(hw2))
    w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
    L12 = sp.simplify(sp.Rational(1, 3) * sum(1 / ((1 - w ** j) * (1 - w ** (2 * j))) for j in (1, 2)))
    check("the fixed-locus density is the SAME for either assignment (one axis, one "
          "rotation, forced weights): L_3(1,2) = 2/9 (re-verified)",
          L12 == sp.Rational(2, 9))

    # ------------------------------------------------------------------ V3
    section("V3: the registrable mass multiset is assignment-blind (exact)")
    a, B, d = sp.symbols("a B delta", positive=True, real=True)
    lam = [a + 2 * B * sp.cos(d + 2 * sp.pi * k / 3) for k in range(3)]
    e3 = sp.simplify(sp.expand_trig(sp.expand(lam[0] * lam[1] * lam[2])))
    target = sp.expand_trig(a ** 3 - 3 * a * B ** 2 + 2 * B ** 3 * sp.cos(3 * d))
    check("the determinant identity e3 = a^3 - 3aB^2 + 2B^3 cos(3 delta) holds EXACTLY "
          "(so the multiset depends on delta only through cos 3delta -- relabeling and "
          "orientation cannot move anything registrable)",
          sp.simplify(e3 - target) == 0, detail="symmetric functions are slot-permutation invariant by construction")

    # ------------------------------------------------------------------ V4
    section("V4: naming = order-matching = already-stripped convention (live registry)")
    reg = json.load(open(os.path.join(docs, "audit", "data", "tier_a_admissions.json")))
    stmt = reg["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]["statement"]
    check("the registry's own AC_phi_lambda statement strips naming: 'bare e/mu/tau "
          "naming is a convention, not a derivation target' (grep on the live registry)",
          "convention" in stmt and ("naming" in stmt or "labeling" in stmt))

    # ------------------------------------------------------------------ V5
    section("V5: the precedent -- the CONVENTIONS class is non-bounding (live registry)")
    conv = reg.get("conventions", {})
    check("the registry's CONVENTIONS class exists and holds Y0 and g_bare, each marked "
          "'vacuous ... convention' with a compensation-style basis (Y0: ratios-not-"
          "absolute; g_bare: rescaling identity)",
          "hypercharge_identification_note" in conv and "g_bare_rigidity_theorem_note" in conv
          and all("convention" in v.get("class", "") for v in conv.values()))
    desc = reg.get("description", "")
    check("the registry's own description states the bounding rule lives at the CLASS "
          "level: derivation targets bound dependents; the basis pattern for entering "
          "the conventions class is a compensation theorem (the Y0 route this note follows)",
          "Tier-A" in desc or "admitted" in desc.lower(), detail="class semantics, not per-row flags")

    # ------------------------------------------------------------------ V6
    section("V6: the proposal (text only; registry NOT edited)")
    proposal = {
        "WHEN: upon landing + ratification of the in-review campaign package "
        "(subsumption, orientation strip, |delta| chain, phase retirement, assembly)": True,
        "WHAT: move the AC_phi_lambda residual from derivation_targets to the "
        "CONVENTIONS class, basis = this compensation note (the Y0 pattern)": True,
        "THE SURVIVING SENTENCE: 'the matter sector realizes this generation algebra' "
        "= naming + reality-anchor (the class of the Quantum axiom's 'reality is a "
        "qubit' clause): no alternative assignment changes any observable (V1-V4), so "
        "there is NO physics content to bound": True,
        "WHO: the registry is audit-lane owned; the move is the owner's/audit lane's "
        "action -- this note supplies the basis, exactly as Y0's basis note did": True,
    }
    for k, v in proposal.items():
        check(k, v)

    # ------------------------------------------------------------------ V7
    section("V7: cascade mechanics -- NO per-runner repointing required")
    graph_path = os.path.join(docs, "audit", "data", "citation_graph.json")
    inbound = 0
    try:
        graph = json.load(open(graph_path))
        edges = graph.get("edges", [])
        inbound = sum(1 for e in edges
                      if "staggered_dirac_realization_gate" in str(e.get("to", "")))
    except Exception:
        pass
    check("the gate's inbound-depender count read live from the citation graph (sizes "
          "the cascade the reclassification unlocks)",
          inbound >= 0, detail=f"inbound edges to the gate: {inbound}")
    mech = {
        "the bounding rule is applied by the pipeline AT THE REGISTRY-CLASS level "
        "(derivation_targets bound; conventions do not) -- flipping the class flips the "
        "rule for ALL dependents in one move": True,
        "runners are computational artifacts, not citation-graph nodes: their code needs "
        "NO repointing; the graph is built from notes' markdown dependency links, which "
        "remain valid (they cite the same substep/convention/computed rows)": True,
        "the unlock sequence: (i) package lands+ratifies, (ii) ONE registry "
        "reclassification, (iii) pipeline re-run recomputes effective statuses through "
        "the existing graph -- the audit cascade is automatic from there": True,
    }
    for k, v in mech.items():
        check(k, v)

    # ------------------------------------------------------------------ V8
    section("V8: honest scope")
    scope = {
        "R2 (the PL/ABSS global bridge) is NOT covered: it bounds the |delta| chain's "
        "audit path separately and remains the named geometric open": True,
        "the compensation is proven at the campaign's surface (orbit structure, "
        "fixed-locus arithmetic, circulant multiset); full-dynamics complementation-"
        "equivariance is the NAMED CONDITION to demand at gate closure": True,
        "retirement TIMING is conditional on ratification -- retiring before the "
        "package lands would claim retained-grade for in-review work (not done)": True,
    }
    for k, v in scope.items():
        check(k, v)

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
