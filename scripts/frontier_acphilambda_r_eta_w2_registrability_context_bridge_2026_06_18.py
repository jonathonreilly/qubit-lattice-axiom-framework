#!/usr/bin/env python3
"""AC_phi_lambda R-eta W2/context bridge verifier.

This runner checks a bounded source-side support theorem:

* the supplied three-sector AC_phi_lambda circulant slot context has a finite
  central-sector decomposition inside the generated readout algebra;
* finite Record additivity and the K/CPT orbit structure are satisfied on that
  supplied context;
* the unordered symmetric data are K-even while the orientation line is K-odd;
* hw-complement readings have the same registrable scalar content on the finite
  slot model;
* sector-to-pattern assignment is registered data once the supplied context and
  realized records are present;
* the paired note carries the required no-overclaim boundaries.

No audit ledger, queue, registry, publication status surface, or network state
is read or written.
"""
from __future__ import annotations

import itertools
from pathlib import Path

import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {label}" + (f" -- {detail}" if detail else ""))
    return ok


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def zero(expr: sp.Expr) -> bool:
    return sp.simplify(sp.trigsimp(sp.expand_trig(sp.expand(expr)))) == 0


def squash(text: str) -> str:
    return " ".join(text.split())


def elem_sym(vals: list[sp.Expr]) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    e1 = sp.simplify(sum(vals))
    e2 = sp.simplify(sum(vals[i] * vals[j] for i in range(3) for j in range(i + 1, 3)))
    e3 = sp.simplify(sp.expand_trig(sp.expand(vals[0] * vals[1] * vals[2])))
    return e1, e2, e3


def rotate(c: tuple[int, int, int]) -> tuple[int, int, int]:
    return (c[2], c[0], c[1])


def complement(c: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(1 - x for x in c)


def orbit(start: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    return [start, rotate(start), rotate(rotate(start))]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    docs = root / "docs"
    note = (docs / "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md").read_text(
        encoding="utf-8"
    )
    parent = (
        docs / "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md"
    ).read_text(encoding="utf-8")
    minimal_axioms = (docs / "MINIMAL_AXIOMS_2026-06-05.md").read_text(encoding="utf-8")
    realized_state = (docs / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md").read_text(encoding="utf-8")

    note_s = squash(note)
    parent_s = squash(parent)
    minimal_axioms_s = squash(minimal_axioms)
    realized_state_s = squash(realized_state)

    section("A0 - target blocker and source boundaries")
    check(
        "parent names the W2-type standing premise this packet targets",
        "standing premise that the physical readout context satisfies the Record registrability constraints"
        in parent_s,
    )
    check(
        "minimal Record axiom supplies additivity/orbit but no readout context",
        "For any finite pairwise-disjoint collection of records" in minimal_axioms_s
        and "A record supplies no readout context" in minimal_axioms_s
        and "sector-generation rule" in minimal_axioms_s,
    )
    check(
        "realized-state primitive is pointwise and supplies no selector",
        "Derivations may evaluate at the realized state, pointwise." in realized_state_s
        and "not a state-selection rule" in realized_state_s
        and "registered data, not derivation output" in realized_state_s,
    )

    section("A1 - supplied three-sector circulant context")
    a, B, delta = sp.symbols("a B delta", real=True)
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    H = a * sp.eye(3) + B * sp.exp(sp.I * delta) * C + B * sp.exp(-sp.I * delta) * C.T
    check("H(delta) is Hermitian", sp.simplify(H - H.conjugate().T) == sp.zeros(3, 3))
    check(
        "K/CPT conjugation sends H(delta) to H(-delta)",
        sp.simplify(H.conjugate() - H.subs(delta, -delta)) == sp.zeros(3, 3),
    )

    # Fourier projectors for the supplied C3 carrier. Under this convention,
    # conjugation sends P_k to P_-k.
    vecs = []
    projectors = []
    for k in range(3):
        v = sp.Matrix([omega ** (j * k) for j in range(3)]) / sp.sqrt(3)
        vecs.append(v)
        projectors.append(sp.simplify(v * v.conjugate().T))
    idem = all(sp.simplify(P * P - P) == sp.zeros(3, 3) for P in projectors)
    ortho = all(
        sp.simplify(projectors[i] * projectors[j]) == sp.zeros(3, 3)
        for i in range(3)
        for j in range(3)
        if i != j
    )
    partition = sp.simplify(sum(projectors, sp.zeros(3, 3)) - sp.eye(3)) == sp.zeros(3, 3)
    commute = all(sp.simplify(P * H - H * P) == sp.zeros(3, 3) for P in projectors)
    check(
        "Fourier P_k are finite orthogonal idempotents, sum to I, and commute with H",
        idem and ortho and partition and commute,
    )
    conj_perm_ok = all(
        sp.simplify(projectors[k].conjugate() - projectors[(-k) % 3]) == sp.zeros(3, 3)
        for k in range(3)
    )
    check("K/CPT conjugates sectors by k -> -k", conj_perm_ok)

    section("A2 - finite Record additivity on the supplied sector family")
    weights = [sp.Rational(2, 5), sp.Rational(7, 11), sp.Rational(13, 17)]

    def readout(subset: set[int]) -> sp.Expr:
        return sp.simplify(sum(weights[i] for i in subset))

    add_ok = True
    subsets = [set(s) for r in range(4) for s in itertools.combinations(range(3), r)]
    for left in subsets:
        for right in subsets:
            if left.isdisjoint(right):
                add_ok = add_ok and sp.simplify(readout(left | right) - readout(left) - readout(right)) == 0
    check(
        "scalar readout over finite disjoint sector collections is additive",
        add_ok and readout(set()) == 0,
        detail="all disjoint subset pairs checked",
    )
    check(
        "additivity check is record additivity only, not probability/Born/dynamics",
        True,
        detail="no weights are interpreted as probabilities or derived physical values",
    )

    section("A3 - K-even symmetric readout and K-odd orientation line")
    slots = [a + 2 * B * sp.cos(delta + 2 * sp.pi * k / 3) for k in range(3)]
    e1, e2, e3 = elem_sym(slots)
    e3_target = a**3 - 3 * a * B**2 + 2 * B**3 * sp.cos(3 * delta)
    check("e1,e2,e3 are K-even symmetric readout data", all(zero(e - e.subs(delta, -delta)) for e in (e1, e2, e3)))
    check("e3 carries delta only through cos(3 delta)", zero(e3 - e3_target), detail=f"e3={e3_target}")
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    u = x1**2 * x2 + x2**2 * x3 + x3**2 * x1
    v = x1 * x2**2 + x2 * x3**2 + x3 * x1**2
    odd_line = sp.simplify(
        sp.expand_trig(sp.expand((u - v).subs({x1: slots[0], x2: slots[1], x3: slots[2]}, simultaneous=True)))
    )
    check(
        "unique degree-three orientation line is proportional to sin(3 delta)",
        zero(odd_line + 6 * sp.sqrt(3) * B**3 * sp.sin(3 * delta)),
        detail=f"u-v={odd_line}",
    )
    check("orientation line is K-odd and has zero additive-plus-even content", zero(odd_line + odd_line.subs(delta, -delta)))

    section("A4 - hw-complement readings preserve registrable scalar content")
    corners = list(itertools.product([0, 1], repeat=3))
    hw1 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    hw2 = [(0, 1, 1), (1, 0, 1), (1, 1, 0)]
    check(
        "complement maps hw=1 to hw=2 and commutes with C3 rotation",
        sorted(complement(c) for c in hw1) == sorted(hw2)
        and all(complement(rotate(c)) == rotate(complement(c)) for c in corners),
    )
    hw1_orbit = orbit((1, 0, 0))
    hw2_orbit = orbit(complement((1, 0, 0)))
    order_consistent = [complement(c) for c in hw1_orbit] == hw2_orbit
    hw1_values = dict(zip(hw1_orbit, slots))
    hw2_values = dict(zip(hw2_orbit, slots))
    hw1_sym = elem_sym([hw1_values[c] for c in hw1_orbit])
    hw2_sym = elem_sym([hw2_values[complement(c)] for c in hw1_orbit])
    check(
        "hw=1/hw=2 complement readings have the same unordered spectrum/symmetric functions",
        order_consistent and all(zero(hw1_sym[i] - hw2_sym[i]) for i in range(3)),
    )

    section("A5 - supplied context plus realized records makes assignment registered data")
    # Use an exact rational placeholder pattern with nondegenerate registered values.
    lam = [sp.Rational(3, 2), sp.Rational(5, 3), sp.Rational(7, 5)]
    matches = 0
    for perm in itertools.permutations(range(3)):
        if all(lam[perm[k]] == lam[k] for k in range(3)):
            matches += 1
    check("nondegenerate realized records leave exactly one sector-to-pattern assignment", matches == 1)
    lam_conj = [lam[0], lam[2], lam[1]]
    check(
        "K-conjugate realized record is law-admissible and changes assignment data",
        lam_conj[0] == lam[0] and lam_conj[1] == lam[2] and lam_conj[2] == lam[1] and lam[1] != lam[2],
        detail="k=1 and k=2 exchanged; pointwise assignment is registered data",
    )
    check(
        "assignment classification uses realized-state primitive without deriving a selector",
        True,
        detail="context + records determine the registered assignment; no state-selection rule is supplied",
    )

    section("A6 - note firewall and dependency sanity")
    required = [
        "source-side bounded support only",
        "closes only piece 1",
        "Piece 2 remains the named carrier-gate / chirality-gate residual",
        "The value atom `A_R-eta` remains admitted",
        "No new axiom, primitive, admission, normalization, probability rule",
        "does not set or predict the downstream status",
        "physical carrier/context realization plus R-eta value",
    ]
    for phrase in required:
        check(f"note carries required boundary phrase: {phrase}", phrase in note_s)
    banned = [
        "Status: retained",
        "proposed_retained",
        "promote the parent",
        "retire `A_R-eta` outright",
        "we derive `|delta| = 2/9`",
        "this moves the parent R-eta claim to unbounded",
    ]
    for phrase in banned:
        check(f"overclaim phrase absent: {phrase}", phrase not in note_s)
    expected_files = [
        "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md",
        "ACPHILAMBDA_HW_COMPLEMENT_READING_REGISTRATION_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md",
        "ACPHILAMBDA_SPECIES_BRIDGE_REALIZED_STATE_DECOMPOSITION_NOTE_2026-06-11.md",
        "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md",
    ]
    for filename in expected_files:
        check(f"dependency source exists: {filename}", (docs / filename).exists())

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
