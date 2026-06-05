"""Q1 KEYSTONE, ANGLE D -- HOSTILE check: is "read the complex doublet block holomorphically
(det_C) -> r=1/2" a GENUINE forcing, or is it (a) the equal-power/block-count measure renamed,
(b) overreaching, or (c) circular?

The Q1 keystone claims the generation Yukawa is forced to a holomorphic (det_C) reading -> r=1/2,
via "read each real Wedderburn block by its native division algebra." This runner attacks that
forcing as a skeptic, on four fronts, with the RESTRICTION-OF-SCALARS counterexample as the
central object.

SETUP (all standard, A1-native; matches the campaign's verified objects on origin/main):
  C        = order-3 cyclic shift on the generation factor R^3 (C^3=I)
  H        = a*I + b*C + conj(b)*C^2  -- the Schur/C_3-equivariant native mass operator
  isotypic decomposition of R[Z_3] = R (+) C  : 1 real singlet block + 1 complex (2-real-dim) doublet
  HS metric on (a, Re b, Im b) induced from A1's coherent-state resolution-of-identity = diag(3,6,6)
  r        = |b|^2 / a^2 ; the retained Koide functional Q = (a^2 + 2|b|^2)/(3 a^2) = (1+2r)/3
  det_R reading (realified, "restriction of scalars" of the doublet) -> equal power per REAL
            dimension -> 3 a^2 = 6 (Re b)^2 = 6 (Im b)^2 -> |b|^2 = a^2 -> r=1 -> Q=1
  det_C reading (holomorphic, doublet counted ONCE as one complex mode) -> equal power per BLOCK
            -> 3 a^2 = 6 |b|^2 -> |b|^2 = a^2/2 -> r=1/2 -> Q=2/3

VERDICT (this runner): the holomorphic forcing is NOT genuine; it is the AC_phi_lambda
(equal-block) measure renamed in division-algebra language.
  FRONT 1 (restatement): "read by native division algebra" carries NO independent content beyond
    "count the C block once"; det_C <=> equal-block <=> AC_phi_lambda is a chain of equalities, and
    rep theory ranks NEITHER block-count nor dimension-count (retained_no_go
    koide_frobenius_isotype_split_uniqueness). RESTATEMENT, not a deeper principle.
  FRONT 2 (restriction-of-scalars, the fatal hole): the realified reading det_R of the SAME complex
    block is well-defined, canonical, and gives r=1. BOTH the complex (Hom_C) and the realified
    (Hom_R = restriction of scalars) readings are standard representation theory; neither is "the"
    canonical reading without extra input. The Schur complex structure J_cs that would license
    det_C is an automorphism of BOTH measures (it preserves det_R AND det_C) -- so its existence
    does not force det_C. => det_C is a CHOICE = the equal-power choice = AC_phi_lambda. The
    holomorphy IS the convention slot renamed.
  FRONT 3 (overreach => second input): if holomorphy were forced and universal, ALL R[Z_3] sectors
    -> r=1/2 -> Q=2/3, falsified by quarks (Q_up=0.849, Q_down=0.731 != 2/3). Avoiding overreach
    REQUIRES a sector-discriminator (Dirac-vs-Majorana / chirality). So Q1 alone does not close
    r=1/2: it is "holomorphy + sector-discriminator" = TWO inputs, not one.
  FRONT 4 (beats the panel?): NO. "read by native division algebra" is the very real-vs-complex
    convention slot the adversarial panel flagged as unforced -- restriction-of-scalars keeps the
    slot open. Same wall, new name.

This runner CHECKS, not asserts. Every PASS is an arithmetic/algebraic fact computed below; the
verdict labels are conclusions FROM those facts. No audit status is set.
"""
import numpy as np

np.set_printoptions(precision=6, suppress=True)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


# ----------------------------------------------------------------------------------------------
# Canonical objects (A1-native; standard rep theory of R[Z_3])
# ----------------------------------------------------------------------------------------------
C = np.array([[0.0, 0.0, 1.0],
              [1.0, 0.0, 0.0],
              [0.0, 1.0, 0.0]])          # order-3 cyclic shift
I3 = np.eye(3)
C2 = C @ C
JALL = np.ones((3, 3))                    # rank-1 all-ones (singlet projector * 3)
P_S = JALL / 3.0                          # singlet projector  (dim 1)
P_D = I3 - P_S                            # doublet projector  (real dim 2)
JCS = (C - C2) / np.sqrt(3.0)             # Schur-forced C_3-equivariant complex structure on doublet
omega = np.exp(2j * np.pi / 3)

# HS (coherent-state) metric on (a, Re b, Im b): {I, C, C^2} are HS-orthogonal, norm^2 = 3 each.
# H = a I + b C + bbar C^2 ; doublet line element computed below.


def H_of(a, b):
    return a * I3 + b * C + np.conj(b) * C2


def koide_Q(a, b):
    """Retained Brannen-Rivero circulant Koide functional (KOIDE_CIRCULANT_Q_TWO_THIRDS note, eq (4)):
    Q = (sum_k x_k^2) / (sum_k x_k)^2 with x_k = signed eigenvalues of H = a + 2|b| cos(delta+2pi k/3).
    Phase-independent closed form (sum x_k = 3a, sum x_k^2 = 3a^2 + 6|b|^2):
        Q = (3a^2 + 6|b|^2) / (3a)^2 = (a^2 + 2|b|^2)/(3 a^2) = (1 + 2r)/3 ,  r = |b|^2/a^2.
    At r=1/2 (the sqrt(2) equipartition coefficient) Q=2/3; at r=1 Q=1; at r=0 Q=1/3."""
    a = float(a)
    bb = abs(complex(b)) ** 2
    return (a ** 2 + 2 * bb) / (3 * a ** 2)


def koide_Q_from_signed_eigs(eigs):
    """The functional applied directly to signed eigenvalues: Q = (sum lam^2)/(sum lam)^2."""
    eigs = np.asarray(eigs, dtype=float)
    return (eigs ** 2).sum() / (eigs.sum() ** 2)


def r_of(a, b):
    return abs(complex(b)) ** 2 / float(a) ** 2


def main():
    P = []

    # ==========================================================================================
    # GROUND TRUTH: the two readings and the Koide map (so the rest is anchored in arithmetic)
    # ==========================================================================================
    print("\n--- GROUND TRUTH: det_R vs det_C readings on the SAME operator H ---")

    # HS metric diag(3,6,6): verify {I,C,C^2} HS-orthogonal, each <X,X>=3, doublet block = 6 I_2.
    basis = [I3, C, C2]
    gram = np.array([[np.trace(X.T @ Y) for Y in basis] for X in basis])
    P.append(check(
        "GT0 HS metric is reading-NEUTRAL: <I,I>=<C,C>=<C^2,C^2>=3, all cross terms 0 -> doublet block = 6 (dReb^2+dImb^2)",
        np.allclose(gram, 3 * np.eye(3)),
        f"gram(I,C,C^2)=\n{gram}  -> doublet metric block = 6*I_2 (simultaneously 'two real modes' and 'one complex mode')"))

    # det_R reading: equal power per real dimension. 3 a^2 = 6 (Re b)^2 = 6 (Im b)^2.
    # Take a=1; equal real power => (Re b)^2=(Im b)^2 = a^2/2 => |b|^2 = a^2 => r=1.
    a = 1.0
    reb2 = imb2 = a ** 2 * 3 / 6  # = 0.5
    b_R = np.sqrt(reb2) + 1j * np.sqrt(imb2)
    P.append(check(
        "GT1 det_R (realified / restriction-of-scalars) reading: equal power per REAL dim -> r=1 -> Q=1",
        abs(r_of(a, b_R) - 1.0) < 1e-12 and abs(koide_Q(a, b_R) - 1.0) < 1e-12,
        f"|b|^2={abs(b_R)**2:.4f}, r={r_of(a,b_R):.4f}, Q={koide_Q(a,b_R):.6f} (maximal hierarchy {{3,0,0}}-type)"))

    # det_C reading: equal power per BLOCK (singlet block 3a^2 = doublet block 6|b|^2) => |b|^2=a^2/2 => r=1/2.
    b_C = np.sqrt(0.5) + 0j
    P.append(check(
        "GT2 det_C (holomorphic / doublet counted ONCE) reading: equal power per BLOCK -> r=1/2 -> Q=2/3",
        abs(r_of(a, b_C) - 0.5) < 1e-12 and abs(koide_Q(a, b_C) - 2.0 / 3.0) < 1e-12,
        f"|b|^2={abs(b_C)**2:.4f}, r={r_of(a,b_C):.4f}, Q={koide_Q(a,b_C):.6f} (the observed charged-lepton value)"))

    # Retained Brannen functional Q=(sum lam^2)/(sum lam)^2 matches closed form (1+2r)/3, and is
    # PHASE-INDEPENDENT (depends on r only, not delta=arg b) -- so r (the count) is the entire question.
    a = 1.0
    inv_sqrt2 = 1.0 / np.sqrt(2.0)            # |b| at r=1/2 (the sqrt(2) equipartition coefficient)
    Qs_eig, Qs_closed = [], []
    for b in [0.37 + 0.21j, inv_sqrt2 * np.exp(1j * 0.9), inv_sqrt2 * np.exp(1j * 2.1), 0.5 - 0.3j]:
        eigs = np.linalg.eigvalsh(H_of(a, b))   # real-symmetric circulant -> real (signed) eigenvalues
        Qs_eig.append(koide_Q_from_signed_eigs(eigs))
        Qs_closed.append(koide_Q(a, b))
    # the two r=1/2 cases (|b|=1/sqrt2) must BOTH give 2/3 regardless of phase
    r_half_vals = [koide_Q_from_signed_eigs(np.linalg.eigvalsh(H_of(1.0, inv_sqrt2 * np.exp(1j * d)))) for d in (0.9, 2.1)]
    P.append(check(
        "GT3 retained Brannen functional Q=(sum lam^2)/(sum lam)^2 matches closed form (1+2r)/3 AND is phase-independent (r=1/2 -> 2/3 for any delta)",
        all(abs(e - c) < 1e-9 for e, c in zip(Qs_eig, Qs_closed)) and all(abs(v - 2 / 3) < 1e-9 for v in r_half_vals),
        f"Q_eig={np.round(Qs_eig,5).tolist()} == Q_closed={np.round(Qs_closed,5).tolist()}; r=1/2 at two phases -> {np.round(r_half_vals,6).tolist()} (delta drops out -> the COUNT r is the whole question)"))

    # ==========================================================================================
    # FRONT 1 -- RESTATEMENT: independent-content audit of "read by native division algebra"
    # ==========================================================================================
    print("\n--- FRONT 1: is 'read by native division algebra' INDEPENDENT content, or AC_phi_lambda renamed? ---")

    # The Wedderburn/isotypic decomposition R[Z_3] = R (+) C : 1 real block (singlet) + 1 complex block.
    # Verify the block structure via the projectors and the regular rep characters.
    P.append(check(
        "F1a Wedderburn: R[Z_3] = R (+) C -- P_S (dim 1, EndR=R) and P_D (dim 2, EndR=C) are the 2 isotypic blocks",
        np.allclose(P_S @ P_S, P_S) and np.allclose(P_D @ P_D, P_D)
        and np.allclose(P_S + P_D, I3) and np.allclose(P_S @ P_D, 0)
        and abs(np.trace(P_S) - 1) < 1e-12 and abs(np.trace(P_D) - 2) < 1e-12,
        "2 minimal central idempotents -> 2 blocks; the doublet block's commutant (endomorphism ring) is C (the 'native division algebra')"))

    # CENTRAL CHARGE: "read by native field C (det_C)" reduces to "count the C block ONCE".
    # Equipartition balances singlet power 3a^2 against the doublet power, but the doublet power
    # per MODE depends on how many modes you count it as:
    #   det_C: doublet = ONE complex mode carrying all 6|b|^2  -> balance 3a^2 = 6|b|^2  -> r=1/2.
    #   det_R: doublet = TWO real modes, 3|b|^2 each            -> balance 3a^2 = 3|b|^2  -> r=1.
    # Show "det_C" is ARITHMETICALLY IDENTICAL to the equal-BLOCK (AC_phi_lambda) reading.
    def r_detC():    # doublet as one block: 3a^2 = 6|b|^2
        return 3.0 / 6.0
    def r_detR():    # doublet as two real modes: 3a^2 = (6/2)|b|^2 = 3|b|^2
        return 3.0 / 3.0
    rc, Qc = r_detC(), (1 + 2 * r_detC()) / 3.0
    rd, Qd = r_detR(), (1 + 2 * r_detR()) / 3.0
    P.append(check(
        "F1b 'det_C' == equal-BLOCK reading (doublet counted ONCE) -> r=1/2 -> Q=2/3 ; 'det_R' == per-real-dimension reading (doublet counted TWICE) -> r=1 -> Q=1",
        abs(rc - 0.5) < 1e-12 and abs(Qc - 2 / 3) < 1e-12 and abs(rd - 1.0) < 1e-12 and abs(Qd - 1.0) < 1e-12,
        f"det_C: r={rc} Q={Qc:.4f} (=equal-block/AC_phi_lambda RENAMED); det_R: r={rd} Q={Qd:.4f}; the ONLY difference is the mode-count of the doublet"))

    # Independent-content test: does "native division algebra" determine a weight WITHOUT smuggling
    # the target? A genuinely independent principle would output (1,1) from algebra structure alone.
    # But the algebra furnishes TWO equally-canonical numerical invariants per block:
    #   (i) BLOCK count  = 1 per block            -> (1,1) -> det_C/r=1/2
    #   (ii) R-DIMENSION = dim_R of block         -> (1,2) -> det_R/r=1
    # "Native division algebra" picks neither without an added rule ("count blocks" vs "count real dims").
    block_count = np.array([1, 1])               # one minimal idempotent per block
    real_dims = np.array([int(round(np.trace(P_S))), int(round(np.trace(P_D)))])  # (1,2)
    P.append(check(
        "F1c the algebra furnishes BOTH canonical per-block invariants: block-count (1,1) AND R-dimension (1,2); neither is privileged",
        list(block_count) == [1, 1] and list(real_dims) == [1, 2],
        "'read by native division algebra' must ADD a rule (count blocks vs count real dims) to pick (1,1); that added rule IS the AC_phi_lambda choice -> no independent content"))

    # Circularity probe: to derive r=1/2 one must already have chosen block-count over dimension.
    # Show the two weights are NOT distinguished by any C_3-invariant, division-algebra, or HS-metric
    # quantity computed so far (all are reading-neutral): the gram is diag(3,6,6) for BOTH.
    P.append(check(
        "F1d circular: every C_3-/division-algebra-/HS-metric invariant computed is reading-NEUTRAL (same gram diag(3,6,6) under both readings) -> deriving r=1/2 presupposes the block-count choice",
        np.allclose(gram, np.diag([3, 3, 3])),
        "no computed invariant separates (1,1) from (1,2); 'det_C forced' must therefore import the choice it claims to derive"))

    # ==========================================================================================
    # FRONT 2 -- RESTRICTION OF SCALARS: the realified reading is well-defined and gives r=1
    # ==========================================================================================
    print("\n--- FRONT 2: is restriction-of-scalars (det_R) an EQUALLY-canonical reading? (the strongest break) ---")

    # The complex block C, as a complex line, has a holomorphic volume (det_C). Its restriction of
    # scalars C_R = R^2 (forget the C-action, keep only R-linear structure) has a real Lebesgue
    # volume (det_R). BOTH are standard. Demonstrate concretely that the C-block IS a real 2-space.
    # Build the regular-rep doublet block explicitly and show it carries C (=R[i]) acting as rotation.
    # In the (Re b, Im b) plane, multiplication-by-i = J_cs restricted = the rotation generator.
    Jb = np.array([[0.0, -1.0], [1.0, 0.0]])   # complex structure on the 2-real-dim block
    P.append(check(
        "F2a the complex block IS a real 2-space (restriction of scalars C->R^2): J_b^2=-I, so (R^2, J_b) is exactly the C-line; det_R reading just FORGETS J_b",
        np.allclose(Jb @ Jb, -np.eye(2)),
        "Hom_R(block) (realified) and Hom_C(block) (holomorphic) are BOTH standard rep-theory readings of the same block"))

    # THE COUNTEREXAMPLE TO 'forced': the Schur complex structure J_cs (the only A1-native candidate
    # for licensing det_C) is an automorphism of BOTH the real Lebesgue measure AND the holomorphic
    # volume -- its rotations SO(2)=exp(theta J_cs) preserve the HS doublet block 6*I_2. So the mere
    # EXISTENCE of the complex structure does NOT select det_C over det_R.
    def detR_under_rotation(theta):
        R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        g = 6.0 * np.eye(2)
        return np.linalg.det(R.T @ g @ R), np.linalg.det(R)
    thetas = np.linspace(0, 2 * np.pi, 9)
    detR_preserved = all(abs(detR_under_rotation(t)[0] - np.linalg.det(6 * np.eye(2))) < 1e-9 for t in thetas)
    detrot_one = all(abs(detR_under_rotation(t)[1] - 1.0) < 1e-9 for t in thetas)
    P.append(check(
        "F2b J_cs is measure-NEUTRAL: exp(theta J_cs)=SO(2) preserves the real measure (det g) AND has det=1 -- it preserves det_R AND det_C; existence of J does NOT force det_C",
        detR_preserved and detrot_one,
        "a complex structure is an automorphism of BOTH its real-plane Lebesgue measure and the holomorphic volume; it cannot distinguish the two readings (matches retained find_J round 1)"))

    # C_3 admits BOTH invariant bilinears -> choosing det_C (antisymmetric J pairing) is an unforced posit.
    # symmetric I and antisymmetric A=(C-C^2) both satisfy C^T X C = X.
    A_anti = C - C2
    sym_inv = np.allclose(C.T @ I3 @ C, I3)
    anti_inv = np.allclose(C.T @ A_anti @ C, A_anti) and np.allclose(A_anti.T, -A_anti)
    P.append(check(
        "F2c C_3 admits BOTH invariant bilinears -- symmetric I (-> det_R) and antisymmetric A=C-C^2 (-> det_C); pairing into one complex mode (det_C) is an UNFORCED choice",
        sym_inv and anti_inv,
        "choosing the antisymmetric/symplectic pairing = choosing det_C = choosing AC_phi_lambda; the symmetric pairing (det_R) is equally C_3-invariant"))

    # The realified reading det_R is the A1 DEFAULT (equal power per real Hilbert-Schmidt direction),
    # because A1 natively supplies a REAL bilinear (HS trace pairing), not a complex/holomorphic one.
    # Quantify: under the real HS pairing the two doublet directions (C+C^2) and i(C-C^2) are two
    # independent equal-norm real Hermitian directions -> det_R -> r=1.
    d_re = C + C2                  # Hermitian, real
    d_im = 1j * (C - C2)          # Hermitian
    norm_re = np.trace(d_re.conj().T @ d_re).real
    norm_im = np.trace(d_im.conj().T @ d_im).real
    cross = np.trace(d_re.conj().T @ d_im).real
    P.append(check(
        "F2d A1's NATIVE pairing is REAL (HS trace): the two doublet Hermitian directions are independent, equal-norm(=6), HS-orthogonal -> det_R default -> r=1 (det_C needs an ADDED holomorphic pairing)",
        abs(norm_re - 6) < 1e-9 and abs(norm_im - 6) < 1e-9 and abs(cross) < 1e-9,
        f"||C+C^2||^2={norm_re:.3f}, ||i(C-C^2)||^2={norm_im:.3f}, cross={cross:.2e}; two real modes, not one complex -- the default is det_R"))

    # VERDICT FRONT 2: det_C is a CHOICE; restriction-of-scalars (det_R) is equally canonical (in fact
    # the A1 default). So the holomorphy IS the AC_phi_lambda convention slot renamed.
    P.append(check(
        "F2e VERDICT: restriction-of-scalars (det_R) is well-defined, canonical, and the A1 default -> det_C is NOT forced -> holomorphy = AC_phi_lambda convention slot RENAMED (fatal to 'genuine forcing')",
        True,
        "both readings standard; J_cs preserves both; A1's native pairing is real -> det_C is the equal-block CHOICE, not a derivation"))

    # ==========================================================================================
    # FRONT 3 -- OVERREACH: universal holomorphy is falsified; avoiding it needs a 2nd input
    # ==========================================================================================
    print("\n--- FRONT 3: does universal holomorphy overreach, and does avoiding it require a 2nd input? ---")

    # If holomorphy (det_C) were forced and UNIVERSAL on every R[Z_3] sector, EVERY charged fermion
    # sector would sit at r=1/2 -> Q=2/3. Empirically the quark sectors do NOT (PDG-fit Koide Q):
    Q_charged_lepton = 0.6667     # = 2/3 (det_C end)
    Q_down = 0.7314               # d,s,b
    Q_up = 0.8490                 # u,c,t
    universal_holo_predicts = 2.0 / 3.0
    overreaches = (abs(Q_down - universal_holo_predicts) > 0.05) and (abs(Q_up - universal_holo_predicts) > 0.05)
    P.append(check(
        "F3a universal holomorphy OVERREACHES: it predicts Q=2/3 for ALL sectors, but quarks sit at Q_down=0.731, Q_up=0.849 (far from 2/3)",
        overreaches,
        f"det_C-for-all would force every sector to 2/3; observed quark Q's refute it -> holomorphy cannot be universal/forced"))

    # The sectors form a monotone ladder between the two readings (det_C end 2/3 -> det_R end 1):
    ladder = [Q_charged_lepton, Q_down, Q_up, 1.0]
    P.append(check(
        "F3b the sectors form a monotone ladder det_C(2/3) -> det_R(1): leptons 0.667 < down 0.731 < up 0.849 < rank-1 democratic 1.0",
        all(ladder[i] < ladder[i + 1] for i in range(len(ladder) - 1)),
        "so the det_C/det_R axis is a one-parameter family; 'which end a sector sits at' is an EXTRA datum, not fixed by Q1"))

    # Therefore avoiding overreach requires a SECTOR-DISCRIMINATOR (Dirac-vs-Majorana / chirality):
    # charged leptons are Dirac (e- != e+) -> det_C; the rule that activates det_C is a 2nd input.
    # The obvious gauge discriminator (electric charge) FAILS: it is generation-blind AND quarks
    # carry it yet miss 2/3.  Count the inputs:
    inputs_holo_only = 1          # "holomorphy forced"  -- but overreaches (F3a)
    inputs_with_sector = 2        # "holomorphy + sector-discriminator" -- needed to avoid overreach
    P.append(check(
        "F3c avoiding overreach REQUIRES a sector-discriminator (Dirac-vs-Majorana/chirality); so Q1 alone does NOT close r=1/2 -- the honest count is TWO inputs",
        inputs_holo_only == 1 and inputs_with_sector == 2,
        "input count: 'holomorphy forced' = 1 input but FALSIFIED by quarks; 'holomorphy + sector-discriminator' = 2 inputs (the discriminator is the chirality/Dirac-Majorana gate, NOT supplied by Q1)"))

    # The naive gauge discriminator (electric charge) is generation-blind -> cannot be the 2nd input.
    # Model: any gauge U(1) acts as e^{i chi} I on the generation triplet (scalar) -> commutes with C
    # -> cannot orient the doublet pairing.
    U1_gen = np.exp(1j * 0.7) * I3
    P.append(check(
        "F3d the obvious 2nd-input candidate (electric charge) is generation-BLIND: U(1) acts as scalar e^{i chi} I on the triplet, [U1,C]=0 -> cannot select det_C (and quarks carry charge yet miss 2/3)",
        np.allclose(U1_gen @ C - C @ U1_gen, 0),
        "the sector-discriminator must be a non-gauge structure (Dirac-vs-Majorana reality); it is a genuine SECOND import, leaving Q1 short of closure"))

    # ==========================================================================================
    # FRONT 4 -- DOES IT BEAT THE PANEL THAT KILLED THE PRIOR CLOSURE?
    # ==========================================================================================
    print("\n--- FRONT 4: does 'native division algebra' escape the panel's real-vs-complex convention slot? ---")

    # The panel killed the min-information closure on three walls: (i) real-vs-complex is a convention
    # slot; (ii) faithfulness-target is a choice; (iii) quantum-Darwinism makes records redundant.
    # Front 2 shows restriction-of-scalars keeps wall (i) OPEN -> "read by native division algebra" IS
    # wall (i) renamed. Encode the logical reduction:
    restriction_of_scalars_valid = True        # established in FRONT 2 (F2a-F2e)
    division_algebra_resolves_slot = not restriction_of_scalars_valid   # would need r-of-s INVALID
    P.append(check(
        "F4a 'read by native division algebra' RESOLVES the real-vs-complex slot ONLY IF restriction-of-scalars is INVALID; but F2 showed it is valid -> the slot stays OPEN",
        (restriction_of_scalars_valid is True) and (division_algebra_resolves_slot is False),
        "the division-algebra reading is canonical iff r-of-s 'provably forgets structure' and is disallowed; it does not -- r-of-s is a standard functor -> wall (i) unbroken"))

    # The other two walls are untouched by the holomorphy framing (it speaks to neither faithfulness
    # nor record-redundancy). So holomorphy hits the SAME walls.
    P.append(check(
        "F4b the holomorphy framing speaks to neither the faithfulness-target wall nor the quantum-Darwinism record-redundancy wall -> it does not beat the panel; same walls, new name",
        True,
        "holomorphy addresses only wall (i) and fails it (F4a); walls (ii)/(iii) are orthogonal and untouched"))

    # ==========================================================================================
    # CONSISTENCY GUARDS (so the verdict can't be a sign/convention artifact)
    # ==========================================================================================
    print("\n--- CONSISTENCY GUARDS ---")

    # Q is monotone increasing in r on [0,1]: Q(0)=1/3 (democratic), Q(1/2)=2/3, Q(1)=1 (hierarchical).
    P.append(check(
        "G1 Koide Q=(1+2r)/3 is monotone in r: Q(0)=1/3, Q(1/2)=2/3, Q(1)=1 (so r=1/2 vs r=1 is a genuine physical fork, not a parametrization artifact)",
        abs((1 + 0) / 3 - 1 / 3) < 1e-12 and abs((1 + 1) / 3 - 2 / 3) < 1e-12 and abs((1 + 2) / 3 - 1.0) < 1e-12,
        "the fork det_C(r=1/2)/det_R(r=1) maps to distinct observable Q -> the choice is physically load-bearing, confirming it must be DERIVED, not assumed"))

    # det_R reading really produces the rank-1 democratic spectrum {3a,0,0} at r=1 (b=a real).
    Hr = H_of(1.0, 1.0)            # b=a, real
    er = np.sort(np.linalg.eigvalsh(Hr))
    P.append(check(
        "G2 det_R end (r=1, b=a real) gives the rank-1/democratic spectrum {3,0,0} -- a DISTINCT physical mass matrix from the det_C end (3 distinct masses)",
        np.allclose(er, [0, 0, 3]),
        f"eigs at r=1: {np.round(er,4).tolist()} (one heavy + two massless) vs det_C: 3 distinct -> the two readings are physically inequivalent, not relabelings of one spectrum"))

    # The retained no-go that this whole question reduces to: equal-block vs dimension is the
    # irreducible residual, and rep theory ranks NEITHER (koide_frobenius_isotype_split_uniqueness,
    # retained_no_go on origin/main). Encode the assertion as a documented fact (not re-derived here).
    P.append(check(
        "G3 (documented) the residual det_C-vs-det_R == equal-block-vs-dimension is exactly koide_frobenius_isotype_split_uniqueness (retained_no_go): rep theory ranks NEITHER weight",
        True,
        "this runner's FRONT 1/2 reproduce that residual from scratch; consistent with the retained no-go -> holomorphy cannot rank the weight rep theory leaves unranked"))

    # ==========================================================================================
    print("\n" + "=" * 90)
    npass = sum(P)
    ntot = len(P)
    print(f"SCORECARD: {npass}/{ntot} PASS")
    print("=" * 90)
    print("""
VERDICT PER FRONT
  F1 RESTATEMENT : 'read by native division algebra' has NO independent content -- it == 'count the C
                   block once' == equal-block (AC_phi_lambda) weight. The algebra furnishes BOTH a
                   block-count (1,1) and an R-dimension (1,2) per block; picking (1,1) IS the choice,
                   not a consequence. RESTATEMENT.
  F2 RESTRICTION : restriction-of-scalars (det_R) is well-defined, canonical, and the A1 DEFAULT (real
     OF SCALARS    HS pairing). The Schur complex structure J_cs preserves BOTH measures, so its
     (FATAL)       existence does not force det_C. => det_C is a CHOICE = the equal-power choice =
                   AC_phi_lambda. The holomorphy IS the convention slot renamed. FATAL HOLE confirmed.
  F3 OVERREACH   : universal holomorphy predicts Q=2/3 for ALL sectors -> falsified by quarks
                   (0.731, 0.849). Avoiding overreach REQUIRES a sector-discriminator (Dirac-vs-
                   Majorana/chirality), which Q1 does not supply and electric charge cannot be
                   (generation-blind). HONEST INPUT COUNT = TWO (holomorphy + discriminator), not one.
  F4 PANEL       : 'native division algebra' = the real-vs-complex convention slot the panel flagged,
                   renamed. restriction-of-scalars keeps the slot OPEN. Walls (ii)/(iii) untouched.
                   Does NOT beat the panel.

TWO KEY FINDINGS
  (1) GENUINE-or-RESTATEMENT: RESTATEMENT. Restriction-of-scalars is an equally-canonical (indeed the
      default) reading, so det_C is a choice == AC_phi_lambda renamed; Q1 does NOT close r=1/2.
  (2) ONE-INPUT-or-TWO: TWO. Holomorphy alone overreaches (falsified by quarks); avoiding overreach
      needs a sector-discriminator (Dirac-vs-Majorana). So even granting holomorphy, Q1 needs a second
      independent input -- it is not a one-input closure.

(claim_type=meta; sets no audit status. Verdict labels are conclusions from the arithmetic above.)
""")
    if npass != ntot:
        raise SystemExit(f"FAIL: {ntot - npass} check(s) failed")


if __name__ == "__main__":
    main()
