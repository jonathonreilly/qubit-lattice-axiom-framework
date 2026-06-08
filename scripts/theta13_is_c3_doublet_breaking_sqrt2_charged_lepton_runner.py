"""
theta_13 is the C3-DOUBLET-degeneracy breaking measure; the trimaximal geometry forces
sin(theta_13) = sin(theta_e)/sqrt(2), with theta_e the charged-lepton correction (the residual).

The neutrino records einselect the C3 SINGLET (1,1,1)/sqrt3 = the trimaximal 2nd PMNS column
(the active-sector sieve; pmns_tm2_trimaximal_column..., pmns_tm2_magnitudes_conditional_bounded).
The C3 DOUBLET (1st + 3rd columns) is 2-fold DEGENERATE under a C3-invariant einselection
(flavor_einselection_2sector_modulo_kreality), so the doublet ROTATION -- i.e. theta_13 -- is NOT
fixed by the neutrino records (the existing notes: "does not predict sin^2 theta_13"). theta_13 != 0
is therefore a direct measure of C3-doublet breaking, sourced by the charged-lepton correction.

This runner LOCATES theta_13 and DERIVES the sqrt(2):
- the C3 singlet + the real doublet basis {(2,-1,-1)/sqrt6, (0,1,-1)/sqrt2} IS the TBM form;
- a charged-lepton 1-2 rotation by theta_e gives, exactly, |U_e3| = sin(theta_e)/sqrt(2)
  -- the sqrt(2) is the normalization of the C3-doublet imaginary basis vector (0,1,-1)/sqrt2;
- the observed theta_13 = 8.57deg then implies theta_e = 12.16deg ~ the Cabibbo angle 13.04deg
  (quark-lepton-complementarity-consistent).

So theta_13 moves from "no prediction / free" to "= theta_e/sqrt2" with the sqrt(2) DERIVED and
theta_e the residual DIMENSIONLESS input (the charged-lepton/Cabibbo-sized rotation).

Memory-safe: 3x3 matrices. Class-A. TOTAL: PASS=N FAIL=0 expected.
"""
import numpy as np

PASS = 0; FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ""))
    return ok

# PDG / NuFit central values
SIN2_T13_OBS = 0.02220        # sin^2(theta_13)
THETA_C_DEG = 13.04           # Cabibbo angle
w = np.exp(2j*np.pi/3)

print("=" * 78)
print("A1. the C3 structure (singlet + real doublet basis) IS the TBM form (trimaximal 2nd column)")
print("=" * 78)
s = np.array([1, 1, 1]) / np.sqrt(3)            # C3 SINGLET = the records-einselected trimaximal column
d1 = np.array([2, -1, -1]) / np.sqrt(6)         # C3 doublet, real part
d2 = np.array([0, 1, -1]) / np.sqrt(2)          # C3 doublet, imaginary part  (the sqrt2)
U_TBM = np.column_stack([d1, s, d2])            # columns 1, 2(=trimaximal), 3
orthonormal = np.allclose(U_TBM.T @ U_TBM, np.eye(3))
trimax_col = np.allclose(np.abs(U_TBM[:, 1])**2, 1/3)
# d1,d2 are real combinations of the C3 doublet eigenvectors (1,w,w^2)/sqrt3, (1,w^2,w)/sqrt3:
dp = np.array([1, w, w**2]) / np.sqrt(3); dm = np.array([1, w**2, w]) / np.sqrt(3)
doublet_from_C3 = np.allclose(np.abs(np.real((dp+dm)/np.sqrt(2))), np.abs(d1)) or \
                  np.allclose(sorted(np.abs((dp+dm)/np.sqrt(2))), sorted(np.abs(d1)))
print(f"   orthonormal: {orthonormal}; 2nd column trimaximal |U_x2|^2=1/3: {trimax_col}")
print(f"   doublet basis = real/imag parts of the C3 doublet eigenvectors (1,w,w^2),(1,w^2,w): {doublet_from_C3}")
check("the C3 singlet + real doublet basis is the TBM form with the trimaximal 2nd column",
      orthonormal and trimax_col, "the framework's C3 structure (records-einselected)")

print()
print("=" * 78)
print("A2. the C3 doublet is DEGENERATE under C3-invariant einselection => theta_13 unfixed by nu records")
print("=" * 78)
# a C3-invariant Hermitian operator is a real circulant a I + b(C + C^2); eigenvalues:
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], float)
a, b = 1.3, 0.4
H = a*np.eye(3) + b*(C + C.T)                   # C3-invariant (C + C^2 = C + C^T here)
ev = np.sort(np.linalg.eigvalsh(H))
doublet_degenerate = np.isclose(ev[0], ev[1])   # two eigenvalues equal => 2-fold doublet
singlet_isolated = not np.isclose(ev[1], ev[2])
print(f"   C3-invariant H eigenvalues = {np.round(ev,4)} -> doublet 2-fold degenerate: {doublet_degenerate}")
print("   so the records resolve the singlet (trimaximal column) but NOT the doublet rotation => theta_13 free")
check("C3-invariant einselection leaves the doublet degenerate => theta_13 (doublet rotation) unfixed",
      doublet_degenerate and singlet_isolated, "theta_13 != 0 is a MEASURE of C3-doublet breaking")

print()
print("=" * 78)
print("A3. a charged-lepton 1-2 rotation theta_e gives EXACTLY sin(theta_13) = sin(theta_e)/sqrt(2)")
print("=" * 78)
def R12(t):
    c, sn = np.cos(t), np.sin(t)
    return np.array([[c, sn, 0], [-sn, c, 0], [0, 0, 1]])
sqrt2_exact = True
for te_deg in (13.04, 12.16, 9.0, 5.0):
    te = np.radians(te_deg)
    PMNS = R12(te).T @ U_TBM                     # PMNS = U_e^dag U_nu  (U_e = 1-2 rotation)
    s13 = abs(PMNS[0, 2])                         # |U_e3| = sin(theta_13)
    if not np.isclose(s13, np.sin(te)/np.sqrt(2)):
        sqrt2_exact = False
print(f"   |U_e3| = sin(theta_e)/sqrt(2) for all tested theta_e: {sqrt2_exact}")
print("   the sqrt(2) is the norm of the C3-doublet imaginary basis vector (0,1,-1)/sqrt2 (column 3)")
check("the trimaximal geometry forces sin(theta_13) = sin(theta_e)/sqrt(2) (the sqrt2 is DERIVED)",
      sqrt2_exact, "theta_13 = theta_e/sqrt2 to leading order; theta_e = the charged-lepton residual")

print()
print("=" * 78)
print("A4. observed theta_13 => theta_e = 12.16deg ~ Cabibbo (13.04deg): QLC-consistent")
print("=" * 78)
s13_obs = np.sqrt(SIN2_T13_OBS)
te_implied_deg = np.degrees(np.arcsin(np.sqrt(2) * s13_obs))
# forward: theta_e = Cabibbo -> predicted theta_13
te_c = np.radians(THETA_C_DEG)
s13_pred = np.sin(te_c) / np.sqrt(2)
sin2_pred = s13_pred**2
print(f"   observed sin^2(theta_13) = {SIN2_T13_OBS} (theta_13 = {np.degrees(np.arcsin(s13_obs)):.2f}deg)")
print(f"   => implied theta_e = arcsin(sqrt2 * sin theta_13) = {te_implied_deg:.2f}deg  (Cabibbo = {THETA_C_DEG}deg)")
print(f"   forward (theta_e = Cabibbo): predicted sin^2(theta_13) = {sin2_pred:.4f} vs observed {SIN2_T13_OBS} "
      f"(angle {np.degrees(np.arcsin(s13_pred)):.2f}deg vs {np.degrees(np.arcsin(s13_obs)):.2f}deg)")
qlc_consistent = abs(te_implied_deg - THETA_C_DEG) < 1.5   # within ~1 deg of Cabibbo
check("observed theta_13 implies theta_e ~ Cabibbo (QLC-consistent); sqrt2 derived, theta_e the residual",
      qlc_consistent, "theta_13 = theta_e/sqrt2 with theta_e ~ 12.2deg ~ theta_C; the residual is dimensionless")

print()
print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
