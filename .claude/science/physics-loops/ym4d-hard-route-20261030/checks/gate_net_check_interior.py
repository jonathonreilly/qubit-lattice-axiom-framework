#!/usr/bin/env python3
"""Does the strip bound extend to moving one thick interior observable alone?

g(z) = Z^-1 Tr( F^ T^(m1+z) A^ T^(m2-z) G^ T^r ), all slabs of thickness 1, on 3D Z_2 on
2 x 2 x T. Lemma 10.1 bounds one cut only. Theorem 10.2(e) claims analyticity in one
coordinate by "bounded analytic functions on a strip". Here: maximise |g(x+iy)| over all
F, A, G with sup norm 1 (complex), by alternating maximisation of this trilinear form.
A value above 1 at y != 0 means the sup-norm bound fails for the interior move on this torus.
Controls: real z at integer shifts is an expectation, so it must stay <= 1. For one cut
(A = 1) Lemma 10.1 says <= 1 everywhere on the strip.
"""
import numpy as np
from net_check_lemma101 import build, slab_op

np.set_printoptions(precision=5, suppress=True, linewidth=120)
rng = np.random.default_rng(7)


def op(h, B, K):
    """Slab kernel with an insertion depending on (eta, eta') only."""
    return slab_op(h, B, np.broadcast_to(K, (16, 256, 256)))


def maximise(h, B, T0, lam, Q, m1, m2, r, z, Z, iters=40, fix_A=False):
    good = lam > 0
    lq = np.where(good, np.log(np.where(good, lam, 1)), -np.inf)

    def Tpow(w):
        d = np.where(good, np.exp(w * lq), 0.0)
        return (Q * d) @ Q.T

    P1 = Tpow(m1 + z)
    P2 = Tpow(m2 - z)
    P3 = Tpow(r)
    # weights of the slab kernels, normalised by the top eigenvalue
    wgt = T0 / lam_scale
    # T0 = slab kernel with insertion 1, entrywise positive; insertions multiply entrywise
    # only after the u sum when the insertion does not depend on u.
    F = np.exp(2j * np.pi * rng.random((256, 256)))
    A = np.ones((256, 256), dtype=complex) if fix_A else np.exp(2j * np.pi * rng.random((256, 256)))
    G = np.exp(2j * np.pi * rng.random((256, 256)))
    val = 0.0
    for _ in range(iters):
        # gradient wrt F: entrywise wgt * transpose of (P1 A^ P2 G^ P3)
        X = P1 @ (wgt * A) @ P2 @ (wgt * G) @ P3
        F = np.exp(-1j * np.angle(X.T + 1e-300))
        X = P2 @ (wgt * G) @ P3 @ (wgt * F) @ P1
        if not fix_A:
            A = np.exp(-1j * np.angle(X.T + 1e-300))
        X = P3 @ (wgt * F) @ P1 @ (wgt * A) @ P2
        G = np.exp(-1j * np.angle(X.T + 1e-300))
        val = abs(np.trace((wgt * F) @ P1 @ (wgt * A) @ P2 @ (wgt * G) @ P3)) / Z
    return val


print(" beta  T  m1 m2  r     z            max|g|  (A free)   max|g|  (A = 1, one cut)")
for beta in [0.05, 0.2, 0.44, 0.76, 1.5]:
    h, B = build(beta)
    T0 = slab_op(h, B)
    T0 = 0.5 * (T0 + T0.T)
    ev, Q = np.linalg.eigh(T0)
    ev[np.abs(ev) < 1e-13 * ev.max()] = 0.0
    lam_scale = ev.max()
    lam = ev / lam_scale
    for (m1, m2, r) in [(1, 1, 1), (1, 1, 2), (2, 2, 1), (1, 1, 6)]:
        T = 3 + m1 + m2 + r
        Z = np.sum(lam[lam > 0] ** T)
        for z in [0.0, 0.5, 0.5j, 3.1j, 17.0j, 0.5 + 3.1j]:
            a = maximise(h, B, T0, lam, Q, m1, m2, r, z, Z)
            b = maximise(h, B, T0, lam, Q, m1, m2, r, z, Z, fix_A=True)
            flag = "  <-- exceeds 1" if a > 1 + 1e-9 else ""
            print("%5.2f %2d  %d  %d  %d  %-12s %.6f        %.6f%s" % (beta, T, m1, m2, r, z, a, b, flag))
