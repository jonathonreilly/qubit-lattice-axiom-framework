#!/usr/bin/env python3
"""COLOR_GENERATION_Z3_IDENTIFICATION_NO_GO derivation runner (2026-06-05).

Runner for docs/COLOR_GENERATION_Z3_IDENTIFICATION_NO_GO_2026-06-05.md.

Result (bounded no-go):

    The color-SU(3) carrier and the generation carrier cannot be identified
    as the same abstract Z_3 representation, because their Z_3 characters are
    inequivalent. Physical SM color/generation identification remains a separate
    bridge question.

Adopted premises (cited by name): the color and generation carrier provenance
from Lattice/Quantum structure. The two carriers and their Z_3 actions are:

  * Color carrier B_sym -- the 3-dim symmetric base of the (b1,b2,b3) qubit
    triple (fiber b3 factored as (x) I_2), from the cited
    cl3_color_automorphism_theorem:

        B_sym = span{ |00>, |11>, (|01>+|10>)/sqrt2 }.

    The SU(3)_c center element acts on this triplet as the scalar w * I_3,
    giving the Z_3 character chi_color = (3, 3w, 3w^2) = 3 * chi_w.

  * Generation carrier G -- the hw=1 corner orbit {e1,e2,e3} of the Brillouin
    zone {0,pi}^3, from cl3_taste_generation_theorem.  The generation C_3 is
    the derived cubic axis cycle e1->e2->e3->e1, the regular representation,
    giving the Z_3 character chi_gen = (3, 0, 0) = chi_0 + chi_w + chi_w2.

This runner reconstructs both characters from first principles (it does NOT
import the value from any note) and computes the obstruction:

  1. both Z_3 characters at every group element (e, g, g^2);
  2. their inequivalence by trace comparison at the non-identity elements
     (3w vs 0);
  3. the chi_w multiplicities: 3 in the color rep, 1 in the generation rep;
  4. the Schur obstruction: dim Hom_{Z_3}(generation, color) = 3 (all of it in
     the single shared chi_w line), yet every intertwiner has rank <= 1, so no
     equivariant isomorphism exists;
  5. the precise import that WOULD identify the abstract representations
     (stipulate the generation Z_3 to
     act as w * I_3, discarding the derived axis-cycle), shown to be a
     non-native stipulation -- an import, not a consequence of the named
     premises alone.

Reproduce:
    PYTHONPATH=scripts python3 \
        scripts/color_generation_z3_identification_no_go_2026_06_05.py

Target: PASS >= 15, FAIL = 0.
"""

from __future__ import annotations

import sys

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    line = f"  [{tag}] {label}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return cond


def section(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# ---------------------------------------------------------------------------
# Shared algebra: primitive cube root of unity in algebraic form so that the
# cube-root identities (1 + w + w^2 = 0) reduce exactly under simplification.
# ---------------------------------------------------------------------------

W = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2   # symbolic w = exp(2 pi i / 3)
wn = complex(W)                                  # numeric w


def cycle_P() -> sp.Matrix:
    """Generation Z_3 generator: axis cycle e1->e2->e3->e1 (regular rep)."""
    return sp.Matrix([[0, 0, 1],
                      [1, 0, 0],
                      [0, 1, 0]])


def center_scalar() -> sp.Matrix:
    """Color SU(3)_c center generator on the triplet B_sym: scalar w * I_3."""
    return W * sp.eye(3)


def char_vector(gen: sp.Matrix) -> tuple:
    """Z_3 character (chi(e), chi(g), chi(g^2)) of a 3x3 order-3 generator."""
    return (sp.simplify(sp.trace(sp.eye(3))),
            sp.simplify(sp.trace(gen)),
            sp.simplify(sp.trace(gen * gen)))


def irr_chars() -> dict:
    """The three Z_3 irreducible characters, on (e, g, g^2)."""
    return {
        "chi_0": (sp.Integer(1), sp.Integer(1), sp.Integer(1)),
        "chi_w": (sp.Integer(1), W, W**2),
        "chi_w2": (sp.Integer(1), W**2, W**4),
    }


def _reduce(expr):
    """Force algebraic reduction of cube-root-of-unity expressions to 0/int."""
    return sp.nsimplify(sp.simplify(sp.expand(sp.expand_complex(expr))),
                        rational=False)


def decompose(chi: tuple) -> dict:
    """Multiplicity m(irr) = <chi, chi_irr> of each Z_3 irrep in character chi."""
    out = {}
    for name, ic in irr_chars().items():
        m = sp.Rational(1, 3) * sum(
            chi[k] * sp.conjugate(ic[k]) for k in range(3)
        )
        out[name] = _reduce(m)
    return out


# ===========================================================================
# Step 1: the two Z_3 characters, reconstructed from the native carriers
# ===========================================================================

def step1_characters() -> tuple:
    section("STEP 1: NATIVE Z_3 CHARACTERS (color center scalar vs generation cycle)")

    P = cycle_P()
    Z = center_scalar()

    # Both generators are genuine order-3 elements.
    check("Generation generator P is order 3 (P^3 = I), det P = 1",
          sp.simplify(P**3 - sp.eye(3)) == sp.zeros(3, 3) and P.det() == 1)
    check("Color center generator Z is order 3 (Z^3 = I)",
          sp.simplify(Z**3 - sp.eye(3)) == sp.zeros(3, 3))

    chi_gen = char_vector(P)
    chi_col = char_vector(Z)

    # Color carrier: SU(3)_c center acts as scalar w on B_sym => (3, 3w, 3w^2).
    check("Color character chi_color = (3, 3w, 3w^2)",
          _reduce(chi_col[0] - 3) == 0
          and _reduce(chi_col[1] - 3 * W) == 0
          and _reduce(chi_col[2] - 3 * W**2) == 0,
          f"numerically (3, {complex(chi_col[1]):.3f}, {complex(chi_col[2]):.3f})")

    # Generation carrier: axis cycle is fixed-point-free => regular character.
    check("Generation character chi_gen = (3, 0, 0)",
          chi_gen == (3, 0, 0), str(chi_gen))

    return chi_gen, chi_col


# ===========================================================================
# Step 2: inequivalence by trace comparison at each group element
# ===========================================================================

def step2_inequivalence(chi_gen: tuple, chi_col: tuple) -> None:
    section("STEP 2: INEQUIVALENCE (trace comparison at each group element)")

    # The trace (character value) is a similarity invariant, so two reps are
    # isomorphic iff their characters agree at EVERY group element.
    eq_e = _reduce(chi_col[0] - chi_gen[0]) == 0
    eq_g = _reduce(chi_col[1] - chi_gen[1]) == 0
    eq_g2 = _reduce(chi_col[2] - chi_gen[2]) == 0

    check("At e: chi_color(e) = chi_gen(e) = 3 (same dimension)",
          eq_e, "both 3-dimensional")
    check("At g: chi_color(g) = 3w  != chi_gen(g) = 0  (THEY DIFFER)",
          (not eq_g) and _reduce(chi_col[1] - 3 * W) == 0 and chi_gen[1] == 0,
          f"3w = {complex(3*W):.3f} vs 0")
    check("At g^2: chi_color(g^2) = 3w^2 != chi_gen(g^2) = 0 (THEY DIFFER)",
          (not eq_g2) and _reduce(chi_col[2] - 3 * W**2) == 0 and chi_gen[2] == 0,
          f"3w^2 = {complex(3*W**2):.3f} vs 0")

    # |trace| is a basis-independent class invariant.
    check("|chi_color(g)| = 3 (scalar) but |chi_gen(g)| = 0 (fixed-point-free)",
          abs(complex(_reduce(chi_col[1]))) > 2.99
          and abs(complex(chi_gen[1])) < 1e-9)

    check("Characters differ at g => generation and color reps are INEQUIVALENT",
          (not eq_g) or (not eq_g2))

    # The only automorphism of Z_3 (relabel g <-> g^2) sends the color
    # character to (3, 3w^2, 3w), still != (3, 0, 0): no relabel rescues it.
    auto_col = (sp.Integer(3), 3 * W**2, 3 * W)
    check("Z_3 generator relabel g->g^2 gives (3,3w^2,3w) != (3,0,0)",
          auto_col != (3, 0, 0))


# ===========================================================================
# Step 3: chi_w multiplicities (3 in color, 1 in generation)
# ===========================================================================

def step3_multiplicities(chi_gen: tuple, chi_col: tuple) -> None:
    section("STEP 3: chi_w MULTIPLICITIES (3 in color vs 1 in generation)")

    d_col = decompose(chi_col)
    d_gen = decompose(chi_gen)

    check("Color rep = 3 * chi_w  (chi_0 and chi_w2 absent)",
          _reduce(d_col["chi_w"] - 3) == 0
          and _reduce(d_col["chi_0"]) == 0
          and _reduce(d_col["chi_w2"]) == 0,
          str({k: sp.sstr(v) for k, v in d_col.items()}))

    check("Generation rep = chi_0 + chi_w + chi_w2 (each multiplicity 1)",
          all(_reduce(d_gen[k] - 1) == 0 for k in d_gen),
          str({k: sp.sstr(v) for k, v in d_gen.items()}))

    check("Multiplicity of chi_w: 3 (color) != 1 (generation)",
          _reduce(d_col["chi_w"] - 3) == 0
          and _reduce(d_gen["chi_w"] - 1) == 0)

    # The multiplicity of any single irrep is a complete isomorphism invariant
    # for Z_3 reps; differing chi_w multiplicity alone forbids isomorphism.
    check("Differing chi_w multiplicity (3 vs 1) alone forbids isomorphism",
          _reduce(d_col["chi_w"] - d_gen["chi_w"]) != 0)


# ===========================================================================
# Step 4: Schur obstruction -- dim Hom = 1, every intertwiner has rank <= 1
# ===========================================================================

def step4_schur(chi_gen: tuple, chi_col: tuple) -> None:
    section("STEP 4: SCHUR OBSTRUCTION (Hom rank <= 1, no equivariant iso)")

    P = np.array(cycle_P().tolist(), dtype=complex)   # generation generator
    Z = wn * np.eye(3)                                 # color generator

    # Hom_{Z_3}(generation, color) = { T : Z T = T P }.  By Schur its dimension
    # is sum_irr m_gen(irr) * m_col(irr) = m_gen(chi_w) * m_col(chi_w) = 1*3 = 3
    # (the only shared irrep is chi_w: present once in the regular rep, three
    # times in the color scalar rep).  Every such T factors through the single
    # chi_w line in the regular rep, so its image is at most that 1-dim line:
    # rank <= 1.  Solve the linear system Z T P^{-1} - T = 0 on vec(T) in C^9.
    Pin = np.linalg.inv(P)
    L = np.kron(Pin.T, Z) - np.eye(9)
    U, sv, Vh = np.linalg.svd(L)
    null = Vh[np.where(sv < 1e-9)[0]]
    hom_dim = null.shape[0]

    check("dim Hom_{Z3}(generation, color) = 3 (= m_gen(chi_w)*m_col(chi_w) = 1*3)",
          hom_dim == 3, f"dim={hom_dim}")

    # Every intertwiner factors through the single shared chi_w line, hence has
    # rank <= 1 and is therefore NOT invertible: no equivariant isomorphism.
    max_rank = 0
    for nv in null:
        T = nv.reshape(3, 3)
        max_rank = max(max_rank, int(np.linalg.matrix_rank(T, tol=1e-9)))
    check("Every equivariant map generation->color has rank <= 1 (Schur)",
          max_rank <= 1, f"max rank over Hom = {max_rank}")
    check("Rank <= 1 < 3 => NO Z_3-equivariant ISOMORPHISM (Schur's lemma)",
          max_rank < 3)

    # Cross-check the other direction: dim Hom(color, generation) is also
    # m_col(chi_w)*m_gen(chi_w) = 3*1 = 3, but again only rank-1 maps exist, so
    # neither direction yields an isomorphism (an iso would need rank 3).
    Zin = np.linalg.inv(Z)
    L2 = np.kron(Zin.T, P) - np.eye(9)  # { S : P S = S Z }
    U2, sv2, Vh2 = np.linalg.svd(L2)
    null2 = Vh2[np.where(sv2 < 1e-9)[0]]
    max_rank2 = 0
    for nv in null2:
        max_rank2 = max(max_rank2,
                        int(np.linalg.matrix_rank(nv.reshape(3, 3), tol=1e-9)))
    check("dim Hom(color, generation) = 3 but every such map also has rank <= 1",
          null2.shape[0] == 3 and max_rank2 <= 1,
          f"dim={null2.shape[0]}, max rank={max_rank2}")


# ===========================================================================
# Step 5: the precise import that WOULD bridge it -- and that it is an import
# ===========================================================================

def step5_named_import() -> None:
    section("STEP 5: THE NAMED IMPORT 'scalar-generation-action' (an import, not a derivation)")

    P = np.array(cycle_P().tolist(), dtype=complex)
    Z = wn * np.eye(3)

    # The ONLY way to make the characters agree is to REPLACE the derived
    # generation action P (axis cycle) by the scalar action w * I_3 on the
    # hw=1 orbit.  That stipulation -- 'scalar-generation-action' -- discards
    # the cubic-symmetry provenance of the generation Z_3.
    stip = wn * np.eye(3)
    chi_stip = (np.trace(np.eye(3)), np.trace(stip), np.trace(stip @ stip))

    check("Stipulated scalar generation action has character (3, 3w, 3w^2)",
          abs(chi_stip[0] - 3) < 1e-9
          and abs(chi_stip[1] - 3 * wn) < 1e-9
          and abs(chi_stip[2] - 3 * wn**2) < 1e-9,
          "matches the color center scalar trivially")

    check("...but it discards the derived axis cycle P (different operator)",
          not np.allclose(stip, P, atol=1e-9),
          "w*I_3 != axis-cycle permutation => a non-native stipulation = IMPORT")

    # Without that import the bridge fails: equal determinant is necessary but
    # not sufficient (det P = 1 = w^3 = det Z), so determinant cannot rescue it.
    check("det(P) = 1 = w^3 = det(Z): equal determinant is necessary, NOT sufficient",
          abs(np.linalg.det(P) - 1) < 1e-9 and abs(np.linalg.det(Z) - 1) < 1e-9)


def main() -> int:
    print("=" * 78)
    print("COLOR_GENERATION_Z3_IDENTIFICATION_NO_GO  (derivation runner)")
    print("=" * 78)
    print("Premises: cited color and generation carrier provenance.")
    print("Result: the supplied color-carrier and generation-carrier Z_3 actions")
    print("        cannot be identified because their characters are inequivalent.")

    chi_gen, chi_col = step1_characters()
    step2_inequivalence(chi_gen, chi_col)
    step3_multiplicities(chi_gen, chi_col)
    step4_schur(chi_gen, chi_col)
    step5_named_import()

    # ----------------------------------------------------------------------
    # Hard class-A assertions: the load-bearing facts must hold exactly.
    # ----------------------------------------------------------------------
    section("CLASS-A ASSERTIONS")
    P = cycle_P()
    Z = center_scalar()
    assert char_vector(P) == (3, 0, 0)
    assert _reduce(char_vector(Z)[1] - 3 * W) == 0
    d_col = decompose(char_vector(Z))
    d_gen = decompose(char_vector(P))
    assert _reduce(d_col["chi_w"] - 3) == 0
    assert _reduce(d_col["chi_0"]) == 0 and _reduce(d_col["chi_w2"]) == 0
    assert _reduce(d_gen["chi_w"] - 1) == 0
    assert _reduce(d_col["chi_w"] - d_gen["chi_w"]) != 0  # 3 != 1
    print("  [PASS] color = 3*chi_w, generation = chi_0+chi_w+chi_w2;")
    print("         chi_w multiplicity 3 != 1; characters inequivalent (class-A)")

    print()
    print("=" * 78)
    print(f"COLOR_GENERATION_Z3_IDENTIFICATION_NO_GO: PASS={PASS} FAIL={FAIL}")
    print("VERDICT: BOUNDED NO-GO -- the color center scalar rep 3*chi_w (3, 3w, 3w^2)")
    print("  and the generation regular rep chi_0+chi_w+chi_w2 (3, 0, 0) are")
    print("  INEQUIVALENT Z_3 representations: their characters differ at the")
    print("  non-identity elements (3w vs 0), chi_w multiplicity is 3 vs 1, and")
    print("  every Z_3 intertwiner has rank <= 1 (Schur), so no equivariant")
    print("  isomorphism exists. This is an abstract carrier no-identification")
    print("  boundary only: physical SM color and generation labels still require")
    print("  separate bridge theorems. Forcing an identification requires the named")
    print("  non-native import 'scalar-generation-action' (replace the derived axis")
    print("  cycle by w*I).")
    print("=" * 78)

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
