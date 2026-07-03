#!/usr/bin/env python3
"""Conditional tensor-product separation of two chirality gates.

Bounds the recent keystone-collapse claim (the massive-Dirac-field "one
keystone" reduction) to its sound conditional algebraic scope. Given the finite
carrier (generation R^3) x (L+R) with gamma_5 = I_3 x sigma_3 and beta =
I_3 x sigma_1, gamma_5 is generation-blind and therefore does NOT supply the
Koide Q=2/3 generation chirality (the `koide_anticommuting_operator_derivation`
requirement). "Not blocked by the narrow no-go" != "supplied".

Grounds in the algebraic inputs (no new axiom/import, no PDG):
  - koide_anticommuting_operator_derivation_theorem  (retained):
        the one-way anti-commuting route used here: a generation mass operator
        M_gen that anticommutes with Gamma_chi = (2/3)J - I supplies the
        chiral Koide Q=2/3 readout. This runner does not use or claim a
        converse/completeness theorem.
  - koide_z3_equivariant_anticommuting_no_go          (retained_bounded):
        a C3-equivariant (circulant) M_gen with {M_gen, Gamma_chi}=0 is M_gen=0.

This restricted runner does not derive gamma_5 from Cl(3,1) and does not prove
spin-statistics use of that grading. Those are separate bridge claims.

Exact / finite / memory-safe.
"""

from pathlib import Path

import numpy as np

PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "CHIRALITY_GATE_IS_TWO_INDEPENDENT_GATES_DIRAC_VS_GENERATION_SCOPING_NOTE_2026-06-08.md"


def check(name, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"  PASS  {name}")
    else:
        FAIL += 1
        print(f"  FAIL  {name}")


I3 = np.eye(3)
# cyclic shift R on the generation triplet (the C3 generator)
R = np.array([[0, 0, 1],
              [1, 0, 0],
              [0, 1, 0]], dtype=float)
J = np.ones((3, 3))
Gamma_chi = (2.0 / 3.0) * J - I3          # generation grading
sigma_1 = np.array([[0, 1], [1, 0]], dtype=float)
sigma_3 = np.array([[1, 0], [0, -1]], dtype=float)
I2 = np.eye(2)


def comm(A, B):
    return A @ B - B @ A


def acomm(A, B):
    return A @ B + B @ A


print("== Koide/generation grading Gamma_chi ==")
# Gamma_chi spectrum {+1,-1,-1}: signature (1,2)
ev = np.sort(np.linalg.eigvalsh(Gamma_chi))
check("Gamma_chi eigenvalues are {-1,-1,+1} (signature (1,2))",
      np.allclose(ev, [-1, -1, 1]))
check("Gamma_chi is an involution (a grading): Gamma_chi^2 = I",
      np.allclose(Gamma_chi @ Gamma_chi, I3))
check("Gamma_chi is C3-equivariant (circulant): [Gamma_chi, R] = 0",
      np.allclose(comm(Gamma_chi, R), 0))

print("== Dirac/spinor chirality gamma_5 = I_3 (x) sigma_3 ==")
gamma5 = np.kron(I3, sigma_3)              # 6x6, separate-factor Dirac chirality
beta = np.kron(I3, sigma_1)               # a Dirac mass term on the spinor factor
Gchi_x_I = np.kron(Gamma_chi, I2)         # the generation grading on the product
check("gamma_5 is an involution (a grading): gamma_5^2 = I",
      np.allclose(gamma5 @ gamma5, np.eye(6)))
check("gamma_5 anticommutes with the Dirac mass beta (REAL chiral mass, L<->R)",
      np.allclose(acomm(gamma5, beta), 0))
# this is the sound part of the keystone claim: the Dirac chirality is genuine.

print("== The separation: gamma_5 is GENERATION-BLIND ==")
# gamma_5 = I_3 (x) sigma_3: its generation-block structure is delta_ij * sigma_3,
# i.e. the IDENTITY on the generation factor.
blocks = gamma5.reshape(3, 2, 3, 2)
gen_blind = all(
    np.allclose(blocks[i, :, j, :], (sigma_3 if i == j else np.zeros((2, 2))))
    for i in range(3) for j in range(3)
)
check("gamma_5 = I_3 (x) sigma_3: trivial (identity) on the generation factor",
      gen_blind)
# the meaningful generation-blind statement: gamma_5 commutes with EVERY
# generation-sector operator G (x) I_2 -- so it cannot impose any constraint there.
G_rand = np.array([[2, 1, 0], [1, 3, 1], [0, 1, 5]], dtype=float)  # arbitrary sym gen op
check("gamma_5 commutes with every generation op G (x) I_2  (R, Gamma_chi, random)",
      all(np.allclose(comm(gamma5, np.kron(G, I2)), 0)
          for G in (R, Gamma_chi, G_rand)))
check("the Dirac mass beta ALSO commutes with the generation grading",
      np.allclose(comm(beta, Gchi_x_I), 0))
# => neither gamma_5 nor beta contributes anything to {M_gen, Gamma_chi}.

print("== Koide/generation chirality is NOT supplied: it needs a C3-BREAKING M_gen ==")
# Solve the finite symmetric-generation algebra directly. The intersection of
# {M, Gamma_chi}=0 with [M, R]=0 is zero, while {M, Gamma_chi}=0 alone has
# nonzero solutions.
sym_basis = []
for i in range(3):
    for j in range(i, 3):
        E = np.zeros((3, 3))
        E[i, j] = E[j, i] = 1.0
        sym_basis.append(E)
L = np.column_stack([(acomm(E, Gamma_chi)).reshape(-1) for E in sym_basis])  # 9 x 6
L_comm = np.column_stack([(comm(E, R)).reshape(-1) for E in sym_basis])
intersection_rank = np.linalg.matrix_rank(np.vstack([L, L_comm]))
c3_equivariant_zero = intersection_rank == len(sym_basis)
check("finite algebra: no nonzero symmetric M_gen both commutes with C3 and anticommutes Gamma_chi",
      c3_equivariant_zero)
_, sv, Vt = np.linalg.svd(L)
null_dirs = Vt[np.isclose(np.r_[sv, [0] * (len(sym_basis) - len(sv))], 0)]
M_break = sum(coef * E for coef, E in zip(null_dirs[0], sym_basis))
check("a C3-BREAKING M_gen exists that anticommutes Gamma_chi (null space nonempty)",
      null_dirs.shape[0] >= 1 and not np.allclose(M_break, 0)
      and np.allclose(acomm(M_break, Gamma_chi), 0))
check("...and every such M_gen genuinely breaks C3: [M_break, R] != 0",
      c3_equivariant_zero and not np.allclose(comm(M_break, R), 0))
# the generation chirality lives on the generation R^3 and must break C3 there;
# a C3-trivial (I_3) spinor grading like gamma_5 cannot produce it.

print("== Conclusion: independent chirality requirements ==")
two_gates = (
    np.allclose(comm(gamma5, Gchi_x_I), 0)          # A is generation-blind
    and np.allclose(acomm(gamma5, beta), 0)          # A is a real Dirac chirality
    and c3_equivariant_zero                          # B needs to break C3
    and not np.allclose(comm(M_break, R), 0)         # the only working M_gen breaks C3
)
check("Dirac/spinor chirality is independent of Koide/generation chirality",
      two_gates)

print("== Scope guard: conditional tensor-product separation only ==")
note_text = NOTE.read_text(encoding="utf-8")
check("source note states conditional tensor-product separation only",
      "conditional tensor-product separation only" in note_text)
check("source note does not derive gamma_5 from Cl(3,1)",
      "does **not** derive this `γ_5` from the `Cl(3,1)`" in note_text)
check("source note does not prove spin-statistics use",
      "does **not** prove the spin-statistics use" in note_text)
check("source note does not claim retained Cl(3,1) supplies this theorem",
      "Cl(3,1)` supplies" not in note_text and "Cl(3,1) supplies" not in note_text)

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
raise SystemExit(0 if FAIL == 0 else 1)
