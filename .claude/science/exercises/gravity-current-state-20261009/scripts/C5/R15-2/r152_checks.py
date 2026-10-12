#!/usr/bin/env python3
"""C5 R15-2: spin-2 conserved-noise assembly for set A route E1 with the repaired (zero-first-moment) gain.
Sections:
 [1] exchange decomposition of linearized GR for conserved sources in the CMB frame: TT radiative, vector + scalar instantaneous
 [2] conserved S/V record noise with a finite start: free data filtered by the gain, derived components by time derivatives
 [3] mean-field finite-start Bianchi defect of R13-6's H3 and an exact conserved initial-memory repair B
 [4] TT channel: exact per-polarization normalization, hdot regularity with the gain, and the weight vs R11-5's O(1) formula
 [5] complete positivity in the exact limit: arcsine-quadrature approximants, trace-norm convergence of the covariance
 [6] budget: TT secular + quasi-static with exact weight; drag ceiling; constraint-channel (S/V) noise field energy (conditional)
 [7] second-order PPN: <h^2> per channel (TT log-growing at t_H; S stationary)
 [8] scalar block: least-decoherence floor for mass-density superpositions with correlated (rho, T_perp) noise
Run: OMP_NUM_THREADS=2 python3 r152_checks.py
"""
import math, numpy as np
from scipy import special, integrate, signal
rng = np.random.default_rng(1502)
hbar = 1.054571817e-34; c = 2.99792458e8; G = 6.67430e-11
lP2 = G*hbar/c**3
tH = 4.35e17                      # s (as R11-5 / R13-6 / R14-2)
rho_crit = 8.5e-27*c**2           # J/m^3 (RECALLED, as R11-5)
rho_L = 0.69*rho_crit
gE = 0.5772156649

# ------------------------------------------------------------------ [1]
print("[1] linearized-GR exchange for conserved sources, p = (w, 0, 0, k) in the CMB frame, eta = diag(-1,1,1,1), units 16 pi G = 1")
eta = np.diag([-1.0, 1, 1, 1])
def cons_tensor(rho, T0a, Tab, w, k):
    T = np.zeros((4, 4), complex); r = w/k
    T[0, 0] = rho
    T[0, 1] = T[1, 0] = T0a[0]; T[0, 2] = T[2, 0] = T0a[1]
    T[1, 1] = Tab[0, 0]; T[1, 2] = T[2, 1] = Tab[0, 1]; T[2, 2] = Tab[1, 1]
    T[0, 3] = T[3, 0] = r*rho
    T[1, 3] = T[3, 1] = r*T0a[0]; T[2, 3] = T[3, 2] = r*T0a[1]
    T[3, 3] = r*r*rho
    return T
def rnd():
    a = rng.normal(size=6) + 1j*rng.normal(size=6)
    Tab = np.array([[a[3], a[4]], [a[4], a[5]]])
    return a[0], a[1:3], Tab
maxres = 0; maxcons = 0
for trial in range(200):
    k = rng.uniform(0.2, 3); w = rng.uniform(-4, 4)
    if abs(abs(w) - k) < 1e-3: continue
    d1, d2 = rnd(), rnd()
    T1 = cons_tensor(*d1, w, k); T2 = cons_tensor(*d2, w, k)
    pl = np.array([-w, 0, 0, k])
    maxcons = max(maxcons, np.abs(pl @ T1).max())
    T2l = eta @ T2 @ eta
    tr1 = np.sum(np.diag(eta)*np.diag(T1)); tr2 = np.sum(np.diag(eta)*np.diag(T2))
    E = (np.sum(T1*T2l) - 0.5*tr1*tr2)/(k*k - w*w)
    def TT(Tab):
        tp = Tab[0, 0] + Tab[1, 1]
        return Tab - 0.5*np.eye(2)*tp, tp
    TT1, tp1 = TT(d1[2]); TT2, tp2 = TT(d2[2])
    pred = (np.sum(TT1*TT2)/(k*k - w*w) - 2*np.dot(d1[1], d2[1])/k**2
            + 0.5*d1[0]*d2[0]*(k*k - w*w)/k**4 + 0.5*(d1[0]*tp2 + tp1*d2[0])/k**2)
    maxres = max(maxres, abs(E - pred)/max(1, abs(E)))
print(f"    200 random conserved pairs: max |p_mu T^mu nu| = {maxcons:.1e}; max rel |E_Lorenz - (TT/s + V/k^2 + S-block)| = {maxres:.1e}")
print("    E = TT:TT'/(k^2-w^2) - 2 T^0a T'^0a/k^2 + (1/2) rho rho' (k^2-w^2)/k^4 + (1/2)(rho T'_perp + T_perp rho')/k^2  [x 16 pi G]")
print("    => only TT carries the cone pole; V and S blocks are instantaneous (polynomial in w over k^n); S block det = -1/(4k^4) < 0 (indefinite)")
w = 1.0; k = 1.0 + 1e-9
print(f"    at w -> k: S block entries ({0.5*(k*k-w*w)/k**4:.1e}, {0.5/k**2:.2f}), V entry {-2/k**2:.2f}: finite (no 1/s)")

# ------------------------------------------------------------------ gain
def f_rep(t, tau=1.0):      # impulse response of (1 - 4 i w tau)(1 - i w tau)^-4  (Laplace (1+4 p tau)/(1+p tau)^4)
    x = t/tau; return np.where(t >= 0, np.exp(-x)*x**2*(4 - x)/(2*tau), 0.0)
def fp_rep(t, tau=1.0):
    x = t/tau; return np.where(t >= 0, np.exp(-x)*(8*x - 7*x**2 + x**3)/(2*tau**2), 0.0)
def fpp_rep(t, tau=1.0):
    x = t/tau; return np.where(t >= 0, np.exp(-x)*(8 - 22*x + 10*x**2 - x**3)/(2*tau**3), 0.0)
def f_n(t, n, tau=1.0):     # literal (1 - i w tau)^-n
    x = t/tau; return np.where(t >= 0, x**(n-1)*np.exp(-x)/(math.factorial(n-1)*tau), 0.0)
m0 = integrate.quad(lambda t: f_rep(t), 0, 80)[0]; m1 = integrate.quad(lambda t: t*f_rep(t), 0, 80)[0]
m3 = integrate.quad(lambda t: t**3*f_rep(t), 0, 80)[0]
chk = max(abs(integrate.quad(lambda t: fp_rep(t), 0, 80)[0] - (0 - f_rep(0.0))), 0)
print(f"\n    repaired gain f(t) = e^-x x^2 (4-x)/(2 tau): int f = {m0:.12f}, first moment = {m1:.1e}, third moment = {m3:.4f} tau^3; f(0) = {float(f_rep(0.0)):.1f}, f'(0) = {float(fp_rep(0.0)):.1f}, f''(0) = {float(fpp_rep(0.0)):.1f}/tau^3")

# ------------------------------------------------------------------ [2]
print("\n[2] conserved S/V record noise with a finite start t0 = 0 (one mode, k = 2/tau): free data rho, T^0a filtered by the gain; derived")
print("    J^z0 = (i/k) d_t J^00, J^zz = (i/k)^2 d_t^2 J^00  (exact conservation  d_t J^0nu + i k J^z nu = 0)")
dt = 2e-3; Tn = 60.0; t = np.arange(0, Tn, dt); kk = 2.0
xi = rng.normal(size=t.size)/math.sqrt(dt)
for name, f0, f1, f2 in [("repaired n=4", f_rep(t), fp_rep(t), fpp_rep(t)),
                         ("literal n=2 (f'(0)=1)", f_n(t, 2), np.where(t >= 0, (1 - t)*np.exp(-t), 0), np.where(t >= 0, (t - 2)*np.exp(-t), 0))]:
    J00 = signal.fftconvolve(f0, xi)[:t.size]*dt
    dJ00 = signal.fftconvolve(f1, xi)[:t.size]*dt            # = d_t (f * xi) when f(0) = 0
    J0z = (1j/kk)*dJ00
    # J^zz built two ways: (a) as (i/k)^2 times the true second derivative f''*xi + f'(0) xi; (b) the f''*xi convolution only
    d2_true = signal.fftconvolve(f2, xi)[:t.size]*dt + float(f1[0])*xi
    Jzz = (1j/kk)**2*d2_true
    # conservation residuals by finite differences on the sampled paths
    r0 = np.gradient(J00, dt) + 1j*kk*J0z
    rz = np.gradient(J0z, dt) + 1j*kk*Jzz
    sl = slice(50, t.size - 50)
    print(f"    {name}: J^0nu(t0) = ({J00[0]:.1e}, {abs(J0z[0]):.1e}); rel. residual nu=0: {np.std(r0[sl])/np.std(np.gradient(J00, dt)[sl]):.1e}; "
          f"Var J^zz (sample) = {np.var(Jzz[sl].real):.3e} vs int (f'')^2/k^4 = {np.sum(f2**2)*dt/kk**4:.3e}"
          + ("" if float(f1[0]) == 0 else " (white-noise term f'(0) xi present: Var J^zz = infinity in the dt -> 0 limit)"))
print("    TT channel: xi^TT_ij is spatial, transverse, traceless => d_mu xi^mu nu = 0 identically, no time derivative, enters no constraint")
print("    => with f(0) = f'(0) = 0 (repaired n = 4; literal n >= 3) the conserved S/V noise starts at zero (J^0nu(t0) = 0, so the Gauss/momentum")
print("       constraints hold with h = hdot = 0 at t0) and every component has finite variance. subtraction: none")

# ------------------------------------------------------------------ [3]
print("\n[3] mean field with a finite start: J = f *_{t0} T for pre-existing conserved matter (one mode, k = 2, tau = 1)")
dt3 = 1e-3; t3 = np.arange(0, 40, dt3)
A = lambda s: np.cos(0.7*s + 0.3) + 0.5*np.cos(1.9*s)
Ad = lambda s: -0.7*np.sin(0.7*s + 0.3) - 0.95*np.sin(1.9*s)
Add = lambda s: -0.49*np.cos(0.7*s + 0.3) - 1.805*np.cos(1.9*s)
T00 = A(t3); Tz0 = (1j/kk)*Ad(t3); Tzz = (1j/kk)**2*Add(t3)
for name, ff in [("repaired n=4", f_rep(t3)), ("literal n=3", f_n(t3, 3))]:
    conv = lambda X: signal.fftconvolve(ff, X)[:t3.size]*dt3
    J00, Jz0, Jzz = conv(T00), conv(Tz0), conv(Tzz)
    D0 = np.gradient(J00, dt3) + 1j*kk*Jz0
    Dz = np.gradient(Jz0, dt3) + 1j*kk*Jzz
    pred0 = ff*T00[0]; predz = ff*Tz0[0]
    psi = 1 - np.cumsum(ff)*dt3                 # psi(s) = int_s^inf f
    Psi1 = np.cumsum(psi)*dt3                   # Psi1(s) = int_0^s psi -> first moment of f
    B00 = psi*T00[0] + Psi1*Ad(0.0); Bz0 = psi*Tz0[0]; Bzz = 0*psi
    D0B = np.gradient(J00 + B00, dt3) + 1j*kk*(Jz0 + Bz0)
    DzB = np.gradient(Jz0 + Bz0, dt3) + 1j*kk*(Jzz + Bzz)
    sl = slice(20, t3.size - 20)
    print(f"    {name}: max|defect nu=0| = {np.abs(D0[sl]).max():.3f} (predicted f(t-t0) T^00(t0): {np.abs(pred0[sl]).max():.3f}; "
          f"max|defect - prediction| = {np.abs(D0 - pred0)[sl].max():.1e}); nu=z: {np.abs(Dz[sl]).max():.3f} vs {np.abs(predz[sl]).max():.3f}")
    print(f"        with the initial-memory term B: max|defect| = {max(np.abs(D0B[sl]).max(), np.abs(DzB[sl]).max()):.1e}; "
          f"J^00(t0+) + B^00(t0) = {J00[0] + B00[0]:.4f} vs T^00(t0) = {T00[0]:.4f}; Psi1(inf) = {Psi1[-1]:.2e} tau (first moment)")
print("    B^00 = psi(t-t0) T^00(t0) - Psi1(t-t0) div T^0i(t0),  B^0i = psi(t-t0) T^0i(t0),  B^ij = 0;  psi(s) = int_s^inf f,  Psi1(s) = int_0^s psi")
print("    => R13-6's H3 (h = hdot = 0, couplings switched on) violates the Bianchi identity for t - t0 ~ tau whenever T^0nu(t0) != 0;")
print("       B repairs it exactly and is transient iff the first moment vanishes (repaired gain); the literal gain leaves a frozen B^00 = n tau dT^00/dt(t0)")

# ------------------------------------------------------------------ [4]
print("\n[4] TT channel: least-decoherence per polarization, S_h,lambda = 8 pi G hbar |F|^2 /(c^2 |W^2 - w^2|) (W = ck); h_lambda = sqrt(8 pi G hbar/c^2) (f * J0(W.)) * xi")
for a in [0.1, 1.0]:      # a = W tau
    dt4 = min(0.01, a/40); T4 = 3000.0; t4 = np.arange(0, T4, dt4)
    ff = f_rep(t4, a)
    K = signal.fftconvolve(ff, special.j0(t4))[:t4.size]*dt4
    Kp = signal.fftconvolve(ff, -special.j1(t4))[:t4.size]*dt4        # K' = f * J0' since f(0) = 0
    vh = np.cumsum(K**2)*dt4; vhd = np.cumsum(Kp**2)*dt4
    F2 = (1 + 16*a*a)/(1 + a*a)**4
    out = []
    for T in [30, 300, 3000]:
        i = int(T/dt4) - 1
        out.append(f"T={T}: Var h = {vh[i]:.4f}, Var hdot = {vhd[i]:.4f}")
    slope_h = (vh[int(3000/dt4)-1] - vh[int(300/dt4)-1])/math.log(10)
    slope_hd = (vhd[int(3000/dt4)-1] - vhd[int(300/dt4)-1])/math.log(10)
    print(f"    W tau = {a}: K(0) = {K[0]:.1e}, K'(0) = {Kp[0]:.1e}; " + "; ".join(out))
    print(f"        slopes per ln T: Var h {slope_h:.4f}, Var hdot {slope_hd:.4f}; predicted |F(W)|^2/pi = {F2/math.pi:.4f}")
# asymptotic constants for the unfiltered kernels
X = 1e5; xs = np.linspace(0, X, 4000001)
I0 = integrate.simpson(special.j0(xs)**2, x=xs); I1 = integrate.simpson(special.j1(xs)**2, x=xs)
c0 = math.pi*I0 - math.log(X); c1 = math.pi*I1 - math.log(X)
print(f"    int_0^X J0^2 = (ln X + {c0:.4f})/pi  (ln 8 + gamma_E = {math.log(8)+gE:.4f});  int_0^X J1^2 = (ln X + {c1:.4f})/pi  (X = 1e5)")
print("    unfiltered kernel J0 (F = 1): hdot = xi - W (J1 * xi), Var hdot = infinity (referee R13-6 point 4); with the gain K(0) = K'(0) = 0 => finite")
print("    energy: rho_GW = (c^2/32 pi G) <hdot_ij hdot_ij>, h_ij = sum_lambda h_lambda e^lambda_ij, e:e = 2, two polarizations")
print("      => rho_GW = (hbar c /(2 pi^3)) int dk k^3 eps |F|^2 [ln(c k t) + c1]  vs R11-5/R13-6 formula (2 hbar c/pi^3) int dk k^3 eps |F|^2 ln(c k t)")
print("      => exact TT weight = 1/4 of the assumed O(1) normalization at leading log; constant c1 = ln 8 + gamma_E - 2 inside the log")

# ------------------------------------------------------------------ [5]
print("\n[5] CP in the exact limit: approximant kernels J0_N(t) = (1/N) sum_j cos(W cos th_j t) e^{-Gam t} (Gauss-Chebyshev for the arcsine measure)")
T5 = 200.0; dt5 = 0.02; t5 = np.arange(0, T5, dt5); a = 1.0
ff = f_rep(t5, a)
Kex = signal.fftconvolve(ff, special.j0(t5))[:t5.size]*dt5
hs_ex = math.sqrt(np.sum(Kex**2*(T5 - t5))*dt5)   # ||A||_HS on [0,T]: int_0^T K(s)^2 (T - s) ds
print(f"    ||A||_HS = {hs_ex:.3e} (so ||C||_1 = ||A||_HS^2 = {hs_ex**2:.3e}); quadrature is exact-in-practice for t < ~N/W, so convergence sets in at N ~ T W")
for N in [8, 32, 128, 512, 2048]:
    th = (np.arange(1, N + 1) - 0.5)*math.pi/N
    Gam = 1.0/(N*T5)         # damping -> 0 together with N -> infinity
    J0N = np.mean(np.cos(np.outer(np.cos(th), t5)), axis=0)*np.exp(-Gam*t5)
    KN = signal.fftconvolve(ff, J0N)[:t5.size]*dt5
    dK = KN - Kex
    hs_d = math.sqrt(np.sum(dK**2*(T5 - t5))*dt5)
    hs_N = math.sqrt(np.sum(KN**2*(T5 - t5))*dt5)
    # positive-real (outer) check of the approximant transfer function on Re p >= 0
    ps = (rng.uniform(0, 3, 400) + 1j*rng.uniform(-5, 5, 400))
    HN = np.array([np.mean((p + Gam)/((p + Gam)**2 + np.cos(th)**2)) for p in ps])
    print(f"    N={N:4d}: ||A_N - A||_HS = {hs_d:.2e}; relative trace-norm bound ||C_N - C||_1/||C||_1 <= {hs_d*(hs_N + hs_ex)/hs_ex**2:.2e}; min Re H_N(Re p >= 0) = {HN.real.min():.2e} (positive-real => outer)")
print("    => C_N = A_N A_N^* -> C in trace norm on L^2[t0, t]; Gaussian CP maps with converging covariances converge pointwise; limits of CP maps are CP")

# ------------------------------------------------------------------ [6]
print("\n[6] budget at t_H (Isaacson premise for the TT parts; R13-6/R14-2 inputs otherwise)")
n = 4
Ft2 = lambda x: (1 + n*n*x*x)/(1 + x*x)**n
cshift = c1                        # secular constant for <hdot^2> per mode: int_0^{WT} J1^2 = (ln WT + c1)/pi
def rho_log_exact(l, ctc, eps=1.0):
    f = lambda lk: (lambda k: k**4*math.exp(-(k*l)**2)*Ft2(k*ctc)*(math.log(c*k*tH) + cshift))(math.exp(lk))
    v = integrate.quad(f, math.log(1e-6/ctc), math.log(30/l), limit=400)[0]
    return eps*hbar*c/(2*math.pi**3)*v
def rho_log_R136(l, ctc):
    f = lambda lk: (lambda k: k**4*math.exp(-(k*l)**2)*Ft2(k*ctc)*math.log(c*k*tH))(math.exp(lk))
    v = integrate.quad(f, math.log(1e-6/ctc), math.log(30/l), limit=400)[0]
    return hbar*c/math.pi**3*2*v
def rho_qs(l, ctc, xmax=0.5, weight=1.0):
    def inner(k):
        a_ = k*ctc
        g = lambda ly: (lambda y: y**3/(1-(y/a_)**2)*Ft2(y))(math.exp(ly))
        return a_**-3*integrate.quad(g, math.log(1e-8), math.log(xmax*a_), limit=400)[0]
    f = lambda lk: (lambda k: k**4*math.exp(-(k*l)**2)*inner(k))(math.exp(lk))
    v = integrate.quad(f, math.log(1e-6/ctc), math.log(30/l), limit=200)[0]
    return weight*hbar*c/math.pi**3*2*v
for l in [1e-8, 1e-6]:
    ctc = 1e-3
    print(f"    l={l:.0e}, c tau_c=1e-3 m: rho_log exact / R13-6 formula = {rho_log_exact(l, ctc)/rho_log_R136(l, ctc):.4f}")
print("    (A) strict tau = l/c (no F_t in the near-cone count, as R13-6): eps needed, exact TT weight vs R13-6:")
for l in [1e-8, 2e-7, 1e-6, 5e-6]:
    eps = 1.0; epsR = 1.0
    for _ in range(60):
        Le = math.log(max(eps, 1e-300)*c*tH/l) + cshift
        eps = rho_L*2*math.pi**3*l**4/(Le*hbar*c/2)/1.0   # rho = eps*Le*hbar c/(2 pi^3) * int k^3 e^{-k^2l^2} = eps*Le*hbar c/(4 pi^3 l^4)
        LeR = math.log(max(epsR, 1e-300)*c*tH/l)
        epsR = rho_L*math.pi**3*l**4/(LeR*hbar*c)
    print(f"      l={l:.0e}: eps < {eps:.2e} (exact TT) vs {epsR:.2e} (R13-6); ratio {eps/epsR:.2f}")
print("    (B) tau_c variant (eps = 1): lower end of c tau_c for rho_log + rho_qs < rho_L, exact weight (x 1/4) vs R13-6; drag ceiling 1.49e-3 m (R14-2)")
def solve(fun, lo, hi):
    for _ in range(45):
        mid = math.sqrt(lo*hi)
        if fun(mid) > rho_L: lo = mid
        else: hi = mid
    return hi
lows = {}
for l in [4e-10, 1e-9, 2e-9, 1e-8, 1e-6, 5e-6]:
    tex = solve(lambda x: rho_log_exact(l, x) + rho_qs(l, x, weight=0.25), 20*l, 1e2)
    tR = solve(lambda x: rho_log_R136(l, x) + rho_qs(l, x), 20*l, 1e2)
    lows[l] = tex
    print(f"      l={l:.0e} m: c tau_c > {tex:.2e} m (exact) vs {tR:.2e} m (R13-6 weight); window to 1.49e-3: {'open, factor %.1f' % (1.49e-3/tex) if tex < 1.49e-3 else 'closed'}")
# closing point
lo, hi = 1e-10, 1e-8
for _ in range(25):
    mid = math.sqrt(lo*hi)
    if solve(lambda x: rho_log_exact(mid, x) + rho_qs(mid, x, weight=0.25), 20*mid, 1e2) > 1.49e-3: lo = mid
    else: hi = mid
print(f"      window (exact TT weight, CMB-velocity drag ceiling) closes at l ~ {hi:.2e} m (R14-2 with the assumed weight: ~1-2e-9 m)")
print("    (C) constraint-channel (S, V) record-noise field energy at the least-decoherence split (conditional: counts only if a nonlinear")
print("        completion makes non-radiative metric noise gravitate; R6-4's H-cosmo made explicit). Per instantaneous channel:")
print("        |u_1| = (1/2g)<|grad phi|^2> = (hbar/4) int d^3k dw/(2pi)^4 |F|^2 = (hbar/4) (8 pi^{3/2} l^3)^-1 I_F/tau, independent of g")
IF = integrate.quad(lambda x: Ft2(x), -np.inf, np.inf)[0]/(2*math.pi)
print(f"        I_F = (1/2pi) int |F_t|^2 dx = {IF:.6f} (closed form 21/32 = {21/32:.6f})")
u1 = lambda l, tau: hbar/4/(8*math.pi**1.5*l**3)*IF/tau
for l in [4e-10, 1e-8, 1e-6, 5e-6]:
    s_strict = u1(l, l/c)/rho_L; s_tc = u1(l, 1.49e-3/c)/rho_L
    need = hbar/4/(8*math.pi**1.5*l**3)*IF/rho_L*c
    print(f"        l={l:.0e} m: |u_1|/rho_L = {s_strict:.1e} (strict tau = l/c), {s_tc:.1e} (c tau_c = 1.49e-3 m, drag ceiling); |u_1| < rho_L needs c tau > {need:.2e} m")
print("        sign: S (Newtonian, attractive) binding energy negative; V (gravitomagnetic, like currents repel) positive (suggested; gauge/completion-dependent)")
print("    subtraction: none (positive spectral densities; |u| magnitudes)")

# ------------------------------------------------------------------ [7]
print("\n[7] second-order PPN: <h^2> per channel at t_H (eps = 1, repaired gain); alpha_1, alpha_2 ~ C <h^2>, C = O(1-10) (suggested)")
def h2_TT(l, ctc):
    f = lambda lk: (lambda k: k**3*math.exp(-(k*l)**2)*Ft2(k*ctc)*(math.log(8*c*k*tH) + gE)/(math.pi*c*k))(math.exp(lk))
    v = integrate.quad(f, math.log(1e-6/ctc), math.log(30/l), limit=400)[0]/(2*math.pi**2)
    return 2*2*(8*math.pi*G*hbar/c**2)*v          # <h_ij h_ij> = 2 sum_lambda Var h_lambda
def phi2_S(l, tau):
    # <phi^2>, phi = Phi/c^2, S_phi = hbar (4 pi G) |F|^2 /(2 c^4 k^2)
    v = (1/(2*math.pi**2))*math.sqrt(math.pi)/(2*l)       # int d^3k/(2pi)^3 e^{-k^2l^2}/k^2
    return hbar*4*math.pi*G/(2*c**4)*v*IF/tau
for l in [4e-10, 1e-6, 5e-6]:
    for ctc in [l, 1.49e-3]:
        tt = h2_TT(l, ctc); ss = phi2_S(l, ctc/c)
        print(f"    l={l:.0e} m, c tau={ctc:.1e} m: <h_ij h_ij>_TT = {tt:.1e}, <phi^2>_S = {ss:.1e}; (l_P/l)^2 = {lP2/l**2:.1e}; vs alpha2-hat < 1.6e-9, |alpha1-hat| < ~4e-5")
AU = 1.496e11; H0 = 1/tH; beta = 369.82e3/c
print(f"    homogeneous noise fluid at rest in the CMB frame: alpha-type effect ~ (rho_n/rho_crit)(H0 r/c)^2 beta at 1 AU = {(H0*AU/c)**2*beta:.1e} x rho_n/rho_crit")

# ------------------------------------------------------------------ [8]
print("\n[8] scalar block (rho, T_perp): least-decoherence floor for mass-density superpositions (units 16 pi G = hbar = 1, K = P^-1/4 + G P G)")
def Sblock(w, k):
    return np.array([[0.5*(k*k - w*w)/k**4, 0.5/k**2], [0.5/k**2, 0.0]])
for (w, k) in [(0.0, 1.0), (0.5, 1.0), (0.99, 1.0)]:
    Gs = Sblock(w, k); g11, g12 = Gs[0, 0], Gs[0, 1]
    # correlated optimum: P v || e_rho with v = G e_rho; choose p2 then q = -p2 g12/g11, p1 = p2 (g12/g11)^2 + Delta
    Delta = 1/(2*abs(g11)); p2 = Delta
    q = -p2*g12/g11; p1 = p2*(g12/g11)**2 + Delta
    P = np.array([[p1, q], [q, p2]])
    K = 0.25*np.linalg.inv(P) + Gs @ P @ Gs
    # uncorrelated isotropic comparison
    Pi = np.eye(2)*0.5/np.abs(np.linalg.eigvalsh(Gs)).max()
    Ki = 0.25*np.linalg.inv(Pi) + Gs @ Pi @ Gs
    print(f"    w/k={w/k:.2f}: floor |G_rr| = {abs(g11):.4f}; correlated K_rr = {K[0,0]:.4f}, K_pp = {K[1,1]:.3e}, min eig K = {np.linalg.eigvalsh(K).min():.2e}; "
          f"isotropic K_rr = {Ki[0,0]:.4f}, K_pp = {Ki[1,1]:.3f}")
print("    => the rho-floor (R6-4's 4 pi G/(hbar k^2) at w = 0) is attained with anticorrelated pressure-record noise and finite K_pp;")
print("       enforcing it up to the cone makes K_pp ~ 1/|G_rr| diverge there (pressure superpositions); a bounded isotropic choice keeps K = O(G/hbar k^2)")

# ------------------------------------------------------------------ [9]
print("\n[9] constraint-channel energy reduced by R6-4's gamma-trade (P_J -> gamma P_opt, matter kernel (gamma + 1/gamma)/2 x floor):")
print("    gamma_min(l) interpolated log-log from C5_R6-4_report.md:151-160 (4e-10: 1; 1e-9: 0.03; 1e-8: 3e-5; >=1e-6: 2e-10); suggested")
lg = np.log10([4e-10, 1e-9, 1e-8, 1e-6, 1e-5]); gg = np.log10([1.0, 0.03, 3e-5, 2e-10, 2e-10])
gmin = lambda l: 10**np.interp(math.log10(l), lg, gg)
for variant, taufun in [("strict tau = l/c", lambda l: l/c), ("tau_c at drag ceiling 1.49e-3 m", lambda l: 1.49e-3/c)]:
    rows = []
    for l in [2e-8, 5e-8, 1e-7, 2e-7, 3e-7, 5e-7, 1e-6, 5e-6]:
        for nch in [1, 3]:
            greq = rho_L/(nch*u1(l, taufun(l)))
            rows.append((l, nch, greq, gmin(l)))
    # closing points
    for nch in [1, 3]:
        lo, hi = 1e-9, 5e-6
        for _ in range(60):
            mid = math.sqrt(lo*hi)
            if rho_L/(nch*u1(mid, taufun(mid))) < gmin(mid): lo = mid
            else: hi = mid
        print(f"    {variant}, {nch} channel(s) at |u_1| each: allowed for l >= {hi:.1e} m")
    for (l, nch, greq, gm) in rows:
        if nch == 1:
            print(f"      l={l:.0e}: gamma needed <= {greq:.1e} (1 ch) / {greq/3:.1e} (3 ch); gamma_min = {gm:.1e}")

print("\nDONE")
