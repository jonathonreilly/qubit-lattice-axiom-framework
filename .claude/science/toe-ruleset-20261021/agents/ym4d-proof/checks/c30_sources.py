"""c30: session-15 instances (criteria: checks/c30_criteria.md, written first).

Part A: strip constants at the corrected (eta, r0) pairs (mpmath, 30 digits).
Part B: the f_0 half of Lemma SRC-id (iii) at complex points.
Part C: the linear chain with sources at every level (generalised source identity, transport, reciprocity, C4 bound).
Part D: informational soft-output constants.
Run one part per job: python3 -I c30_sources.py A|B|C|D
"""
import os
import resource
import sys
import time

import numpy as np
import scipy.sparse.linalg as spla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c26_led as C26  # noqa: E402
import c28_exp as C28  # noqa: E402

L = 3
T0 = time.time()


def rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 30


# ====================================================================== Part A
def part_A():
    from mpmath import mp, mpf, cosh, sinh, exp, sqrt, pi, atan, cos, sin
    mp.dps = 30

    def common(eta, kap, kh):
        kap = mpf(kap); kh = mpf(kh)
        Rb = 1 + kh / (L * L - 1) + kap / 9
        bs = min(kap, 24 / pi ** 2)
        Gam = max(pi ** 2 / 4, Rb)
        eps = exp(eta) - 1
        lam = 1 - 4 * eta ** 2 * cosh(eta) ** 2 / 9
        eZ = (4 * eta ** 2 / 9 + 4 * eta / 3) * cosh(eta)
        cZ = (eps * exp(4 * eta) + 4 * exp(3 * eta) * eps * (1 + exp(eta))) / (9 * lam) + eZ / (9 * lam)
        return kap, kh, Rb, bs, Gam, eps, lam, cZ

    def strip1(eta, r0, kap, kh):          # Lemma EXP-strip (P1)-(P7) + Theorem N2-exp conditions
        eta = mpf(eta); r0 = mpf(r0)
        kap, kh, Rb, bs, Gam, eps, lam, cZ = common(eta, kap, kh)
        e5 = (1 + pi ** 2 / 4 * eps) ** 5 - 1
        eR = kh / (L * L - 1) * eps + kap * cZ
        rho = e5 + (4 * eta ** 2 / bs + 4 * eta / sqrt(bs)) * cosh(eta) * (Rb + eR) + eR
        PsiU = kap * (1 - r0 ** 2 / 6) / (kap + r0 ** 2 * Rb)
        ePsi = ((4 * eta ** 2 + 4 * eta * r0) * cosh(eta) * (Rb + eR) + r0 ** 2 * eR) / ((1 - rho) * bs) + rho / (1 - rho)
        psi0 = 4 * r0 ** 2 / pi ** 2
        brV = 1 / ((1 + rho) * Gam) - (4 * eta ** 2 / psi0 + 4 * eta / sqrt(psi0)) * cosh(eta) / (1 - rho)
        f0 = (4 * eta ** 2 / psi0 + 4 * eta / sqrt(psi0)) * cosh(eta)
        return dict(rho=rho <= mpf(1) / 2, ePsi=ePsi <= PsiU / 2, brV=brV >= (mpf(1) / 2) / ((1 + rho) * Gam),
                    f0=f0 <= mpf(15) / 100, lam=lam > 0, r0=r0 ** 2 < 6), dict(f0=f0, brVratio=brV * (1 + rho) * Gam * 2,
                                                                            ePsiratio=ePsi / (PsiU / 2))

    def strip2(eta, r0, kap, kh):          # Lemma EXP-strip' (S1)-(S7) + Theorem N2-exp' conditions
        eta = mpf(eta); r0 = mpf(r0)
        kap, kh, Rb, bs, Gam, eps, lam, cZ = common(eta, kap, kh)
        ce = cosh(eta) - 1; se = sinh(eta); cphi = 18 * (cosh(eta / 3) - 1); sphi = 6 * sinh(eta / 3)
        a1 = pi ** 2 / 4 * ce; g1 = pi ** 2 / 12
        mm = (1 - a1) ** 5; mpl = ((1 + a1) ** 2 + se ** 2 * g1 ** 2) ** (mpf(5) / 2); tha = 5 * atan(se * g1 / (1 - a1))
        eRR = kh * ce / (L * L - 1) + kap * cZ; eRI = kh * se / (L * L - 1) + kap * cZ
        rR = 1 - mm * cos(tha) + eRR + 4 * cphi * (Rb + eRR) / bs + 2 * sphi * eRI / sqrt(bs)
        rRp = mpl - 1 + eRR + 2 * sphi * eRI / sqrt(bs)
        rI = mpl * sin(tha) + eRI * (1 + 4 * cphi / bs) + 2 * sphi * (Rb + eRR) / sqrt(bs)
        PsiL = 1 - (r0 ** 2 + 4 * cphi + 2 * sphi * r0) * (Rb + eRR + eRI) / ((1 - rR) * bs)
        D2 = (1 + rRp) ** 2 + rI ** 2; psi0 = 4 * r0 ** 2 / pi ** 2
        brV = (1 - rR) / (D2 * Gam) - (8 * ce * (1 + rRp) / psi0 + 4 * se * rI / sqrt(psi0)) / (1 - rR) ** 2
        req = (1 - rR) / (4 * D2 * Gam)
        return dict(tha=tha <= pi / 2, rhoR=rR <= mpf(1) / 2, PsiL=PsiL >= mpf(1) / 10, brV=brV >= req,
                    cphi=4 * cphi <= psi0 / 2, lam=lam > 0), dict(brVratio=brV / req, PsiL=PsiL)

    def bis(f, r0, kap, kh):
        lo, hi = mpf(0), mpf("0.1")
        if not all(f(mpf("1e-8"), r0, kap, kh)[0].values()):
            return mpf(0)
        for _ in range(40):
            mid = (lo + hi) / 2
            if all(f(mid, r0, kap, kh)[0].values()):
                lo = mid
            else:
                hi = mid
        return lo

    ok = True
    for name, f, pairs in [("N2-exp ", strip1, [(1, 1, "0.0111", "0.57"), (0.25, 1, "0.0077", "0.37"), (4, 1, "0.0117", "0.65"),
                                                (0.25, 16, "0.0037", "0.25"), (4, 16, "0.0082", "0.60")]),
                           ("N2-exp'", strip2, [(1, 1, "0.0384", "0.70"), (0.25, 1, "0.0273", "0.37"), (4, 1, "0.0306", "0.90"),
                                                (0.25, 16, "0.0140", "0.24"), (1, 16, "0.0226", "0.47"), (4, 16, "0.0216", "0.67")])]:
        for (kap, kh, eta, r0) in pairs:
            conds, info = f(mpf(eta), mpf(r0), kap, kh)
            good = all(conds.values()); ok &= good
            eb = bis(f, mpf(r0), kap, kh)
            infos = " ".join(f"{k}={float(v):.4f}" for k, v in info.items())
            bad = [k for k, v in conds.items() if not v]
            print(f"A {name} kap={kap} kh={kh} eta={eta} r0={r0}: {'ALL HOLD' if good else 'FAIL ' + str(bad)}; "
                  f"{infos}; bisection eta at this r0 = {float(eb):.5f} (margin {float(eb - mpf(eta)):+.5f})")
    print(f"A1: {'PASS' if ok else 'FAIL'}")
    print(f"c30 A: {'PASS' if ok else 'FAIL'}; time {time.time() - T0:.1f} s, peak RSS {rss():.2f} GB")


# ====================================================================== Part B
def part_B():
    rng = np.random.default_rng(20261027 + 15)
    d = 4
    worst = dict(B1=0.0, B2=0.0, B3=0.0)
    for (k, kap) in [(1, (1.0,)), (2, (1.0, 1.0)), (2, (0.5, 2.0)), (3, (1.0, 1.0, 1.0))]:
        n = L ** k; kp = kap[-1]
        npts = 200 if k < 3 else 60
        for _ in range(npts):
            z = rng.uniform(-np.pi, np.pi, d) + 1j * rng.uniform(-0.05, 0.05, d)
            B = C28.blocks(z, n, k, kap)
            Dn = np.array([C28.Dn_c(z[a], n) for a in range(d)])
            Db = np.array([np.exp(1j * z[a] * np.arange(n) / n).sum() / n for a in range(d)])
            PiD, PiDb = np.prod(Dn), np.prod(Db)
            W, Wb = PiD * Dn, PiDb * Db
            nu = np.exp(1j * z) - 1
            nun = n * (np.exp(1j * z / n) - 1); nubn = n * (np.exp(-1j * z / n) - 1)
            a, dl, R, be, Psi, phi = B["a"], B["dl"], B["R"], B["beta"], B["Psi"], B["phi"]
            jh = rng.normal(size=d) + 1j * rng.normal(size=d)
            rel = lambda x, y: np.max(np.abs(x - y)) / max(np.max(np.abs(x)), np.max(np.abs(y)), 1e-300)
            worst["B1"] = max(worst["B1"], rel(kp * W * Wb, a * dl), rel(W * nu, PiD * nun * dl))
            S = np.sum(nubn * R * jh / be)
            rh = Wb * jh / be + nu * PiDb * S / (be * Psi)
            lhs = jh - kp * W * rh
            Y = (phi * R / be) * jh - a * nun * (dl / be) * S / Psi
            worst["B2"] = max(worst["B2"], rel(lhs, Y))
            for rr in range(d):
                for ss in range(d):
                    if rr == ss:
                        continue
                    c1 = nun[rr] * Y[ss] - nun[ss] * Y[rr]
                    c2 = phi * (nun[rr] * R[ss] * jh[ss] / be[ss] - nun[ss] * R[rr] * jh[rr] / be[rr]
                                - (S / Psi) * nun[rr] * nun[ss] * (R[rr] / be[rr] - R[ss] / be[ss]))
                    worst["B3"] = max(worst["B3"], rel(np.array([c1]), np.array([c2])))
    ok = {kk: v <= 1e-10 for kk, v in worst.items()}
    for kk in worst:
        print(f"{kk}: max relative error {worst[kk]:.2e} -> {'PASS' if ok[kk] else 'FAIL'}")
    print(f"c30 B: {'PASS' if all(ok.values()) else 'FAIL'}; time {time.time() - T0:.1f} s, peak RSS {rss():.2f} GB")


# ====================================================================== Part C/D: chain with sources at every level
def fine_hodge_inverse(j, d_, Nf):
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


class SChain:
    def __init__(self, d_, T, k, kap):
        self.ch = C26.Chain(d_, T, k, kap)
        self.d, self.k, self.kap = d_, k, kap
        self.dm = [self.ch.levels[l].dmat() for l in range(k)]
        M = self.ch.M
        n = M.shape[1]
        self.A = spla.LinearOperator((n, n), matvec=lambda x: M.T @ (M @ x), dtype=float)

    def Qc(self, a, b, x):            # composite root map level a -> level b applied to x
        for i in range(a, b):
            x = self.ch.Q[i] @ x
        return x

    def QcT(self, a, b, y):           # its transpose, level b -> level a
        for i in range(b - 1, a - 1, -1):
            y = self.ch.Q[i].T @ y
        return y

    def solve(self, Bk, js):
        ch, k = self.ch, self.k
        b = np.zeros(ch.M.shape[0]); b[-ch.levels[k].NL:] = np.sqrt(self.kap[-1]) * Bk
        rhs = ch.M.T @ b
        if js is not None:
            rhs = rhs + np.concatenate(js)
        x, info = spla.minres(self.A, rhs, rtol=1e-14, maxiter=200000)
        ne = np.linalg.norm(self.A @ x - rhs) / max(np.linalg.norm(rhs), 1e-300)
        Bs = [x[ch.off[i]:ch.off[i + 1]] for i in range(k)]
        r = [ch.Q[i] @ Bs[i] - (Bs[i + 1] if i + 1 < k else Bk) for i in range(k)]
        return dict(B=Bs, r=r, ne=ne)


def rel(x, y):
    return np.max(np.abs(x - y)) / max(np.max(np.abs(x)), np.max(np.abs(y)), 1e-300)


def part_C():
    rng = np.random.default_rng(20261027 + 30)
    ok = dict(V1=True, C1=True, C2=True, C3=True, C4=True)
    cases = [(2, 5, 2, (1.0, 1.0)), (2, 5, 3, (0.5, 2.0, 1.0)), (2, 3, 3, (1.0, 1.0, 1.0)), (4, 3, 1, (1.0,)),
             (4, 2, 2, (1.0, 1.0))]
    for (d_, T, k, kap) in cases:
        tt = time.time()
        S = SChain(d_, T, k, kap); ch = S.ch
        Nf = ch.levels[0].n
        G = [rng.normal(size=S.dm[l].shape[0]) for l in range(k)]
        js = [S.dm[l].T @ G[l] for l in range(k)]
        Bk = rng.normal(size=ch.levels[k].NL)
        s1 = S.solve(Bk, js)
        # C1: effective datum
        jtot = js[0].copy()
        for l in range(1, k):
            jtot += S.QcT(0, l, js[l])
        geff = S.Qc(0, k, fine_hodge_inverse(jtot, d_, Nf))
        for i in range(0, k - 1):
            acc = np.zeros(ch.levels[i + 1].NL)
            for l in range(i + 1, k):
                acc += S.QcT(i + 1, l, js[l])
            geff += S.Qc(i + 1, k, acc) / kap[i]
        s2 = S.solve(Bk - geff, None)
        c1 = rel(s1["r"][k - 1], s2["r"][k - 1])
        # C2: transport + fine curvature
        c2 = 0.0
        rt = s1["r"][k - 1]
        for i in range(k):
            pred = kap[k - 1] * S.QcT(i + 1, k, rt)
            for l in range(i + 1, k):
                pred -= S.QcT(i + 1, l, js[l])
            c2 = max(c2, rel(kap[i] * s1["r"][i], pred))
        J0 = jtot - kap[k - 1] * S.QcT(0, k, rt)
        c2 = max(c2, rel(S.dm[0] @ s1["B"][0], S.dm[0] @ fine_hodge_inverse(J0, d_, Nf)))
        # C3: reciprocity (B_k = 0 with sources; data B'_k without sources)
        s0 = S.solve(np.zeros(ch.levels[k].NL), js)
        c3 = 0.0; ne = max(s1["ne"], s2["ne"], s0["ne"])
        for _ in range(3):
            Bp = rng.normal(size=ch.levels[k].NL)
            sp_ = S.solve(Bp, None); ne = max(ne, sp_["ne"])
            lhs = kap[k - 1] * float(s0["r"][k - 1] @ Bp)
            rhs = sum(float(G[l] @ (S.dm[l] @ sp_["B"][l])) for l in range(k))
            c3 = max(c3, abs(lhs - rhs) / max(abs(lhs), abs(rhs), 1e-300))
        # C4: 2-form transport bound
        c4 = 0.0
        for l in range(k - 1):
            for m in (1, 2):
                if l + m > k - 1:
                    continue
                dm_top = S.dm[l + m]
                for _ in range(20):
                    H = rng.uniform(-1, 1, size=dm_top.shape[0])
                    v = S.QcT(l, l + m, dm_top.T @ H)
                    c4 = max(c4, np.max(np.abs(v)) / (2 * (d_ - 1) * L ** ((2 - d_) * m) * np.max(np.abs(H))))
        ok["V1"] &= ne <= 1e-8; ok["C1"] &= c1 <= 1e-6; ok["C2"] &= c2 <= 1e-6; ok["C3"] &= c3 <= 1e-6; ok["C4"] &= c4 <= 1
        print(f"C d={d_} T={T} k={k} kap={kap}: ne {ne:.1e}  C1 {c1:.2e}  C2 {c2:.2e}  C3 {c3:.2e}  C4 max ratio {c4:.3f}"
              f"  ({time.time() - tt:.0f} s, RSS {rss():.2f} GB)", flush=True)
    for kk, v in ok.items():
        print(f"{kk}: {'PASS' if v else 'FAIL'}")
    print(f"c30 C: {'PASS' if all(ok.values()) else 'FAIL'}; time {time.time() - T0:.0f} s, peak RSS {rss():.2f} GB")


def part_D():
    rng = np.random.default_rng(20261027 + 40)
    cases = [(2, 5, 1, (1.0,)), (2, 5, 2, (1.0, 1.0)), (2, 5, 3, (1.0, 1.0, 1.0)), (4, 2, 1, (1.0,)), (4, 2, 2, (1.0, 1.0))]
    for (d_, T, k, kap) in cases:
        S = SChain(d_, T, k, kap); ch = S.ch
        for l in sorted({0, k - 1}):
            Gc = rng.uniform(-1, 1, size=S.dm[l].shape[0])
            Gl = Gc / L ** (2 * (k - l))
            js = [np.zeros(ch.levels[i].NL) for i in range(k)]
            js[l] = S.dm[l].T @ Gl
            s = S.solve(np.zeros(ch.levels[k].NL), js)
            top = np.max(np.abs(s["r"][k - 1])) / np.max(np.abs(Gc))
            lv = [L ** (k - 1 - i) * L ** (k - 1 - i) * np.max(np.abs(s["r"][i])) / np.max(np.abs(Gc)) for i in range(k)]
            print(f"D d={d_} T={T} k={k} source level {l}: sup|r^c_(k-1)|/sup|G^c| = {top:.4f}; "
                  f"L^(k-1-i) sup|r^c_i|/sup|G^c| (i=0..k-1) = {[round(x, 4) for x in lv]}  ne {s['ne']:.1e}", flush=True)
    print(f"c30 D: done (informational); time {time.time() - T0:.0f} s, peak RSS {rss():.2f} GB")


if __name__ == "__main__":
    {"A": part_A, "B": part_B, "C": part_C, "D": part_D}[sys.argv[1]]()
