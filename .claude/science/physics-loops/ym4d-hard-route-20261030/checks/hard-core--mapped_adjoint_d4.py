#!/usr/bin/env python3
"""Lemma AD of `library/composite-adjoint.md` in d = 4: an adversarial search for a violation of the power L^2. Consumer: the top coefficient of the contraction, `library/one-step-closure.md`.

Written before running. The earlier checks of this lemma are in d = 2, where the bound is not sharp. Only d = 4 can decide whether the constant in

 (AD1)  ||Res^* lambda||_{l^2} <= C L^2 E |lambda|,  E^4 := sum over plaquettes in the block and its neighbours of theta_p^4,

is free of L. Here Res := Q^o - P_U on one parent bond, at one level, at a Cartan background with adjoint bond angles a_b, to first order in a. Derivation of the form used (own, from the exact formula of Lemma 3.9 of the parts file; tested by R0 below): with P_x the path from y along its contour to x, the line to x' = x + L e_mu, and back along the contour from y' to x'; v_x := sum over P_x of +- a_b, minus the same for the centre x = y; and w_x the signed indicator of the contour from y to x, the line, and the contour from y' to x', all taken forward,

 Res_b = (i/2) avg_x (A - v_x) w_x(b),   A := avg_x v_x.

So Res = T a with T := (1/2) L^-4 W^T (Pi - 1) P, a sparse real linear map, with W, P the path incidence matrices, and the problem is the search for the supremum of R(a) := ||T a||_2 / (L^2 ||d a||_4) over bond angles a on the two blocks. This is a norm from l^4 of the curvature to l^2, by gradient ascent from several seeds.

PRE-STATED criteria.
 R0. Control on the formula, L = 3: against a finite difference of the true map N_0 at a background of amplitude 1e-4, on 30 bonds of the paths, | |Res_b| - |T a|_b | <= 0.02 max_b |T a|_b.
 R1. Control: for a pure gauge a = d omega, ||T a|| <= 1e-10 ||a||.
 R2. For L = 3, 5, 7, 9 and mu = 0, 1, 3, Rmax(L) := the largest R found over all seeds. The bound holds with absolute C if Rmax(L) does not grow: PASS if the fitted power p of Rmax against L over L = 5, 7, 9 is at most 0.25. If p is above 0.25, C is not free of L on this evidence, and the power is what the contraction would have to pay: report p, and FAIL.
 R3. Reported: R at a constant flux in one plane, at the best sheet field (flux on the plane through y, y' spanned by e_mu and the first contour direction, with the return flux left to closure), and at the optimiser; and how far the optimiser's flux is concentrated, as the participation ratio (sum theta^2)^2 / sum theta^4 over the number of plaquettes.

Limits. One level, first order in the flux, a Cartan background, axis-ordered contours (one per point), a local optimum of a non-convex search, so a lower bound on the supremum. RSS guard 2 GB.
"""
import importlib.util
import os
import resource
import sys

import numpy as np
import scipy.sparse as sp

HERE = os.path.dirname(os.path.abspath(__file__))


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def guard():
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")


D = 4
MULT = int(sys.argv[1]) if len(sys.argv) > 1 else 1  # Sensitivity to the optimiser: the same criteria with more steps.


class Geo:
    def __init__(self, L, mu):
        self.L, self.mu = L, mu
        self.h = (L - 1) // 2
        self.shape = tuple(2 * L if i == mu else L for i in range(D))
        self.y = np.array([self.h] * D)
        self.yp = self.y.copy()
        self.yp[mu] += L
        self.strides = np.array([int(np.prod(self.shape[i + 1 :])) for i in range(D)])
        self.nsites = int(np.prod(self.shape))
        self.nb = D * self.nsites

    def bond(self, ax, x):
        return ax * self.nsites + int(np.dot(np.asarray(x) % np.array(self.shape), self.strides))

    def contour(self, start, end):
        """Forward list of (bond id, sign) from start to end, axis ordered."""
        out = []
        x = np.array(start)
        for ax in range(D):
            n = end[ax] - x[ax]
            for _ in range(abs(n)):
                if n > 0:
                    out.append((self.bond(ax, x), 1))
                    x[ax] += 1
                else:
                    x[ax] -= 1
                    out.append((self.bond(ax, x), -1))
        return out

    def matrices(self):
        L, mu = self.L, self.mu
        rs = np.array(np.meshgrid(*[np.arange(-self.h, self.h + 1)] * D, indexing="ij")).reshape(D, -1).T
        rowP, colP, valP = [], [], []
        rowW, colW, valW = [], [], []
        centre = []
        for i, r in enumerate(rs):
            x = self.y + r
            xp = x.copy()
            xp[mu] += L
            G = self.contour(self.y, x)
            Gp = self.contour(self.yp, xp)
            line = []
            z = x.copy()
            for _ in range(L):
                line.append((self.bond(mu, z), 1))
                z[mu] += 1
            path = G + line + [(b, -s) for b, s in Gp]
            for b, s in path:
                rowP.append(i), colP.append(b), valP.append(s)
            for b, s in G + line + Gp:
                rowW.append(i), colW.append(b), valW.append(s)
            if np.all(r == 0):
                centre = i
        n = len(rs)
        P = sp.csr_matrix((valP, (rowP, colP)), shape=(n, self.nb), dtype=float)
        W = sp.csr_matrix((valW, (rowW, colW)), shape=(n, self.nb), dtype=float)
        # v_x = (P a)_x - (P a)_centre; A - v_x = -(v_x - mean v) so the centre drops out.
        return P, W, n

    def curl(self):
        rows, cols, vals = [], [], []
        k = 0
        idx = np.indices(self.shape).reshape(D, -1).T
        pr = 0
        for mu in range(D):
            for nu in range(mu + 1, D):
                for x in idx:
                    xm = x.copy()
                    xm[mu] += 1
                    xn = x.copy()
                    xn[nu] += 1
                    inside = xm[mu] < self.shape[mu] and xn[nu] < self.shape[nu]
                    if not inside:
                        continue
                    for b, s in ((self.bond(mu, x), 1), (self.bond(nu, xm), 1), (self.bond(mu, xn), -1), (self.bond(nu, x), -1)):
                        rows.append(pr), cols.append(b), vals.append(s)
                    pr += 1
        return sp.csr_matrix((vals, (rows, cols)), shape=(pr, self.nb), dtype=float)


class Problem:
    def __init__(self, L, mu):
        self.g = Geo(L, mu)
        self.P, self.W, self.n = self.g.matrices()
        self.C = self.g.curl()
        self.L = L

    def T(self, a):
        v = self.P @ a
        v = v - v.mean()
        return -0.5 * (self.W.T @ v) / self.n

    def Tt(self, r):
        u = self.W @ r
        u = u - u.mean()
        return -0.5 * (self.P.T @ u) / self.n

    def R(self, a):
        t = self.C @ a
        return float(np.linalg.norm(self.T(a)) / (self.L**2 * np.sum(t**4) ** 0.25))

    def ascend(self, a, steps=400):
        best = self.R(a)
        a = a / np.linalg.norm(a)
        eta = 0.2
        for _ in range(steps):
            Ta = self.T(a)
            t = self.C @ a
            g = self.Tt(Ta) / np.dot(Ta, Ta) - (self.C.T @ t**3) / np.sum(t**4)
            g = g - np.dot(g, a) * a
            n = np.linalg.norm(g)
            if n < 1e-12:
                break
            while eta > 1e-6:
                b = a + eta * g / n
                b /= np.linalg.norm(b)
                val = self.R(b)
                if val > best:
                    a, best = b, val
                    eta *= 1.3
                    break
                eta *= 0.5
            if eta <= 1e-6:
                break
        return best, a


def sheet(prob):
    """Flux f on the plane through y, y' spanned by e_mu and the first contour direction: bonds of direction mu carry f (x_0 - y_0) on that plane."""
    g = prob.g
    mu = g.mu
    first = 0 if mu != 0 else 1
    a = np.zeros(g.nb)
    idx = np.indices(g.shape).reshape(D, -1).T
    for x in idx:
        ok = all(x[i] == g.y[i] for i in range(D) if i not in (mu, first))
        if ok:
            a[g.bond(mu, x)] = float(x[first] - g.y[first])
    return a


def constant(prob):
    g = prob.g
    mu = g.mu
    first = 0 if mu != 0 else 1
    a = np.zeros(g.nb)
    idx = np.indices(g.shape).reshape(D, -1).T
    for x in idx:
        a[g.bond(mu, x)] = float(x[first])
    return a


def control_R0():
    """Q^o - P on one parent, from the true map M at a Cartan background, by a difference in the fine bond, against the first-order form."""
    spec = importlib.util.spec_from_file_location("cj", os.path.join(HERE, "hard-core--mapped_composite_jet_d4.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    L, mu = 3, 1
    prob = Problem(L, mu)
    g = prob.g
    rng = np.random.default_rng(3)
    eps = 1e-4
    a = rng.standard_normal(g.nb)
    a = a / np.max(np.abs(a))
    Ta = prob.T(a) * eps
    rs = np.array(np.meshgrid(*[np.arange(-g.h, g.h + 1)] * D, indexing="ij")).reshape(D, -1).T
    paths, Gs, Gps, lines = [], [], [], []
    for r in rs:
        x = g.y + r
        xp = x.copy()
        xp[mu] += L
        G = g.contour(g.y, x)
        Gp = g.contour(g.yp, xp)
        line = []
        z = x.copy()
        for _ in range(L):
            line.append((g.bond(mu, z), 1))
            z[mu] += 1
        Gs.append(G), Gps.append(Gp), lines.append(line)
        paths.append(G + line + [(b, -s) for b, s in reversed(Gp)])
    c_i = int(np.nonzero(np.all(rs == 0, axis=1))[0][0])

    def M_parent(Vf):
        Om = []
        for path in paths:
            q = np.array([1.0, 0, 0, 0])
            for b, sg in path:
                q = m.qmul(q, Vf[b] if sg > 0 else m.qinv(Vf[b]))
            Om.append(q)
        Oc = Om[c_i]
        tavg = sum(m.qlog(m.qmul(O, m.qinv(Oc))) for O in Om) / len(Om)
        return m.qmul(m.qexp(tavg), Oc)

    def coeff(lst, b, start_chi=0.0):
        """Coefficient of the charged component of H_b in the covariant sum along lst."""
        chi = start_chi
        out = 0.0 + 0.0j
        for bb, sg in lst:
            if sg > 0:
                if bb == b:
                    out += np.exp(1j * chi)
                chi += eps * a[bb]
            else:
                chi -= eps * a[bb]
                if bb == b:
                    out -= np.exp(1j * chi)
        return out, chi

    Vf0 = np.zeros((g.nb, 4))
    tv = np.zeros((g.nb, 3))
    tv[:, 2] = 0.5 * eps * a
    Vf0 = m.qexp(tv)
    M0 = M_parent(Vf0)
    Xi = 2 * m.qlog(M0)[2]
    t = 1e-7
    cand = np.nonzero(np.abs(np.asarray(prob.W.sum(axis=0)).ravel()) > 0)[0]
    chosen = rng.choice(cand, size=min(30, cand.size), replace=False)
    worst = 0.0
    for b in chosen:
        V1 = Vf0.copy()
        V1[b] = m.qmul(m.qexp(np.array([t, 0.0, 0.0])), Vf0[b])
        w = m.qlog(m.qmul(M_parent(V1), m.qinv(M0))) / t
        cQ = complex(w[0], w[1])
        Py, Pyp, Pline = 0.0j, 0.0j, 0.0j
        for G, Gp, line in zip(Gs, Gps, lines):
            cg, chi = coeff(G, b)
            cgp, _ = coeff(Gp, b)
            cl, _ = coeff(line, b, chi)
            Py += cg
            Pyp += cgp
            Pline += cl
        n = len(rs)
        Res = cQ - Py / n + np.exp(1j * Xi) * Pyp / n - Pline / n
        worst = max(worst, abs(abs(Res) - abs(Ta[b])))
    return worst, float(np.max(np.abs(Ta)))


def main():
    ok = True
    print("R0", flush=True)
    worst, scale = control_R0()
    r0 = worst <= 0.02 * scale
    ok = ok and r0
    print(f" max | |Res_b| - |T a|_b | = {worst:.3e} against max |T a|_b = {scale:.3e}: {r0}", flush=True)
    print("R1, R2, R3", flush=True)
    table = {}
    for L in (3, 5, 7, 9):
        best = 0.0
        for mu in (0, 1, 3):
            prob = Problem(L, mu)
            guard()
            om = np.random.default_rng(1).standard_normal(prob.g.nsites)
            a = np.zeros(prob.g.nb)
            idx = np.indices(prob.g.shape).reshape(D, -1).T
            for ax in range(D):
                ss = np.array(prob.g.shape)
                om_nd = om.reshape(prob.g.shape)
                diff = np.roll(om_nd, -1, axis=ax) - om_nd
                # Bonds that wrap are not in the model's open box: zero them, and compare on the paths only.
                sl = [slice(None)] * D
                sl[ax] = -1
                diff[tuple(sl)] = 0
                a[ax * prob.g.nsites : (ax + 1) * prob.g.nsites] = diff.ravel()
            r1 = float(np.linalg.norm(prob.T(a)) / np.linalg.norm(a))
            good = r1 <= 1e-10
            ok = ok and good
            vals = {}
            vals["constant"] = prob.R(constant(prob))
            vals["sheet"] = prob.R(sheet(prob))
            top, top_a = 0.0, None
            for seed, a0 in enumerate([sheet(prob), constant(prob)] + [np.random.default_rng(10 + i).standard_normal(prob.g.nb) for i in range(2)]):
                v, x = prob.ascend(a0, steps=(300 if L <= 7 else 150) * MULT)
                if v > top:
                    top, top_a = v, x
            t = prob.C @ top_a
            pr = float(np.sum(t**2) ** 2 / np.sum(t**4) / t.size)
            best = max(best, top)
            guard()
            print(f" L={L} mu={mu}: pure gauge {r1:.1e}: {good}; R constant={vals['constant']:.4f} sheet={vals['sheet']:.4f} optimiser={top:.4f}, participation {pr:.4f} rss={rss_gb():.2f}GB", flush=True)
        table[L] = best
    Ls = np.array([5.0, 7.0, 9.0])
    p = float(np.polyfit(np.log(Ls), np.log([table[5], table[7], table[9]]), 1)[0])
    r2 = p <= 0.25
    ok = ok and r2
    print(" Rmax: " + " ".join(f"L={L}: {table[L]:.4f}" for L in table) + f"; fitted power over L=5,7,9: {p:.3f}: {r2}", flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
