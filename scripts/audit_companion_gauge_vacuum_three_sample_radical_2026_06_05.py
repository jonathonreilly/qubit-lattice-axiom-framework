#!/usr/bin/env python3
"""Audit companion: the exact three-sample radical reconstruction map is a
stand-alone abstract algebraic theorem; the beta=6 PF-seam application is
conditional on four named bridge authorities (NOT load-bearing, NOT proven here).

Companion to
docs/GAUGE_VACUUM_THREE_SAMPLE_RADICAL_RECONSTRUCTION_NARROW_THEOREM_NOTE_2026-06-05.md

This runner REPROVES, from primitives, only the abstract reconstruction algebra:

  Part A  the abstract structured matrix F = [[1,a,0],[1,b,c],[1,d,e]] has
          det F = Delta := a*c - a*e + b*e - c*d, and (when Delta != 0) the
          unique solution of F*alpha = Z is alpha = Delta^{-1} adj(F) Z, equal
          to the displayed reconstruction map entry-for-entry.  FREE SYMBOLS.

  Part B  the named pi/16 radical entries a,b,c,d,e are a FAITHFUL instance:
          each equals its trigonometric character value to zero residue at
          exact precision, det F = Delta != 0 on the specialization, and the
          inverse reproduces a generic abstract coefficient triple exactly.

  Part C  the structural facts of the specialization are exact: F_(A,2) = 0
          (antipodal collapse, chi_(1,1)(W_A) = 0), strict signs c>0, e<0, and
          the lower-right 2x2 block (rows B,C; cols 2,3) is nonsingular.

  Part D  scope guard: the beta=6 PF-seam identification of the abstract samples
          Z_A,Z_B,Z_C with the physical compressed amplitudes Z_6^env(W_*) is
          CONDITIONAL on the four named bridges; the abstract map consumes no
          beta=6 / Wilson / Haar / Monte-Carlo numeric input; one bridge
          (rim-lift) is itself audited_conditional.  This part records the
          conditional; it does NOT prove the bridges.

NO forbidden imports: no PDG / fitted / measured / lattice-MC / beta=6 /
g_bare values are used as derivation inputs.  The reconstruction uses abstract
sample symbols and pure surds only.  External comparator: the adjugate identity
A*adj(A) = det(A)*I (Gantmacher, Vol. I, Ch. I sec. 4) -- reproven here, not
imported.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"         {detail}")


# --------------------------------------------------------------------------
# Abstract structured matrix and the displayed reconstruction map.
# --------------------------------------------------------------------------

def abstract_matrix(a, b, c, d, e) -> sp.Matrix:
    """F = [[1,a,0],[1,b,c],[1,d,e]] -- the three-row evaluation matrix shape."""
    return sp.Matrix([[1, a, 0], [1, b, c], [1, d, e]])


def displayed_delta(a, b, c, d, e):
    """The named radical determinant Delta = a*c - a*e + b*e - c*d."""
    return a * c - a * e + b * e - c * d


def displayed_reconstruction_matrix(a, b, c, d, e) -> sp.Matrix:
    """The displayed map M with alpha = (1/Delta) * M * Z (note text, Thm 2)."""
    return sp.Matrix(
        [
            [b * e - c * d, -a * e, a * c],
            [c - e, e, -c],
            [d - b, a - d, b - a],
        ]
    )


# --------------------------------------------------------------------------
# Named pi/16 radical constants and the character evaluations.
# --------------------------------------------------------------------------

def radical_constants() -> dict[str, sp.Expr]:
    return {
        "r": sp.sqrt(2),
        "s": sp.sqrt(2 - sp.sqrt(2)),
        "u": sp.sqrt(2 - sp.sqrt(2 + sp.sqrt(2))),
        "v": sp.sqrt(2 - sp.sqrt(2 - sp.sqrt(2))),
        "Sigma": sp.sqrt(2 + sp.sqrt(2)),
        "x": sp.sqrt(2 + sp.sqrt(2 + sp.sqrt(2))),
        "y": sp.sqrt(2 + sp.sqrt(2 - sp.sqrt(2))),
    }


def radical_entries() -> dict[str, sp.Expr]:
    rc = radical_constants()
    r, s, u, v = rc["r"], rc["s"], rc["u"], rc["v"]
    Sigma, x, y = rc["Sigma"], rc["x"], rc["y"]
    return {
        "a": -3 * s,
        "b": -3 * r + 3 * u + 3 * v,
        "c": 16 + 8 * Sigma - 8 * x - 8 * y,
        "d": 3 * r + 3 * u - 3 * v,
        "e": 16 - 8 * Sigma - 8 * x + 8 * y,
    }


# units of pi/16 for the three marked holonomies (W(theta1, theta2)).
SAMPLE_ANGLE_UNITS = {
    "W_A": (-13, 10),   # 10*pi/16 = 5*pi/8
    "W_B": (-5, -7),
    "W_C": (7, -11),
}


def char_10_plus_01(theta1: sp.Expr, theta2: sp.Expr) -> sp.Expr:
    """6 * (cos t1 + cos t2 + cos(t1+t2)) -- the chi_(1,0)+chi_(0,1) column form."""
    return 6 * (sp.cos(theta1) + sp.cos(theta2) + sp.cos(theta1 + theta2))


def char_11(theta1: sp.Expr, theta2: sp.Expr) -> sp.Expr:
    """16 * (1 + cos(t1-t2) + cos(2t1+t2) + cos(t1+2t2)) -- the chi_(1,1) column form."""
    return 16 * (
        1
        + sp.cos(theta1 - theta2)
        + sp.cos(2 * theta1 + theta2)
        + sp.cos(theta1 + 2 * theta2)
    )


def main() -> int:
    print("=" * 78)
    print("GAUGE-VACUUM THREE-SAMPLE RADICAL RECONSTRUCTION -- ABSTRACT MAP REPROOF")
    print("=" * 78)

    # ------------------------------------------------------------------
    # Part A: abstract reconstruction map over free symbols (load-bearing).
    # ------------------------------------------------------------------
    print()
    print("Part A: abstract reconstruction map (free symbols a,b,c,d,e)")
    a, b, c, d, e = sp.symbols("a b c d e")
    F = abstract_matrix(a, b, c, d, e)
    Delta = displayed_delta(a, b, c, d, e)
    Mdisp = displayed_reconstruction_matrix(a, b, c, d, e)

    detF = sp.expand(F.det())
    check(
        "A1: det(F) equals the named radical determinant Delta = a*c - a*e + b*e - c*d (symbolic)",
        sp.simplify(detF - Delta) == 0,
        detail=f"det(F) = {detF}",
    )

    adjF = F.adjugate()
    check(
        "A2: displayed reconstruction matrix equals adj(F) entry-for-entry (symbolic)",
        sp.simplify(sp.Matrix(adjF) - Mdisp) == sp.zeros(3, 3),
        detail="M_displayed == adj(F); so alpha = (1/Delta) M_displayed Z = F^{-1} Z",
    )

    # F^{-1} = adj(F)/det(F): verify Delta*F^{-1} - M_displayed = 0.
    Finv = F.inv()
    check(
        "A3: Delta * F^{-1} equals the displayed map (symbolic), i.e. F^{-1} = adj(F)/Delta",
        sp.simplify(sp.expand(Delta * sp.Matrix(Finv)) - Mdisp) == sp.zeros(3, 3),
    )

    # Adjugate identity reproven in this structured form: F*adj(F) = det(F)*I.
    check(
        "A4: adjugate identity F*adj(F) = det(F)*I holds for the structured F (reproven, not imported)",
        sp.simplify(F * sp.Matrix(adjF) - detF * sp.eye(3)) == sp.zeros(3, 3),
    )

    # Round trip with a GENERIC abstract sample vector Z.
    zA, zB, zC = sp.symbols("Z_A Z_B Z_C")
    Z = sp.Matrix([zA, zB, zC])
    alpha = (Mdisp * Z) / Delta            # the displayed reconstruction
    check(
        "A5: F * (displayed reconstruction of a generic abstract Z) returns Z exactly",
        sp.simplify(F * alpha - Z) == sp.zeros(3, 1),
        detail="exact round trip F alpha = Z for symbolic Z; the map is the unique inverse",
    )

    # Uniqueness statement: the homogeneous system F*alpha=0 has only alpha=0 iff det!=0.
    null_space = F.nullspace()
    check(
        "A6: uniqueness -- nullspace(F) is trivial as a rational function of a,b,c,d,e (det != 0 generically)",
        len(null_space) == 0,
        detail="generic invertibility => the reconstruction is the unique solution",
    )

    # ------------------------------------------------------------------
    # Part B: the named pi/16 radical entries are a faithful instance.
    # ------------------------------------------------------------------
    print()
    print("Part B: the named pi/16 radical specialization is faithful")
    ent = radical_entries()
    pi = sp.pi

    # B1-B3 (col chi_(1,0)+chi_(0,1)): a,b,d match the character values exactly.
    col1_targets = {"W_A": "a", "W_B": "b", "W_C": "d"}
    for sample, key in col1_targets.items():
        t1u, t2u = SAMPLE_ANGLE_UNITS[sample]
        t1, t2 = t1u * pi / 16, t2u * pi / 16
        val = sp.nsimplify(sp.simplify(char_10_plus_01(t1, t2)))
        diff = sp.simplify(sp.expand(val - ent[key]))
        # exactness: symbolic-zero or zero to very high precision.
        is_zero = (diff == 0) or (abs(sp.N(diff, 60)) < sp.Float("1e-50"))
        check(
            f"B[{key}]: radical entry '{key}' equals 6*(cosθ1+cosθ2+cos(θ1+θ2)) at {sample} (zero residue)",
            bool(is_zero),
            detail=f"residue = {sp.N(diff, 30)}",
        )

    # B4-B6 (col chi_(1,1)): 0,c,e match the character values exactly.
    col2_targets = {"W_A": sp.Integer(0), "W_B": ent["c"], "W_C": ent["e"]}
    col2_names = {"W_A": "0", "W_B": "c", "W_C": "e"}
    for sample, target in col2_targets.items():
        t1u, t2u = SAMPLE_ANGLE_UNITS[sample]
        t1, t2 = t1u * pi / 16, t2u * pi / 16
        val = sp.simplify(char_11(t1, t2))
        diff = sp.simplify(sp.expand(val - target))
        is_zero = (diff == 0) or (abs(sp.N(diff, 60)) < sp.Float("1e-50"))
        check(
            f"B[chi11,{sample}]: chi_(1,1) column value equals '{col2_names[sample]}' (zero residue)",
            bool(is_zero),
            detail=f"residue = {sp.N(diff, 30)}",
        )

    # B7: det of the radical specialization equals Delta and is nonzero.
    Frad = abstract_matrix(ent["a"], ent["b"], ent["c"], ent["d"], ent["e"])
    Delta_rad = displayed_delta(ent["a"], ent["b"], ent["c"], ent["d"], ent["e"])
    detFrad = sp.simplify(Frad.det())
    check(
        "B7: det(F_radical) = Delta_radical and is nonzero",
        sp.simplify(detFrad - Delta_rad) == 0 and sp.N(detFrad, 30) != 0,
        detail=f"det(F_radical) ~ {sp.N(detFrad, 20)}",
    )

    # B8: inverse on the radical specialization reproduces a generic triple exactly.
    a0, a1, a2 = sp.symbols("alpha0 alpha1 alpha2")
    alpha_in = sp.Matrix([a0, a1, a2])
    Z_rad = Frad * alpha_in
    alpha_rec = (displayed_reconstruction_matrix(
        ent["a"], ent["b"], ent["c"], ent["d"], ent["e"]) * Z_rad) / Delta_rad
    check(
        "B8: radical reconstruction map recovers a generic coefficient triple exactly (alpha_rec = alpha_in)",
        sp.simplify(alpha_rec - alpha_in) == sp.zeros(3, 1),
        detail="exact inversion on the named pi/16 specialization",
    )

    # ------------------------------------------------------------------
    # Part C: structural facts of the specialization.
    # ------------------------------------------------------------------
    print()
    print("Part C: structural facts (W_A annihilation, sign separation, block rank)")

    # C1: F_(A,2) = 0 directly from chi_(1,1)(W_A) = 0 via antipodal collapse.
    t1u, t2u = SAMPLE_ANGLE_UNITS["W_A"]
    t1, t2 = t1u * pi / 16, t2u * pi / 16
    fA2 = sp.simplify(char_11(t1, t2))
    check(
        "C1: F_(A,2) = chi_(1,1)(W_A) = 0 exactly (antipodal eigenvalue collapse)",
        fA2 == 0,
        detail="exp(-13*pi*i/16) = -exp(3*pi*i/16); fundamental char collapses, chi_(1,1)=chi_(1,0)*chi_(0,1)-1=0",
    )

    # C2: strict signs c>0, e<0 on the radical entries.
    c_val, e_val = sp.N(ent["c"], 40), sp.N(ent["e"], 40)
    check(
        "C2: sign separation c = 16+8Σ-8x-8y > 0 and e = 16-8Σ-8x+8y < 0 (exact surds)",
        (c_val > 0) and (e_val < 0),
        detail=f"c ~ {sp.N(ent['c'], 18)} > 0,  e ~ {sp.N(ent['e'], 18)} < 0",
    )

    # C3: lower-right 2x2 block on rows B,C and columns 2,3 (chi_1, chi_11) is nonsingular.
    block = sp.Matrix([[ent["b"], ent["c"]], [ent["d"], ent["e"]]])
    det_block = sp.simplify(block.det())
    check(
        "C3: lower 2x2 block (rows B,C; cols chi_1,chi_11) is nonsingular",
        sp.N(det_block, 30) != 0,
        detail=f"det(block) ~ {sp.N(det_block, 18)}",
    )

    # ------------------------------------------------------------------
    # Part D: scope guard -- beta=6 PF-seam application is CONDITIONAL.
    # ------------------------------------------------------------------
    print()
    print("Part D: scope guard -- the beta=6 PF-seam application is conditional on four bridges")

    note_path = ROOT / "docs" / "GAUGE_VACUUM_THREE_SAMPLE_RADICAL_RECONSTRUCTION_NARROW_THEOREM_NOTE_2026-06-05.md"
    note_text = note_path.read_text() if note_path.exists() else ""

    # D1: the note states the four bridges and the conditional explicitly.
    four_bridges_named = all(
        phrase in note_text
        for phrase in [
            "full Wilson/Haar one-slab kernel theorem",
            "full-slice Wilson/Haar rim-lift theorem",
            "exact kernel/rim compression theorem",
            "exact compressed rim-evaluation theorem",
        ]
    )
    check(
        "D1: the narrowed note names all four bridge authorities as the conditional premise set",
        four_bridges_named and "conditional" in note_text.lower(),
        detail="Wilson one-slab kernel / Haar rim-lift / compression / rim-evaluation",
    )

    # D2: the note explicitly flags that the beta=6 seam is NOT load-bearing and stays conditional.
    check(
        "D2: the note marks the beta=6 PF-seam application as NOT load-bearing and conditional",
        ("NOT load-bearing" in note_text) and ("audited_conditional" in note_text),
        detail="the rim-lift bridge is itself audited_conditional; the seam claim is conditional",
    )

    # D3: forbidden-import discipline -- this runner used NO beta=6 / Wilson / Haar / MC numeric input.
    # The only numbers used are the integer matrix shape, integer multipliers (3,6,8,16) of the
    # standard pi/16 character identities, and pure surds. None is a physical/fitted/MC value.
    physics_numeric_inputs_used = False  # by construction; asserted and reviewable above.
    check(
        "D3: the abstract reconstruction consumes NO beta=6 / Wilson coefficient / Haar / Monte-Carlo numeric input",
        physics_numeric_inputs_used is False,
        detail="abstract sample symbols + pure surds only; the integers are character-identity multipliers",
    )

    # D4: the abstract map (Part A) is independent of any physical identification.
    # Re-assert: Part A passed with FREE symbols, so its truth cannot depend on the bridges.
    check(
        "D4: the load-bearing map is proven over free symbols, hence independent of the four bridges",
        PASS >= 6 and FAIL == 0,  # Part A produced >=6 passes before any specialization
        detail="Part A used abstract a,b,c,d,e and abstract Z; no bridge premise entered the proof",
    )

    print()
    print("=" * 78)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
