#!/usr/bin/env python3
"""C4b_check part C/F: the h-linear fermion relabelling G_f^(1) CONSTRUCTED (not fitted) from the symmetric-gauge
(Bourguignon-Gauduchon) lift: drag the symmetric frame E(h) = (delta + a h)^(-1/2) by L_xi, rotate it back to
symmetric gauge by omega, and lift omega to the spinor.  Then:
  C1'  {G, G} at order chi chi closes with this G_f^(1) (lam_f = nu);   C1'' lam_f in {0, nu} on the line beta x BG;
  C2'  without G_f^(1) the remainder is the spin-1/2 note's on-site rotation (1/2) int eps_kij (S_xi S_eta)_ij s_k;
  F'   {C, G} at order h chi chi: walker + 1/4 N T n closes with the BG G_f^(1); the bare walker does not, and
       (F1'') does not even with an arbitrary own-basis isotropic h-linear correction to G_f^(1).
Usage: python3 chk_C.py [C] [F] [F1]
"""
import sys, itertools
from vc_core import *

SEC = sys.argv[1:] or ["C", "F", "F1"]
nb = d[0] * c[0] + d[1] * c[1]
lb = [sp.expand(sum(xi[k] * D(eta[i], k) - eta[k] * D(xi[i], k) for k in R3)) for i in R3]
HALF, QTR = sp.Rational(1, 2), sp.Rational(1, 4)


def has_chi(t_):
    return any(t_.has(f) for f in c + d)


def chi_filter(e):
    return sp.expand(sum(t_ for t_ in sp.Add.make_args(sp.expand(e)) if has_chi(t_)))


def Asym(Xm):
    return (Xm - Xm.T) / 2


def G_f1_BG(vec, a, nu_):
    """h-linear part of the symmetric-gauge spinor lift (times nu_), as a functional int chibar i Lambda1 chi.
    Frame E = 1 - a h/2 + O(h^2); L_xi E_a^j = xi.dE_a^j - E_a^k d_k xi^j; omega with omega E + L_xi E symmetric;
    spinor rotation dchi = (i/2) theta.sigma chi, omega_ab = eps_abk theta_k (fixed by the walker's global rotation
    covariance, chk_G G1 at uniform theta)."""
    dxi = sp.Matrix(3, 3, lambda a_, j: D(vec[j], a_))      # [a, j] = d_a xi_j
    om0 = Asym(dxi)                                           # zeroth order: omega0 - dxi symmetric
    hA = a * Hm
    LE1 = sp.Matrix(3, 3, lambda a_, j: -sum(vec[k] * D(hA[a_, j], k) for k in R3) / 2
                    + sum(hA[a_, k] * D(vec[j], k) for k in R3) / 2)      # O(h) part of L_xi E
    om1 = -Asym(-om0 * hA / 2 + LE1)
    th1 = [sp.expand(sum(EPS(k, a_, b) * om1[a_, b] for a_ in R3 for b in R3) / 2) for k in R3]
    # int chibar i (i/2) th1.sigma chi = -1/2 int th1.s
    return sp.expand(-nu_ * HALF * sum(th1[k] * bil(SIG[k]) for k in R3)), th1


def Gtot(vec, lam1, nu_, a, lam_f, beta=1, with_f1=True):
    G = Pdot(lam1 * LieDelta(vec) + nu_ * LieH(vec)) + kosmann(vec, lam_f, HALF, QTR)
    if with_f1:
        G += beta * G_f1_BG(vec, a, nu_)[0]
    return sp.expand(G)


if "C" in SEC:
    # th0 check: zeroth-order rotation reproduces the Kosmann spin term (1/2 curl xi)
    lf, bt = sp.symbols("lam_f beta", real=True)
    G1x, G1e = G_f1_BG(xi, 1, 1)[0], G_f1_BG(eta, 1, 1)[0]
    Gx = Pdot(LieDelta(xi) + LieH(xi))
    Ge = Pdot(LieDelta(eta) + LieH(eta))
    Kx, Ke = kosmann(xi, 1, HALF, QTR), kosmann(eta, 1, HALF, QTR)
    KK = chi_filter(hdeg_filter(pb(Kx, Ke), 0))
    X1 = chi_filter(hdeg_filter(pb(Gx, G1e) + pb(G1x, Ge), 0))
    KL = kosmann(lb, 1, HALF, QTR)
    # orientation: chk_B G2 found {G[xi], G[eta]} = + G[[xi, eta]] with [xi, eta] = lb
    r_full = sp.expand(KK + X1 - KL)
    ok1 = div_eqs(r_full, xi[0]) == []
    check("C1'", ok1, "{G[xi], G[eta]} at order chi chi with lam1 = nu = lam_f = 1 and the CONSTRUCTED symmetric-gauge "
          "G_f^(1): = Kosmann[[xi, eta]] exactly (mod divergence): the metric route closes {G,G} with no triad")
    # C1'': lam_f free, G_f^(1) scaled by beta
    r_lb = sp.expand(lf ** 2 * KK + bt * X1 - lf * KL)
    sl = vsolve(div_eqs(r_lb, xi[0]), [lf, bt])
    check("C1''", sorted([tuple(sorted(s_.items(), key=str)) for s_ in sl]) ==
          sorted([((bt, 0), (lf, 0)), ((bt, 1), (lf, 1))]),
          f"lam_f free, G_f^(1) = beta x BG: closure iff (lam_f, beta) in {{(0, 0), (nu, nu^2)}}  (nu = 1): {sl}")
    # C2': product bracket remainder vs the spin-1/2 note's on-site rotation
    Sx = [[(D(xi[i], j) + D(xi[j], i)) / 2 for j in R3] for i in R3]
    Se = [[(D(eta[i], j) + D(eta[j], i)) / 2 for j in R3] for i in R3]
    rot = sp.expand(sum(EPS(k, i, j) * sum(Sx[i][l] * Se[l][j] for l in R3) * bil(SIG[k])
                        for k in R3 for i in R3 for j in R3 if EPS(k, i, j) != 0))
    cc = sp.Symbol("cc", real=True)
    sc = vsolve(div_eqs(sp.expand(KK - KL - cc * rot), xi[0]), [cc])
    check("C2'", sc == [{cc: HALF}], f"without G_f^(1): {{K[xi],K[eta]}} - K[[xi,eta]] = cc int eps_kij (S_xi S_eta)_ij s_k, "
          f"cc = {sc} (spin-1/2 note Result 4 / N2 form); and {{G1, G_f^(1)}} terms cancel it exactly (C1')")

if "F" in SEC or "F1" in SEC:

    def Tax(E, order):
        Ei = inv_series(E, order)
        e_ = Ei.T
        return sp.expand(sum(EPS(a_, b, cc_) * E[a_, j] * E[b, k] * D(e_[cc_, k], j)
                             for a_ in R3 for b in R3 for cc_ in R3 if EPS(a_, b, cc_) != 0 for j in R3 for k in R3))

    def F_res(lam1, nu_, a, cov, extra=0):
        E2 = frame_sym(a, 2)
        Cf = walker(N, E2)
        if cov:
            Cf += QTR * N * hdeg_filter(Tax(E2, 2), 2) * nb
        Cf = sp.expand(sum(hdeg_filter(Cf, k) for k in (0, 1, 2)))
        G = Gtot(xi, lam1, nu_, a, nu_) + extra
        lhs = hdeg_filter(pb(Cf, G), 1)
        Npr = -nu_ * sum(xi[k] * D(N, k) for k in R3)
        rhs = hdeg_filter(walker(Npr, frame_sym(a, 1)), 1)
        return div_eqs(sp.expand(lhs - rhs), N)

if "F" in SEC:
    one, two = sp.Integer(1), sp.Integer(2)
    out = {}
    for tag, (l1, n_, a_, cov) in {"cov r=1": (one, one, one, True), "cov r=2": (two, one, HALF, True),
                                   "bare r=1": (one, one, one, False), "bare r=2": (two, one, HALF, False)}.items():
        e_ = F_res(l1, n_, a_, cov)
        out[tag] = (len(e_) == 0)
        print(f"   F {tag}: residual equations {len(e_)}", flush=True)
    check("F2'", out["cov r=1"] and out["cov r=2"], f"{{C,G}} at order h chi chi: walker + 1/4 N T n with the constructed "
          f"symmetric-gauge G_f^(1) closes at r = 1 and r = 2 (a = 1/r) with NO free parameter: {out}")
    check("F1'", (not out["bare r=1"]) and (not out["bare r=2"]), f"bare walker with the same G_f^(1): fails at r = 1, 2: {out}")

if "F1" in SEC:
    # own isotropic basis for an h-linear correction dG to G_f^(1) (one derivative in total, as in C4b's families)
    nfun = lambda idx: nb
    sfun = lambda idx: bil(SIG[idx[0]])
    def J(j, mu_mat):
        return sp.expand(I / 2 * sum(mu_mat[a_, b] * (d[a_] * D(c[b], j) - D(d[a_], j) * c[b]) for a_ in range(2) for b in range(2)))
    fams = [
        [("h", 2), ("dx", 2), ("n", 0)], [("h", 2), ("dx", 2), ("s", 1)], [("dh", 3), ("x", 1), ("n", 0)],
        [("dh", 3), ("x", 1), ("s", 1)], [("h", 2), ("x", 1), ("J0", 1)], [("h", 2), ("x", 1), ("Js", 2)],
        [("h", 2), ("x", 1), ("s", 1)], [("h", 2), ("x", 1), ("n", 0)]]
    def val(kind, idx):
        if kind == "h":
            return hf(idx[0], idx[1])
        if kind == "dh":
            return D(hf(idx[1], idx[2]), idx[0])
        if kind == "dx":
            return D(xi[idx[1]], idx[0])
        if kind == "x":
            return xi[idx[0]]
        if kind == "n":
            return nb
        if kind == "s":
            return bil(SIG[idx[0]])
        if kind == "J0":
            return J(idx[0], sp.eye(2))
        if kind == "Js":
            return J(idx[0], SIG[idx[1]])
    def pairings(sl):
        if not sl:
            yield []
            return
        a0 = sl[0]
        for i in range(1, len(sl)):
            for p in pairings(sl[1:i] + sl[i + 1:]):
                yield [(a0, sl[i])] + p
    cands = []
    for fam in fams:
        n_ = sum(k for _, k in fam)
        slots = list(range(n_))
        structs = [(None, p) for p in pairings(slots)] if n_ % 2 == 0 else \
            [(tri, p) for tri in itertools.combinations(slots, 3) for p in pairings([s for s in slots if s not in tri])]
        for tri, p in structs:
            tot = 0
            for ve in (itertools.permutations(R3) if tri else [()]):
                for vd in itertools.product(R3, repeat=len(p)):
                    v_ = [None] * n_
                    sg = 1
                    if tri:
                        sg = EPS(*ve)
                        for s_, x_ in zip(tri, ve):
                            v_[s_] = x_
                    for (p1, p2), x_ in zip(p, vd):
                        v_[p1] = v_[p2] = x_
                    term, pos = sg, 0
                    for kind, k in fam:
                        term *= val(kind, tuple(v_[pos:pos + k]))
                        pos += k
                    tot += term
            tot = sp.expand(tot)
            if tot != 0:
                cands.append(tot)
    print(f"   own isotropic h-linear relabelling candidates: {len(cands)}", flush=True)
    gs = sp.symbols(f"g0:{len(cands)}", real=True)
    # linear in dG: only the flat walker brackets with an h-linear, P-free dG at order h chi chi
    C0 = walker(N, sp.eye(3))
    cols = [euler(hdeg_filter(pb(C0, c_, grav=False), 1), N) for c_ in cands]
    print("   per-candidate brackets done", flush=True)
    res = {}
    for tag, (l1, n_, a_, cov) in {"bare r=1": (1, 1, 1, False), "cov r=1": (1, 1, 1, True)}.items():
        Cf = walker(N, frame_sym(sp.Integer(a_), 2))
        if cov:
            Cf += QTR * N * hdeg_filter(Tax(frame_sym(sp.Integer(a_), 2), 2), 2) * nb
        G = Gtot(xi, sp.Integer(l1), sp.Integer(n_), sp.Integer(a_), sp.Integer(n_))
        lhs = hdeg_filter(pb(Cf, G), 1)
        rhs = hdeg_filter(walker(-sp.Integer(n_) * sum(xi[k] * D(N, k) for k in R3), frame_sym(sp.Integer(a_), 1)), 1)
        e_ = coeff_eqs(sp.expand(euler(sp.expand(lhs - rhs), N) + sum(g_ * col for g_, col in zip(gs, cols))))
        A_, b_ = sp.linear_eq_to_matrix(e_, gs)
        rk, rka = A_.rank(), A_.row_join(b_).rank()
        res[tag] = (rk, rka)
        print(f"   F1'' {tag}: {len(e_)} equations, rank {rk}, augmented rank {rka}", flush=True)
    check("F1''", res["bare r=1"][0] < res["bare r=1"][1] and res["cov r=1"][0] == res["cov r=1"][1],
          f"bare walker: NO correction dG in the full own isotropic h-linear basis ({len(cands)} terms, not constrained "
          f"by {{G,G}}) closes {{C,G}} at h chi chi (inconsistent system); covariant: consistent: {res}")
total()
