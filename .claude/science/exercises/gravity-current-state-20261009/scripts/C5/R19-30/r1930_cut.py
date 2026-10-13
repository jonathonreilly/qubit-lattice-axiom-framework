"""R19-30 probes (a)-(c): placement audit, jump at q_l = +-pi, and convention-free Fourier decay, for
  scalar U: R13-5's per-leg kernel (as coded in r135_w1_pair.py; R19-5's 'U' completion) and R17-4's E1 midpoint kernel
            (the root's off-axis scalar vertex, which R19-5 says its completion also covers);
  Dirac UD: R18-5's midpoint vertex, (i) as placed in R19-5's r195_dirac_exact.py (UD(kbar) as the site-label kernel,
            no placement phase), (ii) at R9-9's placement with tilde = UD(kbar) (the convention of the rows), then
            (iii) R19-26's F(q_i)F(q_j) re-placement and (iv) the parity-resolved re-placement (lib1930.tilde_component).
Usage: python r1930_cut.py [m]"""
import sys, time, numpy as np
from lib1930 import Scalar, Dirac, wrap, tilde_component, place_phase, GAM, parity_parts
t0 = time.time()
m = float(sys.argv[1]) if len(sys.argv) > 1 else 0.01
SC, DI = Scalar(m=m), Dirac(m=m)
rng = np.random.default_rng(19300)
COMPS = [(0, 1), (0, 2), (1, 2), (0, 0), (1, 1), (2, 2)]
CN = 'xyz'

# ------------------------------ kernels: site-label G (complex scalar or 4x4) ----------------------------------------
def G_scalar(kind, mode, k1, k2, i, j):
    q = wrap(k1 + k2)                                   # pair creation a^dag_{k1} a^dag_{k2}
    nrm = np.sqrt(SC.eps(k1)*SC.eps(k2))
    if kind == 'Upl':                                   # R13-5: -(w_i(k1) w_j(k2) + w_j(k1) w_i(k2)) / (2 sqrt(e1 e2))
        t = -(SC.f(k1[..., i])*SC.f(k2[..., j]) + SC.f(k1[..., j])*SC.f(k2[..., i]))/(2*nrm)
        if mode == 'FF' and i != j:
            from lib1930 import Fplace
            t = t*Fplace(q[..., i])*Fplace(q[..., j])
        if mode == 'PR':
            raise ValueError
    else:                                               # E1: f_i(K) f_j(K) / sqrt(e1 e2), K = k1 - q/2 (relative)
        K = k1 - q/2
        fun = lambda kb: (SC.f(kb[..., i])*SC.f(kb[..., j]))[..., None]
        t = tilde_component(fun, K, q, i, j, mode)[..., 0]/nrm
    return place_phase(q, i, j)*t

def G_dirac(conv, mode, k1, k2, i, j):
    q = wrap(k1 - k2); kb = k2 + q/2
    fun = lambda kk: DI.UDcoef(kk, i, j)
    c = tilde_component(fun, kb, q, i, j, mode)
    X = np.einsum('...a,aij->...ij', c, GAM)
    Pp1, Pm1, Pp2, Pm2 = DI.proj(k1, 1), DI.proj(k1, -1), DI.proj(k2, 1), DI.proj(k2, -1)
    B = Pp1 @ X @ Pm2 + Pm1 @ X @ Pp2
    if conv == 'R19-5':                                 # UD(kbar) used directly as the site-label kernel
        return B
    return place_phase(q, i, j)[..., None, None]*B      # tilde = UD(kbar) (+ re-placement), rows' convention

# ------------------------------ (b) jump across q_l = +-pi ------------------------------------------------------------
def cut_points(n, l, eps, chan):
    k2 = rng.uniform(-np.pi, np.pi, (n, 3)); qo = rng.uniform(-np.pi, np.pi, (n, 3))
    qa, qb = qo.copy(), qo.copy(); qa[:, l] = np.pi - eps; qb[:, l] = np.pi + eps
    if chan == 'pair':                                   # k1 + k2 = q
        return qa - k2, qb - k2, k2
    return k2 + qa, k2 + qb, k2                          # k1 - k2 = q

def jump(Gf, l, eps, chan, n=120):
    k1a, k1b, k2 = cut_points(n, l, eps, chan)
    ga, gb = Gf(k1a, k2), Gf(k1b, k2)
    ax = tuple(range(1, ga.ndim))
    d = np.abs(ga - gb); s = np.abs(ga)
    if ga.ndim > 1:
        d = d.max(axis=ax); s = s.max(axis=ax)
    return d.max(), s.max()

# ------------------------------ (c) Fourier coefficients along a full k1 line -----------------------------------------
def fourier(Gf, l, N=4096, chan='scat', seed=0):
    r = np.random.default_rng(1930 + seed)
    k2 = r.uniform(-np.pi, np.pi, 3); k1o = r.uniform(-np.pi, np.pi, 3)
    t = 2*np.pi*np.arange(N)/N - np.pi
    k1 = np.tile(k1o, (N, 1)); k1[:, l] = t
    g = Gf(k1, np.tile(k2, (N, 1)))
    g = g.reshape(N, -1)
    c = np.abs(np.fft.fft(g, axis=0)).max(1)/N
    idx = np.minimum(np.arange(N), N - np.arange(N))
    return [c[(idx >= a) & (idx < b)].max() for (a, b) in ((32, 64), (128, 256), (512, 1024), (1024, 2048))]

def report(label, Gf, chan, comps=COMPS):
    print('== %s ==' % label, flush=True)
    for (i, j) in comps:
        g = lambda k1, k2: Gf(k1, k2, i, j)
        js = []
        for l in range(3):
            j6, s6 = jump(g, l, 1e-6, chan); j8, _ = jump(g, l, 1e-8, chan)
            js.append('%s: %.1e/%.1e' % (CN[l], j6, j8))
        F = fourier(g, 0, chan=chan); Fz = fourier(g, 2, chan=chan, seed=1)
        print('  T^%s%s  jump at q_l=+-pi (eps=1e-6/1e-8) %s  |G|max %.2f | Fourier max|c_n| along k1_x n=[32,64) %.1e [128,256) %.1e [512,1024) %.1e [1024,2048) %.1e ; along k1_z [1024,2048) %.1e'
              % (CN[i], CN[j], '  '.join(js), s6, *F, Fz[-1]), flush=True)

if __name__ == '__main__':
    print('R19-30 cut/Fourier audit, m = %g. Scalar G_w(%.7f, %.6f); Dirac D1(%.9f, %.9f) (analytic laws).'
          % (m, SC.bs, SC.w, DI.b, DI.r))
    # parity content of the per-axis building blocks (fraction of the 'wrong' class), sanity
    kk = np.linspace(-np.pi, np.pi, 2001)
    fo = 0.5*(SC.f(kk) - SC.f(kk + np.pi)); fe = 0.5*(SC.f(kk) + SC.f(kk + np.pi))
    print('scalar f = sigma sigma\': max|odd-class part| %.3f, max|even-class part| %.3f (NN f = sin k would be pure odd)' % (np.abs(fo).max(), np.abs(fe).max()))
    Sx = DI.S(kk); print('Dirac S(k+pi) + S(k): %.1e ; dW(k+pi) + dW(k): %.1e ; W(k+pi) + W(k) - W_pi: %.1e  (S, W\', W - W_pi/2 are pure odd class)'
          % (np.abs(DI.S(kk + np.pi) + Sx).max(), np.abs(DI.dW(kk + np.pi) + DI.dW(kk)).max(), np.abs(DI.W(kk + np.pi) + DI.W(kk) - DI.Wpi).max()))
    report('scalar U, R13-5 per-leg kernel as coded (site-label = e^{-iq.p} x per-leg product)', lambda a, b, i, j: G_scalar('Upl', 'raw', a, b, i, j), 'pair', comps=[(0, 1), (0, 0)])
    report('scalar U, R13-5 per-leg kernel + R19-26 F(q_i)F(q_j)', lambda a, b, i, j: G_scalar('Upl', 'FF', a, b, i, j), 'pair', comps=[(0, 1), (0, 0)])
    report('scalar U, E1 midpoint kernel (root off-axis vertex) at R9-9 placement', lambda a, b, i, j: G_scalar('E1', 'raw', a, b, i, j), 'pair', comps=[(0, 1), (0, 0)])
    report('scalar U, E1 midpoint + F(q_i)F(q_j)', lambda a, b, i, j: G_scalar('E1', 'FF', a, b, i, j), 'pair', comps=[(0, 1), (0, 0)])
    report('scalar U, E1 midpoint + parity-resolved re-placement', lambda a, b, i, j: G_scalar('E1', 'PR', a, b, i, j), 'pair', comps=[(0, 1), (0, 0)])
    report('Dirac UD as placed in R19-5 r195_dirac_exact.py (UD(kbar) = site-label kernel)', lambda a, b, i, j: G_dirac('R19-5', 'raw', a, b, i, j), 'scat', comps=[(0, 1), (0, 0)])
    report('Dirac UD at R9-9 placement, tilde = UD(kbar) (rows convention)', lambda a, b, i, j: G_dirac('rows', 'raw', a, b, i, j), 'scat', comps=[(0, 1), (0, 0)])
    report('Dirac UD at R9-9 placement + F(q_i)F(q_j)', lambda a, b, i, j: G_dirac('rows', 'FF', a, b, i, j), 'scat', comps=[(0, 1), (0, 0)])
    report('Dirac UD at R9-9 placement + parity-resolved re-placement', lambda a, b, i, j: G_dirac('rows', 'PR', a, b, i, j), 'scat')
    print('time %.1f s' % (time.time() - t0))
