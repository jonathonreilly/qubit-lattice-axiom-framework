"""R19-34 library: one-loop U(1) ADDITIVE mass of a separable box/Wilson-type Dirac law on Z^3 x R under uniform strain.

Law (per axis j, H-cov strain: cell lengths l = (l_x, l_y, l_z), symbols scale 1/l_j at fixed lattice momentum):
  S^-1(P) = i g0 p0 + sum_j [ i g_j s(p_j) + W(p_j) ]/l_j + m          (Wilson-type: W multiplies the unit matrix, like m)
  photon:  Omega^2 = sum_j d(q_j)^2/l_j^2 + lam^2 ;   Feynman gauge (all four components, propagator 1/(Q0^2+Omega^2))
  Peierls/Ward vertex (R8-5/R13-7 convention, as in the referee-confirmed runner r137/r1610_core.dirac_pt):
      V_j(p,p') = l_j [S^-1_j(p) - S^-1_j(p')]/d(p_j - p'_j) ,  seagull T_j(p;q) = (l_j^2/2)[S^-1_j(p+q)+S^-1_j(p-q)-2 S^-1_j(p)]/d(q_j)^2
      V_0 = -i g0.
  At P = 0 with s(0) = W(0) = 0, k = q (internal fermion), a_j = s(q_j)/d(q_j), b_j = W(q_j)/d(q_j):
      V_j(0,q) = V_j(q,0) = i g_j a_j + b_j  (for naive s = sin, d = 2 sin(q/2): a = cos(q/2), b = r sin(q/2) -- R19-31's vertex)
  Mass part dm = (1/4) tr Sigma(P=0), Sigma = sum_j T_j D - sum_mu V_mu S V_mu D, frequency integral done analytically:
      dm/e^2 = (1/V) < sum_j l_j W(q_j)/d(q_j)^2 /(2 Om) >
             + (1/V) < [ M + sum_j ( (a_j^2 - b_j^2) M - 2 a_j b_j s(q_j)/l_j ) ] / (2 E Om (E + Om)) >
      M = m + sum_j W(q_j)/l_j,  E^2 = sum_j s(q_j)^2/l_j^2 + M^2,  V = l_x l_y l_z (=1 for traceless strain),
  < . > = BZ average d^3q/(2pi)^3.  Reduces EXACTLY to R19-31's r1931_wilson_mass.dm for s = sin, W = r(1-cos), d = 2 sin(q/2).
Only d^2 enters, so the sign convention of an odd photon symbol at q = +-pi is irrelevant.
Quadrature: integrand even in each q_j -> [0, pi]^3 x 8; composite Gauss-Legendre with breakpoints at the box edges.
"""
import numpy as np, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'arch'))


def panels(breaks, n, hmax=0.25, ir=True):
    """1D composite GL nodes on [0, pi] with given interior breakpoints (box edges) plus IR grading near 0."""
    br = {0.0, np.pi}
    if ir:
        for x in (0.0025, 0.005, 0.01, 0.02, 0.04, 0.08, 0.16, 0.32):
            br.add(x)
    for x in breaks:
        if 0 < x < np.pi:
            br.add(float(x))
    br = sorted(br)
    fine = [br[0]]
    for a, b in zip(br[:-1], br[1:]):
        k = max(1, int(np.ceil((b - a)/hmax)))
        for i in range(1, k + 1):
            fine.append(a + (b - a)*i/k)
    fine = np.array(fine)
    xg, wg = np.polynomial.legendre.leggauss(n)
    nodes, wts = [], []
    for a, b in zip(fine[:-1], fine[1:]):
        nodes.append(0.5*(b - a)*xg + 0.5*(b + a)); wts.append(0.5*(b - a)*wg)
    nodes = np.concatenate(nodes); wts = np.concatenate(wts)/np.pi    # average over [0, pi] (= BZ average for even integrands)
    return nodes, wts


class Grid:
    def __init__(self, breaks, n, hmax=0.25):
        self.x, self.w = panels(breaks, n, hmax)


def dm_mass(law_s, law_W, law_d, grid, l=(1.0, 1.0, 1.0), m=0.0, lam=0.0, parts=False, chunk=None, wexp=1.0):
    """one-loop additive mass dm/e^2 at P = 0 for the H-cov strained law. law_* are 1D callables on [0, pi].
    wexp: Wilson-term strain placement W_j = W/l_j^wexp (wexp = 1: H-cov, R19-31's choice; 0: unscaled per-site Wilson mass).
    General: M = m + sum W_j, b_j = l_j W_j/d, seagull l_j^2 W_j/d^2 (reduces to the docstring formula at wexp = 1)."""
    x, w = grid.x, grid.w
    s1, W1, d1 = law_s(x), law_W(x), law_d(x)
    d2 = d1*d1
    a1, b1 = s1/d1, W1/d1
    V = l[0]*l[1]*l[2]
    tad = 0.0; loop = 0.0
    # loop over the first axis in slices to bound memory
    for i0 in range(len(x)):
        sx = [s1[i0], s1[:, None], s1[None, :]]
        Wx = [W1[i0], W1[:, None], W1[None, :]]
        dd = [d2[i0], d2[:, None], d2[None, :]]
        aa = [a1[i0], a1[:, None], a1[None, :]]
        bb = [b1[i0], b1[:, None], b1[None, :]]
        Om = np.sqrt(sum(dd[j]/l[j]**2 for j in range(3)) + lam*lam)
        Wl = [Wx[j]/l[j]**wexp for j in range(3)]
        bl = [bb[j]*l[j]**(1 - wexp) for j in range(3)]
        M = m + sum(Wl)
        E = np.sqrt(sum(sx[j]**2/l[j]**2 for j in range(3)) + M*M)
        ww = w[i0]*w[:, None]*w[None, :]
        tad += float((ww*sum(l[j]**2*Wl[j]/dd[j] for j in range(3))/(2*Om)).sum())
        num = M + sum((aa[j]**2 - bl[j]**2)*M - 2*aa[j]*bl[j]*sx[j]/l[j] for j in range(3))
        loop += float((ww*num/(2*E*Om*(E + Om))).sum())
    if parts:
        return (tad + loop)/V, tad/V, loop/V
    return (tad + loop)/V


def strain_l(h, kind='Eg'):
    if kind == 'Eg':
        return (np.exp(h), np.exp(-h), 1.0)
    if kind == 'Eg2':               # the other E_g component: (e^h, e^h, e^-2h) normalised traceless
        return (np.exp(h), np.exp(h), np.exp(-2*h))
    if kind == 'iso':
        return (np.exp(h), np.exp(h), np.exp(h))
    raise ValueError(kind)


def hessian(f, d):
    """central second differences with steps d and 2d plus Richardson."""
    f0 = f(0.0); fp, fm = f(d), f(-d); fp2, fm2 = f(2*d), f(-2*d)
    h1 = (fp - 2*f0 + fm)/d**2; h2 = (fp2 - 2*f0 + fm2)/(2*d)**2
    g1 = (fp - fm)/(2*d)
    return f0, g1, h1, h2, (4*h1 - h2)/3


# ---- laws ----
def naive_wilson(r):
    return (np.sin, (lambda k: r*(1 - np.cos(k))), (lambda q: 2*np.sin(q/2)))


def d1_law(b, r):
    from dirac import D1
    L = D1(b, r)
    return L.S, L.W, L


def photon(kind, *args):
    from sublum import SymG
    if kind == 'naive':
        return lambda q: 2*np.sin(np.asarray(q, float)/2)
    if kind == 'Gph':                     # R16-10 'Gph'(c) = R18-5 gamma G_w(c, pi - c) on [0, pi]: d = SymG(c).h
        c, = args; g = SymG(c)
        return lambda q: g.h(np.asarray(q, float))
    if kind == 'cont':
        return lambda q: np.asarray(q, float)
    raise ValueError(kind)
