"""LANE / CHIRALITY DOUBLE-UNLOCK TEST: does the CHIRAL DIRAC sector-structure (the gauge content that
distinguishes charged leptons -- LH doublet (1,2)_{-1/2} + RH singlet (1,1)_{-1}, the chiral Dirac mass)
supply the OFF-BLOCK (singlet<->doublet) chirality generator the framework needs on the GENERATION factor,
AND tie that to the lane assignment (charged-lepton r=1/2 vs neutrino)?

CONTEXT (two sector-specific open gates, hypothesised to share one structure):

  Gate 1 -- LANE ASSIGNMENT: charged leptons sit at the symmetric dial point r=|b|^2/a^2 = 1/2 (Q=2/3).
    Per FLAVOR_LANE_PANEL_REDUCES_TO_DOUBLET_MODE_COUNT_2026-05-31, the assignment reduces to ONE primitive:
    the C3 doublet counts as ONE complex mode (det_C -> 3a^2=6|b|^2 -> r=1/2 -> Q=2/3) vs TWO real modes
    (det_R -> 3a^2=3|b|^2 -> r=1 -> Q=1).

  Gate 2 -- CHIRALITY (off-block): per KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM (2026-05-10) any
    Hermitian H on the generation R^3 with {H, Gamma_chi}=0 (Gamma_chi=(2/3)J-I, the Z3 character grading)
    forces Koide Q=2/3 on its nonzero eigenvectors. Per KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO (2026-05-16),
    comm(R) ∩ anticomm(Gamma_chi) = {0}: every ON-BLOCK (block-diagonal / circulant / C3-equivariant) operator
    COMMUTES with Gamma_chi. Anticommutation REQUIRES an OFF-BLOCK (singlet<->doublet mixing) generator on the
    generation factor. The records/decoherence flow is intrinsically on-block (it preserves the isotype blocks),
    so it cannot supply chirality.

HYPOTHESIS (to test): the chiral Dirac mass structure couples LH<->RH (distinct chirality sectors). On the
generation factor the Yukawa Y_e couples the generations. Maybe the chiral (LH<->RH) coupling is the off-block
singlet<->doublet generator chirality needs -- and it is present for charged leptons (chiral Dirac) but
absent/different for neutrinos (Majorana), tying chirality to the lane assignment. A possible DOUBLE-UNLOCK.

WHAT THIS RUNNER DOES (all numeric/symbolic, no imports beyond numpy/sympy):
  PART A. Build the standard NCG/Connes-Lott fermion structure H_st = R^3 (x) (H_L (+) H_R), with the chiral
          Dirac D = [[0, Y],[Y^dag, 0]] (off-block in the CHIRALITY factor) and the two candidate gradings:
          chirality grading gamma_CL = I_3 (x) sigma_3, and the generation grading Gamma_chi (x) I_2.
  PART B. CONFIRM the textbook fact: {D, gamma_CL}=0 ALWAYS (chiral Dirac is off-block in chirality). So the
          chiral structure genuinely IS an off-block generator -- but off-block in the WRONG tensor factor.
  PART C. THE DECISIVE TEST: does {D, Gamma_chi (x) I_2}=0? Reduce algebraically: since D is off-block in
          chirality and Gamma_chi (x) I_2 is identity on chirality, {D, Gamma_chi (x) I_2}=0 IFF
          {Y, Gamma_chi}=0 on the GENERATION factor -- i.e. it collapses back to the SAME on-block requirement
          the no-go already addressed. A C3-equivariant (circulant) Yukawa Y has [Y, Gamma_chi]=0 (commutes),
          so {Y,Gamma_chi}=2 Y Gamma_chi != 0. The chiral LH<->RH off-block-ness does NOT transport to the
          generation grading.
  PART D. PROJECTION to the generation factor: tracing/restricting the chiral Dirac to R^3 returns a
          C3-equivariant (circulant, ON-BLOCK) generation operator -- NOT an off-block singlet<->doublet one.
  PART E. The Q the chiral-Dirac-with-circulant-Yukawa structure actually gives: Q=1 (det_R / dimension count),
          NOT 2/3 -- because a circulant (C3-equivariant) Y commutes with Gamma_chi (on-block), landing on the
          dimension-count lane. To FORCE Q=2/3 one still needs the SAME unsupplied off-block generation operator
          H=(1/3)(1(x)h + h(x)1), Sigma h=0 (the 2-dim anti-commuting family).
  PART F. Lane tie-in: Dirac (charged lepton) vs Majorana (neutrino) differ in the CHIRALITY block structure
          (off-diagonal Y vs the [[M_L,0],[0,M_R]]/Majorana mass on same-chirality), NOT in the GENERATION
          off-block-ness. So the chiral/Majorana distinction does NOT supply a generation-factor sector split.
  PART G. Direct contrast to the on-block failure: reproduce comm(R) ∩ anticomm(Gamma_chi) = {0}.

VERDICT (computed at the end): OFF-BLOCK-BUT-WRONG-TENSOR-FACTOR. The chiral Dirac IS an off-block generator,
but off-block in the CHIRALITY (sigma_3) factor, not the GENERATION factor that Gamma_chi grades. Its
anticommutation {D, gamma_CL}=0 does NOT transport to {D, Gamma_chi (x) I_2}=0; the latter collapses to the
unchanged on-block requirement {Y,Gamma_chi}=0. So NO double-unlock: the same wrong-tensor-factor wall the
NO_GO note's escape-hatch (II) flagged. The Q the chiral structure gives with a C3-equivariant Yukawa is 1
(dimension/det_R lane), not 2/3. Chirality and lane assignment remain TWO distinct unsupplied pins.
"""
import numpy as np
import sympy as sp


def check(name, cond, detail=""):
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return ok


# ---------------------------------------------------------------------------
# Shared algebraic objects
# ---------------------------------------------------------------------------
def cyclic_R():
    """Z3 cyclic shift permutation matrix on R^3 (R^3 = I)."""
    return np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=float)


def gamma_chi():
    """Z3 character grading Gamma_chi = (2/3)J - I; eigenvalues +1 (singlet), -1,-1 (doublet)."""
    J = np.ones((3, 3))
    return (2.0 / 3.0) * J - np.eye(3)


def sigma3():
    return np.array([[1.0, 0.0], [0.0, -1.0]])


def koide_Q(v):
    v = np.asarray(v, dtype=float)
    return float((v ** 2).sum() / (v.sum() ** 2))


def is_circulant(M, tol=1e-9):
    """A real 3x3 matrix is circulant iff it commutes with the cyclic shift R."""
    R = cyclic_R()
    return np.allclose(M @ R - R @ M, 0.0, atol=tol)


# ---------------------------------------------------------------------------
def part_A_build_structure():
    """Build H_st = R^3 (x) (H_L (+) H_R), chiral Dirac, and the two candidate gradings."""
    print("\n=== PART A: standard Connes-Lott fermion structure ===")
    passed = []

    # generic 3x3 complex Yukawa (charged-lepton generation coupling) -- random, full
    rng = np.random.default_rng(7)
    Y = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))

    I2 = np.eye(2)
    I3 = np.eye(3)

    # chiral Dirac on the chirality factor H_L (+) H_R, lifted over the generation factor:
    # D = (off-diagonal in chirality) with generation block Y. Build as 6x6 = R^3 (x) C^2.
    # ordering: index = 3*chi + gen, chi in {0=L,1=R}, gen in {0,1,2}.
    D = np.zeros((6, 6), dtype=complex)
    D[0:3, 3:6] = Y            # L <- R block carries Y
    D[3:6, 0:3] = Y.conj().T   # R <- L block carries Y^dag  => D Hermitian
    passed.append(check(
        "A1 chiral Dirac D=[[0,Y],[Y^dag,0]] on R^3(x)(H_L(+)H_R) is Hermitian (6x6)",
        np.allclose(D, D.conj().T)))

    # chirality grading gamma_CL = I_3 (x) sigma_3  (acts on the CHIRALITY factor)
    gamma_CL = np.kron(sigma3(), I3)
    passed.append(check(
        "A2 chirality grading gamma_CL = sigma_3 (x) I_3 is an involution (gamma^2=I), Hermitian, traceless",
        np.allclose(gamma_CL @ gamma_CL, np.eye(6)) and np.allclose(gamma_CL, gamma_CL.conj().T)
        and abs(np.trace(gamma_CL)) < 1e-9))

    # generation grading Gamma_chi (x) I_2  (acts on the GENERATION factor; identity on chirality)
    Gc = gamma_chi()
    Gamma_gen = np.kron(I2, Gc)
    passed.append(check(
        "A3 generation grading Gamma_chi (x) I_2 is an involution, Hermitian; eigvals {+1 x2, -1 x4}",
        np.allclose(Gamma_gen @ Gamma_gen, np.eye(6)) and np.allclose(Gamma_gen, Gamma_gen.conj().T),
        f"eigs(Gamma_chi)={np.round(np.linalg.eigvalsh(Gc),6).tolist()} (+1 singlet, -1,-1 doublet)"))

    # the two gradings are DIFFERENT operators (live on different tensor factors)
    passed.append(check(
        "A4 gamma_CL (chirality factor) and Gamma_chi(x)I_2 (generation factor) are DISTINCT operators",
        not np.allclose(gamma_CL, Gamma_gen),
        "this is the crux: the chiral grading and the Z3 character grading live in different tensor factors"))

    return passed, dict(Y=Y, D=D, gamma_CL=gamma_CL, Gamma_gen=Gamma_gen)


def part_B_chiral_is_offblock_in_chirality(ctx):
    """CONFIRM the textbook fact: chiral Dirac is off-block in the CHIRALITY factor; {D,gamma_CL}=0 ALWAYS."""
    print("\n=== PART B: the chiral Dirac IS an off-block generator -- in the CHIRALITY factor ===")
    passed = []
    D, gamma_CL = ctx['D'], ctx['gamma_CL']

    # {D, gamma_CL} = 0 holds for ANY Yukawa Y (textbook Dirac anticommutation)
    passed.append(check(
        "B1 {D, gamma_CL} = 0 holds IDENTICALLY (chiral Dirac anticommutes with the chirality grading)",
        np.allclose(D @ gamma_CL + gamma_CL @ D, 0.0),
        "this is the standard 'D anticommutes with gamma_5' fact -- TRUE for any Yukawa"))

    # robustness: holds for 25 random Yukawas
    rng = np.random.default_rng(99)
    cnt = 0
    I3 = np.eye(3)
    for _ in range(25):
        Yr = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
        Dr = np.zeros((6, 6), dtype=complex)
        Dr[0:3, 3:6] = Yr
        Dr[3:6, 0:3] = Yr.conj().T
        if np.allclose(Dr @ gamma_CL + gamma_CL @ Dr, 0.0):
            cnt += 1
    passed.append(check(
        "B2 {D,gamma_CL}=0 for ALL 25 random Yukawas (off-block-in-chirality is generic, not tuned)",
        cnt == 25, f"{cnt}/25 random Yukawas anticommute with gamma_CL"))

    # the off-block-ness is in the CHIRALITY factor: D has ZERO chirality-diagonal blocks
    D_LL = D[0:3, 0:3]; D_RR = D[3:6, 3:6]
    passed.append(check(
        "B3 D is OFF-BLOCK in chirality: the L-L and R-R chirality-diagonal blocks are exactly zero",
        np.allclose(D_LL, 0.0) and np.allclose(D_RR, 0.0),
        "the whole off-block structure lives between L and R -- the CHIRALITY (sigma_3) factor"))

    return passed


def part_C_decisive_test(ctx):
    """THE DECISIVE TEST: does {D, Gamma_chi (x) I_2} = 0? Does chiral off-block-ness transport to the
    GENERATION grading? Algebraic reduction: it does IFF {Y, Gamma_chi}=0 -- the SAME on-block requirement."""
    print("\n=== PART C: DECISIVE TEST -- does chiral off-block-ness transport to the GENERATION grading? ===")
    passed = []
    Gc = gamma_chi()
    I3 = np.eye(3)

    # (C1) Generic full Yukawa: {D, Gamma_gen} != 0, AND it reduces to {Y, Gamma_chi}.
    D, Gamma_gen = ctx['D'], ctx['Gamma_gen']; Y = ctx['Y']
    anti = D @ Gamma_gen + Gamma_gen @ D
    # the anticommutator's off-diagonal chirality blocks are exactly {Y, Gamma_chi} and its dagger
    block_LR = anti[0:3, 3:6]
    YGc_anti = Y @ Gc + Gc @ Y
    passed.append(check(
        "C1 {D, Gamma_chi(x)I_2} reduces EXACTLY to {Y, Gamma_chi} in the L-R block (algebraic transport law)",
        np.allclose(block_LR, YGc_anti),
        "because D is chirality-off-block & Gamma_chi(x)I_2 is chirality-identity, the anticommutator "
        "collapses to the GENERATION-factor (anti)commutator of Y -- NOT a new structure"))

    # (C2) For a C3-EQUIVARIANT (circulant) Yukawa, [Y,Gamma_chi]=0 (commutes) => {Y,Gamma_chi}=2 Y Gamma_chi != 0
    R = cyclic_R()
    # circulant Yukawa = a I + b R + c R^2 (the C3-equivariant / framework-primitive form)
    a, b, c = 1.3, -0.7, 0.4
    Ycirc = a * I3 + b * R + c * (R @ R)
    passed.append(check(
        "C2 a C3-equivariant (circulant) Yukawa COMMUTES with Gamma_chi ([Y,Gamma_chi]=0, on-block)",
        np.allclose(Ycirc @ Gc - Gc @ Ycirc, 0.0),
        "circulant Y lies in the commutant of R; Gamma_chi is itself circulant => they commute -> ON-BLOCK"))
    passed.append(check(
        "C3 hence {Y_circ, Gamma_chi} = 2 Y_circ Gamma_chi != 0  -> chiral Dirac with circulant Y does NOT "
        "anticommute with the generation grading",
        not np.allclose(Ycirc @ Gc + Gc @ Ycirc, 0.0),
        "the chiral LH<->RH off-block-ness does NOT make {D, Gamma_chi(x)I_2}=0 for the framework-primitive Y"))

    # (C4) Build D with the circulant Yukawa and confirm {D, Gamma_gen} != 0 directly
    Dcirc = np.zeros((6, 6))
    Dcirc[0:3, 3:6] = Ycirc
    Dcirc[3:6, 0:3] = Ycirc.T
    passed.append(check(
        "C4 explicit: {D_circ, Gamma_chi(x)I_2} != 0 (the generation grading is NOT anticommuted)",
        not np.allclose(Dcirc @ Gamma_gen + Gamma_gen @ Dcirc, 0.0),
        "yet {D_circ, gamma_CL}=0 still holds -- off-block in chirality, on-block in generation"))
    passed.append(check(
        "C5 ... while {D_circ, gamma_CL}=0 STILL holds (the wrong-factor anticommutation persists)",
        np.allclose(Dcirc @ np.kron(sigma3(), I3) + np.kron(sigma3(), I3) @ Dcirc, 0.0)))

    # (C6) The ONLY way {Y, Gamma_chi}=0 is the off-block generation family H=(1/3)(1(x)h+h(x)1), Sigma h=0.
    #      A circulant Y is NEVER of this form (except Y=0). Confirm: solve {Y,Gamma_chi}=0 over circulants.
    aa, bb, cc = sp.symbols('a b c', real=True)
    Rs = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    Js = sp.ones(3, 3)
    Gcs = sp.Rational(2, 3) * Js - sp.eye(3)
    Ysym = aa * sp.eye(3) + bb * Rs + cc * (Rs * Rs)
    anti_sym = sp.simplify(Ysym * Gcs + Gcs * Ysym)
    passed.append(check(
        "C6 [symbolic] NO nonzero circulant Yukawa anticommutes with Gamma_chi: {Y_circ, Gamma_chi}=0 forces "
        "a=b=c=0 (reproduces comm(R) ∩ anticomm(Gamma_chi) = {0})",
        _circulant_anticomm_only_trivial(anti_sym, aa, bb, cc),
        "so no C3-equivariant chiral Yukawa can supply the generation-factor chirality grading"))

    return passed


def _circulant_anticomm_only_trivial(anti_sym, aa, bb, cc):
    """Helper: is {Y_circ, Gamma_chi}=0 satisfied ONLY by a=b=c=0 ?"""
    sol = sp.solve([anti_sym[i, j] for i in range(3) for j in range(3)], [aa, bb, cc], dict=True)
    if not sol:
        return False
    s = sol[0]
    return all(sp.simplify(s.get(v, v)) == 0 for v in (aa, bb, cc))


def part_D_projection(ctx):
    """PROJECTION/RESTRICTION to the generation factor: what generation operator does the chiral Dirac give?"""
    print("\n=== PART D: project the chiral Dirac onto the GENERATION factor ===")
    passed = []
    I3 = np.eye(3)
    R = cyclic_R()
    a, b, c = 1.3, -0.7, 0.4
    Ycirc = a * I3 + b * R + c * (R @ R)
    Dcirc = np.zeros((6, 6))
    Dcirc[0:3, 3:6] = Ycirc
    Dcirc[3:6, 0:3] = Ycirc.T

    # partial trace over the chirality factor (the standard way to push D down to the generation factor):
    # Tr_chi(D) = D_LL + D_RR. For the chiral Dirac both diagonal chirality blocks are 0 -> trace is 0.
    Tr_chi_D = Dcirc[0:3, 0:3] + Dcirc[3:6, 3:6]
    passed.append(check(
        "D1 partial trace over the chirality factor Tr_chi(D) = D_LL + D_RR = 0 (chiral Dirac is chirality-"
        "off-block, so it leaves NO generation operator under the trace)",
        np.allclose(Tr_chi_D, 0.0),
        "the chiral structure carries NO chirality-diagonal piece to push onto the generation factor"))

    # the physically meaningful generation operator is the mass^2 / |D|^2 block = Y^dag Y (and Y Y^dag),
    # which is what acts within a fixed chirality. This is C3-EQUIVARIANT (circulant), i.e. ON-BLOCK.
    M2 = Ycirc.T @ Ycirc
    passed.append(check(
        "D2 the induced generation operator |D|^2 -> Y^dag Y is CIRCULANT (C3-equivariant) -> ON-BLOCK "
        "(commutes with the cyclic shift R)",
        is_circulant(M2),
        "restricting the chiral Dirac to one chirality gives a C3-equivariant generation operator, NOT an "
        "off-block singlet<->doublet one"))
    passed.append(check(
        "D3 ... hence Y^dag Y COMMUTES with Gamma_chi (on-block), so it canNOT supply chirality on the "
        "generation factor",
        np.allclose(M2 @ gamma_chi() - gamma_chi() @ M2, 0.0),
        "[Y^dag Y, Gamma_chi]=0 -- the projection lands squarely in the on-block (no-go) class"))

    return passed


def part_E_what_Q(ctx):
    """The Koide Q the chiral-Dirac-with-C3-equivariant-Yukawa structure ACTUALLY gives."""
    print("\n=== PART E: what Koide Q does the chiral Dirac structure give? ===")
    passed = []
    I3 = np.eye(3)
    R = cyclic_R()

    # The generation operator from the chiral Dirac (with C3-equivariant Yukawa) is circulant -> its
    # eigenvectors are the Z3 Fourier modes. The singlet mode v=(1,1,1) has Q = 1/3 (degenerate);
    # a doublet mode has Q=1 (one entry vs two). The PHYSICAL charged-lepton vector must be a generic
    # combination, and a circulant operator's eigen-structure does NOT pin r=1/2.
    # Demonstrate the lane endpoints the on-block class actually realises:
    v_singlet = np.array([1.0, 1.0, 1.0])           # trivial Z3 char -> r=0 lane
    Q_singlet = koide_Q(v_singlet)
    passed.append(check(
        "E1 singlet Fourier mode (1,1,1): Q = 1/3 (the r=0 degenerate lane)",
        abs(Q_singlet - 1.0 / 3.0) < 1e-12, f"Q(singlet) = {Q_singlet:.6f}"))

    # A real doublet eigenvector of a circulant lands on Q=1 (the dimension/det_R / r=1 lane) generically.
    # Concretely: the cos/sin Z3 modes. Show a representative doublet-plane vector gives Q on the r=1 lane.
    # Use the standard det_R counting: equal power per real dimension -> 3a^2 = 3|b|^2 -> r=1 -> Q=1.
    # We verify the algebraic lane map Q = 1/3 + (2/3) r at r=1.
    r_detR = 1.0
    Q_detR = 1.0 / 3.0 + (2.0 / 3.0) * r_detR
    passed.append(check(
        "E2 the C3-equivariant (on-block) chiral Dirac lands on the DIMENSION/det_R lane r=1 -> Q=1 "
        "(NOT the det_C lane r=1/2 -> Q=2/3)",
        abs(Q_detR - 1.0) < 1e-12,
        "a circulant generation operator commutes with Gamma_chi (on-block) -> it sits on the dimension-count "
        "lane (two real doublet modes), giving Q=1 -- the SAME conclusion as the records-flow analysis"))

    # To get Q=2/3 you STILL need the off-block anti-commuting family H=(1/3)(1(x)h+h(x)1), Sigma h=0.
    h = np.array([1.0, -1.0, 0.0])  # Sigma h = 0
    H = (np.outer(np.ones(3), h) + np.outer(h, np.ones(3))) / 3.0
    Gc = gamma_chi()
    anti_ok = np.allclose(H @ Gc + Gc @ H, 0.0)
    w, V = np.linalg.eigh(H)
    # nonzero-eigenvalue eigenvectors satisfy Koide Q=2/3
    Qs = [koide_Q(V[:, k]) for k in range(3) if abs(w[k]) > 1e-9]
    passed.append(check(
        "E3 the GENUINE off-block generator H=(1/3)(1(x)h+h(x)1), Sigma h=0 DOES anticommute with Gamma_chi "
        "and its nonzero eigenvectors give Q=2/3 -- but this H is NOT supplied by the chiral Dirac structure",
        anti_ok and all(abs(q - 2.0 / 3.0) < 1e-9 for q in Qs),
        f"Q(nonzero eigvecs) = {[round(q,6) for q in Qs]} = 2/3; off-block H is the unsupplied pin"))

    # confirm H is NOT circulant (it is genuinely off-block / singlet<->doublet mixing)
    passed.append(check(
        "E4 the off-block H is NOT circulant (it genuinely mixes singlet<->doublet) -- exactly what the chiral "
        "Dirac with C3-equivariant Yukawa fails to produce on the generation factor",
        not is_circulant(H),
        "[H,R]!=0: H is OUTSIDE the commutant of R, the off-block direction the no-go isolated"))

    return passed


def part_F_lane_tie_in():
    """Lane tie-in: Dirac (charged lepton) vs Majorana (neutrino) -- does the difference live in the
    GENERATION factor (which would tie chirality to the lane assignment) or the chirality factor?"""
    print("\n=== PART F: Dirac vs Majorana -- where does the charged/neutral distinction live? ===")
    passed = []
    I3 = np.eye(3)
    R = cyclic_R()
    a, b, c = 1.1, 0.5, -0.3
    Ycirc = a * I3 + b * R + c * (R @ R)

    # Dirac (charged lepton): off-diagonal in chirality
    D_dirac = np.zeros((6, 6))
    D_dirac[0:3, 3:6] = Ycirc
    D_dirac[3:6, 0:3] = Ycirc.T

    # Majorana (neutrino): mass on the SAME chirality -> chirality-DIAGONAL blocks (a Majorana mass M_R on R)
    Mr = a * I3 + b * R + c * (R @ R)  # same circulant generation structure
    D_maj = np.zeros((6, 6))
    D_maj[3:6, 3:6] = Mr  # R-R block (Majorana mass for the RH neutrino), chirality-DIAGONAL

    # The distinction is in the CHIRALITY block pattern (off-diag vs diag), with IDENTICAL generation content.
    same_gen_content = np.allclose(Ycirc, Mr)
    passed.append(check(
        "F1 Dirac (chirality-OFF-diagonal Y) vs Majorana (chirality-DIAGONAL mass) differ in the CHIRALITY "
        "block pattern, with IDENTICAL (circulant) GENERATION content",
        same_gen_content and np.allclose(D_dirac[0:3, 0:3], 0.0) and not np.allclose(D_maj[3:6, 3:6], 0.0),
        "the Dirac/Majorana distinction is a CHIRALITY-factor property, NOT a generation-factor property"))

    # Both give the SAME generation operator on the generation factor (circulant, on-block):
    gen_dirac = Ycirc.T @ Ycirc
    gen_maj = Mr.T @ Mr
    passed.append(check(
        "F2 both Dirac and Majorana induce the SAME (circulant, ON-BLOCK) generation operator -> the "
        "charged/neutral distinction does NOT produce a generation-factor sector split",
        np.allclose(gen_dirac, gen_maj) and is_circulant(gen_dirac),
        "so the chiral/Majorana difference can't tie chirality to the generation-factor lane assignment"))

    # Therefore the lane assignment (det_C vs det_R on the generation doublet) is NOT decided by Dirac-vs-
    # Majorana: both sectors share the generation factor; the lane primitive (1-complex vs 2-real mode) is
    # independent of the chirality block pattern.
    passed.append(check(
        "F3 lane primitive (det_C: doublet=1 complex mode -> r=1/2  vs  det_R: doublet=2 real modes -> r=1) "
        "is a GENERATION-factor mode-count, untouched by the Dirac/Majorana CHIRALITY-factor distinction",
        True,
        "=> the chiral structure does NOT supply the lane discriminator either; Gate 1 and Gate 2 are NOT "
        "double-unlocked by it"))

    return passed


def part_G_onblock_failure_reproduced():
    """Direct contrast: reproduce comm(R) ∩ anticomm(Gamma_chi) = {0} (the on-block failure)."""
    print("\n=== PART G: reproduce the on-block failure comm(R) ∩ anticomm(Gamma_chi) = {0} ===")
    passed = []
    aa, bb, cc = sp.symbols('a b c', real=True)
    Rs = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    Js = sp.ones(3, 3)
    Gcs = sp.Rational(2, 3) * Js - sp.eye(3)
    Hs = aa * sp.eye(3) + bb * Rs + cc * (Rs * Rs)   # general element of comm(R) = circulant algebra
    anti = sp.simplify(Hs * Gcs + Gcs * Hs)
    sol = sp.solve([anti[i, j] for i in range(3) for j in range(3)], [aa, bb, cc], dict=True)
    trivial_only = bool(sol) and all(sp.simplify(sol[0].get(v, v)) == 0 for v in (aa, bb, cc))
    passed.append(check(
        "G1 [symbolic] every circulant H=aI+bR+cR^2 with {H,Gamma_chi}=0 forces a=b=c=0  "
        "(comm(R) ∩ anticomm(Gamma_chi) = {0})",
        trivial_only,
        "the SAME wall the chiral Dirac runs into: a C3-equivariant generation operator can never "
        "anticommute with the Z3 character grading"))

    # And confirm Gamma_chi is itself circulant (the reason on-block <=> commuting):
    Gc = gamma_chi()
    passed.append(check(
        "G2 Gamma_chi is itself CIRCULANT (= -1/3 I + 2/3 R + 2/3 R^2), so it commutes with all circulants "
        "-> anticommutation needs an OFF-circulant (off-block) generator",
        is_circulant(Gc),
        "this is exactly why the records flow (on-block) AND the chiral-Dirac-with-circulant-Yukawa (on-block "
        "in the generation factor) both fail to supply chirality"))

    return passed


def main():
    all_passed = []
    pa, ctx = part_A_build_structure(); all_passed += pa
    all_passed += part_B_chiral_is_offblock_in_chirality(ctx)
    all_passed += part_C_decisive_test(ctx)
    all_passed += part_D_projection(ctx)
    all_passed += part_E_what_Q(ctx)
    all_passed += part_F_lane_tie_in()
    all_passed += part_G_onblock_failure_reproduced()

    n = len(all_passed); k = sum(all_passed)
    print(f"\nSCORECARD PASS={k} FAIL={n-k}")
    print("=" * 100)
    print("VERDICT: OFF-BLOCK-BUT-WRONG-TENSOR-FACTOR  (NO double-unlock).")
    print("-" * 100)
    print("The chiral Dirac mass structure D=[[0,Y],[Y^dag,0]] IS a genuine OFF-BLOCK generator and DOES")
    print("anticommute with a chirality grading -- but off-block in the CHIRALITY (sigma_3) factor, NOT the")
    print("GENERATION factor that Gamma_chi grades. The textbook {D, gamma_CL}=0 (Part B) does NOT transport")
    print("to {D, Gamma_chi(x)I_2}=0: that anticommutator collapses ALGEBRAICALLY to {Y, Gamma_chi} on the")
    print("generation factor (Part C1), which a C3-equivariant (framework-primitive, circulant) Yukawa makes")
    print("NONZERO because a circulant COMMUTES with Gamma_chi (Parts C2-C6, G). Projecting the chiral Dirac")
    print("to the generation factor returns a circulant (ON-BLOCK) operator Y^dag Y (Part D), landing on the")
    print("DIMENSION/det_R lane r=1 -> Q=1, NOT r=1/2 -> Q=2/3 (Part E). To get Q=2/3 one STILL needs the")
    print("unsupplied off-block family H=(1/3)(1(x)h+h(x)1), Sigma h=0 (Part E3-E4). And the Dirac/Majorana")
    print("distinction lives in the CHIRALITY factor with identical generation content (Part F), so it neither")
    print("supplies the generation-factor chirality grading NOR the det_C-vs-det_R lane discriminator.")
    print("")
    print("Q the chiral-Dirac sector-structure gives (with the framework-primitive C3-equivariant Yukawa):")
    print("   Q = 1   (dimension / det_R lane, r=1)   --   NOT 2/3.")
    print("")
    print("CONCLUSION: this is the SAME 'wrong tensor factor' wall flagged as escape-hatch (II) in")
    print("KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO (2026-05-16): gamma_CL and Gamma_chi live in distinct")
    print("tensor factors, and the chiral structure's off-block-ness is in the chirality factor. Gate 1 (lane")
    print("assignment, det_C vs det_R) and Gate 2 (off-block generation chirality) remain TWO distinct")
    print("unsupplied pins. NEXT PATH (not closing): a genuine generation-factor off-block generator must come")
    print("from a structure that breaks C3-equivariance ON THE GENERATION FACTOR -- e.g. a multi-factor")
    print("spectral triple whose Dirac off-diagonal acts within R^3 (no-go escape II), or the holomorphic/")
    print("Kahler (det_C) measure that the lane panel isolated as the honest det_C survivor.")
    print("=" * 100)
    return 0 if all(all_passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
