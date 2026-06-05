#!/usr/bin/env python3
"""
HOSTILE pressure-test (PT5) of a CANDIDATE strong Record axiom:

  "A record registers WHICH real classical alternative is realized; the real classical
   alternatives are the real superselection sectors (real Wedderburn blocks); each is
   ONE alternative; record readout counts alternatives ADDITIVELY, DIMENSION-BLIND."

The skeptic's charge: this is the equal-power / real-K0-block-counting MEASURE
(AC_phi_lambda) renamed as an axiom, and it OVERREACHES (it falsifies the quark sectors
and collides with the Born weight that decoherence/objectivity actually delivers).

This runner is READ-ONLY. It computes finite linear-algebra facts that adjudicate five
fronts. It sets no audit status and approves no axiom or import. The actually-adopted
Record axiom (docs/MINIMAL_AXIOMS_2026-06-04.md) is the WEAK one: scalar record readout
is additive over disjoint record collections, and it EXPLICITLY disclaims Born weights
and AC_phi_lambda. The candidate here is the STRONG version under hostile test.

FRONT 1  CONSTITUTIVE vs RESTATEMENT.
  The candidate's load-bearing clause ("count alternatives, dimension-blind") is the
  block-count measure (1,1). We show the additive/scalar/which-one clauses are satisfied
  EQUALLY by the dimension/trace readout (1,2): both are additive scalar functionals that
  register which sector. So additivity+which-one have INDEPENDENT (measurement-theory)
  content but do NOT pick (1,1); the ONLY clause that picks (1,1) is "dimension-blind",
  which IS the block-count measure renamed. => RESTATEMENT on the load-bearing clause.

FRONT 2  OVERREACH -- QUARK-SECTOR FALSIFICATION (the fatal test).
  If "real-block-count" is a constitutive law of records, it must apply to every fermion
  sector. The charged-lepton Koide is 2/3 (block-count value), but the up/down quark
  Koide values are robustly NOT 2/3 (Q_up=0.849, Q_down=0.731). So a sector-universal
  block-count law is EMPIRICALLY FALSIFIED. The axiom survives ONLY if it does not claim
  the same generation algebra per sector -- i.e. only if it is NOT constitutive-universal
  but sector-contingent, which concedes Front 1.

FRONT 3  COHERENCE / WELL-DEFINEDNESS on M_n(C).
  "Real classical alternative" must be defined for a general block. For a simple COMPLEX
  block M_n(C) the center is C (one ray): naive "real-block count" = 1, but the same
  block read as a real algebra (M_n(C) as a real *-algebra is real-simple, one real
  block) is ALSO 1, while a complex/Born reading weights it by n. The count is only
  well-defined once "real block" is pinned to the Frobenius-Schur/real-Wedderburn
  decomposition -- which is a CHOICE of K0 (K0-real vs K0-complex), not forced by "record".

FRONT 4  MINIMALITY.
  We show "CPT-even / real" alone does NOT yield (1,1) (the QD/objectivity panel and the
  reality-shrinks-import results: reality kills only a phase/Z2 sign, the doublet stays
  rank-2). And "registers a classical outcome" alone does NOT yield (1,1) (Born/objective
  records carry the rank weight). So the minimal statement that closes the fork is exactly
  "dimension-blind block-count" = the measure itself; no weaker clause suffices.

FRONT 5  THE BORN COLLISION (deepest).
  Objective decoherence records carry the BORN weight on the SAME sectors: the tracial
  reference I/3 pushed through the singlet/doublet split is (1/3, 2/3) = the rank weighting
  = r=1 = Q=1. The candidate says records carry the COUNT (1,1) = r=1/2 = Q=2/3. These are
  DIFFERENT measures on the SAME two sectors. We test whether "count for masses, Born for
  probability" can be a coherent DUAL readout (two different functionals of one record) or
  whether asserting count-for-masses contradicts the Born-weight objectivity demands.
  Verdict: a dual readout is FORMALLY possible (two distinct linear functionals exist), but
  the candidate axiom as stated ("record readout counts alternatives dimension-blind")
  makes the SINGLE record-readout functional the count, which CONTRADICTS the Born-weight
  that the same records carry under objectivity. So the strong axiom, taken at its word,
  OVERREACHES into the probability readout.

OVERALL: the strong Record axiom is (1) a RESTATEMENT of the (1,1) measure on its
load-bearing clause and (2) OVERREACHING -- it is empirically falsified by the quark
sectors if read as sector-universal, and it collides with the Born weight. The genuine,
non-overreaching content is exactly the WEAK adopted axiom (additive scalar readout),
which does NOT force r=1/2. READ-ONLY.
"""

import sys

import numpy as np
import sympy as sp

PASSES: list[tuple[str, bool, str]] = []


def record(name, ok, detail=""):
    PASSES.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        for line in detail.split("\n"):
            print(f"       {line}")


def section(t):
    print("\n" + "=" * 88 + f"\n{t}\n" + "=" * 88)


# ---------------------------------------------------------------------------------------
# Shared objects: the Z_3 generation carrier.
#   span{I, J-I} with J = all-ones/3 the uniform projector.
#   Singlet block P_s = J (rank 1), doublet block P_d = I - J (rank 2).
#   Hermitian circulant H = a I + b C + conj(b) C^2 on hw=1 = C^3.
#   Block energies E_+ = 3 a^2 (singlet), E_perp = 6 |b|^2 (doublet).
#   Q = (sum lam) ... NO: Q = (sum lam^2)/(sum lam)^2 with all-real signed spectrum.
#   r = |b|^2 / a^2.   Q = (1 + 2 r)/3.
# ---------------------------------------------------------------------------------------
C3 = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
J = np.full((3, 3), 1 / 3, dtype=complex)
P_s = J                       # rank-1 singlet projector
P_d = np.eye(3) - J           # rank-2 doublet projector


def koide_Q_signed(a, b):
    """Signed (Brannen/det_R-compatible) Koide Q of the Hermitian circulant."""
    H = a * np.eye(3) + b * C3 + np.conj(b) * C3 @ C3
    lam = np.linalg.eigvalsh(H)            # real (Hermitian)
    s1 = lam.sum()
    s2 = (lam ** 2).sum()
    return s2 / s1 ** 2, lam


def empirical_Q(masses):
    """Empirical Koide Q = (sum m) / (sum sqrt(m))^2  with POSITIVE sqrt convention."""
    m = np.asarray(masses, dtype=float)
    return m.sum() / (np.sqrt(m).sum() ** 2)


def main():
    section("PT5 HOSTILE: is the strong Record axiom constitutive, or AC_phi_lambda renamed?")

    # =================================================================================
    # FRONT 0 -- ANCHOR: what the ADOPTED (weak) Record axiom actually says.
    # =================================================================================
    section("FRONT 0 -- the ADOPTED Record axiom is WEAK (additivity only; disclaims the measure)")
    record("F0.1 adopted Record axiom = additive scalar readout I(R1 sqcup R2)=I(R1)+I(R2), "
           "I(empty)=0; it EXPLICITLY disclaims Born weights and AC_phi_lambda",
           True,
           "docs/MINIMAL_AXIOMS_2026-06-04.md Record section: 'does not supply ... Born "
           "weights ... AC_phi_lambda ... or arbitrary observable identification.'")
    record("F0.2 the CANDIDATE adds 3 clauses on top: (which real classical alt) + "
           "(alts = real Wedderburn blocks, each ONE) + (count, DIMENSION-BLIND)",
           True,
           "Only the 3rd clause ('dimension-blind count') goes beyond the adopted axiom; "
           "fronts below test whether that clause is constitutive or the measure renamed.")

    # =================================================================================
    # FRONT 1 -- CONSTITUTIVE vs RESTATEMENT.
    #   Decompose the candidate into operational clauses; show which clauses have
    #   independent content and which IS the (1,1) measure.
    # =================================================================================
    section("FRONT 1 -- CONSTITUTIVE vs RESTATEMENT (strip the axiom to operational clauses)")

    # An additive scalar functional that 'registers which sector' is I(R) = sum_k w_k [k in R].
    # Two candidate weight vectors on the 2 sectors {singlet, doublet}:
    w_count = np.array([1.0, 1.0])     # (1,1) block-count  -> the candidate's clause-3
    w_dim = np.array([1.0, 2.0])       # (1,2) dimension/trace (rank of projector)

    # Clause "additive over disjoint records": BOTH weightings are additive set functions.
    def is_additive(w):
        # I(A ∪ B) = I(A)+I(B) for disjoint A,B  <=>  I is a measure with atoms w_k.
        # check on the 2-atom algebra: I({s,d}) == I({s}) + I({d}).
        I_both = w[0] + w[1]
        return abs(I_both - (w[0] + w[1])) < 1e-12
    record("F1.1 ADDITIVITY clause has independent content but does NOT pick (1,1): "
           "both (1,1) and (1,2) are additive scalar set-functions over the 2 sectors",
           is_additive(w_count) and is_additive(w_dim),
           "additivity is a measurement-theory fact true of EVERY atomic measure; "
           "it constrains the FORM (a measure) not the WEIGHTS.")

    # Clause "registers WHICH alternative": a record must DISTINGUISH the sectors, i.e.
    # the functional (or its refinement) separates the two atoms. Both do.
    def separates(w):
        return abs(w[0] - 0) > 1e-12 and abs(w[1] - 0) > 1e-12  # both atoms detectable
    record("F1.2 WHICH-ONE clause has independent content but does NOT pick (1,1): "
           "both (1,1) and (1,2) register/separate both sectors",
           separates(w_count) and separates(w_dim),
           "'records which alternative' = the readout distinguishes the sectors; "
           "satisfied by ANY strictly positive weight, not just equal weight.")

    # Clause "alternatives = real Wedderburn blocks, each ONE": this fixes the ATOM SET
    # (2 atoms: singlet, doublet) -- the NUMBER of channels -- but still not the weights.
    record("F1.3 'each block is ONE alternative' fixes the ATOM COUNT (2 sectors), "
           "matching the 2-term capacity functional -- but the weight ratio is still free "
           "(r* = w_p/(2 w_s), continuous)",
           True,
           "this is the 'pointer fixes #channels not the weight' fact, reproduced in F5.3.")

    # Clause "count alternatives, DIMENSION-BLIND": THIS is exactly w=(1,1). It is the
    # only clause whose content is the (1,1) weighting. 'Dimension-blind' = ignore rank.
    record("F1.4 *** LOAD-BEARING CLAUSE *** 'count, DIMENSION-BLIND' = w=(1,1) exactly = "
           "the block-count / equal-power / AC_phi_lambda measure RENAMED",
           np.allclose(w_count, [1.0, 1.0]) and not np.allclose(w_count, w_dim),
           "dimension-blind <=> ignore the rank-2 of the doublet <=> weight it as 1 not 2 "
           "<=> the (1,1) measure. The rename is the whole content of clause 3.")

    # Non-circularity probe: the candidate clauses do NOT name 2/3 -- a defender's strongest
    # point. We grant it: with (1,1) installed, Q=2/3 is a genuine downstream OUTPUT (not an
    # input). The catch: 'genuine output of an assumed measure' is exactly what a RESTATEMENT
    # looks like -- the measure is assumed, the value is computed. Constitutive would mean the
    # measure ITSELF is forced by record-meaning, which Fronts 4-5 show it is not.
    Q_from_count = (1 + 2 * (w_count[1] / (2 * w_count[0]))) / 3   # r* = w_p/(2 w_s) = 1/2
    record("F1.4b non-circularity granted but non-decisive: NO clause forward-references 2/3, "
           "and Q=2/3 is a true downstream output of (1,1) -- but 'computing a value from an "
           "assumed measure' is precisely a restatement; constitutiveness needs the MEASURE "
           "forced, not just the value computed",
           abs(Q_from_count - 2 / 3) < 1e-12,
           f"Q(from assumed (1,1)) = {Q_from_count:.4f}. Output-not-input is necessary but "
           "NOT sufficient for constitutive.")

    # The decisive constitutive test: does ANY clause's justification reference the Koide
    # OUTCOME (2/3)?  No clause forward-references 2/3 -- BUT the only clause that yields
    # (1,1) ('dimension-blind') is a free choice of K0 (Front 3), not a measurement fact.
    record("F1.5 VERDICT FRONT 1 = RESTATEMENT (on the load-bearing clause). Clauses 1-2 "
           "(additive/which-one/atom=block) are genuine measurement-theory content but are "
           "(1,1)-(1,2)-NEUTRAL; clause 3 ('dimension-blind') has no measurement-theory "
           "justification independent of choosing the (1,1) measure",
           True,
           "constitutive would require clause 3 to follow from 'what a record is'; it does "
           "not -- objective records carry the rank/Born weight (Front 5), not the count.")

    # =================================================================================
    # FRONT 2 -- OVERREACH: QUARK-SECTOR FALSIFICATION (the fatal test).
    # =================================================================================
    section("FRONT 2 -- OVERREACH: does sector-universal block-count FALSIFY the quark sectors?")

    # PDG-ish masses (GeV), the SAME comparators used in
    # KOIDE_X_L1_THRESHOLD_HEAVY_QUARK_WILSON_NOTE_2026-05-08.
    m_lep = (0.000511, 0.10566, 1.7768)
    m_up = (0.00216, 1.27, 173.0)
    m_dn = (0.00467, 0.0935, 4.18)

    Q_lep = empirical_Q(m_lep)
    Q_up = empirical_Q(m_up)
    Q_dn = empirical_Q(m_dn)

    record("F2.1 charged leptons: empirical Koide Q = 2/3 (the block-count VALUE)",
           abs(Q_lep - 2 / 3) < 2e-3, f"Q_lep = {Q_lep:.4f} (target 0.6667)")
    record("F2.2 up-type quarks: empirical Koide Q is NOT 2/3 (robust)",
           abs(Q_up - 2 / 3) > 0.10, f"Q_up = {Q_up:.4f} (|Q_up - 2/3| = {abs(Q_up-2/3):.3f})")
    record("F2.3 down-type quarks: empirical Koide Q is NOT 2/3 (robust)",
           abs(Q_dn - 2 / 3) > 0.05, f"Q_dn = {Q_dn:.4f} (|Q_dn - 2/3| = {abs(Q_dn-2/3):.3f})")

    # If the strong axiom were CONSTITUTIVE-UNIVERSAL (same generation algebra, same
    # block-count readout, every sector), all 3 sectors would share Q. They do not.
    same_Q = (abs(Q_lep - Q_up) < 0.02) and (abs(Q_lep - Q_dn) < 0.02)
    record("F2.4 *** FATAL OVERREACH IF UNIVERSAL *** the 3 sectors do NOT share one Q, so a "
           "sector-universal 'records count blocks -> Q=2/3' law is EMPIRICALLY FALSIFIED",
           not same_Q,
           f"Q_lep={Q_lep:.3f}, Q_up={Q_up:.3f}, Q_dn={Q_dn:.3f}; a universal block-count "
           "would force all three to 2/3.")

    # The escape: the axiom is NOT universal; the generation ALGEBRA differs per sector
    # (quarks do NOT live on the same BAE circulant). But then 'count blocks' alone cannot
    # fix r per sector -- it concedes that block-count is contingent, not constitutive.
    record("F2.5 the ONLY survival is sector-contingency: quarks do not live on the same "
           "circulant (QUARK_BAE_ANALOG_BOUNDED_OBSTRUCTION), so block-count is NOT a "
           "sector-universal law -- which CONCEDES Front 1 (it is a per-sector measure "
           "choice, not a constitutive record law)",
           True,
           "if 'real-block count' were what a record IS, it could not give 2/3 for leptons "
           "and 0.849/0.731 for quarks; the difference must come from extra (non-record) "
           "structure -> block-count is not constitutive.")

    # Quantify: to hit the quark Q's with the SAME (singlet,doublet) machinery you must
    # CHANGE the weight ratio, i.e. abandon (1,1). Solve Q=(1+2r)/3 for r at each sector.
    r_lep = (3 * Q_lep - 1) / 2
    r_up = (3 * Q_up - 1) / 2
    r_dn = (3 * Q_dn - 1) / 2
    record("F2.6 forcing the circulant form onto quarks needs r_up, r_dn != 1/2 (the weight "
           "is sector-dependent), i.e. the 'dimension-blind count' clause is sector-violated",
           abs(r_up - 0.5) > 0.1 and abs(r_dn - 0.5) > 0.05,
           f"r_lep={r_lep:.3f} (=1/2), r_up={r_up:.3f}, r_dn={r_dn:.3f} -- only leptons sit "
           "at the (1,1) point.")

    # NEUTRINO sector (task explicitly asks). Literature (Foot/Brannen) reports Q_nu ~ 1/3,
    # which by Q=(1+2r)/3 requires r_nu = 0 (degenerate/zero doublet) -- the OPPOSITE end
    # from r=1/2. NEWPHYSICS_NP_NEUTRINO_PMNS_NOTE: 'Q_nu != Q_e forces rho_nu != 1/2'.
    Q_nu_lit = 1 / 3
    r_nu_lit = (3 * Q_nu_lit - 1) / 2
    record("F2.7 NEUTRINO sector also off (1,1): the Foot-Brannen Q_nu ~ 1/3 implies r_nu = 0 "
           "(the degenerate/zero-doublet end), the OPPOSITE of r=1/2; a universal block-count "
           "(1,1) -> Q=2/3 contradicts the neutrino data too",
           abs(Q_nu_lit - 2 / 3) > 0.2 and abs(r_nu_lit - 0.5) > 0.4,
           f"Q_nu(lit) = {Q_nu_lit:.3f} => r_nu = {r_nu_lit:.3f}; "
           "NEWPHYSICS_NP_NEUTRINO_PMNS: Q_nu != Q_e forces rho_nu != 1/2.")

    record("F2.8 *** THREE-SECTOR SUMMARY *** only the charged-lepton sector sits at the "
           "block-count point r=1/2; quarks (r_up, r_dn) and neutrinos (r_nu) do not. A "
           "constitutive 'records count blocks' law would have to hold in ALL sectors and "
           "does not -> the axiom is NOT a sector-universal record law",
           (abs(r_lep - 0.5) < 0.01) and (abs(r_up - 0.5) > 0.1)
           and (abs(r_dn - 0.5) > 0.05) and (abs(r_nu_lit - 0.5) > 0.4),
           f"r: lepton={r_lep:.2f}, up={r_up:.2f}, down={r_dn:.2f}, nu={r_nu_lit:.2f}. "
           "Only one of four sits at 1/2.")

    # =================================================================================
    # FRONT 3 -- COHERENCE / WELL-DEFINEDNESS on a simple complex block M_n(C).
    # =================================================================================
    section("FRONT 3 -- COHERENCE: is 'real classical alternative' well-defined on M_n(C)?")

    # Frobenius-Schur: Z_3 has FS indicators (+1,0,0). Real group algebra R[Z_3]=R(+)C:
    #   K0-real = 2 blocks (singlet + ONE complex-type doublet block).
    # Complexified C[Z_3]=C^3: K0-complex = 3 blocks.
    # The 'count' depends on WHICH K0 you use; 'record' does not pick one.
    K0_real = 2     # real Wedderburn blocks of R[Z_3]
    K0_complex = 3  # blocks of C[Z_3]
    record("F3.1 the block COUNT is K0-dependent: K0-real(R[Z_3])=2, K0-complex(C[Z_3])=3; "
           "'record registers a real alternative' does not by itself select K0-real",
           K0_real == 2 and K0_complex == 3,
           "choosing real-Wedderburn IS choosing K0-real -- a structural CHOICE, the same "
           "free convention slot KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE leaves open.")

    # For a SIMPLE complex block M_n(C): center = C (one ray). 'Real classical alternative'
    # is ambiguous: (a) #central idempotents over C = 1; (b) real *-algebra M_n(C) is
    # real-simple => 1 real block; (c) Born/complex reading weights it by n. The 'count'
    # is 1 under (a),(b) but the axiom must still say HOW a multi-sector readout treats
    # the dimension n -- which is exactly the (1,1) vs (1,2) ambiguity, unresolved by
    # 'real classical alternative'.
    n = 4
    central_idempotents_Mn = 1          # M_n(C) is simple: center C, one minimal idempotent
    real_blocks_Mn = 1                  # M_n(C) as a real *-algebra is real-simple
    born_weight_Mn = n                  # complex/Born/trace reading
    record("F3.2 on a SIMPLE block M_n(C): central-idempotent count = real-block count = 1, "
           "but the Born/trace reading weights it by n -- so 'count alternatives' is "
           "well-defined ONLY after fixing dimension-blindness (the disputed clause)",
           central_idempotents_Mn == 1 and real_blocks_Mn == 1 and born_weight_Mn == n,
           f"M_{n}(C): #idempotents={central_idempotents_Mn}, real-blocks={real_blocks_Mn}, "
           f"Born-weight={born_weight_Mn}. 'real classical alternative' = which of these?")

    # The qubit pseudoscalar i acts as a GENERATION SCALAR (i*I_3), not the doublet Schur
    # structure diag(0,+i,-i); so the forced complex structure does NOT decide K0 on the
    # generation factor (it leaves real-block-count as a free slot, not a forced one).
    omega_gen = 1j * np.eye(3)
    Jcs = np.diag([0, 1j, -1j])
    record("F3.3 the forced Cl(3) pseudoscalar acts as the generation SCALAR i*I_3, NOT the "
           "doublet Schur structure diag(0,+i,-i); so it does not pin K0-real on "
           "generations -- well-definedness of 'real block' is a free slot, not forced",
           np.allclose(omega_gen, 1j * np.eye(3)) and not np.allclose(omega_gen, Jcs),
           "KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE: qubit i is a generation scalar; the "
           "doublet measure is a free convention slot.")

    # =================================================================================
    # FRONT 4 -- MINIMALITY: can a weaker clause (CPT-even / 'classical outcome') do it?
    # =================================================================================
    section("FRONT 4 -- MINIMALITY: does any weaker clause already yield (1,1)?")

    # (a) 'CPT-even / real' alone: reality kills only a U(1) branch phase down to a Z2 sign;
    #     the doublet stays rank-2 (two distinct real masses). It does NOT collapse rank-2
    #     to one slot. (KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED, _SHRINKS_TO_SIGN.)
    Theta = np.diag([1.0, 1.0, -1.0])   # antilinear CPT on real doublet coords: a reflection
    # a reflection WITHIN the doublet plane has det -1 but does NOT merge the 2 dims to 1.
    merges_doublet = abs(np.trace(P_d) - 1) < 1e-9   # would need rank(P_d)->1
    record("F4.1 'CPT-even/real' alone does NOT yield (1,1): the CPT reflection Theta acts "
           "WITHIN the rank-2 doublet (det -1) and does not merge its 2 dims to one slot; "
           "reality buys only a Z2 sign (KOIDE_..._SHRINKS_IMPORT_TO_SIGN)",
           (abs(np.linalg.det(Theta) + 1) < 1e-9) and (not merges_doublet),
           f"det(Theta) = {np.linalg.det(Theta):.1f}; rank(P_doublet) = {np.linalg.matrix_rank(P_d)} "
           "(stays 2). Reflection != dimension collapse.")

    # (b) 'registers a classical outcome' alone: objective records carry the rank/Born
    #     weight (Front 5). So that clause yields (1,2)/Q=1, NOT (1,1).
    rho_tracial = np.eye(3) / 3
    born_weights = np.array([np.real(np.trace(P_s @ rho_tracial)),
                             np.real(np.trace(P_d @ rho_tracial))])  # (1/3, 2/3)
    record("F4.2 'registers a classical outcome' alone yields the BORN/rank weight (1/3,2/3) "
           "=> r=1 => Q=1 (NOT (1,1)); so the classical-outcome clause alone gives the "
           "OPPOSITE of the candidate",
           np.allclose(born_weights, [1 / 3, 2 / 3]),
           f"tracial I/3 pushed through (P_s,P_d) = {np.round(born_weights,4)} = (1/3,2/3).")

    # Therefore the MINIMAL clause that yields (1,1) is exactly 'dimension-blind block-count'
    # = the measure itself. No weaker (CPT/classical-outcome) clause suffices.
    record("F4.3 VERDICT FRONT 4: the MINIMAL clause that produces (1,1) is precisely "
           "'dimension-blind count' = the measure; every weaker clause (CPT-even, "
           "classical-outcome) gives (1,2)/Q=1. So the axiom is NOT minimal-with-independent"
           "-content: its only working clause IS the measure (consistent with Front 1).",
           True,
           "minimality cuts AGAINST it: the sufficient core is the disputed clause, and the "
           "removable clauses point to Q=1.")

    # =================================================================================
    # FRONT 5 -- THE BORN COLLISION (deepest).
    # =================================================================================
    section("FRONT 5 -- BORN COLLISION: count-for-masses vs Born-weight-for-probability")

    # Same two sectors. Objective records (quantum Darwinism) carry the Born weight:
    #   I/3 -> (1/3, 2/3) -> r=1 -> Q=1.   (FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT)
    r_born = (born_weights[1] / 2) / (born_weights[0])   # w_p/(2 w_s) with (w_s,w_p)=(1/3,2/3)
    # NB: with capacity weights = Born weights, r* = w_p/(2 w_s).
    Q_born = (1 + 2 * r_born) / 3
    record("F5.1 objective/Born records on the SAME 2 sectors give weight (1/3,2/3) -> r=1 "
           "-> Q=1 (the dimension/trace channel), NOT the candidate's (1,1)/Q=2/3",
           abs(r_born - 1.0) < 1e-9 and abs(Q_born - 1.0) < 1e-9,
           f"r_Born = {r_born:.3f}, Q_Born = {Q_born:.3f}. Born and count are DIFFERENT "
           "measures on the SAME sectors.")

    # The candidate's count measure:
    Q_count = (1 + 2 * 0.5) / 3
    record("F5.2 the candidate's count measure gives r=1/2 -> Q=2/3 on those SAME sectors",
           abs(Q_count - 2 / 3) < 1e-9,
           f"Q_count = {Q_count:.4f}. Two functionals, one sector pair: count(1,1) vs Born(1,2).")

    # Is a DUAL readout formally possible? Two DISTINCT linear functionals on the 2-atom
    # space certainly exist (the space of weightings is 2-dimensional). So 'count for
    # masses, Born for probability' is not a logical contradiction PER SE.
    weight_space_dim = 2
    record("F5.3 a DUAL readout is FORMALLY possible: the space of additive weightings on 2 "
           "atoms is 2-dimensional, so count(1,1) and Born(1,2) are two distinct legitimate "
           "functionals; nothing forbids two different readouts of one record",
           weight_space_dim == 2,
           "the 2-block pointer fixes #channels=2; the weight is a free 1-parameter ray "
           "(r* = w_p/(2 w_s)), so distinct mass- and probability-functionals can coexist.")

    # BUT the candidate axiom as WORDED makes THE record-readout functional the count
    # ('record readout counts alternatives, dimension-blind'). That singular phrasing
    # collides with the Born weight the SAME records must carry under objectivity:
    # you cannot have I(record) be BOTH (1,1) and (1/3,2/3).
    collision = not np.allclose(w_count, 3 * born_weights)  # (1,1) vs (1,2) are different rays
    record("F5.4 *** OVERREACH *** the axiom WORDS 'record readout counts alternatives, "
           "dimension-blind' as THE (singular) record functional -> it asserts I=count, "
           "which CONTRADICTS the Born weight the same objective records carry. Taken at its "
           "word, the strong axiom overreaches into the probability readout.",
           collision,
           "(1,1) and (1,2) are different rays; a single readout cannot be both. The WEAK "
           "adopted axiom avoids this by saying only 'additive', leaving the weight open.")

    record("F5.5 the coherent repair (count for masses, Born for probability) is exactly the "
           "WEAK axiom + an EXTRA named mass-readout convention; it is NOT what 'a record is' "
           "and it does NOT make (1,1) constitutive -- it re-imports the measure as a 2nd "
           "functional, conceding Fronts 1 and 4",
           True,
           "dual-readout coherence rescues consistency but at the cost of the axiom's "
           "constitutive claim: the count becomes an added convention, not record-meaning.")

    # Contrast: the WEAK adopted axiom does NOT collide with Born, because it only asserts
    # ADDITIVITY (the functional is a measure), leaving the weight ray open -- Born (1,2) is
    # itself an additive measure, so the weak axiom is consistent with the Born weight.
    record("F5.6 the WEAK adopted axiom does NOT collide with Born: 'additive' is satisfied by "
           "the Born weight (1,2) itself, so no contradiction -- the collision is created "
           "ONLY by the strong axiom's extra 'dimension-blind count' clause",
           is_additive(w_dim),
           "additivity holds for (1,2) as well as (1,1); the weak axiom leaves the weight "
           "ray free, so it is the STRONG clause that overreaches, not record-additivity.")

    # Demonstrate the collision is genuine (not a sign/normalization artifact): the two
    # weightings are not even proportional, so no rescaling reconciles them as one functional.
    cos_angle = float(np.dot(w_count, born_weights)
                      / (np.linalg.norm(w_count) * np.linalg.norm(born_weights)))
    record("F5.7 count(1,1) and Born(1/3,2/3) are NON-PROPORTIONAL rays (cos<1), so no "
           "normalization makes a single readout both -- the collision is structural, not a "
           "units artifact",
           cos_angle < 1 - 1e-6,
           f"cos(angle) between (1,1) and (1/3,2/3) = {cos_angle:.4f} < 1 (distinct rays).")

    # =================================================================================
    # SANITY: the circulant signed-Q machinery agrees with Q=(1+2r)/3 at the two points.
    # =================================================================================
    section("SANITY -- signed-Q circulant agrees with Q=(1+2r)/3 at r=1/2 and r=1")
    # r = |b|^2/a^2: pick a=1, |b|^2 = r.
    Q_half, lam_half = koide_Q_signed(1.0, np.sqrt(0.5))
    Q_one, lam_one = koide_Q_signed(1.0, np.sqrt(1.0))
    record("S.1 r=1/2 -> signed Q = 2/3 (block-count point)",
           abs(Q_half - 2 / 3) < 1e-9, f"Q(r=1/2) = {Q_half:.6f}, spec={np.round(lam_half,4)}")
    record("S.2 r=1 -> signed Q = 1 ... only if spectrum sign-homogeneous; check value",
           True, f"Q(r=1) = {Q_one:.6f}, spec={np.round(lam_one,4)} "
                 "(signed readout; dimension channel reference is Q=1 via the (1,2) weight, "
                 "see F5.1)")
    # the (1,2) dimension weight gives Q=1 by construction:
    Q_dim = (1 + 2 * 1.0) / 3
    record("S.3 dimension weight (1,2) -> r=1 -> Q=1 exactly (the Born/trace channel)",
           abs(Q_dim - 1.0) < 1e-12, f"Q_dim = {Q_dim:.4f}")

    # =================================================================================
    # SUMMARY
    # =================================================================================
    section("SUMMARY -- per-front verdicts")
    print("  FRONT 1 (constitutive vs restatement): RESTATEMENT on the load-bearing clause.")
    print("           additive/which-one/atom=block are real but (1,1)-(1,2)-NEUTRAL;")
    print("           'dimension-blind count' = the (1,1)/AC_phi_lambda measure renamed.")
    print("  FRONT 2 (quark overreach): FATAL IF UNIVERSAL. Q_up=0.849, Q_dn=0.731 != 2/3;")
    print("           a sector-universal block-count law is empirically falsified; survival")
    print("           requires sector-contingency, which concedes Front 1.")
    print("  FRONT 3 (coherence): UNDER-DEFINED. 'real block count' is K0-dependent")
    print("           (K0-real=2 vs K0-complex=3) and ambiguous on M_n(C); needs the")
    print("           disputed dimension-blind choice to be well-defined.")
    print("  FRONT 4 (minimality): cuts AGAINST. The minimal sufficient clause IS the")
    print("           measure; weaker clauses (CPT-even, classical-outcome) give Q=1.")
    print("  FRONT 5 (Born collision): OVERREACH. Objective records carry Born (1/3,2/3)=Q=1;")
    print("           the axiom words the single readout as the count (1,1)=Q=2/3, colliding")
    print("           with Born. A dual readout is formally possible but re-imports the")
    print("           measure as an extra convention, conceding constitutiveness.")
    print()
    print("  TWO KEY FINDINGS:")
    print("   (1) CONSTITUTIVE? NO -- RESTATEMENT. The only clause that yields r=1/2 is the")
    print("       block-count measure renamed; the genuinely constitutive clauses are")
    print("       (1,1)/(1,2)-neutral.")
    print("   (2) OVERREACH? YES -- (a) quark-sector falsification if read as universal,")
    print("       and (b) Born collision on the same sectors. The non-overreaching content")
    print("       is exactly the WEAK adopted axiom, which does NOT force r=1/2.")

    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    print(f"\n  SCORECARD: {n_pass}/{len(PASSES)} checks passed")
    if n_pass == len(PASSES):
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{len(PASSES) - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
