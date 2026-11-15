# al55_hcg.py -- exact check of Lemma HC-1 (hierarchical Coulomb-detail gauge), ALIGN55.md section 5.4.
# Criteria: checks/al55_hcg_criteria.md (written first). Fractions/ints only. stdout only. One real component (d = 2).
from fractions import Fraction as F
import random

random.seed(5502)
results = []
def rep(name, ok, info=""):
    results.append((name, ok)); print(("PASS " if ok else "FAIL ") + name + ((" | " + info) if info else ""))
def ctl(name, fired, info=""):
    results.append((name, fired)); print(("CONTROL FIRES " if fired else "CONTROL DOES NOT FIRE ") + name + ((" | " + info) if info else ""))

# ---------- 1D masks (centred at the coarse point; fine index 1 + n <- coarse j via a_{n - 3j}) ----------
A_DD = {e: F(v, 81) for e, v in zip(range(-5, 6), (-4, -5, 0, 30, 60, 81, 60, 30, 0, -5, -4)) if v != 0}
A_BS = {e: F(v, 9) for e, v in zip(range(-3, 4), (1, 3, 6, 7, 6, 3, 1))}   # ternary cubic B-spline (non-interpolatory)
def lmul(p, q):
    r = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            r[e1 + e2] = r.get(e1 + e2, F(0)) + c1 * c2
    return {e: c for e, c in r.items() if c != 0}
def ldiv_sigma3(p):
    lo = min(p); hi = max(p)
    P = [p.get(lo + i, F(0)) for i in range(hi - lo + 1)]
    Q = [F(0)] * max(0, len(P) - 2)
    for k in range(len(P) - 1, 1, -1):
        c = P[k]
        if c != 0:
            Q[k - 2] = c
            for t in range(3): P[k - t] -= c
    assert all(v == 0 for v in P), "sigma_3 does not divide"
    return {lo + i: c for i, c in enumerate(Q) if c != 0}
def derived(a):   # a1 = z^2 a / sigma_3
    return ldiv_sigma3({e + 2: c for e, c in a.items()})

class Model:
    def __init__(self, T, k, mask=A_DD, dmask=None):
        self.T, self.k = T, k
        self.M = {l: T * 3 ** (k - l) for l in range(k + 1)}      # level-l torus side (level-l index units)
        self.a = mask
        self.a1 = derived(mask) if dmask is None else dmask
        self.fac = {}
    # functions at level l: dict (i, j) -> F ; 1-forms: dict (i, j, mu) -> F
    def sites(self, l): return [(i, j) for i in range(self.M[l]) for j in range(self.M[l])]
    def links(self, l): return [(i, j, mu) for i in range(self.M[l]) for j in range(self.M[l]) for mu in (0, 1)]
    def nb(self, l, y, mu, s=1):
        M = self.M[l]; z = list(y); z[mu] = (z[mu] + s) % M; return tuple(z)
    def d(self, l, f):
        return {(i, j, mu): f[self.nb(l, (i, j), mu)] - f[(i, j)] for (i, j, mu) in self.links(l)}
    def dstar(self, l, w):
        g = {y: F(0) for y in self.sites(l)}
        for (i, j, mu), v in w.items():
            g[self.nb(l, (i, j), mu)] += v; g[(i, j)] -= v
        return g      # d^* = adjoint of d: (d^* w)(y) = sum_mu [w(y - e) - w(y)] (pre-run fix: no extra sign)
    def R(self, l, f):                              # level l -> l+1 restriction (coarse J at fine 1 + 3J)
        M1 = self.M[l + 1]; Ml = self.M[l]
        return {(I, J): f[((1 + 3 * I) % Ml, (1 + 3 * J) % Ml)] for I in range(M1) for J in range(M1)}
    def RT(self, l, c):                             # level l+1 -> l placement
        Ml = self.M[l]; f = {y: F(0) for y in self.sites(l)}
        for (I, J), v in c.items(): f[((1 + 3 * I) % Ml, (1 + 3 * J) % Ml)] += v
        return f
    def w1d(self, mask, n_fine, M_fine, M_coarse):
        """weights (coarse j, coeff) for fine index i = 1 + n (mod M_fine)"""
        n = (n_fine - 1) % M_fine
        out = {}
        for e, c in mask.items():
            # n - 3j = e  -> j = (n - e)/3 (mod M_coarse); each mask entry counted once (pre-run fix)
            if (n - e) % 3 == 0:
                j = ((n - e) // 3) % M_coarse
                out[j] = out.get(j, F(0)) + c
        return out
    def W(self, l, mask):
        key = (l, tuple(sorted(mask.items())))
        if key not in self.fac:
            Ml, M1 = self.M[l], self.M[l + 1]
            self.fac[key] = [self.w1d(mask, i, Ml, M1) for i in range(Ml)]
        return self.fac[key]
    def S0(self, l, c):                             # level l+1 -> l
        Wt = self.W(l, self.a); Ml = self.M[l]
        f = {}
        for i in range(Ml):
            for j in range(Ml):
                s = F(0)
                for I, wi in Wt[i].items():
                    for J, wj in Wt[j].items():
                        s += wi * wj * c[(I, J)]
                f[(i, j)] = s
        return f
    def S0T(self, l, f):                            # level l -> l+1
        Wt = self.W(l, self.a); M1 = self.M[l + 1]
        c = {(I, J): F(0) for I in range(M1) for J in range(M1)}
        for (i, j), v in f.items():
            if v == 0: continue
            for I, wi in Wt[i].items():
                for J, wj in Wt[j].items():
                    c[(I, J)] += wi * wj * v
        return c
    def S1(self, l, w):                             # coarse 1-forms (level l+1) -> fine 1-forms (level l)
        Wt = self.W(l, self.a); Wd = self.W(l, self.a1); Ml = self.M[l]
        out = {}
        for i in range(Ml):
            for j in range(Ml):
                s0 = F(0); s1 = F(0)
                for I, wi in Wd[i].items():
                    for J, wj in Wt[j].items(): s0 += wi * wj * w[(I, J, 0)]
                for I, wi in Wt[i].items():
                    for J, wj in Wd[j].items(): s1 += wi * wj * w[(I, J, 1)]
                out[(i, j, 0)] = s0; out[(i, j, 1)] = s1
        return out
    # exact Laplacian solve on the level-l torus (pin site (0,0)), mean-zero output
    def factor(self, l):
        if ('lap', l) in self.fac: return self.fac[('lap', l)]
        M = self.M[l]; n = M * M
        idx = lambda i, j: (i % M) * M + (j % M)
        A = []
        for i in range(M):
            for j in range(M):
                r = {}
                k0 = idx(i, j); r[k0] = r.get(k0, F(0)) + 4
                for (a, b) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    kk = idx(i + a, j + b); r[kk] = r.get(kk, F(0)) - 1
                A.append(r)
        if n == 1:
            self.fac[('lap', l)] = None; return None
        A = [{c - 1: v for c, v in A[k].items() if c != 0 and v != 0} for k in range(1, n)]
        m = n - 1; ops = []
        for p in range(m):
            piv = A[p][p]; rowp = A[p]
            for q in range(p + 1, m):
                v = A[q].get(p)
                if v is None or v == 0: continue
                f = v / piv; ops.append((q, p, f)); rq = A[q]
                for c, x in rowp.items():
                    if c >= p:
                        nv = rq.get(c, F(0)) - f * x
                        if nv == 0: rq.pop(c, None)
                        else: rq[c] = nv
        self.fac[('lap', l)] = (A, ops, m, idx, M)
        return self.fac[('lap', l)]
    def lapinv(self, l, g):
        tot = sum(g.values(), F(0)); assert tot == 0, "Delta^{-1} needs mean zero"
        fa = self.factor(l)
        if fa is None: return {y: F(0) for y in g}
        A, ops, m, idx, M = fa
        b = [F(0)] * m
        for (i, j), v in g.items():
            k0 = idx(i, j)
            if k0 != 0: b[k0 - 1] = v
        for (q, p, f) in ops: b[q] -= f * b[p]
        x = [F(0)] * m
        for p in range(m - 1, -1, -1):
            s = b[p] - sum((v * x[c] for c, v in A[p].items() if c > p), F(0))
            x[p] = s / A[p][p]
        u = {(i, j): (x[idx(i, j) - 1] if idx(i, j) != 0 else F(0)) for i in range(M) for j in range(M)}
        mean = sum(u.values(), F(0)) / (M * M)
        return {y: v - mean for y, v in u.items()}
    # position of level-l index in level-0 index units
    def pos(self, l, y):
        off = sum(3 ** i for i in range(l))     # OFF_l = 1 + 3 + ... + 3^{l-1}
        return ((off + 3 ** l * y[0]) % self.M[0], (off + 3 ** l * y[1]) % self.M[0])
    def ev(self, l, f0):
        return {y: f0[self.pos(l, y)] for y in self.sites(l)}
    def Xi1(self, nu):
        return {l: self.d(l, self.ev(l, nu)) for l in range(self.k)}
    def roots(self):
        return set(self.pos(self.k, y) for y in self.sites(self.k))
    def rand_Lambda0(self):
        nu = {y: F(random.randint(-6, 6)) for y in self.sites(0)}
        for r in self.roots(): nu[r] = F(0)
        return nu
    def rand_chain(self):
        return {l: {b: F(random.randint(-6, 6)) for b in self.links(l)} for l in range(self.k)}
    # Lambda_HC and variants
    def Lam(self, x, detail=True, inherit=True, return_levels=False):
        lam = {self.k: {y: F(0) for y in self.sites(self.k)}}
        for l in range(self.k - 1, -1, -1):
            u = self.lapinv(l, self.dstar(l, x[l]))
            if detail:
                SR = self.S0(l, self.R(l, u))
                mu = {y: -(u[y] - SR[y]) for y in u}
            else:
                mu = {y: -u[y] for y in u}
            if inherit:
                Sl = self.S0(l, lam[l + 1])
                lam[l] = {y: Sl[y] + mu[y] for y in u}
            else:
                lam[l] = mu
        return lam if return_levels else lam[0]

def neg(f): return {y: -v for y, v in f.items()}
def pair(a, b): return sum((a[k] * b[k] for k in a), F(0))

# ================= Model MA =================
MA = Model(T=2, k=2)
ok1 = True
for _ in range(3):
    nu = MA.rand_Lambda0(); ok1 = ok1 and (MA.Lam(MA.Xi1(nu)) == neg(nu))
rep("H1(MA) Lambda_HC Xi_1 nu = -nu (3 random nu)", ok1)
ok2 = True
for _ in range(2):
    x = MA.rand_chain(); lv = MA.Lam(x, return_levels=True)
    for l in range(MA.k + 1):
        ok2 = ok2 and (MA.ev(l, lv[0]) == lv[l])
rep("H2(MA) ev^(l) Lambda_HC x = lambda_l, all l (2 random chains)", ok2)
# H7: R S0 = 1, constants, polynomial reproduction (1D infinite-line proxy)
c1 = {(I, J): F(random.randint(-5, 5)) for I in range(MA.M[1]) for J in range(MA.M[1])}
okR = MA.R(0, MA.S0(0, c1)) == c1
const = MA.S0(0, {(I, J): F(1) for I in range(MA.M[1]) for J in range(MA.M[1])})
okC = all(v == 1 for v in const.values())
def s1d(mask, cfun, n):   # fine index 1+n on the infinite line
    return sum((c * cfun((n - e) // 3) for e, c in mask.items() if (n - e) % 3 == 0), F(0))
okP = True
for p in (1, 2, 3):
    for n in range(-12, 13):
        okP = okP and (s1d(A_DD, lambda j: F(j) ** p, n) == (F(n, 3)) ** p)
rep("H7 R S_0 = 1, constants reproduced, j, j^2, j^3 reproduced (1D)", okR and okC and okP)
# H8 commuting pair on MA levels 1->0 and 2->1
ok8 = True
for l in (0, 1):
    c = {(I, J): F(random.randint(-5, 5)) for I in range(MA.M[l + 1]) for J in range(MA.M[l + 1])}
    ok8 = ok8 and (MA.d(l, MA.S0(l, c)) == MA.S1(l, MA.d(l + 1, c)))
rep("H8 d S_0 = S_1 d (commuting pair), MA levels 1->0 and 2->1", ok8)

# ================= Model MB =================
MB = Model(T=1, k=3)
ok1b = True
for _ in range(3):
    nu = MB.rand_Lambda0(); ok1b = ok1b and (MB.Lam(MB.Xi1(nu)) == neg(nu))
rep("H1(MB) Lambda_HC Xi_1 nu = -nu (3 random nu)", ok1b)
ok2b = True
xs = [MB.rand_chain() for _ in range(2)]
for x in xs:
    lv = MB.Lam(x, return_levels=True)
    for l in range(MB.k + 1):
        ok2b = ok2b and (MB.ev(l, lv[0]) == lv[l])
rep("H2(MB) ev^(l) Lambda_HC x = lambda_l, all l (2 random chains)", ok2b)
x = xs[0]; base = MB.Lam(x, return_levels=True)
ok3 = True
for l in range(1, MB.k):
    for m in range(l):
        xm = {lev: dict(f) for lev, f in x.items()}
        for b in xm[m]: xm[m][b] += F(random.randint(-3, 3))
        ok3 = ok3 and (MB.Lam(xm, return_levels=True)[l] == base[l])
    xl = {lev: dict(f) for lev, f in x.items()}
    for b in xl[l]: xl[l][b] += F(random.randint(1, 3))
    ok3 = ok3 and (MB.Lam(xl, return_levels=True)[l] != base[l])
rep("H3(MB) lambda_l independent of x_m (m < l), dependent on x_l", ok3)
# H4: x^phi at a level-1 non-root site
y0_1 = (1, 0); y0 = MB.pos(1, y0_1)
assert y0 not in MB.roots()
phi = {y: F(0) for y in MB.sites(0)}; phi[y0] = F(1)
xphi = {0: MB.d(0, phi)}; xphi.update({l: {b: F(0) for b in MB.links(l)} for l in range(1, MB.k)})
lphi = MB.Lam(xphi)
rep("H4(MB) Lambda_HC x^phi vanishes on level-1 sites", all(v == 0 for v in MB.ev(1, lphi).values()),
    "level-0 value at y0 = %s" % lphi[y0])
# H5: transpose formula
def transpose_formula(Mo, q, omit_S=False):
    cs = {}
    for m in range(Mo.k):
        if omit_S:
            p = Mo.ev(m, q) if m > 0 else dict(q)
        else:
            p = dict(q)
            for i in range(m): p = Mo.S0T(i, p)
        w = {y: p[y] - v for y, v in Mo.RT(m, Mo.S0T(m, p)).items()}
        cs[m] = {b: -v for b, v in Mo.d(m, Mo.lapinv(m, w)).items()}
    return cs
ok5 = True; zero_ok = True; k4fired = False
for l in range(MB.k):
    q = {y: F(0) for y in MB.sites(0)}
    for y in MB.sites(l): q[MB.pos(l, y)] = F(random.randint(-4, 4))
    xr = MB.rand_chain()
    lhs = pair(q, MB.Lam(xr))
    cs = transpose_formula(MB, q)
    rhs = sum((pair(cs[m], xr[m]) for m in range(MB.k)), F(0))
    ok5 = ok5 and (lhs == rhs)
    for m in range(l):
        zero_ok = zero_ok and all(v == 0 for v in cs[m].values())
    if l == 0:
        cs2 = transpose_formula(MB, q, omit_S=True)
        rhs2 = sum((pair(cs2[m], xr[m]) for m in range(MB.k)), F(0))
        k4fired = (rhs2 != lhs)
rep("H5(MB) <q, Lambda_HC x> = sum_m <c_m, x_m>, and c_m = 0 for m < l (q on level-l sites, l = 0, 1, 2)", ok5 and zero_ok)
# H6: homogeneous step
ok6 = True
for l in range(MB.k):
    xz = {lev: dict(f) for lev, f in xs[1].items()}
    xz[l] = {b: F(0) for b in MB.links(l)}
    lv = MB.Lam(xz, return_levels=True)
    ok6 = ok6 and (lv[l] == MB.S0(l, lv[l + 1]))
rep("H6(MB) x_l = 0 gives lambda_l = S_0 lambda_{l+1}", ok6)

# ================= controls =================
xc = MA.rand_chain(); lvc = MA.Lam(xc, detail=False, return_levels=True)
ctl("K1 without the detail projection, nested restriction fails", any(MA.R(l, lvc[l]) != lvc[l + 1] for l in range(MA.k)))
MBS = Model(T=2, k=2, mask=A_BS, dmask=derived(A_BS))
nu = MBS.rand_Lambda0(); okK2a = MBS.Lam(MBS.Xi1(nu)) == neg(nu)
lvK = MBS.Lam(MBS.rand_chain(), return_levels=True)
okK2b = all(MBS.ev(l, lvK[0]) == lvK[l] for l in range(MBS.k + 1))
ctl("K2 non-interpolatory S_0 (cubic B-spline) breaks H1 or H2", (not okK2a) or (not okK2b), "H1 ok=%s, H2 ok=%s" % (okK2a, okK2b))
nu = MA.rand_Lambda0()
ctl("K3 dropping S_0 lambda_{l+1} breaks H1", MA.Lam(MA.Xi1(nu), inherit=False) != neg(nu))
ctl("K4 omitting S^(m->0)T in the transpose formula breaks H5 (q on level-0 sites)", k4fired)
MW = Model(T=2, k=2, dmask=dict(A_DD))
c = {(I, J): F(random.randint(-5, 5)) for I in range(MW.M[1]) for J in range(MW.M[1])}
ctl("K5 underived link scheme (s^[1] := s) breaks H8", MW.d(0, MW.S0(0, c)) != MW.S1(0, MW.d(1, c)))

print("SUMMARY: %d items, all ok = %s" % (len(results), all(ok for _, ok in results)))
