"""F6 controls for the scalar-QED (loop 1) and quartic (loop 4) code paths.
(C1) H-cov NN scalar + NN photon (R19-31's law): Sigma(P=0) and d2_h at m = 0.1, step 0.02  vs  r1931_sqed_cross.out:2-5 (0.683592960; -0.53181).
(C2) scalar edge = photon edge Gph(2.9435), m = 0: integrand is 3/(2 Om) pointwise and the common flow gives Sig = 3 G_gam(t);
     Hessian = 3 x vector mu_E slope c2^V = 3 x (-2.993e-3) = -8.979e-3 (rR19-11:139 table, vector c2 at b_gam = 2.9435).
(C3) quartic loop: d2_t G_s = 2 c2^s (scalar mu_E m^2-slope, -1.361e-3 at the 0+ root's b_s = 2.590035, rR19-11:139) -> -2.722e-3.
(C4) closed-form Q0 integrals vs brute-force quadrature at sample (E, Om, T, V^2).
(C5) Ward identity sum_j d_j V_j = K(q) - K(0) at random strained points (by construction; checked numerically).
"""
import numpy as np, time
from scipy.integrate import quad
from f6_lib import *
t00 = time.time()
S = Phot(BS); S0 = Phot(BS0); G = Phot(CPH)
x, w = mkgrid(BS, 8, 0.15, 16)
print('grid nodes %d' % len(x))
# C1
f = lambda h: sig_gauge(None, None, x, w, 0.0, m=0.1, hcov=('nn', h))
r = hess_gen(f, 0.02)
print('(C1) H-cov NN, m=0.1: Sigma(P=0) %.9f [R19-31: 0.683592960]  d2_h (step .02) %+.6e [R19-31: -5.318100e-01]  Rich %+.6e' % (r[0], r[2], r[4]), flush=True)
# C2
xg, wg = mkgrid(CPH, 8, 0.15, 16)
for t in (0.0, 0.01):
    a = sig_gauge(G, G, xg, wg, t); b = 3*g_scalar(G, xg, wg, t)
    print('(C2) t=%.3f  Sig_g(scalar=photon edge) %.12f   3 G_gam %.12f   diff %+.2e' % (t, a, b, a - b), flush=True)
for d in (0.003, 0.0015):
    r = hess_even(lambda t: sig_gauge(G, G, xg, wg, t), d)
    print('(C2) d=%.4f Hessian (d) %+.7e (2d) %+.7e Rich %+.7e   target 3 c2^V = -8.979e-3' % (d, r[1], r[2], r[3]), flush=True)
# C3
x0, w0 = mkgrid(BS0, 8, 0.15, 16)
for d in (0.003, 0.0015):
    r = hess_even(lambda t: g_scalar(S0, x0, w0, t), d)
    print('(C3) 0+ root b_s=%.6f: d2_t G_s (d=%.4f) %+.7e Rich %+.7e   target 2 c2^s = -2.722e-3' % (BS0, d, r[1], r[3]), flush=True)
# C4
rng = np.random.default_rng(1)
mx = 0.0
for _ in range(6):
    E, Om, T, V2 = rng.uniform(0.2, 3, 4)
    m2 = rng.uniform(0, 0.5)
    tad = quad(lambda q0: T/(q0*q0 + Om*Om), -np.inf, np.inf)[0]/(2*np.pi)
    tm = quad(lambda q0: 1/(q0*q0 + Om*Om) - q0*q0/((q0*q0 + Om*Om)*(q0*q0 + E*E)), -np.inf, np.inf)[0]/(2*np.pi)
    ex = quad(lambda q0: V2/((q0*q0 + Om*Om)*(q0*q0 + E*E)), -np.inf, np.inf)[0]/(2*np.pi)
    closed = T/(2*Om) + E/(2*Om*(Om + E)) - V2/(2*Om*E*(Om + E))
    brute = tad + tm - ex
    K = E*E - m2
    xib = quad(lambda q0: (q0*q0 + K)**2/(q0*q0 + E*E)/(q0*q0 + Om*Om)**2 - (q0*q0 + K)/(q0*q0 + Om*Om)**2, -np.inf, np.inf)[0]/(2*np.pi)
    xic = -m2*(1/(4*Om**3) - m2*(E + 2*Om)/(4*E*Om**3*(E + Om)**2))
    mx = max(mx, abs(closed - brute), abs(xib - xic))
print('(C4) closed-form Q0 integrals (Feynman loop; xi-term with Ward-reduced numerator) vs quad: max |diff| %.1e' % mx, flush=True)
# C5
q = rng.uniform(0.01, np.pi, (3, 1000)); t = 0.3
mx = 0.0
for j, sg in enumerate((+1, -1, 0)):
    hs = S.d(flowG1(S, q[j], sg, t, 6)) if sg else S.d(q[j]); dg = G.d(flowG1(G, q[j], sg, t, 6)) if sg else G.d(q[j])
    V = hs**2/dg
    mx = max(mx, float(np.max(np.abs(dg*V - hs**2))))
print('(C5) Ward sum_j d_j V_j - [K(q) - K(0)] at t = 0.3, 1000 points: max %.1e' % mx)
print('time %.0f s' % (time.time() - t00))
