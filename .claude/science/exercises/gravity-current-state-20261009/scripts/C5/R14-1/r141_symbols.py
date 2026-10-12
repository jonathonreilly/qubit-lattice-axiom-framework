"""R14-1 (A)-(D): group velocity over the whole zone, doublers/corners, Theorem E anomaly A = Hess(eps^2/2) - I,
kernel decay, and rapidity budgets, for the superluminal laws used so far and the subluminal ones.
All laws separable: eps^2 = m^2 + sum_i G(k_i); per axis G, G' (= d/dk G), G'' supplied.
  R7-1 literal (b=2, b2=3.1, m=0.3) and R8-1/R9-x law (b=2.6, b2=3.0, m=0.5): G = s^2, s = rho k + (1-rho) sin k.
  R8-2 gapped (b=2, b2=3.1): G' = rho 2k + (1-rho) C sin k, C = 2b/sin b.
  S(b): R13-4 odd subluminal symbol, G = s^2.   G(b): gapped even form G = h^2, h' = 1 - sstep((k-b)/(pi-b)).
"""
import numpy as np, sys
from scipy.interpolate import CubicSpline
from sublum import sstep, dsstep, wrap, SymS, SymG
out = []
def pr(*a):
    l = ' '.join(str(x) for x in a); print(l, flush=True); out.append(l)

def num(f, k, h=1e-5): return (f(k+h) - f(k-h))/(2*h)
def lit(b, b2):
    def s(k):
        k = wrap(k); r = sstep((b2 - np.abs(k))/(b2 - b)); return r*k + (1-r)*np.sin(k)
    G = lambda k: s(k)**2
    dG = lambda k: num(G, k); d2G = lambda k: num(dG, k, 1e-4)
    return G, dG, d2G
def gap82(b, b2):
    C = 2*b/np.sin(b); kg = np.linspace(0, np.pi, 400001)
    r = sstep((b2 - kg)/(b2 - b)); up = r*2*kg + (1-r)*C*np.sin(kg)
    ug = np.concatenate([[0.0], np.cumsum(0.5*(up[1:]+up[:-1])*np.diff(kg))]); cs = CubicSpline(kg, ug)
    G = lambda k: np.where(np.abs(wrap(k)) <= b, wrap(k)**2, cs(np.minimum(np.abs(wrap(k)), np.pi)))
    def dG(k):
        kw = wrap(k); ka = np.abs(kw); r = sstep((b2 - ka)/(b2 - b)); return np.sign(kw)*(r*2*ka + (1-r)*C*np.sin(ka))
    d2G = lambda k: num(dG, k)
    return G, dG, d2G
def symS(b):
    A = SymS(b); return (lambda k: A.s(k)**2), (lambda k: 2*A.s(k)*A.ds(k)), (lambda k: 2*(A.ds(k)**2 + A.s(k)*A.d2s(k)))
def symG(b):
    A = SymG(b); return A.g, A.dg, A.d2g

laws = [('R7-1 literal b=2.0,b2=3.1', lit(2.0, 3.1), 2.0, 0.3),
        ('R8-1/R9 law b=2.6,b2=3.0', lit(2.6, 3.0), 2.6, 0.5),
        ('R8-2 gapped b=2.0,b2=3.1', gap82(2.0, 3.1), 2.0, 0.3),
        ('S(1.4) R13-4 odd sublum', symS(1.4), 1.4, 0.3),
        ('S(1.4) R13-4 odd sublum', symS(1.4), 1.4, 0.5),
        ('G(1.4) gapped sublum', symG(1.4), 1.4, 0.3),
        ('G(1.4) gapped sublum', symG(1.4), 1.4, 0.5),
        ('G(2.0) gapped sublum', symG(2.0), 2.0, 0.3),
        ('G(2.6) gapped sublum', symG(2.6), 2.6, 0.5)]
N1 = 400000; k1 = np.linspace(-np.pi, np.pi, N1, endpoint=False) + np.pi/N1
N3 = 160; k3 = np.linspace(-np.pi, np.pi, N3, endpoint=False) + np.pi/N3
pr('(A) whole-zone group velocity, corners (doublers), box exactness')
for name, (G, dG, d2G), b, m in laws:
    v1 = np.max(np.abs(dG(k1))/(2*np.sqrt(m*m + G(k1))))
    g, dg = G(k3), dG(k3); best = 0
    for a in range(N3):
        E = np.sqrt(m*m + g[a] + g[:, None] + g[None, :])
        vv = np.sqrt(dg[a]**2 + dg[:, None]**2 + dg[None, :]**2)/(2*E); best = max(best, vv.max())
    # refine d=3 near the best: also check diagonal line k(1,1,1) and (k,k,0)
    vd = max(np.max(np.sqrt(3*dG(k1)**2)/(2*np.sqrt(m*m + 3*G(k1)))), np.max(np.sqrt(2*dG(k1)**2)/(2*np.sqrt(m*m + 2*G(k1)))))
    inb = np.abs(k1) <= b
    ex = np.max(np.abs(G(k1[inb]) - k1[inb]**2))
    corners = [np.sqrt(m*m + j*G(np.array([np.pi]))[0]) for j in (1, 2, 3)]
    emin_edge = np.min(np.sqrt(m*m + G(k1[~inb])))
    pr('  %-28s m=%.1f: v_max d=1 %.4f, d=3 grid %.4f (axis-diag lines %.4f); max|G-k^2| on box %.1e; corner eps (pi,0,0),(pi,pi,0),(pi,pi,pi) = %.4f %.4f %.4f; min eps outside box (1D) %.4f vs face sqrt(m^2+b^2) %.4f'
       % (name, m, v1, best, vd, ex, *corners, emin_edge, np.sqrt(m*m + b*b)))
A = SymS(1.4); q = np.linspace(-1.4, 1.4, 2001)
pr('  S(1.4) mirror identity: max|s(pi+q) + q| over |q|<=1.4 = %.1e (exact relativistic doubler band at each corner; s(pi-k)=s(k))' % np.max(np.abs(A.s(np.pi + q) + q)))
pr('  S(1.4): s\'(pi+q) = %.3f on the mirror box -> [K,P] = i s\' H = -iH there (parity-image representation)' % A.ds(np.array([np.pi+0.3]))[0])

pr('\n(B) Theorem E anomaly A_xx = G\'\'/2 - 1 (Hess(eps^2/2) - I, per axis); zone mean must be -1')
for name, (G, dG, d2G), b, m in laws:
    Ak = d2G(k1)/2 - 1; inb = np.abs(k1) <= b
    sl = (~inb)
    # d=3 edge statistics as R8-2 (tr A / 3), on the N3 grid: edge = outside the cube box
    g, a3 = G(k3), d2G(k3)/2 - 1
    E = np.sqrt(m*m + g[:, None, None] + g[None, :, None] + g[None, None, :])
    trA = (a3[:, None, None] + a3[None, :, None] + a3[None, None, :])/3
    box = (np.abs(k3)[:, None, None] <= b) & (np.abs(k3)[None, :, None] <= b) & (np.abs(k3)[None, None, :] <= b)
    edge = ~box
    em = trA[edge].mean(); ew = (trA*E)[edge].sum()/E[edge].sum(); w = np.exp(-(E - m)/0.1); lt = (trA*w)[edge].sum()/w[edge].sum()
    pr('  %-28s m=%.1f: zone mean %.6f; max|A| on box %.1e; A range off box [%.2f, %.2f]; 1D share of zone with A!=0: %.3f; d=3 edge: mean tr/3 %.3f, energy-wtd %.3f, low-T(0.1) %.3f; box volume fraction (b/pi)^3 = %.3f'
       % (name, m, Ak.mean(), np.max(np.abs(Ak[inb & (np.abs(k1) < b - 1e-3)])), Ak[sl].min(), Ak[sl].max(), np.mean(np.abs(Ak) > 1e-9), em, ew, lt, (b/np.pi)**3))
A = SymS(1.4)
pr('  S(1.4): A_xx = s\'^2 - 1 + s s\'\' with |s\'| <= 1 and s s\'\' <= 0 on (0, pi) -> A <= 0 pointwise (checked max A = %.2e)'
   % np.max(A.ds(k1)**2 - 1 + A.s(k1)*A.d2s(k1)))

pr('\n(C) real-space kernel decay of the symbol (1D FFT, N = 8192): |kernel(r)|')
Nf = 8192; kf = 2*np.pi*np.fft.fftfreq(Nf)
for name, (G, dG, d2G), b, m in laws[:5] + laws[5:7]:
    e_r = np.abs(np.fft.ifft(np.sqrt(m*m + G(kf))))
    pr('  eps %-28s m=%.1f: ' % (name, m) + ' '.join('r=%d:%.1e' % (r, e_r[r]) for r in [1, 8, 32, 64, 128, 256, 512, 1024]) + ' | odd r: ' + ' '.join('r=%d:%.1e' % (r, e_r[r]) for r in [9, 33, 129]))
A = SymS(1.4); s_r = np.abs(np.fft.ifft(A.s(kf)))
pr('  S(1.4): eps(k+pi) = eps(k) (pi-periodic) -> H hops only even distances: the free law is 2^d decoupled sublattice copies (exact doubling); s(k+pi) = -s(k) -> |s kernel| odd r: ' + ' '.join('r=%d:%.1e' % (r, s_r[r]) for r in [1, 9, 33, 65, 129, 257, 513]) + '; even r=8: %.1e' % s_r[8])
R = lit(2.0, 3.1); sr71 = np.abs(np.fft.ifft(np.sign(wrap(kf))*np.sqrt(R[0](kf))))

pr('\n(D) rapidity budgets at rest, asinh(b E_P/m) (a = l_P), and toy two-body plateau budgets')
EP = 1.220890e22   # MeV
for nm, mm in [('electron', 0.51099895), ('proton', 938.27209), ('top', 172.69e3)]:
    pr('  %-8s: b=2.6 %.2f | b=2.0 %.2f | b=1.4 %.2f | b=1.2 %.2f   (shift b 2->1.4: %.3f = ln(2/1.4))'
       % (nm, *[np.arcsinh(bb*EP/mm) for bb in (2.6, 2.0, 1.4, 1.2)], np.arcsinh(2.0*EP/mm) - np.arcsinh(1.4*EP/mm)))
with open(__file__.replace('.py', '.out'), 'w') as f: f.write('\n'.join(out) + '\n')
