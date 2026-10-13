#!/usr/bin/env python3
"""R18-7 [3]-[8]: E1 + completion N at O(G^2), numerical checks.  OMP_NUM_THREADS=2; runtime < 1 min.
Units G = c = 1 in [3]-[6] unless stated.  Each section prints its subtraction.
"""
import numpy as np
from scipy import special, integrate
np.set_printoptions(precision=4)
rng = np.random.default_rng(18007)

def smear_radial(f, r, sig, rmax_fac=12.0):
    """3D Gaussian convolution (width sig) of a radial function f(s), evaluated at radius r."""
    lo = max(0.0, r - rmax_fac*sig); hi = r + rmax_fac*sig
    kern = lambda s: f(s)*s*(np.exp(-(r-s)**2/(2*sig**2)) - np.exp(-(r+s)**2/(2*sig**2)))
    pts = [p for p in (r,) if lo < p < hi]
    val, _ = integrate.quad(kern, lo, hi, points=pts, limit=400, epsabs=0, epsrel=1e-11)
    return val/(np.sqrt(2*np.pi)*sig*r)

# ---------------- [3] beta for a smeared point mass: N_1 (Lambda unfiltered) vs N_F (Lambda filtered) ----------------
print("[3] static point mass M = 1 smeared by F = exp(-k^2 l^2/2), l = 1; O(M^2) g00 outside")
print("    subtraction: the GR exterior -2M^2/r^2 and the fitted O(M^2) mass renormalisation 2 dM/r")
l = 1.0
UF = lambda r: special.erf(r/(np.sqrt(2)*l))/r
dUF = lambda r: (np.sqrt(2/np.pi)/l*np.exp(-r**2/(2*l**2)))/r - special.erf(r/(np.sqrt(2)*l))/r**2
L00 = lambda r: -(7/(8*np.pi))*dUF(r)**2
Lkk = lambda r: -(1/(8*np.pi))*dUF(r)**2
# N_F - N_1 differs by the source (F-1)Lambda; compute its potential exactly (radial Green function)
def dh_from(dS, rs):
    """lap h = -16 pi dS; h(r) = (16pi/r) int_0^r dS s^2 ds + 16 pi int_r^inf dS s ds (radial Green)"""
    out = []
    for r in rs:
        a, _ = integrate.quad(lambda s: dS(s)*s**2, 0, r, limit=400, epsrel=1e-10, epsabs=0)
        b, _ = integrate.quad(lambda s: dS(s)*s, r, np.inf, limit=400, epsrel=1e-10, epsabs=0)
        out.append(16*np.pi*(a/r + b))
    return np.array(out)
# tabulate (F-1)Lambda on a grid and interpolate (log-log on the tail)
rg = np.concatenate([np.linspace(0.02, 30, 1500), np.geomspace(30.0, 3000.0, 600)[1:]])
dS00 = np.array([smear_radial(L00, r, l) - L00(r) for r in rg])
dSkk = np.array([smear_radial(Lkk, r, l) - Lkk(r) for r in rg])
def interp_tail(vals):
    def f(s):
        s = np.atleast_1d(s)
        v = np.interp(s, rg, vals)
        tail = s > rg[-1]
        v[tail] = vals[-1]*(rg[-1]/s[tail])**6
        return v if v.size > 1 else float(v[0])
    return f
dS00f, dSkkf = interp_tail(dS00), interp_tail(dSkk)
# check: tail of (F-1)Lambda00 against the local formula (l^2/2) lap(Lambda) = -(7/8pi)(l^2/2)(12/r^6)
for r in (20.0, 100.0, 1000.0):
    print("    r = %6.0f l: (F-1)Lambda00 = %.6e ; local (l^2/2)lap Lambda00 = %.6e" % (r, np.interp(r, rg, dS00), -(7/(8*np.pi))*(l**2/2)*12/r**6))
rs = np.array([10.0, 30.0, 100.0, 300.0])
# split the radial integrals at the grid breaks for accuracy
dh00 = dh_from(dS00f, rs); dhkk = dh_from(dSkkf, rs)
# numerical monopole leak of (F-1)Lambda (exactly zero analytically): its 1/r field is a mass renormalisation -> subtract
Q00 = integrate.quad(lambda s: dS00f(s)*s**2, 0, np.inf, limit=800)[0]
Qkk = integrate.quad(lambda s: dSkkf(s)*s**2, 0, np.inf, limit=800)[0]
dh00 = dh00 - 16*np.pi*Q00/rs; dhkk = dhkk - 16*np.pi*Qkk/rs
print("    numerical monopole leak subtracted as mass renormalisation: 16pi Q00 = %.2e, 16pi Qkk = %.2e (analytic: 0)" % (16*np.pi*Q00, 16*np.pi*Qkk))
print("    integral of (F-1)Lambda00 over space (F preserves integrals -> 0): %.3e (vs int Lambda00 = %.4f)" %
      (4*np.pi*integrate.quad(lambda s: dS00f(s)*s**2, 0, np.inf, limit=800)[0], 4*np.pi*integrate.quad(lambda s: L00(s)*s**2, 0, np.inf, limit=400)[0]))
for r, a, b in zip(rs, dh00, dhkk):
    dg = 0.5*(a + b)
    print("    r = %5.0f l: N_F - N_1: dh00 r^4/l^2 = %8.4f (pred 7), dhkk r^4/l^2 = %7.4f (pred 1), dg00 r^4/l^2 = %7.4f (pred 4) -> beta_eff - 1 = -dg00 r^2/2 = %.3e"
          % (r, a*r**4, b*r**4, dg*r**4, -dg*r**2/2))
# N_1: exterior Lambda equals the point-mass one up to erfc terms
for r in (5.0, 8.0, 10.0):
    print("    N_1 exterior check r = %4.0f l: |Lambda00(smeared U)/Lambda00(M/r) - 1| = %.2e" % (r, abs(L00(r)/(-(7/(8*np.pi))/r**4) - 1)))
print("    => N_1: beta = 1 up to exp(-r^2/2l^2); N_F: beta = 1 in PPN form plus a non-PPN 4 l^2 M^2/r^4 term in g00")

# ---------------- [4] conservation defect of literal N with geodesic matter (static Gaussian body) ----------------
print("\n[4] defect D = (F rho) grad U_F - F[rho grad U_F] (matter in hydrostatic equilibrium in the record metric U_F)")
print("    subtraction: none (D measured against zero; ratio to |rho grad U_F|)")
def defect_ratio(R, l):
    s2 = np.sqrt(R**2 + l**2)
    rho = lambda r: np.exp(-r**2/(2*R**2))/((2*np.pi)**1.5*R**3)
    rhoF = lambda r: np.exp(-r**2/(2*s2**2))/((2*np.pi)**1.5*s2**3)
    dU = lambda r: (np.sqrt(2/np.pi)/s2*np.exp(-r**2/(2*s2**2)))/r - special.erf(r/(np.sqrt(2)*s2))/r**2
    v = lambda r: rho(r)*dU(r)                       # radial force density magnitude (signed)
    rgr = np.linspace(1e-3*R, 12*R, 2400)
    # psi with psi' = v, psi(inf) = 0
    psi_vals = np.array([-integrate.quad(v, r, 14*R, limit=200)[0] for r in rgr])
    psi = lambda s: np.interp(s, rgr, psi_vals, right=0.0)
    Fpsi = np.array([smear_radial(psi, r, l) for r in rgr])
    Fv = np.gradient(Fpsi, rgr)
    D = rhoF(rgr)*dU(rgr) - Fv
    w = rgr**2
    return np.sqrt(np.trapezoid(D**2*w, rgr)/np.trapezoid((rho(rgr)*dU(rgr))**2*w, rgr))
for lr in (0.3, 0.1, 0.03):
    q = defect_ratio(1.0, lr)
    print("    l/R = %.2f: ||D|| / ||rho grad U|| = %.4e ; /(l/R)^2 = %.4f" % (lr, q, q/lr**2))
print("    => D != 0 at O(G): R16-14's 'Bianchi holds at O(G^2) because F commutes with d' needs a conserved total source, which literal N lacks")

# ---------------- [5] S-channel noise: mean of the O(G^2) source for insertion weight (1 + aU) ----------------
print("\n[5] homogeneous static Gaussian noise potential U_n on a periodic box; rho_n = -lap U_n/(4 pi); u1 = <|grad U|^2>/(8 pi)")
print("    subtraction: none (means of positive/indefinite quadratic forms; <rho_n> = 0 exactly)")
N, Lb = 64, 1.0
k1 = 2*np.pi*np.fft.fftfreq(N, d=Lb/N)
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij'); K2 = KX**2 + KY**2 + KZ**2
amp = np.exp(-K2*(0.03)**2)/np.where(K2 > 0, np.sqrt(K2), 1.0); amp[0, 0, 0] = 0
res = []
for trial in range(4):
    Wk = np.fft.fftn(rng.standard_normal((N, N, N)))*amp
    Un = np.real(np.fft.ifftn(Wk))
    rho_n = np.real(np.fft.ifftn(K2*Wk))/(4*np.pi)
    g2 = sum(np.real(np.fft.ifftn(1j*KK*Wk))**2 for KK in (KX, KY, KZ))
    u1 = g2.mean()/(8*np.pi)
    res.append((np.mean(Un*rho_n)/u1, rho_n.mean()))
res = np.array(res)
print("    <U rho>/u1 over 4 realisations: %s (identity: 2)" % res[:, 0])
for a in (0, 3.5, 3.75, 4, 6):
    e00 = 2*a - 7; act = 2*a - 8
    print("    insertion (1 + %.2f U) rho_n: <tau00>/u1 = %+.2f, <tau00 + tau_kk>/u1 = %+.2f" % (a, e00, act))
print("    (a = 0: meter measures (-g)T, noise added after; a = 4: record multiplied by (-g) classically; a = 6: noise as static dust (-g)u0u0)")
print("    min over a of max(|2a-7|, |2a-8|) = 0.5 at a = 3.75: no one-parameter insertion removes both the energy and the active density")
# gauge-invariant (static slicing) active density from the lapse equation D^2 N = 4 pi N rho_H ([1b]):
# lap N2 = 4 pi U rho + |grad U|^2 + 4 pi a' U rho, rho_H = rho_n (1 + a' U); harmonic weight a = a' + 6 ((-g) u0 u0 = 1 + 6U)
Wk = np.fft.fftn(rng.standard_normal((N, N, N)))*amp
Un = np.real(np.fft.ifftn(Wk)); rho_n = np.real(np.fft.ifftn(K2*Wk))/(4*np.pi)
g2 = sum(np.real(np.fft.ifftn(1j*KK*Wk))**2 for KK in (KX, KY, KZ)); u1 = g2.mean()/(8*np.pi)
for a in (0, 4, 6):
    ap = a - 6
    lapN2 = 4*np.pi*Un*rho_n + g2 + 4*np.pi*ap*Un*rho_n
    print("    lapse equation (spatial-gauge invariant): a = %d (a' = %+d): <rho_act> = <lap N2>/(4 pi) = %+.4f u1 ; harmonic-LL value 2a-8 = %+d"
          % (a, ap, lapN2.mean()/(4*np.pi)/u1, 2*a - 8))
print("    => the static active density (2a-8)u1 is not a harmonic-gauge artefact; a = 4 (unchanged meter; tau = (-g)(J + t_LL) + t_H formed classically) gives 0")

# ---------------- [6] harmonic vs Poisson gauge for S-channel noise ----------------
print("\n[6] per frame mode: harmonic-gauge h00 is a resonant oscillator driven by the S noise; Poisson-gauge Phi is instantaneous")
print("    subtraction: none.  R(k) = secular harmonic 'energy' / stationary Poisson analogue = (1/2) W^2 |F_t(W)|^2 T tau / I, I = tau int |F_t|^2 dw/2pi")
Ft2 = lambda x: (1 + 16*x**2)/(1 + x**2)**4
I_t = integrate.quad(lambda x: Ft2(x), -np.inf, np.inf)[0]/(2*np.pi)
print("    I = tau int |F_t|^2 dw/(2 pi) = %.5f (repaired gain)" % I_t)
# numeric check of the secular growth law for one mode with the colored drive
W, tau = 1.0, 1.0
for T in (200.0, 800.0):
    # energy growth of x'' + W^2 x = s, <s s> spectrum Ft2(w tau): E(T) = (1/2) int dw/2pi S(w) |int_0^T e^{iwt} e^{iW(T-t)}...|^2 ~ (1/2) S(W) T
    w = np.linspace(-40, 40, 400001) + 1.234567e-5; S = Ft2(w*tau)
    kern = (np.sin((w - W)*T/2)/((w - W)/2))**2 + (np.sin((w + W)*T/2)/((w + W)/2))**2
    E = 0.25*np.trapezoid(S*kern, w)/(2*np.pi)
    print("    T = %5.0f: E(T) numeric = %.4f ; (1/2)|F_t(W)|^2 T = %.4f" % (T, E, 0.5*Ft2(W*tau)*T))
c = 2.99792458e8; tH = 1/(67.7e3/3.0857e22)
for ell, ctau, lab in ((5e-6, 5e-6, "strict tau=l/c, l=5e-6"), (4e-10, 4e-10, "strict, l=4e-10"), (5e-6, 1.49e-3, "tau_c ceiling, l=5e-6")):
    tau = ctau/c
    Wmax = max([(0.5*(c*k)**2*Ft2(c*k*tau)*tH*tau/I_t, k) for k in np.geomspace(1e-3/ctau, 1/ell, 400)])
    print("    %-26s: max_k R(k) at t_H = %.2e (at k = %.2e /m)" % (lab, Wmax[0], Wmax[1]))
print("    => in harmonic gauge the realised S/V record noise carries secular pure-gauge parts ~1e29 x the Poisson-gauge field;")
print("       the LL pseudotensor of the realised field is gauge-dependent, so N must be posed in the frame's Poisson gauge (P-r15b)")

# ---------------- [7] CP: adaptive measurement + nonlinear classical feedback vs mean-field feedback ----------------
print("\n[7] qubit toy, 6 steps: weak sigma_z measurement with record-dependent strength eps(q), feedback exp(-i th(q) sigma_x),")
print("    q updated NONLINEARLY from records (q <- q + r + 0.7 r q^2).  Averaged map's Choi matrix; mean-field variant uses <sigma_z>_rho")
sx = np.array([[0, 1], [1, 0]], complex); sz = np.diag([1.0, -1.0]).astype(complex); I2 = np.eye(2)
def Ux(th): return np.cos(th)*I2 - 1j*np.sin(th)*sx
def run(rho, meanfield=False, nsteps=6):
    branches = [(rho, 0.0)]
    for n in range(nsteps):
        nb = []
        for (sig, q) in branches:
            eps = 0.4*np.tanh(1 + q**2)
            for r in (+1, -1):
                A = np.sqrt(np.diag([(1 + r*eps)/2, (1 - r*eps)/2])).astype(complex)
                s2 = A @ sig @ A.conj().T
                q2 = q + r + 0.7*r*q**2
                if meanfield:
                    p = np.real(np.trace(s2))
                    mz = np.real(np.trace(sz @ s2))/p if p > 0 else 0
                    th = 0.9*np.sin(q2) + 1.3*mz      # depends on the conditional state: nonlinear in rho
                else:
                    th = 0.9*np.sin(q2) + 0.5*q2**2   # depends on records only
                U = Ux(th); nb.append((U @ s2 @ U.conj().T, q2))
        branches = nb
    return sum(b[0] for b in branches)
def choi(meanfield):
    C = np.zeros((4, 4), complex)
    for i in range(2):
        for j in range(2):
            E = np.zeros((2, 2), complex); E[i, j] = 1
            C += np.kron(E, run(E, meanfield))
    return C
for mf in (False, True):
    C = choi(mf)
    ev = np.linalg.eigvalsh((C + C.conj().T)/2)
    if not mf:
        print("    record-controlled map: Choi eigenvalues %s (all >= 0 -> CP) ; trace-preservation err %.1e" % (np.round(ev, 6), np.abs(np.trace(C) - 2)))
r1 = np.diag([1.0, 0.0]).astype(complex); r2 = 0.5*np.array([[1, 1], [1, 1]], complex)
for mf in (False, True):
    lin = np.abs(run(0.5*r1 + 0.5*r2, mf) - 0.5*run(r1, mf) - 0.5*run(r2, mf)).max()
    print("    meanfield=%s: linearity defect |Phi(mix) - mix(Phi)| = %.3e" % (mf, lin))
print("    => record-controlled nonlinear feedback is a CP instrument (linear in rho); mean-metric (N-bar-type) feedback is not linear in rho")

# ---------------- [8] noise-fed medium under N (harmonic LL, quasi-static S channel) against Mercury ----------------
print("\n[8] |u1| = hbar I_F/(32 pi^1.5 l^3 tau), I_F = 21/32 (R15-2, vR15-2:17); Mercury bound |rho_act| < 9.29e-15 kg/m^3 (R16-14, vR16-14:11)")
print("    subtraction: none")
hbar = 1.054571817e-34; G = 6.674e-11
H0 = 67.7e3/3.0857e22; rho_L = 0.69*3*H0**2/(8*np.pi*G)
merc = 9.286e-15
for lab, ctf in (("strict", None), ("tau_c=1.49e-3/c", 1.49e-3)):
    for ell in (4e-10, 3e-8, 1e-6, 5e-6):
        tau = (ell if ctf is None else ctf)/c
        u1 = hbar*(21/32)/(32*np.pi**1.5*ell**3*tau)/c**2     # kg/m^3
        print("    %-16s l = %.0e m: |u1|/rho_L = %.2e ; a=0 active 8|u1| / Mercury bound = %.2e ; a=3.75 (max 0.5|u1|) / rho_L = %.2e"
              % (lab, ell, u1/rho_L, 8*u1/merc, 0.5*u1/rho_L))
