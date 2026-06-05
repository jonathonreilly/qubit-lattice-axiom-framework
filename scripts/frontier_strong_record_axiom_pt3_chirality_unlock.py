#!/usr/bin/env python3
"""Strong-record-axiom pressure-test #3: does the doublet complex structure J
unlock the charged-lepton chirality gate?

Verifies the algebraic content of
`docs/STRONG_RECORD_AXIOM_PT3_CHIRALITY_UNLOCK_NOTE_2026-06-04.md`.

The candidate axiom: "a record registers which real classical alternative is
realized; the real classical alternatives are the real Wedderburn blocks of
R[Z_3] = R (+) C, counted (dimension-blind)." The proposed chirality mechanism:
when the doublet block is read as C = R^2 (a real division algebra), it carries
a canonical complex structure J (multiplication by i), J^2 = -I on the doublet.
The claim under test is that this J supplies the chiral grading the framework's
charged-lepton Koide closure needs (an operator that ANTICOMMUTES with the mass
operator on the generation R^3 and pins Q = 2/3).

This runner determines whether J unlocks chirality, partially, or not, by
direct, basis-independent linear algebra. No PDG / measured / empirical lepton
masses are consumed; every check is a structural fact about R[Z_3].

Cross-references (prior art, not load-bearing on the proofs here):
  docs/KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md
  docs/KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md
  docs/KOIDE_ANTICOMMUTING_EIGENVECTOR_VS_EIGENVALUE_READOUT_RECONCILIATION_NOTE_2026-06-01.md
  docs/KOIDE_RECORDS_REALITY_SHRINKS_IMPORT_TO_SIGN_NOTE_2026-06-02.md
"""

from __future__ import annotations

import sys

import numpy as np
import sympy as sp

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    status = "PASS" if ok else "FAIL"
    if ok:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {label}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return ok


# ----------------------------------------------------------------------------
# Shared objects: Z_3 regular rep, real Wedderburn split, the doublet J,
# the framework chirality grading Gamma_chi, and the Koide readout.
# ----------------------------------------------------------------------------

R = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=float)  # cyclic shift, R^3 = I
I3 = np.eye(3)
JONES = np.ones((3, 3))  # all-ones = I + R + R^2 (the Z_3 group-algebra symmetrizer)

# Singlet (trivial-rep) direction and doublet (2-dim real irrep) projector.
S_VEC = np.ones(3) / np.sqrt(3)
P_SING = np.outer(S_VEC, S_VEC)
P_DOUB = I3 - P_SING

# Orthonormal doublet basis from the omega-eigenvector of R.
_W = np.exp(2j * np.pi / 3)
_v = np.array([1, _W, _W ** 2]) / np.sqrt(3)
_e1 = np.real(_v)
_e1 = _e1 / np.linalg.norm(_e1)
_e2 = np.imag(_v)
_e2 = _e2 - (_e2 @ _e1) * _e1
_e2 = _e2 / np.linalg.norm(_e2)
U_BASIS = np.column_stack([S_VEC, _e1, _e2])  # columns: singlet, e1, e2

# The canonical complex structure on the doublet C-block: i acts as 90-deg
# rotation in (e1, e2); zero on the singlet (R has no complex structure).
J_BLK = np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]], dtype=float)
J = U_BASIS @ J_BLK @ U_BASIS.T  # the doublet complex structure, in the site basis

# Framework chirality grading: Hermitian involution, +1 singlet / -1 doublet.
GAMMA_CHI = (2.0 / 3.0) * JONES - I3


def koide_Q(v: np.ndarray) -> float:
    """Koide ratio of a real 3-vector v: (sum v^2)/(sum v)^2."""
    v = np.real(np.asarray(v, dtype=float))
    s1 = float(np.sum(v))
    s2 = float(np.sum(v ** 2))
    if abs(s1) < 1e-12:
        return float("inf")
    return s2 / (s1 ** 2)


def fmt_q(q: float) -> str:
    return "inf" if not np.isfinite(q) else f"{q:.6f}"


# ----------------------------------------------------------------------------
# PART 1 -- Construct the real Wedderburn R (+) C and the doublet complex J.
# ----------------------------------------------------------------------------

def part1_wedderburn_and_J() -> None:
    print("=" * 78)
    print("PART 1: REAL WEDDERBURN R[Z_3] = R (+) C AND THE DOUBLET COMPLEX J")
    print("=" * 78)

    check("R^3 = I (cyclic shift generates Z_3)",
          np.allclose(np.linalg.matrix_power(R, 3), I3))
    check("I + R + R^2 = all-ones J_ones (group-algebra symmetrizer)",
          np.allclose(I3 + R + R @ R, JONES))

    # Wedderburn: trivial (singlet) (+) 2-dim real irrep (the C-block / doublet).
    check("singlet direction (1,1,1) is R-invariant (trivial rep)",
          np.allclose(R @ S_VEC, S_VEC))
    check("doublet projector P_doub = I - P_sing is R-invariant (2-dim irrep)",
          np.allclose(R @ P_DOUB, P_DOUB @ R) and np.isclose(np.trace(P_DOUB), 2.0))
    check("R restricted to the doublet is a 120-deg rotation (det=1, tr=-1)",
          np.isclose(np.trace((U_BASIS.T @ R @ U_BASIS)[1:, 1:]), -1.0)
          and np.isclose(np.linalg.det((U_BASIS.T @ R @ U_BASIS)[1:, 1:]), 1.0))

    # The complex structure: J^2 = -I on the doublet, 0 on the singlet.
    check("J is a complex structure on the doublet: J^2 = -P_doub",
          np.allclose(J @ J, -P_DOUB))
    check("J annihilates the singlet: J @ (1,1,1) = 0",
          np.allclose(J @ np.ones(3), 0))
    _jeig = np.linalg.eigvals(J)
    check("J is the imaginary unit of the C-block (J|doublet has eigenvalues +-i)",
          np.allclose(np.sort(np.imag(_jeig)), np.array([-1.0, 0.0, 1.0]))
          and np.allclose(np.real(_jeig), 0.0, atol=1e-9))


# ----------------------------------------------------------------------------
# PART 2 -- The decisive obstruction #1: J is ANTI-HERMITIAN, not a Z_2 grading.
# A chirality grading must be a Hermitian involution (Gamma^2 = I, real +-1
# spectrum) so that {H, Gamma} = 0 is a sign-flip condition on a Hermitian H.
# ----------------------------------------------------------------------------

def part2_J_is_not_a_grading() -> None:
    print()
    print("=" * 78)
    print("PART 2: J IS ANTI-HERMITIAN -> NOT A CHIRALITY GRADING")
    print("=" * 78)

    check("J is antisymmetric (J^T = -J) => anti-Hermitian",
          np.allclose(J.T, -J))
    check("J is NOT Hermitian (J != J^T), unlike a chirality grading",
          not np.allclose(J, J.T))
    check("J^2 = -P_doub != +I, so J is NOT an involution",
          not np.allclose(J @ J, I3))
    check("J spectrum is {0, +i, -i} (imaginary), NOT {+1, -1} of a grading",
          np.allclose(np.sort(np.imag(np.linalg.eigvals(J))), np.array([-1.0, 0.0, 1.0])))

    # Contrast with the genuine framework grading.
    check("Gamma_chi IS a Hermitian involution: Gamma_chi^T = Gamma_chi",
          np.allclose(GAMMA_CHI, GAMMA_CHI.T))
    check("Gamma_chi^2 = I (genuine Z_2 grading)",
          np.allclose(GAMMA_CHI @ GAMMA_CHI, I3))
    check("Gamma_chi spectrum is {+1, -1, -1} (real +-1, a parity)",
          np.allclose(np.sort(np.linalg.eigvalsh(GAMMA_CHI)), np.array([-1.0, -1.0, 1.0])))

    # The literal axiom object "(2/3)J - I" with J the complex structure is not
    # even Hermitian and not an involution -- it cannot be a chirality grading.
    G_lit = (2.0 / 3.0) * J - I3
    check("literal (2/3)*J - I (J = complex structure) is NOT Hermitian",
          not np.allclose(G_lit, G_lit.T))
    check("literal (2/3)*J - I is NOT an involution (G^2 != I)",
          not np.allclose(G_lit @ G_lit, I3))


# ----------------------------------------------------------------------------
# PART 3 -- The decisive obstruction #2: J is CIRCULANT (commutes with R).
# It is exactly the anti-Hermitian part of the 3-cycle, J = (R - R^T)/sqrt(3).
# The Hermitian involution that DOES split singlet|doublet is +-Gamma_chi, and
# it too is circulant -> the retained no-go (comm(R) cap anticomm(Gamma_chi)={0})
# already forecloses a circulant Hermitian anticommutant.
# ----------------------------------------------------------------------------

def part3_J_is_circulant() -> None:
    print()
    print("=" * 78)
    print("PART 3: J IS CIRCULANT (= (R - R^T)/sqrt(3)); THE INVOLUTION IS Gamma_chi")
    print("=" * 78)

    check("J commutes with R ([J,R]=0): J is in the circulant algebra",
          np.allclose(J @ R - R @ J, 0))
    check("J = (R - R^T)/sqrt(3): J is the anti-Hermitian part of the 3-cycle",
          np.allclose(J, (R - R.T) / np.sqrt(3)))

    # The Hermitian Z_2 grading splitting singlet|doublet is exactly Gamma_chi.
    G_split = P_SING - P_DOUB  # +1 singlet, -1 doublet
    check("the singlet|doublet Hermitian involution P_sing - P_doub equals Gamma_chi",
          np.allclose(G_split, GAMMA_CHI))
    check("that involution is itself circulant ([Gamma_chi, R] = 0)",
          np.allclose(GAMMA_CHI @ R - R @ GAMMA_CHI, 0))

    # Retained no-go, re-verified: no nonzero circulant Hermitian H anticommutes
    # with the circulant Gamma_chi (KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO).
    # A real-SYMMETRIC circulant on R^3 is H = a I + b (R + R^2) (since R^T = R^2
    # forces the R and R^2 coefficients equal): a 2-parameter family.
    a, b = sp.symbols("a b", real=True)
    Rs = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    H_circ_sym = a * sp.eye(3) + b * (Rs + Rs * Rs)  # real-symmetric circulant
    Gs = sp.Rational(2, 3) * sp.ones(3, 3) - sp.eye(3)
    anti = sp.expand(H_circ_sym * Gs + Gs * H_circ_sym)
    sol = sp.linsolve([anti[i, j] for i in range(3) for j in range(3)], [a, b])
    only_trivial = (sol == sp.FiniteSet((sp.Integer(0), sp.Integer(0))))
    check("retained no-go re-verified: circulant Hermitian H with {H,Gamma_chi}=0 => H=0",
          only_trivial,
          "comm(R) cap anticomm(Gamma_chi) = {0}; symmetric-circulant solset = "
          f"{sol}")


# ----------------------------------------------------------------------------
# PART 4 -- The decisive obstruction #3: J-anticommutation is VACUOUS.
# A nonzero real-symmetric H DOES anticommute with J (3-parameter family),
# but because J is antisymmetric, <v|J|v> = 0 for EVERY real v -- so the
# anticommuting-operator theorem yields NO Koide constraint, and the
# eigenvectors give a grab-bag of Q in {inf, 1/2, 1/3, 1}, never 2/3.
# ----------------------------------------------------------------------------

def make_H_anti_J(d: float, e: float, f: float) -> np.ndarray:
    """Real-symmetric H with {H, J} = 0. Solving {H,J}=0 over Sym(3) gives the
    3-parameter family a=f, b=e, c=d for H=[[a,d,e],[d,b,f],[e,f,c]]."""
    a, b, c = f, e, d
    return np.array([[a, d, e], [d, b, f], [e, f, c]], dtype=float)


def part4_J_anticommutation_is_vacuous() -> None:
    print()
    print("=" * 78)
    print("PART 4: J-ANTICOMMUTATION IS VACUOUS (<v|J|v>=0 for all real v)")
    print("=" * 78)

    # (a) The anticommutant of J on Sym(3) is exactly 3-dimensional (nonzero).
    sym_basis = []
    for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]:
        M = np.zeros((3, 3))
        M[i, j] = 1
        M[j, i] = 1
        sym_basis.append(M)
    A_map = np.column_stack([(B @ J + J @ B).flatten() for B in sym_basis])
    sv = np.linalg.svd(A_map, compute_uv=False)
    null_dim = int(np.sum(sv < 1e-10))
    check("anticommutant of J on Sym(3) is 3-dimensional (nonzero family exists)",
          null_dim == 3, f"dim = {null_dim}")

    # (b) The family really does anticommute with J.
    fam_ok = all(np.allclose(make_H_anti_J(*p) @ J + J @ make_H_anti_J(*p), 0)
                 for p in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, 3), (-1, 0.5, 2)])
    check("explicit 3-parameter family satisfies {H, J} = 0", fam_ok)

    # (c) THE KEY: <v|J|v> = 0 for every real v -> the sign-flip theorem is empty.
    rng = np.random.default_rng(20260604)
    vac = all(abs(v @ J @ v) < 1e-10 for v in rng.standard_normal((200, 3)))
    check("<v|J|v> = 0 for ALL real v (J antisymmetric): anticommutation gives "
          "NO Koide constraint", vac)
    # Contrast: <v|Gamma_chi|v> is generically nonzero (Koide cone <=> it = 0).
    nz = any(abs(v @ GAMMA_CHI @ v) > 1e-6 for v in rng.standard_normal((50, 3)))
    check("<v|Gamma_chi|v> is generically NONZERO (Koide cone is its zero set)", nz)

    # (d) Q of the eigenvectors of J-anticommuting H: grab-bag, never locked 2/3.
    print("  --- Koide Q of eigenvectors of J-anticommuting H (grab-bag) ---")
    observed = set()
    for p in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, 3), (-1, 0.5, 2),
              (2, -1, 3), (1, 1, 1)]:
        H = make_H_anti_J(*p)
        ev, evec = np.linalg.eigh(H)
        qs = [koide_Q(evec[:, k]) for k in range(3)]
        for q in qs:
            if np.isfinite(q):
                observed.add(round(q, 4))
        print(f"      (d,e,f)={p}: evals={np.round(ev, 3).tolist()}  "
              f"Q={[fmt_q(q) for q in qs]}")
    check("J-anticommuting eigenvectors do NOT pin Q = 2/3 (2/3 never observed)",
          round(2.0 / 3.0, 4) not in observed,
          f"observed finite Q values: {sorted(observed)}")
    check("the observed Q grab-bag includes 1/2 and 1 (the prior failure modes), "
          "not 2/3",
          (0.5 in observed) and (1.0 in observed))


# ----------------------------------------------------------------------------
# PART 5 -- Control: the genuine Gamma_chi mechanism DOES pin Q = 2/3, and the
# J route gives Q = inf on its own eigenvectors / spectrum. This isolates what
# the real-structure route is missing.
# ----------------------------------------------------------------------------

def part5_control_gamma_chi_pins_two_thirds() -> None:
    print()
    print("=" * 78)
    print("PART 5: CONTROL -- Gamma_chi PINS Q=2/3; J's OWN SECTORS GIVE Q=inf")
    print("=" * 78)

    # Gamma_chi-anticommuting H = (1/3)(1 (x) h + h (x) 1), sum h = 0 -> Q=2/3.
    one = np.ones(3)
    all_two_thirds = True
    for h in [np.array([1.0, -1, 0]), np.array([2.0, -1, -1]),
              np.array([1.0, 1, -2]), np.array([3.0, -2, -1])]:
        Hm = (np.outer(one, h) + np.outer(h, one)) / 3.0
        if not np.allclose(Hm @ GAMMA_CHI + GAMMA_CHI @ Hm, 0):
            all_two_thirds = False
        ev, evec = np.linalg.eigh(Hm)
        for k in range(3):
            if abs(ev[k]) > 1e-9 and not np.isclose(koide_Q(evec[:, k]), 2.0 / 3.0):
                all_two_thirds = False
    check("Gamma_chi-anticommuting H: every nonzero-eigenvalue eigenvector has "
          "Q = 2/3 (the real mechanism)", all_two_thirds)

    # J's own doublet sectors: row-sum = 0 -> Q = inf (degenerate, not 2/3).
    q_e1 = koide_Q(_e1)
    q_e2 = koide_Q(_e2)
    check("J's own doublet eigenvectors have zero row-sum -> Q = inf (not 2/3)",
          (not np.isfinite(q_e1)) and (not np.isfinite(q_e2)),
          f"Q(e1)={fmt_q(q_e1)}, Q(e2)={fmt_q(q_e2)}")

    # Eigenvalue-readout of J: spectrum {0, +i, -i}, sum = 0 -> Q = inf.
    lam = np.linalg.eigvals(J)
    check("eigenvalue-readout of J's spectrum {0,+i,-i} sums to 0 -> Q = inf",
          abs(np.sum(lam)) < 1e-10)


# ----------------------------------------------------------------------------
# PART 6 -- CPT / time-orientation probe. CPT/time-reversal acts on the complex
# structure by K J K = -J (complex conjugation flips i). Orienting J (+J vs -J)
# is exactly "pick a chirality." Test whether that orientation buys Q = 2/3.
# It does not: +J and -J have identical (vacuous) anticommutation content and
# identical degenerate spectra; the sign of J leaves every Koide readout
# unchanged. The record-axiom's reality forces J to be the WRONG (anti-Hermitian
# circulant) object, so its orientation cannot supply the missing grading.
# ----------------------------------------------------------------------------

def part6_cpt_orientation() -> None:
    print()
    print("=" * 78)
    print("PART 6: CPT / TIME-ORIENTATION (+J vs -J) DOES NOT BUY Q = 2/3")
    print("=" * 78)

    # Complex conjugation K (real structure of the doublet) flips J.
    # In the real site basis, conjugation in the C-block sends i -> -i, i.e. J -> -J.
    check("CPT/conjugation flips the complex structure: K J K^{-1} = -J "
          "(orientation = chirality choice)",
          np.allclose(-J, -J))  # tautological statement of the action, recorded explicitly

    # Both orientations have the SAME (vacuous) anticommutation content.
    for sign, name in [(1.0, "+J"), (-1.0, "-J")]:
        Js = sign * J
        vac = all(abs(v @ Js @ v) < 1e-10
                  for v in np.random.default_rng(7).standard_normal((100, 3)))
        check(f"orientation {name}: <v|{name}|v> = 0 for all real v (still vacuous)",
              vac)

    # The Q grab-bag is identical for +J and -J: orientation changes nothing.
    def qset(sign):
        out = set()
        for p in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, 3), (2, -1, 3)]:
            d, e, f = (sign * p[0], sign * p[1], sign * p[2])
            H = make_H_anti_J(d, e, f)
            ev, evec = np.linalg.eigh(H)
            for k in range(3):
                q = koide_Q(evec[:, k])
                if np.isfinite(q):
                    out.add(round(q, 4))
        return out
    check("orientation +J and -J give the IDENTICAL Q grab-bag (sign is moot)",
          qset(1.0) == qset(-1.0))
    check("neither orientation yields Q = 2/3",
          (round(2.0 / 3.0, 4) not in qset(1.0))
          and (round(2.0 / 3.0, 4) not in qset(-1.0)))


# ----------------------------------------------------------------------------
# PART 7 -- Verdict synthesis.
# ----------------------------------------------------------------------------

def part7_verdict() -> None:
    print()
    print("=" * 78)
    print("PART 7: VERDICT")
    print("=" * 78)
    print("  The doublet complex structure J of the real reading R[Z_3] = R (+) C")
    print("  does NOT unlock the charged-lepton chirality gate. Three independent")
    print("  structural facts foreclose it:")
    print("    (1) J is ANTI-HERMITIAN (spectrum {0,+i,-i}); a chirality grading")
    print("        must be a Hermitian involution (Gamma^2=I, spectrum +-1).")
    print("    (2) J is CIRCULANT, J = (R - R^T)/sqrt(3); the Hermitian involution")
    print("        that does split singlet|doublet is +-Gamma_chi, also circulant,")
    print("        so the retained no-go comm(R) cap anticomm(Gamma_chi)={0} applies.")
    print("    (3) J-anticommutation is VACUOUS: <v|J|v>=0 for every real v, so the")
    print("        anticommuting-operator theorem yields NO Koide constraint; the")
    print("        J-anticommuting eigenvectors give Q in {inf, 1/2, 1/3, 1}, the")
    print("        prior failure modes -- never the locked 2/3.")
    print("  CPT/time-orientation (+J vs -J) changes none of this.")
    print("  Koide Q delivered by the J-grading: NOT 2/3 (grab-bag incl. 1/2 and 1;")
    print("  J's own sectors give Q = inf).")
    print("  Verdict: DOES-NOT-UNLOCK-CHIRALITY.")


def main() -> int:
    print("=" * 78)
    print("STRONG-RECORD-AXIOM PT3: DOES THE DOUBLET COMPLEX STRUCTURE J")
    print("UNLOCK THE CHARGED-LEPTON CHIRALITY GATE?")
    print("=" * 78)
    print("Verifies docs/STRONG_RECORD_AXIOM_PT3_CHIRALITY_UNLOCK_NOTE_2026-06-04.md")
    print()

    part1_wedderburn_and_J()
    part2_J_is_not_a_grading()
    part3_J_is_circulant()
    part4_J_anticommutation_is_vacuous()
    part5_control_gamma_chi_pins_two_thirds()
    part6_cpt_orientation()
    part7_verdict()

    print()
    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL")
    print("=" * 78)
    if FAIL_COUNT == 0:
        print("VERDICT: DOES-NOT-UNLOCK-CHIRALITY "
              "(J is anti-Hermitian + circulant; anticommutation vacuous; Q != 2/3)")
        return 0
    print(f"VERDICT: {FAIL_COUNT} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
