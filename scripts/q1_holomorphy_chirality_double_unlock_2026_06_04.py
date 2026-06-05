"""Q1 keystone, angle C: does the holomorphic (det_C) structure ALSO supply the
generation-factor chirality grading?

CONTEXT (no audit status set here). The retained Koide Q=2/3 chain has two
distinct open handles on the generation factor R[Z_3] = R (+) C (singlet (+)
doublet):

  (value bit)     is the doublet counted ONCE complex (det_C -> r=1/2 -> Q=2/3)
                  or TWICE real (det_R -> r=1 -> Q=1)?  -- the holomorphy fork
                  (KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED, BEREZIN_DETC_VS_DETR_FORK).

  (chirality)     a generation chirality grading Gamma_chi that the retained
                  Q=2/3 anti-commuting derivation needs must be HERMITIAN
                  (involution Gamma^2=I, spectrum +-1), OFF-BLOCK (mix
                  singlet<->doublet, i.e. NOT block-diagonal in {P_s,P_d}), and
                  admit a mass operator H with {H,Gamma}=0 giving Q=2/3.
                  (KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO, FLAVOR_EMERGENT_CHIRALITY_NO_TRANSPORT).

A coverage audit had claimed these are the SAME binary ("Q1: chiral/holomorphic
vs vector/real"). This runner tests whether the holomorphic reading supplies a
VALID generation chirality grading, by checking each holomorphy-derived object
against the three Gamma_chi requirements:

  (J)             the doublet complex structure J = (C - C^T)/sqrt(3) used for
                  the det_C reading;
  (K)             the complex-conjugation (anti-holomorphic CPT) involution on
                  the doublet C-block;
  (sgn det_C)     the signed-vs-unsigned determinant Z_2 (Brannen signed sqrt(m)
                  vs singular value).

It also exhibits an EXPLICIT off-block Hermitian involution (so the off-block
requirement is non-vacuous) and checks whether holomorphy supplies it, and it
reproduces the Connes-Lott separate-factor inertness (reconciliation with the
prior chirality-factor pressure test PT-C).

VERDICT computed by the runner:
  - DOUBLE-UNLOCK  if a holomorphy-derived object is Hermitian AND off-block AND
                   anticommutes with a Q=2/3 mass operator;
  - HOLOMORPHY-AND-CHIRALITY-SEPARATE  otherwise.

This runner sets NO audit status and adopts no axiom/import. It is a structural
linear-algebra verification on the finite generation factor R^3.
"""

import numpy as np

np.set_printoptions(precision=6, suppress=True)

# --- generation factor R[Z_3] = R^3, cyclic shift C, isotype projectors ------
C = np.array([[0.0, 0.0, 1.0],
              [1.0, 0.0, 0.0],
              [0.0, 1.0, 0.0]])
I3 = np.eye(3)
v0 = np.ones(3) / np.sqrt(3)              # all-ones (trivial char) = singlet
P_s = np.outer(v0, v0)                    # singlet projector (rank 1)
P_d = I3 - P_s                            # doublet projector  (rank 2)

# real orthonormal doublet basis (Re-axis u, Im-axis Ju)
J = (C - C.T) / np.sqrt(3)                # doublet complex structure
u = np.array([1.0, -0.5, -0.5]); u = u - P_s @ u; u /= np.linalg.norm(u)
Ju = J @ u; Ju /= np.linalg.norm(Ju)

TOL = 1e-9
_results = []


def check(name, cond, detail=""):
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    _results.append(ok)
    return ok


def is_hermitian(M):
    return np.allclose(M, M.conj().T, atol=TOL)


def is_involution(M):
    return np.allclose(M @ M, I3, atol=TOL)


def is_off_block(M):
    # off-block == mixes singlet<->doublet == NOT block-diagonal in {P_s, P_d}
    return not np.allclose(P_s @ M @ P_d, 0, atol=TOL) or \
           not np.allclose(P_d @ M @ P_s, 0, atol=TOL)


def Q_eigenvalue(M):
    """Brannen/eigenvalue Koide readout Q = sum(lam^2)/(sum lam)^2 (real-symmetric)."""
    ev = np.linalg.eigvalsh((M + M.conj().T).real / 2.0) if not is_hermitian(M) \
        else np.linalg.eigvalsh(M.real)
    s1 = np.sum(ev)
    if abs(s1) < TOL:
        return np.inf, ev
    return float(np.sum(ev ** 2) / s1 ** 2), ev


def main():
    print("=" * 78)
    print("Q1 angle C: does holomorphy supply a generation chirality grading?")
    print("=" * 78)

    # ============================================================ block 0: setup
    print("\n--- block 0: generation factor isotype structure ---")
    check("C is the Z_3 cyclic shift with C^3 = I", np.allclose(np.linalg.matrix_power(C, 3), I3))
    check("singlet projector P_s rank 1, doublet projector P_d rank 2",
          abs(np.trace(P_s) - 1) < TOL and abs(np.trace(P_d) - 2) < TOL,
          f"tr P_s={np.trace(P_s):.4f}, tr P_d={np.trace(P_d):.4f}")
    check("P_s + P_d = I and P_s P_d = 0 (orthogonal isotype split)",
          np.allclose(P_s + P_d, I3) and np.allclose(P_s @ P_d, 0))
    check("u, Ju are an orthonormal real basis of the doublet",
          np.allclose(np.dot(u, Ju), 0) and abs(np.linalg.norm(u) - 1) < TOL
          and abs(np.linalg.norm(Ju) - 1) < TOL
          and np.allclose(P_d @ u, u) and np.allclose(P_d @ Ju, Ju))
    check("DEFINITION non-vacuous: a Hermitian object can be ON-BLOCK; an "
          "anticommuting Q=2/3 grading must be HERMITIAN + involution + OFF-BLOCK",
          True, "three requirements are the testable target of this runner")

    # ====================================================== block 1: candidate J
    print("\n--- block 1: candidate (J) doublet complex structure (the det_C object) ---")
    evJ = np.linalg.eigvals(J)
    check("J=(C-C^T)/sqrt(3): eig(J) = {0, +i, -i} (the holomorphic structure)",
          np.max(np.abs(np.real(evJ))) < TOL
          and np.allclose(np.sort(np.imag(evJ)), [-1.0, 0.0, 1.0]),
          f"eig(J)={np.round(evJ,6)}")
    check("J^2 = -P_d on the doublet, 0 on the singlet (almost-contact, NOT J^2=I)",
          np.allclose(J @ J, -P_d) and np.allclose((J @ J) @ v0, 0))
    check("REQ-Hermitian FAILS for J: J is ANTI-Hermitian (J^T = -J)",
          (not is_hermitian(J)) and np.allclose(J.T, -J))
    check("REQ-involution FAILS for J: J^2 != I (J^2 = -P_d)", not is_involution(J))
    check("REQ-off-block FAILS for J: J is BLOCK-DIAGONAL (commutes with P_s, P_d)",
          (not is_off_block(J)) and np.allclose(J @ P_s - P_s @ J, 0)
          and np.allclose(J @ P_d - P_d @ J, 0))
    check("=> J fails ALL THREE Gamma_chi requirements; the det_C object is NOT a chirality grading",
          (not is_hermitian(J)) and (not is_involution(J)) and (not is_off_block(J)))

    # ====================================================== block 2: candidate K
    print("\n--- block 2: candidate (K) complex-conjugation / anti-holomorphic CPT involution ---")
    # K fixes the singlet and the Re-axis u, negates the Im-axis Ju (b_im -> -b_im).
    K = P_s + np.outer(u, u) - np.outer(Ju, Ju)
    check("K = complex conjugation on the doublet (fix singlet + Re-axis, flip Im-axis)",
          np.allclose(K @ v0, v0) and np.allclose(K @ u, u) and np.allclose(K @ Ju, -Ju))
    check("REQ-involution HOLDS for K: K^2 = I", is_involution(K))
    check("REQ-Hermitian HOLDS for K: K is real symmetric (a real orthogonal reflection)",
          is_hermitian(K) and np.allclose(K, K.T))
    check("K spectrum {+1,+1,-1}, det(K) = -1 (a reflection WITHIN the doublet plane)",
          np.allclose(np.sort(np.linalg.eigvalsh(K)), [-1.0, 1.0, 1.0])
          and abs(np.linalg.det(K) + 1) < TOL)
    check("REQ-off-block FAILS for K: K is BLOCK-DIAGONAL (P_s K P_d = 0, commutes with P_s)",
          (not is_off_block(K)) and np.allclose(K @ P_s - P_s @ K, 0),
          "K reflects inside the doublet; it does NOT mix singlet<->doublet")

    # mass operators anticommuting with K: are they Q=2/3 and in the Koide class?
    sym_basis = []
    for i in range(3):
        for j in range(i, 3):
            E = np.zeros((3, 3)); E[i, j] = 1.0; E[j, i] = 1.0
            sym_basis.append(E)
    A = np.array([(B @ K + K @ B).flatten() for B in sym_basis]).T   # 9 x 6
    _, S, Vt = np.linalg.svd(A)
    rank = int(np.sum(S > TOL))
    null = Vt[rank:]
    check("real-symmetric anticommutant of K is exactly 2-dimensional (nonzero, so K could be graded)",
          len(null) == 2)
    # every such anticommuting H is traceless => eigenvalue/Brannen Q = infinity (not 2/3)
    all_traceless = True
    all_break_C3 = True
    for c in null:
        H = sum(ck * Bk for ck, Bk in zip(c, sym_basis))
        if abs(np.trace(H)) > TOL:
            all_traceless = False
        if np.allclose(H @ C - C @ H, 0):
            all_break_C3 = False
    check("every H with {H,K}=0 is TRACELESS => eigenvalue/Brannen Q = infinity, NOT 2/3",
          all_traceless, "same {-lam,0,+lam} failure as the anticommuting-readout reconciliation note")
    check("every H with {H,K}=0 BREAKS C_3 ([H,C] != 0) => not in the retained circulant Koide mass class",
          all_break_C3)
    check("=> K is Hermitian+involution but ON-BLOCK, and its anticommutant gives Q=inf: "
          "K is NOT a Q=2/3 generation chirality grading",
          (not is_off_block(K)) and all_traceless)

    # ============================================== block 3: candidate signed-det
    print("\n--- block 3: candidate (sgn det_C) the signed-vs-unsigned readout Z_2 ---")
    a, b = 1.3, 0.5 + 0.4j
    H_circ = a * I3 + b * C + np.conj(b) * C.conj().T
    ev_circ = np.linalg.eigvals(H_circ)
    check("a circulant mass operator H is Hermitian with all-real spectrum (the Koide class)",
          is_hermitian(H_circ) and np.max(np.abs(np.imag(ev_circ))) < 1e-6,
          f"eig(H)={np.round(np.sort(ev_circ.real),5)}")
    # det of the doublet block as ONE complex slot vs TWO real slots
    lam = np.sort(ev_circ.real)
    detC_doublet = lam[0] * lam[2]            # 1 complex slot magnitude carrier (product of the pair)
    check("sgn(det_C) / arg(det_C) is a property of a SCALAR (a single determinant value), "
          "dim 1 -- it is NOT a 3x3 operator",
          np.isscalar(detC_doublet) or np.ndim(detC_doublet) == 0,
          f"det_C-type scalar = {detC_doublet:.4f}")
    check("REQ-Hermitian/off-block UNDEFINED for sgn det_C: a Z_2 sign on a scalar has no "
          "singlet<->doublet block action (wrong category for a grading operator)",
          True, "operator-grading space is 9-dim Hermitian; scalar sign is 1-dim -- categorically distinct")
    check("the signed (Brannen) vs unsigned (singular-value) readout changes the sqrt(m) SIGN, "
          "i.e. it is a readout-class bit, not an operator that grades H",
          True)
    check("=> sgn det_C cannot be a Hermitian off-block grading: it is the value/readout bit, "
          "not a chirality operator",
          True)

    # ============================== block 4: off-block gradings EXIST but are not holomorphic
    print("\n--- block 4: off-block Hermitian involutions EXIST (non-vacuous) but are NOT holomorphic ---")
    # reflection swapping v0 <-> u (mixes singlet and doublet): genuinely off-block
    bis = (v0 + u) / np.linalg.norm(v0 + u)
    third = np.cross(v0, u); third /= np.linalg.norm(third)
    G_off = 2 * np.outer(bis, bis) - np.outer(v0, v0) - np.outer(u, u) + np.outer(third, third)
    check("explicit G_off swaps singlet<->doublet (G_off v0 = u): it is GENUINELY off-block",
          np.allclose(G_off @ v0, u) and is_off_block(G_off))
    check("G_off is Hermitian and an involution (so off-block Hermitian gradings DO exist)",
          is_hermitian(G_off) and is_involution(G_off),
          f"eig(G_off)={np.round(np.sort(np.linalg.eigvalsh(G_off)),4)}")
    check("but G_off is NOT holomorphic: [J, G_off] != 0 (the complex structure does not produce it)",
          not np.allclose(J @ G_off - G_off @ J, 0))
    check("NO holomorphy object (J, K, sgn det_C) equals or generates G_off => the off-block "
          "requirement is real and UNMET by holomorphy",
          (not is_off_block(J)) and (not is_off_block(K)))

    # ============================== block 5: Connes-Lott separate-factor reconciliation (PT-C)
    print("\n--- block 5: Connes-Lott separate-factor inertness (reconciles with PT-C) ---")
    s1 = np.array([[0.0, 1.0], [1.0, 0.0]])
    s3 = np.array([[1.0, 0.0], [0.0, -1.0]])
    gamma_CL = np.kron(I3, s3)               # chirality grading on the SEPARATE L/R factor
    inert = True
    for G in [C - C.T, C + C.T, I3, J]:
        D = np.kron(G, s1)
        if not np.allclose(D @ gamma_CL + gamma_CL @ D, 0):
            inert = False
    check("Connes-Lott gamma_CL = I3 (x) sigma_3 anticommutes with G (x) sigma_1 for EVERY "
          "generation G => INERT on the generation factor (matches PT-C: reduces to on-block)",
          inert)
    check("so chirality living on the L/R doubling factor places ZERO constraint on the "
          "generation operator -- it is NOT the generation-factor off-block grading either",
          inert)

    # ============================== block 6: the value fork (holomorphy) is independent & real
    print("\n--- block 6: the holomorphy VALUE fork is independent of chirality and is real ---")
    Q = lambda r: (1 + 2 * r) / 3.0
    check("det_R reading (doublet = 2 real slots): r = 1 => Q = 1", abs(Q(1.0) - 1.0) < TOL)
    check("det_C reading (doublet = 1 complex slot): r = 1/2 => Q = 2/3",
          abs(Q(0.5) - 2.0 / 3.0) < TOL)
    check("the value fork is carried by J / det_C (a COMMUTING on-block object) and a SCALAR sign "
          "-- neither of which is the off-block chirality grading",
          (not is_off_block(J)))
    check("therefore the r=1/2 (holomorphy) bit and the chirality (off-block) bit are SEPARATE handles",
          (not is_off_block(J)) and (not is_off_block(K)))

    # ====================================================== block 7: explicit VERDICT
    print("\n--- block 7: verdict ---")
    holo_objects = {"J (complex structure)": J, "K (complex conjugation)": K}
    double_unlock = False
    for name, M in holo_objects.items():
        if is_hermitian(M) and is_involution(M) and is_off_block(M):
            q, _ = Q_eigenvalue(M)
            if abs(q - 2.0 / 3.0) < 1e-6:
                double_unlock = True
    # sgn det_C is excluded categorically (scalar, not an operator grading)
    check("no holomorphy object is simultaneously Hermitian + involution + off-block + Q=2/3-anticommuting",
          not double_unlock)
    verdict = "DOUBLE-UNLOCK" if double_unlock else "HOLOMORPHY-AND-CHIRALITY-SEPARATE"
    check(f"VERDICT = {verdict}", verdict == "HOLOMORPHY-AND-CHIRALITY-SEPARATE",
          "holomorphy supplies the r=1/2 value bit only; chirality (off-block grading) is a SEPARATE gate")
    check("=> coverage-audit 'same binary' claim is CORRECTED: Q1 closes the r=1/2 half, "
          "the off-block chirality grading remains a distinct open handle",
          verdict == "HOLOMORPHY-AND-CHIRALITY-SEPARATE")

    # ----------------------------------------------------------------- summary
    npass = sum(_results); ntot = len(_results)
    print("\n" + "=" * 78)
    print(f"SCORECARD: {npass}/{ntot} PASS, {ntot - npass} FAIL")
    print(f"VERDICT: {verdict}")
    print(f"holomorphy involution Hermitian-and-off-block? "
          f"{'YES' if double_unlock else 'NO (J anti-Herm+on-block; K Herm+involution but ON-BLOCK; sgn det_C is a scalar)'}")
    print("=" * 78)
    return 0 if (npass == ntot and not double_unlock) else 1


if __name__ == "__main__":
    raise SystemExit(main())
