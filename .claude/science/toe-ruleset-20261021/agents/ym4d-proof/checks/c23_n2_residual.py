"""c23: N2 linear half (criteria: checks/c23_criteria.md, written before this script).

Part A: abelian linearised soft chain (Setting SC), S4' root-based linearised Q, L = 3, kappa_i = 1.
Part B: SU(2), d = 4, one soft step, c22 machinery, large pure gauge / large flat field times small curvature.
Usage: python3 c23_n2_residual.py A | B
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

T0 = time.time()
L = 3


# ----------------------------------------------------------------------------- Part A geometry
class Level:
    def __init__(self, d, n):
        self.d, self.n = d, n
        self.N = n ** d
        self.NL = d * self.N
        self.planes = list(itertools.combinations(range(d), 2))

    def site(self, X):                      # X: (..., d) integer array
        X = np.mod(X, self.n)
        s = np.zeros(X.shape[:-1], dtype=np.int64)
        for i in range(self.d):
            s = s * self.n + X[..., i]
        return s

    def coords(self):
        g = np.indices((self.n,) * self.d).reshape(self.d, -1).T
        return g                            # row j = coordinates of site j (lexicographic)

    def link(self, X, mu):
        return mu * self.N + self.site(X)

    def dmat(self):
        X = self.coords(); rows, cols, vals = [], [], []
        for p, (mu, nu) in enumerate(self.planes):
            r = p * self.N + np.arange(self.N)
            em = np.zeros(self.d, dtype=np.int64); em[mu] = 1
            en = np.zeros(self.d, dtype=np.int64); en[nu] = 1
            for (c, v) in ((self.link(X, mu), 1.0), (self.link(X + em, nu), 1.0),
                           (self.link(X + en, mu), -1.0), (self.link(X, nu), -1.0)):
                rows.append(r); cols.append(c); vals.append(np.full(self.N, v))
        return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                             shape=(len(self.planes) * self.N, self.NL))


def axial(a, b, order):
    out = []; z = list(a)
    for c in order:
        while z[c] != b[c]:
            if b[c] > z[c]:
                out.append((tuple(z), c, 1)); z[c] += 1
            else:
                w = list(z); w[c] -= 1; out.append((tuple(w), c, -1)); z[c] -= 1
    return out


def template(d, mu):
    """S4' contour family for the coarse link (0, mu) with root at the origin: {(z, nu): weight}."""
    h = (L - 1) // 2
    orders = list(itertools.permutations(range(d)))
    tw = {}
    w = 1.0 / (len(orders) * L ** d)
    cY = [0] * d; cY[mu] = L
    for sig in orders:
        for off in itertools.product(range(-h, h + 1), repeat=d):
            y = list(off); yL = list(y); yL[mu] += L
            seq = axial([0] * d, y, sig)
            for j in range(L):
                z = list(y); z[mu] += j; seq.append((tuple(z), mu, 1))
            seq += [(z, c, -s) for (z, c, s) in reversed(axial(cY, yL, sig))]
            for (z, c, s) in seq:
                tw[(z, c)] = tw.get((z, c), 0.0) + s * w
    return {k: v for k, v in tw.items() if abs(v) > 1e-15}


def qmat(fine, coarse, tmpls):
    d = fine.d; h = (L - 1) // 2
    Xc = coarse.coords(); rows, cols, vals = [], [], []
    for mu in range(d):
        r = coarse.link(Xc, mu)
        root = L * Xc + h
        for (z, nu), wv in tmpls[mu].items():
            rows.append(r); cols.append(fine.link(root + np.array(z), nu)); vals.append(np.full(coarse.N, wv))
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                         shape=(coarse.NL, fine.NL))


def whitney(Bk, top, lev, m):
    """R_i W(B_k) on a level with m = k - i (coarse coordinates: level-i site x -> (x - o)/L^m)."""
    d = top.d; s = L ** m; o = (s - 1) // 2
    x = lev.coords(); out = np.zeros(lev.NL)
    for mu in range(d):
        rel = x - o
        n = np.floor_divide(rel, s); fr = np.mod(rel, s) / s
        val = np.zeros(lev.N)
        for a in itertools.product((0, 1), repeat=d - 1):
            aa = list(a); aa.insert(mu, 0); aa = np.array(aa)
            wgt = np.ones(lev.N)
            for nu in range(d):
                if nu == mu:
                    continue
                wgt *= fr[:, nu] if aa[nu] == 1 else (1.0 - fr[:, nu])
            val += wgt * Bk[top.link(n + aa, mu)]
        out[mu * lev.N:(mu + 1) * lev.N] = val / s
    return out


class Chain:
    def __init__(self, d, T, k):
        self.d, self.T, self.k = d, T, k
        self.levels = [Level(d, T * L ** (k - i)) for i in range(k + 1)]
        tm = [template(d, mu) for mu in range(d)]
        self.Q = [qmat(self.levels[i], self.levels[i + 1], tm) for i in range(k)]
        self.D0 = self.levels[0].dmat(); self.Dk = self.levels[k].dmat()
        nv = [lv.NL for lv in self.levels[:k]]
        self.off = np.concatenate([[0], np.cumsum(nv)])
        blocks = [[None] * k for _ in range(k + 1)]
        blocks[0][0] = self.D0
        for i in range(k):
            blocks[i + 1][i] = self.Q[i]
            if i + 1 < k:
                blocks[i + 1][i + 1] = -sp.identity(self.levels[i + 1].NL, format="csr")
        self.M = sp.bmat(blocks, format="csr")
        self.nrow = [self.D0.shape[0]] + [lv.NL for lv in self.levels[1:]]

    def rhs(self, Bk):
        b = np.zeros(self.M.shape[0]); b[-self.levels[self.k].NL:] = Bk
        return b

    def split(self, x):
        return [x[self.off[i]:self.off[i + 1]] for i in range(self.k)]

    def energy_parts(self, Bs, Bk):
        f = self.D0 @ Bs[0]
        r = [self.Q[i] @ Bs[i] - (Bs[i + 1] if i + 1 < self.k else Bk) for i in range(self.k)]
        return 0.5 * float(f @ f) + 0.5 * sum(float(ri @ ri) for ri in r), f, r

    def solve(self, Bk):
        b = self.rhs(Bk)
        out = lsmr(self.M, b, atol=1e-14, btol=1e-14, maxiter=200000)
        x, flag, its = out[0], out[1], out[2]
        Mtb = self.M.T @ b
        ne = np.linalg.norm(self.M.T @ (self.M @ x - b)) / max(np.linalg.norm(Mtb), 1e-300)
        E, f, r = self.energy_parts(self.split(x), Bk)
        return dict(E=E, f=f, r=r, flag=flag, its=its, ne=ne)

    def whitney_energy(self, Bk):
        Bs = [whitney(Bk, self.levels[self.k], self.levels[i], self.k - i) for i in range(self.k)]
        back = whitney(Bk, self.levels[self.k], self.levels[self.k], 0)
        E, f, r = self.energy_parts(Bs, Bk)
        return E, float(np.max(np.abs(back - Bk)) / max(np.max(np.abs(Bk)), 1e-300))

    def cell_profile(self, f, r, X0):
        """chain energy per coarse cell vs torus sup-distance from coarse site X0."""
        top = self.levels[self.k]; prof = np.zeros(top.N)
        lv0 = self.levels[0]; x = lv0.coords(); s = L ** self.k; o = (s - 1) // 2
        cell = top.site(np.floor_divide(x - o, s))
        for p in range(len(lv0.planes)):
            np.add.at(prof, cell, 0.5 * f[p * lv0.N:(p + 1) * lv0.N] ** 2)
        for i in range(self.k):
            lv = self.levels[i + 1]; x = lv.coords(); s = L ** (self.k - i - 1); o = (s - 1) // 2
            cell = top.site(np.floor_divide(x - o, s))
            for mu in range(self.d):
                np.add.at(prof, cell, 0.5 * r[i][mu * lv.N:(mu + 1) * lv.N] ** 2)
        Xc = top.coords(); dlt = np.abs(Xc - np.array(X0)); dlt = np.minimum(dlt, self.T - dlt)
        dist = dlt.max(axis=1)
        return {int(dd): float(prof[dist == dd].max()) for dd in np.unique(dist)}


def part_A():
    rng = np.random.default_rng(20261027)
    ok = {k: True for k in ("V1", "V2", "Q1", "Q2", "Q3")}
    ratios = {}
    for (d, T, ks) in ((2, 9, (1, 2, 3, 4)), (4, 3, (1,))):
        for k in ks:
            t = time.time(); ch = Chain(d, T, k); top = ch.levels[k]
            Xc = top.coords()
            BR = rng.normal(size=top.NL)
            BS = np.zeros(top.NL)
            for mu in range(d):
                for _ in range(3):
                    m = rng.integers(-1, 2, size=d); a = rng.normal(); ph = rng.uniform(0, 2 * np.pi)
                    BS[mu * top.N:(mu + 1) * top.N] += a * np.cos(2 * np.pi * (Xc @ m) / T + ph)
            lam = 50 * rng.normal(size=top.N); cst = 10 * rng.normal(size=d)
            grad = np.concatenate([lam[top.site(Xc + np.eye(d, dtype=np.int64)[mu])] - lam for mu in range(d)])
            const = np.repeat(cst, top.N)
            BZ = grad + const
            BG = BR + BZ
            res = {}
            for name, B in (("R", BR), ("S", BS), ("G", BG), ("Z", BZ)):
                s = ch.solve(B); EW, back = ch.whitney_energy(B)
                dB = ch.Dk @ B; nd = float(dB @ dB)
                s.update(EW=EW, back=back, nd=nd, nB=float(B @ B)); res[name] = s
                if name != "Z":
                    ok["V1"] &= s["flag"] in (1, 2) and s["ne"] <= 1e-6
                    ok["V2"] &= back <= 1e-12 and s["E"] <= EW * (1 + 1e-8)
            rR, rG = res["R"]["r"][-1], res["G"]["r"][-1]
            q1 = (np.max(np.abs(rG - rR)) <= 1e-6 * np.max(np.abs(rR))
                  and np.max(np.abs(res["G"]["f"] - res["R"]["f"])) <= 1e-6 * np.max(np.abs(res["R"]["f"]))
                  and abs(res["G"]["E"] - res["R"]["E"]) <= 1e-6 * res["R"]["E"])
            q2 = res["Z"]["E"] <= 1e-12 * res["Z"]["nB"]
            ok["Q1"] &= bool(q1); ok["Q2"] &= bool(q2)
            supr = float(np.max(np.abs(rR))) / float(np.max(np.abs(ch.Dk @ BR)))
            supf = L ** (2 * k) * float(np.max(np.abs(res["R"]["f"]))) / float(np.max(np.abs(ch.Dk @ BR)))
            ratios[(d, k)] = {n_: (res[n_]["EW"] / res[n_]["nd"], res[n_]["E"] / res[n_]["nd"]) for n_ in ("R", "S")}
            print(f"d={d} k={k}: fine side {T * L ** k}, {ch.M.shape[1]} unknowns; LSMR its "
                  f"{[res[n_]['its'] for n_ in 'RSGZ']}, normal-eq rel {max(res[n_]['ne'] for n_ in 'RSG'):.1e}; "
                  f"{time.time() - t:.0f} s", flush=True)
            for n_ in "RS":
                print(f"   data {n_}: E_k/|dB|^2 = {res[n_]['E'] / res[n_]['nd']:.5f}, "
                      f"E_W/|dB|^2 = {res[n_]['EW'] / res[n_]['nd']:.5f}")
            print(f"   Q1 orbit: max|dr|/max|r| = {np.max(np.abs(rG - rR)) / np.max(np.abs(rR)):.1e}; "
                  f"Q2 closed: E/|B|^2 = {res['Z']['E'] / res['Z']['nB']:.1e}; "
                  f"I1: sup|r_top|/sup|dB| = {supr:.4f}, sup|f_0|/sup|dB| = {supf:.4f}", flush=True)
            if d == 2:
                e1 = np.zeros(top.NL); e1[top.link(np.array([[0, 0]]), 0)[0]] = 1.0
                s = ch.solve(e1)
                prof = ch.cell_profile(s["f"], s["r"], (0, 0))
                rr = [r_ for r_ in (2, 3, 4) if r_ in prof and prof[r_] > 0]
                slope = -np.polyfit(rr, np.log([prof[r_] for r_ in rr]), 1)[0] if len(rr) >= 2 else float("nan")
                ratios[(d, k)]["m"] = slope
                print(f"   I2 local energy per cell vs r: " + " ".join(f"r={r_}:{prof[r_]:.2e}" for r_ in sorted(prof))
                      + f"; fitted decay rate m = {slope:.3f}", flush=True)
            del ch
    for n_ in "RS":
        for j in (0, 1):
            vals = [ratios[(2, k)][n_][j] for k in (1, 2, 3, 4)]
            ok["Q3"] &= max(vals) <= 1.5 * vals[1]
    for key in ("V1", "V2", "Q1", "Q2", "Q3"):
        print(f"{key}: {'PASS' if ok[key] else 'FAIL'}")
    ms = [ratios[(2, k)].get("m") for k in (1, 2, 3, 4)]
    print("I2 decay rates m_k (k = 1..4): " + " ".join(f"{m:.3f}" for m in ms)
          + f"; m_4 >= 0.5 m_2: {ms[3] >= 0.5 * ms[1]} (informational)")
    print(f"c23 A: {'VALID' if ok['V1'] and ok['V2'] else 'INVALID'}; time {time.time() - T0:.0f} s, "
          f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.0f} MB")


# ----------------------------------------------------------------------------- Part B
def part_B():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import c22_soft_su2_4d as c22
    q = c22
    model = q.FastModel()
    Xc = q.coarse_field()
    t = 0.1
    rng = np.random.default_rng(20261028)
    V0 = q.qexp(t * Xc)
    h = rng.normal(size=(len(q.COARSE), 4)); h /= np.linalg.norm(h, axis=1, keepdims=True)
    xid = {X: i for i, X in enumerate(q.COARSE)}
    th = (0.9, 0.7, 0.5, 0.3)
    Dq = np.array([q.qexp(np.array([0.0, 0.0, th[mu]])) for mu in range(q.D)])
    V1 = np.zeros_like(V0); V2 = np.zeros_like(V0); V3 = np.zeros_like(V0)
    for ci, (X, mu) in enumerate(q.CLINKS):
        Y = list(X); Y[mu] = (Y[mu] + 1) % q.NC
        V1[ci] = q.qmul(q.qmul(h[xid[X]], V0[ci]), q.qconj(h[xid[tuple(Y)]]))
        V2[ci] = q.qmul(Dq[mu], V0[ci]); V3[ci] = Dq[mu]

    def coarse_curv(V):
        m = 0.0
        for X in q.COARSE:
            for (mu, nu) in itertools.combinations(range(q.D), 2):
                Xm = list(X); Xm[mu] = (Xm[mu] + 1) % q.NC
                Xn = list(X); Xn[nu] = (Xn[nu] + 1) % q.NC
                a = V[q.CID[(X, mu)]]; b = V[q.CID[(tuple(Xm), nu)]]
                c = V[q.CID[(tuple(Xn), mu)]]; e = V[q.CID[(X, nu)]]
                P = q.qmul(q.qmul(a, b), q.qmul(q.qconj(c), q.qconj(e)))
                m = max(m, float(np.linalg.norm(q.qlog(P))))
        return m

    out = {}
    conv = True
    for name, V in (("B0", V0), ("B1", V1), ("B2", V2), ("B3", V3)):
        tt = time.time()
        U, ev, it, g0, gn, cv = q.minimise(model, V, q.start_config(V))
        conv &= cv
        Mb = ev["Mb"]; P = Mb / np.linalg.norm(Mb, axis=1, keepdims=True)
        res = np.linalg.norm(q.qlog(q.qmul(q.qconj(V), P)), axis=1)
        F = q.factors(U, model.plk, model.psg); Tp = q.products(F)[:, -1]
        S = L ** 2 * float(np.max(np.linalg.norm(q.qlog(Tp), axis=1)))
        out[name] = dict(E=ev["E"], Rt=float(res.max()), Rm=float(res.mean()), C=coarse_curv(V),
                         Phi=float(np.max(np.linalg.norm(q.qlog(V), axis=1))), S=S)
        o = out[name]
        print(f"{name}: {'CONVERGED' if cv else 'NOT CONVERGED'} it={it} |g|/|g0|={gn / g0:.1e} E={o['E']:.8e} "
              f"R_top={o['Rt']:.5e} mean resid={o['Rm']:.5e} C={o['C']:.5f} Phi={o['Phi']:.5f} S={o['S']:.5f} "
              f"({time.time() - tt:.0f} s)", flush=True)
    b0, b1, b2, b3 = out["B0"], out["B1"], out["B2"], out["B3"]
    Q4 = abs(b1["E"] - b0["E"]) <= 1e-4 * b0["E"] and abs(b1["Rt"] / b0["Rt"] - 1) <= 0.05
    rr = b2["Rt"] / b0["Rt"]
    Q5 = rr <= 2 * b2["C"] / b0["C"] and rr <= 0.5 * b2["Phi"] / b0["Phi"]
    Q6 = b3["E"] <= 1e-8 and b3["Rt"] <= 1e-4
    print(f"Q5 numbers: R_top(B2)/R_top(B0) = {rr:.4f}; 2 C(B2)/C(B0) = {2 * b2['C'] / b0['C']:.4f}; "
          f"0.5 Phi(B2)/Phi(B0) = {0.5 * b2['Phi'] / b0['Phi']:.4f}")
    for k_, v in (("V3", conv), ("Q4", Q4), ("Q5", Q5), ("Q6", Q6)):
        print(f"{k_}: {'PASS' if v else 'FAIL'}")
    print(f"c23 B: {'VALID' if conv else 'INVALID'}; time {time.time() - T0:.0f} s, "
          f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.0f} MB")


if __name__ == "__main__":
    part_A() if sys.argv[1] == "A" else part_B()
