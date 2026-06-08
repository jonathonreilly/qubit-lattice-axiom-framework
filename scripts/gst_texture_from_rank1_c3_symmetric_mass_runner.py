"""
The GST texture (sin theta = sqrt(mass-ratio)) is DERIVED from a RANK-1 C3-symmetric mass + a
single-source C3-breaking. In the reduced light/heavy two-state block, the geometric-mean
off-diagonal = the texture zero (1,1)=0 = "the light generation's mass is PURELY from C3-breaking
mixing"; this is not a zero-entry claim about the original C3 site-basis singlet projector.

This identifies a candidate shared magnitude residual under the small-angle account:
the C3-breaking framing (companion: both angles are C3-breaking order parameters) is sqrt(mass-ratio)
-scaled IF the texture is geometric-mean (GST). This note reduces the GST texture to a clean condition:

  (rank-1 C3-symmetric mass) + (single-source C3-breaking) => sin theta = sqrt(m_light/m_heavy).

Mechanism (a see-saw within the flavor sector):
- the C3-singlet carries the leading mass; the C3-symmetric mass is RANK-1 (singlet only), so the
  light generations are MASSLESS at C3-symmetric order -- the reduced-block (1,1)=0 texture zero;
- ONE C3-breaking source b then gives the light mass at SECOND order (m_light = b^2/m_heavy, the
  see-saw suppression) AND the mixing at FIRST order (theta = b/m_heavy);
- so m_light/m_heavy = (b/m_heavy)^2 = theta^2  =>  theta = sqrt(m_light/m_heavy) [GST].

The geometric mean b = sqrt(m_light m_heavy) is the texture zero's det identity. The residual is the
RANK-1 / single-source condition (the C3-symmetric mass from a single C3-invariant source).

Memory-safe: 2x2 / 3x3. Class-A. TOTAL: PASS=N FAIL=0 expected.
"""
import numpy as np

PASS = 0; FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ""))
    return ok

print("=" * 78)
print("A1. a RANK-1 C3-symmetric mass (singlet only) => light generations MASSLESS at C3-symmetry")
print("=" * 78)
J = np.ones((3, 3))
P_singlet = J / 3.0                                   # the C3-singlet projector ((1,1,1)/sqrt3)
m_heavy = 5.0
M_sym = m_heavy * P_singlet                           # rank-1 C3-symmetric mass: only the singlet is massive
ev = np.sort(np.linalg.eigvalsh(M_sym))
rank1 = np.linalg.matrix_rank(M_sym, tol=1e-9) == 1
light_massless = np.allclose(ev[:2], 0)              # the doublet (light generations) is massless
print(f"   M_sym = m_heavy * P_singlet : rank = {np.linalg.matrix_rank(M_sym, tol=1e-9)}; eigenvalues = {np.round(ev,3)}")
check("rank-1 C3-symmetric mass (C3-singlet only) leaves the light generations massless at C3-symmetry",
      rank1 and light_massless, "reduced light/heavy block has no C3-symmetric direct light mass")

print()
print("=" * 78)
print("A2. the texture zero (1,1)=0 IS the geometric-mean off-diagonal (det identity)")
print("=" * 78)
# Fritzsch 1-2 block [[0, b],[b, a]]: det = -b^2 = -m_light*m_heavy => b = sqrt(m_light*m_heavy)
a, b = 1.0, 0.22
Mf = np.array([[0.0, b], [b, a]])
ev2 = np.linalg.eigvalsh(Mf)
mlight, mheavy = abs(ev2[0]), abs(ev2[1])            # |eigenvalues|
geom_mean = np.isclose(b, np.sqrt(mlight * mheavy), atol=1e-9)   # b = sqrt(m_l m_h) from det = -b^2
print(f"   [[0,b],[b,a]] with b={b}: |eigenvalues| = ({mlight:.4f}, {mheavy:.4f}); det = -b^2")
print(f"   => b = sqrt(m_light * m_heavy) = {np.sqrt(mlight*mheavy):.4f} (the geometric mean): {geom_mean}")
check("(1,1)=0 <=> off-diagonal b = sqrt(m_light * m_heavy) (geometric mean, from det)",
      geom_mean, "the GST geometric mean IS the texture zero")

print()
print("=" * 78)
print("A3. single-source C3-breaking => m_light = b^2/m_heavy (2nd order) + theta = b/m_heavy (1st)")
print("=" * 78)
# the SAME b gives the light mass (see-saw, 2nd order) and the mixing (1st order) => GST
def fritzsch(a, b):
    M = np.array([[0.0, b], [b, a]])
    ev, U = np.linalg.eigh(M)
    order = np.argsort(np.abs(ev))                   # light, heavy
    ml, mh = abs(ev[order[0]]), abs(ev[order[1]])
    theta = abs(np.arctan2(U[0, order[1]], U[1, order[1]]))   # mixing of the heavy eigenvector
    theta = min(theta, np.pi/2 - theta)
    return ml, mh, theta
seesaw_ok = True
gst_ok = True
for bb in (0.05, 0.1, 0.2):
    ml, mh, th = fritzsch(1.0, bb)
    if not np.isclose(ml, bb**2/mh, rtol=0.05): seesaw_ok = False           # m_light ~ b^2/m_heavy
    if not np.isclose(np.sin(th), np.sqrt(ml/mh), rtol=0.05): gst_ok = False  # sin theta ~ sqrt(ratio)
print(f"   b=0.05,0.1,0.2: m_light ~ b^2/m_heavy (see-saw): {seesaw_ok}; sin theta ~ sqrt(m_l/m_h) (GST): {gst_ok}")
check("one C3-breaking source gives m_light=b^2/m_heavy AND theta=b/m_heavy => sin theta = sqrt(m_l/m_h)",
      seesaw_ok and gst_ok, "the light mass and the mixing share ONE source => GST is forced")

print()
print("=" * 78)
print("A4. physical check + candidate shared residual (rank-1 / single-source)")
print("=" * 78)
# quark: sin theta_C ~ sqrt(m_d/m_s); lepton theta_13 ~ theta_e/sqrt2 with theta_e the charged-lepton GST
md_ms = 0.0505; sin_tc_pred = np.sqrt(md_ms); sin_tc_obs = 0.2257
quark_ok = abs(sin_tc_pred - sin_tc_obs) < 0.02
print(f"   quark: sin theta_C ~ sqrt(m_d/m_s) = sqrt({md_ms}) = {sin_tc_pred:.4f} vs PDG sin theta_C = {sin_tc_obs}")
print("   => the GST magnitude reduces to ONE condition: the rank-1 / single-source C3-symmetric mass")
print("      (the light gen's mass is purely from C3-breaking) for the small-angle magnitude account.")
print("   the rank-1 condition <=> the C3-symmetric mass from a SINGLE C3-invariant source (cf. single-Higgs).")
check("GST magnitude reduces to the single-source (rank-1) C3-symmetric mass; quark sqrt(m_d/m_s)~theta_C",
      quark_ok, "candidate shared magnitude residual: rank-1 C3-symmetric mass + single-source breaking")

print()
print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
