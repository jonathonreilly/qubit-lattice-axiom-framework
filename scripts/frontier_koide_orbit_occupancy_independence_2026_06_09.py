#!/usr/bin/env python3
"""Check the repaired Koide orbit-occupancy boundary.

The runner establishes three narrow facts:

* the Gaussian moment for ``E = 3 a**2 + 6 |b|**2`` gives ``r = 1`` in
  Cartesian and polar coordinates, so the former ``rho`` map cannot derive
  ``r = 1/2``;
* an aggregate equal-energy-per-counting-unit condition gives ``r = 1`` when
  the doublet is counted by its two real dimensions and ``r = 1/2`` when it is
  counted as one supplied K/CPT outcome cell;
* the two aggregate conditions are nonempty and invariant under the checked
  ``Z_3`` and conjugation actions.  No componentwise equality between fixed
  Cartesian coordinates is claimed.

The per-outcome-cell condition is proposed content, not an axiom, approved
primitive, derived selector, probability rule, or audit verdict.  The PDG
charged-lepton ratio is printed as a report-only observational comparator and
never contributes to PASS/FAIL.
"""
from __future__ import annotations

from itertools import permutations
import json
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
    print("KOIDE ORBIT OCCUPANCY: HONEST MOMENTS + AGGREGATE GRANULARITY CONDITIONS")
    print("(source repair; independent audit remains pending)")
    print("=" * 88)

    w = np.exp(2j * np.pi / 3)
    C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)

    def idem(k):
        return sum((w ** (-k * j)) * np.linalg.matrix_power(C, j) for j in range(3)) / 3.0

    e0, e1, e2 = idem(0), idem(1), idem(2)

    section("Ground-truth orbit and circulant checks")
    check("orbit partition under canonical K: {e0}, {e1,e2} (K(e1)=e2)",
          np.allclose(np.conj(e1), e2) and np.allclose(np.conj(e0), e0))

    a_exact = sp.Symbol("a_exact", positive=True, real=True)
    x_exact, y_exact = sp.symbols("x_exact y_exact", real=True)
    b_exact = x_exact + sp.I * y_exact
    C_exact = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    H_exact = a_exact * sp.eye(3) + b_exact * C_exact + sp.conjugate(b_exact) * C_exact**2
    q_exact = sp.simplify(sp.trace(H_exact**2) / sp.trace(H_exact) ** 2)
    q_target = sp.simplify((1 + 2 * (x_exact**2 + y_exact**2) / a_exact**2) / 3)
    check("Q dictionary derived exactly from trace(H) and trace(H^2)",
          sp.simplify(q_exact - q_target) == 0,
          detail=f"Q={q_exact}")

    rng = np.random.default_rng(7)
    ok_q = True
    for _ in range(100):
        a = rng.uniform(0.5, 3.0)
        b = rng.uniform(0.05, 1.2) * np.exp(1j * rng.uniform(0, 2 * np.pi))
        H = a * np.eye(3) + b * C + np.conj(b) * (C @ C)
        lam = np.linalg.eigvalsh(H)
        if abs(np.sum(lam ** 2) / np.sum(lam) ** 2 - (1 + 2 * (abs(b) / a) ** 2) / 3) > 1e-10:
            ok_q = False
    check("independent numerical diagonalization matches Q = (1 + 2 |b|^2/a^2)/3 "
          "(100 deterministic draws)", ok_q)

    section("Current premise-boundary source checks")
    ax_path = os.path.join(os.path.dirname(__file__), "..", "docs", "MINIMAL_AXIOMS_2026-06-29.md")
    ax_text = open(ax_path, encoding="utf-8").read()
    ax_flat = " ".join(re.sub(r"-\s+", "-", ax_text).split())
    q1 = ("These axioms state only their named primitive content. Further physical "
          "structure requires a retained derivation or bridge, or explicit approved-"
          "primitive registration, before use as a premise. A choice not fixed by the "
          "supplied structure remains a named conditional or open dependency.")
    q2 = ("A law privileges no states. Its domain is a supplied condition, and at every "
          "state where the condition holds it gives exactly one answer.")
    live_qualification_ok = q1 in ax_flat and q2 in ax_flat
    check("current minimal-axiom Qualification keeps non-fixed structure conditional/open "
          "and requires one answer on a supplied law domain",
          live_qualification_ok, detail="grep on MINIMAL_AXIOMS_2026-06-29.md")

    prim_path = os.path.join(os.path.dirname(__file__), "..", "docs",
                             "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")
    prim_text = open(prim_path, encoding="utf-8").read()
    prim_flat = " ".join(prim_text.split())
    primitive_boundary_ok = (
        "The laws do not pick the state" in prim_flat
        and "no averaging over alternatives" in prim_flat
        and "registered data, not derivation output" in prim_flat
    )
    check("realized-state primitive supplies pointwise evaluation but no averaging or "
          "state-contingent value",
          primitive_boundary_ok,
          detail="grep on REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")

    registry_path = os.path.join(os.path.dirname(__file__), "..", "docs", "audit", "data",
                                 "axiom_premise_nodes.json")
    with open(registry_path, encoding="utf-8") as handle:
        registered_nodes = set(json.load(handle)["canonical_ids"])
    expected_nodes = {"minimal_axioms", "scale_reference_primitive",
                      "kinetic_isotropy_primitive", "realized_state_primitive"}
    check("the proposed equipartition-granularity condition is absent from the approved "
          "premise registry",
          registered_nodes == expected_nodes,
          detail=f"registered={sorted(registered_nodes)}")

    section("Two compatible aggregate channel-energy conditions")

    def aggregate_residual(a_value, b_value, doublet_count):
        return 6 * abs(b_value) ** 2 - doublet_count * 3 * a_value**2

    symmetry_ok = True
    nonempty_ok = True
    for doublet_count in (1, 2):
        for phase in np.linspace(0.0, 2 * np.pi, 17, endpoint=False):
            a_value = 1.3
            b_value = np.sqrt(doublet_count / 2) * a_value * np.exp(1j * phase)
            nonempty_ok &= abs(aggregate_residual(a_value, b_value, doublet_count)) < 1e-12
            symmetry_ok &= abs(aggregate_residual(a_value, w * b_value, doublet_count)) < 1e-12
            symmetry_ok &= abs(aggregate_residual(a_value, np.conj(b_value), doublet_count)) < 1e-12
    check("both aggregate solution sets are nonempty", nonempty_ok)
    check("both aggregate conditions are invariant under b -> omega b and b -> conjugate(b)",
          symmetry_ok)

    cells = ("singlet", "doublet")
    subsets = [frozenset(), frozenset({cells[0]}), frozenset({cells[1]}), frozenset(cells)]

    def readout(subset, singlet_energy, doublet_energy):
        values = {"singlet": singlet_energy, "doublet": doublet_energy}
        return sum(values[cell] for cell in subset)

    additive_ok = True
    for doublet_count in (1, 2):
        energies = (3.0, 3.0 * doublet_count)
        for left in subsets:
            for right in subsets:
                if left.isdisjoint(right):
                    additive_ok &= readout(left | right, *energies) == (
                        readout(left, *energies) + readout(right, *energies)
                    )
    check("both two-cell witness readouts are finitely additive (all disjoint subsets)",
          additive_ok)

    section("Moment-honesty diagnostic: the stated Gaussian gives r = 1")
    beta = sp.Symbol("beta", positive=True, real=True)
    g = sp.Symbol("g", positive=True, real=True)
    measure_scale = sp.Symbol("measure_scale", positive=True, real=True)
    a_s = sp.Symbol("a", real=True)
    x_s, y_s = sp.symbols("x y", real=True)
    rho_s = sp.Symbol("rho", positive=True)

    # Landed circulant lever (cited, KOIDE_CIRCULANT_Q_TWO_THIRDS...): the channel
    # energy is E = E_s + E_d with E_s = 3 a^2 and E_d = 6 |b|^2. Single physical
    # inverse-temperature beta; Gibbs/Gaussian weight exp(-beta E).

    # -- singlet second moment, honest integral --
    w_singlet = sp.exp(-beta * 3 * a_s ** 2)
    Z_singlet = sp.integrate(w_singlet, (a_s, -sp.oo, sp.oo))
    mean_a2 = sp.simplify(sp.integrate(a_s ** 2 * w_singlet, (a_s, -sp.oo, sp.oo)) / Z_singlet)
    check("singlet moment derived by honest integral: <a^2> = 1/(6 beta)",
          sp.simplify(mean_a2 - 1 / (6 * beta)) == 0, detail=f"<a^2>={mean_a2}")

    # Polar coordinates for the same Cartesian density:
    # d^2 b = rho d rho d theta and exp(-6 beta |b|^2).
    w_doublet = sp.exp(-beta * 6 * rho_s ** 2)
    Z_doublet_holo = sp.integrate(2 * sp.pi * rho_s * w_doublet, (rho_s, 0, sp.oo))
    mean_b2_holo = sp.simplify(
        sp.integrate(2 * sp.pi * rho_s * rho_s ** 2 * w_doublet, (rho_s, 0, sp.oo)) / Z_doublet_holo
    )
    r_moment_holo = sp.simplify(mean_b2_holo / mean_a2)
    # Contact with the audit's notation (g = 6 beta): Z = pi/g, <|b|^2> = 1/g.
    Z_holo_in_g = sp.simplify(Z_doublet_holo.subs(beta, g / 6))
    mean_b2_holo_in_g = sp.simplify(mean_b2_holo.subs(beta, g / 6))
    check("audit finding reproduced: the polar Gaussian integral gives "
          "Z_d = pi/(6 beta) = pi/g and <|b|^2> = 1/(6 beta) = 1/g (with g = 6 beta); "
          "hence r = <|b|^2>/<a^2> = 1, NOT 1/2",
          sp.simplify(Z_holo_in_g - sp.pi / g) == 0
          and sp.simplify(mean_b2_holo_in_g - 1 / g) == 0
          and r_moment_holo == 1,
          detail=f"Z_d(holo)={sp.simplify(Z_doublet_holo)}; <|b|^2>={mean_b2_holo}; "
                 f"r_moment(holo)={r_moment_holo}")

    # Cartesian coordinates for exactly the same density.
    w_doublet_real = sp.exp(-beta * 6 * (x_s ** 2 + y_s ** 2))
    Z_doublet_real = sp.integrate(
        sp.integrate(w_doublet_real, (x_s, -sp.oo, sp.oo)), (y_s, -sp.oo, sp.oo))
    mean_b2_real = sp.simplify(
        sp.integrate(sp.integrate((x_s ** 2 + y_s ** 2) * w_doublet_real,
                                  (x_s, -sp.oo, sp.oo)), (y_s, -sp.oo, sp.oo)) / Z_doublet_real
    )
    r_moment_real = sp.simplify(mean_b2_real / mean_a2)
    check("Cartesian and polar coordinates give the same partition integral and moment",
          sp.simplify(Z_doublet_real - Z_doublet_holo) == 0
          and sp.simplify(mean_b2_real - mean_b2_holo) == 0
          and r_moment_real == 1,
          detail=f"Z={sp.simplify(Z_doublet_real)}; <|b|^2>={mean_b2_real}; r={r_moment_real}")

    scaled_mean = sp.simplify(
        (measure_scale * sp.integrate(2 * sp.pi * rho_s**3 * w_doublet,
                                      (rho_s, 0, sp.oo)))
        / (measure_scale * Z_doublet_holo)
    )
    check("a multiplicative measure normalization cancels from the normalized moment",
          sp.simplify(scaled_mean - mean_b2_holo) == 0)

    # The diagnostic is the standard Gaussian equipartition identity in this density.
    mean_x2 = sp.simplify(
        sp.integrate(x_s ** 2 * sp.exp(-beta * 6 * x_s ** 2), (x_s, -sp.oo, sp.oo))
        / sp.integrate(sp.exp(-beta * 6 * x_s ** 2), (x_s, -sp.oo, sp.oo))
    )
    check("the stated Gaussian satisfies per-coordinate equipartition in expectation, "
          "<3 a^2> = <6 x^2> = <6 y^2> = 1/(2 beta), hence <E_d> = 2 <E_s> "
          "and r_moment = 1; it does not satisfy <E_d> = <E_s>",
          sp.simplify(3 * mean_a2 - 1 / (2 * beta)) == 0
          and sp.simplify(6 * mean_x2 - 1 / (2 * beta)) == 0
          and sp.simplify(6 * mean_b2_holo - 2 * (3 * mean_a2)) == 0
          and sp.simplify(6 * mean_b2_holo - 3 * mean_a2) != 0,
          detail=f"<3a^2>={sp.simplify(3 * mean_a2)}; <6x^2>={sp.simplify(6 * mean_x2)}; "
                 f"<E_d>={sp.simplify(6 * mean_b2_holo)} = 2*<E_s>")

    section("Exact aggregate equal-energy-per-counting-unit conditions")
    a_v = sp.Symbol("a_v", positive=True)
    bmag2 = sp.Symbol("bmag2", positive=True)
    eps = sp.Symbol("eps", positive=True)
    E_s = 3 * a_v ** 2
    E_d = 6 * bmag2

    # Aggregate real-dimension counting: one singlet dimension and two doublet
    # dimensions.  This does not impose equality on fixed x/y components.
    sol_mode = sp.solve([sp.Eq(E_s, eps), sp.Eq(E_d, 2 * eps)], [eps, bmag2], dict=True)[0]
    r_mode = sp.simplify(sol_mode[bmag2] / a_v ** 2)
    Q_mode = sp.simplify((1 + 2 * r_mode) / 3)
    check("aggregate real-dimension condition E_s = eps, E_d = 2 eps gives r = 1",
          sp.simplify(sol_mode[bmag2] - a_v ** 2) == 0 and r_mode == 1
          and sp.simplify(sol_mode[eps] - 3 * a_v ** 2) == 0,
          detail=f"|b|^2(law)={sol_mode[bmag2]}; eps={sol_mode[eps]}; r_mode={r_mode}")

    # Outcome-cell counting on the supplied orbit indexing: one singlet cell and
    # one doublet cell.
    sol_cell = sp.solve([sp.Eq(E_s, eps), sp.Eq(E_d, eps)], [eps, bmag2], dict=True)[0]
    r_cell = sp.simplify(sol_cell[bmag2] / a_v ** 2)
    Q_cell = sp.simplify((1 + 2 * r_cell) / 3)
    check("aggregate outcome-cell condition E_s = E_d = eps gives r = 1/2",
          sp.simplify(sol_cell[bmag2] - a_v ** 2 / 2) == 0 and r_cell == sp.Rational(1, 2),
          detail=f"|b|^2(law)={sol_cell[bmag2]}; eps={sol_cell[eps]}; r_cell={r_cell}")
    check("circulant Q dictionary maps the two conditional endpoints to Q = 1 and Q = 2/3",
          Q_mode == 1 and Q_cell == sp.Rational(2, 3),
          detail=f"Q_mode={Q_mode}; Q_cell={Q_cell}")
    check("r = 1/2 comes from the supplied aggregate cell condition, not from the Gaussian moment",
          r_cell != r_mode and r_mode == r_moment_holo == 1
          and r_cell == sp.Rational(1, 2))

    sol_competitor = sp.solve([sp.Eq(E_s, eps), sp.Eq(E_d, 3 * eps)],
                              [eps, bmag2], dict=True)[0]
    r_competitor = sp.simplify(sol_competitor[bmag2] / a_v**2)
    check("wrong-count discriminator: doublet_count = 3 gives r = 3/2 and is rejected",
          r_competitor == sp.Rational(3, 2)
          and r_competitor not in {r_mode, r_cell})

    section("Witness premise-surface parity and discriminators")
    # r produced by each witness, computed above (not hard-coded):
    r_sector_derived = r_mode
    r_orbit_derived = r_cell
    Q_sector_derived = Q_mode
    Q_orbit_derived = Q_cell

    shared_carrier = "(a, b) in R_{>0} x C"
    shared_energy = "E_s = 3 a^2; E_d = 6 |b|^2"
    shared_dict = "Q = (1 + 2 r)/3"
    shared_symmetry = "aggregate relation invariant under b -> omega b and b -> conjugate(b)"
    shared_orbits = "supplied orbit indexing {e0}; {e1,e2}"
    shared_form = "E_s = eps; E_d = doublet_count * eps"

    M_sector = {
        "carrier": shared_carrier,
        "channel_energy": shared_energy,
        "outcome_dictionary": shared_dict,
        "checked_symmetry": shared_symmetry,
        "outcome_indexing": shared_orbits,
        "aggregate_condition_form": shared_form,
        "doublet_count": 2,
    }
    M_orbit = {
        "carrier": shared_carrier,
        "channel_energy": shared_energy,
        "outcome_dictionary": shared_dict,
        "checked_symmetry": shared_symmetry,
        "outcome_indexing": shared_orbits,
        "aggregate_condition_form": shared_form,
        "doublet_count": 1,
    }
    differing = [k for k in M_sector if M_sector[k] != M_orbit[k]]
    shared = [k for k in M_sector if M_sector[k] == M_orbit[k]]
    check("the two constructed extensions share carrier, channel energy, Q dictionary, "
          "symmetry, supplied orbit indexing, and aggregate condition form",
          set(shared) == {"carrier", "channel_energy", "outcome_dictionary",
                          "checked_symmetry", "outcome_indexing", "aggregate_condition_form"},
          detail=f"shared={sorted(shared)}")
    check("exactly one supplied element differs: doublet_count = 2 versus 1",
          differing == ["doublet_count"], detail=f"differing={differing}")

    mutant = dict(M_orbit)
    mutant["channel_energy"] = "E_s = 3 a^2; E_d = 5 |b|^2"
    mutant_differences = [k for k in M_sector if M_sector[k] != mutant[k]]
    check("parity discriminator rejects a witness with a second changed premise",
          set(mutant_differences) == {"channel_energy", "doublet_count"},
          detail=f"mutant_differences={mutant_differences}")

    check("changing only doublet_count changes r from 1 to 1/2",
          r_sector_derived == 1 and r_orbit_derived == sp.Rational(1, 2)
          and r_sector_derived != r_orbit_derived,
          detail=f"r(real-dimension aggregate)={r_sector_derived}; r(cell aggregate)={r_orbit_derived}")
    check("conditional endpoints are derived rather than inserted",
          (r_sector_derived, Q_sector_derived) == (sp.Integer(1), sp.Integer(1))
          and (r_orbit_derived, Q_orbit_derived) == (sp.Rational(1, 2), sp.Rational(2, 3)),
          detail=f"sector=({r_sector_derived},{Q_sector_derived}); "
                 f"orbit=({r_orbit_derived},{Q_orbit_derived})")

    section("Decoupled quadratic-kernel and determinant-power arithmetic")
    # These are separate integral/kernel facts.  They are not coordinate forms
    # of the identical density used in the moment check above.
    Z_real_gaussian = sp.integrate(
        sp.integrate(sp.exp(-g * (x_s ** 2 + y_s ** 2) / 2), (x_s, -sp.oo, sp.oo)),
        (y_s, -sp.oo, sp.oo))
    Z_holo_gaussian = sp.integrate(2 * sp.pi * rho_s * sp.exp(-g * rho_s ** 2), (rho_s, 0, sp.oo))
    majorana_kernel = sp.Matrix([[0, 2 * sp.pi / g], [-2 * sp.pi / g, 0]])
    Z_majorana_berezin = pfaffian_two_by_two(majorana_kernel)
    holo_kernel = sp.Matrix([[sp.pi / g]])
    Z_holo_berezin = berezin_det(holo_kernel)
    check("quadratic-kernel/determinant-power cells: real two-coordinate "
          "Z_d = 2 pi/g (Gaussian and Majorana-Berezin); holomorphic one-complex-slot "
          "Z_d = pi/g (Gaussian and Berezin)",
          sp.simplify(Z_real_gaussian - 2 * sp.pi / g) == 0
          and sp.simplify(Z_majorana_berezin - 2 * sp.pi / g) == 0
          and sp.simplify(Z_holo_gaussian - sp.pi / g) == 0
          and sp.simplify(Z_holo_berezin - sp.pi / g) == 0,
          detail=f"Z_real={sp.simplify(Z_real_gaussian)}, "
                 f"Z_majorana={sp.simplify(Z_majorana_berezin)}, "
                 f"Z_holo_gauss={sp.simplify(Z_holo_gaussian)}, "
                 f"Z_holo_berezin={sp.simplify(Z_holo_berezin)}")
    check("the two integral/kernel cells differ by the factor 2",
          sp.simplify((2 * sp.pi / g) / (sp.pi / g) - 2) == 0)
    print("  [REPORT] The two Z values alone provide no equation for r; the former "
          "rho-map attribution is not used.")
    check("honest conditional consequence map: real-dimension aggregate -> (r,Q)=(1,1); "
          "outcome-cell aggregate -> (r,Q)=(1/2,2/3)",
          (r_sector_derived, Q_sector_derived, r_orbit_derived, Q_orbit_derived)
          == (sp.Integer(1), sp.Integer(1), sp.Rational(1, 2), sp.Rational(2, 3)))

    section("Report-only observational comparator")
    # F. Takahashi et al. (Particle Data Group), RPP 2026 lepton summary table.
    # These values never enter check().
    me, mmu, mtau = 0.51099895069, 105.6583755, 1776.93
    Q_pdg = (me + mmu + mtau) / (np.sqrt(me) + np.sqrt(mmu) + np.sqrt(mtau)) ** 2
    print(f"  [REPORT] PDG 2026 central-value Q = {Q_pdg:.12f}")
    print(f"  [REPORT] Q_PDG - 2/3 = {Q_pdg - 2 / 3:+.12e}")
    print("  [REPORT] Comparator values are observational inputs and are not thresholded.")

    section("Scope boundaries")
    scope = [
        "not a derivation or adoption of the per-outcome-cell condition",
        "not a componentwise equality in a fixed Cartesian basis",
        "not a Gaussian-moment route to r = 1/2",
        "not a link from the decoupled partition-cell arithmetic to r",
        "not a charged-lepton mass prediction or audit verdict",
    ]
    for statement in scope:
        print(f"  [SCOPE] {statement}")

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
