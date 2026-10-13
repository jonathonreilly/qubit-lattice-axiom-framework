#!/usr/bin/env python3
"""R19-6 [L]: one Lie-derivative lemma behind R18-11's Theorem G and R19-3's Lemma D.

Lemma L (stated before the run).  Let Y^{mu nu} be a symmetric contravariant tensor density of weight w that is
flat-conserved, d_mu Y^{mu nu} = 0, and let xi be a vector field; both linear in the same fluctuation (one Fourier
mode and its conjugate, i.e. zero total momentum after averaging).  Then the zero-momentum (phase-averaged) part of
the Lie derivative is
        < (L_xi Y)^{mu nu} >  =  (w - 1) < (d.xi) Y^{mu nu} > .
Instances:
  (i)  Y = the set-A record mode J (flat-conserved by construction, R15-2 Lemma CU)          -> Theorem G (a = 4 - 2w);
  (ii) Y = G^(1)mu nu[X] for arbitrary X (conserved identically: linearized Bianchi)         -> Lemma D, via the
       bilinear covariance identity 2 Y_w^(2)(L_xi eta, X) = L_xi(Y_w^(1)[X]) - Y_w^(1)[L_xi X], whose last term has
       zero forward part.
Checks: exact rationals, off-shell (w != k), random amplitudes, 4 draws; symbolic weight w in [L1].
Subtraction: none.
Run: OMP_NUM_THREADS=2 python3 r196_lemmaL.py
"""
import sympy as sp, random, time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r196_lib import C, S, eps, eta, N, make_D, avg, einstein_lower, einstein_upper_density, order

t0 = time.time()
W = sp.Symbol('w')          # density weight (symbolic in [L1])
rng = random.Random(19606)


def rq(lo=-5, hi=5):
    v = 0
    while v == 0:
        v = sp.Rational(rng.randint(lo, hi), rng.randint(1, 4))
    return v


def conserved_mode(om, k):
    """random flat-conserved symmetric amplitude: Y^{3 nu} = (om/k) Y^{0 nu} (channel structure of R15-2)."""
    x = om / k
    Y = sp.zeros(4, 4)
    Y[0, 0] = rq(); Y[0, 1] = Y[1, 0] = rq(); Y[0, 2] = Y[2, 0] = rq()
    Y[0, 3] = Y[3, 0] = x * Y[0, 0]; Y[1, 3] = Y[3, 1] = x * Y[0, 1]; Y[2, 3] = Y[3, 2] = x * Y[0, 2]
    Y[3, 3] = x**2 * Y[0, 0]; Y[1, 1] = rq(); Y[2, 2] = rq(); Y[1, 2] = Y[2, 1] = rq()
    return Y


def lie_density(Yf, xi, w, D):
    """(L_xi Y)^{mu nu} for a contravariant weight-w density; Yf, xi are expressions in C, S."""
    div = sum(D(l, xi[l]) for l in range(N))
    out = sp.zeros(4, 4)
    for m in range(N):
        for n in range(N):
            v = sum(xi[l] * D(l, Yf[m, n]) for l in range(N))
            v -= sum(Yf[l, n] * D(l, xi[m]) for l in range(N))
            v -= sum(Yf[m, l] * D(l, xi[n]) for l in range(N))
            v += w * div * Yf[m, n]
            out[m, n] = sp.expand(v)
    return out, div


print("[L1] Lemma L on a generic flat-conserved density mode (this is instance (i): the record mode J, all six of")
print("     R15-2's channel variables rho, T_perp, j_x, j_y, t_+, t_x), symbolic weight w, off-shell, 4 random draws")
for draw in range(4):
    om, k = rq(1, 9), rq(1, 9)
    while om == k:
        k = rq(1, 9)
    D = make_D(om, k)
    Y, Z = conserved_mode(om, k), conserved_mode(om, k)
    Yf = (Y * C + Z * S)
    cons = [sp.expand(sum(D(m, Yf[m, n]) for m in range(N))) for n in range(N)]
    xi = [rq() * C + rq() * S for _ in range(N)]
    L, div = lie_density(Yf, xi, W, D)
    lhs = L.applyfunc(avg)
    rhs = (Yf * div).applyfunc(lambda e: sp.expand((W - 1) * avg(e)))
    diff = (lhs - rhs).applyfunc(sp.simplify)
    nz = sum(1 for e in (Yf * div).applyfunc(avg) if e != 0)
    print("     draw %d: w/k = %s ; conserved: %s ; <L_xi Y> - (w-1)<(d.xi)Y> = 0 in %d/16 comps ; <(d.xi)Y> nonzero in %d/16 comps"
          % (draw, om / k, all(c == 0 for c in cons), sum(1 for e in diff if e == 0), nz))
print("     => <L_xi Y> vanishes for every xi iff w = 1 (generic <(d.xi)Y> != 0)  [%.1fs]" % (time.time() - t0))

print("\n[L2] instance (ii): field side.  h = L_xi eta (pure gauge, lower: d_mu xi_nu + d_nu xi_mu) and X arbitrary,")
print("     same phase (zero total momentum after averaging).  Forward cross term of Y_w^(2) = [(-g)^{w/2} G^{mu nu}]^(2),")
print("     compared with Lemma L applied to the conserved density G^(1)mu nu[X]:  (w-1)<(d.xi) G^(1)[X]>")
for draw in range(2):
    om, k = rq(1, 9), rq(1, 9)
    while om == k:
        k = rq(1, 9)
    D = make_D(om, k)
    xiu = [rq() * C + rq() * S for _ in range(N)]
    xil = [eta[m, m] * xiu[m] for m in range(N)]
    hA = sp.zeros(4, 4)
    for m in range(N):
        for n in range(N):
            hA[m, n] = sp.expand(D(m, xil[n]) + D(n, xil[m]))
    Xc, Xs = sp.zeros(4, 4), sp.zeros(4, 4)
    for m in range(N):
        for n in range(m, N):
            Xc[m, n] = Xc[n, m] = rq(); Xs[m, n] = Xs[n, m] = rq()
    hB = Xc * C + Xs * S
    res = {}
    GB, giB = einstein_lower(hB, D)
    G1B_up = (eta * GB.applyfunc(lambda e: order(e, 1)) * eta)
    cons = [sp.expand(sum(D(m, G1B_up[m, n]) for m in range(N))) for n in range(N)]
    for wv in (0, 1, 2):
        Ys = {}
        for lab, hh in (("A", hA), ("B", hB), ("AB", hA + hB)):
            G, gi = einstein_lower(hh, D)
            Yd = einstein_upper_density(G, gi, hh, wv)
            Ys[lab] = Yd.applyfunc(lambda e: avg(order(e, 2)))
        cross = (Ys["AB"] - Ys["A"] - Ys["B"]).applyfunc(sp.expand)
        L, div = lie_density(G1B_up, xiu, wv, D)
        lieavg = L.applyfunc(avg)
        pred = (G1B_up * div).applyfunc(lambda e: (wv - 1) * avg(e))
        res[wv] = (sum(1 for e in cross if e != 0), all(sp.expand(a - b) == 0 for a, b in zip(cross, lieavg)),
                   all(sp.expand(a - b) == 0 for a, b in zip(lieavg, pred)))
    # lower-index weight-0 G_mu nu (R19-3's (B) form)
    Gs = {}
    for lab, hh in (("A", hA), ("B", hB), ("AB", hA + hB)):
        G, gi = einstein_lower(hh, D)
        Gs[lab] = G.applyfunc(lambda e: avg(order(e, 2)))
    crossL = (Gs["AB"] - Gs["A"] - Gs["B"]).applyfunc(sp.expand)
    print("     draw %d (w/k = %s): G^(1)[X] conserved: %s" % (draw, om / k, all(c == 0 for c in cons)))
    for wv in (0, 1, 2):
        nzc, eq_lie, eq_pred = res[wv]
        print("       weight %d: gauge-X cross term nonzero in %2d/16 comps ; equals <L_xi G^(1)[X]>: %s ; equals (w-1)<(d.xi)G^(1)[X]>: %s"
              % (wv, nzc, eq_lie, eq_pred))
    print("       lower G_mu nu (weight 0): gauge-X cross term nonzero in %d/16 comps" % sum(1 for e in crossL if e != 0))
    print("       [%.1fs]" % (time.time() - t0))
print("\n[L3] conclusion: Theorem G (records) and Lemma D (field) are the same identity, Lemma L, applied to the two")
print("     conserved objects that enter the one-point source: the recorded stress and the linearized Einstein tensor.")
print("total time %.1fs" % (time.time() - t0))
