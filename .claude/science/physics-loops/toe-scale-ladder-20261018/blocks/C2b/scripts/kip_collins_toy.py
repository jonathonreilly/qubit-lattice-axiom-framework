#!/usr/bin/env python3
"""C2b / KI+ radiative test (toy, Euclidean lattice, a = 1).

Model: real scalar phi with tree kinetic form sum_mu phat_mu^2 (B4), Yukawa coupling g phi psibar psi,
Wilson fermion S^{-1}(k) = i sum_mu gamma_mu s_mu(k) + M(k).
One loop: K_phi(p) = phat^2 + Pi(p),  Pi(p) = g^2 int_BZ d^4k/(2pi)^4 tr[S(k) S(k+p)]
(from Gamma = -Tr ln(D + g phi)), and tr[S S'] = 4 (-s.s' + M M') / (D D'), D = s^2 + M^2.
Write Pi(p) = Pi(0) + g^2 sum_mu Z_mu p_mu^2 + O(p^4). The induced dimension-4 speed shift of phi is
  delta_phi = (1/2) ln[(1 + g^2 Z_s)/(1 + g^2 Z_0)] ~ (g^2/2)(Z_s - Z_0).

Variants (all have the SAME dimension-4 tree form for the fermion, c_t = c_s = 1: 'KI+_w' holds):
  SYM      s_mu = sin k_mu, M = m + r sum_mu (1 - cos k_mu)         -> full action B4-invariant (KI+_G)
  T3(eps)  s_0 = sin k0 (1 - eps/3 + (eps/3) cos k0): k0 - (1+eps) k0^3/6 + ...  (dimension-6 time/space mismatch)
  RT(rt)   Wilson term r_t (1 - cos k0) + r_s sum_j (1 - cos k_j), r_t != r_s   (dimension-5 mismatch)
Checks (expected constants fixed independently of the code):
  * SYM: Z_0 = Z_s to rounding (B4 relabelling of the symmetric node set).
  * log slope dZ_0/d ln(1/m) -> 1/(4 pi^2) (continuum Feynman-parameter computation, done by hand in NOTE.md sec. 4).
  * T3, RT: Z_0 - Z_s tends to a nonzero constant as m a -> 0 (Collins-type: not suppressed by the cutoff).
Claim type: numerical (product Gauss-Legendre quadrature with a sinh map; convergence shown, not certified).
"""
import sys
import time
import numpy as np

PASS = FAIL = 0


def check(name, ok, tag='numerical'):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"{'PASS' if ok else 'FAIL'} [{tag}] {name}", flush=True)


def nodes(N, m):
    """1D nodes/weights on [-pi, pi]: Gauss-Legendre in u, k = pi sinh(c u)/sinh(c)."""
    c = max(1.0, np.log(2*np.pi/m))
    u, w = np.polynomial.legendre.leggauss(N)
    k = np.pi*np.sinh(c*u)/np.sinh(c)
    jac = np.pi*c*np.cosh(c*u)/np.sinh(c)
    return k, w*jac/(2*np.pi)


def make_variant(kind, par):
    def s0(k):
        if kind == 'T3':
            return np.sin(k)*(1 - par/3 + (par/3)*np.cos(k))
        return np.sin(k)
    rt = par if kind == 'RT' else 1.0
    return s0, rt


def Zcoeffs(kind, par, m, N, hrel=0.1):
    """Return (Z_0, Z_1) per unit g^2: half the second p-derivative of Pi/g^2 along e_0 and e_1."""
    k, w = nodes(N, m)
    s0f, rt = make_variant(kind, par)
    rs = 1.0
    h = hrel*m
    shifts = [-2*h, -h, h, 2*h]
    # 1D tables
    S0 = s0f(k); Sj = np.sin(k)
    W0 = rt*(1 - np.cos(k)); Wj = rs*(1 - np.cos(k))
    S0sh = [s0f(k + d) for d in shifts]; W0sh = [rt*(1 - np.cos(k + d)) for d in shifts]
    Sjsh = [np.sin(k + d) for d in shifts]; Wjsh = [rs*(1 - np.cos(k + d)) for d in shifts]
    # 3D spatial arrays (axes 1,2,3)
    s1 = Sj[:, None, None]; s2 = Sj[None, :, None]; s3 = Sj[None, None, :]
    wsp = Wj[:, None, None] + Wj[None, :, None] + Wj[None, None, :]
    ssp2 = s1**2 + s2**2 + s3**2
    w3 = w[:, None, None]*w[None, :, None]*w[None, None, :]
    P0 = 0.0; P_t = np.zeros(4); P_x = np.zeros(4)
    for i in range(N):
        M = m + W0[i] + wsp
        D = S0[i]**2 + ssp2 + M**2
        wt = w[i]*w3
        P0 += np.sum(wt*(-(S0[i]**2 + ssp2) + M*M)/(D*D))
        for a in range(4):
            # shift along time axis: only k0 -> k0 + d
            s0p = S0sh[a][i]; Mp = m + W0sh[a][i] + wsp
            Dp = s0p**2 + ssp2 + Mp**2
            P_t[a] += np.sum(wt*(-(S0[i]*s0p + ssp2) + M*Mp)/(D*Dp))
            # shift along x axis: k1 -> k1 + d
            s1p = Sjsh[a][:, None, None]
            Mpx = m + W0[i] + Wjsh[a][:, None, None] + Wj[None, :, None] + Wj[None, None, :]
            Dpx = S0[i]**2 + s1p**2 + s2**2 + s3**2 + Mpx**2
            P_x[a] += np.sum(wt*(-(S0[i]**2 + s1*s1p + s2**2 + s3**2) + M*Mpx)/(D*Dpx))
    P0 *= 4; P_t *= 4; P_x *= 4
    # 5-point second derivative: f'' = (-f(2h) + 16 f(h) - 30 f(0) + 16 f(-h) - f(-2h)) / (12 h^2)
    d2 = lambda P: (-P[0] + 16*P[1] - 30*P0 + 16*P[2] - P[3])/(12*h*h)
    return d2(P_t)/2, d2(P_x)/2


t0 = time.time()
MS = (0.4, 0.2, 0.1, 0.05, 0.025, 0.0125, 0.00625, 0.003125)
NS = (72, 96)
print("Z_mu per unit g^2 (coefficient of p_mu^2 in Pi/g^2)")
res = {}
for kind, par in (('SYM', 0.0), ('T3', 0.5), ('T3', 0.25), ('RT', 0.5)):
    for m in MS:
        for N in NS:
            z0, z1 = Zcoeffs(kind, par, m, N)
            res[(kind, par, m, N)] = (z0, z1)
            print(f"  {kind:3s} par={par:4.2f} m={m:8.6f} N={N}: Z_0={z0:+.9f} Z_s={z1:+.9f} Z_0-Z_s={z0-z1:+.6e}"
                  f"  [{time.time()-t0:5.0f}s]", flush=True)
A = lambda kind, par, m, N=NS[-1]: res[(kind, par, m, N)][0] - res[(kind, par, m, N)][1]

# 1. B4 symmetric: exact relabelling symmetry of the node set
mx = max(abs(A('SYM', 0.0, m, N)) for m in MS for N in NS)
check(f'SYM (full action B4-invariant): |Z_0 - Z_s| <= 1e-9 at every m, N (max {mx:.1e})', mx < 1e-9)
# 2. convergence in N
for kind, par in (('SYM', 0.0), ('T3', 0.5), ('T3', 0.25), ('RT', 0.5)):
    dv = max(abs(res[(kind, par, m, NS[0])][0] - res[(kind, par, m, NS[1])][0]) for m in MS)
    da = max(abs(A(kind, par, m, NS[0]) - A(kind, par, m, NS[1])) for m in MS)
    check(f'{kind} par={par}: quadrature converged: max |Z_0(N={NS[0]}) - Z_0(N={NS[1]})| = {dv:.1e} < 1e-6, anisotropy {da:.1e} < 1e-7',
          dv < 1e-6 and da < 1e-7)
# 3. log slope vs continuum 1/(4 pi^2)
z = [res[('SYM', 0.0, m, NS[-1])][0] for m in MS]
slopes = np.array([(z[i+1] - z[i])/np.log(2) for i in range(len(MS) - 1)])
target = 1/(4*np.pi**2)
dev = np.abs(slopes - target)
print(f"  SYM log slopes dZ_0/dln(1/m): {np.round(slopes, 6)}  (continuum 1/(4 pi^2) = {target:.6f})")
print(f"  |slope - 1/(4pi^2)|: {np.array2string(dev, precision=2)}")
check('SYM: last log slope within 5% of the continuum value 1/(4 pi^2)', dev[-1] < 0.05*target)
check('SYM: deviation from 1/(4 pi^2) decreases monotonically over the last four steps (O(m a) Wilson corrections)',
      all(dev[i+1] < dev[i] for i in range(len(dev) - 4, len(dev) - 1)))
# 4. Collins-type: anisotropy tends to a nonzero constant as m -> 0
Ainf = {}
for kind, par in (('T3', 0.5), ('T3', 0.25), ('RT', 0.5)):
    a = np.array([A(kind, par, m) for m in MS])
    steps = np.abs(np.diff(a))
    r = max(steps[-3:]/steps[-4:-1])
    tailb = steps[-1]*r/(1 - r) if r < 1 else np.inf
    Ainf[(kind, par)] = a[-1] + np.sign(a[-1] - a[-2])*tailb
    print(f"  {kind} par={par}: Z_0 - Z_s vs m: {np.array2string(a, precision=6)}")
    print(f"     step sizes {np.array2string(steps, precision=2)}; max ratio of last three = {r:.3f}; geometric tail bound {tailb:.2e}")
    check(f'{kind} par={par}: Z_0 - Z_s converges as m a -> 0 (step ratio {r:.2f} < 0.8) to a NONZERO limit '
          f'(|A(m_min)| = {abs(a[-1]):.3e} > 5 x tail bound {tailb:.2e})', r < 0.8 and abs(a[-1]) > 5*tailb)
    check(f'{kind} par={par}: |Z_0 - Z_s| grows as m a decreases (not suppressed by a power of m a)', abs(a[-1]) > abs(a[0]))
ratio = A('T3', 0.5, MS[-1])/A('T3', 0.25, MS[-1])
print(f"  T3: ratio A(eps=0.5)/A(eps=0.25) at m_min = {ratio:.4f} (linear response would give 2)")
check('T3: induced anisotropy is approximately linear in the dimension-6 mismatch eps (ratio in [1.7, 2.3])', 1.7 < ratio < 2.3)
for (kind, par), v in Ainf.items():
    C = v/par*16*np.pi**2/2 if kind == 'T3' else v*16*np.pi**2/2
    unit = 'eps' if kind == 'T3' else '1 (r_t = 0.5, r_s = 1)'
    print(f"  {kind} par={par}: extrapolated A_inf ~ {v:+.4e};  delta_phi = (g^2/2)(Z_s - Z_0) = C (g^2/16pi^2) x {unit},"
          f"  C ~ {-C:+.3f}")
print("  QED-size illustration: g^2/16pi^2 -> alpha/4pi = 5.81e-4; with C ~ 0.3 and eps ~ 0.05 the cutoff mismatch is ~ 1e-5.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
