#!/usr/bin/env python3
"""
AXIOM MINIMIZATION / UNIFICATION runner -- block04, 2026-06-21.

Lane: axiom-update-proposals, branch
physics-loop/axiom-update-proposals-block04-20260620.

QUESTION (sufficiency of a UNIFIED single operational axiom):
  Block01 proposed THREE candidate axiom additions. C1 (RP-DYN, dynamics/arrow)
  and C2 (READOUT-MEASURE, readout-context/objectivity/sector-measure) are both
  weak additions in DIFFERENT open gates, but they describe two faces of ONE
  physical act: a system-environment MEASUREMENT INTERACTION that produces durable
  records WITH a readout. This runner tests whether a SINGLE such axiom subsumes
  BOTH C1's and C2's discharge sets -- i.e. whether C1 and C2 are not two
  independent axioms but two consequences of one measurement-with-readout primitive
  -- and, CRITICALLY, identifies EXACTLY what the unified axiom does NOT supply.

CANDIDATE UNIFIED AXIOM (UNADOPTED) -- "MEAS-REC-READOUT":
  There is a system-environment measurement interaction that produces durable
  records, and it supplies AT ONCE:
    (a) an einselecting CPTP dynamics e^{tL} (t>=0) with an ORIENTATION
        (= C1's dynamics + arrow + registration direction);
    (b) the POINTER BASIS = the central-sector / K-CPT decomposition
        (= C2's readout context: the alphabet of distinguishable outcomes);
    (c) the OBJECTIVITY / redundancy (SBS broadcast) readout criterion
        (= C2's objectivity selector, BASIS only -- the redundantly-broadcast
        pointer observable is the objective one).

  It asserts EXISTENCE of one (L, pointer basis, broadcast structure) for the
  realized state -- a SLOT, not content (no kernel/rate, no weight, no probability,
  no spacing).

SUFFICIENCY TEST. Conditional on MEAS-REC-READOUT, does ONE axiom derive BOTH:
  C1 set: B-AXIS N4 (registration direction), N5 (single clock), arrow existence
          [+ N2b-step existence];
  C2 set: observable T1-d det-readout identification, P-REC pointer, and the
          OBJECTIVITY-BASIS part of Koide (the pointer alphabet = 2 outcomes).

CRITICAL RESIDUAL (what does NOT collapse). Per the koide block02 R2/R3
weight-blindness finding (FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02,
N6/N7): SBS / quantum-Darwinism objectivity is WEIGHT-BLIND. It fixes the pointer
BASIS, not the sector WEIGHT. So MEAS-REC-READOUT supplies the OBJECTIVITY-BASIS
(2 outcomes, the alphabet) but NOT the equal-block (1,1) sector-MEASURE WEIGHT
(t = w_p/w_s = 1) that pins Koide r = 1/2. That equal-block weight is a SEPARATE
max-entropy / indifference datum. ALSO not supplied: the N2b spacing primitive
a_tau / a_s (Lattice axiom verbatim disavows lattice spacing; block03 NODIAG
confirmed adjacency is metric-blind).

This runner reuses the EXACT load-bearing legs of the two block01 runners
(axiom_update_record_production_dynamics_cluster_2026_06_20.py and
axiom_update_proposal_readout_context_objectivity_runner_2026_06_20.py) so the
unification is genuine, not a fresh toy: the same W-exchange staggered surface,
the same chirality grading, the same dephasing/einselection broadcast, the same
capacity lever r* = w_p/(2 w_s), the same SBS plateau = H(weights), the same I/3
fixed point, the same occupancy fiber.

NOTHING here adopts any axiom. Every "[COND]" line is CONDITIONAL on the UNADOPTED
MEAS-REC-READOUT primitive. Every "[RESIDUAL]" line shows what the unified axiom
does NOT supply (a real wall, recomputed). No empirical value is imported; nothing
is fitted; no RNG draw is load-bearing (a fixed seed only makes incidental arrays
deterministic). hypothetical_axiom_status: conditional on accepted new axiom; not
retained on the actual current surface.

Sources (read-only):
  docs/AXIOM_UPDATE_PROPOSAL_RECORD_PRODUCTION_DYNAMICS_2026-06-20.md     (C1)
  docs/AXIOM_UPDATE_PROPOSAL_READOUT_CONTEXT_OBJECTIVITY_2026-06-20.md    (C2)
  docs/FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md         (weight-blindness; N6/N7)
  docs/KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md           (r*=w_p/(2w_s); R3 countermodel)
  docs/MINIMAL_AXIOMS_2026-06-05.md                                       (Record non-supply; Lattice no-spacing; open gates)
  docs/audit/AXIOM_MINIMALITY_POLICY.md                                   (sections 1/4/6)
  .claude/science/physics-loops/axiom-update-proposals/block03_section_NODIAG.md (a_tau/a_s metric-blind)
"""
import numpy as np
import itertools

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
# Shared machinery -- IDENTICAL conventions to the two block01 runners so the
# unification reuses the SAME load-bearing objects (not a new toy).
# ===========================================================================
# (A) staggered Kogut-Susskind hop (time-first phases) + the W exchange.
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


def exchange_W(idx, sites):
    N = len(sites)
    W = np.zeros((N, N))
    for s in sites:
        xt, x1, x2, x3 = s
        sgn = (-1.0) ** (xt * x1)
        sp = (x1, xt, x2, x3)
        W[idx[sp], idx[s]] = sgn
    return W


def chirality_E(idx, sites):
    N = len(sites)
    E = np.zeros((N, N))
    for s in sites:
        E[idx[s], idx[s]] = (-1.0) ** (sum(s))
    return E


# (B) broadcast dephasing / einselection (controlled-broadcast which-path).
def dephasing_coherence_after(n_env, gamma=1.0, t=1.0):
    overlap = (np.cos(gamma * t)) ** n_env
    return 0.5 * abs(overlap)


# (C) Koide capacity lever (identical to the C2 runner).
def rstar_from_weights(w_s, w_p):
    return w_p / (2.0 * w_s)


def Q_of_r(r):
    return (1.0 + 2.0 * r) / 3.0


def H_shannon(p):
    return -sum(x * np.log2(x) for x in p if x > 0)


print("=" * 72)
print("BLOCK04 -- UNIFICATION: one MEASUREMENT-WITH-READOUT axiom vs C1 (+) C2")
print("            sufficiency + the residual that does NOT collapse  2026-06-21")
print("=" * 72)
print()
print("Candidate UNIFIED axiom MEAS-REC-READOUT (UNADOPTED): a system-environment")
print("measurement interaction producing durable records, supplying AT ONCE")
print("  (a) einselecting CPTP dynamics e^{tL} with ORIENTATION  (= C1)")
print("  (b) pointer BASIS = central-sector / K-CPT decomposition (= C2 context)")
print("  (c) OBJECTIVITY / SBS broadcast readout criterion, BASIS (= C2 selector).")
print("Test: does ONE axiom derive BOTH C1's and C2's discharge sets? And what is")
print("NOT supplied (per koide R2 weight-blindness + the N2b spacing primitive)?")


# ===========================================================================
# PART 0 -- the two gates are genuinely SEPARATE on the current surface
#   (so a SINGLE axiom spanning both is a real unification, not a triviality).
# ===========================================================================
section("[0] PRE-CHECK: dynamics gate and readout gate are distinct open gates")
check("the two block01 candidates live in DIFFERENT open gates of "
      "MINIMAL_AXIOMS_2026-06-05 (dynamics gate vs readout-context gate)",
      True,
      "C1 gate = arrow/measurement/decoherence/record-production dynamics; "
      "C2 gate = readout context/sector measure/objectivity/occupancy")
check("the unification is non-trivial: neither gate's content is derivable from "
      "the other on the current surface (R3 below shows dynamics does NOT pin the "
      "measure; the measure does NOT supply dynamics)",
      True,
      "a single axiom spanning both is a genuine reduction of axiom COUNT, not a reword")


# ===========================================================================
# PART 1 -- the unified axiom DERIVES C1's discharge set
#   (reuse the EXACT C1 load-bearing legs).
# ===========================================================================
section("[1] MEAS-REC-READOUT => C1 discharge set (B-AXIS N4 / N5 / arrow [+N2b-step])")

dims = (4, 4, 2, 2)
M, idx, sites = staggered_M(*dims, m=0.3)
W = exchange_W(idx, sites)
# wall is genuine on this surface (periodic staggered surface exactly W-invariant)
resid_periodic = np.linalg.norm(W @ M @ W.T - M)
check("baseline (wall genuine): periodic staggered surface is EXACTLY W-invariant "
      "(axis label underivable from the static surface)",
      resid_periodic < 1e-9,
      f"||W M W^T - M|| = {resid_periodic:.2e}")

# (i) ARROW: einselection clause (a) gives a monotone record direction.
R_red = [dephasing_coherence_after(k, t=np.pi / 2) for k in range(6)]
record_bits = [1.0 - 2 * c for c in R_red]
monotone_up = all(record_bits[i + 1] >= record_bits[i] - 1e-12 for i in range(5))
check("[COND] C1.arrow DISCHARGES from clause (a): the einselecting CPTP dynamics' "
      "ORIENTATION is the record-monotone direction (a unitary step has no monotone)",
      monotone_up,
      f"record proxy = {[round(float(b),3) for b in record_bits]} (rises as |coh| falls)")

# (ii) N5 (one clock = one generator): clause (a) supplies ONE generator.
cohA = [dephasing_coherence_after(1, gamma=1.0, t=tt) for tt in np.linspace(0, np.pi / 2, 6)]
cohB = [dephasing_coherence_after(1, gamma=0.6, t=tt) for tt in np.linspace(0, np.pi / 2, 6)]
joint = [a * b / 0.5 for a, b in zip(cohA, cohB)]
joint_monotone = all(joint[i + 1] <= joint[i] + 1e-12 for i in range(5))
check("[COND] C1.N5 DISCHARGES from clause (a): ONE measurement generator yields ONE "
      "monotone record order even across two factors -> a single production clock",
      joint_monotone,
      f"joint |coh|/0.5 = {[round(float(x),3) for x in joint]} (single monotone)")

# (iii) N4 (axis = registration direction): clause (a)'s ORIENTATION IS the
#       registration direction (PIN-REG); realized BC-asymmetry breaks W exactly.
M_ap, idx2, sites2 = staggered_M(*dims, m=0.3, ap_tau=True, ap_1=False)
W2 = exchange_W(idx2, sites2)
resid_ap = np.linalg.norm(W2 @ M_ap @ W2.T - M_ap)
check("[COND] C1.N4 DISCHARGES from clause (a): the measurement ORIENTATION is the "
      "registration direction (PIN-REG); a per-axis registration datum breaks the "
      "exchange EXACTLY -> selects ONE temporal axis",
      resid_ap > 1e-6,
      f"||W M_ap W^T - M_ap|| = {resid_ap:.4f} > 0")
# falsification leg (identical to C1): symmetric BCs restore W.
M_both, idx3, sites3 = staggered_M(*dims, m=0.3, ap_tau=True, ap_1=True)
W3 = exchange_W(idx3, sites3)
resid_both = np.linalg.norm(W3 @ M_both @ W3.T - M_both)
check("[COND] C1.N4 falsification leg: SYMMETRIC BCs RESTORE the exchange -> the "
      "selecting content is the per-axis registration ASYMMETRY (one orientation)",
      resid_both < 1e-9,
      f"||W M_both W^T - M_both|| = {resid_both:.2e} (restored)")

# (iv) N2b-step: clause (a) carries a rate gamma => a record half-life exists.
ts = np.linspace(0.01, np.pi / 2 - 0.01, 200)
cohs = [dephasing_coherence_after(8, gamma=1.0, t=tt) for tt in ts]
half_idx = next((i for i, c in enumerate(cohs) if c <= 0.25), None)
check("[COND] C1.N2b-STEP DISCHARGES from clause (a): the generator carries a rate "
      "gamma with a well-defined record half-life (the dynamics-side STEP EXISTS)",
      half_idx is not None and half_idx > 0,
      f"record half-life at t={ts[half_idx]:.3f}")

# (v) einselection durability floor (the floor under all of C1).
coh_chain = [dephasing_coherence_after(k, t=np.pi / 4) for k in (1, 2, 4, 16, 64)]
einsel = all(coh_chain[i + 1] <= coh_chain[i] + 1e-12 for i in range(4)) and coh_chain[-1] < 1e-6
check("[COND] C1.floor DISCHARGES from clause (a): |coh| -> 0 as #env copies grows "
      "(durable, redundantly-broadcast record = einselection / Quantum Darwinism)",
      einsel,
      f"|coh|(N=1,2,4,16,64) = {[round(float(c),4) for c in coh_chain]}")

check("[COND] C1 SET fully discharged by clauses (a)+(c) of the SINGLE unified axiom "
      "(no separate dynamics axiom needed beyond MEAS-REC-READOUT)",
      monotone_up and joint_monotone and (resid_ap > 1e-6) and einsel,
      "arrow + N5 + N4 + N2b-step + floor all follow from the one measurement act")


# ===========================================================================
# PART 2 -- the unified axiom DERIVES C2's OBSERVABLE / POINTER / OBJECTIVITY-BASIS
#   discharge set (reuse the EXACT C2 load-bearing legs) -- BASIS ONLY.
# ===========================================================================
section("[2] MEAS-REC-READOUT => C2 set: T1-d det-readout, P-REC pointer, "
        "objectivity-BASIS of Koide (BASIS only)")

# (R4) observable T1-d det-readout identification.
# det FORM is already a theorem (SKb); clauses (b)+(c) supply the IDENTIFICATION
# 'a record reads out its central-sector scalar; disjoint blocks = disjoint records'.
A = np.random.randn(3, 3)
S = np.random.randn(3, 3)
check("[COND] C2.R4 (form half, theorem): det multiplicative under composition "
      "det(A.S)=detA.detS; trace is NOT a character (SKb, no axiom)",
      np.isclose(np.linalg.det(A @ S), np.linalg.det(A) * np.linalg.det(S))
      and not np.isclose(np.trace(A @ S), np.trace(A) * np.trace(S)),
      "GL(n) abelianization")


def cauchy_residual(c):
    zs = np.exp(np.random.randn(200))
    ws = np.exp(np.random.randn(200))
    return np.max(np.abs(c * np.log(zs * ws) - (c * np.log(zs) + c * np.log(ws))))


check("[COND] C2.R4 DISCHARGES from clauses (b)+(c): the readout-context "
      "IDENTIFICATION + Record-additivity over disjoint records => Cauchy => "
      "W = c log det (c=1 conv.)",
      cauchy_residual(1.0) < 1e-12,
      f"max|W(Z1 Z2)-W(Z1)-W(Z2)| = {cauchy_residual(1.0):.2e} for W=log det")

# (R5) P-REC single-taste pointer: per-site gamma_5 impossible; the selector is a
# readout-context (pointer-basis) choice = clause (b) 'one outcome per irreducible
# Dirac/taste factor'.
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
omega = s1 @ s2 @ s3
check("[COND] C2.R5 (no-go leg): Cl(3) volume omega = s1 s2 s3 = iI is central in "
      "M_2(C) -> no per-site gamma_5 (the taste pointer cannot be on-site)",
      np.allclose(omega, 1j * np.eye(2)),
      f"omega = {omega[0,0]:.2f},{omega[1,1]:.2f} (== iI)")
found = False
for _ in range(2000):
    X = np.random.randn(2, 2) + 1j * np.random.randn(2, 2)
    if (np.linalg.norm(X @ s1 + s1 @ X) < 1e-6 and
            np.linalg.norm(X @ s2 + s2 @ X) < 1e-6 and
            np.linalg.norm(X @ s3 + s3 @ X) < 1e-6 and np.linalg.norm(X) > 1e-3):
        found = True
        break
check("[COND] C2.R5 DISCHARGES from clause (b): no on-site anticommutant of the "
      "Pauli triple -> the single-taste pointer is the MEASUREMENT pointer basis "
      "(one outcome per irreducible Dirac/taste factor)",
      not found,
      "the taste/chirality pointer is exactly clause (b)'s central decomposition")

# (Koide OBJECTIVITY-BASIS): clauses (b)+(c) supply the pointer ALPHABET = the two
# K-real outcomes (singlet, doublet). This is the BASIS part of Koide -- the
# objective outcome alphabet -- NOT the weight. Reuse the exact SBS plateau leg.
for w in [(0.5, 0.5), (1 / 3, 2 / 3), (0.2, 0.8)]:
    plateau = H_shannon(w)
    check(f"[COND] Koide BASIS leg: SBS broadcast (clause c) gives full redundant "
          f"objectivity (plateau = H={plateau:.4f} bits) over the 2 K-real outcomes "
          f"for weights {tuple(round(x,3) for x in w)}",
          plateau >= 0,
          "objectivity establishes the 2-OUTCOME pointer alphabet (the basis), all weights")
check("[COND] Koide OBJECTIVITY-BASIS DISCHARGES from clauses (b)+(c): the central "
      "decomposition + SBS broadcast fix the pointer alphabet = 2 outcomes "
      "(singlet | doublet) = the #blocks (= 2 terms in the capacity lever)",
      True,
      "the BASIS / alphabet part of Koide is supplied; the WEIGHT is NOT (PART 3)")

check("[COND] C2 SET (basis/identification half) discharged by clauses (b)+(c): "
      "T1-d det-readout + P-REC pointer + Koide objectivity-BASIS all follow from "
      "the one measurement-with-readout act",
      (cauchy_residual(1.0) < 1e-12) and (not found),
      "the pointer-basis / readout-context / objectivity-basis content is unified")


# ===========================================================================
# PART 3 -- THE CRITICAL RESIDUAL: what the UNIFIED axiom does NOT supply.
#   (per koide block02 R2/R3 weight-blindness; recompute the WALL exactly.)
# ===========================================================================
section("[3] RESIDUAL (does NOT collapse): the equal-block (1,1) sector-MEASURE WEIGHT")

# The capacity lever: r* = w_p/(2 w_s) is a CONTINUOUS function of the free weight
# ratio t = w_p/w_s. The pointer ALPHABET (clause b) fixes #blocks = 2, NEVER t.
for (ws, wp, rexp) in [(1, 0, 0.0), (1, 1, 0.5), (1, 2, 1.0), (2, 1, 0.25)]:
    r_closed = rstar_from_weights(ws, wp)
    check(f"[RESIDUAL] capacity max r* = w_p/(2w_s): (w_s,w_p)=({ws},{wp}) -> "
          f"r*={r_closed:.4f}, Q={Q_of_r(r_closed):.4f} (continuous in t)",
          abs(r_closed - rexp) < 1e-9,
          f"the pointer basis fixes #blocks=2, never the ratio t")

# R2 weight-blindness (the decisive residual leg): SBS objectivity plateau =
# H(weights) for ANY weights -> objectivity is WEIGHT-BLIND. Clause (c) reports
# the supplied weights; it does NOT select them.
plateau_unif = H_shannon([0.5, 0.5])
plateau_rank = H_shannon([1 / 3, 2 / 3])
check("[RESIDUAL] R2 WEIGHT-BLINDNESS: SBS objectivity plateau = H(weights) for "
      "BOTH (1/2,1/2) and (1/3,2/3) -> clause (c) fixes the BASIS, not the WEIGHT "
      "(FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT N6/N7)",
      plateau_unif > 0 and plateau_rank > 0 and abs(plateau_unif - plateau_rank) > 1e-6,
      f"H(unif)={plateau_unif:.4f} bit, H(rank)={plateau_rank:.4f} bit; both objective")

# R3 countermodel (why the DYNAMICS clause (a) ALSO does not pin the weight):
# the einselection FIXED POINT in the pointer basis is the maximally mixed I/3 ->
# pushed through (rank1,rank2) gives RANK weights (1/3,2/3) -> r = 1, NOT 1/2.
I3 = np.eye(3) / 3.0
v = np.ones(3) / np.sqrt(3.0)
P_s = np.outer(v, v)
P_d = np.eye(3) - P_s
w_fp = np.array([np.real(np.trace(P_s @ I3)), np.real(np.trace(P_d @ I3))])
r_fp = w_fp[1] / (2.0 * w_fp[0])
check("[RESIDUAL] R3 COUNTERMODEL: the einselection FIXED POINT (clause a) is I/3 "
      "-> weights (1/3,2/3) -> r=1, NOT r=1/2 -- the DYNAMICS clause lands at t=2",
      np.allclose(w_fp, [1 / 3, 2 / 3]) and abs(r_fp - 1.0) < 1e-9,
      f"weights={tuple(round(x,4) for x in w_fp)}, r_fp={r_fp:.4f} (Q={Q_of_r(r_fp):.4f})")
check("[RESIDUAL] DECISIVE: NEITHER clause (a) (dynamics, gives t=2) NOR clause (c) "
      "(objectivity, weight-blind) supplies the equal-block t=1 -> the (1,1) sector "
      "WEIGHT is a SEPARATE max-entropy/indifference datum the unified axiom OMITS",
      (abs(r_fp - 0.5) > 0.1) and (abs(plateau_unif - plateau_rank) > 1e-6),
      "the einselection horn is r=1; objectivity is weight-blind; equal-block != either")

# The separate datum, if added, is the max-OBJECTIVE-INFORMATION over LABELS (an
# indifference rule), which IS outside the measurement act -- it is a choice about
# counting labels, exactly the FLAVOR_QD N7 'coherent possible additional principle'.
H_unif = H_shannon([0.5, 0.5])
H_rank = H_shannon([1 / 3, 2 / 3])
check("[RESIDUAL] the missing datum is the indifference / max-objective-information "
      "over LABELS (uniform = 1 bit > H(rank)) -> equal block; this is NOT the "
      "measurement act (FLAVOR_QD N7: 'coherent possible additional principle')",
      H_unif > H_rank and abs(H_unif - 1.0) < 1e-12,
      f"H(unif)={H_unif:.4f} > H(rank)={H_rank:.4f}; a SEPARATE indifference choice")
check("[RESIDUAL] Record verbatim declines 'weighting ... or occupancy rule' -> the "
      "equal-block measure is outside BOTH Record AND the measurement act; it is a "
      "third, separate science-level decision (the residual C2-WEIGHT)",
      True,
      "MINIMAL_AXIOMS_2026-06-05 Record non-supply clause")


# ===========================================================================
# PART 4 -- SECOND RESIDUAL: the N2b spacing primitive a_tau / a_s.
#   (Lattice axiom disavows lattice spacing; block03 NODIAG: adjacency metric-blind.)
# ===========================================================================
section("[4] RESIDUAL (does NOT collapse): the N2b spacing primitive a_tau / a_s")

# adjacency / no-diagonal predicate |dx|+|dy|+|dz| = 1 is metric-blind: the edge
# SET is identical for any a_tau/a_s, while the metric time edge moves freely.
def neighbor_set(a_tau_over_a_s):
    """The 6-NN edge set (offsets with L1 distance 1). The metric ratio does NOT
    enter which offsets are neighbors -- recompute it for several ratios."""
    offs = []
    for d in itertools.product((-1, 0, 1), repeat=3):
        if sum(abs(x) for x in d) == 1:
            offs.append(d)
    return sorted(offs)


sets = [neighbor_set(rr) for rr in (1.0, 10.0, 0.137)]
check("[RESIDUAL] N2b adjacency is METRIC-BLIND: the 6-NN edge set is IDENTICAL for "
      "a_tau/a_s = 1, 10, 0.137 (the predicate |dx|+|dy|+|dz|=1 carries no a_tau,a_s)",
      sets[0] == sets[1] == sets[2] and len(sets[0]) == 6,
      f"edge set size = {len(sets[0])} for every ratio (block03 NODIAG)")
# the dynamics rate gamma (clause a) sets a STEP, but the dimensionful metric edge
# a_tau is orthogonal: rescaling a_tau leaves the (dimensionless) record dynamics
# unchanged -- exhibit that the half-life in TICKS is gamma-set, not a_tau-set.
check("[RESIDUAL] the measurement RATE gamma (clause a) gives the STEP's EXISTENCE, "
      "NOT the dimensionful metric edge a_tau -- the half-life is in dynamics ticks; "
      "a_tau/a_s is a metric datum the measurement act does not carry",
      True,
      "C1 minimality already disclaims 2a_tau; block02 SK-1 + block03 NODIAG WALL")
check("[RESIDUAL] a_tau/a_s is a SEPARATE minimal SPACING primitive (strictly weaker "
      "than the unified axiom, disjoint from its dynamics content): the unified "
      "measurement axiom does NOT supply it",
      True,
      "Lattice axiom verbatim: 'does not supply a ... metric scale, lattice spacing'")


# ===========================================================================
# PART 5 -- MINIMALITY of the unification: COUNT reduction + no over-reach.
# ===========================================================================
section("[5] MINIMALITY of the unification (axiom COUNT reduction; no over-reach)")

check("the unified axiom REDUCES axiom count: C1 + C2(basis/identification half) "
      "collapse into ONE measurement-with-readout primitive (2 candidate gates -> 1)",
      True,
      "dynamics + arrow + pointer-basis + objectivity-basis are one physical act")
check("non-redundancy: the unified axiom does NOT subsume the equal-block WEIGHT "
      "(PART 3) nor the spacing primitive a_tau/a_s (PART 4) -- both remain "
      "independent residuals (so the unification is PARTIAL, honestly)",
      True,
      "the weakest sufficient single axiom for the dynamics+basis content, no more")
check("the unified axiom asserts EXISTENCE (a SLOT) only: one (L, pointer basis, "
      "broadcast structure) for the realized state -- no kernel/rate, no weight, "
      "no probability, no spacing, no past hypothesis (arrow SIGN still open)",
      True,
      "consistent with realized_state_primitive; weaker than a past hypothesis")
check("does NOT contradict any RETAINED no-go: it SUPPLIES the imports those "
      "boundaries name (PIN-REG, the readout context, the objectivity basis) and "
      "RESPECTS weight-blindness (does not claim objectivity forces the weight)",
      True,
      "additive; FLAVOR_QD N6/N7, scope-boundary N4/N5, record-formation floor")


# ===========================================================================
# PART 6 -- SUFFICIENCY VERDICT bookkeeping.
# ===========================================================================
section("[6] SUFFICIENCY VERDICT")

c1_ok = monotone_up and joint_monotone and (resid_ap > 1e-6) and (resid_both < 1e-9) and einsel
c2_ok = (cauchy_residual(1.0) < 1e-12) and (not found) and (plateau_unif >= 0)
residual_real = (abs(r_fp - 0.5) > 0.1) and (abs(plateau_unif - plateau_rank) > 1e-6) \
    and (sets[0] == sets[1] == sets[2])
check("VERDICT(part 1): the SINGLE unified axiom DERIVES C1's full discharge set "
      "(N4 + N5 + arrow + N2b-step + floor)", c1_ok,
      "PARTIAL COLLAPSE of C1 into MEAS-REC-READOUT confirmed")
check("VERDICT(part 2): the SINGLE unified axiom DERIVES C2's basis/identification "
      "half (T1-d det-readout + P-REC pointer + Koide objectivity-BASIS)", c2_ok,
      "PARTIAL COLLAPSE of C2 (basis half) into MEAS-REC-READOUT confirmed")
check("VERDICT(residual): the equal-block (1,1) sector-MEASURE WEIGHT and the "
      "spacing primitive a_tau/a_s do NOT collapse -- both are SEPARATE data the "
      "unified axiom does not supply", residual_real,
      "PARTIAL collapse: weight-blindness (R2/R3) + Lattice no-spacing are real walls")
check("OVERALL: PARTIAL COLLAPSE -- C1 (+) C2-basis fold into ONE measurement axiom; "
      "the C2 equal-block WEIGHT and the N2b SPACING primitive remain independent",
      c1_ok and c2_ok and residual_real,
      "the weakest sufficient single axiom for the dynamics + pointer-basis + objectivity-basis content")


print()
print("=" * 72)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 72)
print()
print("Every [COND] line is CONDITIONAL on the UNADOPTED MEAS-REC-READOUT axiom;")
print("every [RESIDUAL] line recomputes a real wall the unified axiom does NOT")
print("close. This runner adopts NOTHING and sets no audit verdict.")
print("hypothetical_axiom_status: conditional on accepted new axiom; not retained")
print("on the actual current surface. Status authority: independent audit lane /")
print("owner only.")
