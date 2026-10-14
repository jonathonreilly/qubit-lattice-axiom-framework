"""F6 (a) loops 1 and 4 on the R18-9 root (scalar SymG(b_s) + photon Gph(2.9435)), SF, Feynman gauge, P = 0, counterterm fixed at t = 0.
Convergence in grid (n, hmax, mph) and FD step d; branches: m = 0 (main; m_H a ~ 1e-17) and m = 0.01 (the rows' mass); 0+ root b_s.
Decomposition: scalar strained alone / photon strained alone / common flows (relabelling controls); gauge-parameter term."""
import numpy as np, time
from f6_lib import *
t00 = time.time()
G = Phot(CPH)
def run(bs, n, hm, mph, d, m=0.0, **kw):
    S = Phot(bs); x, w = mkgrid(bs, n, hm, mph)
    return len(x), hess_even(lambda t: sig_gauge(S, G, x, w, t, m=m, **kw), d)
print('LOOP 1 (U(1)), per e^2, SF units t.  R18-9 root b_s = %.9f, Gph(%.4f)' % (BS, CPH))
for (n, hm, mph, d) in ((6, 0.25, 6, 0.003), (8, 0.15, 16, 0.003), (10, 0.10, 24, 0.003), (10, 0.10, 24, 0.0015), (12, 0.08, 32, 0.0015)):
    N, r = run(BS, n, hm, mph, d)
    print('  m=0  n=%2d hmax=%.2f mph=%2d nodes=%3d d=%.4f: Sig(0) %+.10f  Hess (d) %+.8e (2d) %+.8e Rich %+.8e  [H-cov x4 %+.5e]  (%.0fs)'
          % (n, hm, mph, N, d, r[0], r[1], r[2], r[3], 4*r[3], time.time() - t00), flush=True)
S = Phot(BS); x, w = mkgrid(BS, 10, 0.10, 24)
print('parts at t=0 (tad, temporal, -exch):', ['%+.8f' % v for v in sig_gauge(S, G, x, w, 0.0, parts=True)[1:]])
for t in (0.003,):
    p0 = sig_gauge(S, G, x, w, 0.0, parts=True); p1 = sig_gauge(S, G, x, w, t, parts=True)
    print('parts Hessian (single step %.4f): tad %+.6e temporal %+.6e exch %+.6e' % (t, *[2*(a - b)/t**2 for a, b in zip(p1[1:], p0[1:])]))
d = 0.0015
for lab, kw in (('m = 0.01 (rows mass)', dict(m=0.01)), ('m = 0.001', dict(m=0.001)),
                ('control: photon unstrained (scalar own flow)', dict(gflow='none')),
                ('control: scalar unstrained (photon own flow)', dict(sflow='none')),
                ('control K1: scalar on the photon flow (common separable flow)', dict(sflow='phot')),
                ('control K2: photon on the scalar flow (common separable flow)', dict(gflow='scal'))):
    r = hess_even(lambda t: sig_gauge(S, G, x, w, t, **kw), d)
    print('  %-62s Sig(0) %+.10f  Hess Rich %+.8e' % (lab, r[0], r[3]), flush=True)
x0, w0 = mkgrid(BS0, 10, 0.10, 24); S0 = Phot(BS0)
r = hess_even(lambda t: sig_gauge(S0, G, x0, w0, t), d)
print('  %-62s Sig(0) %+.10f  Hess Rich %+.8e' % ('0+ root b_s = 2.590035, m = 0', r[0], r[3]), flush=True)
print('gauge-parameter term: Sig_xi/e^2 = (1 - xi) X(m);  X and d2_t X:')
for m in (0.01, 0.003, 0.001):
    r = hess_even(lambda t: sig_gauge(S, G, x, w, t, m=m, xi=True), d)
    print('  m=%.3f  X %+.6e  d2_t X %+.6e   (X/m^2 %+.4f, d2X/m^2 %+.4f)' % (m, r[0], r[3], r[0]/m**2, r[3]/m**2), flush=True)
print('LOOP 4 (quartic): d2_t G_s  (Sigma_lam = 6 lam G_s)')
for (n, hm, mph, d) in ((8, 0.15, 16, 0.003), (10, 0.10, 24, 0.0015), (12, 0.08, 32, 0.0015)):
    xx, ww = mkgrid(BS, n, hm, mph)
    r = hess_even(lambda t: g_scalar(S, xx, ww, t), d)
    print('  R18-9 b_s, m=0, nodes %3d d %.4f: G_s(0) %+.10f  Hess Rich %+.8e' % (len(xx), d, r[0], r[3]), flush=True)
r = hess_even(lambda t: g_scalar(S, x, w, t, m=0.01), 0.0015)
print('  R18-9 b_s, m=0.01: Hess Rich %+.8e' % r[3])
r = hess_even(lambda t: g_scalar(S0, x0, w0, t), 0.0015)
print('  0+ root b_s, m=0: Hess Rich %+.8e   (= 2 c2^s; R19-11 -2.722e-3)' % r[3])
print('time %.0f s' % (time.time() - t00))
