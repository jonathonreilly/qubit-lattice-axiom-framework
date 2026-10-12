"""C5 R11-5 checks: regulated preferred-frame CQ kernel (R9-4 variant iv).
Sections:
 [1] explicit dilation: bipartite (QND) resonator-chain meter; quantum limit at every w; chi_FF = 0; backaction falloff
 [2] cone lemma: D0' + c^2 M >= c|F|/|s| under (H-T); 1/|s| not locally integrable
 [3] finite-age regulator: free-GW energy after time T for P_J ~ |u|^alpha near the cone (linear / log / bounded)
 [4] UV: vacuum photon-pair energy injection converges iff backaction falls faster than w^-6 (total)
 [5] moving matter: K(k.v, k)/K(0,k) at v = CMB-frame speed; annual modulation; no O(beta) term
 [6] PPN / lag numbers for the mean field
 [7] cosmological GW content: bounded-D0' kernel (secular, linear) and log option (finite age)
 [8] window arithmetic
Subtractions named (TESTS rule): every decay/tail statement below is of a positive integrand; no channel limit is
subtracted anywhere ("subtraction: none").
"""
import math
import numpy as np
from scipy import integrate

rng = np.random.default_rng(1155)
hbar = 1.054571817e-34; c = 2.99792458e8; G = 6.67430e-11
lP2 = G*hbar/c**3
tH = 4.35e17                      # s (RECALLED, ~1/H0)
rho_crit = 8.5e-27*c**2           # J/m^3 (RECALLED)
rho_L = 0.69*rho_crit

# ------------------------------------------------------------------ [1]
print("[1] bipartite resonator-chain meter (rotating frame, resonant): H = lam*A*X1 + g*sum(XjXj+1 + PjPj+1); mode N leaks at kappa")
def chain_response(N, g, kappa, w):
    # state v = (X1,P1,...,XN,PN); inputs u = (Xin, Pin, A); hbar = 1, [X,P] = i
    M = np.zeros((2*N, 2*N)); B = np.zeros((2*N, 3))
    for j in range(N):
        X, P = 2*j, 2*j+1
        for nb in (j-1, j+1):
            if 0 <= nb < N:
                M[X, 2*nb+1] += g      # dX_j/dt = g (P_{j-1} + P_{j+1})
                M[P, 2*nb] -= g        # dP_j/dt = -g (X_{j-1} + X_{j+1})
    M[2*N-2, 2*N-2] -= kappa/2; M[2*N-1, 2*N-1] -= kappa/2
    B[2*N-2, 0] = math.sqrt(kappa); B[2*N-1, 1] = math.sqrt(kappa)
    B[1, 2] = -1.0                      # dP1/dt = ... - lam*A  (lam = 1 here)
    R = np.linalg.solve(-1j*w*np.eye(2*N) - M, B)
    # output X quadrature: Xout = Xin - sqrt(kappa) X_N
    out = np.array([1.0, 0.0, 0.0]) - math.sqrt(kappa)*R[2*N-2, :]
    X1 = R[0, :]
    return out, X1
N, g, kappa = 4, 1.0, 1.0
print(f"    N={N}, g={g}, kappa={kappa}; vacuum inputs with S_XinXin = S_PinPin = 1/2 (symmetrized), uncorrelated")
worst = 0.0; chiFF = 0.0
for w in [0.0, 0.1, 0.5, 1.0, 2.0, 5.0, 20.0, 100.0]:
    out, X1 = chain_response(N, g, kappa, w)
    S_II = 0.5*(abs(out[0])**2 + abs(out[1])**2)       # record noise
    gain = out[2]                                       # dI/dA
    S_FF = 0.5*(abs(X1[0])**2 + abs(X1[1])**2)          # backaction X1 noise (lam = 1)
    chiFF = max(chiFF, abs(X1[2]))                      # response of X1 to A: dynamical backaction
    ratio = S_II*S_FF/(abs(gain)**2/4) if abs(gain) > 0 else float('nan')
    worst = max(worst, abs(ratio-1))
    print(f"    w={w:7.2f}: S_II={S_II:.6f}  S_FF={S_FF:.3e}  |gain|^2={abs(gain)**2:.3e}  S_II*S_FF/(|gain|^2/4)={ratio:.9f}")
print(f"    max |ratio-1| = {worst:.2e} (quantum limit saturated at every w); max |dX1/dA| = {chiFF:.1e} (chi_FF = 0: no friction, symmetric backaction)")
ws = np.array([1e2, 1e3])
SF = []
for w in ws:
    _, X1 = chain_response(N, g, kappa, w); SF.append(0.5*(abs(X1[0])**2+abs(X1[1])**2))
print(f"    backaction falloff exponent d ln S_FF/d ln w at w~1e2-1e3: {math.log(SF[1]/SF[0])/math.log(10):.3f} (expect -2N = {-2*N})")
print("    subtraction: none (S_FF is a positive spectral density)")

# ------------------------------------------------------------------ [2]
print("\n[2] cone lemma: (H-T) P_J D0' >= |F|^2/4, M = |G_R|^2 P_J = P_J/s^2  =>  D0' + c^2 M >= c|F|/|s|")
worst = np.inf
for _ in range(20000):
    s = rng.choice([-1, 1])*10**rng.uniform(-8, 4)
    F = 10**rng.uniform(-3, 0); cc = 10**rng.uniform(-3, 3)
    PJ = 10**rng.uniform(-10, 10); D0p = F**2/(4*PJ)*(1+10**rng.uniform(-6, 3))
    M = PJ/s**2
    worst = min(worst, (D0p + cc**2*M)/(cc*F/abs(s)))
print(f"    min (D0' + c^2 M)/(c|F|/|s|) over 20000 draws = {worst:.6f} (>= 1)")
for d in [1e-2, 1e-4, 1e-8, 1e-16]:
    print(f"    int_(d<|s|<1) ds/|s| = {2*math.log(1/d):.2f} at d={d:.0e}  (diverges: not locally finite)")

# ------------------------------------------------------------------ [3]
print("\n[3] finite-age regulator: free (on-shell) GW energy after time T, E(T) = int du P_J(u) sin^2(uT/2)/u^2 (per mode, unit slope)")
def E_T(alpha, T, U=1.0):
    f = lambda u: (u**alpha)*math.sin(u*T/2)**2/u**2
    pts = np.unique(np.concatenate([[0.0], np.linspace(0, U, 2001)]))
    tot = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        tot += integrate.quad(f, a, b, limit=200)[0]
    return 2*tot   # both signs of u
for alpha in [0.0, 1.0, 2.0]:
    vals = [E_T(alpha, T) for T in [1e1, 1e2, 1e3]]
    print(f"    alpha={alpha:.0f}: E(T=1e1,1e2,1e3) = {vals[0]:.4f}, {vals[1]:.4f}, {vals[2]:.4f}")
print("    alpha=0 (P_J(cone)>0, D0' bounded): linear in T;  alpha=1: + ln T per decade (ln 10 = 2.3026 x slope);")
print("    alpha=2: saturates (but then D0' ~ 1/u^2: matter null-transfer decoherence grows ~ T)")
print("    subtraction: none (positive integrand; no channel limit subtracted)")

# ------------------------------------------------------------------ [4]
print("\n[4] UV: vacuum photon-pair energy injection ~ int dw w * Dtot(w) * W(s), W ~ s^2 ~ w^4, spatial k cut at 1/l")
for m in [2, 3, 4]:
    f = lambda w: w*w**4/(1+w**2)**m * 1.0
    vals = [integrate.quad(f, 0, L, limit=400)[0] for L in [1e1, 1e2, 1e3, 1e4]]
    print(f"    Dtot ~ (1+w^2)^-{m}: injection up to 1e1..1e4 = " + ", ".join(f"{v:.4g}" for v in vals))
print("    => converges iff total backaction falloff faster than w^-6 (m >= 4; equivalently 1/|s| x (1+w^2 tau^2)^-n with n >= 3)")
print("    the chain meter of [1] gives w^-2N: N >= 4 stages; subtraction: none")

# ------------------------------------------------------------------ [5]
print("\n[5] moving matter: lab static kernel K_lab(0,k) = K_frame(k.v, k); K = cN |F_u|^2/|s|, F_u = e^{-k^2l^2/2}(1+w^2 tau^2)^{-n/2}, tau=l/c")
beta = 369.82e3/c; beta_orb = 29.78e3/c
# CMB dipole direction (Planck 2018: l=264.021, b=48.253) -> ecliptic latitude
lg, bg = math.radians(264.021), math.radians(48.253)
vg = np.array([math.cos(bg)*math.cos(lg), math.cos(bg)*math.sin(lg), math.sin(bg)])
# Galactic -> ICRS (J2000) rotation matrix (standard, Hipparcos)
Rgi = np.array([[-0.0548755604, +0.4941094279, -0.8676661490],
                [-0.8734370902, -0.4448296300, -0.1980763734],
                [-0.4838350155, +0.7469822445, +0.4559837762]])
veq = Rgi @ vg   # Rgi as written is A_G^T (A_G maps ICRS->Gal), so this maps Gal->ICRS
ra, dec = math.degrees(math.atan2(veq[1], veq[0])) % 360, math.degrees(math.asin(veq[2]))
eps = math.radians(23.4392911)
vecl = np.array([veq[0], math.cos(eps)*veq[1]+math.sin(eps)*veq[2], -math.sin(eps)*veq[1]+math.cos(eps)*veq[2]])
blat = math.degrees(math.asin(vecl[2]))
print(f"    beta_CMB = {beta:.6e} (v = 369.82 km/s, web-checked); dipole RA,Dec = {ra:.2f},{dec:.2f} deg (RECALLED value ~167.9,-6.9); ecliptic latitude = {blat:.2f} deg")
def Kratio(kl, b, n=3, cos=None):
    # average over direction cos(theta) between k and v of K(k v cos, k)/K(0,k)
    def r(mu):
        w_over_ck = b*mu                       # w = k v mu
        s_ratio = abs((w_over_ck)**2 - 1)      # |s|/(c^2k^2)
        temp = (1 + (kl*w_over_ck)**2)**(-n)   # (w tau)^2 = (k l v mu / c)^2
        return temp/s_ratio
    if cos is not None:
        return r(cos)
    return 0.5*integrate.quad(r, -1, 1)[0]
for kl in [0.1, 1.0, 3.0]:
    d0 = Kratio(kl, beta) - 1
    dmax = Kratio(kl, beta, cos=1.0) - 1
    print(f"    k*l={kl:4.1f}: direction-averaged dK/K = {d0:+.3e}; along v: {dmax:+.3e}  (beta^2 = {beta**2:.3e})")
# annual modulation of |v|: v(t) = v_CMB + v_orb(t), v_orb in ecliptic plane
proj = beta_orb*math.cos(math.radians(blat))
b_hi, b_lo = beta + proj, beta - proj
amp = 0.5*((Kratio(1.0, b_hi, cos=1.0)-1) - (Kratio(1.0, b_lo, cos=1.0)-1))
print(f"    annual: max projection of v_orb on dipole = {proj*c/1e3:.2f} km/s; modulation amplitude of dK/K (k*l=1, along v) = {amp:.3e}")
print("    odd-in-w terms: K_frame is even in w (classical record noise symmetric; chi_FF = 0 so backaction symmetric) => no O(beta) term")
print("    subtraction: dK/K is measured against the same kernel at v = 0 (subtraction: the rest-frame static kernel)")

# ------------------------------------------------------------------ [6]
print("\n[6] mean field: h = G_R F_u <T>; moving source (velocity w) sees F_u(k.w, k) = e^{-k^2l^2/2}(1 - i k.w tau)^-n")
AU = 1.496e11
for l in [1e-8, 2e-7, 5e-6]:
    tau = l/c
    lag = 3*tau
    disp = 369.82e3*lag
    corr = 3*beta*l/AU
    print(f"    l={l:.0e} m: lag n*tau = {lag:.2e} s; frame-velocity displacement = {disp:.2e} m; dipole correction at 1 AU ~ n beta l/r = {corr:.1e}")
print("    PPN alpha1, alpha2 bounds (web-checked): |alpha1-hat| < ~4e-5 (PSR J1738+0333, Shao & Wex 2012); |alpha2-hat| < 1.6e-9 (Shao et al. 2013)")
print("    mean-field alpha1 = alpha2 = 0 at r >> l (F_u -> 1 as k -> 0 for every w); corrections O(beta l/r) are short-range, not 1/r PPN terms")

# ------------------------------------------------------------------ [7]
print("\n[7] cosmological GW content (order of magnitude; Isaacson premise; O(1) tensor weights)")
# (a) bounded D0' (as in [1]-built kernel with static least-decoherence D0'): P_J(cone) = static value hbar k^2 |g|^2/(8 pi G) per mass-density unit
#     drho/dt ~ (8 pi G/c^2) * 2 pol * int d^3k/(2pi)^3 c^4 P_J(ck,k) = 2 hbar c^2 int d^3k/(2pi)^3 k^2 e^{-k^2 l^2}
coef = 2/(2*math.pi**2)*(3*math.sqrt(math.pi)/8)   # int k^4 e^{-k^2 l^2} dk = 3 sqrt(pi)/(8 l^5)
for l in [1e-8, 2e-7, 1e-6, 5e-6]:
    rate = coef*hbar*c**2/l**5
    rho = rate*tH
    print(f"    bounded D0' (P_J(cone) = static floor): l={l:.0e}: drho/dt = {rate:.2e} W/m^3; rho_GW(t_H) = {rho:.2e} J/m^3 = {rho/rho_crit:.1e} rho_crit;"
          f" needed cone suppression eps < {rho_L/rho:.1e}")
lmin_bounded = (coef*hbar*c**2*tH/rho_L)**0.2
print(f"    unsuppressed bounded kernel needs l > {lmin_bounded:.1f} m: EXCLUDED for every l in the lab window if the GW content gravitates")
# (b) log option (R9-4): rho_GW ~ eps * L * hbar c/(pi^3 l^4), with L = ln(c t_H / l) from the finite age (R9-4 took L = 10)
for l in [1e-8, 2e-7, 1e-6, 5e-6]:
    L = math.log(c*tH/l)
    rho1 = L*hbar*c/(math.pi**3*l**4)
    print(f"    log option: l={l:.0e}: L = ln(c t_H/l) = {L:.1f} (R9-4 used 10); rho_GW(eps=1) = {rho1:.2e} J/m^3; eps needed < {rho_L/rho1:.1e}")
print("    subtraction: none (positive energy densities)")

# ------------------------------------------------------------------ [8]
print("\n[8] window arithmetic")
u_EBL = 4*math.pi*6e-8/c
for Ap in [1e-4, 1e-2, 1.0]:
    lmin = (Ap*hbar*c**2*lP2*tH/u_EBL)**(1/7)
    print(f"    vacuum photon injection (R8-3 [5], n>=3, cone suppression narrow-band so not multiplied by 1/eps): A'={Ap:.0e}: l > {lmin:.2e} m")
# ISL: smeared point potential force deficit at 52 um (R6-4 referee formula) vs Yukawa alpha=1 lambda < 38.6 um
from scipy.special import erf
r = 52e-6
for l in [1e-6, 5e-6, 1e-5]:
    x = r/(2*l)
    fd = 1 - (erf(x) - 2*x*math.exp(-x*x)/math.sqrt(math.pi))
    print(f"    ISL: l={l:.0e} m: point-mass force deficit at 52 um = {fd:.2e}")
lam = 38.6e-6
print(f"    Yukawa alpha=1, lambda=38.6 um at r=52 um: force excess (1+r/lambda)e^(-r/lambda) = {(1+r/lam)*math.exp(-r/lam):.3f} (excluded at 95% CL, Lee et al. 2020, web-checked)")
print("    => any l with deficit << 0.6 at 52 um is far inside the Yukawa-excluded size; 5e-6 m stays R6-4's conservative upper end (no geometry fit)")

# ------------------------------------------------------------------ [9]
print("\n[9] explicit regulated kernel K_eps (R8-3 convention: P_J*D0' >= 1/4, K = D0'|F|^2 + c^2|F|^2 P_J/s^2), per frame mode, units c*k = 1")
print("    D0'(s) = c/(2 e(s) sqrt(s^2+s0^2)),  P_J = e(s) sqrt(s^2+s0^2)/(2c),  e(s) = eps + (1-eps) s^2/(s^2 + d^2),  d = sqrt(eps), s0 = 2/T*")
cN = 1.0
def kern(s, eps, s0):
    d = math.sqrt(eps)
    e = eps + (1-eps)*s*s/(s*s + d*d)
    D0p = cN/(2*e*math.sqrt(s*s+s0*s0)); PJ = e*math.sqrt(s*s+s0*s0)/(2*cN)
    return D0p, PJ
for eps in [1e-6, 1e-10]:
    s0 = 2/1e8
    Dmax = kern(0.0, eps, s0)[0]
    # (H-T) saturation and local finiteness
    sat = max(abs(kern(s, eps, s0)[0]*kern(s, eps, s0)[1]-0.25) for s in np.linspace(-2, 2, 4001))
    # static point s = -1 (w = 0): K/floor
    D0p, PJ = kern(-1.0, eps, s0); Kst = D0p + cN**2*PJ/1.0
    # photon-pair band check: int_0^1 s^2 D0'(s) ds vs least-decoherence int_0^1 s^2 /(2s) ds = 1/4
    band = integrate.quad(lambda s: s*s*kern(s, eps, s0)[0], 0, 1, points=[math.sqrt(eps)], limit=400)[0]
    # free-GW energy after T (P_J near the cone, u = s/2): secular slope dE/dlnT vs non-secular forced part
    def EGW(T):
        f = lambda u: kern(2*u, eps, s0)[1]*math.sin(u*T/2)**2/u**2
        pts = list(np.logspace(-10, 0, 500))
        return 2*sum(integrate.quad(f, a, b, limit=200)[0] for a, b in zip([0.0]+pts[:-1], pts))
    E6, E7 = EGW(1e6), EGW(1e7)
    slope = (E7-E6)/math.log(10)
    print(f"    eps={eps:.0e}: max|P_J D0' - 1/4| = {sat:.1e}; sup D0' = {Dmax:.2e} (bounded => locally finite); static K/floor = {Kst/(cN/1.0):.6f};"
          f" photon band int s^2 D0' = {band:.4f} (least-decoherence 0.25); E(T=1e6)={E6:.4f}, secular slope dE/dlnT = {slope:.2e} (unsuppressed: 1); forced part ~ ln(1/d) = {0.5*math.log(1/eps):.2f}")
print("    => sup D0' finite; static kernel = R6-4 floor; photon-pair weight unchanged; SECULAR free-GW growth suppressed ~eps; a non-secular forced near-cone TT part ~ (1/2)ln(1/eps) remains unless the suppression is broadband (premise ii)")

# ------------------------------------------------------------------ [10]
print("\n[10] near-cone matter heating under premise (i) (SUGGESTED, order of magnitude)")
print("     heating_cone/heating_static ~ f_cone * L/eps, f_cone = mass-weighted f-sum fraction of matter excitations at hbar w ~ hbar c/l")
hb_static_1e8 = 9.9e-22   # W/kg at l = 1e-8 m (R6-4 table, least-decoherence floor)
earth = 7.9e-12
for l, fcone in [(1e-8, 1.6e-4), (4e-8, 1.6e-4), (2e-7, 1e-3), (1e-6, 1.0), (5e-6, 1.0)]:
    L = math.log(c*tH/l)
    rho1 = L*hbar*c/(math.pi**3*l**4); eps_need = min(1.0, rho_L/rho1)
    hs = hb_static_1e8*(1e-8/l)**3
    hc = hs*fcone*L/eps_need
    print(f"     l={l:.0e} m: hbar c/l = {1.97327e-7/l:.2e} eV, f_cone={fcone:.0e}, eps={eps_need:.1e}: heating ~ {hc:.1e} W/kg (Earth bound {earth:.1e}) {'FAIL' if hc>earth else 'pass'}")
lcross = 1e-8*((hb_static_1e8*1.6e-4*math.log(c*tH/1e-8)/min(1.0, rho_L/(math.log(c*tH/1e-8)*hbar*c/(math.pi**3*1e-32))))/earth)**(1/7)
print(f"     crossover (f_cone = 1.6e-4, heating ~ l^-7): l ~ {lcross:.1e} m; x/÷ 1e2 in f_cone moves it by x/÷ {100**(1/7):.2f}")

# ------------------------------------------------------------------ [11]
print("\n[11] premise (ii) (R9-4 broadband: TT noise at w >~ |k| gravitates): joint lower end with L = ln(c t_H/l) instead of 10")
for Ap in [1e-4, 1e-2, 1.0]:
    lmin0 = (Ap*hbar*c**2*lP2*tH/u_EBL)**(1/7)
    def g_(l):
        L = math.log(c*tH/l); eps = rho_L*math.pi**3*l**4/(L*hbar*c)
        return l - lmin0*eps**(-1/7)
    lo, hi = 1e-9, 1e-4
    for _ in range(200):
        mid = math.sqrt(lo*hi)
        if g_(mid) > 0: hi = mid
        else: lo = mid
    print(f"     A'={Ap:.0e}: lower end ~ {hi:.2e} m")
print("\n[12] margins at l = 1e-6 m (premise ii, A'=1): photon injection / EBL x 1/eps")
l = 1e-6; L = math.log(c*tH/l); eps = rho_L*math.pi**3*l**4/(L*hbar*c)
r = (1.71e-8/l)**7/eps
print(f"     eps = {eps:.1e}; photon injection / u_EBL = {r:.1e}")

print("\n[13] quasi-static TT metric-noise energy fraction (least-decoherence P_J = |s|/2c, weight w^2/|s|): int_0^x0 x^2/(1-x^2) dx")
for x0 in [0.5, 0.1, 0.01]:
    v = -x0 + math.atanh(x0)
    print(f"     w < {x0} ck: {v:.3e}  (near-cone log region carries ~L ~ 70-80 in the same units)")
for l in [1e-6, 5e-6]:
    unit = hbar*c/(math.pi**3*l**4)
    print(f"     l={l:.0e}: unit hbar c/(pi^3 l^4) = {unit:.2e} J/m^3 = {unit/rho_crit:.1e} rho_crit; part w<0.5ck: {0.0493*unit/rho_crit:.1e} rho_crit; part w<0.01ck: {3.33e-7*unit/rho_crit:.1e} rho_crit")
