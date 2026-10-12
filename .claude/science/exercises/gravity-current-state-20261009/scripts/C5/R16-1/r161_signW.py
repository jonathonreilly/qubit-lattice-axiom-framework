"""R16-1 Theorem W checks.
(1) Lemma K (pointwise convexity): for t(q) = 2 - 2cos q (naive photon edge) or t = q^2 (continuum photon), and
    Omega(t; u) = u [D^2 - t(1 - A')] / (2 t s D (D + u)), s = sqrt(t + T), D = s + B', T = dy^2 + dz^2 + lam^2,
    B' = Wy + Wz, A' = Wy^2/dy^2 + Wz^2/dz^2:  d^2 Omega / dq^2 > 0 whenever u > 0, Wy <= dy, Wz <= dz, lam < d(b).
    Random sampling, including outside (H3) (rho = W/d > 1) to see whether the hypothesis is needed.
(2) L*U (Theorem W's coefficient) over D1(b, r) laws, photons (naive; box with c2 <= b), lam; BQ r-family (naive photon),
    and R8-5's overlapping photon boxes (outside H2'), with (H3) diagnostics.
"""
import sys, time; sys.path.insert(0, '.')
import numpy as np
from r161_laws import D1Law, BQLaw
from r161_heavy import L_photon_slot, H3_check, U
rng = np.random.default_rng(161)
t0 = time.time()
def omega_q(q, u, dy, dz, Wy, Wz, lam, kind):
    t = 2 - 2 * np.cos(q) if kind == 'naive' else q ** 2
    T = dy ** 2 + dz ** 2 + lam ** 2; s = np.sqrt(t + T); B = Wy + Wz; Ap = (Wy / dy) ** 2 + (Wz / dz) ** 2
    D = s + B
    return u * (D ** 2 - t * (1 - Ap)) / (2 * t * s * D * (D + u))
print('(1) Lemma K sampling: min over samples of q^2-second-difference / Omega (must be > 0 where hypotheses hold)')
for kind, qlo, qhi in (('naive', 0.3, np.pi), ('continuum', 0.3, 2.5)):
    for rhomax in (1.0, 2.0, 4.0, 16.0):
        n = 400000
        q = rng.uniform(qlo, qhi, n); u = rng.uniform(1e-4, 3.0, n) * rng.choice([1e-3, 1e-1, 1.0], n)
        dy = rng.uniform(0.05, 2.0, n); dz = rng.uniform(0.05, 2.0, n)
        offy = rng.random(n) < 0.5; offz = rng.random(n) < 0.5          # q_y / q_z inside the box -> W = 0
        Wy = np.where(offy, 0.0, rng.uniform(0, rhomax, n) * dy); Wz = np.where(offz, 0.0, rng.uniform(0, rhomax, n) * dz)
        dmin = np.minimum(np.where(offy, 9, dy), np.where(offz, 9, dz))
        lam = rng.uniform(0, 1, n) * np.minimum(dmin, 1.0)                 # lam < d(b) proxy: lam < min d over W>0 legs
        h = 1e-3
        f = lambda s: omega_q(q + s, u, dy, dz, Wy, Wz, lam, kind)
        d2 = (-f(2 * h) + 16 * f(h) - 30 * f(0) + 16 * f(-h) - f(-2 * h)) / (12 * h * h)
        r = d2 / f(0)
        print('  %-9s rho_max=%5.1f: min d2/Omega = %+.4e (fraction negative %.2e)' % (kind, rhomax, r.min(), np.mean(r < 0)), flush=True)
print('(2) L*U, Theorem W coefficient (dc_e ~ L m). (H3): max W/|d|; photon "naive" or (c1,c2)')
rows = []
for b in (1.4, 1.2, 1.0):
    for r in (1 / np.sqrt(3), 0.4, 0.1):
        for ph in ('naive', (0.5 * b, b)):
            for lam in (0.01, 0.05, 0.2):
                law = D1Law(b, r, 1.0, ph)
                L = L_photon_slot(law, lam, Np=64) * U
                rho, _ = H3_check(law)
                print('  D1 b=%.1f r=%.3f photon=%-12s lam=%.2f : L*U = %+.5f   max W/d = %.3f' % (b, r, str(ph), lam, L, rho), flush=True)
for r in (1.0, 2.0, 4.0, 8.0, 16.0, 32.0):
    for (b1, b2) in ((1.0, 2.0), (2.0, 3.0), (0.5, 1.5)):
        law = BQLaw(b1, b2, r, 1.0, 'naive')
        L = L_photon_slot(law, 0.05, Np=64) * U; rho, _ = H3_check(law)
        print('  BQ (%.1f,%.1f) r=%4.1f naive photon lam=0.05: L*U = %+.5f   max W/d = %.3f %s' % (b1, b2, r, L, rho, '(H3 ok)' if rho <= 1 else '(H3 fails)'), flush=True)
print('  outside H2\' (photon plateau transition on the electron edge), R8-5 shapes, r = 1, lam = 0.05:')
for lab, b1, b2, c1, c2 in (('S1', 1.0, 2.0, 1.0, 2.0), ('S2', 1.5, 2.5, 1.5, 2.5), ('S3', 2.0, 3.0, 2.0, 3.0), ('S5', 0.5, 1.5, 0.5, 1.5), ('S7', 1.0, 3.0, 1.0, 3.0), ('S8', 2.5, 3.1, 2.5, 3.1)):
    law = BQLaw(b1, b2, 1.0, 1.0, (c1, c2))
    print('  %s: L*U = %+.5f' % (lab, L_photon_slot(law, 0.05, Np=64) * U), flush=True)
law = D1Law(1.4, 1 / np.sqrt(3), 1.0, (1.4, 2.4))
print('  D1(1.4,1/sqrt3) with photon box (1.4, 2.4) [transition ON the slab, outside H2\']: L*U = %+.5f' % (L_photon_slot(law, 0.05, Np=64) * U))
law = D1Law(1.4, 1 / np.sqrt(3), 1.0, (1.5, 2.8))
print('  D1(1.4,1/sqrt3) with photon box (1.5, 2.8) [outside H2\']: L*U = %+.5f' % (L_photon_slot(law, 0.05, Np=64) * U))
print('elapsed %.1fs' % (time.time() - t0))
