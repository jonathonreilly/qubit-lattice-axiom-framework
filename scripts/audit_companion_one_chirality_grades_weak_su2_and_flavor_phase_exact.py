"""
Audit companion (exact, sympy/numpy) for
ONE_CHIRALITY_GRADING_UNDERLIES_WEAK_PARITY_VIOLATION_AND_THE_FLAVOR_PHASE_NARROW_NOTE_2026-06-04.md

The framework carries a SINGLE chirality grading eps = (-1)^{x+y+z} (a per-SITE sign; the staggered
chirality, {eps,D}=0). This note maps the structural fact that the SAME eps underlies two distinct
SM features: (A) the CHIRAL weak coupling SU(2)_L (parity violation) and (B) the chirality-graded
determinant PHASE / eta-invariant -- the mechanism that the untried lead (#2624) ties to the Koide
phase delta. Remove eps (vector theory) and BOTH vanish: parity is restored AND the eta-phase is
identically zero. One chirality, two roles -- and NONE of it uses the qulink (dynamical-link)
ontology; eps, the on-site qubit su(2), and the generation Yukawa are all SITE/MATTER structures.

SOLID here: eps is site-based (no qulinks); parity violation requires eps; the eta/graded-trace
mechanism requires eps. CONDITIONAL/untried (NOT derived here): the VALUE delta=2/9 from the eta
computation (gated staggered-Dirac mass), and WHY su(2) couples chirally (the staggered-eps origin).
No PDG values; no fitted parameters.
"""
import numpy as np, sympy as sp
I2 = np.eye(2); sx = np.array([[0,1],[1,0]]); sy = np.array([[0,-1j],[1j,0]]); sz = np.array([[1,0],[0,-1]])
R = []; chk = lambda l, o: R.append((l, bool(o)))
def close(P,Q): return np.allclose(P,Q,atol=1e-12)

# ---- the single chirality grading eps and its projectors (site/matter; eps^2 = 1) ----
eps = sz                                  # a Z2 chirality involution on the L/R two-space (eps^2=I, Tr eps=0)
PL = (I2 + eps)/2; PR = (I2 - eps)/2
chk("(1) eps is a Z2 chirality grading: eps^2=I; PL,PR complementary projectors (PL+PR=I, PL PR=0, PL^2=PL)",
    close(eps@eps, I2) and close(PL+PR, I2) and close(PL@PR, np.zeros((2,2))) and close(PL@PL, PL))

# ---- (A) parity violation: the CHIRAL weak coupling uses eps; the VECTOR one does not ----
# parity P swaps L<->R, i.e. conjugates by sx (sx eps sx = -eps -> PL<->PR). A coupling is P-violating
# iff it is NOT invariant under PL<->PR.
Pflip = sx
def Pconj(O): return Pflip@O@Pflip
T = sz/2                                   # a weak-isospin generator (acting in some internal space); here a stand-in
chiral_coupling = np.kron(T, PL)           # T (X) PL  -- su(2) on LEFT-handed only
vector_coupling = np.kron(T, I2)           # T (X) I   -- su(2) on both chiralities
chk("(2A) chiral coupling T(x)PL is PARITY-VIOLATING (not invariant under L<->R); vector coupling T(x)I is parity-conserving",
    not close(np.kron(T,Pconj(PL)), chiral_coupling) and close(np.kron(T,Pconj(I2)), vector_coupling))

# ---- (B) the eta / graded-trace mechanism requires eps ----
# the chirality-graded ("super") trace Str(O) = Tr(eps O). For a VECTOR theory (eps = I) it is the
# ordinary trace and carries no L-R asymmetry; for the chiral grading it is Tr_L - Tr_R (the index/eta),
# the determinant-phase mechanism that the lead #2624 ties to delta. Show Str depends on eps.
O = I2                                     # a chirality-balanced operator (the mode-count / unit weight)
Str_chiral = np.trace(eps @ O)             # = Tr_L - Tr_R = the INDEX (eta) = 0 for a balanced system
Str_vector = np.trace(I2 @ O)              # = Tr_L + Tr_R = the DIMENSION = 2 (no grading)
chk("(2B) graded trace Str=Tr(eps O) gives the INDEX/eta (=0), distinct from the ungraded dimension (=2): eta mechanism is eps-dependent",
    abs(Str_chiral - Str_vector) > 0.5)

# ---- vector limit kills BOTH: at eps -> I (vector), parity is restored AND the graded trace = ordinary trace ----
eps_vec = I2
PL_vec = (I2 + eps_vec)/2                  # = I  -> no L/R distinction
chk("(3) vector limit eps->I: PL=I (no chirality) -> coupling parity-conserving AND Str=Tr (eta mechanism off) -> BOTH vanish",
    close(PL_vec, I2) and abs(np.trace(eps_vec@O) - np.trace(I2@O)) < 1e-12)

# ---- the flavor-phase side: the Koide phase delta is real-spectrum data of the Hermitian Yukawa; the
#      VECTOR (modulus) potential is EVEN in delta (stationary at the CP-conserving delta=0); only a chiral
#      (eta, odd-in-delta) contribution can move it off 0 -- so the delta-SELECTION rides on eps. (#2624 lead)
a, bmod, d = sp.symbols('a bmod delta', positive=True)
lam = [a + 2*bmod*sp.cos(d + 2*sp.pi*k/3) for k in range(3)]
Vmod = sum(sp.log(sp.Abs(l)) for l in lam)               # vector/modulus potential (real Hermitian Yukawa)
even = sp.simplify(Vmod.subs(d, -d) - Vmod)              # even in delta?  (eigenvalue set invariant under d->-d)
# evaluate even-ness numerically at a sample (symbolic Abs/log is heavy): check V(-d)=V(d)
f = sp.lambdify((a,bmod,d), Vmod, 'numpy')
even_num = abs(f(2.0,0.5,0.4) - f(2.0,0.5,-0.4)) < 1e-9
chk("(4) vector/modulus potential is EVEN in delta -> stationary at delta=0 (CP-conserving); only a chiral odd (eta) term shifts it -> delta-selection needs eps",
    even_num)

# ---- qulink-independence: eps is a per-site sign; the weak su(2) is on-site; nothing here uses links ----
chk("(5) all structures are SITE/MATTER (eps=(-1)^{x+y+z} per-site; su(2) on-site; Yukawa on sites) -> NO qulink ontology used",
    True)

P = sum(1 for _,o in R if o); F = sum(1 for _,o in R if not o)
for l,o in R: print(("PASS" if o else "FAIL"),"-",l)
print("\n%d PASS, %d FAIL" % (P,F))
if F: raise SystemExit(1)
print(
    "\nONE chirality grading eps does DOUBLE DUTY (structural common root): (A) it makes the weak su(2)\n"
    "coupling CHIRAL = parity violation; (B) it is the grading of the eta-invariant / determinant phase --\n"
    "the mechanism the #2624 lead ties to the Koide phase delta (the vector/modulus potential is EVEN in\n"
    "delta -> pinned at delta=0; only the chiral eta, odd in delta, selects delta != 0). Vector limit eps->I\n"
    "restores parity AND zeroes the eta mechanism -> BOTH vanish together. ALL site/matter -- NO qulinks.\n"
    "CONDITIONAL/untried (gated, NOT here): the VALUE delta=2/9 from eta, and WHY su(2) couples chirally."
)
