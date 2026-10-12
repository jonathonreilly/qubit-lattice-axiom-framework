#!/usr/bin/env python3
"""C5 R9-4 checks (worker, Opus 5.5). Every number in R9-4_report.md comes from here.
Sections:
 [1] variant (i): far field of a spacelike-supported form factor F = theta(-s), finite-part prescription
 [2] variants (i)/(ii): block positivity of the CQ trade-off matrix per spin channel
 [3] variant (ii): scalar admixture -> gamma; trace-only kernel -> gamma = -1; Cassini
 [4] variant (iii): OWD Eq.27-type spacetime-correlated kernels integrate to an ADDITIVE matter kernel
 [5] variant (iii): correlated (non-additive) measurement-feedback: Wiseman-Milburn identity,
     sub-floor total decoherence, and the two-qubit entanglement test (joint vs local meters)
 [6] variant (iii): emission-side lemma and the absorption bound (random spectral matrices)
 [7] variant (iv): R8-3 regulated ansatz excess; n >= 3 for finite vacuum energy injection;
     near-cone classical-GW content and the window it leaves (order of magnitude)
"""
import numpy as np
from scipy import integrate, special, linalg

rng = np.random.default_rng(94)
np.set_printoptions(precision=6, suppress=True)

# ---------------------------------------------------------------- [1]
print("[1] variant (i): far field of F = theta(-s) (spacelike support) for a monochromatic point source")
print("    2 pi^2 r h(r) = Pf int_w^inf k sin(kr) g(k)/(k^2-w^2) dk ; full F=1 gives (pi/2) e^{i w r} (bounded)")
w, K = 1.0, 40.0
def gk(k):  # k e^{-(k/K)^2}/(k+w), the regular part of k/(k^2-w^2)
    return k*np.exp(-(k/K)**2)/(k+w)
g0 = gk(w)
def hreg(u):
    # (g(w+u)-g(w))/u, regular at u=0
    u = np.asarray(u, dtype=float)
    small = np.abs(u) < 1e-7
    du = 1e-6
    deriv = (gk(w+du)-gk(w-du))/(2*du)
    with np.errstate(divide='ignore', invalid='ignore'):
        val = np.where(small, deriv, (gk(w+u)-g0)/np.where(small, 1.0, u))
    return float(val)
def A_of_r(r):
    # near part u in (0,1]: sin(kr) = sin(wr)cos(ur)+cos(wr)sin(ur), k = w+u
    I1 = integrate.quad(hreg, 0, 1, weight='cos', wvar=r, limit=400)[0]
    I1 += g0*(special.sici(r)[1] - np.euler_gamma - np.log(r))   # Pf int_0^1 cos(ur)/u du (scale 1)
    I2 = integrate.quad(hreg, 0, 1, weight='sin', wvar=r, limit=400)[0] + g0*special.sici(r)[0]
    near = np.sin(w*r)*I1 + np.cos(w*r)*I2
    # tail k in (w+1, inf): weight sin(kr)
    tail = integrate.quad(lambda k: gk(k)/(k-w), w+1, np.inf, weight='sin', wvar=r, limlst=200)[0]
    return near + tail
print("    r (at sin(wr)=+1)      A(r)          -(g0)*ln r     A(r)+g0*ln r")
for n in [3, 30, 300, 3000, 30000]:
    r = (np.pi/2 + 2*np.pi*n)/w
    A = A_of_r(r)
    print(f"    r={r:11.3f}  A={A:+.5f}   {-g0*np.log(r):+.5f}   {A+g0*np.log(r):+.5f}")
print(f"    g0 = g(w) = {g0:.6f}; A(r) + g0 ln r is constant => r*h grows like ln r: no finite radiation zone.")
print("    A light-cone counterterm c*delta(k^2-w^2) adds c'*sin(wr) (r-independent): it cannot cancel g0*ln r*sin(wr).")
print("    radiated power through radius r ~ r^2 |d_r h|^2 ~ (g0 ln r)^2 -> grows without bound.")

# ---------------------------------------------------------------- [2]
print("\n[2] block positivity per spin channel: M = [[P_J, F/2],[F*/2, D0]] (channels 0 and 2), D0 scalar-only")
bad = 0
for t in range(20000):
    PJ = np.diag(rng.uniform(0, 10, 2))
    D0 = np.diag([rng.uniform(0, 10), 0.0])           # no spin-2 decoherence
    F = np.diag([rng.uniform(-3, 3), rng.uniform(0.01, 3)])  # nonzero spin-2 drift
    M = np.block([[PJ, F/2], [F.T/2, D0]])
    if np.linalg.eigvalsh(M).min() < -1e-12:
        bad += 1
print(f"    draws with min eigenvalue < 0: {bad}/20000  (=> scalar decoherence cannot pay for a spin-2 drift)")
bad2 = 0
for t in range(20000):  # spacelike-supported noise: both kernels vanish at a timelike p, drift F(p) != 0
    f = rng.uniform(0.01, 3)
    M = np.array([[0.0, f/2], [f/2, 0.0]])
    if np.linalg.eigvalsh(M).min() < -1e-12:
        bad2 += 1
print(f"    variant (i) at timelike p (P_J = D0 = 0, F != 0): non-PSD in {bad2}/20000 draws")

# ---------------------------------------------------------------- [3]
print("\n[3] variant (ii): Barnes-Rivers bookkeeping, static source T00=M")
P2_massive, P0_massive = 2/3, 1/3
GR = P2_massive - 0.5*P0_massive
print(f"    massive test body: P2={P2_massive:.6f}, P0={P0_massive:.6f}, GR numerator={GR:.6f}; photon: P2 part=1, P0 part=0")
def gamma_of_c0(c0):
    return 2/(1+2*c0/3) - 1
# Cassini: gamma-1 = (2.1 +- 2.3)e-5 (comparator; web-checked in R8-3)
lo, hi = 2.1e-5 - 2*2.3e-5, 2.1e-5 + 2*2.3e-5
# gamma-1 = -(4c0/3)/(1+2c0/3)  =>  c0 = -(3/4)(gamma-1)/(1+(gamma-1)/2)
c0_hi = -(0.75)*lo/(1+lo/2); c0_lo = -(0.75)*hi/(1+hi/2)
print(f"    gamma(c0) = (1-2c0/3)/(1+2c0/3); Cassini 2-sigma gamma-1 in [{lo:.2e},{hi:.2e}] => c0 in [{c0_lo:.2e},{c0_hi:.2e}]")
print(f"    trace-only drift (no spin-2): photons not deflected => gamma = -1, |gamma-1| = 2 = {2/2.3e-5:.3e} Cassini sigmas")

# ---------------------------------------------------------------- [4]
print("\n[4] OWD Eq.27 class: integrate the classical field out of a Gaussian history (1 mode)")
# exponent: i h Delta - (a h - b)^2/(2 N)   -> expect  i Delta b/a - Delta^2 N/(2 a^2)
for (a, b, N, D) in [(1.3, 0.7, 0.4, 0.9), (2.0, -1.1, 2.5, 0.3), (0.5, 0.2, 0.1, 1.7)]:
    re = integrate.quad(lambda h: np.cos(h*D)*np.exp(-(a*h-b)**2/(2*N)), -50, 50, limit=400)[0]
    im = integrate.quad(lambda h: np.sin(h*D)*np.exp(-(a*h-b)**2/(2*N)), -50, 50, limit=400)[0]
    norm = np.sqrt(2*np.pi*N)/a
    val = (re+1j*im)/norm
    pred = np.exp(1j*D*b/a - D**2*N/(2*a**2))
    print(f"    a={a} b={b} N={N} D={D}: numeric={val:.8f} predicted={pred:.8f}")
print("    => matter noise = D0 + |G|^2 D2 (additive), response = G F: no cross term exists in that class.")

# ---------------------------------------------------------------- [5]
print("\n[5] variant (iii): correlated measurement-feedback (Wiseman-Milburn)")
def D(L, rho):
    return L@rho@L.conj().T - 0.5*(L.conj().T@L@rho + rho@L.conj().T@L)
def comm(A, B):
    return A@B - B@A
n = 4
errs = []
for t in range(200):
    c = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
    Fh = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); Fh = (Fh+Fh.conj().T)/2
    X = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); rho = X@X.conj().T; rho /= np.trace(rho)
    wm = D(c, rho) - 1j*comm(Fh, c@rho + rho@c.conj().T) + D(Fh, rho)
    alt = D(c-1j*Fh, rho) - 1j*comm((Fh@c + c.conj().T@Fh)/2, rho)
    errs.append(np.abs(wm-alt).max())
print(f"    WM generator == D[c - iF] - i[(Fc+c^dag F)/2, .]: max error over 200 random draws = {max(errs):.2e}")
print("    single system, c = sqrt(k)(1+i mu)A, F = lam A: total dephasing = k + (sqrt(k) mu - lam)^2, coupling g = 2 sqrt(k) lam")
for mu in [0.0, 1.0, 10.0, 100.0]:
    g = 1.0
    if mu == 0.0:
        k = g/2; lam = g/(2*np.sqrt(k))  # additive optimum: k = lam^2 -> dephasing 2k = g
    else:
        k = g/(2*mu); lam = np.sqrt(k)*mu
    deph = k + (np.sqrt(k)*mu - lam)**2
    print(f"    mu={mu:6.1f}: kappa={k:.4e} lam={lam:.4e} coupling g={2*np.sqrt(k)*lam:.4f} total dephasing={deph:.4e} (AM-GM floor for g=1: {g:.4f})")

# two qubits
Z = np.diag([1.0, -1.0]).astype(complex); I2 = np.eye(2, dtype=complex)
Z1, Z2 = np.kron(Z, I2), np.kron(I2, Z)
def liouv(H, Ls):
    d = H.shape[0]; Id = np.eye(d)
    Lv = -1j*(np.kron(Id, H) - np.kron(H.T, Id))
    for L in Ls:
        LdL = L.conj().T@L
        Lv += np.kron(L.conj(), L) - 0.5*np.kron(Id, LdL) - 0.5*np.kron(LdL.T, Id)
    return Lv
def negativity(rho):
    r = rho.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)  # partial transpose on qubit 2
    ev = np.linalg.eigvalsh((r+r.conj().T)/2)
    return float(-ev[ev < 0].sum())
plus = np.array([1, 1], dtype=complex)/np.sqrt(2)
psi = np.kron(plus, plus); rho0 = np.outer(psi, psi.conj())
print("    two qubits, target coherent coupling g Z1 Z2 with g = 1 (time t = pi/8 maximises coherent entanglement)")
t = np.pi/8
for mu in [0.0, 1.0, 10.0, 100.0]:
    g = 1.0
    # (a) one joint meter on A = Z1+Z2, feedback F = lam A onto both: H = lam sqrt(k) A^2
    if mu == 0.0:
        k = 0.5; lam = 0.5/np.sqrt(k)  # g = 2 sqrt(k) lam per Z1Z2 coefficient -> 2 lam sqrt(k) = g
    else:
        k = g/(2*mu); lam = np.sqrt(k)*mu
    A = Z1 + Z2
    c = np.sqrt(k)*(1+1j*mu)*A; Fh = lam*A
    H = (Fh@c + c.conj().T@Fh)/2
    Lv = liouv((H+H.conj().T)/2, [c-1j*Fh])
    rt = (linalg.expm(Lv*t)@rho0.reshape(-1, order='F')).reshape(4, 4, order='F')
    Na = negativity(rt)
    # (b) two LOCAL meters: record of qubit 1 fed back to qubit 2 and vice versa (LOCC)
    c1 = np.sqrt(k)*(1+1j*mu)*Z1; c2 = np.sqrt(k)*(1+1j*mu)*Z2
    F2 = lam*Z2; F1 = lam*Z1
    Hb = (F2@c1 + c1.conj().T@F2)/2 + (F1@c2 + c2.conj().T@F1)/2
    Lvb = liouv((Hb+Hb.conj().T)/2, [c1-1j*F2, c2-1j*F1])
    rtb = (linalg.expm(Lvb*t)@rho0.reshape(-1, order='F')).reshape(4, 4, order='F')
    Nb = negativity(rtb)
    Hcoef_a = np.real(np.trace(H@Z1@Z2))/4; Hcoef_b = np.real(np.trace(Hb@Z1@Z2))/4
    print(f"    mu={mu:6.1f}: joint meter: Z1Z2 coeff={Hcoef_a:.3f}, negativity={Na:.4f} | local meters (LOCC): Z1Z2 coeff={Hcoef_b:.3f}, negativity={Nb:.2e}")
print("    pure coherent g Z1Z2 at t=pi/8 gives negativity 0.5*sin(2*g*t)... reference:", end=" ")
Uc = linalg.expm(-1j*1.0*Z1@Z2*t); rc = Uc@rho0@Uc.conj().T
print(f"{negativity(rc):.4f}")

# ---------------------------------------------------------------- [6]
print("\n[6] variant (iii): emission side vs absorption side (unsymmetrised spectral matrices of B and J)")
viol = 0; minratio = np.inf
for t in range(20000):
    G = rng.normal() + 1j*rng.normal()
    # emission side S(-p): rank one with null vector [1, G]  (perfect anticorrelation, f = B + G J silent)
    v = np.array([np.conj(G), -1.0]); sig = rng.uniform(0.1, 5)
    Sm = sig*np.outer(v, v.conj())
    SJJ = Sm[1, 1].real            # classical output: S_JJ(p) = S_JJ(-p)
    # absorption side S(p): random PSD with that S_JJ
    X = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); Sp = X@X.conj().T
    Sp = Sp*(SJJ/Sp[1, 1].real)
    u = np.array([1.0, G])
    emit = (u.conj()@Sm@u).real; absb = (u.conj()@Sp@u).real
    # commutator spectral weight C(p) = S_Jf(p) - [S_fJ(-p)]* ; the gain F obeys |F| = |C| with no reverse gain
    SJf_p = (np.array([0, 1.0])@Sp@u); SfJ_m = (u.conj()@Sm@np.array([0, 1.0]))
    C = SJf_p - np.conj(SfJ_m)
    if absb < abs(C)**2/SJJ - 1e-9:
        viol += 1
    if abs(C) > 1e-6:
        minratio = min(minratio, absb*SJJ/abs(C)**2)
    assert emit < 1e-9
print(f"    emission-silent draws: 20000; absorption < |C|^2/S_JJ in {viol} draws; min absorption*S_JJ/|C|^2 = {minratio:.6f}")
print("    => zero vacuum excitation forces matter to be ABSORBED into the hidden meter at rate >= |F|^2/S_JJ,")
print("       and the felt field f = B + G J is not the classical record (perfect B-J anticorrelation).")
viol = 0
for t in range(20000):  # uncorrelated emission side (OWD-additive): S_BJ(-p) = 0
    G = rng.normal() + 1j*rng.normal(); sB = rng.uniform(0, 5); sJ = rng.uniform(0.01, 5)
    Sm = np.diag([sB, sJ]); u = np.array([1.0, G])
    if (u.conj()@Sm@u).real < abs(G)**2*sJ - 1e-12:
        viol += 1
print(f"    uncorrelated emission side: S_ff(-p) >= |G|^2 S_JJ violated in {viol}/20000 draws")

# ---------------------------------------------------------------- [7]
print("\n[7] variant (iv): preferred frame")
print("    R8-3 regulated ansatz D0 = c|F|^2/(|s|+mu^2) at saturation: K/floor = x/(x+1) + (x+1)/(4x), x = |s|/mu^2")
for x in [1e2, 1.0, 1e-2, 1e-4, 1e-6]:
    print(f"      x={x:8.0e}: K/floor = {x/(x+1) + (x+1)/(4*x):.6e}")
print("    (referee r83 [4] values 1.0, 25.26, 2500.25, 250000.25 reproduced; large-x limit 1.25, not 1)")
print("    exact pointwise least-decoherence: D0' = c/(2|s|), P_J = |s|/(2c)  => K = c|F|^2/|s| (ratio 1), no mu needed")
print("    vacuum energy injection with K = floor: integrand ~ w * s * |F_u|^2, |F_u|^2 = e^{-k^2 l^2}(1+w^2 tau^2)^{-n}  (l = tau = 1)")
for nn in [2, 3, 4]:
    def inner(om):
        # int_{k<om} d^3k om (om^2-k^2) e^{-k^2}
        val = integrate.quad(lambda k: 4*np.pi*k*k*om*(om*om-k*k)*np.exp(-k*k), 0, om)[0]
        return val*(1+om*om)**(-nn)
    parts = []
    for Wmax in [1e1, 1e2, 1e3, 1e4]:
        edges = np.concatenate([[0], np.logspace(-2, np.log10(Wmax), 60)])
        tot = sum(integrate.quad(inner, edges[i], edges[i+1], limit=200)[0] for i in range(len(edges)-1))
        parts.append(tot)
    print(f"      n={nn}: integral up to w=1e1,1e2,1e3,1e4: " + ", ".join(f"{p:.5f}" for p in parts))
print("      => n=2 grows by a constant per decade (log-divergent energy injection); n>=3 converges. R8-3's 'n >= 2' must read n >= 3.")
# near-cone classical GW content: rho ~ hbar c L/(pi^3 l^4) for P_J = eps*|s|/(2c) near the cone, cut at k ~ 1/l
hbar_c = 3.16153e-26  # J m
rho_L = 5.9e-10       # J/m^3 (dark energy density; recalled)
rho_c = 8.5e-10       # J/m^3 critical density (recalled)
print("    near-cone classical GW energy (suggested, O(1) normalisation): rho_GW ~ eps * L * hbar c/(pi^3 l^4), L = log factor")
for l in [1e-8, 1e-7, 1e-6, 5e-6]:
    for L in [10.0]:
        r = L*hbar_c/(np.pi**3*l**4)
        print(f"      l={l:.0e} m: rho_GW(eps=1) = {r:.2e} J/m^3 = {r/rho_c:.2e} rho_crit; eps needed for rho_GW < rho_Lambda: {rho_L/r:.2e}")
# vacuum photon injection scales as 1/eps when the near-cone noise is suppressed broadband (D0 ~ 1/(eps|s|))
print("    combine with R8-3's EBL estimate l_min(eps=1) = 8.86e-9 m (A'=1e-2), l_min ~ eps^(-1/7):")
for (lab, lmin1) in [("A'=1e-4", 4.59e-9), ("A'=1e-2", 8.86e-9), ("A'=1", 1.71e-8)]:
    # need l >= lmin1 * eps(l)^(-1/7), eps(l) = rho_L pi^3 l^4/(L hbar c), L = 10
    f = lambda l: l - lmin1*(min(1.0, rho_L*np.pi**3*l**4/(10*hbar_c)))**(-1/7)
    from scipy.optimize import brentq
    lsol = brentq(f, 1e-10, 1e-3)
    print(f"      {lab}: lower end with near-cone suppression ~ {lsol:.2e} m (upper end 5e-6 m from R6-4)")
