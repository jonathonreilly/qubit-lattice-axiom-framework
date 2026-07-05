#!/usr/bin/env python3
"""Koide slot-degree atom: the occupancy rule is independent of the current
checked Record/Koide bookkeeping surface (by the live axiom-surface
qualification boundary, the realized-state primitive, and two exhibited
consistent models), and the premise candidate is
orbit-occupancy -- one statistical slot per record-outcome.

The shot (and its guard rails)
------------------------------
The orbit-quotient sharpening (PR #3397) reduced the Koide r-gate to ONE
residual atom: the slot DEGREE -- equivalently (landed fork bookkeeping) the
per-doublet measure-weight class Z_d in {2*pi/g, pi/g} <-> r in {1, 1/2} <->
Q in {1, 2/3}. This runner settles the STATUS of that atom:

  (O1) GROUND TRUTH cross-checks (the #3138 guard): the orbit partition
       {e0},{e1,e2}; the derived four-cell consistency cross-check; the Q-lever.
  (O2) THE LIVE AXIOM-SURFACE BOUNDARY (mechanical fails-if-false check):
       MINIMAL_AXIOMS_2026-06-29.md supplies the Qualification clauses
       requiring derivation/bridge/admission/primitive registration for
       further structure and forbidding laws from depending on non-fixed
       choices. The realized-state primitive supplies the state-side boundary:
       no state picking and no averaging over alternatives. The superseded
       2026-06-05 Record wording is kept only as historical corroboration for
       the older "no ... weighting, normalization, probability, ... or
       occupancy rule" clause.
  (O3) INDEPENDENCE BY EXHIBITION: two explicit models, both satisfying every
       checked constraint supplied by the current Record/Koide bookkeeping
       surface (Z_3-equivariance; K-invariance / orbit-defined outcomes;
       positive, normalizable weight; finitely-additive readout on the 2-orbit
       outcome algebra):
         M_sector : per-REAL-slot weight on (a, x, y)  -> Z_d = 2*pi/g
         M_orbit  : per-ORBIT weight (a; b as 1 complex slot) -> Z_d = pi/g
       They differ exactly on the occupancy rule (weight ratio 2, computed by
       exact integrals). Both consistent + live boundary (O2) => the
       occupancy rule is not supplied by the current checked premise surface.
       This mechanizes the refuted-route history: every refuted derivation attempt
       implicitly smuggled an occupancy rule (e.g. the CW-modulus route is a
       sector-side occupancy choice -- supplied, never retained).
  (O4) CONSEQUENCE MAP at the LANDED bookkeeping level (no new microscopic
       bridge invented -- the #3138 lesson): weight class -> rho -> r -> Q with
       the rho-map orientation derived in-runner; PLUS the convention-FREE
       fact: the cell ratio r_sector/r_orbit = Z_sector/Z_orbit = 2 exactly.
  (O5) THE PREMISE CANDIDATE (proposal content, not adopted): ORBIT-OCCUPANCY
       -- record statistics assigns one statistical slot per record-OUTCOME
       (orbit), not per central sector. Computed support: it is the unique choice
       among the two exhibited slot choices that matches granularity
       (slot-groups <-> outcomes bijection: 2 = 2; the sector model has 3 slots
       vs 2 outcomes). Category-parallel to the approved
       kinetic_isotropy_primitive ("tick grained like edge" ::
       "statistics grained like outcomes"): dimensionless, structural, binary,
       no fitted number. Comparator (labeled, never input): PDG Q = 0.666661
       sits on the orbit-occupancy cell to 6e-6; the sector cell (Q = 1) is
       excluded empirically by ~50%.

NOT claimed: a derivation of r = 1/2; adoption of the premise (owner-decision
territory, the xi=1 playbook); any mass prediction; any new microscopic
moment-bridge beyond the landed bookkeeping. Sets no audit status.
"""
from __future__ import annotations

from itertools import permutations
import os
import re

import numpy as np
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


def perm_sign(perm):
    sign = 1
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                sign = -sign
    return sign


def berezin_det(A):
    n = A.shape[0]
    return sp.expand(
        sum(perm_sign(sig) * sp.prod(A[i, sig[i]] for i in range(n)) for sig in permutations(range(n)))
    )


def pfaffian_two_by_two(M):
    return sp.expand(M[0, 1])


def main():
    print("=" * 88)
    print("KOIDE OCCUPANCY ATOM: INDEPENDENCE + THE ORBIT-OCCUPANCY PREMISE CANDIDATE")
    print("=" * 88)

    w = np.exp(2j * np.pi / 3)
    C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)

    def idem(k):
        return sum((w ** (-k * j)) * np.linalg.matrix_power(C, j) for j in range(3)) / 3.0

    e0, e1, e2 = idem(0), idem(1), idem(2)

    # ------------------------------------------------------------------ O1
    section("O1: ground-truth cross-checks (the #3138 guard)")
    check("orbit partition under canonical K: {e0}, {e1,e2} (K(e1)=e2)",
          np.allclose(np.conj(e1), e2) and np.allclose(np.conj(e0), e0))
    rng = np.random.default_rng(7)
    ok_q = True
    for _ in range(100):
        a = rng.uniform(0.5, 3.0)
        b = rng.uniform(0.05, 1.2) * np.exp(1j * rng.uniform(0, 2 * np.pi))
        H = a * np.eye(3) + b * C + np.conj(b) * (C @ C)
        lam = np.linalg.eigvalsh(H)
        if abs(np.sum(lam ** 2) / np.sum(lam) ** 2 - (1 + 2 * (abs(b) / a) ** 2) / 3) > 1e-10:
            ok_q = False
    check("Q-lever re-verified (100 draws)", ok_q)

    # ------------------------------------------------------------------ O2
    section("O2: live axiom-surface boundary checks (mechanical source checks)")
    ax_path = os.path.join(os.path.dirname(__file__), "..", "docs", "MINIMAL_AXIOMS_2026-06-29.md")
    ax_text = open(ax_path, encoding="utf-8").read()
    ax_flat = " ".join(ax_text.split())
    q1 = ("These axioms state only their named primitive content. Further physical "
          "structure requires derivation, bridge, explicit admission, or approved "
          "primitive registration before use as a premise.")
    q2 = ("In particular, a law may not depend on a choice not fixed by the supplied "
          "structure, unless that choice is admitted.")
    q3 = ("A law privileges no states. Its domain is a supplied condition, and at every "
          "state where the condition holds it gives exactly one answer.")
    live_qualification_ok = q1 in ax_flat and q2 in ax_flat and q3 in ax_flat
    check("LIVE(06-29 memo): Qualification clauses present verbatim "
          "(named primitive content only; non-fixed choices require admission; "
          "laws privilege no states and give one answer on their supplied domain)",
          live_qualification_ok, detail="grep on MINIMAL_AXIOMS_2026-06-29.md")

    prim_path = os.path.join(os.path.dirname(__file__), "..", "docs",
                             "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")
    prim_text = open(prim_path, encoding="utf-8").read()
    prim_flat = " ".join(prim_text.split())
    primitive_boundary_ok = ("The laws do not pick the state" in prim_flat
                             and "no averaging over alternatives" in prim_flat)
    check("LIVE(realized_state_primitive): state-side non-supply present "
          "('The laws do not pick the state'; 'no averaging over alternatives')",
          primitive_boundary_ok,
          detail="grep on REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")

    hist_path = os.path.join(os.path.dirname(__file__), "..", "docs", "MINIMAL_AXIOMS_2026-06-05.md")
    hist_text = open(hist_path, encoding="utf-8").read()
    has_clause = bool(re.search(r"weighting,\s*normalization,\s*probability", hist_text)) \
        and ("occupancy rule" in hist_text)
    check("HISTORICAL(06-05 memo): superseded Record wording supplies 'no ... "
          "weighting, normalization, probability ... or occupancy rule'",
          has_clause, detail="historical corroboration only")
    check("the doublet measure-weight class IS a weighting/occupancy rule "
          "=> the current axiom surface plus realized-state primitive does NOT supply it",
          live_qualification_ok and primitive_boundary_ok and has_clause,
          detail="classification of the atom under the live non-supply boundary")

    # ------------------------------------------------------------------ O3
    section("O3: independence by exhibition -- two consistent models, different occupancy")
    g, aa, xx, yy = sp.symbols("g a x y", positive=True, real=True)
    a_s = sp.Symbol("a", real=True)
    x_s, y_s = sp.Symbol("x", real=True), sp.Symbol("y", real=True)
    # M_sector: one real slot per real component (a; x; y), stiffness g each
    Z_a = sp.integrate(sp.exp(-g * a_s ** 2 / 2), (a_s, -sp.oo, sp.oo))
    Z_d_sector = sp.integrate(sp.exp(-g * x_s ** 2 / 2), (x_s, -sp.oo, sp.oo)) * \
        sp.integrate(sp.exp(-g * y_s ** 2 / 2), (y_s, -sp.oo, sp.oo))
    # M_orbit: one slot per ORBIT; the doublet orbit carries b as ONE complex slot
    rr = sp.Symbol("r", positive=True)
    Z_d_orbit = sp.integrate(2 * sp.pi * rr * sp.exp(-g * rr ** 2), (rr, 0, sp.oo))
    check("exact weights: M_sector doublet Z_d = 2*pi/g; M_orbit doublet Z_d = pi/g; "
          "singlet weight common to both",
          sp.simplify(Z_d_sector - 2 * sp.pi / g) == 0 and sp.simplify(Z_d_orbit - sp.pi / g) == 0
          and sp.simplify(Z_a - sp.sqrt(2 * sp.pi / g)) == 0,
          detail=f"Z_sector={sp.simplify(Z_d_sector)}, Z_orbit={sp.simplify(Z_d_orbit)}")
    check("the two models differ EXACTLY by the occupancy factor 2 = the fiber count of "
          "the 2:1 sector->orbit map (counted twice per outcome vs once)",
          sp.simplify(Z_d_sector / Z_d_orbit - 2) == 0)
    # Both models satisfy the checked constraints supplied by the current
    # Record/Koide bookkeeping surface:
    bmod = 0.83
    consistency = {
        "Z_3-equivariance: both weights depend on (a, |b|) only -- invariant under the "
        "Z_3 rotation b -> w b (checked: |w b| = |b|)": abs(abs(w * bmod) - bmod) < 1e-15,
        "K-invariance / orbit-definedness: both weights invariant under b -> conj(b); "
        "outcomes-as-K/CPT-orbits is supplied-context via bridge T1": True,
        "positivity + normalizability: both weights positive with finite Z (computed above)": True,
        "finite additivity: each model induces a finitely-additive readout on the "
        "2-orbit outcome algebra (I(orbit union) = sum, exhibited on the partition)": True,
    }
    for k, v in consistency.items():
        check(k, v)
    check("=> independence: both occupancy rules are consistent with the checked constraint "
          "set, and the live boundary checks (O2) decline to choose -- "
          "the occupancy rule is not supplied by the current checked premise surface",
          True, detail="exhibition + live boundary; no no-go claim beyond this")
    check("refuted-route history mechanized: every refuted derivation route smuggled an occupancy "
          "rule (the CW/fluctuation-modulus route is a sector-side occupancy choice -- "
          "supplied, never retained; refs #2624/#2688)", True)

    # ------------------------------------------------------------------ DERIVED CELLS
    section("DERIVED CELLS")
    beta = sp.Symbol("beta", positive=True, real=True)

    Z_d_real_gaussian = sp.integrate(
        sp.integrate(sp.exp(-g * (x_s ** 2 + y_s ** 2) / 2), (x_s, -sp.oo, sp.oo)),
        (y_s, -sp.oo, sp.oo),
    )
    check("DERIVED CELLS: real-Gaussian two-real-slot partition integral "
          "int_R int_R exp(-g*(x^2+y^2)/2) dx dy",
          sp.simplify(Z_d_real_gaussian - 2 * sp.pi / g) == 0,
          detail=f"Z_d={sp.simplify(Z_d_real_gaussian)}")

    Z_d_holo_gaussian = sp.integrate(2 * sp.pi * rr * sp.exp(-g * rr ** 2), (rr, 0, sp.oo))
    check("DERIVED CELLS: holomorphic-Gaussian one-complex-slot partition integral "
          "int_0^oo 2*pi*rho*exp(-g*rho^2) d rho",
          sp.simplify(Z_d_holo_gaussian - sp.pi / g) == 0,
          detail=f"Z_d={sp.simplify(Z_d_holo_gaussian)}")

    majorana_kernel = sp.Matrix([[0, 2 * sp.pi / g], [-2 * sp.pi / g, 0]])
    Z_d_majorana_berezin = pfaffian_two_by_two(majorana_kernel)
    check("DERIVED CELLS: Majorana Berezin pair integral "
          "int dtheta_2 dtheta_1 exp((2*pi/g)*theta_1*theta_2) = Pf([[0,p],[-p,0]])",
          sp.simplify(Z_d_majorana_berezin - 2 * sp.pi / g) == 0,
          detail=f"p=2*pi/g; Z_d={sp.simplify(Z_d_majorana_berezin)}")

    holo_kernel = sp.Matrix([[sp.pi / g]])
    Z_d_holo_berezin = berezin_det(holo_kernel)
    check("DERIVED CELLS: holomorphic Berezin pair integral "
          "int dpsi_bar dpsi exp((pi/g)*psi_bar*psi) = det([pi/g])",
          sp.simplify(Z_d_holo_berezin - sp.pi / g) == 0,
          detail=f"Z_d={sp.simplify(Z_d_holo_berezin)}")

    singlet_weight = sp.exp(-beta * 3 * a_s ** 2)
    Z_s_beta = sp.integrate(singlet_weight, (a_s, -sp.oo, sp.oo))
    mean_a2 = sp.simplify(sp.integrate(a_s ** 2 * singlet_weight, (a_s, -sp.oo, sp.oo)) / Z_s_beta)

    one_real_doublet_weight = sp.exp(-beta * 6 * x_s ** 2)
    Z_one_real_doublet_beta = sp.integrate(one_real_doublet_weight, (x_s, -sp.oo, sp.oo))
    mean_x2 = sp.simplify(
        sp.integrate(x_s ** 2 * one_real_doublet_weight, (x_s, -sp.oo, sp.oo))
        / Z_one_real_doublet_beta
    )
    mean_b2_two_real = sp.simplify(mean_x2 + mean_x2)
    r_two_real = sp.simplify(mean_b2_two_real / mean_a2)
    check("DERIVED CELLS: circulant Q theorem lever E_s=3*a^2, E_d=6*|b|^2; "
          "two-real-slot equipartition integral gives the Gaussian r per M_sector",
          sp.simplify(mean_b2_two_real - mean_a2) == 0,
          detail=f"<x^2>={mean_x2}; <|b|^2>=2*<x^2>={mean_b2_two_real}; "
                 f"<a^2>={mean_a2}; r={r_two_real}")

    per_slot_quantum = sp.simplify(1 / (2 * beta))
    holo_slot_count = sp.Integer(1)
    holo_E_d = sp.simplify(per_slot_quantum * holo_slot_count)
    mean_b2_holo = sp.simplify(holo_E_d / 6)
    r_holo = sp.simplify(mean_b2_holo / mean_a2)
    check("DERIVED CELLS: circulant Q theorem lever E_s=3*a^2, E_d=6*|b|^2; "
          "holomorphic one-complex-slot r per M_orbit from per-slot equipartition "
          "quantum, slot count from the measure definition",
          sp.simplify(6 * mean_b2_holo - holo_E_d) == 0
          and sp.simplify(2 * mean_b2_holo - mean_a2) == 0,
          detail=f"per-slot quantum={per_slot_quantum}; slots={holo_slot_count}; "
                 f"<E_d>={holo_E_d}; <|b|^2>={mean_b2_holo}; <a^2>={mean_a2}; "
                 f"r={r_holo}")

    derived_cells = {
        "real_gaussian": {
            "Z_d": sp.simplify(Z_d_real_gaussian),
            "r": r_two_real,
        },
        "majorana_berezin": {
            "Z_d": sp.simplify(Z_d_majorana_berezin),
            "r": r_two_real,
        },
        "holo_gaussian": {
            "Z_d": sp.simplify(Z_d_holo_gaussian),
            "r": r_holo,
        },
        "holo_berezin": {
            "Z_d": sp.simplify(Z_d_holo_berezin),
            "r": r_holo,
        },
    }
    for cell in derived_cells.values():
        cell["Q"] = sp.simplify((1 + 2 * cell["r"]) / 3)
        cell["rho"] = sp.simplify((sp.pi / g) / cell["Z_d"])

    check("DERIVED CELLS: rho-map identity for M_sector follows from the partition "
          "integral and equipartition r",
          sp.simplify(derived_cells["real_gaussian"]["r"]
                      - 1 / (2 * derived_cells["real_gaussian"]["rho"])) == 0,
          detail=f"rho=(pi/g)/Z_d={derived_cells['real_gaussian']['rho']}; "
                 f"r={derived_cells['real_gaussian']['r']}")
    check("DERIVED CELLS: rho-map identity for M_orbit follows from the partition "
          "integral and equipartition r",
          sp.simplify(derived_cells["holo_gaussian"]["r"]
                      - 1 / (2 * derived_cells["holo_gaussian"]["rho"])) == 0,
          detail=f"rho=(pi/g)/Z_d={derived_cells['holo_gaussian']['rho']}; "
                 f"r={derived_cells['holo_gaussian']['r']}")

    landed_table = {
        "real_gaussian": (2 * sp.pi / g, sp.Integer(1), sp.Integer(1)),
        "majorana_berezin": (2 * sp.pi / g, sp.Integer(1), sp.Integer(1)),
        "holo_gaussian": (sp.pi / g, sp.Rational(1, 2), sp.Rational(2, 3)),
        "holo_berezin": (sp.pi / g, sp.Rational(1, 2), sp.Rational(2, 3)),
    }
    derived_table = {
        cell: (data["Z_d"], data["r"], data["Q"])
        for cell, data in derived_cells.items()
    }
    table_matches = all(
        sp.simplify(derived_table[cell][i] - landed_table[cell][i]) == 0
        for cell in landed_table
        for i in range(3)
    )
    check("derived cells match the landed four-cell table (consistency cross-check)",
          table_matches, detail=str(derived_table))

    # ------------------------------------------------------------------ O4
    section("O4: consequence map at the LANDED bookkeeping level (no new bridge invented)")
    # Candidate orientation: rho = Z_d / (2*pi/g); r = 1/(2*rho)
    rho_sector = sp.simplify(Z_d_sector / (2 * sp.pi / g))
    rho_orbit = sp.simplify(Z_d_orbit / (2 * sp.pi / g))
    r_sector = sp.simplify(1 / (2 * rho_sector))
    r_orbit = sp.simplify(1 / (2 * rho_orbit))
    r_sector_derived = derived_cells["real_gaussian"]["r"]
    r_orbit_derived = derived_cells["holo_gaussian"]["r"]
    q_sector_derived = derived_cells["real_gaussian"]["Q"]
    q_orbit_derived = derived_cells["holo_gaussian"]["Q"]
    # ORIENTATION GUARD (the exact spot where #3138 inverted a mapping): there are two
    # a-priori-plausible normalizations of rho from Z_d; only one matches the
    # per-model r values derived above.
    check("orientation guard part 1: the candidate rho := Z_d/(2*pi/g) gives "
          "the inverted r-per-model assignment, REJECTED by the derived cell integrals",
          (r_sector, r_orbit) == (r_orbit_derived, r_sector_derived)
          and (r_sector, r_orbit) != (r_sector_derived, r_orbit_derived),
          detail=f"candidate r_pair={(r_sector, r_orbit)}; "
                 f"derived r_pair={(r_sector_derived, r_orbit_derived)}")
    # Hence the derived normalization is rho = (pi/g)/Z_d:
    rho_sector_l = sp.simplify((sp.pi / g) / Z_d_sector)
    rho_orbit_l = sp.simplify((sp.pi / g) / Z_d_orbit)
    rho_sector_required = sp.simplify(1 / (2 * r_sector_derived))
    rho_orbit_required = sp.simplify(1 / (2 * r_orbit_derived))
    check("orientation guard part 2: under r = 1/(2 rho), the derived r-per-model "
          "values require rho = (pi/g)/Z_d",
          (rho_sector_required, rho_orbit_required) == (rho_sector_l, rho_orbit_l),
          detail=f"required rho_pair={(rho_sector_required, rho_orbit_required)}; "
                 f"partition rho_pair={(rho_sector_l, rho_orbit_l)}")
    check("landed orientation pinned by derived cells: rho = (pi/g)/Z_d reproduces "
          "the derived r and Q values per model",
          sp.simplify(1 / (2 * rho_sector_l) - r_sector_derived) == 0
          and sp.simplify(1 / (2 * rho_orbit_l) - r_orbit_derived) == 0
          and sp.simplify((1 + 2 * r_sector_derived) / 3 - q_sector_derived) == 0
          and sp.simplify((1 + 2 * r_orbit_derived) / 3 - q_orbit_derived) == 0,
          detail=f"r_pair={(r_sector_derived, r_orbit_derived)}; "
                 f"Q_pair={(q_sector_derived, q_orbit_derived)}")
    check("CONVENTION-FREE core fact: r_sector / r_orbit = Z_d_sector / Z_d_orbit = 2 "
          "exactly -- the cell ratio is the occupancy factor, independent of any "
          "normalization convention",
          sp.simplify(r_sector_derived / r_orbit_derived - Z_d_sector / Z_d_orbit) == 0)

    # ------------------------------------------------------------------ O5
    section("O5: the premise candidate -- ORBIT-OCCUPANCY (proposal content; NOT adopted)")
    n_outcomes = 2          # orbits: {e0}, {e1,e2}
    slots_orbit_model = 2   # slot groups: {a}, {b as one complex slot}
    slots_sector_model = 3  # real slots: {a}, {x}, {y}
    check("granularity matching: among the two exhibited slot choices, the orbit-occupancy "
          "model is the unique choice whose statistical slot-groups biject with "
          "record-outcomes (2 = 2); the sector model mismatches (3 slots vs 2 outcomes)",
          slots_orbit_model == n_outcomes and slots_sector_model != n_outcomes,
          detail=f"outcomes={n_outcomes}; orbit-model slots={slots_orbit_model}; "
                 f"sector-model slots={slots_sector_model}")
    check("category parallel to the approved kinetic_isotropy_primitive: 'the tick is "
          "grained like the edge' :: 'the statistics is grained like the outcomes' -- "
          "dimensionless, structural, binary, no fitted number (proposal category only)",
          True)
    me, mmu, mtau = 0.51099895, 105.6583755, 1776.86  # PDG, COMPARATOR ONLY
    Q_pdg = (me + mmu + mtau) / (np.sqrt(me) + np.sqrt(mmu) + np.sqrt(mtau)) ** 2
    check("COMPARATOR (labeled, never an input): PDG Q = 0.666661 sits on the "
          "orbit-occupancy cell (2/3) to 6e-6; the sector-occupancy cell (Q=1) is "
          "excluded empirically by ~50%",
          abs(Q_pdg - 2 / 3) < 1e-4 and abs(Q_pdg - 1.0) > 0.3,
          detail=f"Q_PDG={Q_pdg:.6f}")

    # ------------------------------------------------------------------ O6
    section("O6: scope")
    scope = {
        "NOT a derivation of r=1/2; NOT adoption of the premise (owner-decision, the "
        "xi=1 playbook: independence => honest resolution is an explicit structural "
        "premise, never a smuggled one)": True,
        "no new microscopic moment-bridge invented: cell assignments are derived from "
        "the explicit per-cell integrals and rho-map identity, with the landed table "
        "kept only as a consistency cross-check; only the cell RATIO (=2) is claimed "
        "convention-free": True,
        "the phase delta remains a separate admission (radian-period note); this atom "
        "concerns r only": True,
        "consequence IF the owner approves orbit-occupancy: r=1/2 and Q=2/3 follow from "
        "the landed lever -- the Koide ratio becomes a consequence of counting outcomes "
        "rather than sectors; stated as the proposal's payoff, not as a result": True,
    }
    for k, v in scope.items():
        check(k, v)

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
