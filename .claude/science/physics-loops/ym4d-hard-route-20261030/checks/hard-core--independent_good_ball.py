#!/usr/bin/env python3
"""Lemma 4.7e of Text 4.7 on the ball: state G as a measure on the whole contour, adjoint 3-vector labels.

mu_s[Phi]  := int_{|x| <= P} rho_3(x - s) Phi(x) d^3 x
muA_s[Phi] := int_{|t| <= p} rho_3(t) Phi(s + t) d^3 t
G_s := mu_s - muA_s,  s = u + i v in C^3.

The lemma claims (i) an exact identity G_s = (horizontal tail over p < |t|, |t + u| <= P) + (wall over |x| = P, 0 <= tau <= 1),
and (ii) |G_s[Phi]| <= C exp(-p^2 / 3) M_s(Phi), M_s := sup over the body D_s of exp(-|z - s|^2 / 8) |Phi(z)|.
C below is computed from the proof, not fitted.

PRE-STATED CRITERIA, written before the first run. Axisymmetric tests about e_3, s = (0, 0, u3 + i y), P = 6, p = 3, y in {0.25, 0.75},
u3 in {0, 1.5}. Phi: exp(i a z_3) for a in {1, 5, 15, 30, 60, 90}, exp(q z.z) for q in {0.02, 0.1}, and 1 + z_3^3.
PASS-IDENT: mu - muA equals tail + wall, relative error at most 1e-7 or absolute at most 1e-12.
PASS-BOUND: |G| <= C exp(-p^2 / 3) M_s, with M_s sampled on the body (sampled sup: a lower estimate of M_s; the bound must hold with it
only if it is not too low, so this is a test that can fail, not a proof).
PASS-D1: at y = 0.75, u3 = 0, the old shifted-line inequality |G| <= C exp(-p^2 / 3) exp(-a y) fails by a factor above 1e3 at some a,
which is defect 1 of gates/independent-2c-codex-b4de676b7.md in three dimensions. CONTROL: that factor must not be above 1 at a = 1.
RESULT OF THE FIRST RUN, as registered: FAIL-IDENT, with error up to 1.4e-7 at |G| = 0.6; PASS-BOUND, PASS-D1, CONTROL-OK. ident on the waves was at most 6e-10 absolute. Suspected cause, written before the rerun: the wall used a subsample of Gauss nodes
in tau, which is not a quadrature rule (a 'coarser net' of mine). ADDED BEFORE THE SECOND RUN: 60-point Gauss rule in tau, same criteria.
RESULT OF THE SECOND RUN: PASS-IDENT, PASS-BOUND, PASS-D1 (factor 2.15 at a = 30, 6.5e9 at a = 60, 1e19 at a = 90), CONTROL-OK, with C = 2.79 from the proof, largest ratio to M_s 1.72 (gauss.10, u3 = 0, y = 0.75, a sampled sup). It tests the formula of Lemma 4.7e on axisymmetric cases, and nothing about the actual integrand.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
import resource
import numpy as np

P, p = 6.0, 3.0
NOD = np.polynomial.legendre.leggauss(1400)


def nodes(a, b):
    x, w = NOD
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w


def rho3(z1sq_plus_z2sq, z3):
    return (2 * np.pi) ** -1.5 * np.exp(-(z1sq_plus_z2sq + z3 * z3) / 2)


def ball_integral(f, R, centre3=0.0):
    """int over |x| <= R of f(varrho^2, x3) with x3 measured from 0, axisymmetric, polar about the origin."""
    r, wr = nodes(0.0, R)
    th, wt = nodes(0.0, np.pi)
    rr, tt = np.meshgrid(r, th, indexing="ij")
    ww = np.outer(wr, wt)
    x3 = rr * np.cos(tt)
    vs = (rr * np.sin(tt)) ** 2
    return np.sum(2 * np.pi * rr * rr * np.sin(tt) * ww * f(vs, x3 + centre3))


def checks(Phi, name, u3, y):
    s3 = u3 + 1j * y
    mu = ball_integral(lambda vs, x3: rho3(vs, x3 - s3) * Phi(vs, x3 + 0j), P)
    muA = ball_integral(lambda vs, t3: rho3(vs, t3) * Phi(vs, t3 + s3), p)
    G = mu - muA
    # horizontal part at tau = 1: int over |t + u| <= P, in x = t + u, minus state A
    hor = ball_integral(lambda vs, x3: rho3(vs, x3 - u3) * Phi(vs, x3 + 1j * y), P) - muA
    # wall: i int_0^1 dtau int_{|x| = P} (v . n) h(x + i tau v) dsigma, h(z) = rho_3(z - s) Phi(z), mu = F(0) = F(1) - int_0^1 F'
    xg, wg = np.polynomial.legendre.leggauss(60)
    tau, wtau = 0.5 * (xg + 1), 0.5 * wg
    th, wt = nodes(0.0, np.pi)
    wall = 0j
    for ta, wta in zip(tau, wtau):
        x3 = P * np.cos(th)
        vs = (P * np.sin(th)) ** 2
        z3 = x3 + 1j * ta * y
        wall += wta * 1j * np.sum(2 * np.pi * P * P * np.sin(th) * wt * y * np.cos(th) * rho3(vs, z3 - s3) * Phi(vs, z3))
    rhs = hor - wall
    ident = abs(G - rhs)
    # M_s, sampled on the body
    rs = np.linspace(0, P, 61)
    ths = np.linspace(0, np.pi, 61)
    tas = np.linspace(0, 1, 9)
    Ms = 0.0
    for ta in tas:
        rr, tt = np.meshgrid(rs, ths, indexing="ij")
        x3 = rr * np.cos(tt)
        vs = (rr * np.sin(tt)) ** 2
        z3 = x3 + 1j * ta * y
        dist2 = vs + (x3 - u3) ** 2 + (1 - ta) ** 2 * y * y
        Ms = max(Ms, float(np.max(np.exp(-dist2 / 8) * np.abs(Phi(vs, z3)))))
    return G, ident, Ms


# C from the proof: tails (2 pi)^(-3/2) 4 pi int_p^inf r^2 exp(-3 r^2 / 8) dr, walls |v| 4 pi P^2 (2 pi)^(-3/2) exp(-103 P^2 / 512)
r, wr = nodes(p, 12 * p)
tail = (2 * np.pi) ** -1.5 * 4 * np.pi * np.sum(wr * r * r * np.exp(-3 * r * r / 8))
wall_c = (P / 8) * 4 * np.pi * P * P * (2 * np.pi) ** -1.5 * np.exp(-103 * P * P / 512)
C = (tail + wall_c) * np.exp(p * p / 3)
print("C from the proof at P=%g, p=%g: %.4f (tail part %.3e, wall part %.3e)" % (P, p, C, tail, wall_c))

ok_ident = ok_bound = True
d1_factor = {}
for u3 in (0.0, 1.5):
    for y in (0.25, 0.75):
        for a in (1.0, 5.0, 15.0, 30.0, 60.0, 90.0):
            Phi = lambda vs, z3, a=a: np.exp(1j * a * z3)
            G, ident, Ms = checks(Phi, "wave", u3, y)
            rel = ident / max(abs(G), 1e-300)
            ok_ident &= (rel <= 1e-7 or ident <= 1e-12)
            ratio = abs(G) / (np.exp(-p * p / 3) * Ms)
            ok_bound &= ratio <= C
            old = abs(G) / (C * np.exp(-p * p / 3) * np.exp(-a * y))
            if y == 0.75 and u3 == 0.0:
                d1_factor[a] = old
            print("wave a=%5.1f u3=%.1f y=%.2f |G|=%.3e ident=%.1e ratio to M_s=%.3e old-line factor=%.3e" % (a, u3, y, abs(G), ident, ratio, old))
        for name, Phi in (("gauss.02", lambda vs, z3: np.exp(0.02 * (vs + z3 * z3))), ("gauss.10", lambda vs, z3: np.exp(0.10 * (vs + z3 * z3))), ("cubic", lambda vs, z3: 1 + z3 ** 3)):
            G, ident, Ms = checks(Phi, name, u3, y)
            rel = ident / max(abs(G), 1e-300)
            ok_ident &= (rel <= 1e-7 or ident <= 1e-12)
            ratio = abs(G) / (np.exp(-p * p / 3) * Ms)
            ok_bound &= ratio <= C
            print("%s u3=%.1f y=%.2f |G|=%.3e ident=%.1e ratio to M_s=%.3e" % (name, u3, y, abs(G), ident, ratio))

print("PASS-IDENT" if ok_ident else "FAIL-IDENT")
print("PASS-BOUND" if ok_bound else "FAIL-BOUND")
print("PASS-D1" if max(d1_factor.values()) > 1e3 else "FAIL-D1", {k: float("%.3g" % v) for k, v in d1_factor.items()})
print("CONTROL-OK" if d1_factor[1.0] <= 1 else "CONTROL-FAIL")
print("max RSS MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6)
