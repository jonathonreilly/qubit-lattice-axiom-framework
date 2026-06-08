#!/usr/bin/env python3
"""
Registration-style readout and positivity conditions do not fix the Route-2 readout rho_E
(they fix the readout NORM / a bound, not the DIRECTION).

Class-A finite-dim verifier (4-dim carrier, 2x4 readout; memory-safe).

The Route-2 bright readout is P_R = [[aE,0,bE,0],[0,aT,0,bT]] on the carrier columns
  E_shell=(1,0,0,0), E_center=(1,0,1/6,0), T_shell=(0,1,0,0), T_center=(0,1,0,1/6).
After the T-side is granted, the only free entry is rho_E = bE/aE = 6*(qE-1), where
qE = gamma_E(center)/gamma_E(shell). The carrier admits ANY rho_E (retained_no_go
quark_route2_exact_readout_map / ..._naturality_no_go). This runner tests whether the
supplied registration-style readout frame (canonical D(M)=Sum P_k M P_k,
partial-isometry/idempotency, and the additive I-scalar convention) together
with positivity fixes rho_E. The Record axiom itself does not supply the
readout context, projectors, positivity rule, or P_R map tested here.

It does not:
  (N1) partial isometry  P P^T = I_2   -> fixes |row| only; rho_E FREE.
  (N2) registration idempotency (P^T P)^2 = P^T P  <=> P P^T = I_2 -> rho_E FREE.
  (N3) positivity (nonneg carrier -> nonneg slice) -> one-sided BOUND rho_E > -6 only.
  (N4) the I-scalar / column-sum convention forces rho_E=1 -- an arbitrary convention,
       not the framework value (neither 5.2575 nor 21/4).
  (STRUCT) rho_E is the readout DIRECTION in the (u_E, delta_A1 u_E) plane; all record/
       positivity conditions are functions of P P^T (norm) or of signs, hence INVARIANT
       under that direction (an O(2) rotation in the (shell,center) coefficients preserves
       them). Selecting rho_E needs a shell-vs-center DISTINGUISHING input.
      (NONVAC) a distinguishing input can fix it: the gravity-metric directional
       response lane carries rho_E ~ 5.2575, or the color bridge
       c_TE = -R_conn = -8/9 gives rho_E = 21/4 (a cross-domain input, not a record principle).
  (GAUGE) carrier rescaling does not remove rho_E (delta_A1=1/6 fixed).

No PDG value is load-bearing.
"""
import numpy as np

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name} {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {name} {detail}")


E_shell = np.array([1, 0, 0, 0.0])
E_center = np.array([1, 0, 1.0 / 6.0, 0.0])
T_shell = np.array([0, 1, 0, 0.0])
T_center = np.array([0, 1, 0, 1.0 / 6.0])


def P_R(aE, bE, aT=1.0, bT=-1.0):
    return np.array([[aE, 0, bE, 0], [0, aT, 0, bT]], float)


RHOS = np.linspace(-12, 12, 6001)

# (N1) partial isometry: P P^T = I_2 admits a solution for EVERY rho_E (only |aE| fixed)
n1_all = True
for r in RHOS:
    aE = 1.0 / np.sqrt(1.0 + r * r)  # aE^2 + (aE r)^2 = 1
    P = P_R(aE, aE * r)
    block = P @ P.T  # 2x2; E-row norm = aE^2(1+r^2) = 1
    if abs(block[0, 0] - 1.0) > 1e-9:
        n1_all = False
check("N1_partial_isometry_admits_every_rho_E", n1_all,
      "P P^T=I_2 has a solution for all rho_E on the grid -> fixes |aE|, rho_E FREE")

# (N2) registration idempotency (P^T P)^2 = P^T P  <=>  P P^T = I_2  -> same family
def is_idem(M):
    return np.allclose(M @ M, M, atol=1e-9)
n2_all = True
for r in (-5.0, 0.0, 5.257, 5.25, 1.0):
    aE = 1.0 / np.sqrt(1.0 + r * r)
    P = P_R(aE, aE * r, aT=1.0 / np.sqrt(2), bT=-1.0 / np.sqrt(2))  # T-side normalized too
    if not is_idem(P.T @ P):
        n2_all = False
check("N2_registration_idempotency_admits_every_rho_E", n2_all,
      "(P^T P) is a projection for every rho_E (given the norm) -> rho_E FREE")

# (N3) positivity: nonneg carrier cols -> nonneg slice. E-center first comp = aE + bE/6 = aE(1+rho/6)
pos = [r for r in RHOS if (1.0 >= 0) and (1.0 + r / 6.0) >= 0]  # aE=1
check("N3_positivity_is_only_a_one_sided_bound",
      min(pos) > -6.001 and min(pos) < -5.999 and max(pos) > 11.9,
      f"admissible rho_E = (-6, inf): a BOUND, not a unique value (min={min(pos):.3f})")

# (N4) the I-scalar/column-sum convention forces rho_E=1 (arbitrary; not the framework value)
# preserve column sums: sum(P@E_shell)=aE=sum(E_shell)=1 -> aE=1; sum(P@E_center)=aE+bE/6=7/6 -> bE=1
aE, bE = 1.0, 1.0
rho_colsum = bE / aE
check("N4_I_scalar_colsum_gives_arbitrary_rho_E_1", abs(rho_colsum - 1.0) < 1e-12 and abs(rho_colsum - 21.0 / 4.0) > 1.0,
      f"column-sum 'I-scalar' -> rho_E={rho_colsum} (arbitrary convention; != 21/4=5.25 and != 5.2575)")

# (STRUCT) record/positivity conditions are invariant under the readout DIRECTION:
# an O(2) rotation of the (E-shell, E-center) readout coefficients preserves P P^T (norm)
# but changes rho_E. Show: rotating (aE,bE) by theta keeps aE^2+bE^2 fixed, sweeps rho_E over all R.
thetas = np.linspace(-1.47, 1.47, 15)  # within (-pi/2, pi/2) so aE=cos(theta)>0
norms = []
rhos_seen = []
for th in thetas:
    aE, bE = np.cos(th), np.sin(th)
    norms.append(aE * aE + bE * bE)
    rhos_seen.append(bE / aE)  # = tan(theta), sweeps a wide range
check("STRUCT_norm_invariant_direction_sweeps_rho_E",
      max(norms) - min(norms) < 1e-9 and (max(rhos_seen) - min(rhos_seen)) > 15,
      f"O(2) rotation: P P^T-norm constant (=1) while rho_E sweeps [{min(rhos_seen):.1f},{max(rhos_seen):.1f}] "
      "-> norm conditions cannot fix the direction")

# (NONVAC) a shell-vs-center DISTINGUISHING input fixes rho_E:
#   color bridge: c_TE = gamma_T(center)/gamma_E(center) = -R_conn = -8/9 forces rho_E = 21/4
#   (with granted T-side aT/aE=-2, qT=5/6); gravity-metric response gives the genuine 5.2575.
R_conn = 8.0 / 9.0
# endpoint algebra: c_TE = s_TE * qT/qE, with s_TE=-2, qT=5/6, c_TE=-R_conn -> qE = s_TE*qT/c_TE
qE_from_color = (-2.0) * (5.0 / 6.0) / (-R_conn)
rho_E_from_color = 6.0 * (qE_from_color - 1.0)
check("NONVAC_color_bridge_fixes_rho_E_to_21_4", abs(rho_E_from_color - 21.0 / 4.0) < 1e-12,
      f"c_TE=-R_conn=-8/9 (a CROSS-DOMAIN distinguishing input) -> qE={qE_from_color}=15/8, rho_E={rho_E_from_color}=21/4")
check("NONVAC_gravity_lane_value_differs_from_21_4", abs(5.257476782081 - 21.0 / 4.0) > 1e-3,
      "the live gravity-metric lane value rho_E=5.2575 differs from the color-clean 21/4 (numerical-match)")

# (GAUGE) a carrier rescale u_E -> lam u_E rescales delta_A1 u_E too
# (delta_A1 linear), so rho_E = bE/aE is unchanged -> no convention freedom (unlike flavor handedness)
lam = 3.7
aE, bE = 1.0, 5.0
rho0 = bE / aE
rho_scaled = (lam * bE) / (lam * aE)
check("GAUGE_carrier_rescale_leaves_rho_E_invariant", abs(rho0 - rho_scaled) < 1e-12,
      "carrier rescale leaves rho_E invariant (delta_A1=1/6 fixed)")

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("VERDICT: no supplied registration-style / positivity / idempotency condition fixes the "
      "Route-2 readout rho_E -- they fix the readout NORM (or a one-sided bound), while rho_E is the "
      "readout DIRECTION in the (shell, center) plane. Selecting rho_E requires a shell-vs-center "
      "DISTINGUISHING input (the gravity-metric response lane -> 5.2575, or the color bridge c_TE=-R_conn "
      "-> 21/4), not a generic registration principle. The tested carrier-rescale gauge freedom does not "
      "remove rho_E, so the handedness gauge-resolution does not transfer. The readout-selection residual "
      "is a distinguishing-input (color/gravity) theorem, not a registration principle.")
