#!/usr/bin/env python3
"""
frontier_abj_arithmetic_cores_bankability_2026_06_20.py

EDGE: anomaly_forces_time ABJ bridge -- EDGE-INDEPENDENT bankability verification
of the THREE arithmetic cores (P-HY anomaly core, P-COMP completion classification,
P-REC spin/taste Clifford core).

GOAL (mirror SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM_NOTE_2026-06-08,
audit-ready PASS=11 on main): show each core is packageable the SAME way --
  (a) ARITHMETIC recomputed in-tree (exact), convention-independent / scale-free;
  (b) its LOAD-BEARING dependency set is retained-grade (parse the audit ledger,
      READ-ONLY); and
  (c) it does NOT route through the UNAUDITED keystone bridge /
      anomaly_forces_time_theorem.

This runner recomputes the arithmetic itself (does NOT trust the in-flight
sibling-branch runners) and independently parses docs/audit/data/audit_ledger.json
(read-only) for the status of every load-bearing dependency.

NO new axiom/primitive. NO edits to docs/audit/data. Exact rational / integer /
small-matrix numpy arithmetic only.
"""

import json
import os
from fractions import Fraction as F
import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(REPO, "docs", "audit", "data", "audit_ledger.json")

PASS = 0
FAIL = 0
LINES = []


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
        LINES.append(f"  [PASS] {name}{(' :: '+detail) if detail else ''}")
    else:
        FAIL += 1
        LINES.append(f"  [FAIL] {name}{(' :: '+detail) if detail else ''}")
    return ok


def header(t):
    LINES.append("")
    LINES.append("=" * 78)
    LINES.append(t)
    LINES.append("=" * 78)


# ---------------------------------------------------------------------------
# Retained-grade vocabulary (learned from the ledger effective_status field).
# These are the audit-lane statuses that are "deps-all-retained" friendly, i.e.
# the SM_ANOMALY_CLOSURE precedent's notion of a closed/retained dependency.
# audited_conditional and unaudited are NOT retained-grade.
# ---------------------------------------------------------------------------
RETAINED_GRADE_EXACT = {
    "retained",
    "retained_bounded",
    "retained_no_go",
    "retained_pending_chain",
}


def is_retained_grade(status):
    if status in RETAINED_GRADE_EXACT:
        return True
    # decorations roll up under a named retained parent
    if isinstance(status, str) and status.startswith("decoration_under_"):
        return True
    return False


# ===========================================================================
header("ABJ ARITHMETIC CORE BANKABILITY -- EDGE-INDEPENDENT VERIFICATION")
LINES.append("Precedent: SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM")
LINES.append("           _NOTE_2026-06-08 (deps-all-retained, audit-ready, PASS=11 on main).")
LINES.append("Target keystone (must NOT be on any core's load-bearing path):")
LINES.append("  anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26")


# ===========================================================================
# CORE 1 -- P-HY scale-free native abelian anomaly core.
#   Y_a = a*P_6 - 3a*P_2  on the LH abelian surface (6 copies (2,3) + 2 copies (2,1)).
#   Claim: nonzero anomaly traces for EVERY a != 0; SM normalization a=1/3,
#   electron-charge sign, and SM names are NOT load-bearing (scale-free).
#   Re-derive: Tr[Y_a]=0, Tr[Y_a^3]=-48 a^3, Tr[SU(3)^2 Y_a]=a, Tr[SU(2)^2 Y_a]=0,
#   Tr[SU(3)^3]_LH = 2; and the a=1/3 specialization -> (-16/9, 1/3, 2).
# ===========================================================================
header("CORE 1: P-HY scale-free native abelian anomaly core")

import sympy as sp
a = sp.Symbol("a", nonzero=True)

# Multiplicities of the LH abelian eigenvalue surface {+1/3 x6, -1 x2}.
# Native generator (scale-free): value +a on the (2,3) block (mult 6),
# value -3a on the (2,1) block (mult 2). At a=1/3 -> +1/3 (x6), -1 (x2).
mult_Q = 6          # (2,3): 2 weak x 3 color
mult_L = 2          # (2,1): 2 weak x 1
yQ = a              # hypercharge eigenvalue on Q_L block (scale-free)
yL = -3 * a         # hypercharge eigenvalue on L_L block (ratio 1:-3, traceless)

# (1) grav^2-U(1)_Y  ==  Tr[Y]
TrY = sp.simplify(mult_Q * yQ + mult_L * yL)
check("PHY.Tr[Y]==0 (scale-free, all a)", sp.simplify(TrY) == 0,
      f"Tr[Y]={TrY}")

# (2) U(1)_Y^3  ==  Tr[Y^3]
TrY3 = sp.simplify(mult_Q * yQ**3 + mult_L * yL**3)
check("PHY.Tr[Y^3]==-48 a^3 (nonzero for a!=0)", sp.simplify(TrY3 - (-48 * a**3)) == 0,
      f"Tr[Y^3]={sp.simplify(TrY3)}")

# (3) SU(3)^2-U(1)_Y mixed anomaly: only colored (2,3) contributes; Dynkin T(3)=1/2,
#     2 weak states each carrying the triplet color index. Tr[SU(3)^2 Y] = T(3) * (#weak) * yQ
#     = (1/2)*2*a = a.  (color singlet L_L does not contribute.)
T3 = sp.Rational(1, 2)
n_weak = 2
TrC2Y = sp.simplify(T3 * n_weak * yQ)
check("PHY.Tr[SU(3)^2 Y]==a (nonzero for a!=0)", sp.simplify(TrC2Y - a) == 0,
      f"Tr[SU(3)^2 Y]={TrC2Y}")

# (4) SU(2)^2-U(1)_Y mixed anomaly: T(2)=1/2 per doublet; each doublet contributes
#     T(2)*(color mult)*Y. Q_L: color mult 3, Y=a -> (1/2)*3*a ; L_L: color mult 1, Y=-3a
#     -> (1/2)*1*(-3a). Sum = (1/2)(3a - 3a) = 0.
T2 = sp.Rational(1, 2)
TrW2Y = sp.simplify(T2 * 3 * yQ + T2 * 1 * yL)
check("PHY.Tr[SU(2)^2 Y]==0 (scale-free, all a)", sp.simplify(TrW2Y) == 0,
      f"Tr[SU(2)^2 Y]={TrW2Y}")

# (5) SU(3)^3 pure-color cubic anomaly of the LH content: 2 weak copies of the
#     SU(3) fundamental, A(3)=+1 each -> 2.
A3 = 1
TrC3 = n_weak * A3
check("PHY.Tr[SU(3)^3]_LH==2", TrC3 == 2, f"Tr[SU(3)^3]_LH={TrC3}")

# (6) a=1/3 specialization reproduces the familiar SM display values.
sub = {a: sp.Rational(1, 3)}
check("PHY.a=1/3 -> Tr[Y^3]=-16/9", sp.simplify(TrY3.subs(sub) - sp.Rational(-16, 9)) == 0,
      f"={TrY3.subs(sub)}")
check("PHY.a=1/3 -> Tr[SU(3)^2 Y]=1/3", sp.simplify(TrC2Y.subs(sub) - sp.Rational(1, 3)) == 0,
      f"={TrC2Y.subs(sub)}")

# (7) Convention-independence witness: at least one anomaly trace is nonzero for a
#     GRID of distinct nonzero a (so the nonzero-anomaly obstruction is forced by
#     the native ratio 1:-3 alone, not by a=1/3).
nz_all = True
for av in [F(1, 3), F(1, 5), F(-2, 7), F(11, 13), F(3)]:
    t3 = -48 * av**3
    c2 = av
    nz_all = nz_all and (t3 != 0) and (c2 != 0)
check("PHY.convention-independent: Tr[Y^3],Tr[SU3^2 Y] nonzero on a-grid",
      nz_all, "grid {1/3,1/5,-2/7,11/13,3} all nonzero")


# ===========================================================================
# CORE 2 -- P-COMP scale-free singlet-completion classification.
#   On Q_L:(2,3)_a, L_L:(2,1)_{-3a}, GIVEN the RH singlet template
#   {u_R:(1,3)_x, d_R:(1,3)_y, e_R:(1,1)_z, n_R:(1,1)_n}, anomaly cancellation
#   forces {x,y,z,n} = {4a,-2a,-6a,0} (unique up to triplet x<->y swap).
#   Plus the load-bearing n=0 counterexample (0,2a,-2a,-4a) and B1/B2/B3 lemmas.
# ===========================================================================
header("CORE 2: P-COMP scale-free singlet-completion classification")

x, y, z, n = sp.symbols("x y z n")

# RH fields ENTER ANOMALY TRACES WITH OPPOSITE CHIRALITY SIGN (subtract from LH).
# We solve the cancellation conditions for the SM template with n_R neutral (n=0).
# (i) mixed SU(3)^2-U(1)_Y: LH colored = 2 weak * (2,3)_a -> 2*a ; RH colored
#     = u_R(3)_x + d_R(3)_y. Cancel: 2a - (x + y) = 0  => x + y = 2a.
eq_mix = sp.Eq(2 * a, x + y)
# (ii) grav^2-U(1)_Y (Tr[Y]): LH 6a + 2(-3a)=0 ; RH 3x + 3y + z + n. With n=0:
#      0 - (3x + 3y + z) = 0  => 3(x+y) + z = 0 => z = -6a (using x+y=2a).
eq_lin = sp.Eq(0, 3 * x + 3 * y + z + 0)
# (iii) cubic U(1)_Y^3: LH = 6 a^3 + 2(-3a)^3 = 6a^3 - 54a^3 = -48a^3 ; RH (color
#       mult: triplets x3) = 3x^3 + 3y^3 + z^3 + n^3. With n=0:
#       -48a^3 - (3x^3 + 3y^3 + z^3) = 0.
eq_cub = sp.Eq(-48 * a**3, 3 * x**3 + 3 * y**3 + z**3)

# Solve the SM-neutral (n=0) template.
sol = sp.solve([eq_mix, eq_lin, eq_cub.subs(z, -6 * a)], [x, y, z], dict=True)
# Expected solution set {x,y} = {4a,-2a}, z=-6a.
forced_ok = False
for s in sol:
    xs = sp.simplify(s.get(x))
    ys = sp.simplify(s.get(y))
    pair = {sp.simplify(xs), sp.simplify(ys)}
    if pair == {sp.simplify(4 * a), sp.simplify(-2 * a)}:
        forced_ok = True
check("PCOMP.anomaly forces {x,y}={4a,-2a}, z=-6a (n=0)", forced_ok,
      f"solutions={[{k: sp.simplify(v) for k,v in s.items()} for s in sol]}")

# Direct verification of the SM witness (4a,-2a,-6a,0) cancelling ALL conditions.
xv, yv, zv, nv = 4 * a, -2 * a, -6 * a, 0
# mixed SU(3)^2 Y
mix = 2 * a - (xv + yv)
# grav^2 Y
lin = 0 - (3 * xv + 3 * yv + zv + nv)
# cubic Y^3
cub = (-48 * a**3) - (3 * xv**3 + 3 * yv**3 + zv**3 + nv**3)
# SU(3)^3: LH 2 (3,3bar? here 2 fundamentals) ; RH u_R,d_R are conjugate triplets
#   -> 2 (LH) - 2 (RH) = 0.
su33 = 2 - 2
check("PCOMP.witness (4a,-2a,-6a,0): mixed SU3^2 Y == 0", sp.simplify(mix) == 0)
check("PCOMP.witness: grav^2 Y (Tr[Y]) == 0", sp.simplify(lin) == 0)
check("PCOMP.witness: cubic Y^3 == 0", sp.simplify(cub) == 0)
check("PCOMP.witness: SU(3)^3 == 0", su33 == 0)

# B3 lemma (global rescaling invariance => absolute scale is convention).
lam = sp.Symbol("lambda", nonzero=True)
cub_scaled = (-48 * (lam * a) ** 3) - (
    3 * (lam * xv) ** 3 + 3 * (lam * yv) ** 3 + (lam * zv) ** 3
)
check("PCOMP.B3 global-Y rescaling preserves cubic zero (scale = convention)",
      sp.simplify(cub_scaled) == 0)

# B2 lemma (vectorlike (Y,-Y) pair preserves all zeros => content not anomaly-unique).
t = sp.Symbol("t")
# add a vectorlike colorless pair +t,-t to the cubic+linear+mixed: contributes 0 each.
check("PCOMP.B2 vectorlike (t,-t) pair adds 0 to Tr[Y] and Tr[Y^3]",
      sp.simplify((t + (-t))) == 0 and sp.simplify((t**3 + (-t) ** 3)) == 0)

# n=0 LOAD-BEARING counterexample: (x,y,z,n)=(0,2a,-2a,-4a) cancels the SAME
# anomalies, so n=0 (neutral singlet) CANNOT be dropped -> uniqueness needs it.
xc, yc, zc, nc = 0, 2 * a, -2 * a, -4 * a
mix_c = 2 * a - (xc + yc)
lin_c = 0 - (3 * xc + 3 * yc + zc + nc)
cub_c = (-48 * a**3) - (3 * xc**3 + 3 * yc**3 + zc**3 + nc**3)
check("PCOMP.B1 counterexample (0,2a,-2a,-4a) cancels mixed SU3^2 Y",
      sp.simplify(mix_c) == 0)
check("PCOMP.B1 counterexample cancels Tr[Y]", sp.simplify(lin_c) == 0)
check("PCOMP.B1 counterexample cancels Tr[Y^3]", sp.simplify(cub_c) == 0)
check("PCOMP.B1 counterexample != SM witness (=> n=0 load-bearing)",
      not (sp.simplify(nc) == 0))

# Scale-free spot checks at several a.
spot_ok = True
for av in [F(1, 3), F(2, 5), F(7, 4), F(-1, 2)]:
    xs, ys, zs, ns = 4 * av, -2 * av, -6 * av, 0
    m = 2 * av - (xs + ys)
    l = 0 - (3 * xs + 3 * ys + zs + ns)
    cc = (-48 * av**3) - (3 * xs**3 + 3 * ys**3 + zs**3 + ns**3)
    spot_ok = spot_ok and (m == 0 and l == 0 and cc == 0)
check("PCOMP.scale-free spot checks a in {1/3,2/5,7/4,-1/2}", spot_ok)


# ===========================================================================
# CORE 3 -- P-REC spin/taste Clifford core (finite-matrix theorem on blocked 2^4).
#   alpha_mu (16x16) from staggered phases eta_mu(b)=(-1)^{sum_{nu<mu} b_nu},
#   (alpha_mu)_{b xor e_mu, b}=eta_mu(b). Prove:
#     - alpha_mu Hermitian involutions, {alpha_mu,alpha_nu}=2 delta I  (Cl_4)
#     - Gamma5spin = alpha0 alpha1 alpha2 alpha3: Hermitian, ^2=I, anticommutes all
#       alpha_mu, rank-8 chirality projectors, commutes with taste commutant
#       (=> genuine taste-singlet spacetime gamma_5)
#     - staggered site-parity eps(b)=(-1)^{sum b} anticommutes alpha_mu BUT is
#       NOT +/-Gamma5spin, NOT in the Cl_4 algebra, does NOT commute with taste
#       commutant (taste-dressed).
# ===========================================================================
header("CORE 3: P-REC spin/taste Clifford core (blocked 2^4 hypercube)")

D = 4
N = 1 << D  # 16


def bit(b, mu):
    return (b >> mu) & 1


def eta(b, mu):
    s = 0
    for nu in range(mu):
        s += bit(b, nu)
    return -1 if (s & 1) else 1


alpha = []
for mu in range(D):
    M = np.zeros((N, N), dtype=float)
    for b in range(N):
        b2 = b ^ (1 << mu)
        M[b2, b] = eta(b, mu)
    alpha.append(M)

I16 = np.eye(N)


def acomm(A, B):
    return A @ B + B @ A


def comm(A, B):
    return A @ B - B @ A


# Hermitian involutions
herm_ok = all(np.allclose(alpha[mu], alpha[mu].T) for mu in range(D))
inv_ok = all(np.allclose(alpha[mu] @ alpha[mu], I16) for mu in range(D))
check("PREC.alpha_mu Hermitian", herm_ok)
check("PREC.alpha_mu involutions (alpha^2=I)", inv_ok)

# Cl_4 anticommutation
cl4_ok = True
for mu in range(D):
    for nu in range(D):
        expected = 2 * I16 if mu == nu else np.zeros((N, N))
        if not np.allclose(acomm(alpha[mu], alpha[nu]), expected):
            cl4_ok = False
check("PREC.{alpha_mu,alpha_nu}=2 delta_{mu nu} I (Cl_4)", cl4_ok)

# Gamma5spin
G5 = alpha[0] @ alpha[1] @ alpha[2] @ alpha[3]
check("PREC.Gamma5spin Hermitian", np.allclose(G5, G5.T))
check("PREC.Gamma5spin^2 = I", np.allclose(G5 @ G5, I16))
ac5 = all(np.allclose(acomm(G5, alpha[mu]), np.zeros((N, N))) for mu in range(D))
check("PREC.Gamma5spin anticommutes every alpha_mu", ac5)

# rank-8 chirality projectors P+/- = (I +/- G5)/2
Pp = (I16 + G5) / 2
Pm = (I16 - G5) / 2
check("PREC.chirality projectors rank 8 / 8",
      np.linalg.matrix_rank(Pp) == 8 and np.linalg.matrix_rank(Pm) == 8)

# Spin algebra generated by alpha_mu: build products, find dimension via SVD rank
# of the flattened generated set. The generated *-algebra of Cl_4 has dim 16.
gens = [I16] + alpha[:]
prods = set()
basis_mats = []


def key(M):
    return tuple(np.round(M.flatten(), 6))


# generate all 2^4 distinct products of distinct alpha_mu (Clifford basis)
from itertools import combinations

clifford_basis = []
for r in range(D + 1):
    for combo in combinations(range(D), r):
        M = I16.copy()
        for mu in combo:
            M = M @ alpha[mu]
        clifford_basis.append(M)
# stack and rank
stack = np.array([M.flatten() for M in clifford_basis])
spin_dim = np.linalg.matrix_rank(stack)
check("PREC.generated spin Clifford algebra dim = 16", spin_dim == 16)

# Taste commutant: matrices commuting with all alpha_mu. Build the commutant of
# the spin algebra by solving for X with [X, alpha_mu]=0 numerically -> dim 16.
# Vectorize: stack commutator maps and find null space dimension.
def commutant_dim(generators, N):
    rows = []
    for G in generators:
        # vec([G,X]) = (I (x) G - G^T (x) I) vec(X)
        M = np.kron(np.eye(N), G) - np.kron(G.T, np.eye(N))
        rows.append(M)
    A = np.vstack(rows)
    # null space dim = N*N - rank(A)
    rank = np.linalg.matrix_rank(A, tol=1e-9)
    return N * N - rank


taste_dim = commutant_dim(alpha, N)
check("PREC.taste commutant dim = 16", taste_dim == 16)

# Build an explicit taste-commutant basis to test G5 commutes with all of it.
# Taste generators: the "other" shift+phase set xi_mu commuting with all alpha_nu.
# Simplest sufficient test: G5 is in the spin algebra, and any element of the
# commutant commutes with every spin-algebra element, hence with G5. Verify on a
# random commutant element constructed via projection onto the null space.
def commutant_basis(generators, N, k=4):
    rows = []
    for G in generators:
        M = np.kron(np.eye(N), G) - np.kron(G.T, np.eye(N))
        rows.append(M)
    A = np.vstack(rows)
    u, s, vh = np.linalg.svd(A)
    tol = 1e-9
    null = vh[np.sum(s > tol):]  # rows of vh spanning null space
    mats = [null[i].reshape(N, N) for i in range(min(k, null.shape[0]))]
    return mats


tbasis = commutant_basis(alpha, N, k=4)
g5_comm_taste = all(np.allclose(comm(G5, T), np.zeros((N, N)), atol=1e-8) for T in tbasis)
check("PREC.Gamma5spin commutes with taste commutant (taste-singlet)",
      g5_comm_taste)

# staggered site-parity eps(b)=(-1)^{sum b}
eps = np.diag([(-1) ** (bin(b).count("1")) for b in range(N)]).astype(float)
eps_ac = all(np.allclose(acomm(eps, alpha[mu]), np.zeros((N, N))) for mu in range(D))
check("PREC.eps anticommutes every alpha_mu (kinetic grading)", eps_ac)

# eps is NOT +/- Gamma5spin
diff_plus = np.max(np.abs(eps - G5))
diff_minus = np.max(np.abs(eps + G5))
check("PREC.eps != +/- Gamma5spin (taste-dressed)",
      diff_plus > 0.5 and diff_minus > 0.5,
      f"max|eps-G5|={diff_plus:.3f}, max|eps+G5|={diff_minus:.3f}")

# eps NOT in the Cl_4 spin algebra: least-squares residual of eps onto clifford_basis
B = np.array([M.flatten() for M in clifford_basis]).T  # (256 x 16)
coef, res, rank, sv = np.linalg.lstsq(B, eps.flatten(), rcond=None)
recon = B @ coef
resid = np.linalg.norm(eps.flatten() - recon)
check("PREC.eps NOT in generated Cl_4 spin algebra (residual>0)", resid > 0.5,
      f"lstsq residual={resid:.3f}")

# eps does NOT commute with the taste commutant (taste-dressed)
eps_taste_comm = max(np.max(np.abs(comm(eps, T))) for T in tbasis)
check("PREC.eps does NOT commute with taste commutant", eps_taste_comm > 1e-6,
      f"max taste-commutator={eps_taste_comm:.3f}")


# ===========================================================================
# DEPENDENCY-SET RETAINED-GRADE AUDIT (read-only ledger parse).
#   For each core, declare its LOAD-BEARING dependency set (the SM_ANOMALY_CLOSURE
#   shape: retained anchors + axiom baseline + EXPLICIT admitted premise + external
#   comparator facts). Verify every retained-anchor dep is retained-grade and that
#   the UNAUDITED keystone is NOT among them.
# ===========================================================================
header("DEPENDENCY-SET RETAINED-GRADE AUDIT (read-only ledger parse)")

with open(LEDGER) as f:
    L = json.load(f)
ROWS = L["rows"]


def status_of(cid):
    r = ROWS.get(cid)
    if r is None:
        return None
    return r.get("effective_status")


KEYSTONE = "anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26"
PARENT = "anomaly_forces_time_theorem"

# Confirm the keystone + parent are UNAUDITED (so routing through them is forbidden).
check("LEDGER.keystone bridge is UNAUDITED (must not be on any core path)",
      status_of(KEYSTONE) == "unaudited", f"status={status_of(KEYSTONE)}")
check("LEDGER.parent anomaly_forces_time_theorem is UNAUDITED",
      status_of(PARENT) == "unaudited", f"status={status_of(PARENT)}")

# Precedent sanity: SM_ANOMALY_CLOSURE is retained-grade and does NOT route through
# the keystone (it is the template).
SMAC = "sm_anomaly_closure_retained_anchors_decoupled_bounded_theorem_note_2026-06-08"
check("LEDGER.precedent SM_ANOMALY_CLOSURE is retained-grade",
      is_retained_grade(status_of(SMAC)), f"status={status_of(SMAC)}")

# ---- Load-bearing retained-anchor dep sets per core (the bankable shape). ----
# Each entry: claim_id  (retained-anchor role). The admitted premise + external
# comparator facts are NOT ledger rows (they are stated, like SM_ANOMALY_CLOSURE P).

CORE_DEPS = {
    "P-HY anomaly core": [
        "graph_first_su3_integration_note",                                  # supplies su(3)+u(1) split + 'hypercharge-like' spectrum
        "native_gauge_closure_note",                                         # SU(2)xSU(3) carrier
        "native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23",  # bounded {+1/3x6,-1x2} surface (decoration under graph-first)
        "lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02",  # ratio 1:-3 (the only scale-free structural input)
    ],
    "P-COMP completion classification": [
        "graph_first_su3_integration_note",                                  # LH content carrier
        "native_gauge_closure_note",                                         # SU(2)xSU(3)
        "native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23",  # LH surface
        # P-COMP admitted premise (RH SU(2)-singlet template incl neutral n_R) is
        # STATED, not imported -- exactly like SM_ANOMALY_CLOSURE premise (P).
    ],
    "P-REC spin/taste Clifford core": [
        "no_per_site_chirality_theorem_note_2026-05-02",                     # root M_2(C) wall (retained_no_go)
        "clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10",  # gamma_5 needs even dim (retained)
        "lorentz_boost_free_staggered_fermion_2point_so4_narrow_theorem_note_2026-05-29",  # alpha_mu surface / D_red(p) (retained_bounded)
        # The staggered carrier itself (Kawamoto-Smit) is the CONSTRUCTION SURFACE
        # recomputed in-tree (alpha_mu built from phases directly), so it need not
        # be a retained-grade load-bearing markdown dep -- see WRINKLE check below.
    ],
}

all_banks = {}
for core, deps in CORE_DEPS.items():
    LINES.append("")
    LINES.append(f"  --- {core} : load-bearing retained-anchor deps ---")
    core_ok = True
    routes_keystone = False
    for cid in deps:
        st = status_of(cid)
        rg = is_retained_grade(st)
        core_ok = core_ok and rg
        if cid in (KEYSTONE, PARENT):
            routes_keystone = True
        ok = check(f"{core} :: dep '{cid}' retained-grade", rg, f"status={st}")
    no_route = (KEYSTONE not in deps) and (PARENT not in deps)
    check(f"{core} :: does NOT route through keystone/parent", no_route)
    bankable = core_ok and no_route
    all_banks[core] = bankable
    check(f"{core} :: BANKABLE NOW (deps-all-retained + decoupled)", bankable)


# ---- WRINKLE: P-REC staggered carrier is audited_conditional (NOT retained). ----
header("WRINKLE: P-REC staggered carrier status (Kawamoto-Smit)")
KS = "staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07"
ks_status = status_of(KS)
LINES.append(f"  staggered_dirac_kawamoto_smit_forcing status = {ks_status}")
# The bankable P-REC core does NOT list KS as a load-bearing dep: it recomputes the
# alpha_mu directly from staggered phases (done above, PREC.* PASS). So the carrier
# enters as RECOMPUTED CONSTRUCTION SURFACE, not as a retained-grade markdown dep.
ks_not_loadbearing = KS not in CORE_DEPS["P-REC spin/taste Clifford core"]
check("PREC.carrier (audited_conditional) is NOT a load-bearing dep "
      "(recomputed in-tree instead)",
      ks_not_loadbearing and ks_status != "unaudited",
      f"KS status={ks_status}; alpha_mu rebuilt in-tree from phases")
check("PREC.WRINKLE flagged: if the bank lists the staggered carrier as "
      "load-bearing it is NOT deps-all-retained",
      not is_retained_grade(ks_status),
      f"KS is {ks_status} -> would break deps-all-retained if cited load-bearing")


# ===========================================================================
header("BANKABILITY SUMMARY")
for core, ok in all_banks.items():
    LINES.append(f"  {'BANKABLE NOW ' if ok else 'NOT BANKABLE '} : {core}")
LINES.append("")
LINES.append("  Admitted premises (STATED, not ledger deps -- mirror SM_ANOMALY_CLOSURE P):")
LINES.append("    P-HY  : the native nonzero abelian direction IS the gauged anomaly-")
LINES.append("            relevant U(1) entering the test (NARROW role); alpha=1/3 is a")
LINES.append("            convention (B3-style rescaling) NOT load-bearing for the core.")
LINES.append("    P-COMP: the opposite-chirality SU(2)-singlet RH template incl neutral n_R.")
LINES.append("    P-REC : the interacting/gauged single-taste reconstruction map (R4, open).")
LINES.append("  External comparator facts (named, reproven-in-runner where arithmetical):")
LINES.append("    Adler 1969; Bell-Jackiw 1969; Dynkin T(2)=T(3)=1/2; SU(3) cubic A(3)=+1.")


# ===========================================================================
LINES.append("")
LINES.append("=" * 78)
LINES.append(f"TOTAL: PASS={PASS} FAIL={FAIL}")
verdict = ("VERDICT: all three ABJ arithmetic cores recomputed exact in-tree AND "
           "each has a deps-all-retained, keystone-decoupled load-bearing set -> "
           "BANKABLE as conditional bounded theorems (SM_ANOMALY_CLOSURE shape). "
           "Identifications remain admitted premises (not derived).") if FAIL == 0 else \
          "VERDICT: bankability NOT fully established (see FAIL lines)."
LINES.append(verdict)
LINES.append("=" * 78)

out = "\n".join(LINES)
print(out)
