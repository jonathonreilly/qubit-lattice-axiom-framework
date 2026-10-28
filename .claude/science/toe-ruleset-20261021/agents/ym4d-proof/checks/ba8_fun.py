"""ba8 (BFT lane A, session 8): checks of BFT_A §36 (push-down identities, root-funnel identity RF, funnel spikes in
three representatives of the plaquette response, eps geometry, PW-cc ratios).

Abelian Setting LIN, L = 3, kappa = 1, d = 4; imports checks/ba5_y.py and checks/c26_led.py read-only.
Criteria: checks/ba8_criteria.md (written before this file).  Usage: python3 ba8_fun.py E1|E2
"""
import itertools
import sys
import time

import numpy as np

sys.path.insert(0, "/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/.claude/science/"
                   "toe-ruleset-20261021/agents/ym4d-proof/checks")
import ba5_y as b5  # noqa: E402
import c26_led as c26  # noqa: E402

L = b5.L; H = b5.H
T0 = time.time()
RNG = np.random.default_rng(8)


def stamp():
    return f"({time.time() - T0:.0f} s, RSS {b5.rss():.0f} MB)"


def off(j):
    return (L ** j - 1) // 2


# h template: averaged axial line integral from the root to root + offset (24 orders, offsets in [-H, H]^4)
HT = {}
_orders = list(itertools.permutations(range(4)))
_w = 1.0 / (len(_orders) * L ** 4)
for _sig in _orders:
    for _off in itertools.product(range(-H, H + 1), repeat=4):
        for (z, c, s) in c26.axial([0] * 4, list(_off), _sig):
            key = (tuple(H + zi for zi in z), c)
            HT[key] = HT.get(key, 0.0) + s * _w
HT = {k_: v for k_, v in HT.items() if abs(v) > 1e-15}


def hfun(v, Tc):
    """h(v): level-(i+1) function (side Tc) from a level-i 1-form v (side Tc*L)."""
    out = np.zeros((Tc,) * 4); v8 = [b5.view8(a, Tc) for a in v]
    for (o, c), wt in HT.items():
        out += wt * v8[c][b5.sl(o)]
    return out


def qstr(v, Tc):
    out = []
    for mu in range(4):
        w = sum(np.roll(v[mu], -j, axis=mu) for j in range(L))
        out.append(b5.view8(w, Tc).mean(axis=(1, 3, 5, 7)))
    return out


def grad(f):
    return [b5.fwd(f, mu) for mu in range(4)]


def div(e):
    return sum(b5.bwd(e[mu], mu) for mu in range(4))


def ev(f, j, l):
    """restriction of a level-j function to the level-l sites (l >= j)."""
    s = L ** (l - j); o = (s - 1) // 2
    return f[o::s, o::s, o::s, o::s]


class Tools:
    def __init__(self, ch):
        self.ch = ch; self.k = ch.k; self.S = ch.S

    def Phi(self, v0, l):
        acc = np.zeros((self.S[l],) * 4); u = v0
        for i in range(l):
            phi = hfun(u, self.S[i + 1])
            acc += ev(phi, i + 1, l)
            u = qstr(u, self.S[i + 1])
        return acc

    def qstr_to(self, v0, l):
        u = v0
        for i in range(l):
            u = qstr(u, self.S[i + 1])
        return u

    def q_to(self, v, a, b):
        u = v
        for i in range(a, b):
            u = b5.Qop(u, self.S[i + 1])
        return u

    def qT_to(self, j, a, b):
        """(Q^(a->b))^T j, j a level-b 1-form."""
        u = j
        for i in range(b - 1, a - 1, -1):
            u = b5.QTop(u, self.S[i + 1])
        return u

    def sigma(self, X0):
        M = self.S[0]; sg = np.zeros((M,) * 4)
        for l in range(1, self.k):
            P = self.Phi(X0, l); s = L ** l; o = off(l)
            sg[o::s, o::s, o::s, o::s] = P
        s = L ** self.k; o = off(self.k)
        sg[o::s, o::s, o::s, o::s] = 0.0
        return sg

    def xi(self, lam):
        out = []
        for j in range(self.k):
            out += grad(ev(lam, 0, j))
        return out

    def coulomb0(self, X):
        """S_C0 representative: lambda = 0 at level-k roots, d*(Y_0 + d lambda) = 0 elsewhere."""
        M = self.S[0]; s = L ** self.k; o = off(self.k)
        mask = np.ones((M,) * 4); mask[o::s, o::s, o::s, o::s] = 0.0
        Y0 = self.ch.lev(X, 0)
        rhs = [-mask * div(Y0)]

        def op(p):
            return [mask * div(grad(mask * p[0]))]
        lam, r, it = b5.cg(op, rhs, tol=1e-13, maxit=20000)
        lam = mask * lam[0]
        return b5.axpy(1.0, self.xi(lam), X), r, it

    def sp(self, X, l, Zfine):
        idx = tuple((z - off(l)) // L ** l for z in Zfine)
        return float(div(self.ch.lev(X, l))[idx]) / 8.0


def E1():
    # (a) one step Q = Q_str - d h, levels 0->1 and 1->2 (k = 2, T = 2)
    ch = b5.Chain(2, 2)
    for i in range(2):
        v = [RNG.standard_normal((ch.S[i],) * 4) for _ in range(4)]
        a = b5.Qop(v, ch.S[i + 1]); b = b5.axpy(-1.0, grad(hfun(v, ch.S[i + 1])), qstr(v, ch.S[i + 1]))
        print(f"  E1a step {i}->{i + 1}: max|Qv - (Q_str v - d h v)| / max|Qv| = {b5.mx(b5.axpy(-1.0, b, a)) / b5.mx(a):.2e}",
              flush=True)
    # (b) push-down identities, k = 3, T = 1
    ch = b5.Chain(3, 1); tl = Tools(ch); k = 3
    X = []
    for j in range(k):
        X += [RNG.standard_normal((ch.S[j],) * 4) for _ in range(4)]
    B = [RNG.standard_normal((ch.S[k],) * 4) for _ in range(4)]
    r = ch.res(X, B)
    l = 2; jj = [RNG.standard_normal((ch.S[l],) * 4) for _ in range(4)]
    lhs = b5.dot(jj, ch.lev(X, l))
    rhs = b5.dot(tl.qT_to(jj, 0, l), ch.lev(X, 0)) - sum(b5.dot(tl.qT_to(jj, m + 1, l), r[m]) for m in range(l))
    print(f"  E1b push-down (l = 2): |lhs - rhs|/|lhs| = {abs(lhs - rhs) / abs(lhs):.2e}", flush=True)
    bb = [RNG.standard_normal((ch.S[k],) * 4) for _ in range(4)]
    lhs = b5.dot(tl.qT_to(bb, 0, k), ch.lev(X, 0))
    rhs = b5.dot(bb, B) + sum(b5.dot(tl.qT_to(bb, i + 1, k), r[i]) for i in range(k))
    print(f"  E1b top identity: |lhs - rhs|/|lhs| = {abs(lhs - rhs) / abs(lhs):.2e}", flush=True)
    # (c) RF identity at every level-l site, l = 1, 2
    X0 = ch.lev(X, 0)
    for l in (1, 2):
        sp = div(ch.lev(X, l)) / 8.0
        P = tl.Phi(X0, l)
        nb = sum(np.roll(P, sgn, axis=mu) for mu in range(4) for sgn in (1, -1))
        f = -P + nb / 8.0 + div(tl.qstr_to(X0, l)) / 8.0
        for i in range(l):
            f = f - div(tl.q_to(r[i], i + 1, l)) / 8.0
        print(f"  E1c RF l = {l}: max|sp_l - RF| / max|sp_l| = {np.max(np.abs(sp - f)) / np.max(np.abs(sp)):.2e} {stamp()}",
              flush=True)


def response(ch, site):
    M = ch.S[0]
    F = b5.delta_p(M)
    F = [np.roll(a, tuple(site), axis=(0, 1, 2, 3)) for a in F]
    Y, rY, itY = ch.solve(ch.rhs(cur={0: b5.dT(F)}))
    return Y, rY, itY


def report(tl, name, Y, Z):
    k = tl.k; out = {}
    for l in range(k):
        Yl = tl.ch.lev(Y, l)
        isite = all((z - off(l)) % L ** l == 0 for z in Z)
        spl = tl.sp(Y, l, Z) if isite else float("nan")
        mxl = b5.mx(Yl); s1 = b5.l1(Yl)
        out[l] = (spl, mxl)
        print(f"      {name:4s} l={l}: sp_l(Z) L^2l = {spl * L ** (2 * l):+.4f}; max|Y_l| L^2l = {mxl * L ** (2 * l):.4f}; "
              f"sum|Y_l|/L^(k-3l) = {s1 / float(L) ** (k - 3 * l):.4f}", flush=True)
    return out


def E2():
    k, T = 3, 1
    ch = b5.Chain(k, T); tl = Tools(ch)
    Z = (4, 4, 4, 4)
    offs = [(0, 0, 0, 0), (1, 0, 0, 0), (-1, 0, 0, 0), (0, 0, 1, 0), (1, 1, 0, 0)]
    # reference p (as REVIEW_BFT_A_S7 D2)
    Y, rY, it = response(ch, (8, 8, 8, 8))
    Yc, rc, itc = tl.coulomb0(Y)
    ref = {"CG": b5.mx(ch.lev(Y, 2)) * L ** 4, "C0": b5.mx(ch.lev(Yc, 2)) * L ** 4}
    print(f"  E2 k=3 T=1 reference p at (8,8,8,8): CG res {rY:.0e}, C0 res {rc:.0e} ({itc} it); "
          f"max|Y_2| L^4: CG {ref['CG']:.4f}, C0 {ref['C0']:.4f} {stamp()}", flush=True)
    del Y, Yc
    for o in offs:
        site = tuple((Z[i] + o[i]) % ch.S[0] for i in range(4))
        Y, rY, it = response(ch, site)
        Yc, rc, itc = tl.coulomb0(Y)
        Ys = b5.axpy(1.0, tl.xi(tl.sigma(ch.lev(Yc, 0))), Yc)
        print(f"    p = (0,1)-plaquette at Z + {o}: CG res {rY:.0e} ({it} it), C0 res {rc:.0e} ({itc} it) {stamp()}",
              flush=True)
        a = report(tl, "CG", Y, Z); b = report(tl, "C0", Yc, Z); c = report(tl, "C0#", Ys, Z)
        rho = abs(b[2][0]) * L ** 4 / max(abs(b[1][0]) * L ** 2, 1e-300)
        f3 = (rho >= 4.0) and (abs(b[2][0]) * L ** 4 >= 2.0 * ref["C0"])
        f6 = abs(c[2][0]) * L ** 4 > 0.5 * abs(b[2][0]) * L ** 4
        Z1 = tuple((z - off(1)) // L for z in Z)
        eps_c0 = float(hfun(ch.lev(Yc, 0), ch.S[1])[Z1]); eps_cg = float(hfun(ch.lev(Y, 0), ch.S[1])[Z1])
        print(f"      rho = {rho:.3f}; F3-test {'YES' if f3 else 'no'}; F6-test {'YES' if f6 else 'no'}; "
              f"eps(C0) = phi_1(Y_0)(Z) = {eps_c0:+.6f}; eps(CG) = {eps_cg:+.6f}; "
              f"sum_l sp_l(CG) = {sum(a[l][0] for l in range(k)):+.2e}", flush=True)
        if o == (1, 0, 0, 0):
            for l in range(k):
                jj = b5.coulomb([RNG.standard_normal((ch.S[l],) * 4) for _ in range(4)])
                val = abs(b5.dot(jj, ch.lev(Y, l))) / (float(L) ** (k - 3 * l) * b5.mx(jj))
                print(f"      E4 l={l}: |<j, Y_l>|/(L^(k-3l) max|j|) = {val:.4f} (random co-closed j)", flush=True)
        del Y, Yc, Ys
    # k = 2, T = 2 (informational)
    k, T = 2, 2
    ch = b5.Chain(k, T); tl = Tools(ch)
    for name, Z in [("Z1 = (7,7,7,7), l(Z1) = 1", (7, 7, 7, 7)), ("level-2 root (4,4,4,4)", (4, 4, 4, 4))]:
        site = tuple((Z[i] + (1, 0, 0, 0)[i]) % ch.S[0] for i in range(4))
        Y, rY, it = response(ch, site)
        Yc, rc, itc = tl.coulomb0(Y)
        print(f"  E2 k=2 T=2, {name}, p at Z + (1,0,0,0): CG res {rY:.0e}, C0 res {rc:.0e} {stamp()}", flush=True)
        report(tl, "CG", Y, Z); report(tl, "C0", Yc, Z)
        del Y, Yc


if __name__ == "__main__":
    {"E1": E1, "E2": E2}[sys.argv[1]]()
