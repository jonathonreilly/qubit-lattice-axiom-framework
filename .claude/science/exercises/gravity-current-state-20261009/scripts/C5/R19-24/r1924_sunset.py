"""R19-24 probe (b) toy: does a one-loop speed clause stay zero at two loops?
lambda phi^4 on Z^3 x R (continuous Euclidean time), real scalar, spatial symbol eps(k)^2:
  NN:   sum_j 4 sin^2(k_j/2)
  G(b): sum_j h_b(k_j)^2  (R14-1 box-exact subluminal scalar edge, archived sublum.SymG; b = 2.526 is the gravity root's scalar edge)
Gamma = w^2 + eps^2 + m^2 + Pi.  One loop: Pi_1 = (lam/2) G(0,0): momentum- and frequency-independent, so delta c^2 = 0 EXACTLY at one loop
(proved). Two loops: the double tadpole is also constant; the sunset Pi_2(x,tau) = -(lam^2/6) G(x,tau)^3 is the only O(lam^2) source of a speed shift.
Speed (first order): c^2 - 1 = d_{p^2} Pi + d_{E^2} Pi on shell (E = m, p = 0)  [Pi(p, w = iE)];  Euclidean-zero variant: d_{p^2}Pi - d_{w^2}Pi at (0,0).
Position space: d_{p1^2} -> -1/2 sum x1^2 (.), cosh(E tau) weight on shell, d_{E^2} -> sum tau sinh(E tau)/(2E) (.).
Control: Z^4 hypercubic (time on the grid, a_t = a_s): Euclidean-zero LV = 0 by the 90-degree t<->x1 rotation.
Printed: delta c^2 / lam^2 (multiply by lam^2; (16 pi^2)^2 = 24936 converts to 'per (lam/16pi^2)^2')."""
import sys, os, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'arch', 'R16-10', 'arch', 'R16-2'))
from sublum import SymG
t0 = time.time()

def panels(tmax):
    edges = [0.0, 0.25, 0.5, 1.0]
    while edges[-1] < tmax: edges.append(edges[-1]*1.6)
    xg, wg = np.polynomial.legendre.leggauss(20)
    T, W = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        T.append(0.5*(b-a)*xg + 0.5*(b+a)); W.append(0.5*(b-a)*wg)
    return np.concatenate(T), np.concatenate(W)

def sunset_speed(L, m, eps2):
    k = 2*np.pi*np.fft.fftfreq(L)
    KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
    E = np.sqrt(m**2 + eps2(KX) + eps2(KY) + eps2(KZ))
    n = np.fft.fftfreq(L)*L                      # minimal-image coordinates
    X1 = np.meshgrid(n, n, n, indexing='ij')[0]
    T, Wt = panels(40.0/m)
    # accumulators: Euclidean-zero and on-shell moments of S = G^3 (Pi_2 = -(lam^2/6) S)
    A_x2 = A_t2 = A_x2c = A_ts = 0.0; tail = 0.0
    for tau, w in zip(T, Wt):
        G = np.real(np.fft.ifftn(np.exp(-E*tau)/(2*E)))        # G(x,tau) = (1/L^3) sum_k e^{ikx} e^{-E tau}/(2E)
        S = G**3
        sx2 = np.sum(X1**2*S); s0 = np.sum(S)
        A_x2 += 2*w*sx2; A_t2 += 2*w*tau**2*s0                  # factor 2: tau in (-inf, inf), S even in tau
        A_x2c += 2*w*np.cosh(m*tau)*sx2; A_ts += 2*w*tau*np.sinh(m*tau)/(2*m)*s0
        if tau > 0.8*T[-1]: tail = max(tail, abs(np.cosh(m*tau)*s0))
    pref = -1.0/6.0                                               # Pi_2 / lam^2 = -(1/6) S
    dp2_E = pref*(-0.5*A_x2); dw2_E = pref*(-0.5*A_t2)
    dp2_os = pref*(-0.5*A_x2c); dE2_os = pref*A_ts
    return dp2_E - dw2_E, dp2_os + dE2_os, dp2_E, dw2_E, tail

nn = lambda k: 4*np.sin(k/2)**2
gb = SymG(2.526103698477); gbox = lambda k: gb.g(k)
gb2 = SymG(1.4); gbox2 = lambda k: gb2.g(k)
print('lambda phi^4 sunset speed shift on Z^3 x R; one-loop shift = 0 exactly (constant tadpole).')
print('columns: edge, L, m | delta c^2/lam^2 (Euclidean-zero LV) | delta c^2/lam^2 (on-shell) | [d_p2 Pi, d_w2 Pi at 0] | on-shell tail', flush=True)
for name, e2 in (('NN', nn), ('G(2.526)', gbox), ('G(1.4)', gbox2)):
    for m in (1.0, 0.5, 0.3):
        for L in ((24, 32) if m >= 0.5 else (32, 48)):
            dE, dos, a, b, tl = sunset_speed(L, m, e2)
            print('%-9s L=%2d m=%.2f | %+.4e | %+.4e | [%+.4e, %+.4e] | %.1e  (%.0fs)' % (name, L, m, dE, dos, a, b, tl, time.time()-t0), flush=True)

# Z^4 hypercubic control (Euclidean, a_t = a_s): Pi_2(x,t) = -(1/6) G^3, G = 4D lattice propagator
def z4_control(L, m):
    k = 2*np.pi*np.fft.fftfreq(L)
    K = np.meshgrid(k, k, k, k, indexing='ij')
    den = m**2 + sum(4*np.sin(q/2)**2 for q in K)
    G = np.real(np.fft.ifftn(1.0/den)); S = G**3
    n = np.fft.fftfreq(L)*L; X = np.meshgrid(n, n, n, n, indexing='ij')
    dp2 = (-1/6)*(-0.5)*np.sum(X[1]**2*S); dw2 = (-1/6)*(-0.5)*np.sum(X[0]**2*S)
    return dp2 - dw2, dp2
for m in (0.5, 0.3):
    d, a = z4_control(24, m)
    print('Z^4 control L=24 m=%.2f: Euclidean-zero LV = %+.3e (d_p2 Pi = %+.4e)  (%.0fs)' % (m, d, a, time.time()-t0), flush=True)
print('elapsed %.1fs' % (time.time()-t0))
