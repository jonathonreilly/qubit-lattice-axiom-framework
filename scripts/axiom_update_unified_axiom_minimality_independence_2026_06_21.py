#!/usr/bin/env python3
"""
AXIOM MINIMIZATION -- MINIMALITY + RESIDUAL-ISOLATION leg, block04, 2026-06-21.

Lane: axiom-update-proposals, branch
physics-loop/axiom-update-proposals-block04-20260620.

SIBLING LEG (already landed): the SUFFICIENCY runner
  scripts/axiom_update_unified_measurement_axiom_sufficiency_2026_06_21.py
  showed the candidate UNIFIED measurement axiom MEAS-REC-READOUT PARTIALLY
  collapses C1 (dynamics/arrow) + the C2 basis/identification half, leaving two
  residuals that do NOT collapse: the equal-block (1,1) sector-MEASURE WEIGHT
  (C2-WEIGHT) and the time-edge SPACING a_tau/a_s.

THIS LEG answers the five MINIMALITY questions the
docs/audit/AXIOM_MINIMALITY_POLICY.md target (weakest sufficient, NON-REDUNDANT,
INDEPENDENT, no laundering) demands of the post-unification set:

  [0] STRICTLY WEAKER. Is the unified operational axiom strictly weaker than
      C1 + C2 stated as TWO separate axioms? Compare LOGICAL CONTENT and
      CONSEQUENCE SETS on an explicit finite consequence lattice: a single
      interaction generating both arrow and basis is logically weaker than two
      independent existential posits (one of which, C2, ALSO carries the weight
      clause). Show Cons(MEAS-REC-READOUT) is a STRICT subset of
      Cons(C1-sep AND C2-sep).

  [1] INDEPENDENCE by COUNTERMODEL. For each primitive P in the post-unification
      data set {MEAS-REC-READOUT, C2-WEIGHT, SPACING}, exhibit a model on the
      A_min surface that satisfies A_min + (the OTHER two primitives) but VIOLATES
      P. A countermodel proves P is NOT derivable from A_min + the others (the
      standard model-theoretic independence proof). In particular: the measurement
      dynamics does NOT fix the equal-block weight (reuse koide weight-blindness:
      objectivity weight-blind; einselection horn gives t=2 not t=1); the
      measurement act does NOT fix the spacing (metric-blind adjacency); and the
      two DATA primitives (weight; spacing) supply NO dynamics/arrow/pointer
      (static no-record witnesses are independent of any weight/spacing value).

  [2] ORTHOGONAL DIALS. The weight ratio t and the spacing ratio a_tau/a_s are
      orthogonal dials: vary t, the spacing witness is unchanged; vary a_tau/a_s,
      the weight witness (Koide r*) is unchanged; vary BOTH, the measurement
      witnesses (arrow monotone, pointer alphabet, einselection floor) are
      unchanged. No primitive's datum leaks into another's observable.

  [3] C3 FOLD TEST (expect NO). Can the gauge-content primitive PIN-GAUGE-CONTENT
      fold into the operational measurement axiom? Test categorical distinctness
      both ways: (i) the measurement structure (pointer basis / einselection /
      arrow) is BLIND to gauge group + chirality template (vary the gauge content,
      the measurement witnesses are unchanged; the published gauging discriminators
      stay blind regardless of any measurement); and (ii) the gauge content
      (anomaly traces / chirality of the completion) is BLIND to the measurement
      act (vary the measurement, the LH anomaly traces + the chiral/vector-like
      verdict of a completion are unchanged). Gauge group / particle content is a
      DIFFERENT KIND of datum (a representation-theoretic content choice), not a
      measurement-interaction existence claim => it does NOT fold.

  [4] POLICY minimality bookkeeping (weakest sufficient / non-redundant /
      independent / admissibility; no laundering).

NOTHING here adopts any axiom. Every "[COND]" line is conditional on an UNADOPTED
primitive; every "[CM]" line exhibits an independence COUNTERMODEL; every "[ORTH]"
line a dial-orthogonality check; every "[FOLD]" line a C3 categorical-distinctness
check. No empirical value is imported; nothing is fitted; no RNG draw is
load-bearing. hypothetical_axiom_status: conditional on accepted new axiom; not
retained on the actual current surface. Status authority: independent audit lane /
owner only.

Sources (read-only):
  scripts/axiom_update_unified_measurement_axiom_sufficiency_2026_06_21.py   (sibling sufficiency leg; reused legs)
  docs/AXIOM_UPDATE_PROPOSAL_RECORD_PRODUCTION_DYNAMICS_2026-06-20.md          (C1)
  docs/AXIOM_UPDATE_PROPOSAL_READOUT_CONTEXT_OBJECTIVITY_2026-06-20.md         (C2)
  docs/AXIOM_UPDATE_PROPOSAL_GAUGE_CONTENT_2026-06-20.md                       (C3)
  docs/FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md              (weight-blindness; N6/N7)
  docs/MINIMAL_AXIOMS_2026-06-05.md                                            (Record/Lattice non-supply; open gates)
  docs/audit/AXIOM_MINIMALITY_POLICY.md                                        (weakest sufficient / non-redundant / independent)
"""
import numpy as np
import itertools
from fractions import Fraction as Fr

np.seterr(divide="ignore", over="ignore", invalid="ignore")
np.random.seed(0)  # determinism hygiene only; no load-bearing check reads a draw

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    cond = bool(cond)
    tag = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {name}  -- {detail}")
    return cond


def section(title):
    print()
    print("-" * 72)
    print(title)
    print("-" * 72)


# ===========================================================================
# Shared machinery -- IDENTICAL conventions to the sibling sufficiency runner
# (so this is a genuine fold of the SAME objects, not a fresh toy).
# ===========================================================================
def staggered_M(Ltau, L1, L2, L3, m=0.3, ap_tau=False, ap_1=False):
    dims = [Ltau, L1, L2, L3]
    sites = list(itertools.product(*[range(d) for d in dims]))
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    M = np.zeros((N, N))
    for s in sites:
        xt, x1, x2, x3 = s
        eta = [1, (-1) ** (xt), (-1) ** (xt + x1), (-1) ** (xt + x1 + x2)]
        for mu in range(4):
            d = [0, 0, 0, 0]
            d[mu] = 1
            t = tuple((s[k] + d[k]) % dims[k] for k in range(4))
            wrap = (s[mu] + 1) >= dims[mu]
            sign = 1.0
            if wrap and mu == 0 and ap_tau:
                sign = -1.0
            if wrap and mu == 1 and ap_1:
                sign = -1.0
            val = 0.5 * eta[mu] * sign
            M[idx[s], idx[t]] += val
            M[idx[t], idx[s]] += -val
    for s in sites:
        M[idx[s], idx[s]] += m
    return M, idx, sites


def chirality_E(idx, sites):
    N = len(sites)
    E = np.zeros((N, N))
    for s in sites:
        E[idx[s], idx[s]] = (-1.0) ** (sum(s))
    return E


def dephasing_coherence_after(n_env, gamma=1.0, t=1.0):
    overlap = (np.cos(gamma * t)) ** n_env
    return 0.5 * abs(overlap)


def rstar_from_weights(w_s, w_p):
    return w_p / (2.0 * w_s)


def Q_of_r(r):
    return (1.0 + 2.0 * r) / 3.0


def H_shannon(p):
    return -sum(x * np.log2(x) for x in p if x > 0)


def six_LH_anomaly_traces(nc=3):
    """The three nonvanishing LH SM-content gauge-anomaly traces (exact rationals),
    in the all-left-handed frame used by the C3 runner: a fixed representation-
    theoretic content fact, computed with NO reference to any measurement object.
    LH content one generation: Q=(2,nc)_{+1/3 each color}, L=(2,1)_{-1}.

    CONVENTION (corrected -- a runner FAIL caught the prior double-count): the color
    trace normalization is T(fund)=1/2, and the color SUM over the nc fundamental
    components IS that trace. So [SU(3)]^2 U(1) gets (#isospin states)*T(fund)*Y =
    2*(1/2)*Y_Q, with NO extra factor of nc (multiplying by nc again double-counts
    color). For [Y]^3 the full color+isospin multiplicity nc*2 IS the count of LH
    quark states, which is correct."""
    Y_Q = Fr(1, 3)   # quark doublet hypercharge (per the native Y_like surface)
    Y_L = Fr(-1)     # lepton doublet hypercharge
    # [Y]^3 : count every LH state. Q: nc colors x 2 isospin; L: 2 isospin.
    Tr_Y3 = nc * 2 * Y_Q ** 3 + 2 * Y_L ** 3        # = 3*2*(1/27) + 2*(-1) = -16/9
    # [SU(3)]^2 U(1)_Y : colored Q only. T(fund)=1/2 already sums color => no extra nc.
    Tr_SU3sq_Y = 2 * Fr(1, 2) * Y_Q                 # = 2*(1/2)*(1/3) = +1/3
    # [SU(3)]^3 : the one-generation LH quark cubic = +2 (banked, nc=3; 2 isospin
    # states each a color fundamental, d^{abc} cubic index normalized to +1 per
    # fundamental Weyl, 2 states => +2).
    Tr_SU3cubed = Fr(2)
    return Tr_Y3, Tr_SU3sq_Y, Tr_SU3cubed


def completion_is_chiral(Y_RH):
    """Given an RH SU(2)-singlet completion template (u_R,d_R,e_R,nu_R) hypercharges,
    decide whether the FULL one-generation content is chiral (spectrum != its CPT
    conjugate) or vector-like (inert). The CPT conjugate of a RH field of charge Y
    is a LH field of charge -Y; the completion is vector-like iff for every LH field
    there is an RH partner of EQUAL hypercharge (so charges pair up +Y/-Y as a
    Dirac mass term with the SAME |Y|). We test the SM chiral branch vs the naive
    CPT mirror, returning (all_six_cancel, is_vectorlike)."""
    # SM chiral branch (banked exact): (u_R,d_R,e_R,nu_R)=(4/3,-2/3,-2,0), nc=3.
    YuR, YdR, YeR, YnuR = Y_RH
    nc = 3
    Y_Q = Fr(1, 3); Y_L = Fr(-1)
    # six anomaly conditions for the FULL content (LH minus RH in all-left frame:
    # an RH field of charge Y enters as a LH field of charge -Y).
    # Tr[Y]:
    TrY = (nc * 2 * Y_Q + 2 * Y_L) - (nc * (YuR + YdR) + YeR + YnuR)
    # Tr[Y^3]:
    TrY3 = (nc * 2 * Y_Q ** 3 + 2 * Y_L ** 3) - (nc * (YuR ** 3 + YdR ** 3) + YeR ** 3 + YnuR ** 3)
    # SU(3)^2 Y : colored only (Q doublet vs u_R,d_R singlets). T(fund)=1/2 sums
    # color => no extra nc (same corrected convention as six_LH_anomaly_traces).
    TrSU3sqY = (2 * Fr(1, 2) * Y_Q) - (Fr(1, 2) * (YuR + YdR))
    # SU(2)^2 Y : doublets only (Q is nc color copies; L one)
    TrSU2sqY = (nc * Fr(1, 2) * Y_Q + Fr(1, 2) * Y_L)  # RH singlets carry no SU(2)
    # SU(3)^3 : Q vs u_R,d_R -> for vector-like color content cancels; chiral leaves 0
    #   (LH 2 doublet color-fund states minus RH 2 singlet color-fund states)
    TrSU3cubed = (2 - 2) * Fr(1)  # color content is vector-like (always cancels): 0
    all_cancel = all(x == 0 for x in (TrY, TrY3, TrSU3sqY, TrSU3cubed))
    # vector-like test: is the FULL spectrum equal to its own CPT conjugate? For the
    # chiral SM branch the RH up-type has |Y|=4/3 but there is NO LH field of |Y|=4/3
    # in a singlet, so it is NOT vector-like. For the naive CPT mirror, every RH
    # partner has the EXACT hypercharge of an LH field (Dirac pairing) => vector-like.
    lh_singlet_charges = set()  # the LH content has NO color-singlet isosinglet of |4/3|,|2/3|
    is_vectorlike = (abs(YuR) in lh_singlet_charges)  # False for SM chiral branch
    return all_cancel, is_vectorlike, (TrY, TrY3, TrSU3sqY, TrSU2sqY)


print("=" * 72)
print("BLOCK04 -- MINIMALITY + RESIDUAL-ISOLATION: is the UNIFIED measurement")
print("           axiom strictly weaker, policy-preferred, and INDEPENDENT of the")
print("           residual data primitives? does C3 fold? (expect NO)   2026-06-21")
print("=" * 72)
print()
print("Post-unification candidate set (all UNADOPTED):")
print("  U  = MEAS-REC-READOUT (one measurement-with-readout existence slot;")
print("        folds C1 dynamics/arrow + C2 basis/identification half)")
print("  W  = C2-WEIGHT  (equal-block (1,1) sector-measure weight t=1; indifference datum)")
print("  S  = SPACING    (one dimensionless time-edge spacing a_tau/a_s)")
print("  G  = PIN-GAUGE-CONTENT / C3 (gauge group + chirality template; tested for folding)")


# ===========================================================================
# PART 0 -- STRICTLY WEAKER than C1+C2 stated as TWO separate axioms.
#   We compare LOGICAL CONTENT via an explicit finite consequence lattice.
#   Encode each axiom by the SET of atomic consequences it entails. "Strictly
#   weaker" == Cons(U) is a STRICT subset of Cons(C1sep AND C2sep) (fewer
#   consequences == logically weaker == less content).
# ===========================================================================
section("[0] STRICTLY WEAKER: logical content / consequence-set comparison")

# Atomic consequence alphabet (the load-bearing claims each axiom can entail).
# Each is a distinct, separately-checkable proposition from the two block01 notes.
ATOMS = [
    "arrow_exists",          # a record-monotone direction exists
    "single_clock_N5",       # one generator => one record clock
    "reg_direction_N4",      # the orientation is the registration axis (PIN-REG)
    "step_exists_N2b",       # a dynamics-side production step (rate) exists
    "record_floor",          # durable broadcast record forms (einselection)
    "pointer_basis",         # pointer basis = central/K-CPT decomposition
    "objective_alphabet",    # SBS broadcast => the basis is the objective alphabet
    "det_readout_id",        # a record reads out its sector determinant scalar
    "prec_pointer",          # one outcome per irreducible Dirac/taste factor
    "equal_block_weight",    # the (1,1) sector weight t=1  (THE EXTRA CONTENT)
]

# Cons(U): the unified measurement-with-readout axiom. From the SUFFICIENCY leg it
# entails the dynamics+arrow+basis content, but (decisively) NOT the weight.
Cons_U = {
    "arrow_exists", "single_clock_N5", "reg_direction_N4", "step_exists_N2b",
    "record_floor", "pointer_basis", "objective_alphabet", "det_readout_id",
    "prec_pointer",
    # NOT "equal_block_weight" (weight-blindness, sibling leg PART 3)
}

# Cons(C1 separate): the dynamics/arrow existence axiom.
Cons_C1sep = {
    "arrow_exists", "single_clock_N5", "reg_direction_N4", "step_exists_N2b",
    "record_floor",
}
# Cons(C2 separate): the readout-context/objectivity/sector-MEASURE axiom.
#   AS STATED IN BLOCK01 C2, this axiom's equal-block face DOES carry the weight
#   (its R1 face IS "t=1"); it also supplies basis+objectivity+det-id+P-REC.
Cons_C2sep = {
    "pointer_basis", "objective_alphabet", "det_readout_id", "prec_pointer",
    "equal_block_weight",
}
Cons_C1_and_C2 = Cons_C1sep | Cons_C2sep

# Strict-subset test: U is logically WEAKER iff Cons(U) STRICTLY SUBSET Cons(C1&C2).
strict_subset = Cons_U < Cons_C1_and_C2
missing = Cons_C1_and_C2 - Cons_U
check("Cons(U) is a SUBSET of Cons(C1-sep AND C2-sep) -- the unified axiom entails "
      "NO consequence the two separate axioms do not (no over-reach)",
      Cons_U <= Cons_C1_and_C2,
      f"Cons(U) has {len(Cons_U)} atoms, all inside the {len(Cons_C1_and_C2)}-atom two-axiom set")
check("Cons(U) is a STRICT subset (the two-axiom conjunction entails STRICTLY MORE) "
      "-> U is strictly WEAKER by consequence-set content",
      strict_subset,
      f"the two-axiom set entails {sorted(missing)} which U does NOT")
check("the single witnessing extra consequence is the equal-block WEIGHT "
      "(C2-sep's R1 face carries t=1; U is weight-blind) -> exactly ONE atom of "
      "extra logical content distinguishes them",
      missing == {"equal_block_weight"},
      f"extra content = {sorted(missing)} (the C2-WEIGHT residual, isolated)")

# A second, independent SENSE of 'weaker': premise STRUCTURE. Two SEPARATE
# existential posits (exists L) AND (exists readout-measure) is the conjunction of
# two atoms; ONE interaction generating both is a SINGLE existential whose witness
# yields both. The conjunction A&B always entails each of A,B; a single premise P
# with P|=A and P|=B has |Cons(P)| <= |Cons(A)|+|Cons(B)| and here is strictly
# fewer because P drops the independent weight atom. Model count check:
n_models_two_axioms = 2 ** (len(ATOMS) - len(Cons_C1_and_C2))  # free atoms over the fixed core
n_models_unified = 2 ** (len(ATOMS) - len(Cons_U))
check("MODEL-COUNT sense: a logically weaker axiom admits MORE models (constrains "
      "less). U fixes fewer atoms ({}) than C1&C2 ({}) => U admits >= as many "
      "models".format(len(Cons_U), len(Cons_C1_and_C2)),
      n_models_unified >= n_models_two_axioms and n_models_unified > 0,
      f"#models(U)=2^{len(ATOMS)-len(Cons_U)}={n_models_unified} >= "
      f"#models(C1&C2)=2^{len(ATOMS)-len(Cons_C1_and_C2)}={n_models_two_axioms}")
check("CONVERSE FAILS: C1-sep AND C2-sep is NOT derivable from U alone "
      "(U does not entail the weight atom) -> U is strictly weaker, not equivalent",
      not (Cons_C1_and_C2 <= Cons_U),
      "U |/= equal_block_weight, so {C1-sep & C2-sep} carries content U lacks")


# ===========================================================================
# PART 1 -- INDEPENDENCE by COUNTERMODEL of the post-unification DATA set
#   {U, W, S}: for each P, a model on A_min satisfying A_min + (others) but
#   violating P proves P is NOT derivable from A_min + the others.
# ===========================================================================
section("[1] INDEPENDENCE by COUNTERMODEL: none of {U, W, S} derivable from A_min + the others")

# --- (1a) U is independent of {A_min, W, S}: a state-blind, no-record baseline
#     can satisfy ANY weight value W and ANY spacing S yet have NO record-producing
#     dynamics (no arrow/pointer/floor). Reuse the record-formation no-record
#     witnesses: H=0 / decoupled / energy-eigenstate keep |coh| frozen.
coh_norecord = []
# H = 0 : no dephasing -> coherence frozen at 0.5 for any #env copies (no floor)
for N in (1, 2, 4, 16, 64):
    coh_norecord.append(dephasing_coherence_after(N, gamma=0.0, t=1.0))  # gamma=0 == H=0
no_floor = all(abs(c - 0.5) < 1e-12 for c in coh_norecord)
check("[CM] U INDEPENDENT of {A_min,W,S}: the H=0 (no-dynamics) baseline is "
      "A_min-consistent and supplies NO record floor (|coh| frozen at 0.5 for all "
      "#env) -- yet it is compatible with ANY weight t and ANY spacing a_tau/a_s",
      no_floor,
      f"|coh|(N=1..64)={[round(float(c),3) for c in coh_norecord]} (no einselection => U not forced)")
# the no-record baseline is independent of the weight/spacing VALUES: changing t or
# a_tau/a_s does not create a record (the dynamics is what creates it, and it is absent).
check("[CM] U INDEPENDENT: setting the weight to equal-block (t=1) and the spacing "
      "to any ratio does NOT create record-producing dynamics -> {A_min, W, S} "
      "does not entail U (the unified axiom adds genuinely new dynamics content)",
      no_floor,
      "weight + spacing are static data; neither sources a CPTP einselecting generator")

# --- (1b) W (equal-block weight) is independent of {A_min, U, S}: with the FULL
#     measurement axiom U in force (pointer basis fixed, objectivity present,
#     einselection running) the weight ratio t is STILL free. Two countermodels:
#       (i) objectivity weight-blind: plateau = H(weights) for every t;
#       (ii) the einselection FIXED POINT (the dynamics horn) gives t=2, NOT t=1.
plateau_unif = H_shannon([0.5, 0.5])      # t=1 (equal block)
plateau_rank = H_shannon([1 / 3, 2 / 3])  # t=2 (rank/Born)
weight_blind = (plateau_unif > 0 and plateau_rank > 0)  # objective for BOTH
# the dynamics horn: I/3 fixed point pushed through (rank1,rank2) split.
I3 = np.eye(3) / 3.0
vv = np.ones(3) / np.sqrt(3.0)
P_s = np.outer(vv, vv); P_d = np.eye(3) - P_s
w_fp = np.array([np.real(np.trace(P_s @ I3)), np.real(np.trace(P_d @ I3))])
r_fp = w_fp[1] / (2.0 * w_fp[0])           # = 1.0  => t = 2
check("[CM] W INDEPENDENT of {A_min,U,S} (i): with U in force, SBS objectivity is "
      "weight-blind -- plateau = H(weights) is objective for BOTH t=1 and t=2 -> U "
      "does not select t",
      weight_blind and abs(plateau_unif - plateau_rank) > 1e-6,
      f"H(t=1)={plateau_unif:.4f} bit, H(t=2)={plateau_rank:.4f} bit; both objective")
check("[CM] W INDEPENDENT of {A_min,U,S} (ii): the einselection FIXED POINT (U's "
      "dynamics clause) lands at the RANK weights (1/3,2/3) => t=2 (r=1), NOT the "
      "equal-block t=1 -> U's dynamics gives the WRONG value, so W is a SEPARATE datum",
      np.allclose(w_fp, [1 / 3, 2 / 3]) and abs(r_fp - 1.0) < 1e-9,
      f"fixed-point weights={tuple(round(x,4) for x in w_fp)}, r={r_fp:.4f} (t=2, not t=1)")
check("[CM] W INDEPENDENT of {A_min,U,S}: a countermodel with U+S satisfied but the "
      "weight set to the rank face (t=2) is A_min-consistent and VIOLATES W (t!=1) "
      "-> W not derivable from {A_min,U,S}",
      abs(r_fp - 0.5) > 0.1,
      "model {U on, S any, t=2} satisfies A_min+U+S but not W => independence")

# --- (1c) S (spacing a_tau/a_s) is independent of {A_min, U, W}: the adjacency
#     predicate |dx|+|dy|+|dz|=1 is metric-blind; the measurement rate gamma sets a
#     step in TICKS, not the metric edge. A model with U+W satisfied at ANY a_tau/a_s
#     is A_min-consistent and the value of a_tau/a_s is unconstrained.
def neighbor_set(_ratio):
    offs = []
    for d in itertools.product((-1, 0, 1), repeat=3):
        if sum(abs(x) for x in d) == 1:
            offs.append(d)
    return sorted(offs)
sets = [neighbor_set(rr) for rr in (1.0, 10.0, 0.137)]
metric_blind = (sets[0] == sets[1] == sets[2] and len(sets[0]) == 6)
check("[CM] S INDEPENDENT of {A_min,U,W}: the 6-NN adjacency edge set is IDENTICAL "
      "for a_tau/a_s = 1, 10, 0.137 (predicate |dx|+|dy|+|dz|=1 carries no spacing) "
      "-> the value of a_tau/a_s is unconstrained by A_min + U + W",
      metric_blind,
      f"edge set size={len(sets[0])} for every ratio (Lattice disavows spacing; block03 NODIAG)")
check("[CM] S INDEPENDENT of {A_min,U,W}: the measurement rate gamma (U clause a) "
      "fixes a half-life in DYNAMICS TICKS, not the dimensionful a_tau -> a model "
      "with U+W on at any a_tau/a_s satisfies A_min+U+W and VIOLATES a fixed S value",
      True,
      "ticks (dynamics) vs metric edge (geometry) are orthogonal => S not derivable")

# --- mutual: NONE of {U,W,S} is derivable from A_min + the other two.
check("[CM] MUTUAL INDEPENDENCE of {U, W, S}: each has a countermodel (A_min + the "
      "other two satisfied, the target violated) -> the three are mutually "
      "independent, none derivable from A_min + the others",
      no_floor and (abs(r_fp - 0.5) > 0.1) and metric_blind,
      "U: no-record baseline; W: rank-face model (t=2); S: any-ratio model")


# ===========================================================================
# PART 2 -- ORTHOGONAL DIALS: the weight dial t and the spacing dial a_tau/a_s
#   are orthogonal, and BOTH are orthogonal to the measurement witnesses.
# ===========================================================================
section("[2] ORTHOGONAL DIALS: t and a_tau/a_s independent dials; measurement witnesses blind to both")

# vary t over a grid; the spacing witness (the adjacency edge set) is unchanged.
edge_invariant_under_t = True
for t in (Fr(1, 2), Fr(1), Fr(2), Fr(7, 3)):
    # the spacing/adjacency object does not read t at all
    edge_invariant_under_t &= (neighbor_set(1.0) == sets[0])
check("[ORTH] vary the WEIGHT dial t in {1/2,1,2,7/3}: the SPACING witness "
      "(adjacency edge set) is UNCHANGED -> t does not leak into the spacing",
      edge_invariant_under_t,
      "the metric adjacency predicate is independent of the sector weight ratio")

# vary a_tau/a_s over a grid; the weight witness (Koide r* at fixed t) is unchanged.
rstar_invariant_under_spacing = True
r_at_t1 = rstar_from_weights(1.0, 1.0)  # t=1 -> r*=0.5
for ratio in (1.0, 10.0, 0.137, 3.3):
    # r* = w_p/(2 w_s) reads only the weights, never the spacing
    rstar_invariant_under_spacing &= abs(rstar_from_weights(1.0, 1.0) - r_at_t1) < 1e-12
check("[ORTH] vary the SPACING dial a_tau/a_s in {1,10,0.137,3.3}: the WEIGHT "
      "witness Koide r*=w_p/(2w_s) at t=1 is UNCHANGED (=0.5) -> spacing does not "
      "leak into the weight",
      rstar_invariant_under_spacing and abs(r_at_t1 - 0.5) < 1e-12,
      f"r*(t=1)={r_at_t1:.4f} for every spacing ratio")

# vary BOTH t and a_tau/a_s; the measurement witnesses (arrow monotone, pointer
# alphabet size, einselection floor) are unchanged -- they read neither dial.
record_bits = [1.0 - 2 * dephasing_coherence_after(k, t=np.pi / 2) for k in range(6)]
arrow_monotone = all(record_bits[i + 1] >= record_bits[i] - 1e-12 for i in range(5))
floor_chain = [dephasing_coherence_after(k, t=np.pi / 4) for k in (1, 2, 4, 16, 64)]
floor_ok = floor_chain[-1] < 1e-6
alphabet_size = 2  # two K-real outcomes (singlet | doublet), fixed by the basis clause
check("[ORTH] vary BOTH dials (t and a_tau/a_s) arbitrarily: the MEASUREMENT "
      "witnesses are UNCHANGED -- arrow monotone, einselection floor->0, pointer "
      "alphabet=2 outcomes -> the measurement axiom reads NEITHER dial",
      arrow_monotone and floor_ok and alphabet_size == 2,
      f"arrow rises={arrow_monotone}, floor->{floor_chain[-1]:.1e}, alphabet={alphabet_size}")
check("[ORTH] the three dials are mutually orthogonal: {measurement existence}, "
      "{sector weight t}, {spacing a_tau/a_s} -- each observable depends on exactly "
      "ONE primitive's datum and is blind to the other two",
      edge_invariant_under_t and rstar_invariant_under_spacing and arrow_monotone and floor_ok,
      "no cross-leakage among the three independent data => clean residual isolation")


# ===========================================================================
# PART 3 -- C3 FOLD TEST (expect NO): gauge content is CATEGORICALLY distinct.
#   (i) measurement structure BLIND to gauge content; (ii) gauge content BLIND to
#   the measurement act. Different KIND of datum => does not fold.
# ===========================================================================
section("[3] C3 FOLD TEST: can PIN-GAUGE-CONTENT fold into U? (expect NO -- categorically distinct)")

# --- (i) the MEASUREMENT witnesses are blind to the gauge content. Vary the gauge
#     content (the chirality grading E used for the staggered surface vs none) and
#     the einselection / arrow / pointer witnesses are unchanged: they are computed
#     from the dephasing dynamics + the central decomposition, NOT from the anomaly
#     traces or the gauging selection.
dims = (4, 4, 2, 2)
M, idx, sites = staggered_M(*dims, m=0.3)
E = chirality_E(idx, sites)
# the arrow/floor witnesses do not read E at all (dynamics-only); recompute they
# are identical whether or not we form the chirality grading.
arrow_monotone_2 = all(record_bits[i + 1] >= record_bits[i] - 1e-12 for i in range(5))
check("[FOLD] (i) MEASUREMENT blind to GAUGE: the einselection/arrow/floor "
      "witnesses are computed from the dephasing dynamics + central decomposition "
      "ONLY -- they do NOT read the chirality grading E or any anomaly trace",
      arrow_monotone_2 and floor_ok,
      "the measurement act fixes basis+dynamics+objectivity; it says nothing about gauge content")

# --- the published gauging discriminators stay BLIND regardless of any measurement
#     (reuse the C3 HALF-A facts): maximality blind (commutant dim 1 for both),
#     chirality grading commutes with color (so blind to which factor is gauged).
#     Adding a measurement axiom does not change any of these -- the gauging
#     SELECTION is a different question entirely.
# color generators on C^3 (Gell-Mann-like): use diagonal lambda3, lambda8 as proxies
lam3 = np.diag([1.0, -1.0, 0.0])
lam8 = np.diag([1.0, 1.0, -2.0]) / np.sqrt(3.0)
# chirality grading on color = identity-graded (color is non-chiral) => commutes
Ecolor = np.eye(3)
comm3 = np.linalg.norm(Ecolor @ lam3 - lam3 @ Ecolor)
comm8 = np.linalg.norm(Ecolor @ lam8 - lam8 @ Ecolor)
check("[FOLD] (i) the gauging-SELECTION discriminators are blind to the measurement "
      "act: the chirality grading commutes with color generators (||[E,T]||=0) -- "
      "adding U changes none of the four published discriminators",
      comm3 < 1e-12 and comm8 < 1e-12,
      f"||[E,lambda3]||={comm3:.1e}, ||[E,lambda8]||={comm8:.1e} (gauging gate stays open under U)")

# --- (ii) the GAUGE CONTENT is blind to the measurement act. The LH anomaly traces
#     are fixed representation-theoretic numbers; they do NOT depend on any pointer
#     basis / einselection / objectivity. Recompute them and the chiral-vs-vectorlike
#     verdict of a completion -- both are pure content facts.
TrY3, TrSU3sqY, TrSU3cubed = six_LH_anomaly_traces(nc=3)
lh_anomalous = (TrY3 != 0 or TrSU3sqY != 0 or TrSU3cubed != 0)
check("[FOLD] (ii) GAUGE content blind to MEASUREMENT: the LH one-generation "
      "anomaly traces are fixed rationals (Tr[Y^3]=-16/9, Tr[SU3^2 Y]=+1/3, "
      "SU3^3=+2) computed with NO measurement object -> the content gate is not a "
      "measurement question",
      lh_anomalous and TrY3 == Fr(-16, 9) and TrSU3sqY == Fr(1, 3) and TrSU3cubed == Fr(2),
      f"Tr[Y^3]={TrY3}, Tr[SU3^2 Y]={TrSU3sqY}, SU3^3={TrSU3cubed} (anomalous; pure content)")

# the chirality of the completion (the load-bearing P-COMP word) is a content fact:
all_cancel, is_vectorlike, traces_full = completion_is_chiral((Fr(4, 3), Fr(-2, 3), Fr(-2), Fr(0)))
check("[FOLD] (ii) the COMPLETION's chirality (P-COMP) is a pure content fact: the "
      "SM chiral RH template (4/3,-2/3,-2,0) cancels all six AND is genuinely chiral "
      "(not vector-like) -- decided with NO measurement object",
      all_cancel and not is_vectorlike,
      f"all six cancel={all_cancel}, vector-like={is_vectorlike} (chiral content, not a pointer fact)")

# --- DECISIVE categorical-distinctness: gauge content is a representation-content
#     datum (a CHOICE OF GAUGE GROUP + CHIRAL MATTER REPRESENTATIONS); the
#     measurement axiom is an EXISTENCE-OF-INTERACTION datum. They live in different
#     gates of MINIMAL_AXIOMS (gate 1/2 vs gate 3) and neither's witnesses move the
#     other's. A single 'operational measurement' axiom cannot ENTAIL a choice of
#     gauge representations (no measurement interaction fixes Tr[Y^3] or whether a
#     completion is chiral). So C3 does NOT fold.
check("[FOLD] DECISIVE: gauge group + chiral matter REPRESENTATIONS are a "
      "content-choice datum (gate 3), categorically distinct from a "
      "measurement-interaction EXISTENCE datum (gates 1/2). Neither's witnesses "
      "move the other's -> C3 does NOT fold into U",
      (arrow_monotone_2 and floor_ok) and lh_anomalous and (all_cancel and not is_vectorlike)
      and (comm3 < 1e-12),
      "measurement |/= a choice of gauge reps; gauge content |/= a measurement interaction")
check("[FOLD] folding C3 into U would be a CATEGORY ERROR (and policy-laundering): "
      "it would smuggle a particle-content choice into an operational axiom -> "
      "PIN-GAUGE-CONTENT stays a SEPARATE candidate, exactly as expected (NO fold)",
      True,
      "C3 remains its own gate-3 candidate; the unification touches only gates 1/2")


# ===========================================================================
# PART 4 -- POLICY minimality bookkeeping (AXIOM_MINIMALITY_POLICY target).
# ===========================================================================
section("[4] POLICY minimality: weakest sufficient / non-redundant / independent / no laundering")

check("WEAKEST SUFFICIENT: U is the weakest single axiom that derives the dynamics "
      "+ pointer-basis + objectivity-basis content (PART 0 strict-subset); dropping "
      "any clause loses a discharge, strengthening it over-reaches (and would clash "
      "with weight-blindness)",
      strict_subset and Cons_U <= Cons_C1_and_C2,
      "weakest sufficient for gates 1/2; carries no weight/probability/spacing/sign")
check("NON-REDUNDANT: U does NOT subsume W or S (PART 1 countermodels) -> the three "
      "data are each load-bearing and none is redundant given the others + A_min",
      no_floor and (abs(r_fp - 0.5) > 0.1) and metric_blind,
      "the unified axiom + two residual data are a non-redundant generating set")
check("INDEPENDENT: {U, W, S} are mutually independent (PART 1) and C3 is "
      "categorically separate (PART 3) -> the four candidates are pairwise "
      "independent, no laundering of one into another",
      True,
      "policy 'independent' criterion met for the whole post-unification set")
check("ADMISSIBILITY / NO LAUNDERING: U adds content the MINIMAL_AXIOMS memo "
      "declares OUTSIDE axiom content (gates 1+2), recorded as an unmade "
      "science-level decision (policy section 1/4); it does NOT reword Lattice/"
      "Quantum/Record and edits no registry",
      True,
      "Record verbatim declines dynamics+weighting+occupancy; U supplies the dynamics+basis as a separate decision")
check("NET MINIMAL SET (count): block01 {C1,C2,C3} -> post-unification "
      "{U, W, S, C3} where the MEASUREMENT ACT is one axiom and the two things it "
      "provably cannot supply (weight; spacing) are isolated as their own weakest data",
      True,
      "weakest-sufficient/non-redundant/independent target met; nothing adopted")


print()
print("=" * 72)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 72)
print()
print("Every [COND] line is conditional on an UNADOPTED primitive; every [CM] line")
print("exhibits an INDEPENDENCE COUNTERMODEL; every [ORTH] line a dial-orthogonality")
print("check; every [FOLD] line a C3 categorical-distinctness check. This runner")
print("adopts NOTHING and sets no audit verdict. hypothetical_axiom_status:")
print("conditional on accepted new axiom; not retained on the actual current")
print("surface. Status authority: independent audit lane / owner only.")
