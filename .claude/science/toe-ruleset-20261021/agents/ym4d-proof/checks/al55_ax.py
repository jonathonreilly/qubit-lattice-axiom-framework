# al55_ax.py -- multiscale axial-in-blocks gauge: seam identity and seam growth (ALIGN55.md section 5.2, Prop. AX-SEAM).
# Criteria: checks/al55_ax_criteria.md (+ Amendment A1, written before this script). Fractions/ints only. stdout only.
from fractions import Fraction as F
import random

random.seed(5503)
results = []
def rep_(name, ok, info=""):
    results.append((name, ok)); print(("PASS " if ok else "FAIL ") + name + ((" | " + info) if info else ""))
def ctl(name, fired, info=""):
    results.append((name, fired)); print(("CONTROL FIRES " if fired else "CONTROL DOES NOT FIRE ") + name + ((" | " + info) if info else ""))

class Ax:
    def __init__(self, k, T=1):
        self.k, self.T = k, T
        self.M = {l: T * 3 ** (k - l) for l in range(k + 1)}
        self.N0 = self.M[0]
    def off(self, l): return (3 ** l - 1) // 2
    def pos(self, l, i): return ((self.off(l) + 3 ** l * i[0]) % self.N0, (self.off(l) + 3 ** l * i[1]) % self.N0)
    def sites(self, l): return [(a, b) for a in range(self.M[l]) for b in range(self.M[l])]
    def links(self, l): return [(a, b, mu) for a in range(self.M[l]) for b in range(self.M[l]) for mu in (0, 1)]
    def nb(self, l, i, mu, s=1):
        z = list(i); z[mu] = (z[mu] + s) % self.M[l]; return tuple(z)
    def step(self, x_l, l, q, mu, s):           # integral of x_l along one level-l step from q
        if s == 1: return x_l[(q[0], q[1], mu)]
        p = self.nb(l, q, mu, -1); return -x_l[(p[0], p[1], mu)]
    def axial(self, x_l, l, P, delta, order):  # integral from P by delta (entries in {-1,0,1}) in the given axis order
        tot = F(0); q = P
        for mu in order:
            s = delta[mu]
            if s != 0:
                tot += self.step(x_l, l, q, mu, s); q = self.nb(l, q, mu, s)
        return tot
    def tau(self, x_l, l, P, delta, orders=((0, 1), (1, 0))):
        return sum((self.axial(x_l, l, P, delta, o) for o in orders), F(0)) / len(orders)
    def parent(self, i): return (i[0] // 3, i[1] // 3)
    def Lam(self, x, orders=((0, 1), (1, 0)), levels=False):
        lam = {self.k: {i: F(0) for i in self.sites(self.k)}}
        for l in range(self.k - 1, -1, -1):
            lam[l] = {}
            for i in self.sites(l):
                J = self.parent(i); P = (1 + 3 * J[0], 1 + 3 * J[1])
                delta = (i[0] - P[0], i[1] - P[1])
                lam[l][i] = lam[l + 1][J] - self.tau(x[l], l, P, delta, orders)
        return lam if levels else lam[0]
    def d(self, l, f): return {(a, b, mu): f[self.nb(l, (a, b), mu)] - f[(a, b)] for (a, b, mu) in self.links(l)}
    def ev(self, l, f0):
        idx = {self.pos(0, i): i for i in self.sites(0)}
        return {i: f0[idx[self.pos(l, i)]] for i in self.sites(l)}
    def Xi1(self, nu): return {l: self.d(l, self.ev(l, nu)) for l in range(self.k)}
    def root_idx0(self):
        idx = {self.pos(0, i): i for i in self.sites(0)}
        return set(idx[self.pos(self.k, j)] for j in self.sites(self.k))
    def rand_Lambda0(self):
        nu = {i: F(random.randint(-5, 5)) for i in self.sites(0)}
        for r in self.root_idx0(): nu[r] = F(0)
        return nu
    def curvature_chain(self, Fc=F(1)):
        C = (self.N0 - 1) // 2                  # centre (level-k root position), T = 1
        x = {}
        for l in range(self.k):
            rho_l = F(3 ** l, 3 ** self.k)
            xl = {}
            for (a, b, mu) in self.links(l):
                p = self.pos(l, (a, b))
                if mu == 0: xl[(a, b, mu)] = F(0)
                else:
                    pc = p[0] if p[0] <= C + (self.N0 - 1) // 2 else p[0] - self.N0
                    u0 = F(pc - C, 3 ** self.k)
                    xl[(a, b, mu)] = Fc * u0 * rho_l
            x[l] = xl
        return x
    def hier_loop(self, x, y, yp, orders=((0, 1), (1, 0))):
        """independent loop sum: Phi_0(y) - Phi_0(y') + x_0(y -> y'), Phi = hierarchical path integral (explicit walk)"""
        def Phi(i0):
            tot = F(0); i = i0
            for l in range(0, self.k):
                J = self.parent(i); P = (1 + 3 * J[0], 1 + 3 * J[1])
                delta = (i[0] - P[0], i[1] - P[1])
                walks = []
                for o in orders:
                    q = P; s_ = F(0)
                    for mu in o:
                        if delta[mu] != 0:
                            s_ += self.step(x[l], l, q, mu, delta[mu]); q = self.nb(l, q, mu, delta[mu])
                    walks.append(s_)
                tot += sum(walks, F(0)) / len(walks)
                i = J
            return tot
        return Phi(y) + x[0][(y[0], y[1], 0)] - Phi(yp)

def seam_link(A):
    k = A.k; C = (A.N0 - 1) // 2; h = (3 ** (k - 2) - 1) // 2
    y = (C + h, C + h); yp = (C + h + 1, C + h)
    return y, yp

vals = {}
xc_fire = False
for k in (2, 3, 4):
    A = Ax(k)
    # X1
    ok1 = True
    for _ in range(2):
        nu = A.rand_Lambda0(); ok1 = ok1 and (A.Lam(A.Xi1(nu)) == {i: -v for i, v in nu.items()})
    xr = {l: {b: F(random.randint(-4, 4)) for b in A.links(l)} for l in range(k)}
    lv = A.Lam(xr, levels=True)
    xr2 = {l: dict(f) for l, f in xr.items()}
    for b in xr2[0]: xr2[0][b] += F(random.randint(-3, 3))
    ok1 = ok1 and (A.Lam(xr2, levels=True)[1] == lv[1])
    rep_("X1(k=%d) Lambda_ax left inverse; level-1 values independent of x_0" % k, ok1)
    # X2 identity on all level-0 links (mu = 0) for the curvature chain and a random chain
    ok2 = True
    for x in (A.curvature_chain(), xr):
        lam = A.Lam(x)
        for (a, b, mu) in A.links(0):
            if mu != 0: continue
            y = (a, b); yp = A.nb(0, y, 0)
            repv = x[0][(a, b, 0)] + lam[yp] - lam[y]
            ok2 = ok2 and (repv == A.hier_loop(x, y, yp))
    rep_("X2(k=%d) seam identity rep(b) = loop sum along the hierarchical paths (all axis-0 links, 2 chains)" % k, ok2)
    # X4 pure gauge
    nu = A.rand_Lambda0(); xg = A.Xi1(nu); lamg = A.Lam(xg)
    ok4 = all(xg[0][(a, b, mu)] + lamg[A.nb(0, (a, b), mu)] - lamg[(a, b)] == 0 for (a, b, mu) in A.links(0))
    rep_("X4(k=%d) pure-gauge chain: representative vanishes on every level-0 link" % k, ok4)
    # X3' values
    xcurv = A.curvature_chain(); lam = A.Lam(xcurv)
    y, yp = seam_link(A)
    repv = xcurv[0][(y[0], y[1], 0)] + lam[yp] - lam[y]
    repc = repv * 3 ** k                              # coarse units at level 0: own / rho_0
    vals[k] = repc
    print("INFO k=%d seam link %s->%s: rep_own = %s, rep^c = %s, rep^c / L^(k-3) = %s" % (k, y, yp, repv, repc, repc / F(3) ** (k - 3)))
    # XC1: order-(0,1)-only loop sum differs from the averaged one on at least one link
    if k >= 3:
        for (a, b, mu) in A.links(0):
            if mu != 0: continue
            yy = (a, b); yyp = A.nb(0, yy, 0)
            if A.hier_loop(xcurv, yy, yyp, orders=((0, 1),)) != A.hier_loop(xcurv, yy, yyp):
                xc_fire = True; break

rep_("X3' |rep^c(k=4)| >= (L/2)|rep^c(k=3)| > 0", vals[3] != 0 and abs(vals[4]) >= F(3, 2) * abs(vals[3]),
     "rep^c(3) = %s, rep^c(4) = %s, ratio = %s" % (vals[3], vals[4], (vals[4] / vals[3]) if vals[3] != 0 else "n/a"))
ctl("XC1 order-(0,1)-only loop sum differs from the permutation-averaged one", xc_fire)
print("SUMMARY: %d items, all ok = %s" % (len(results), all(ok for _, ok in results)))
