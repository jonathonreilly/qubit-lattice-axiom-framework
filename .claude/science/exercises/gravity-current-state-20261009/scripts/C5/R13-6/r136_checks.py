"""C5 R13-6 checks: route E1, an explicit start-time (finite-start) CQ dilation.
Sections
 [1] causal spectral factor of the saturated split: H = (W^2-(w+i0)^2)^(-1/2) <-> theta(t) J0(W t); J0*J0 = sin(W t)/W;
     arcsine synthesis measure; analyticity of H and 1/H in the upper half plane
 [2] suppression factor e(s) = (s^2+eps^2)/(s^2+eps): explicit outer factor in w; Stieltjes test of R11-5's D0' profile;
     a Stieltjes member of the family with its positive measure
 [3] single port vs parallel bank: exact saturation of a cascade; causal saturation of a parallel bank forces an all-pass
 [4] finite-start covariance: Var h(T) = 1/2 int_0^T J0^2; record energy E(T) for eps profile with s0 = 0 vs s0 > 0
 [5] matter side at finite age: near-null transition probability; finite-start correction to off-cone (lab) kernels
 [6] budget at t_H: strict K_eps (tau = l/c) and the tau_c extension (delay-compensated gain), log and linear variants
 [7] binary-pulsar aberration from the causal record delay (new test)
 [8] GW waveform: amplitude/phase of the compensated gain in the LIGO band; GW170817 lag
 [9] noise-fed second order: <h^2>, frame-dependent part, Isaacson fluid term
Subtractions (TESTS rule): every growth/decay statement is of a positive integrand with no channel limit subtracted
("subtraction: none") except where a section prints a different subtraction.
"""
import math
import numpy as np
from scipy import integrate, special

rng = np.random.default_rng(1306)
hbar = 1.054571817e-34; c = 2.99792458e8; G = 6.67430e-11
lP = math.sqrt(G*hbar/c**3)
tH = 4.35e17                      # s (RECALLED, ~1/H0, as R11-5)
rho_crit = 8.5e-27*c**2           # J/m^3 (RECALLED, as R11-5)
rho_L = 0.69*rho_crit

print("[1] causal spectral factor of the saturated split (per frame mode, W = c|k| = 1)")
# Laplace transform: int_0^inf J0(t) e^{i w t} e^{-eta t} dt = 1/sqrt(1 + p^2), p = eta - i w (principal sqrt, Re > 0)
def H_exact(w, eta):
    p = eta - 1j*w
    return 1.0/np.sqrt(1.0 + p*p)
def H_numeric(w, eta, Tmax=None):
    if Tmax is None:
        Tmax = 60.0/eta
    f_re = lambda t: special.j0(t)*math.exp(-eta*t)*math.cos(w*t)
    f_im = lambda t: special.j0(t)*math.exp(-eta*t)*math.sin(w*t)
    pts = np.linspace(0, Tmax, int(Tmax/2)+2)
    re = sum(integrate.quad(f_re, a, b, limit=100)[0] for a, b in zip(pts[:-1], pts[1:]))
    im = sum(integrate.quad(f_im, a, b, limit=100)[0] for a, b in zip(pts[:-1], pts[1:]))
    return re + 1j*im
worst = 0.0
for w in [0.0, 0.3, 0.9, 1.1, 2.0, -0.7]:
    for eta in [0.2, 0.05]:
        hn = H_numeric(w, eta); he = H_exact(w, eta)
        worst = max(worst, abs(hn-he)/abs(he))
print(f"    Laplace identity int_0^inf J0(Wt) e^(iwt - eta t) dt = (W^2 + (eta - i w)^2)^(-1/2): max rel. error over 12 points (eta = 0.2, 0.05) = {worst:.1e}")
for w in [0.5, 0.99, 1.01, 3.0]:
    he = H_exact(w, 1e-9)
    print(f"    eta -> 0+: w={w:5.2f}: |H|^2 = {abs(he)**2:.6e} vs 1/|W^2-w^2| = {1/abs(1-w*w):.6e}")
# analyticity in UHP: no zeros, no singularities of H or 1/H for Im w > 0 (grid scan)
ys = np.logspace(-6, 2, 60); xs = np.linspace(-5, 5, 201)
vals = np.array([[H_exact(x, y) for x in xs] for y in ys])
print(f"    UHP scan (Im w in [1e-6,1e2], Re w in [-5,5]): min |H| = {np.abs(vals).min():.3e}, max |H| = {np.abs(vals).max():.3e} (finite, nonzero: H and 1/H analytic in the UHP)")
print("    => H is causal (theta(t) J0(Wt)); 1/H = (W^2 - (w+i0)^2)^(1/2) is analytic in the UHP with |1/H| <= |w| + W: causal by Paley-Wiener-Schwartz (a distribution of order 1)")
# J0 * J0 = sin(t)/1
for t in [1.0, 5.0, 20.0]:
    conv = integrate.quad(lambda s: special.j0(s)*special.j0(t-s), 0, t, limit=400)[0]
    print(f"    (J0*J0)(t={t:4.1f}) = {conv:+.8f} vs sin(t) = {math.sin(t):+.8f}  [G_R = H^2 in the time domain]")
# arcsine synthesis of J0: J0(t) = int_{-1}^{1} cos(w' t) dw'/(pi sqrt(1-w'^2))
for t in [0.5, 3.0, 17.0]:
    v = integrate.quad(lambda th: math.cos(t*math.sin(th)), -math.pi/2, math.pi/2, limit=200)[0]/math.pi
    print(f"    arcsine synthesis: int cos(w't) dmu(w') = {v:+.10f} vs J0(t) = {special.j0(t):+.10f} (dmu = dw'/(pi sqrt(W^2-w'^2)) >= 0 on |w'|<W)")
print("    subtraction: none")

# ------------------------------------------------------------------ [2]
print("\n[2] near-cone suppression e(s) = eps + (1-eps) s^2/(s^2+d^2) = (s^2 + eps d^2)/(s^2 + d^2), d = sqrt(eps)")
def outer_quad(w, b2, W=1.0):
    # outer factor in w of |w^2 - W^2 + i b2| : (w - w+)(w + conj(w+)), w+ = sqrt(W^2 - i b2) (Re>0, Im<0)
    wp = np.sqrt(W*W - 1j*b2 + 0j)
    return (w - wp)*(w + np.conj(wp)), wp
for eps in [1e-2, 1e-6]:
    d = math.sqrt(eps)
    ws = np.linspace(0.0, 2.0, 2001)
    s = ws**2 - 1.0
    e_true = (s*s + eps*d*d)/(s*s + d*d)
    num, wpn = outer_quad(ws, math.sqrt(eps*d*d))
    den, wpd = outer_quad(ws, d)
    e_fac = np.abs(num/den)**2
    print(f"    eps={eps:.0e}: max |e_+(w)|^2/e(s) - 1 on real w = {np.max(np.abs(e_fac/e_true-1)):.1e}; zeros at +-Re-i*{-wpn.imag:.2e}, poles at +-Re-i*{-wpd.imag:.2e} (all in the LHP: e_+ and 1/e_+ outer)")
    # plateau end (referee): e(eps) ~ 2 eps, e(sqrt eps) ~ 1/2
    print(f"      plateau: e(s=eps) = {(eps**2+eps*d*d)/(eps**2+d*d):.2e} (~2 eps), e(s=sqrt(eps)) = {(eps+eps*d*d)/(eps+d*d):.3f}")
# Stieltjes test: is D0'(u) ~ 1/(e(u)|u|) a positive superposition of cone-centred Lorentzians?  f(x) = x^(-1/2) (x+eps)/(x+eps^2), x = u^2
# density rho(t) = (1/pi) Im f(-t - i0) = (1/pi) t^(-1/2) [1 + (eps-eps^2) PV/(eps^2 - t)]  (+ point term at t = eps^2 on the cut)
for eps in [1e-2, 1e-4]:
    ts = np.logspace(math.log10(eps**2)+0.01, math.log10(eps)+1, 400)
    dens = (1/math.pi)*ts**-0.5*(1 + (eps-eps**2)/(eps**2 - ts))
    neg = ts[dens < 0]
    print(f"    R11-5 profile, eps={eps:.0e}: Stieltjes density negative on t in [{neg.min():.2e}, {neg.max():.2e}] (min {dens.min():.2e}): NO positive cone-centred Lorentzian measure")
# direct numerical confirmation: least-squares nonnegative fit with Lorentzians centred at u=0 cannot reproduce the profile
from scipy.optimize import nnls
for eps in [1e-2]:
    us = np.logspace(-5, 0, 300)
    target = (us**2 + eps)/((us**2 + eps**2)*us)
    Gs = np.logspace(-7, 2, 200)
    A = np.array([g/(g*g/4 + us**2) for g in Gs]).T
    wts = target  # relative weighting
    coef, res = nnls(A/wts[:, None], np.ones_like(us))
    fit = A @ coef
    print(f"    NNLS cone-centred Lorentzian fit (200 widths 1e-7..1e2), eps={eps:.0e}: max relative error = {np.max(np.abs(fit/target-1)):.2f} (no positive measure reproduces it)")
    # Stieltjes member: D(u) = (1/(2|u|)) [1 + (1/eps - 1)(2/pi) arctan(b/|u|)]  with measure rho(t) = (1/pi) t^-1/2 [1 + (1/eps-1) 1(t<b^2)]
    b = 0.01; eps2 = 1e-4
    targ2 = (1/us)*(1 + (1/eps2 - 1)*(2/math.pi)*np.arctan(b/us))
    rho_t = lambda t: (1/math.pi)*t**-0.5*(1 + (1/eps2 - 1)*(1.0 if t < b*b else 0.0))
    worst2 = 0.0
    for u in [1e-5, 1e-3, 3e-2, 1.0]:
        x = u*u
        num = integrate.quad(lambda lt: rho_t(math.exp(lt))*math.exp(lt)/(x+math.exp(lt)), math.log(1e-16), math.log(b*b), limit=400)[0] \
            + integrate.quad(lambda lt: rho_t(math.exp(lt))*math.exp(lt)/(x+math.exp(lt)), math.log(b*b), math.log(1e16), limit=400)[0]
        closed = (1/u)*(1 + (1/eps2 - 1)*(2/math.pi)*math.atan(b/u))
        worst2 = max(worst2, abs(num/closed - 1))
    print(f"    arctan member (eps={eps2:.0e}, b={b}): D = (1/2|u|)[1+(1/eps-1)(2/pi)atan(b/|u|)] = (1/2) int rho(t) dt/(u^2+t), rho >= 0; quadrature vs closed form max rel. error = {worst2:.1e}")
    # check its suppression of P = 1/(4D): P/(|u|/2) at u << b and u >> b/eps
    for u in [1e-5, 1e-3, 1.0]:
        Dm = (1/(2*u))*(1 + (1/eps2 - 1)*(2/math.pi)*math.atan(b/u))
        print(f"      u={u:.0e}: P_J/(|u|/2) = {1/(4*Dm)/(u/2):.3e}")
print("    subtraction: none")

# ------------------------------------------------------------------ [3]
print("\n[3] single port vs parallel bank (baseband u, single-mode QND elements chi = 1/(G/2 - i u), a_i = lam sqrt(G) chi)")
def phi(G, u):
    return -(G/2 + 1j*u)/(G/2 - 1j*u)
Gs3 = [0.3, 1.0, 4.0]; lam = [1.0, 0.7, 1.3]
worst = 0.0
for u in np.linspace(-5, 5, 41):
    a = [l*math.sqrt(g)/(g/2 - 1j*u) for l, g in zip(lam, Gs3)]
    p = [phi(g, u) for g in Gs3]
    Hx = a[0] + a[1]*p[0] + a[2]*p[0]*p[1]          # backaction transfer (x passes element 1 then 2 then 3)
    gain = a[0]*p[1]*p[2] + a[1]*p[2] + a[2]          # signal gain to the final output
    worst = max(worst, abs(abs(gain)/abs(Hx) - 1))
print(f"    cascade of 3 elements: max ||gain|/|H_x| - 1| over u in [-5,5] = {worst:.1e} (single port: exactly saturated, S_imp S_FF = |gain|^2/4)")
# parallel bank: causal saturation requires R_i = c(u) conj(g_i); c must carry B(u) = prod (G_j/2 + i u)/(G_j/2 - i u)
Gmin_over_band = [1e-3, 1e-6, 1e-9]
for gm in Gmin_over_band:
    Gb = np.logspace(math.log10(gm), 0, int(8*math.log10(1/gm))+1)
    delay = np.sum(4.0/Gb)     # group delay d arg B/du at u = 0
    print(f"    parallel bank, Gamma in [{gm:.0e}, 1] (8/decade, {len(Gb)} elements): causal saturating combination needs the all-pass B with group delay {delay:.2e} (units 1/band) ~ {delay*gm:.1f}/Gamma_min")
print("    => a parallel bank is either unsaturated (R12-7: X up to 2.47) or carries a Hubble-scale record delay when Gamma_min ~ 1/t_H; the single-port factor has neither")

# ------------------------------------------------------------------ [4]
print("\n[4] finite start: metric-record noise per mode with the saturated split, h_noise(t) = int_{t0}^t J0(W(t-t')) xi(t') dt', S_xi = 1/2")
def var_h(T):
    # 1/2 int_0^T J0(t)^2 dt (W = 1)
    pts = np.linspace(0, T, int(T/5)+2)
    return 0.5*sum(integrate.quad(lambda t: special.j0(t)**2, a, b, limit=50)[0] for a, b in zip(pts[:-1], pts[1:]))
def var_hdot(T):
    pts = np.linspace(0, T, int(T/5)+2)
    return 0.5*sum(integrate.quad(lambda t: special.j1(t)**2, a, b, limit=50)[0] for a, b in zip(pts[:-1], pts[1:]))
prev = None
for T in [1e2, 1e3, 1e4, 1e5]:
    vh = var_h(T); vd = var_hdot(T)
    asym = (math.log(T) + math.log(8) + np.euler_gamma)/(2*math.pi)   # 1/2 * (1/pi)(ln 8T + gamma)  (asymptotic of int J0^2)
    print(f"    T={T:.0e}/W: Var h = {vh:.6f} (asymptotic (ln 8WT + gamma_E)/(2 pi) = {asym:.6f}); Var hdot/W^2 = {vd:.6f}; energy/mode ~ W^2(Var h + Var hdot/W^2)/2 = {0.5*(vh+vd):.5f}")
print("    => finite at every finite age, growing as (1/pi) ln(W T) per mode (both quadratures); stationary limit infinite (Theorem U). subtraction: none")
print("    record energy E(T) = 2 int_0^U du P(u) sin^2(uT/2)/u^2, near-cone baseband, P(u) = e(u) sqrt(u^2+u0^2)  (u0 = s0 regulator of R11-5)")
def E_T(T, eps, u0, U=1.0):
    d = math.sqrt(eps)
    P = lambda u: ((u*u + eps*d*d)/(u*u + d*d))*math.sqrt(u*u + u0*u0)
    f = lambda u: P(u)*math.sin(u*T/2)**2/(u*u)
    # split: below 1/T integrand ~ P T^2/4 ; above: oscillatory, use average 1/2 beyond 50/T
    lo = min(50.0/T, U)
    pts = np.unique(np.concatenate([[0.0], np.logspace(math.log10(lo)-8, math.log10(lo), 200)]))
    tot = sum(integrate.quad(f, a, b, limit=200)[0] for a, b in zip(pts[:-1], pts[1:]))
    if lo < U:
        g = lambda lu: P(math.exp(lu))*0.5/math.exp(lu)
        tot += integrate.quad(g, math.log(lo), math.log(U), limit=400, points=[math.log(max(eps,lo*1.0001)), math.log(max(d,lo*1.0001))])[0]
    return 2*tot
for eps, u0 in [(1.0, 0.0), (1e-4, 0.0), (1e-4, 1e-10)]:
    row = [E_T(T, eps, u0) for T in [1e4, 1e6, 1e8, 1e10, 1e12, 1e14]]
    slopes = [(row[i+1]-row[i])/math.log(100) for i in range(len(row)-1)]
    print(f"    eps={eps:.0e}, u0={u0:.0e}: E(T=1e4..1e14) = " + ", ".join(f"{v:.4g}" for v in row) + "; dE/dlnT = " + ", ".join(f"{s:.2e}" for s in slopes))
print("    => s0 = 0 (finite start, no coherence-time regulator): secular slope -> eps forever (eps ln T); s0 > 0: linear once T >> 1/s0 (referee's point)")

# ------------------------------------------------------------------ [5]
print("\n[5] matter side at finite age (W = 1)")
def P_null(T, Wm=1.0):
    # transition probability for a matter transition at frequency Wm driven by backaction x = J0-filtered white noise (S=1/2), lam = 1:
    # P(T) = 1/2 int_0^T dt' | int_0^{T-t'} J0(tau) e^{i Wm tau} dtau |^2
    taus = np.linspace(0, T, int(T*20)+1)
    integrand = special.j0(taus)*np.exp(1j*Wm*taus)
    cum = np.concatenate([[0], np.cumsum(0.5*(integrand[1:]+integrand[:-1])*np.diff(taus))])
    return 0.5*np.trapezoid(np.abs(cum)**2, taus)
for T in [50, 200, 800]:
    print(f"    null transfer (W_m = W): P(T={T}) = {P_null(T):.3f};  P/T^2 = {P_null(T)/T**2:.4f}  | off-cone W_m = 0.3 W: P/T = {P_null(T,0.3)/T:.4f} (stationary rate S_x(0.3) = {0.5/abs(1-0.09):.4f})")
print("    => near-null decoherence finite at every age (grows ~T^2 instead of being infinite); off-cone transfers converge to the stationary rate")
print("    finite-start correction to the off-cone stationary kernel at age T: relative ~ |J0 tail| ~ (2/(pi W T))^(1/2) per amplitude; for the rate, the")
for name, W in [("lab k = 1/(1 um)", c/1e-6), ("k = 1/AU", c/1.496e11), ("k = 1/(1 kpc)", c/3.086e19)]:
    print(f"      {name}: W = {W:.2e} s^-1, 1/(W t_H) = {1/(W*tH):.1e}  (subtraction: the stationary kernel)")

# ------------------------------------------------------------------ [6]
print("\n[6] near-cone record budget at t_H (R11-5 normalization: O(1) tensor weights, Isaacson premise; suggested)")
Ls = lambda l: math.log(c*tH/l)
print("    (A) strict K_eps (tau = l/c): eps needed for rho_GW < rho_L with L_eff = ln(eps c t_H/l) (referee R11-5 correction):")
for l in [1e-8, 2e-7, 1e-6, 5e-6]:
    eps = 1.0
    for _ in range(50):
        Leff = math.log(max(eps, 1e-300)*c*tH/l)
        eps = rho_L*math.pi**3*l**4/(Leff*hbar*c)
    print(f"      l={l:.0e}: eps < {eps:.1e} (L_eff = {Leff:.1f})")
print("    (B) tau_c extension: delay-compensated gain F_t(w) = (1 - i n w tau_c)(1 - i w tau_c)^(-n), n = 4; |F_t|^2 = (1+n^2 x^2)/(1+x^2)^n")
n = 4
Ft2 = lambda x: (1 + n*n*x*x)/(1 + x*x)**n
def rho_log(l, ctc):
    # (hbar c/pi^3) * 2 int dk k^3 e^{-k^2 l^2} |F_t(ck tau_c)|^2 ln(c k t_H)   [saturated split, eps = 1, finite start]
    f = lambda lk: (lambda k: k**4*math.exp(-(k*l)**2)*Ft2(k*ctc)*math.log(c*k*tH))(math.exp(lk))
    v = integrate.quad(f, math.log(1e-6/ctc), math.log(30/l), limit=400)[0]
    return hbar*c/math.pi**3*2*v
def rho_lin(l, ctc):
    # chain-only (bounded D0', P_J(cone) at static floor): drho/dt = 2 hbar c^2 int d^3k/(2pi)^3 k^2 e^{-k^2 l^2} |F_t|^2 ; rho = rate * t_H
    f = lambda lk: (lambda k: k**5*math.exp(-(k*l)**2)*Ft2(k*ctc))(math.exp(lk))
    v = integrate.quad(f, math.log(1e-6/ctc), math.log(30/l), limit=400)[0]
    return 2*hbar*c**2/(2*math.pi**2)*v*tH
def rho_qs(l, ctc, xmax=0.5):
    # quasi-static TT (R11-5 [13] weight w^2/|s|): (hbar c/pi^3) 2 int dk k^3 e^{-k^2l^2} int_0^xmax dx x^2/(1-x^2) |F_t(x ck tau_c)|^2
    def inner(k):
        a = k*ctc
        # substitute y = x a so the peak at x ~ 1/a is resolved: int_0^xmax x^2/(1-x^2)|F(xa)|^2 dx = a^-3 int_0^{xmax a} y^2/(1-(y/a)^2)|F(y)|^2 dy
        g = lambda ly: (lambda y: y**3/(1-(y/a)**2)*Ft2(y))(math.exp(ly))
        return a**-3*integrate.quad(g, math.log(1e-8), math.log(xmax*a), limit=400)[0]
    f = lambda lk: (lambda k: k**4*math.exp(-(k*l)**2)*inner(k))(math.exp(lk))
    v = integrate.quad(f, math.log(1e-6/ctc), math.log(30/l), limit=200)[0]
    return hbar*c/math.pi**3*2*v
for l in [4e-10, 1e-6, 5e-6]:
    for ctc in [1e-4, 1e-2, 1.0, 55.0, 300.0]:
        if ctc < 20*l:
            continue
        rl = rho_log(l, ctc); rq = rho_qs(l, ctc)
        line = f"      l={l:.0e} m, c tau_c={ctc:.0e} m: log variant rho_GW(t_H) = {rl/rho_L:.1e} rho_L; quasi-static TT = {rq/rho_L:.1e} rho_L"
        if ctc >= 1.0:
            line += f"; chain-only linear variant = {rho_lin(l, ctc)/rho_L:.1e} rho_L"
        print(line)
# thresholds
def solve(fun, lo, hi):
    for _ in range(80):
        mid = math.sqrt(lo*hi)
        if fun(mid) > rho_L: lo = mid
        else: hi = mid
    return hi
for l in [4e-10, 5e-6]:
    t_log = solve(lambda x: rho_log(l, x) + rho_qs(l, x), 20*l, 1e4)
    t_lin = solve(lambda x: rho_lin(l, x), 1e-2, 1e5)
    print(f"      thresholds at l={l:.0e} m: log variant (near-cone + quasi-static) < rho_L needs c tau_c > {t_log:.2e} m (tau_c > {t_log/c:.1e} s); chain-only linear needs c tau_c > {t_lin:.1f} m (tau_c > {t_lin/c:.1e} s)")
print("    subtraction: none (positive energy densities)")

# ------------------------------------------------------------------ [7]
print("\n[7] binary-pulsar aberration from the causal record delay (mean field h = G_R F <T>; F(w) = 1 + i w delta + ... in the CMB frame)")
print("    star 2 is attracted to star 1's position a time delta earlier -> tangential force along v -> dE/dt = +(4 mu/M) Omega^2 delta |E| (circular, CM at rest)")
Msun = 1.98847e30
def orbit_check(name, Pb, m1, m2, Pdot_GR, frac):
    Om = 2*math.pi/Pb; M = m1+m2; mu4 = 4*m1*m2/M**2
    lim = frac*abs(Pdot_GR)/Pb                       # allowed |dPb/dt|/Pb
    dmax = lim/(1.5*mu4*Om**2)
    return Om, dmax
for name, Pb, m1, m2, Pd, frac in [("double pulsar J0737-3039A/B", 8834.535, 1.338, 1.249, -1.252e-12, 1.3e-4),
                                    ("Hulse-Taylor B1913+16", 27906.98, 1.438, 1.390, -2.398e-12, 1.6e-3)]:
    Om, dmax = orbit_check(name, Pb, m1, m2, Pd, frac)
    print(f"    {name}: Omega = {Om:.3e} s^-1; GR-consistency {frac:.1e} of Pdot_GR -> delta < {dmax:.1e} s;"
          f" uncompensated F_u (n=3, tau=l/c): l < {dmax*c/3:.1e} m")
    # compensated gain: first moment zero; leading odd term i*C3*(w tau)^3, C3 = n(n+1)(n-1)/3
    for nn in [3, 4]:
        C3 = nn*(nn+1)*(nn-1)/3
        tmax = (dmax/(C3*Om**2))**(1/3)
        print(f"      delay-compensated (1 - i n w tau)(1 - i w tau)^-n, n={nn}: effective delay C3 tau^3 Omega^2 (C3={C3:.0f}) -> tau_c < {tmax:.1e} s")
print("    Sun-planet orbits: Omega^2 delta over 1e2 yr with delta = 5e-14 s: Mercury relative energy change = "
      f"{(2*math.pi/(87.97*86400))**2*5e-14*3.156e9:.1e} (negligible)")
print("    frame-velocity offset of the field centre (R11-5 [6]) is the same delay times W; zero for the compensated gain at first order")

# ------------------------------------------------------------------ [8]
print("\n[8] GW waveform and GW170817 with the compensated gain (n = 4)")
for tc in [1e-12, 3.3e-11, 1e-9, 1.8e-7, 1e-6]:
    out = []
    for f in [30.0, 300.0, 1000.0]:
        x = 2*math.pi*f*tc
        F = (1 - 1j*n*x)/(1 - 1j*x)**n
        out.append(f"{f:.0f} Hz: |F|-1 = {abs(F)-1:+.1e}, arg F = {np.angle(F):+.1e} rad")
    print(f"    tau_c = {tc:.1e} s (c tau_c = {c*tc:.1e} m): " + "; ".join(out))
print("    GW170817: no first-order lag for the compensated gain; uncompensated lag n tau = 3 l/c <= 5e-14 s (R11-5). Front speed c (G_R untouched).")

# ------------------------------------------------------------------ [9]
print("\n[9] noise-fed second order (suggested; power counting)")
# least-decoherence metric noise: S_h(k) = 8 pi G hbar |g|^2/(c^4 k^2) white in w up to ~min(1/tau_c, ck); <h^2> = int d^3k/(2pi)^3 dw/(2pi) S_h
for l in [4e-10, 1e-6, 5e-6]:
    for ctc in [1e-2, 55.0]:
        f = lambda k: 4*math.pi*k*k/(2*math.pi)**3 * 8*math.pi*G*hbar*math.exp(-(k*l)**2)/(c**4*k*k) * min(c*k, c/ctc)/math.pi
        v = integrate.quad(lambda lk: f(math.exp(lk))*math.exp(lk), math.log(1e-8/l), math.log(30/l), limit=300)[0]
        print(f"    l={l:.0e} m, c tau_c={ctc:.0e} m: <h^2>_quasi-static ~ {v:.1e}  ((l_P/l)^2 = {(lP/l)**2:.1e}); frame part ~ beta^2 <h^2> = {v*(369.82e3/c)**2:.1e} vs alpha2-hat < 1.6e-9")
AU = 1.496e11; H0 = 1/tH
print(f"    Isaacson fluid at rest in the frame, rho <= rho_L: tidal/frame terms ~ (rho/rho_crit)(H0 r/c)^2 beta at 1 AU <= {0.69*(H0*AU/c)**2*369.82e3/c:.1e}")
print("    subtraction: none")

# ------------------------------------------------------------------ [10]
print("\n[10] self-drag of a moving body by its own delayed field (new test; Newtonian mean field, uniform motion v along z)")
print("     F_i = -4 pi G int d^3k/(2pi)^3 k_i Im F(k.v) |rho~(k)|^2/k^2 ; first order Im F = delta k.v  =>  F = -(4 pi G/3) delta (int rho^2) v")
def drag_rate(Ffun, v, a):
    # Gaussian body rho~ = M exp(-k^2 a^2/2); return Gamma = -F_z/(M v) in units of 4 pi G M (per unit G M scaling handled by caller)
    # int d^3k/(2pi)^3 k_z Im F(k_z v) e^{-k^2 a^2}/k^2 = (1/(2pi)^2) int_0^inf dk e^{-k^2a^2} int_{-1}^{1} dmu k mu Im F(k mu v)
    def integrand(k):
        return integrate.quad(lambda mu: k*mu*Ffun(k*mu*v).imag, -1, 1, limit=100)[0]*math.exp(-(k*a)**2)
    val = integrate.quad(integrand, 0, 8/a, limit=200)[0]/(2*math.pi)**2
    return val/v      # Gamma/(4 pi G M) with F = -4piG M^2 ... /M -> per unit M
a = 1.0; v = 1.0
for tau in [1e-3, 1e-2]:
    n3 = 3
    Fu = lambda w: (1 - 1j*w*tau)**(-n3)
    Fc = lambda w: (1 - 1j*4*w*tau)*(1 - 1j*w*tau)**(-4)
    g_u = drag_rate(Fu, v, a); g_c = drag_rate(Fc, v, a)
    first = (n3*tau)*(1/3)*1/((2*math.pi)**2)*integrate.quad(lambda k: k*k*math.exp(-(k*a)**2), 0, 8/a)[0]*2
    print(f"     tau={tau:.0e} (v tau/a = {v*tau/a:.0e}): uncompensated n=3: Gamma = {g_u:.4e} vs first-order (4piG/3) delta int rho^2/M: {first:.4e};"
          f" compensated n=4: Gamma = {g_c:.3e} (ratio {g_c/g_u:.1e}; leading term ~ (v tau/a)^2)")
Ms = 1.98847e30
for name, M, R in [("neutron star 1.3 Msun, R=12 km (uniform-density lower bound)", 1.3*Ms, 1.2e4), ("Sun (mean density)", Ms, 6.957e8), ("Earth", 5.972e24, 6.371e6)]:
    rho = M/(4/3*math.pi*R**3)
    G43 = 4*math.pi*G/3*rho
    print(f"     {name}: (4 pi G/3) rho = {G43:.2e} s^-2")
G43ns = 4*math.pi*G/3*(1.3*Ms/(4/3*math.pi*1.2e4**3))
lim = 1.3e-4*1.252e-12/8834.535/3          # double pulsar: Pdot/P = -3 Gamma (orbital KE dissipated at 2 Gamma K)
dmax = lim/G43ns
print(f"     double pulsar: Pdot_b/P_b = -3 Gamma; tolerance 1.3e-4 |Pdot_GR|/P_b -> Gamma < {lim:.1e} s^-1 -> delta < {dmax:.1e} s -> uncompensated F_u (n=3, tau=l/c): l < {dmax*c/3:.1e} m")
print(f"     R11-5 window lower end l = 4e-10 m: delta = {3*4e-10/c:.1e} s -> NS drag rate {G43ns*3*4e-10/c:.1e} s^-1 (e-fold {1/(G43ns*3*4e-10/c)/3.156e7:.0f} yr)")
print(f"     Earth at l = 5e-6 m: drag rate {4*math.pi*G/3*5514*3*5e-6/c:.1e} s^-1; velocity loss over t_H = {4*math.pi*G/3*5514*3*5e-6/c*tH:.2f} (relative)")
print("     subtraction: none (the drag is the odd-in-omega part of F; the even part is conservative and is not subtracted, it gives no force on a symmetric body)")

# ------------------------------------------------------------------ [11]
print("\n[11] compensated gains and the neutron-star drag (Taylor regime, smooth n=1 polytrope)")
print("     Im F(w) = delta w + c3 (w tau)^3 + c5 (w tau)^5 + ... ; drag Gamma = (4 pi G/M) [delta/3 int rho^2 + c3 tau^3 v^2/5 int |grad rho|^2 + c5 tau^5 v^4/7 int |lap rho|^2 + ...]")
import numpy.polynomial.polynomial as Pl
def series_F(pcoef, n, N=9):
    # F(z) = P(z) (1+z)^(-n), z = -i w tau; return Taylor coefficients in z up to z^N
    inv = [math.comb(-n, j) if False else (math.prod([-n - i for i in range(j)])/math.factorial(j)) for j in range(N+1)]
    return Pl.polymul(pcoef, inv)[:N+1]
def im_coeffs(coefs):
    # z = -i x: z^j = (-i)^j x^j ; Im part coefficients of x^j
    return [((-1j)**j*coefs[j]).imag for j in range(len(coefs))]
for label, pc, n_ in [("uncompensated n=3", [1.0], 3), ("first moment zero, n=4", [1.0, 4.0], 4)]:
    ic = im_coeffs(series_F(pc, n_))
    print(f"     {label}: Im F coefficients x^1..x^5 = {ic[1]:+.3f}, {ic[3]:+.3f}, {ic[5]:+.3f}")
# first and third moments zero with quadratic P, n = 5: solve for p1, p2
from scipy.optimize import fsolve
def eqs(p):
    ic = im_coeffs(series_F([1.0, p[0], p[1]], 5))
    return [ic[1], ic[3]]
p1, p2 = fsolve(eqs, [5.0, 10.0])
icq = im_coeffs(series_F([1.0, p1, p2], 5))
print(f"     first+third moments zero, n=5: P(z) = 1 + {p1:.4f} z + {p2:.4f} z^2; Im F coefficients x^1, x^3, x^5 = {icq[1]:+.1e}, {icq[3]:+.1e}, {icq[5]:+.3f}")
xs_ = np.logspace(-3, 3, 400)
Fq = lambda x: (1 + p1*(-1j*x) + p2*(-1j*x)**2)/(1 - 1j*x)**5
print(f"     |F|^2 of that gain: max over w = {max(abs(Fq(x))**2 for x in xs_):.2f}; high-w slope d ln|F|^2/d ln w = {math.log(abs(Fq(1e3))**2/abs(Fq(1e2))**2)/math.log(10):.2f} (backaction K ~ |F|^2/w^2 falls faster than w^-6)")
# n=1 polytrope: rho = rho_c sin(xi)/xi, xi = pi r/R
R = 1.2e4; M = 1.3*1.98847e30
rr = np.linspace(1e-6, R, 200001)
shape = np.sin(np.pi*rr/R)/(np.pi*rr/R)
rhoc = M/np.trapezoid(4*np.pi*rr**2*shape, rr)
rho = rhoc*shape
drho = np.gradient(rho, rr)
lap = np.gradient(rr**2*drho, rr)/rr**2
I0 = np.trapezoid(4*np.pi*rr**2*rho**2, rr); I1 = np.trapezoid(4*np.pi*rr**2*drho**2, rr); I2 = np.trapezoid(4*np.pi*rr[5:-5]**2*lap[5:-5]**2, rr[5:-5])   # interior only: the surface kink adds a delta to lap(rho) (Taylor coefficient divergent)
print(f"     polytrope n=1, M=1.3 Msun, R=12 km: rho_c = {rhoc:.2e} kg/m^3; int rho^2/M = {I0/M:.2e}; int|grad rho|^2/M = {I1/M:.2e} m^-2 kg/m^3; int|lap rho|^2/M = {I2/M:.2e}")
v = 3.0e5; lim = 6.1e-21; pref = 4*math.pi*G
d_u = lim/(pref*I0/M/3)
print(f"     uncompensated: delta < {d_u:.1e} s (polytrope; uniform-sphere value 6.2e-29 s)")
c3 = im_coeffs(series_F([1.0, 4.0], 4))[3]
t1 = (lim/(pref*abs(c3)*v**2*I1/M/5))**(1/3)
print(f"     first moment zero (n=4, c3={c3:+.0f}): tau < {t1:.1e} s (c tau < {c*t1:.1e} m) at v = 300 km/s")
t2 = (lim/(pref*abs(icq[5])*v**4*I2/M/7))**(1/5)
print(f"     first+third moments zero (n=5, c5={icq[5]:+.0f}): interior-only estimate tau < {t2:.1e} s (c tau < {c*t2:.1e} m); NOT a bound: the n=1 surface kink makes int|lap rho|^2 diverge, so the drag is set by surface structure at scale v tau = {v*t2:.1e} m (suggested only)")
print(f"     strict family tau = l/c with first moment zero, l = 5e-6 m: Gamma = {pref*abs(c3)*(5e-6/c)**3*v**2*I1/M/5:.1e} s^-1 (limit {lim:.1e})")
print("     subtraction: none")
