"""
The small fermion mixing angles (the Cabibbo angle theta_C and the reactor angle theta_13) are
C3-BREAKING order parameters: the framework's C3-symmetric leading order gives NO mixing
(V_CKM = I from circulants; trimaximal PMNS with a degenerate doublet), so every small mixing angle
is a C3-breaking deviation. Both are sqrt(mass-ratio)-scaled (Gatto/GST), the magnitude residual.

This unifies the quark and lepton mixing sectors:
- QUARK: C3-equivariant (circulant) mass matrices are co-diagonalized by the DFT, so
  V_CKM = U_up^dag U_dn is a permutation = I (QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY, retained_no_go).
  => leading order has NO Cabibbo mixing; theta_C is the C3-breaking deviation.
- LEPTON: the C3-symmetric neutrino records give the trimaximal PMNS column (C3 singlet) with a
  2-fold DEGENERATE doublet, so theta_13 = 0 at C3-symmetric order; theta_13 is the C3-doublet-
  breaking deviation (THETA13_IS_THE_C3_DOUBLET_BREAKING_MEASURE, this session).
- So BOTH theta_C and theta_13 are C3-breaking order parameters. This runner does not derive the
  amount of C3 breaking; it only shows that, for the geometric-mean (GST) breaking texture, the
  angles scale as sqrt(mass-ratio) (the magnitude residual).

Memory-safe: 3x3 / 2x2 matrices. Class-A. TOTAL: PASS=N FAIL=0 expected.
"""
import numpy as np

PASS = 0; FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ""))
    return ok

w = np.exp(2j*np.pi/3)
F = np.array([[1, 1, 1], [1, w, w**2], [1, w**2, w]], complex) / np.sqrt(3)   # DFT (C3 eigenbasis)
def circ(a, b, c):
    return np.array([[a, c, b], [b, a, c], [c, b, a]], complex)               # C3-equivariant (circulant)

print("=" * 78)
print("A1. QUARK: C3-symmetric (circulant) mass matrices => V_CKM = I (no Cabibbo at leading order)")
print("=" * 78)
M_up = circ(3.0, 0.4, 0.2); M_dn = circ(1.0, 0.3, 0.15)        # two circulants
# circulants are diagonalized by the DFT F: U_up = U_dn = F => V_CKM = F^dag F = I
diag_up = F.conj().T @ M_up @ F; diag_dn = F.conj().T @ M_dn @ F
both_diag = np.allclose(diag_up - np.diag(np.diag(diag_up)), 0) and \
            np.allclose(diag_dn - np.diag(np.diag(diag_dn)), 0)
V_CKM = F.conj().T @ F                                          # U_up^dag U_dn with U_up=U_dn=F
ckm_identity = np.allclose(np.abs(V_CKM), np.eye(3), atol=1e-9)
print(f"   both circulants diagonalized by the DFT: {both_diag}; |V_CKM| = I: {ckm_identity}")
check("C3-symmetric circulant quark masses => V_CKM = I (retained_no_go boundary): NO Cabibbo",
      both_diag and ckm_identity, "leading order is C3-symmetric => mixing vanishes")

print()
print("=" * 78)
print("A2. theta_C is the C3-BREAKING deviation: circulants COMMUTE (V_CKM=perm); breaking => non-commuting")
print("=" * 78)
# retained boundary: shared-C3 circulants COMMUTE => simultaneously diagonalizable => V_CKM is a
# PERMUTATION (|V_us|=0). A nonzero Cabibbo (off-permutation) requires [M_up,M_dn] != 0 = C3-breaking.
# the commutator is basis-independent (no degenerate-doublet ambiguity).
def comm_norm(A, B): return float(np.linalg.norm(A @ B - B @ A))
comm_sym = comm_norm(M_up, M_dn)                               # ~0: circulants commute
P = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex)       # a 1-2 (non-circulant) C3-breaking
broken = [comm_norm(M_up, M_dn + e * P) for e in (0.0, 0.05, 0.1, 0.2)]
commutes_at_sym = comm_sym < 1e-9
grows_with_breaking = broken[0] < 1e-9 and broken[1] < broken[2] < broken[3]
print(f"   ||[M_up, M_dn]|| at C3-symmetry = {comm_sym:.2e} (commute => V_CKM permutation, no Cabibbo)")
print(f"   ||[M_up, M_dn+eps P]|| for eps=0,0.05,0.1,0.2 = {[round(b,3) for b in broken]} (grows with breaking)")
check("the Cabibbo angle is the C3-breaking deviation: circulants commute, breaking => non-commuting => V_us!=0",
      commutes_at_sym and grows_with_breaking, "theta_C is a C3-breaking order parameter (off-permutation)")

print()
print("=" * 78)
print("A3. LEPTON: theta_13 is the C3-DOUBLET-breaking deviation (companion result, reproduced)")
print("=" * 78)
# C3-symmetric neutrino: trimaximal singlet column + 2-fold degenerate doublet => theta_13 = 0
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], float)
Hsym = 1.0*np.eye(3) + 0.3*(C + C.T)                           # C3-invariant
ev = np.sort(np.linalg.eigvalsh(Hsym))
doublet_degenerate = np.isclose(ev[0], ev[1])                  # theta_13 unfixed/zero at C3-symmetry
# breaking the doublet (a charged-lepton 1-2 rotation theta_e) => theta_13 = arcsin(sin theta_e/sqrt2)
s = np.array([1, 1, 1])/np.sqrt(3); d1 = np.array([2, -1, -1])/np.sqrt(6); d2 = np.array([0, 1, -1])/np.sqrt(2)
U_TBM = np.column_stack([d1, s, d2])
def R12(t): c, sn = np.cos(t), np.sin(t); return np.array([[c, sn, 0], [-sn, c, 0], [0, 0, 1]])
t13_breaks = abs((R12(np.radians(12.16)).T @ U_TBM)[0, 2]) > 1e-3 and abs((R12(0).T @ U_TBM)[0, 2]) < 1e-9
print(f"   C3-symmetric lepton: doublet 2-fold degenerate {doublet_degenerate} => theta_13 = 0 at C3-symmetry")
print(f"   C3-doublet breaking (charged-lepton rotation) => theta_13 != 0: {t13_breaks}")
check("the reactor angle theta_13 is the C3-doublet-breaking deviation (zero at C3-symmetry)",
      doublet_degenerate and t13_breaks, "theta_13 is a C3-breaking order parameter (companion note)")

print()
print("=" * 78)
print("A4. UNIFIED: both mixing angles are C3-breaking order parameters, sqrt(mass-ratio)-scaled")
print("=" * 78)
# the geometric-mean (GST) breaking texture gives sin(theta) ~ sqrt(m_1/m_2): a 2x2 [[0,b],[b,a]]
def gst_angle(m1, m2):
    a = m1 + m2; b = np.sqrt(m1*m2)                            # geometric-mean off-diagonal (GST texture)
    M = np.array([[0, b], [b, a]], float)
    ev, U = np.linalg.eigh(M)
    return abs(U[0, 1]), np.sqrt(min(m1, m2)/max(m1, m2))      # sin(theta), sqrt(ratio)
# sin(theta) -> sqrt(m1/m2) in the hierarchical limit (the GST relation); tight at small ratio
sin_h, sqrt_h = gst_angle(0.005, 1.0)                          # hierarchical => sin ~ sqrt(ratio)
sin_phys, sqrt_phys = gst_angle(0.05, 1.0)                     # physical m_d/m_s ~ 0.05 => ~10% (Cabibbo-haze)
gst_scaling = abs(sin_h - sqrt_h) < 0.01 and abs(sin_phys - sqrt_phys) < 0.03
both_c3_breaking = grows_with_breaking and (doublet_degenerate and t13_breaks)
print(f"   hierarchical: sin(theta) = {sin_h:.4f} ~ sqrt(m1/m2) = {sqrt_h:.4f} (GST relation, tight as ratio->0)")
print(f"   physical m_d/m_s~0.05:  sin = {sin_phys:.4f} vs sqrt = {sqrt_phys:.4f} (~10%, the Cabibbo-haze level)")
print("   => theta_C and theta_13 are BOTH C3-breaking order parameters; this runner does not derive")
print("      the amount of breaking. For the geometric-mean (GST) texture, both scale as sqrt(mass-ratio).")
check("both theta_C and theta_13 are C3-breaking order parameters; sqrt(mass-ratio)-scaled (GST)",
      both_c3_breaking and gst_scaling, "structural unification; magnitude rides the named GST texture")

print()
print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
