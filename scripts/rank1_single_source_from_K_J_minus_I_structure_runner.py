"""
The rank-1 / single-source template (that the GST texture reduces to) is present in the framework's
DERIVED C3 coupling K = |K|(J-I): the J = 3|K| P_singlet piece is RANK-1 (the single C3-singlet
template). This locates the structural pattern; it does not by itself identify K as the physical
mass operator or close the mixing cascade.

The companion GST note reduced the small-mixing MAGNITUDE to "a rank-1 C3-symmetric mass (the singlet
carries the leading generation-dependent mass; light generations degenerate at C3-symmetry)". The
framework's C3 coupling, derived from the interaction asymmetry delta
(INTERACTION_ASYMMETRY_DELTA_OCCUPATION_CURVATURE_TWO_BODY, retained), is K = |K|(J - I):
- J = 3 P_singlet is RANK-1 (eigenvalues 3,0,0): the SINGLE C3-singlet (democratic) source;
- so K = 3|K| P_singlet - |K| I has eigenvalues (2|K|, -|K|, -|K|): a distinct SINGLET + a 2-fold
  DEGENERATE DOUBLET. The generation-distinguishing part of K is the rank-1 J (single source) =
  a template for the rank-1 condition the GST texture reduces to.

Consequences:
- a DEGENERATE doublet + a (symmetric) C3-breaking gives MAXIMAL 1-2 mixing (45deg) in a reduced
  block -- a leading atmospheric-angle candidate pattern, not a prediction from this runner alone;
- the SMALL Cabibbo (theta_C ~ 13deg, NOT 45deg) requires the doublet to be SPLIT (hierarchical) at
  C3-symmetry, so the GST small-mixing magnitude reduces to the doublet MASS HIERARCHY (-> alpha_s).

So the rank-1 / single-source TEMPLATE is framework-native (K's J-I form, derived); the residual under
the mixing magnitudes remains the mass/readout identification plus the mass hierarchy. Memory-safe:
3x3 / 2x2. Class-A.
"""
import numpy as np

PASS = 0; FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ""))
    return ok

J = np.ones((3, 3)); I3 = np.eye(3)

print("=" * 78)
print("A1. the derived C3 coupling K = |K|(J - I): J = 3 P_singlet is RANK-1 (single source)")
print("=" * 78)
Kmag = 0.4
K = Kmag * (J - I3)                                  # the framework's derived C3 coupling
P_singlet = J / 3.0
J_rank1 = np.linalg.matrix_rank(J, tol=1e-9) == 1 and np.allclose(J, 3 * P_singlet)
evJI = np.sort(np.linalg.eigvalsh(J - I3))           # (J-I) eigenvalues: (-1,-1,2)
singlet_doublet = np.allclose(evJI, [-1, -1, 2])     # distinct singlet + degenerate doublet
print(f"   J rank = {np.linalg.matrix_rank(J, tol=1e-9)} (= 3 P_singlet, the single C3-singlet source): {J_rank1}")
print(f"   (J - I) eigenvalues = {np.round(evJI,3)} : singlet isolated (+2), doublet degenerate (-1,-1)")
check("the derived K = |K|(J-I) has a RANK-1 J piece = the single C3-singlet template",
      J_rank1 and singlet_doublet, "the generation-distinguishing part of K is rank-1 (single-source template)")

print()
print("=" * 78)
print("A2. K gives a distinct SINGLET + a 2-fold DEGENERATE DOUBLET (rank-1 template)")
print("=" * 78)
evK = np.sort(np.linalg.eigvalsh(K))                 # (-|K|, -|K|, 2|K|)
doublet_degenerate = np.isclose(evK[0], evK[1]) and not np.isclose(evK[1], evK[2])
print(f"   K eigenvalues = {np.round(evK,3)} : singlet 2|K|={2*Kmag}, doublet -|K|={-Kmag} (degenerate)")
check("the C3 coupling K yields a distinct singlet + degenerate doublet (rank-1 singlet template)",
      doublet_degenerate, "the singlet carries the distinct coupling; the doublet is degenerate")

print()
print("=" * 78)
print("A3. a degenerate doublet + C3-breaking => MAXIMAL mixing in the reduced block")
print("=" * 78)
# the degenerate doublet [[m,0],[0,m]] + a symmetric off-diagonal breaking b => 45deg mixing
m, b = -Kmag, 0.1
D = np.array([[m, b], [b, m]])
ev2, U2 = np.linalg.eigh(D)
theta23 = np.degrees(np.arccos(abs(U2[0, 0])))
maximal = abs(theta23 - 45.0) < 1.0
print(f"   degenerate doublet [[m,b],[b,m]] => mixing angle = {theta23:.1f}deg (maximal)")
print(f"   comparator: lepton atmospheric angle theta_23 is near 45deg (observed ~49deg)")
check("a degenerate doublet (from K's template) + C3-breaking => maximal reduced-block mixing",
      maximal, "candidate atmospheric-angle pattern; not a standalone prediction")

print()
print("=" * 78)
print("A4. the SMALL Cabibbo requires a SPLIT doublet => GST magnitude reduces to the mass hierarchy")
print("=" * 78)
# small mixing (theta_C ~ 13deg, not 45) requires the doublet to be SPLIT at C3-symmetry (m1 != m2):
def mixing(m1, m2, b):
    return np.degrees(abs(0.5 * np.arctan2(2 * b, m2 - m1)))   # 1-2 mixing: tan(2 theta) = 2b/(m2-m1)
th_degenerate = mixing(1.0, 1.0, 0.1)                # degenerate -> 45
th_split = mixing(0.05, 1.0, np.sqrt(0.05))          # split (hierarchical, GST) -> small ~ sqrt(m1/m2)
small_needs_split = abs(th_degenerate - 45) < 1 and th_split < 20
print(f"   degenerate doublet -> {th_degenerate:.1f}deg (maximal);  split/hierarchical doublet -> {th_split:.1f}deg (small, GST)")
print("   => the SMALL Cabibbo requires a SPLIT (hierarchical) doublet in the GST block; the magnitude")
print("      still reduces to the doublet MASS HIERARCHY (m_d << m_s) -> alpha_s. K supplies a native")
print("      rank-1 singlet/doublet template, not the full physical mass/readout closure.")
check("small Cabibbo needs a split doublet => GST magnitude still reduces to the mass hierarchy",
      small_needs_split, "K supplies the rank-1 template; hierarchy/mass-readout remain residual")

print()
print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
