"""C5 R9-1: edge-sector population for R7-1/R8-2's box law (d = 3), profiles L (literal, doublers) and G (gapped).
Parts
 (A) band geometry: edge fraction, flat edge mean of A = Hess(eps^2/2) - I vs the identity -1/f_edge,
     max group speed on the edge, thermal (number-conserving Boltzmann) edge fraction, energy-weighted A and w = <v^2>/3.
 (B) Lemma Q illustration: [T00(q), Q] matrix elements across the face for a box-only charge.
 (C) gravitational doubler conversion X X -> X_Q X_Q via lattice-momentum-Q graviton exchange (lapse coupling):
     corner sum, thermal average, freeze-in fraction f_D(T_max), Omega_D h^2 with the SM mass spectrum.
 (D) profile G: equilibrium edge yield Y_edge(T) and the Omega bound.
 (E) momentum balance: semiclassical two-body fall (edge quantum + box source): crystal momentum conserved,
     energy centroid self-accelerates by -F*A.
Units: lattice units a = 1 for (A),(B),(D),(E); physical conversion with a = l_P (reading).
"""
import numpy as np, time
T0 = time.time()
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
def wrap(k):
    return -(((-k) + np.pi) % (2*np.pi) - np.pi)
def plateau(k, a, b):
    return sstep((b - np.abs(wrap(k)))/(b - a))

B, B2 = 2.0, 3.1
def s_r71(k):
    k = wrap(k); r = plateau(k, B, B2)
    return r*k + (1-r)*np.sin(k)
def g_L(k): return s_r71(k)**2
Cg = 2*B/np.sin(B)
NG = 400001
kg = np.linspace(0, np.pi, NG)
up = plateau(kg, B, B2)*2*kg + (1-plateau(kg, B, B2))*Cg*np.sin(kg)
ug = np.concatenate([[0.0], np.cumsum(0.5*(up[1:]+up[:-1])*np.diff(kg))])
def g_G(k):
    k = np.abs(wrap(k)); return np.where(k <= B, k*k, np.interp(np.minimum(k, np.pi), kg, ug))
def gp_G(k):
    kw = wrap(k); ka = np.abs(kw); r = plateau(ka, B, B2)
    return np.sign(kw)*(r*2*ka + (1-r)*Cg*np.sin(ka))
def gp_L(k, h=1e-6): return (g_L(k+h)-g_L(k-h))/(2*h)
def gpp(gp, k, h=1e-5): return (gp(k+h)-gp(k-h))/(2*h)
PROF = {'L': (g_L, gp_L), 'G': (g_G, gp_G)}

# ===================== (A) band geometry in d = 3 =====================
pr('=== (A) d = 3 band geometry (b = %.1f, b2 = %.1f) ===' % (B, B2))
N = 144
k1 = (np.arange(N) + 0.5)*2*np.pi/N - np.pi        # midpoint grid
for M in (0.3, 0.05):
    for name, (g, gp) in PROF.items():
        g1, gp1, A1 = g(k1), gp(k1), gpp(gp, k1)/2 - 1.0     # separable: eps^2 = m^2 + sum g(k_i); A_ii = g''(k_i)/2 - 1
        G3 = np.meshgrid(k1, k1, k1, indexing='ij', sparse=True)
        idx = [np.searchsorted(k1, x.ravel()) for x in G3]
        Gs = [g1.reshape([-1 if i == j else 1 for j in range(3)]) for i in range(3)]
        GPs = [gp1.reshape([-1 if i == j else 1 for j in range(3)]) for i in range(3)]
        As = [A1.reshape([-1 if i == j else 1 for j in range(3)]) for i in range(3)]
        Ks = [k1.reshape([-1 if i == j else 1 for j in range(3)]) for i in range(3)]
        E = np.sqrt(M*M + Gs[0] + Gs[1] + Gs[2])
        edge = (np.abs(Ks[0]) > B) | (np.abs(Ks[1]) > B) | (np.abs(Ks[2]) > B)
        trA = (As[0] + As[1] + As[2])/3 + 0*E
        v2 = sum((gpx/(2*E))**2 for gpx in GPs)
        fe = edge.mean()
        pr('[%s, m=%.2f] edge fraction %.5f (exact 1-(b/pi)^3 = %.5f); zone mean trA/3 = %.5f; flat edge mean trA/3 = %.5f vs -1/f_edge = %.5f'
           % (name, M, fe, 1-(B/np.pi)**3, trA.mean(), trA[edge].mean(), -1/fe))
        pr('      min eps edge = %.4f (face %.4f); max |v| on edge = %.3f; max |v| on box = %.4f'
           % (E[edge].min(), np.sqrt(M*M+B*B), np.sqrt(v2[edge].max()), np.sqrt(v2[~edge].max())))
        for T in (0.02, 0.05, 0.1, 0.2, 0.5):
            lw = -E/T; lw = lw - lw.max(); w = np.exp(lw)
            fed = w[edge].sum()/w.sum()
            if w[edge].sum() > 0:
                Aw = (w*E*trA)[edge].sum()/(w*E)[edge].sum(); ww = (w*v2)[edge].sum()/w[edge].sum()/3
            else:
                Aw = ww = np.nan
            pr('      T=%.2f: thermal edge fraction %.3e ; edge energy-weighted <trA/3> = %+.4f ; edge w = <v^2>/3 = %.3f'
               % (T, fed, Aw, ww))
pr('  L-profile doubler valleys (analytic): near k_i = pi, s = sin k on |k|>=b2, so eps^2 = m^2 + sum sin^2(delta_i) + (box axes) k^2;')
pr('  A_ii = cos(2 delta_i) - 1 = -2 sin^2 delta_i; for T << 1/a each of the 7 valleys has the box partition function up to O((Ta)^2): f_edge -> 7/8.')

# ===================== (B) Lemma Q illustration =====================
pr('\n=== (B) Lemma Q: [T00(q), Q] = sum_k F00(k+q,k) (c(k) - c(k+q)) a+_{k+q} a_k for a box-only charge c = 1_B ===')
M = 0.3
for name, (g, gp) in PROF.items():
    eps = lambda kx, ky=0.3, kz=0.2: np.sqrt(M*M + g(np.array(kx)) + g(np.array(ky)) + g(np.array(kz)))
    for d in (0.05, 0.01, 0.001):
        k, kp = B - d, B + d
        F = 0.5*(eps(k) + eps(kp))
        pr('  [%s] k=(%.3f,.3,.2) -> k\'=(%.3f,.3,.2): |F00| = %.5f -> commutator element %.5f (charge 1 -> 0)' % (name, k, kp, F, F))

# ===================== (C) doubler conversion by gravity =====================
pr('\n=== (C) gravitational doubler conversion X X -> X_Q X_Q (profile L), lapse coupling, D = R8-2 symbol ===')
CD1, CD2, PS1, PS2 = 1.0, 2.5, 1.0, 2.0
def Dsym(q):
    q = wrap(q); r = plateau(q, CD1, CD2)
    return r*q + (1-r)*np.sin(q) + 1j*(1 - plateau(q, PS1, PS2))*(1 - np.cos(q))
corners = [(np.pi,0,0),(0,np.pi,0),(0,0,np.pi),(np.pi,np.pi,0),(np.pi,0,np.pi),(0,np.pi,np.pi),(np.pi,np.pi,np.pi)]
SQ = 0.0
for c in corners:
    D2 = sum(abs(Dsym(np.array(x)))**2 for x in c); SQ += 1/D2**2
pr('  |D(pi)|^2 = %.4f ; corner sum S_Q = sum_Q |D(Q)|^-4 = %.5f (expected 3/16+3/64+1/144 = %.5f)' % (abs(Dsym(np.array(np.pi)))**2, SQ, 3/16+3/64+1/144))
# CM-frame golden rule, massless legs: V_Q = 4 pi G (sqrt(s)/2)^2 a^2/|D_Q|^2 ; rho_f = s/(16 pi^2) ; sigma*v_rel(=2) = 2 pi sum|V|^2 rho_f
# => sigma = (pi/16) G^2 a^4 s^3 S_Q ; plasma rate uses <sigma v_Mol>, v_Mol = 1 - cos(theta) for massless legs
csig = np.pi/16*SQ
rng = np.random.default_rng(1)
def therm_E(n, stat):
    # sample energies from E^2 f(E) (T = 1): Boltzmann -> Gamma(3); FD/BE by rejection from Gamma(3)
    E = rng.gamma(3.0, 1.0, size=n)
    if stat == 'B': return E
    w = (np.exp(-E)/(np.exp(-E)+1.0)) if stat == 'F' else None
    acc = rng.random(n) < (1/(np.exp(E)+1))/np.exp(-E)/1.0*0.5 if stat == 'F' else None
    return E[acc]
nmc = 2_000_000
for stat in ('B', 'F'):
    E1 = therm_E(nmc, stat); E2 = therm_E(nmc, stat); nn = min(len(E1), len(E2)); E1, E2 = E1[:nn], E2[:nn]
    c = rng.uniform(-1, 1, nn)
    s = 2*E1*E2*(1-c)
    avg = np.mean(s**3*(1-c))
    pr('  thermal <s^3 (1-cos)>/T^6 [%s] = %.4g (Boltzmann analytic 8*60^2*16/5 = %.4g)' % (stat, avg, 8*3600*3.2))
avgB = 8*3600*3.2
MP = 1.22089e19         # GeV, G = 1/MP^2 ; a = l_P = 1/MP (reading)
gstar = 106.75
nfac = 11.6             # n_tot / T^3 for SM dof (fermions 3/4, zeta(3)/pi^2)
for kap, lab in ((1.0, 'lapse-only (setting)'), (8.0, 'full spin-2, head-on bound kappa=8')):
    # rate per particle Gamma = n_tot <sigma v> = nfac*csig*kap^2*avgB*T^9/MP^8 ; H = 1.66 sqrt(g*) T^2/MP
    cG = nfac*csig*kap**2*avgB
    cH = 1.66*np.sqrt(gstar)
    cr = cG/cH
    Teq = (1/cr)**(1/7)
    pr('  [%s] Gamma/H = %.4g (T/MP)^7 ; Gamma = H at T = %.3f MP = %.3g GeV ; f_D(T_max) = Gamma/H/7 (freeze-in, f_D << 1)'
       % (lab, cr, Teq, Teq*MP))
    # SM spectrum: sum_s c_s g_s m_s (GeV)
    ferm = {'t': (12, 172.6), 'b': (12, 4.18), 'c': (12, 1.27), 's': (12, 0.093), 'd': (12, 0.0047), 'u': (12, 0.0022),
            'tau': (4, 1.777), 'mu': (4, 0.1057), 'e': (4, 0.000511)}
    bos = {'W': (6, 80.37), 'Z': (3, 91.19), 'H': (1, 125.1)}
    SF = sum(0.75*g*m for g, m in ferm.values()); SB = sum(g*m for g, m in bos.values())
    for Sm, lab2 in ((SF, 'fermions'), (SF+SB, 'fermions+W,Z,H')):
        coef = 2.742e8*0.2777/gstar*Sm       # Omega h^2 = coef * f_D
        fneed = 0.120/coef
        Tdm = (7*fneed/cr)**(1/7)
        pr('     %-16s sum c g m = %7.1f GeV ; Omega_D h^2 = %.3g f_D ; Omega_D = Omega_c at f_D = %.3g, T_max = %.4f MP = %.3g GeV'
           % (lab2, Sm, coef, fneed, Tdm, Tdm*MP))
    for Tm in (5.8e15, 1e16, 1e17):
        fD = cr*(Tm/MP)**7/7
        pr('     T_max = %.2g GeV: f_D = %.3g ; Omega_D h^2 (fermions+bosons) = %.3g' % (Tm, fD, 2.742e8*0.2777/gstar*(SF+SB)*fD))
pr('  equilibrium (T_max >~ Teq): f_D -> 7 (7 valleys), Omega_D h^2 ~ %.3g (overclosure); massless-doubler variant Delta N_eff = 2.85 f_D -> ~20' % (2.742e8*0.2777/gstar*(SF+SB)*7))
# non-relativistic lab conversion inside a nucleus: Gamma ~ n_nuc * sigma v ; sigma v = 2 pi sum|V_Q|^2 rho_f, V_Q = 4 pi G m^2 a^2/|D_Q|^2, rho_f = mu p/(2 pi^2)
hbarc = 1.97327e-16     # GeV m
mN = 0.939; nnuc = 0.16e45*hbarc**3   # fm^-3 -> GeV^3
pF = 0.25; mu = mN/2
sv = 2*np.pi*(4*np.pi*mN**2/MP**4)**2*SQ*mu*pF/(2*np.pi**2)*(pF/mu)/(pF/mu)   # rate density per pair density (v cancels in golden rule)
Gam = nnuc*sv           # GeV
pr('  lab: nucleon-nucleon gravitational conversion inside a nucleus: Gamma ~ %.3g GeV = %.3g s^-1 per nucleon (age of universe 4.4e17 s)'
   % (Gam, Gam/6.582e-25))
# EM analogue (G-out without a Dirac sea): e e -> e_Q e_Q via photon exchange of lattice momentum Q, contact strength 4 pi alpha a^2/|D_Q|^2
al = 1/137.036
crEM = nfac*np.pi/16*SQ*avgB/4**2/cH    # replace G*(sqrt(s)/2)^2 by alpha: V_Q = 4 pi alpha a^2/|D_Q|^2 -> sigma = (pi/16)*alpha^2 a^4 s S_Q*16/s^2... (see report)
pr('  EM contact conversion (number-conserving, G-out): sigma = pi*alpha^2*a^4*s*S_Q (CM, massless) ; Gamma/H ~ %.3g (T/MP)^3 [all-species n_tot; charged pairs only in fact]' %
   (nfac*np.pi*al**2*SQ*np.mean(2*rng.gamma(3,1,200000)*rng.gamma(3,1,200000)*(1-rng.uniform(-1,1,200000))**2)/cH))

# ===================== (D) profile G: equilibrium edge yield =====================
pr('\n=== (D) profile G: equilibrium edge number density n_edge/T^3 (lattice units), relic upper bound ===')
M = 0.0
g, gp = PROF['G']
Nf = 220
k1 = (np.arange(Nf) + 0.5)*2*np.pi/Nf - np.pi
g1 = g(k1)
Gs = [g1.reshape([-1 if i == j else 1 for j in range(3)]) for i in range(3)]
Ks = [k1.reshape([-1 if i == j else 1 for j in range(3)]) for i in range(3)]
E = np.sqrt(M*M + Gs[0] + Gs[1] + Gs[2])
edge = (np.abs(Ks[0]) > B) | (np.abs(Ks[1]) > B) | (np.abs(Ks[2]) > B)
Ee = E[edge]
dk3 = (2*np.pi/Nf)**3/(2*np.pi)**3
Emin = Ee.min()
pr('  E_e (grid min on edge) = %.4f (face sqrt(m^2+b^2) = %.4f)' % (Emin, B))
gdof = 106.75
for T in (0.4, 0.2, 0.1, 0.05, 0.03, 0.02, 0.01):
    ln_sum = np.log(np.sum(np.exp(-(Ee-Emin)/T))*dk3) - Emin/T     # log(n_edge per dof)
    lnY = np.log(gdof) + ln_sum - 3*np.log(T) - np.log(2*np.pi**2/45*gdof)
    lnOm = np.log(2.742e8*Emin*MP) + lnY
    pr('  T = %.2f /a (%.3g GeV): log10 Y_edge(eq) = %.2f ; log10 Omega_edge h^2 (stable, no annihilation) = %.2f'
       % (T, T*MP, lnY/np.log(10), lnOm/np.log(10)))

# ===================== (E) momentum balance, two-body semiclassical =====================
pr('\n=== (E) momentum balance: edge quantum (1) + box source (2), H = e1 + e2 - G e1 e2 U(x1-x2), d = 1 ===')
def e1d(prof, M):
    g, gp = PROF[prof]
    e = lambda k: np.sqrt(M*M + g(np.array(k)))
    de = lambda k: gp(np.array(k))/(2*e(k))
    return e, de
def run(prof1, k10, M1, prof2, k20, M2, Gc=1e-4, r0=3.0, x12=60.0, tf=40.0, dt=0.01):
    e1, d1 = e1d(prof1, M1); e2, d2 = e1d(prof2, M2)
    U = lambda r: 1/np.sqrt(r*r + r0*r0); dU = lambda r: -r/(r*r + r0*r0)**1.5
    y = np.array([0.0, k10, x12, k20])
    def f(y):
        x1, k1_, x2, k2_ = y; r = x1 - x2
        E1, E2 = e1(k1_), e2(k2_)
        return np.array([d1(k1_)*(1 - Gc*E2*U(r)), Gc*E1*E2*dU(r), d2(k2_)*(1 - Gc*E1*U(r)), -Gc*E1*E2*dU(r)])
    ts, Y = [0.0], [y.copy()]
    t = 0.0
    while t < tf - 1e-12:
        a1 = f(y); a2 = f(y + dt/2*a1); a3 = f(y + dt/2*a2); a4 = f(y + dt*a3)
        y = y + dt/6*(a1 + 2*a2 + 2*a3 + a4); t += dt; ts.append(t); Y.append(y.copy())
    Y = np.array(Y); ts = np.array(ts)
    E1 = e1(Y[:, 1]); E2 = e2(Y[:, 3])
    P = Y[:, 1] + Y[:, 3]
    XE = E1*Y[:, 0] + E2*Y[:, 2]                    # energy-weighted centroid (free energies; O(G) interaction energy ignored)
    acc = np.polyfit(ts, XE, 2)[0]*2
    F = Gc*e1(k10)*e2(k20)*abs(dU(-x12))
    A1 = gpp(PROF[prof1][1], np.array(k10))/2 - 1
    a1x = np.polyfit(ts, Y[:, 0], 2)[0]*2; a2x = np.polyfit(ts, Y[:, 2], 2)[0]*2
    return P.max() - P.min(), acc, F, A1, a1x, a2x
for lab, args in (('box particle k=0 + box source (control)', ('G', 0.0, 0.3, 'G', 0.0, 5.0)),
                  ('gapped edge top k=pi + box source', ('G', np.pi, 0.3, 'G', 0.0, 5.0)),
                  ('literal doubler k=pi + box source', ('L', np.pi, 0.3, 'G', 0.0, 5.0)),
                  ('literal s-max k*=2.234 + box source', ('L', 2.2337, 0.3, 'G', 0.0, 5.0))):
    dP, acc, F, A1, a1x, a2x = run(*args)
    pr('  %-40s : drift of k1+k2 = %.2e ; d2/dt2 (e1 x1 + e2 x2) = %+.4e ; prediction F*A1 (F toward source) = %+.4e ; A1 = %+.4f'
       % (lab, dP, acc, F*A1, A1))
pr('\nruntime %.1f s' % (time.time() - T0))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
