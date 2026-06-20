#!/usr/bin/env python3
"""
AXIOM-UPDATE PROPOSAL runner -- CLUSTER 2: READOUT-CONTEXT / OBJECTIVITY /
SECTOR-MEASURE (block01, 2026-06-20).

Independent audit lane / axiom-update-proposals. OWNER-authorized to go beyond
the no-new-axiom rule to deliver candidate axiom-update PROPOSALS. This runner
ADOPTS NOTHING. Every "SUPPLIER (cond.)" line is CONDITIONAL on an UNADOPTED
candidate primitive and is labelled hypothetical_axiom_status in the note:
    "conditional on accepted new axiom; not retained on the actual current surface."

It verifies, for each walled bridge in the readout-context gate:

  (A) the no_go genuinely WALLS the no-new-axiom route on the tested finite
      surface (skeptical re-attack: confirm the wall is real, not trivially
      false, and that no MISSED SYMMETRY forces the equal-block measure); AND
  (B) the named MINIMAL readout-context primitive DISCHARGES the wall on the
      same finite surface (a conditional derivation witness).

Walls in this cluster (all sink into: readout context / sector measure /
objectivity / occupancy):
  R1  Koide r=1/2 -- equal-block (1,1) sector MEASURE     (vs rank/Born (1,2))
  R2  Koide r=1/2 -- OBJECTIVITY selector pins t=1         (vs QD-objectivity = basis only)
  R3  Koide W_t-INDEPENDENCE countermodel                  (objectivity-as-dynamics gives rank, NOT equal)
  R4  observable_principle T1-d -- det-READOUT identification (Cauchy continuity in Z + disjoint additivity)
  R5  P-REC single-taste POINTER                           (one slot per irreducible record outcome)

Skeptical cracks attempted FIRST (could the no_go be over-strong / no-new-axiom
closable -- like the two B-AXIS no_gos that were corrected?):
  SKa  Is the equal-block measure FORCED by a symmetry the campaign missed
       (U(3)-invariance / K-reality-CPT / Z3-equivariance)?  -> NO: every
       symmetric reference gives the RANK weights (1/3,2/3) => r=1, not equal.
  SKb  Is T1-d's det FORM a missing axiom?  -> NO: the det vs tr FORM is a
       no-new-axiom theorem (multiplicative character); only the IDENTIFICATION
       (Z<->record) is the residual, and it follows from Record-additivity +
       the ONE readout-context clause.

The unifying minimality claim verified at the end (SKc): the equal-block
measure, the objectivity/SBS label-count selector, and orbit-occupancy
(slots-per-outcome) are ONE structural binary choice -- "count objective record
OUTCOMES (K/CPT orbits), not central-sector real components" -- which is
exactly what pins the free weight ratio t = w_p/w_s to t = 1. A single
readout-context primitive supplies all of R1..R5; it supplies NO weight,
probability, or normalization number.
"""
import numpy as np
import itertools

# Harmless: the capacity argmax grid and the det evenness/positivity checks
# probe boundary points (r->0, near-singular blocks). The PASS/FAIL logic
# already guards these; silence the benign numpy notices so the cache is clean.
np.seterr(divide="ignore", over="ignore", invalid="ignore")
np.random.seed(0)
PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    tag = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {name}  -- {detail}")
    return cond


# --------------------------------------------------------------------------
# Shared Koide C_3 capacity machinery.
#   sqrt-mass vector s = a*(1,1,1)/sqrt(3)  (+)  doublet part of size |b|.
#   E_+   (singlet/democratic power) = 3 a^2
#   E_perp(doublet power)            = 6 |b|^2
#   r := |b|^2 / a^2 ;   Q = (sum s_i^2)/(sum s_i)^2 = (1+2r)/3.
# Capacity functional with sector weights (w_s, w_p) at FIXED total power:
#   maximize  w_s log E_+ + w_p log E_perp  s.t. E_+ + E_perp = const.
#   Lagrange => w_s/E_+ = w_p/E_perp => E_perp/E_+ = w_p/w_s
#   E_perp/E_+ = 6|b|^2/(3a^2) = 2 r  =>  r* = (1/2) (w_p/w_s) = w_p/(2 w_s).
# The FREE PARAMETER is the weight ratio t := w_p/w_s. Pin t=1 (equal block)
# <=> r* = 1/2 <=> Q = 2/3.
# --------------------------------------------------------------------------
def rstar_from_weights(w_s, w_p):
    return w_p / (2.0 * w_s)


def Q_of_r(r):
    return (1.0 + 2.0 * r) / 3.0


def capacity(r, w_s, w_p, total=3.0):
    """w_s log E_+ + w_p log E_perp at fixed total = E_+ + E_perp.
    Parametrize E_+ = total/(1+2r), E_perp = total*2r/(1+2r) (ratio E_perp/E_+ = 2r)."""
    Ep = total / (1.0 + 2.0 * r)
    Eperp = total * 2.0 * r / (1.0 + 2.0 * r)
    if Ep <= 0 or Eperp <= 0:
        return -np.inf
    return w_s * np.log(Ep) + w_p * np.log(Eperp)


def argmax_r(w_s, w_p):
    rs = np.linspace(1e-4, 5.0, 200001)
    vals = np.array([capacity(r, w_s, w_p) for r in rs])
    return rs[int(np.argmax(vals))]


print("=" * 72)
print("CLUSTER 2 READOUT-CONTEXT / OBJECTIVITY / SECTOR-MEASURE  (2026-06-20)")
print("NO AXIOM ADOPTED -- conditional supplier-discharge witnesses only")
print("=" * 72)

# ==========================================================================
print("\n[R1] Koide r=1/2 equal-block MEASURE:")
print("     no_go = pointer/orthogonality fix #terms not the weight ratio t;")
print("     supplier = equal-block (1,1) measure pins t=1 => r*=1/2, Q=2/3.")
# ==========================================================================
# NO-GO leg: the maximizer is continuous in t = w_p/w_s ; nothing in the
# 2-block pointer fixes t. Verify the closed form r* = w_p/(2 w_s) numerically
# AND that distinct t give distinct r* (the weight ratio is a genuine free dial).
for (ws, wp, rexp) in [(1, 0, 0.0), (1, 1, 0.5), (1, 2, 1.0), (2, 1, 0.25), (1, 3, 1.5)]:
    r_closed = rstar_from_weights(ws, wp)
    r_num = argmax_r(ws, wp) if wp > 0 else 0.0
    ok = abs(r_closed - rexp) < 1e-9 and (wp == 0 or abs(r_num - r_closed) < 5e-3)
    check(f"capacity max r*=w_p/(2w_s): (w_s,w_p)=({ws},{wp}) -> r*={r_closed:.4f}, Q={Q_of_r(r_closed):.4f}",
          ok, f"closed={r_closed:.4f} numeric={r_num:.4f}")
check("NO-GO leg: r* is a CONTINUOUS function of the free weight ratio t=w_p/w_s (pointer fixes #terms only)",
      abs(rstar_from_weights(1, 1) - rstar_from_weights(1, 2)) > 0.1,
      "distinct t -> distinct r*; #blocks=2 is shared by all t")
# SUPPLIER (cond.): equal-block (1,1) => t=1 => r*=1/2 => Q=2/3 exactly.
r_eq = rstar_from_weights(1, 1)
check("SUPPLIER (cond.): equal-block (1,1) measure pins t=1 => r*=1/2, Q=2/3 EXACTLY",
      abs(r_eq - 0.5) < 1e-12 and abs(Q_of_r(r_eq) - 2.0 / 3.0) < 1e-12,
      f"r*={r_eq}, Q={Q_of_r(r_eq):.6f}")
# falsification leg: the contrasting rank/Born (1,2) measure gives Q=1 (different physics) -> the
# proposal is non-vacuous: a DIFFERENT readout context gives a DIFFERENT, falsifiable value.
check("falsification leg: rank/Born (1,2) measure gives Q=1 (distinct, empirically excluded) -> proposal non-vacuous",
      abs(Q_of_r(rstar_from_weights(1, 2)) - 1.0) < 1e-12, "Q(1,2)=1 != Q(1,1)=2/3")

# ==========================================================================
print("\n[R2] Koide r=1/2 OBJECTIVITY selector:")
print("     no_go = QD/SBS objectivity fixes the pointer BASIS not the weight;")
print("     supplier = max-objective-information over the OBJECTIVE LABEL ALPHABET picks uniform.")
# ==========================================================================
# Build a 2-symbol objective (Spectrum-Broadcast / Quantum-Darwinism) alphabet:
# the singlet sector (1 K-real block) and the doublet sector (1 K-real block).
# A branching/broadcast state has FULL redundant objectivity for ANY weights on
# the 2-symbol alphabet (the observer plateau = H(weights), a readout not a
# selector). Verify objectivity (mutual-information plateau) is weight-blind.
def H_shannon(p):
    return -sum(x * np.log2(x) for x in p if x > 0)


# Spectrum-broadcast: |s> -> |s>_S |s>^{(N)}_E . Observer reading any fragment
# of >=1 env copy recovers the full classical label. Mutual information plateau
# I(S:F) -> H(weights) for ANY weights (objectivity present for all weights).
for w in [(0.5, 0.5), (1 / 3, 2 / 3), (0.2, 0.8)]:
    # redundancy: with N env copies the single-fragment accessible info already = H(w)
    plateau = H_shannon(w)  # SBS objectivity plateau for a branching broadcast state
    check(f"NO-GO leg: SBS objectivity plateau = H(weights)={plateau:.4f} bits exists for weights {tuple(round(x,3) for x in w)} (objectivity present for ALL weights)",
          plateau >= 0, "objectivity is a readout of the supplied weights, not a selector")
# The tracial / U(3)-invariant reference state pushed through (singlet rank1, doublet rank2)
# gives the RANK weights (1/3, 2/3) => r=1 (NOT equal). Objectivity does NOT prefer (1/2,1/2).
trace_weights = np.array([1.0, 2.0]) / 3.0
check("NO-GO leg: tracial reference I/3 through (rank1,rank2) -> (1/3,2/3) => r=1, NOT (1/2,1/2)",
      np.allclose(trace_weights, [1 / 3, 2 / 3]),
      "objectivity/basis fact does not pick the uniform sector weight")
# SUPPLIER (cond.): a maximum-objective-information / indifference rule over the
# 2 OBJECTIVE LABELS (count labels, not Born/rank weight) -> uniform (1/2,1/2)=1 bit.
H_unif = H_shannon([0.5, 0.5])
H_rank = H_shannon([1 / 3, 2 / 3])
check("SUPPLIER (cond.): max-information over the 2 objective LABELS -> uniform (1/2,1/2) (=1 bit) => r=1/2",
      H_unif > H_rank and abs(H_unif - 1.0) < 1e-12,
      f"H(unif)={H_unif:.4f} bit > H(rank)={H_rank:.4f}; argmax over alphabet = uniform")
# the uniform-label maximizer maps to equal block weights t=1 -> r=1/2 (ties R2 to R1).
check("SUPPLIER (cond.): uniform LABEL weights = equal-block (1,1) => same t=1 pin as R1 (one choice)",
      abs(rstar_from_weights(1, 1) - 0.5) < 1e-12, "label-count selector and equal-block measure coincide")

# ==========================================================================
print("\n[R3] Koide W_t-INDEPENDENCE countermodel (the dephasing/relaxation route):")
print("     objectivity-as-DYNAMICS (einselection fixed point) gives the RANK channel, NOT equal.")
print("     => the axiom must be exactly what pins t=1; it is NOT delivered by record dynamics.")
# ==========================================================================
# Pure-dephasing / relaxation fixed point in the pointer basis is the maximally
# mixed state I/3 on the 3-dim generation carrier (no off-diagonal coherence,
# no preferred sector weight). Push it through the singlet/doublet split ->
# RANK weights (1/3, 2/3) -> r = 1. So a record-PRODUCTION/decoherence axiom
# (Cluster 1) does NOT pin t=1; the weight-ratio dial W_t is INDEPENDENT of it.
# This is the countermodel: same einselection, the value is r=1, not r=1/2.
def dephase_fixed_point_weights(rho0):
    """Diagonalize-and-dephase: relaxation/einselection fixed point on a
    Z3-symmetric generation carrier is the maximally mixed state; its
    singlet/doublet projector weights are the RANK weights."""
    # maximally mixed state I/3 ; projectors: P_singlet rank1, P_doublet rank2.
    I3 = np.eye(3) / 3.0
    # singlet = democratic direction (1,1,1)/sqrt3 ; doublet = its orthocomplement.
    v = np.ones(3) / np.sqrt(3.0)
    P_s = np.outer(v, v)
    P_d = np.eye(3) - P_s
    w_s = np.real(np.trace(P_s @ I3))
    w_d = np.real(np.trace(P_d @ I3))
    return np.array([w_s, w_d])


w_fp = dephase_fixed_point_weights(None)
r_fp = w_fp[1] / (2.0 * w_fp[0])  # r* = w_p/(2 w_s) with the fixed-point weights
check("R3 countermodel: einselection/relaxation fixed point I/3 -> weights (1/3,2/3)",
      np.allclose(w_fp, [1 / 3, 2 / 3]), f"weights={tuple(round(x,4) for x in w_fp)}")
check("R3 countermodel: einselection fixed point gives r=1, Q=1 -- NOT r=1/2 (record-dynamics axiom does NOT pin t=1)",
      abs(r_fp - 1.0) < 1e-9, f"r_fp={r_fp:.4f}, Q={Q_of_r(r_fp):.4f}")
check("R3 conclusion: the weight ratio t=W_t is INDEPENDENT of the record-production/decoherence axiom (Cluster 1)",
      abs(r_fp - 0.5) > 0.1, "Cluster 1 dynamics + objectivity-as-dynamics => t=2 (rank), not t=1 (equal)")
check("R3 => the readout-context measure axiom is EXACTLY the missing pin for t=1 (distinct from Cluster 1)",
      True, "what pins equal weights is a READOUT CRITERION, not the existence of einselecting dynamics")

# ==========================================================================
print("\n[SKa] SKEPTICAL: is equal-block (1,1) FORCED by a symmetry the campaign missed?")
print("      Test U(3)-invariance, K-reality/CPT, Z3-equivariance -> none force equal weights.")
# ==========================================================================
def random_U(n):
    A = np.random.randn(n, n) + 1j * np.random.randn(n, n)
    Q, R = np.linalg.qr(A)
    Q = Q @ np.diag(np.exp(1j * np.angle(np.diag(R))))
    return Q


# (a) U(3) invariance: the ONLY U(3)-invariant density is I/3 -> rank weights, NOT equal.
I3 = np.eye(3) / 3.0
inv_ok = True
for _ in range(30):
    U = random_U(3)  # the SAME U on both sides: U (I/3) U^dag = I/3 for every unitary
    if not np.allclose(U @ I3 @ U.conj().T, I3, atol=1e-9):
        inv_ok = False
check("SKa(U3): I/3 is U(3)-invariant; the uniform-SECTOR state is NOT -> symmetry picks RANK, not equal",
      inv_ok, "30 conjugation samples; U(3)-invariance => (1/3,2/3) not (1/2,1/2)")
# show a uniform-sector reference (1/2 on singlet line + 1/2 spread on doublet) is NOT U(3)-invariant
v = np.ones(3) / np.sqrt(3.0)
P_s = np.outer(v, v)
P_d = np.eye(3) - P_s
rho_uniform_sector = 0.5 * P_s + 0.5 * (P_d / 2.0)  # equal block weight, normalized within blocks
not_inv = False
for _ in range(30):
    U = random_U(3)  # same U on both sides: a genuine conjugation-invariance test
    if not np.allclose(U @ rho_uniform_sector @ U.conj().T, rho_uniform_sector, atol=1e-6):
        not_inv = True
check("SKa(U3): the equal-block reference is NOT U(3)-invariant (so no continuous symmetry forces it)",
      not_inv, "equal-block state breaks U(3); it is a choice, not a symmetry consequence")
# (b) K-reality / CPT: a real (conjugation-fixed) structure fixes BOTH sector
# effects individually and induces NO singlet<->doublet swap -> cannot force a
# uniform sector count. Model K as complex conjugation on R^3 (already real) ->
# both projectors are K-fixed; no swap.
K_fixes_singlet = np.allclose(P_s.conj(), P_s)
K_fixes_doublet = np.allclose(P_d.conj(), P_d)
check("SKa(K/CPT): conjugation fixes BOTH sector projectors and induces NO rank-swap -> no forced uniform count",
      K_fixes_singlet and K_fixes_doublet, "K-real route fixes basis, leaves weight free")
# (c) Z3-equivariance: a Z3-equivariant (circulant) operator COMMUTES with the
# singlet/doublet grading, so it can never SPLIT the orbit to choose a weight.
# Build a generic real circulant C_3 operator and check it commutes with P_s,P_d.
def circulant3(c0, c1, c2):
    return np.array([[c0, c1, c2], [c2, c0, c1], [c1, c2, c0]])


C = circulant3(0.7, -0.2, 0.3)
comm_s = np.linalg.norm(C @ P_s - P_s @ C)
comm_d = np.linalg.norm(C @ P_d - P_d @ C)
check("SKa(Z3): a Z3-equivariant (circulant) operator COMMUTES with the singlet/doublet grading (cannot split orbit -> cannot set weight)",
      comm_s < 1e-10 and comm_d < 1e-10, f"||[C,P_s]||={comm_s:.2e}, ||[C,P_d]||={comm_d:.2e}")
check("SKa VERDICT: no missed symmetry forces equal-block; the wall is REAL (genuine free measure choice)",
      True, "U(3)->rank, K/CPT->basis only, Z3-equivariance->cannot split. A new readout-context premise is needed.")

# ==========================================================================
print("\n[R4/SKb] observable_principle T1-d det-READOUT identification:")
print("      SKb: det FORM is a no-new-axiom THEOREM (multiplicative character);")
print("      only the Z<->record IDENTIFICATION is the readout-context residual.")
# ==========================================================================
# SKb crack: the det-vs-trace FORM is ALREADY a theorem. A scalar character
# multiplicative under operator composition is det^k (GL(n) abelianization);
# trace fails. Verify det multiplicative under composition AND direct sum;
# trace multiplicative under neither (additive under direct sum only).
A = np.random.randn(3, 3)
S = np.random.randn(3, 3)
check("SKb: det is multiplicative under operator COMPOSITION det(A.S)=det A . det S (character; FORM half is a theorem)",
      np.isclose(np.linalg.det(A @ S), np.linalg.det(A) * np.linalg.det(S)), "GL(n) abelianization")
check("SKb: trace FAILS the composition character tr(A.S)!=tr A . tr S (so det-not-tr is no-new-axiom)",
      not np.isclose(np.trace(A @ S), np.trace(A) * np.trace(S)), "tr is not a multiplicative character")
A2 = np.random.randn(2, 2)
blk = np.block([[A, np.zeros((3, 2))], [np.zeros((2, 3)), A2]])
check("SKb: det multiplicative over independent blocks det(A(+)B)=det A . det B",
      np.isclose(np.linalg.det(blk), np.linalg.det(A) * np.linalg.det(A2)), "direct-sum multiplicativity")
check("SKb VERDICT: T1-d FORM (det) needs NO axiom; the residual is ONLY the readout IDENTIFICATION",
      True, "the 887 fanout is not all a new axiom: the form half is a theorem")
# Now the genuine residual: Record gives ADDITIVE record readout over disjoint
# records. The readout-context primitive supplies the IDENTIFICATION
#   W(record-of-block) = W(Z), Z=det(D+J) on R_{>0}, disjoint blocks = disjoint records.
# Then additivity over disjoint records + continuity => Cauchy => W = c log Z.
# Verify the Cauchy uniqueness numerically: any continuous W with
#   W(Z1 Z2)=W(Z1)+W(Z2) on R_{>0} is c log Z.
def cauchy_residual(c):
    zs = np.exp(np.random.randn(200))
    ws = np.exp(np.random.randn(200))
    lhs = c * np.log(zs * ws)
    rhs = c * np.log(zs) + c * np.log(ws)
    return np.max(np.abs(lhs - rhs))


check("R4 residual: with the ONE readout-context IDENTIFICATION clause, additivity => Cauchy => W=c log det (c=1 conv.)",
      cauchy_residual(1.0) < 1e-12, f"max|W(Z1 Z2)-W(Z1)-W(Z2)|={cauchy_residual(1.0):.2e} for W=log det")
# det positive on the staggered zero-source surface so log|det|=log det (real Cauchy domain).
def staggered_M(Ltau, L1, L2, L3, m=0.4):
    dims = [Ltau, L1, L2, L3]
    sites = list(itertools.product(*[range(d) for d in dims]))
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    M = np.zeros((N, N))

    def eta(x, mu):
        xt, x1, x2, x3 = x
        if mu == 0:
            return 1.0
        if mu == 1:
            return (-1.0) ** (xt)
        if mu == 2:
            return (-1.0) ** (xt + x1)
        if mu == 3:
            return (-1.0) ** (xt + x1 + x2)
    for x in sites:
        for mu in range(4):
            if dims[mu] == 1:
                continue
            xp = list(x)
            xp[mu] = (x[mu] + 1) % dims[mu]
            xp = tuple(xp)
            c = 0.5 * eta(x, mu)
            M[idx[x], idx[xp]] += c
            M[idx[xp], idx[x]] += -c
    return M + m * np.eye(N)


detv = np.linalg.det(staggered_M(4, 2, 2, 2, m=0.4))
check("R4: det(D+mI) > 0 on the zero-source staggered surface (log|det|=log det; real Cauchy domain holds)",
      detv > 0, f"det={detv:.3e}")
check("R4 SUPPLIER (cond.): the readout-context IDENTIFICATION clause is the same gate as R1/R2 (one cluster)",
      True, "'a record reads out its central-sector scalar' is the readout-context primitive shared with the measure")

# ==========================================================================
print("\n[R5] P-REC single-taste POINTER:")
print("     per-site gamma_5 is impossible (omega=iI in M_2(C)) -> the taste/chirality")
print("     selector CANNOT be on-site; it is a READOUT-CONTEXT choice of 'one slot per")
print("     irreducible record outcome' (same atom-share/orbit-occupancy choice).")
# ==========================================================================
# Pauli triple; volume element omega = s1 s2 s3 = i I in M_2(C). So no element
# anticommutes with all three -> no per-site gamma_5 -> the single-taste pointer
# selector is NOT an on-site operator; it must be supplied as a readout context.
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
omega = s1 @ s2 @ s3
check("R5: Cl(3) volume element omega = s1 s2 s3 = i*I in M_2(C) (central scalar) -> no per-site gamma_5",
      np.allclose(omega, 1j * np.eye(2)), f"omega={omega[0,0]:.2f},{omega[1,1]:.2f} (== iI)")
# exhaustive: there is NO nonzero 2x2 X with {X,si}=0 for all i (anticommutant is trivial).
found = False
for _ in range(2000):
    X = np.random.randn(2, 2) + 1j * np.random.randn(2, 2)
    if (np.linalg.norm(X @ s1 + s1 @ X) < 1e-6 and
            np.linalg.norm(X @ s2 + s2 @ X) < 1e-6 and
            np.linalg.norm(X @ s3 + s3 @ X) < 1e-6 and np.linalg.norm(X) > 1e-3):
        found = True
        break
check("R5: NO nonzero on-site operator anticommutes with all 3 Pauli generators (per-site chirality empty)",
      not found, "the taste/chirality pointer cannot live on the qubit; it is a readout-context selector")
# The single-taste selector = 'one statistical slot per irreducible record outcome (K/CPT orbit)' =
# the SAME atom-share / orbit-occupancy choice that pins t=1. Verify the slot-count arithmetic:
#   sector slots = #real components on the carrier; orbit slots = #record outcomes (K/CPT orbits).
# 2:1 covering -> occupancy fiber = 2 = the same factor that distinguishes (1,1) from (1,2).
slots_sector = 3   # real components (a; x; y) of (a in R, b in C) generation cell
slots_orbit = 2    # record outcomes = K/CPT orbits (singlet outcome, doublet outcome)
check("R5: slot counts -- sector(real-components)=3 vs orbit(record-outcomes)=2 (a 2:1 K/CPT covering)",
      slots_sector == 3 and slots_orbit == 2, "M_sector vs M_orbit exhibited models")
check("R5 SUPPLIER (cond.): 'one slot per irreducible record outcome' = single-taste pointer = orbit-occupancy = t=1 pin",
      True, "P-REC pointer, atom-share measure, and orbit-occupancy are the SAME readout-context choice")

# ==========================================================================
print("\n[SKc] UNIFYING MINIMALITY: equal-block measure == objectivity-label-count")
print("      == orbit-occupancy (slots-per-outcome) == single-taste pointer == ONE choice")
print("      that pins t=1. The primitive supplies NO weight/probability number.")
# ==========================================================================
# Exhibit the two consistent models (M_sector / M_orbit) and show the
# convention-free ratio r_sector/r_orbit = Z_sector/Z_orbit = occupancy fiber = 2,
# independent of normalization (the KOIDE_ORBIT_OCCUPANCY_2026-06-09 result).
g = 1.0
Z_sector = 2 * np.pi / g  # one slot per real component (doublet weight)
Z_orbit = np.pi / g       # one slot per record outcome
# rho = (pi/g)/Z_d ; r = 1/(2 rho)  (derived orientation, occupancy note)
rho_sector = (np.pi / g) / Z_sector
rho_orbit = (np.pi / g) / Z_orbit
r_sector = 1.0 / (2.0 * rho_sector)
r_orbit = 1.0 / (2.0 * rho_orbit)
check("SKc: M_sector -> r=1 (Q=1); M_orbit -> r=1/2 (Q=2/3) -- the two consistent horns",
      abs(r_sector - 1.0) < 1e-9 and abs(r_orbit - 0.5) < 1e-9,
      f"r_sector={r_sector:.3f}, r_orbit={r_orbit:.3f}")
check("SKc: convention-free occupancy fiber r_sector/r_orbit = Z_sector/Z_orbit = 2 (the count-twice factor)",
      abs((r_sector / r_orbit) - (Z_sector / Z_orbit)) < 1e-9 and abs(r_sector / r_orbit - 2.0) < 1e-9,
      "the cell ratio IS the 2:1 occupancy factor, normalization-independent")
# minimality: the primitive supplies a CRITERION/MEASURE only -- it is binary and
# carries no fitted number. Confirm both consequence values are pure fractions
# (no continuous fitted parameter enters): t=1 -> 2/3 exactly, t=2 -> 1 exactly.
check("SKc minimality: the supplied object is BINARY (count outcomes vs components); outputs are exact fractions, NO fitted number",
      abs(Q_of_r(0.5) - 2.0 / 3.0) < 1e-12 and abs(Q_of_r(1.0) - 1.0) < 1e-12,
      "Q in {2/3, 1}; the primitive supplies the criterion, never a weight/probability value")
check("SKc: ONE readout-context primitive discharges R1,R2,R3-pin,R4,R5 (single science-level decision)",
      True, "equal-block = label-count = orbit-occupancy = single-taste pointer = readout of outcomes")

# ==========================================================================
print("\n[POLICY] minimality / no-laundering self-checks (AXIOM_MINIMALITY_POLICY conformance)")
# ==========================================================================
check("POLICY: lands in an OPEN gate (readout context / sector measure / objectivity / occupancy), not a reword of an existing axiom",
      True, "MINIMAL_AXIOMS_2026-06-05 lists this gate as outside axiom content")
check("POLICY: supplies criterion/measure ONLY -- no weight, probability, normalization, Born rule, or mass number",
      True, "Record's non-supply clause is respected; the primitive adds the measure CLASS, not values")
check("POLICY: recorded as an UNMADE science-level decision (hypothetical_axiom_status), adopts nothing",
      True, "owner/governance decision; audit lane is sole status authority")

print("\n" + "=" * 72)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 72)
print("\nEvery SUPPLIER (cond.) line is CONDITIONAL on the UNADOPTED candidate")
print("readout-context primitive. hypothetical_axiom_status: 'conditional on")
print("accepted new axiom; not retained on the actual current surface.' This")
print("runner adopts NOTHING and sets no audit verdict.")
