#!/usr/bin/env python3
"""Kill checks on the T45 attack (Claude Sonnet 5.5, same family as attacker).
K1  E ensemble: is the pi/2 entry special vs the discrete phases the repo itself uses (pi/3, 2pi/3), and which entry?
K2  Test A rerun on the lattice reading: O_h on the 6 arms of the cubic support (A1 + E + T1).
K3  Reframing bookkeeping: (w, r^2) <-> (alpha, R_u^2) is a change of variables; NLO protected-gamma vs right angle.
K4  Test B: a discrete pi/2 input phase gives a CKM delta that is not a rational multiple of pi anyway.
"""
import numpy as np
from math import pi, sqrt, acos, atan, degrees
rng = np.random.default_rng(2026)

# ------------------------------------------------------------------ K1
print("=" * 70, "\nK1  phase-of-one-entry scan (same ensemble as the attack)\n", "=" * 70)

def ens(N, phi_u, where="12", rngl=(-1.7, -0.6, -3.0, -1.2, -4.2, -2.2)):
    cl, ch, bl, bh, al, ah = rngl
    def sector():
        return (10 ** rng.uniform(al, ah, N), 10 ** rng.uniform(bl, bh, N), 10 ** rng.uniform(cl, ch, N), np.ones(N))
    def mk(A, B, C, D, ph, where):
        M = np.zeros((N, 3, 3), complex)
        M[:, 0, 1] = A; M[:, 1, 0] = A
        M[:, 1, 1] = B; M[:, 1, 2] = C; M[:, 2, 1] = C; M[:, 2, 2] = D
        if where == "12":
            M[:, 0, 1] = A * np.exp(1j * ph); M[:, 1, 0] = A * np.exp(-1j * ph)
        elif where == "23":
            M[:, 1, 2] = C * np.exp(1j * ph); M[:, 2, 1] = C * np.exp(-1j * ph)
        return M
    def diag(M):
        w, U = np.linalg.eigh(M); idx = np.argsort(np.abs(w), axis=1)
        return np.abs(np.take_along_axis(w, idx, 1)), np.take_along_axis(U, idx[:, None, :], 2)
    wu, Uu = diag(mk(*sector(), phi_u, where)); wd, Ud = diag(mk(*sector(), 0.0, "12"))
    V = np.conj(np.transpose(Uu, (0, 2, 1))) @ Ud; ab = np.abs(V)
    win = ((ab[:, 0, 1] > 0.15) & (ab[:, 0, 1] < 0.35) & (ab[:, 1, 2] > 0.02) & (ab[:, 1, 2] < 0.08)
           & (ab[:, 0, 2] > 0.001) & (ab[:, 0, 2] < 0.01)
           & (wu[:, 0] / wu[:, 1] < 0.1) & (wu[:, 1] / wu[:, 2] < 0.2)
           & (wd[:, 0] / wd[:, 1] < 0.3) & (wd[:, 1] / wd[:, 2] < 0.2))
    return V[win]

def alpha_gamma(V):
    g = np.angle(-V[:, 0, 0] * np.conj(V[:, 0, 2]) / (V[:, 1, 0] * np.conj(V[:, 1, 2])))
    a = np.angle(-V[:, 2, 0] * np.conj(V[:, 2, 2]) / (V[:, 0, 0] * np.conj(V[:, 0, 2])))
    return np.degrees(np.abs(a)), np.degrees(np.abs(g))

print("phase(deg)  n     frac|a-90|<5  frac|a-90|<10   med a   gamma p16/med/p84")
for ph in (30, 45, 60, 75, 90, 105, 120, 135):
    V = ens(600000, np.radians(ph))
    a, g = alpha_gamma(V)
    print("%7d %7d   %.3f         %.3f          %6.1f   %.1f / %.1f / %.1f" % (
        ph, len(a), np.mean(abs(a - 90) < 5), np.mean(abs(a - 90) < 10), np.median(a),
        np.percentile(g, 16), np.median(g), np.percentile(g, 84)))
print("\nphase on the up (2,3) entry instead of (1,2):")
for ph in (60, 90, 120):
    V = ens(600000, np.radians(ph), where="23")
    if len(V) == 0:
        print(ph, "no samples"); continue
    a, g = alpha_gamma(V)
    print("%7d %7d   frac|a-90|<5 %.3f   med a %.1f" % (ph, len(a), np.mean(abs(a - 90) < 5), np.median(a)))
print("\nnarrower magnitude ranges (each log-range shrunk by 1/2), phase pi/2 vs pi/3 vs 2pi/3:")
narrow = (-1.4, -0.9, -2.4, -1.8, -3.5, -2.9)
for ph in (60, 90, 120):
    V = ens(1500000, np.radians(ph), rngl=narrow)
    if len(V) == 0:
        print(ph, "no samples"); continue
    a, g = alpha_gamma(V)
    print("%7d %7d   frac|a-90|<5 %.3f   med a %.1f" % (ph, len(a), np.mean(abs(a - 90) < 5), np.median(a)))

# ------------------------------------------------------------------ K2
print("\n" + "=" * 70, "\nK2  Test A on the lattice reading: O_h on the 6 arms (+-x,+-y,+-z)\n", "=" * 70)
import itertools
arms = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
idx = {a:i for i,a in enumerate(arms)}
group = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product([1,-1], repeat=3):
        M = np.zeros((3,3));
        for i in range(3): M[i, perm[i]] = sg[i]
        P = np.zeros((6,6))
        for a in arms:
            b = tuple(int(x) for x in M @ np.array(a))
            P[idx[b], idx[a]] = 1
        group.append(P)
print("|O_h| =", len(group))
rows = [np.kron(P, np.eye(6)) - np.kron(np.eye(6), P.T) for P in group]
sv = np.linalg.svd(np.vstack(rows), compute_uv=False)
print("commutant dim of O_h on 6 arms:", int(np.sum(sv < 1e-10)), "(A1+E+T1 multiplicity one -> 3)")
u = np.ones(6) / sqrt(6)
PA1 = np.outer(u, u)
print("P_A1 commutes with every group element:", all(np.allclose(P @ PA1, PA1 @ P) for P in group))
print("diagonal of P_A1 (weight of any single arm on A1):", np.round(np.diag(PA1), 6), "= 1/6 =", 1/6)
print("=> Test A's own FAIL condition ('a covariant projector with a fractional diagonal entry') is met on this reading;")
print("   the attack tested only SU(2)xSU(3) on Q_L=(2,3).")

# ------------------------------------------------------------------ K3
print("\n" + "=" * 70, "\nK3  bookkeeping and NLO\n", "=" * 70)
def tri(w, r2):
    r = sqrt(r2); rho, eta = r * sqrt(w), r * sqrt(1 - w)
    v1 = np.array([-rho, -eta]); v2 = np.array([1 - rho, -eta])
    al = degrees(acos(v1 @ v2 / np.linalg.norm(v1) / np.linalg.norm(v2)))
    Ru2 = rho ** 2 + eta ** 2; Rt2 = (1 - rho) ** 2 + eta ** 2
    return al, Ru2, Rt2, degrees(acos(sqrt(w)))
worst = 0
for _ in range(2000):
    w, r2 = rng.uniform(0.05, 0.95), rng.uniform(0.05, 0.95)
    al, Ru2, Rt2, dl = tri(w, r2)
    # Pythagoras ⇔ alpha=90 ⇔ r2 = w
    worst = max(worst, abs((abs(al - 90) < 1e-9) - (abs(r2 - w) < 1e-12)))
print("alpha=90 iff r^2 = w (random (w,r^2) pairs, mismatches):", worst)
print("original phase target uses w only:            delta = arccos(sqrt(w))")
print("reframed target uses (alpha, R_u^2):          delta = arccos(R_u) if alpha = 90;  (w, r^2) <-> (alpha, R_u^2) is a 2-number change of variables")
al, Ru2, Rt2, dl = tri(1/6, 1/6)
print("atlas point: alpha=%.6f  R_u^2=%.6f  R_t^2=%.6f  R_t^2/R_u^2=%.6f  delta=%.6f" % (al, Ru2, Rt2, Rt2 / Ru2, dl))
alpha_s = (1/(4*pi))/sqrt(0.5934)
rb = (4 - alpha_s) / 24; eb = sqrt(5) * (4 - alpha_s) / 24
gam = degrees(np.arctan2(eb, rb)); Ru_bar = sqrt(rb**2 + eb**2)
al_bar = degrees(acos(((-rb)*(1-rb) + eb*eb) / sqrt((rb**2+eb**2)*((1-rb)**2+eb**2))))
print("repo NLO closure (CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA...): rho_bar=%.5f eta_bar=%.5f" % (rb, eb))
print("   gamma_bar=%.4f (protected)  alpha_bar=%.3f (drifts)  R_u_bar=%.5f  arccos(R_u_bar)=%.3f deg (vs gamma_bar %.3f)" % (
    gam, al_bar, Ru_bar, degrees(acos(Ru_bar)), gam))
print("=> 'gamma = arccos(R_u) from a right angle' is leading-order only; the repo's NLO structure protects gamma, not alpha.")

# ------------------------------------------------------------------ K4
print("\n" + "=" * 70, "\nK4  Test B: discrete input phase pi/2 -> CKM delta not a rational multiple of pi anyway\n", "=" * 70)
V = ens(600000, pi / 2)
# standard-parametrisation delta from |V_ub|, |V_us|, |V_cb|, |V_td|
ab = np.abs(V)
s13 = ab[:, 0, 2]; c13 = np.sqrt(1 - s13**2)
S12 = ab[:, 0, 1] / c13; S23 = ab[:, 1, 2] / c13
C12 = np.sqrt(1 - S12**2); C23 = np.sqrt(1 - S23**2)
cosd = (S12**2*S23**2 + C12**2*C23**2*s13**2 - ab[:, 2, 0]**2) / (2*S12*S23*C12*C23*s13)
d = np.degrees(np.arccos(np.clip(cosd, -1, 1)))
print("input Lagrangian phase = 90 deg exactly (rational multiple of pi).")
print("resulting standard-parametrisation delta over %d window samples: p16/median/p84 = %.1f / %.1f / %.1f deg" % (
    len(d), *np.percentile(d, [16, 50, 84])))
print("=> a rational-multiple-of-pi Lagrangian phase yields a continuum of delta; irrationality of delta/pi (Test B) does not exclude discrete-phase routes.")
