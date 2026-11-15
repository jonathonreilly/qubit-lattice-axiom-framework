"""c29: session-14 instances. Criteria: checks/c29_criteria.md (written before this script).

A: fine sources as effective coarse data (Lemma SRC-id, linear chain, c26 machinery).
B: sector bounds of Lemma EXP-strip' at complex points (c28 building blocks).
C: SU(2) d = 4 soft-step contraction instance (c22 model, coarse side NC = 3 and 4).
D: covariant Faddeev-Popov identities at an SU(2) critical background (Proposition NA-FP).
Usage: python3 -I c29_su2_contraction.py A | B | C | D | smoke
"""
import itertools
import math
import os
import resource
import sys
import time

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import lsmr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c26_led as C26  # noqa: E402
import c28_exp as C28  # noqa: E402
from c22_soft_su2_4d import qmul, qconj, qexp, qlog, Ad  # noqa: E402

T0 = time.time()
L = 3
d = 4


def rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 30


# ====================================================================== Part A
def fine_hodge_inverse(j, d_, Nf):
    """componentwise inverse of the flat Hodge Laplacian on a fine 1-form (zero mode removed)."""
    out = np.zeros_like(j)
    q = 2 * np.pi * np.arange(Nf) / Nf
    lam = sum(np.meshgrid(*([4 * np.sin(q / 2) ** 2] * d_), indexing="ij"))
    lam0 = lam.copy(); lam0[(0,) * d_] = 1.0
    N = Nf ** d_
    for mu in range(d_):
        jh = np.fft.fftn(j[mu * N:(mu + 1) * N].reshape((Nf,) * d_))
        jh[(0,) * d_] = 0.0
        out[mu * N:(mu + 1) * N] = np.fft.ifftn(jh / lam0).real.reshape(-1)
    return out


def chain_solve_target(ch, Bk, omega):
    """LSMR for 1/2||D0 B0 - omega||^2 + sum kappa/2 ||Q B_i - B_{i+1}||^2: the critical point of E - <d*omega, B0>."""
    k = ch.k
    b = np.zeros(ch.M.shape[0])
    nf = ch.D0.shape[0]
    b[:nf] = omega
    b[-ch.levels[k].NL:] = np.sqrt(ch.kap[-1]) * Bk
    x = lsmr(ch.M, b, atol=1e-15, btol=1e-15, maxiter=400000)[0]
    ne = np.linalg.norm(ch.M.T @ (ch.M @ x - b)) / max(np.linalg.norm(ch.M.T @ b), 1e-300)
    Bs = [x[ch.off[i]:ch.off[i + 1]] for i in range(k)]
    r = [ch.Q[i] @ Bs[i] - (Bs[i + 1] if i + 1 < k else Bk) for i in range(k)]
    return dict(B=Bs, r=r, ne=ne)


def part_A():
    rng = np.random.default_rng(20261027)
    ok = dict(V1=True, A1=True, A2=True, A3=True)
    cases = [(4, 3, 1, (1.0,)), (4, 2, 2, (1.0, 1.0)), (2, 5, 2, (1.0, 1.0)), (2, 5, 3, (0.5, 2.0, 1.0))]
    for (d_, T, k, kap) in cases:
        tt = time.time()
        ch = C26.Chain(d_, T, k, kap)
        lv0 = ch.levels[0]; top = ch.levels[k]; Nf = lv0.n
        omega = rng.normal(size=ch.D0.shape[0])
        j = ch.D0.T @ omega                                   # j = d* omega: co-closed, zero mean
        Bk = rng.normal(size=top.NL)
        s1 = chain_solve_target(ch, Bk, omega)
        g = fine_hodge_inverse(j, d_, Nf)
        for i in range(k):
            g = ch.Q[i] @ g
        s2 = ch.solve(Bk - g)                                  # no source, effective data
        r1 = s1["r"][k - 1]; r2 = s2["r"][k - 1]
        a1 = np.max(np.abs(r1 - r2)) / np.max(np.abs(r1))
        J0 = j - kap[0] * (ch.Q[0].T @ s1["r"][0])
        f_pred = ch.D0 @ fine_hodge_inverse(J0, d_, Nf)
        f_true = ch.D0 @ s1["B"][0]
        a2f = np.max(np.abs(f_pred - f_true)) / np.max(np.abs(f_true))
        rr = r1.copy()
        for i in range(k - 1, 0, -1):
            rr = (kap[i] / kap[i - 1]) * (ch.Q[i].T @ rr)
        a2r = np.max(np.abs(rr - s1["r"][0])) / np.max(np.abs(s1["r"][0]))
        ok["V1"] &= s1["ne"] <= 1e-8 and s2["ne"] <= 1e-8
        ok["A1"] &= a1 <= 1e-6
        ok["A2"] &= max(a2f, a2r) <= 1e-6
        print(f"A d={d_} T={T} k={k} kap={kap}: ne {s1['ne']:.1e}/{s2['ne']:.1e}  A1 {a1:.2e}  A2 f {a2f:.2e} r0 {a2r:.2e}"
              f"  ({time.time() - tt:.0f} s, RSS {rss():.2f} GB)", flush=True)
    # A3: the algebraic identity, analytic blocks at complex points
    worst = 0.0
    for k in (1, 2, 3):
        n = L ** k; kap = (1.0,) * k
        npts = 200 if k < 3 else 60
        for _ in range(npts):
            z = rng.uniform(-np.pi, np.pi, d) + 1j * rng.uniform(-0.05, 0.05, d)
            B = C28.blocks(z, n, k, kap)
            jh = rng.normal(size=d) + 1j * rng.normal(size=d)
            Dn = np.array([C28.Dn_c(z[a], n) for a in range(d)])
            Dbar = np.array([np.exp(1j * z[a] * np.arange(n) / n).sum() / n for a in range(d)])
            PiDbar = np.prod(Dbar)
            Wbar = PiDbar * Dbar
            nub = np.exp(-1j * z) - 1
            nubn = n * (np.exp(-1j * z / n) - 1)
            lhs = B["a"] * np.sum(nub * Wbar * jh / B["beta"])
            rhs = PiDbar * (np.sum(nubn * jh) - B["phi"] * np.sum(nubn * B["R"] * jh / B["beta"]))
            worst = max(worst, abs(lhs - rhs) / max(abs(lhs), abs(rhs), 1e-300))
            _ = Dn
    ok["A3"] = worst <= 1e-10
    print(f"A3 identity: max relative error {worst:.2e}")
    # informational: K = 0 composite symbol vs its 1/phi input along p = (s, 0, 0, 0)
    n = 9; k = 2; kap = (1.0, 1.0)
    print("A info (n = 9, k = 2, kappa = 1, j-hat = e_1 + e_2): s, |g0| = |Wbar_1 j_1/phi|, |r0| (SRC-id K=0 formula)")
    for s in (0.4, 0.1, 0.03, 0.01):
        z = np.array([s, 0.0, 0.0, 0.0], dtype=complex)
        B = C28.blocks(z, n, k, kap)
        Dbar = np.array([np.exp(1j * z[a] * np.arange(n) / n).sum() / n for a in range(d)])
        PiDbar = np.prod(Dbar); Wbar = PiDbar * Dbar
        nu = np.exp(1j * z) - 1; nubn = n * (np.exp(-1j * z / n) - 1)
        jh = np.array([1.0, 1.0, 0, 0], dtype=complex)
        S = np.sum(nubn * B["R"] * jh / B["beta"])
        r0 = Wbar * jh / B["beta"] + nu * PiDbar * S / (B["beta"] * B["Psi"])
        print(f"   s={s}: |g0|={abs(Wbar[0] * jh[0] / B['phi']):.3e}  |r0|={np.max(np.abs(r0)):.3e}")
    for kk, v in ok.items():
        print(f"{kk}: {'PASS' if v else 'FAIL'}")
    print(f"c29 A: {'PASS' if all(ok.values()) else 'FAIL'}; time {time.time() - T0:.0f} s, peak RSS {rss():.2f} GB")


# ====================================================================== Part B (Lemma EXP-strip' arithmetic, verbatim)
def strip2_consts(eta, r0, kap, kh, L=3):
    ce = math.cosh(eta) - 1; se = math.sinh(eta)
    cphi = 18 * (math.cosh(eta / 3) - 1); sphi = 6 * math.sinh(eta / 3)
    Rb = 1 + kh / (L * L - 1) + kap / 9
    bstar = min(kap, 24 / math.pi ** 2); Gam = max(math.pi ** 2 / 4, Rb)
    ch = math.cosh(eta); eps = math.exp(eta) - 1
    lam = 1 - 4 * eta ** 2 * ch ** 2 / 9
    eZ = (4 * eta ** 2 / 9 + 4 * eta / 3) * ch
    dN = eps * math.exp(4 * eta) + 4 * math.exp(3 * eta) * eps * (1 + math.exp(eta))
    cZ = dN / (9 * lam) + eZ / (9 * lam)
    a1 = (math.pi ** 2 / 4) * ce; g1 = math.pi ** 2 / 12
    th1 = math.atan(se * g1 / (1 - a1)); tha = 5 * th1
    mm = (1 - a1) ** 5; mp = ((1 + a1) ** 2 + (se * g1) ** 2) ** 2.5
    eRR = kh * ce / (L * L - 1) + kap * cZ; eRI = kh * se / (L * L - 1) + kap * cZ
    rhoR = 1 - mm * math.cos(tha) + eRR + 4 * cphi * (Rb + eRR) / bstar + 2 * sphi * eRI / math.sqrt(bstar)
    rhoRp = (mp - 1) + eRR + 2 * sphi * eRI / math.sqrt(bstar)
    rhoI = mp * math.sin(tha) + eRI * (1 + 4 * cphi / bstar) + 2 * sphi * (Rb + eRR) / math.sqrt(bstar)
    PsiL = 1 - (r0 ** 2 + 4 * cphi + 2 * sphi * r0) * (Rb + eRR + eRI) / ((1 - rhoR) * bstar)
    psi0 = 4 * r0 ** 2 / math.pi ** 2
    D2 = (1 + rhoRp) ** 2 + rhoI ** 2
    brV = (1 - rhoR) / (D2 * Gam) - (8 * ce * (1 + rhoRp) / psi0 + 4 * se * rhoI / math.sqrt(psi0)) / (1 - rhoR) ** 2
    ok = (eta <= 0.1 and lam > 0 and tha <= math.pi / 2 and eRR < 1 and rhoR <= 0.5 and PsiL >= 0.1
          and brV >= 0.25 * (1 - rhoR) / (D2 * Gam) and 4 * cphi <= 0.5 * psi0)
    return ok, dict(ce=ce, se=se, cphi=cphi, sphi=sphi, Rb=Rb, bstar=bstar, Gam=Gam, cZ=cZ, tha=tha, mm=mm, mp=mp,
                    eRR=eRR, eRI=eRI, rhoR=rhoR, rhoRp=rhoRp, rhoI=rhoI, PsiL=PsiL, psi0=psi0, D2=D2, brV=brV)


def strip2_eta(kap, kh, L=3):
    best = (0.0, None)
    for i in range(150):
        r0 = 0.05 + 0.01 * i
        lo, hi = 0.0, 0.1
        if not strip2_consts(1e-6, r0, kap, kh, L)[0]:
            continue
        for _ in range(50):
            mid = (lo + hi) / 2
            if strip2_consts(mid, r0, kap, kh, L)[0]:
                lo = mid
            else:
                hi = mid
        if lo > best[0]:
            best = (lo, r0)
    return best


def part_B():
    rng = np.random.default_rng(20261028)
    allok = True
    configs = [(1.0, 1.0, (1, 2, 3)), (0.25, 1.0, (1, 2, 3)), (4.0, 1.0, (1, 2, 3)), (1.0, 16.0, (2,))]
    for (kapv, kh, ks) in configs:
        eta, r0 = strip2_eta(kapv, kh)
        _, K = strip2_consts(eta, r0, kapv, kh)
        for k in ks:
            n = L ** k
            kap = (kapv,) * k if kh == 1.0 else (kapv / 16.0, kapv)
            nx = 120 if k < 3 else 40
            xs = [rng.uniform(-np.pi, np.pi, d) for _ in range(nx)]
            xs += [np.zeros(d), np.full(d, np.pi), np.array([np.pi, 0, 0, 0]), np.array([r0, 0, 0, 0]),
                   np.array([r0, r0, 0, 0]) / math.sqrt(2)]
            w = dict(B1=0.0, B2=0.0, B3=0.0, B4=0.0, B5=0.0, B6n=np.inf, B6f=np.inf, B6p=np.inf)
            for x in xs:
                Bx = C28.blocks(x.astype(complex), n, k, kap)
                bx = Bx["beta"].real; dx = Bx["dl"].real; px = Bx["ph"].real; Dx = Bx["De"].real
                adx = Bx["a"].real * dx
                rx = np.linalg.norm(x)
                tx = np.minimum(1 / 3, np.abs(x) / 6)
                ys = [rng.uniform(-eta, eta, d) for _ in range(2)] + [eta * rng.choice([-1, 1], d) for _ in range(2)]
                for y in ys:
                    Bz = C28.blocks(x + 1j * y, n, k, kap)
                    dz = Bz["dl"]; pz = Bz["ph"]; Dz = Bz["De"]
                    b1 = max(np.max(np.abs(dz.real - dx)) / K["ce"],
                             np.max(np.abs(dz.imag) / np.maximum(K["se"] * tx, 1e-300) * (np.abs(dz.imag) > 1e-15)))
                    b2 = max(np.max(pz.real - px - 1e-12 * (1 + px)) / 1e-300 if np.any(pz.real - px > 1e-12 * (1 + px)) else 0.0,
                             np.max(np.maximum(px - pz.real, 0.0)) / K["cphi"],
                             np.max(np.abs(pz.imag) / np.maximum(K["sphi"] * np.sqrt(px), 1e-300) * (np.abs(pz.imag) > 1e-15)),
                             np.max(np.abs(Dz.real - Dx)) / (2 * K["ce"]),
                             np.max(np.abs(Dz.imag) / np.maximum(2 * K["se"] * np.sqrt(Dx), 1e-300) * (np.abs(Dz.imag) > 1e-15)))
                    adz = Bz["a"] * dz
                    ratio = adz / adx
                    b3 = max(np.max(np.abs(np.angle(ratio))) / K["tha"], np.max(np.abs(ratio)) / K["mp"],
                             K["mm"] / np.min(np.abs(ratio)))
                    b4 = max(np.max(np.abs(Bz["R"].real - Bx["R"].real)) / K["eRR"],
                             np.max(np.abs(Bz["R"].imag)) / K["eRI"])
                    bz = Bz["beta"]
                    b5 = max(np.max((1 - K["rhoR"]) * bx / bz.real), np.max(bz.real / ((1 + K["rhoRp"]) * bx)),
                             np.max(np.abs(bz.imag) / (K["rhoI"] * bx)))
                    for key, val in (("B1", b1), ("B2", b2), ("B3", b3), ("B4", b4), ("B5", b5)):
                        w[key] = max(w[key], val)
                    if rx <= r0 + 1e-12:
                        w["B6n"] = min(w["B6n"], abs(Bz["Psi"]) / K["PsiL"])
                    if rx >= r0 - 1e-12:
                        psi = Dx.sum()
                        w["B6f"] = min(w["B6f"], Bz["Sig"].real / (psi / np.min(bx) * K["brV"]))
                        w["B6p"] = min(w["B6p"], Bz["phi"].real / (K["psi0"] / 2))
            ok = all(w[kk] <= 1 for kk in ("B1", "B2", "B3", "B4", "B5")) and all(
                w[kk] >= 1 for kk in ("B6n", "B6f", "B6p"))
            allok &= ok
            print(f"B kap={kapv} khat={kh} k={k} (n={n}) eta'*={eta:.4f} r0={r0:.2f}: "
                  + " ".join(f"{kk} {v:.3f}" for kk, v in w.items()) + f" {'PASS' if ok else 'FAIL'}", flush=True)
    print(f"c29 B: {'PASS' if allok else 'FAIL'}; time {time.time() - T0:.0f} s, peak RSS {rss():.2f} GB")


# ====================================================================== SU(2) model (c22, parametrised by NC)
ORDERS = list(itertools.permutations(range(d)))
OFFS = list(itertools.product((-1, 0, 1), repeat=d))


class Geo:
    def __init__(self, NC):
        self.NC = NC; self.NF = L * NC; self.NS = self.NF ** d; self.NL = d * self.NS
        self.COARSE = list(itertools.product(range(NC), repeat=d))
        self.xid = {X: i for i, X in enumerate(self.COARSE)}
        self.CLINKS = [(X, mu) for mu in range(d) for X in self.COARSE]
        self.NCL = len(self.CLINKS)
        self.NPER = len(ORDERS) * len(OFFS)

    def sidx(self, x):
        NF = self.NF
        x = [c % NF for c in x]
        return ((x[0] * NF + x[1]) * NF + x[2]) * NF + x[3]

    def lidx(self, x, mu):
        return mu * self.NS + self.sidx(x)

    def path(self, a, b, order):
        out = []; z = list(a)
        for c in order:
            while z[c] != b[c]:
                if b[c] > z[c]:
                    out.append((self.lidx(z, c), 1)); z[c] += 1
                else:
                    w = list(z); w[c] -= 1
                    out.append((self.lidx(w, c), -1)); z[c] -= 1
        return out

    def root(self, X):
        return tuple(L * X[i] + 1 for i in range(d))


def factors(U, lk, sg):
    Ue = np.concatenate([U, np.array([[1.0, 0, 0, 0]])], axis=0)
    F = Ue[lk]
    neg = sg < 0
    F[neg] = qconj(F[neg])
    return F


def products(F):
    n = F.shape[1]
    P = np.empty((F.shape[0], n + 1, 4))
    P[:, 0] = [1.0, 0, 0, 0]
    for m in range(n):
        P[:, m + 1] = qmul(P[:, m], F[:, m])
    return P


class SU2Model:
    """c22's FastModel energy and gradient, coarse side NC (no full contour table is built)."""

    def __init__(self, NC, kappa=1.0):
        t = time.time()
        g = self.g = Geo(NC); self.kappa = kappa
        NF, NS, NL = g.NF, g.NS, g.NL
        n = NS * 6
        plk = np.zeros((n, 4), dtype=np.int64); psg = np.ones((n, 4), dtype=np.int8)
        k = 0
        for x in itertools.product(range(NF), repeat=d):
            for (mu, nu) in itertools.combinations(range(d), 2):
                xm = list(x); xm[mu] += 1
                xn = list(x); xn[nu] += 1
                plk[k] = [g.lidx(x, mu), g.lidx(xm, nu), g.lidx(xn, mu), g.lidx(x, nu)]
                psg[k] = [1, 1, -1, -1]; k += 1
        self.plk, self.psg = plk, psg
        self.nA = len(g.COARSE) * len(ORDERS) * len(OFFS)
        alk = np.full((self.nA, d), NL, dtype=np.int64); asg = np.ones((self.nA, d), dtype=np.int8)
        aend = np.zeros(self.nA, dtype=np.int64); aroot = np.zeros(self.nA, dtype=np.int64)
        k = 0
        for X in g.COARSE:
            c = g.root(X)
            for sig in ORDERS:
                for off in OFFS:
                    y = [c[i] + off[i] for i in range(d)]
                    for m, (l_, s_) in enumerate(g.path(c, y, sig)):
                        alk[k, m] = l_; asg[k, m] = s_
                    aend[k] = g.sidx(y); aroot[k] = g.sidx(c)
                    k += 1
        self.alk, self.asg, self.aend, self.aroot = alk, asg, aend, aroot
        slk = np.zeros((NS * d, L), dtype=np.int64); ssg = np.ones((NS * d, L), dtype=np.int8)
        for x in itertools.product(range(NF), repeat=d):
            for mu in range(d):
                for j in range(L):
                    z = list(x); z[mu] += j
                    slk[mu * NS + g.sidx(x), j] = g.lidx(z, mu)
        self.slk, self.ssg = slk, ssg
        no, nf = len(ORDERS), len(OFFS)
        iA1 = np.zeros(g.NCL * g.NPER, dtype=np.int64); iA2 = np.zeros_like(iA1); iS = np.zeros_like(iA1)
        k = 0
        for (X, mu) in g.CLINKS:
            cX = g.root(X)
            Y = list(X); Y[mu] = (Y[mu] + 1) % NC
            for si in range(no):
                for oi, off in enumerate(OFFS):
                    iA1[k] = (g.xid[X] * no + si) * nf + oi
                    iA2[k] = (g.xid[tuple(Y)] * no + si) * nf + oi
                    y = [cX[i] + off[i] for i in range(d)]
                    iS[k] = mu * NS + g.sidx(y)
                    k += 1
        self.iA1, self.iA2, self.iS = iA1, iA2, iS
        print(f"SU2Model NC={NC}: {self.nA} axial paths, {g.NCL * g.NPER} contours, {time.time() - t:.1f} s, "
              f"RSS {rss():.2f} GB", flush=True)

    def _grad_loops(self, F, P, G, lk, sg):
        NL = self.g.NL
        n = F.shape[1]
        gr = np.zeros((NL + 1, 3))
        S = np.zeros((F.shape[0], 4)); S[:, 0] = 1.0
        for m in range(n - 1, -1, -1):
            Sfrom = qmul(F[:, m], S)
            plus = qmul(qmul(qconj(P[:, m]), G), qconj(Sfrom))[:, 1:]
            minus = -qmul(qmul(qconj(P[:, m + 1]), G), qconj(S))[:, 1:]
            c = np.where((sg[:, m] > 0)[:, None], plus, minus)
            for i in range(3):
                gr[:, i] += np.bincount(lk[:, m], weights=c[:, i], minlength=NL + 1)
            S = Sfrom
        return gr[:NL]

    def _paths_backward(self, F, P, Tbar, lk, sg, Ubar):
        NL = self.g.NL
        n = F.shape[1]
        S = np.zeros((F.shape[0], 4)); S[:, 0] = 1.0
        for m in range(n - 1, -1, -1):
            fbar = qmul(qmul(qconj(P[:, m]), Tbar), qconj(S))
            neg = sg[:, m] < 0
            fbar[neg] = qconj(fbar[neg])
            for i in range(4):
                Ubar[:, i] += np.bincount(lk[:, m], weights=fbar[:, i], minlength=NL + 1)
            S = qmul(F[:, m], S)

    def evaluate(self, U, V):
        g = self.g
        F = factors(U, self.plk, self.psg)
        P = products(F)
        Tp = P[:, -1]
        EW = float(np.sum(1.0 - Tp[:, 0]))
        GW = np.zeros_like(Tp); GW[:, 0] = -1.0
        gW = self._grad_loops(F, P, GW, self.plk, self.psg)
        del F, P, Tp, GW
        FA = factors(U, self.alk, self.asg); PA = products(FA)
        FS = factors(U, self.slk, self.ssg); PS = products(FS)
        A = PA[:, -1]; Sg = PS[:, -1]
        X1 = A[self.iA1]; Y1 = Sg[self.iS]; Z1 = qconj(A[self.iA2])
        XY = qmul(X1, Y1)
        T = qmul(XY, Z1)
        Mb = T.reshape(g.NCL, g.NPER, 4).mean(axis=1)
        del T
        nM = np.linalg.norm(Mb, axis=1)
        ES = self.kappa * float(np.sum(nM - np.sum(V * Mb, axis=1)))
        Gc = self.kappa * (Mb / nM[:, None] - V) / g.NPER
        G = np.repeat(Gc, g.NPER, axis=0)
        Xbar = qmul(G, qconj(qmul(Y1, Z1)))
        Abar = np.zeros((self.nA, 4))
        for i in range(4):
            Abar[:, i] = np.bincount(self.iA1, weights=Xbar[:, i], minlength=self.nA)
        del Xbar
        Ybar = qmul(qmul(qconj(X1), G), qconj(Z1))
        Sbar = np.zeros((g.NS * d, 4))
        for i in range(4):
            Sbar[:, i] = np.bincount(self.iS, weights=Ybar[:, i], minlength=g.NS * d)
        del Ybar, X1, Y1, Z1
        A2bar = qconj(qmul(qconj(XY), G))
        del XY, G
        for i in range(4):
            Abar[:, i] += np.bincount(self.iA2, weights=A2bar[:, i], minlength=self.nA)
        del A2bar
        Ubar = np.zeros((g.NL + 1, 4))
        self._paths_backward(FA, PA, Abar, self.alk, self.asg, Ubar)
        self._paths_backward(FS, PS, Sbar, self.slk, self.ssg, Ubar)
        gS = qmul(Ubar[:g.NL], qconj(U))[:, 1:]
        return {"E": EW + ES, "EW": EW, "ES": ES, "g": gW + gS, "Mb": Mb}


def minimise(model, V, U, maxit=12000, tol=1e-9, g0=None):
    ev = model.evaluate(U, V)
    g = ev["g"]
    if g0 is None:
        g0 = np.linalg.norm(g)
    eta = 0.05; gprev = None; it = 0; eta_prev = eta
    while it < maxit:
        gn = np.linalg.norm(g)
        if gn <= tol * g0:
            return U, ev, it, g0, gn, True
        if gprev is not None:
            s = -eta_prev * gprev
            y = g - gprev
            sy = float(np.sum(s * y))
            eta = float(np.sum(s * s)) / sy if sy > 0 else 0.05
            eta = min(max(eta, 1e-3), 5.0)
        Un = qmul(qexp(-eta * g), U)
        Un /= np.linalg.norm(Un, axis=1, keepdims=True)
        evn = model.evaluate(Un, V)
        if evn["E"] > ev["E"] + 1e-3 * abs(ev["E"]) + 1e-12:
            eta *= 0.25
            Un = qmul(qexp(-eta * g), U); Un /= np.linalg.norm(Un, axis=1, keepdims=True)
            evn = model.evaluate(Un, V)
        gprev, eta_prev = g, eta
        U, ev, g = Un, evn, evn["g"]
        it += 1
    return U, ev, it, g0, np.linalg.norm(g), False


def coarse_field(geo, rng):
    Xf = np.zeros((geo.NCL, 3))
    A = rng.normal(size=(d, 3, d)) / 2; B = rng.normal(size=(d, 3, d)) / 2
    for ci, (X, mu) in enumerate(geo.CLINKS):
        for k in range(d):
            ph = 2 * np.pi * X[k] / geo.NC
            Xf[ci] += A[k, :, mu] * np.cos(ph) + B[k, :, mu] * np.sin(ph)
    return Xf


def start_config(geo, V):
    U = np.zeros((geo.NL, 4)); U[:, 0] = 1.0
    third = qexp(qlog(V) / L)
    for ci, (X, mu) in enumerate(geo.CLINKS):
        cX = geo.root(X)
        for j in range(L):
            x = list(cX); x[mu] += j
            U[geo.lidx(x, mu)] = third[ci]
    return U


def residual(V, Mb):
    return qlog(qmul(qconj(V), Mb / np.linalg.norm(Mb, axis=1, keepdims=True)))


def linear_r(NC, Bdata):
    """componentwise linear one-step chain (c26, d = 4, T = NC, k = 1, kappa = 1): coarse residual r."""
    ch = C26.Chain(4, NC, 1, (1.0,))
    out = np.zeros_like(Bdata)
    E = 0.0
    for comp in range(3):
        if np.max(np.abs(Bdata[:, comp])) == 0:
            continue
        sol = ch.solve(Bdata[:, comp])
        out[:, comp] = sol["r"][0]
        E += sol["E"]
    return out, E


def part_C():
    rng = np.random.default_rng(20261029)
    ok = {}
    # ---- C1, NC = 3
    model = SU2Model(3)
    geo = model.g
    Xc = coarse_field(geo, rng)
    rlin, Elin = linear_r(3, Xc)
    print(f"C1 linear prediction: |r_lin|_2 = {np.linalg.norm(rlin):.6e}, E_lin = {Elin:.6e}", flush=True)
    ts = (0.025, 0.05, 0.1, 0.2, 0.3)
    Dv = {}; conv = True
    for t in ts:
        V = qexp(t * Xc)
        tt = time.time()
        U, ev, it, g0, gn, cv = minimise(model, V, start_config(geo, V))
        conv &= cv
        rho = residual(V, ev["Mb"])
        Dv[t] = np.linalg.norm(rho / t - rlin) / np.linalg.norm(rlin)
        print(f"  t={t}: {'CONVERGED' if cv else 'NOT CONVERGED'} it={it} |g|/|g0|={gn / g0:.1e}  D={Dv[t]:.4e} "
              f"D/t={Dv[t] / t:.4f}  E/t^2={ev['E'] / t ** 2:.6e} (E_lin {Elin:.6e})  {time.time() - tt:.0f} s, "
              f"RSS {rss():.2f} GB", flush=True)
    lt = np.log(np.array(ts)); lD = np.log(np.array([Dv[t] for t in ts]))
    p = float(np.polyfit(lt, lD, 1)[0])
    ok["C-V2"] = Dv[0.025] <= 0.05
    ok["C1"] = p >= 0.8 and Dv[0.1] <= 0.1
    print(f"C1: slope p = {p:.3f}; D(0.1) = {Dv[0.1]:.4f} -> {'PASS' if ok['C1'] else 'FAIL'}; "
          f"C-V2 D(0.025) = {Dv[0.025]:.4f} -> {'PASS' if ok['C-V2'] else 'FAIL'}", flush=True)
    del model
    # ---- C2, NC = 4
    model = SU2Model(4)
    geo = model.g
    Xc4 = coarse_field(geo, rng)
    tb, s = 0.2, 0.01
    c0 = geo.CLINKS.index(((0, 0, 0, 0), 0))
    V0 = qexp(tb * Xc4)
    tt = time.time()
    Ub, evb, it, g0, gn, cv = minimise(model, V0, start_config(geo, V0))
    conv &= cv
    print(f"C2 background t={tb}: {'CONVERGED' if cv else 'NOT CONVERGED'} it={it} |g|/|g0|={gn / g0:.1e} "
          f"{time.time() - tt:.0f} s, RSS {rss():.2f} GB", flush=True)
    rhos = {}
    for sgn in (1, -1):
        Bd = tb * Xc4.copy(); Bd[c0, 0] += sgn * s
        V = qexp(Bd)
        tt = time.time()
        U, ev, it, g0p, gn, cv = minimise(model, V, Ub.copy())
        conv &= cv
        rhos[sgn] = residual(V, ev["Mb"])
        print(f"  perturbed {sgn:+d}s: {'CONVERGED' if cv else 'NOT CONVERGED'} it={it} |g|/|g0|={gn / g0p:.1e} "
              f"{time.time() - tt:.0f} s", flush=True)
    drho = (rhos[1] - rhos[-1]) / (2 * s)
    e1 = np.zeros((geo.NCL, 3)); e1[c0, 0] = 1.0
    drl, _ = linear_r(4, e1)
    Dl = drho - drl
    dist = np.array([max(min(X[i], 4 - X[i]) for i in range(d)) for (X, mu) in geo.CLINKS])
    A = {dd: float(np.max(np.linalg.norm(Dl[dist == dd], axis=1))) for dd in (0, 1, 2)}
    Al = {dd: float(np.max(np.linalg.norm(drl[dist == dd], axis=1))) for dd in (0, 1, 2)}
    mNA = math.log(A[0] / A[2]) / 2; mlin = math.log(Al[0] / Al[2]) / 2
    ok["C2-V"] = mlin >= 0.5
    ok["C2a"] = np.max(np.linalg.norm(Dl, axis=1)) <= 0.5 * np.max(np.linalg.norm(drl, axis=1))
    ok["C2b"] = mNA >= 0.5 * mlin
    ok["C-V1"] = conv
    print(f"C2 profiles (d = 0, 1, 2): non-abelian part {A[0]:.3e} {A[1]:.3e} {A[2]:.3e}; linear {Al[0]:.3e} "
          f"{Al[1]:.3e} {Al[2]:.3e}")
    print(f"C2 rates: m_NA = {mNA:.3f}, m_lin = {mlin:.3f}; max|Delta|/max|dr_lin| = "
          f"{np.max(np.linalg.norm(Dl, axis=1)) / np.max(np.linalg.norm(drl, axis=1)):.4f}")
    for kk in ("C-V1", "C-V2", "C1", "C2-V", "C2a", "C2b"):
        print(f"{kk}: {'PASS' if ok[kk] else 'FAIL'}")
    valid = ok["C-V1"] and ok["C-V2"] and ok["C2-V"]
    print(f"c29 C: {'VALID' if valid else 'INVALID'}; time {time.time() - T0:.0f} s, peak RSS {rss():.2f} GB")


# ====================================================================== Part D
def DU(model, U, lam):
    """(D_U lam)_b = Ad(U_b) lam(y) - lam(x), b = (x -> x + e_mu); lam: (NS, 3)."""
    g = model.g
    # head and tail site of each link
    head = np.zeros(g.NL, dtype=np.int64); tail = np.zeros(g.NL, dtype=np.int64)
    for x in itertools.product(range(g.NF), repeat=d):
        sx = g.sidx(x)
        for mu in range(d):
            y = list(x); y[mu] += 1
            head[mu * g.NS + sx] = g.sidx(y); tail[mu * g.NS + sx] = sx
    out = Ad(U, lam[head]) - lam[tail]
    return out


def path_functional(model, U, A):
    """l_P(A) for every axial path P (root -> y): sum_j Ad(T_{j-1}) a~_j; and the full transports T_P."""
    alk, asg = model.alk, model.asg
    Ue = np.concatenate([U, np.array([[1.0, 0, 0, 0]])], axis=0)
    Ae = np.concatenate([A, np.zeros((1, 3))], axis=0)
    T = np.zeros((alk.shape[0], 4)); T[:, 0] = 1.0
    acc = np.zeros((alk.shape[0], 3))
    for m in range(alk.shape[1]):
        lk = alk[:, m]; sg = asg[:, m]
        Ub = Ue[lk]; Ab = Ae[lk]
        fwd = sg > 0
        at = np.where(fwd[:, None], Ab, -Ad(qconj(Ub), Ab))
        acc += Ad(T, at)
        F = np.where(fwd[:, None], Ub, qconj(Ub))
        T = qmul(T, F)
    return acc, T


def h_and_M(model, U, A, lam):
    g = model.g
    acc, T = path_functional(model, U, A)
    nper = len(ORDERS) * len(OFFS)
    h = acc.reshape(len(g.COARSE), nper, 3).mean(axis=1)
    Mv = Ad(T, lam[model.aend]).reshape(len(g.COARSE), nper, 3).mean(axis=1)
    lc = lam[model.aroot].reshape(len(g.COARSE), nper, 3)[:, 0]
    return h, Mv, lc


def hvp(model, U, V, xi, h=1e-4):
    gp = model.evaluate(qmul(qexp(h * xi), U), V)["g"]
    gm = model.evaluate(qmul(qexp(-h * xi), U), V)["g"]
    return (gp - gm) / (2 * h)


def part_D():
    rng = np.random.default_rng(20261029)
    ok = {}
    model = SU2Model(3)
    geo = model.g
    Xc = coarse_field(geo, rng)       # same seed and first draw as Part C's C1
    t = 0.2
    V = qexp(t * Xc)
    U0 = start_config(geo, V)
    tt = time.time()
    Us, ev, it, g0, gn, cv = minimise(model, V, U0)
    print(f"D background t={t}: {'CONVERGED' if cv else 'NOT CONVERGED'} it={it} |g|/|g0|={gn / g0:.1e} "
          f"{time.time() - tt:.0f} s", flush=True)
    roots = np.array([geo.sidx(geo.root(X)) for X in geo.COARSE])
    Urand = qexp(0.3 * rng.normal(size=(geo.NL, 3)))
    worst = 0.0
    for Ux in (Us, Urand):
        for _ in range(3):
            lam = rng.normal(size=(geo.NS, 3))
            Dl = DU(model, Ux, lam)
            h, Mv, lc = h_and_M(model, Ux, Dl, lam)
            worst = max(worst, float(np.max(np.abs(h - (Mv - lc)))) / float(np.max(np.abs(Dl))))
    ok["D1"] = worst <= 1e-12
    print(f"D1 telescoping: max |h_U(D_U lam) - (M_U lam - lam(c))| / max|D_U lam| = {worst:.2e}", flush=True)
    res = {}
    for name, Ux in (("critical U*", Us), ("start U0", U0)):
        rv = []
        for _ in range(3):
            v = rng.normal(size=(geo.NL, 3))
            rv.append(np.linalg.norm(hvp(model, Ux, V, v)) / np.linalg.norm(v))
        med = float(np.median(rv))
        rx = []
        for _ in range(3):
            lam = rng.normal(size=(geo.NS, 3)); lam[roots] = 0.0
            xi = DU(model, Ux, lam)
            rx.append(np.linalg.norm(hvp(model, Ux, V, xi)) / np.linalg.norm(xi))
        res[name] = (max(rx) / med, min(rx) / med)
        print(f"D {name}: |H D_U lam|/|D_U lam| / median|Hv|/|v| = max {max(rx) / med:.2e}, min {min(rx) / med:.2e} "
              f"(median |Hv|/|v| = {med:.3e})", flush=True)
    ok["D2"] = res["critical U*"][0] <= 1e-4
    ok["D3"] = res["start U0"][1] >= 1e-2
    for kk in ("D1", "D2", "D3"):
        print(f"{kk}: {'PASS' if ok[kk] else 'FAIL'}")
    print(f"c29 D: {'PASS' if all(ok.values()) else 'FAIL'}; time {time.time() - T0:.0f} s, peak RSS {rss():.2f} GB")


def smoke():
    rng = np.random.default_rng(1)
    model = SU2Model(4)
    geo = model.g
    V = qexp(0.2 * coarse_field(geo, rng))
    U = start_config(geo, V)
    t = time.time(); ev = model.evaluate(U, V); dt = time.time() - t
    b = int(rng.integers(geo.NL)); xi = rng.normal(size=3); h = 1e-6
    Up = U.copy(); Up[b] = qmul(qexp(h * xi), U[b]); Um = U.copy(); Um[b] = qmul(qexp(-h * xi), U[b])
    fd = (model.evaluate(Up, V)["E"] - model.evaluate(Um, V)["E"]) / (2 * h)
    print(f"smoke NC=4: one evaluation {dt:.2f} s; grad check {float(ev['g'][b] @ xi):.8e} vs fd {fd:.8e}; "
          f"peak RSS {rss():.2f} GB")


if __name__ == "__main__":
    {"A": part_A, "B": part_B, "C": part_C, "D": part_D, "smoke": smoke}[sys.argv[1]]()
