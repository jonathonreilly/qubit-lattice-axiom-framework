# og55_1_route.py -- exact check of OFFGLOB55 §3.2 Lemma HR_U and §3.4 Proposition LOC-cc_U.
# Criteria: checks/og55_1_criteria.md (written before this script). Exact Fractions only; no floats; writes only stdout.
import itertools, random, sys
from fractions import Fraction as F

def mat_mul(a, b):
    return tuple(tuple(sum(a[i][t]*b[t][j] for t in range(3)) for j in range(3)) for i in range(3))
def mat_T(a):
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))
def mat_vec(a, v):
    return tuple(sum(a[i][t]*v[t] for t in range(3)) for i in range(3))
def vadd(u, v): return (u[0]+v[0], u[1]+v[1], u[2]+v[2])
def vsub(u, v): return (u[0]-v[0], u[1]-v[1], u[2]-v[2])
def vneg(u): return (-u[0], -u[1], -u[2])
def vsc(c, u): return (c*u[0], c*u[1], c*u[2])
def dot(u, v): return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
ZERO = (F(0), F(0), F(0))
I3 = ((F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1)))
def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1]) - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
def inv3(m):
    dt = det3(m); assert dt != 0
    c = [[None]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            r = [x for x in range(3) if x != i]; s = [y for y in range(3) if y != j]
            minor = m[r[0]][s[0]]*m[r[1]][s[1]] - m[r[0]][s[1]]*m[r[1]][s[0]]
            c[i][j] = ((-1)**(i+j))*minor
    return tuple(tuple(c[j][i]/dt for j in range(3)) for i in range(3))
def cayley(w):
    a, b, c = w
    W = ((F(0), -c, b), (c, F(0), -a), (-b, a, F(0)))
    Ip = tuple(tuple(I3[i][j] + W[i][j] for j in range(3)) for i in range(3))
    Im = tuple(tuple(I3[i][j] - W[i][j] for j in range(3)) for i in range(3))
    R = mat_mul(inv3(Im), Ip)
    assert mat_mul(mat_T(R), R) == I3 and det3(R) == 1
    return R
def rand_rot(rng):
    return cayley(tuple(F(rng.randint(-3, 3), rng.randint(1, 3)) for _ in range(3)))
def rand_vec(rng):
    return tuple(F(rng.randint(-5, 5), rng.randint(1, 4)) for _ in range(3))

class Model:
    def __init__(self, d, L, k, T):
        self.d, self.L, self.k, self.T = d, L, k, T
        self.n = T * L**k
        self.sites = list(itertools.product(range(self.n), repeat=d))
    def c(self, l):
        return (self.L**l - 1)//2
    def is_site(self, l, y):
        return all(yi % self.L**l == self.c(l) for yi in y)
    def lsites(self, l):
        return [y for y in self.sites if self.is_site(l, y)]
    def shift(self, y, mu, s):
        z = list(y); z[mu] = (z[mu] + s) % self.n; return tuple(z)
    def links(self, l):
        return [(l, y, mu) for y in self.lsites(l) for mu in range(self.d)]
    def all_links(self):
        out = []
        for l in range(self.k): out += self.links(l)
        return out
    def end(self, b):
        l, y, mu = b; return self.shift(y, mu, self.L**l)
    def root_of(self, j, Z):
        # root (level-(j+1) site) of the level-(j+1) block containing the level-j site Z
        B = self.L**(j+1)
        return tuple((zi // B)*B + self.c(j+1) for zi in Z)
    def path(self, j, Z):
        # level-j axial path from R(Z) to Z: coordinate 0 first, then 1, ...; steps (x_from, x_to, link, sign)
        R = self.root_of(j, Z); x = list(R); steps = []; h = self.L**j
        for mu in range(self.d):
            diff = Z[mu] - R[mu]
            assert diff % h == 0 and abs(diff) <= (self.L - 1)//2 * h
            sgn = 1 if diff > 0 else -1
            for _ in range(abs(diff)//h):
                xf = tuple(x); x[mu] = x[mu] + sgn*h; xt = tuple(x)
                if sgn == 1: steps.append((xf, xt, (j, xf, mu), 1))
                else:        steps.append((xf, xt, (j, xt, mu), -1))
        assert tuple(x) == Z
        return R, steps
    def roots(self):
        return set(self.lsites(self.k))

def D_U(M, U, S):
    D = {z: ZERO for z in M.sites}
    for b, v in S.items():
        y = b[1]; yp = M.end(b)
        D[yp] = vadd(D[yp], mat_vec(mat_T(U[b]), v))
        D[y] = vsub(D[y], v)
    return D
def Xi_U(M, U, lam):
    return {b: vsub(mat_vec(U[b], lam[M.end(b)]), lam[b[1]]) for b in M.all_links()}
def pair(S, X):
    return sum((dot(S[b], X[b]) for b in S if b in X), F(0))
def pair_fn(Dv, lam):
    return sum((dot(Dv[z], lam[z]) for z in Dv), F(0))

def route(M, U, u, wrong_back_sign=False, wrong_side=False, flat=False):
    # returns (S = P_U^T u as dict link -> vec, Vk = dict root -> vec)
    S = {b: ZERO for b in M.all_links()}
    V = dict(u)  # level-0 charges
    for j in range(M.k):
        Vn = {}
        for Z in M.lsites(j):
            R, steps = M.path(j, Z)
            us = []
            for (xf, xt, b, sg) in steps:
                Ub = I3 if flat else U[b]
                us.append(Ub if sg == 1 else mat_T(Ub))
            # T_{U,i} = u_i ... u_m
            m = len(us); Ts = [None]*m; acc = I3
            for i in range(m-1, -1, -1):
                acc = mat_mul(us[i], acc); Ts[i] = acc
            for i, (xf, xt, b, sg) in enumerate(steps):
                Ji = mat_vec(Ts[i], V[Z])
                if sg == 1: S[b] = vadd(S[b], Ji)
                else:
                    Ub = I3 if flat else U[b]
                    cur = mat_vec(Ub, Ji)
                    S[b] = vadd(S[b], cur) if wrong_back_sign else vsub(S[b], cur)
            Tfull = Ts[0] if m > 0 else I3
            if wrong_side: Tfull = mat_T(Tfull)
            Vn[R] = vadd(Vn.get(R, ZERO), mat_vec(Tfull, V[Z]))
        V = Vn
    return S, V

def perp(M, D):
    rts = M.roots(); return {z: (ZERO if z in rts else D[z]) for z in D}
def P_cc(M, U, Sp):
    q = perp(M, D_U(M, U, Sp)); corr, _ = route(M, U, q)
    return {b: vsub(Sp[b], corr[b]) for b in Sp}
def is_zero_fn(D): return all(v == ZERO for v in D.values())
def eq_chain(A, B): return all(A[b] == B[b] for b in A)

def midpoint(M, b):
    l, y, mu = b; m = [F(yi) for yi in y]; m[mu] += F(M.L**l, 2); return m
def partition(M):
    chis = []
    for b in M.all_links():
        m = midpoint(M, b)
        w = [1 + m[0], 1 + m[-1], F(2)]
        s = sum(w); chis.append((b, [wi/s for wi in w]))
    return {b: c for b, c in chis}

def run(name, d, L, k, T, seed, results):
    rng = random.Random(seed)
    M = Model(d, L, k, T)
    links = M.all_links()
    U = {b: rand_rot(rng) for b in links}
    def rec(tag, ok, ctl=False):
        results.append((name, tag, ok, ctl))
        print(f"{name} {tag}: {'PASS' if ok and not ctl else ('FIRES' if (ctl and ok) else ('FAIL' if not ctl else 'DOES-NOT-FIRE'))}")
    # A0 adjointness
    ok = True
    for _ in range(3):
        S = {b: rand_vec(rng) for b in links}; lam = {z: rand_vec(rng) for z in M.sites}
        ok &= pair(S, Xi_U(M, U, lam)) == pair_fn(D_U(M, U, S), lam)
    rec("A0 adjointness", ok)
    # A1 identity
    rts = M.roots(); ok = True
    for _ in range(3):
        u = {z: rand_vec(rng) for z in M.sites}
        S, Vk = route(M, U, u); D = D_U(M, U, S)
        for z in M.sites:
            expect = vsub(u[z], Vk.get(z, ZERO)) if z in rts else u[z]
            if D[z] != expect: ok = False
        assert set(Vk.keys()) == rts
    rec("A1 D_U(P_U^T u) = u - sum V_k delta_root", ok)
    # A2 covariance
    g = {z: rand_rot(rng) for z in M.sites}
    Ug = {b: mat_mul(mat_mul(g[b[1]], U[b]), mat_T(g[M.end(b)])) for b in links}
    ok = True
    for _ in range(2):
        u = {z: rand_vec(rng) for z in M.sites}
        S, _ = route(M, U, u)
        Sg, _ = route(M, Ug, {z: mat_vec(g[z], u[z]) for z in M.sites})
        for b in links:
            if Sg[b] != mat_vec(g[b[1]], S[b]): ok = False
    rec("A2 covariance P_{U^g}^T(Ad_g u) = M_g P_U^T u", ok)
    # A3, A4 local decomposition
    S_raw = {b: rand_vec(rng) for b in links}
    S = P_cc(M, U, S_raw)
    ccS = is_zero_fn(perp(M, D_U(M, U, S)))
    chi = partition(M); npc = 3
    pieces = [P_cc(M, U, {b: vsc(chi[b][a], S[b]) for b in links}) for a in range(npc)]
    tot = {b: ZERO for b in links}
    for p in pieces:
        for b in links: tot[b] = vadd(tot[b], p[b])
    rec("A3 S cc_U and sum of pieces = S", ccS and eq_chain(tot, S))
    rec("A4 every piece cc_U", all(is_zero_fn(perp(M, D_U(M, U, p))) for p in pieces))
    # A5 flat limit vs HR's flat formula
    Uone = {b: I3 for b in links}
    u = {z: rand_vec(rng) for z in M.sites}
    S1, _ = route(M, Uone, u)
    Sflat = {b: ZERO for b in links}; V = dict(u)
    for j in range(M.k):
        Vn = {}
        for Z in M.lsites(j):
            R, steps = M.path(j, Z)
            for (xf, xt, b, sg) in steps:
                Sflat[b] = vadd(Sflat[b], vsc(sg, V[Z]))
            Vn[R] = vadd(Vn.get(R, ZERO), V[Z])
        V = Vn
    rec("A5 flat limit = HR flat formula", eq_chain(S1, Sflat))
    # Controls
    # C1 flat routing at curved U leaves a piece not cc_U
    fired = False
    for a in range(npc):
        Sp = {b: vsc(chi[b][a], S[b]) for b in links}
        q = perp(M, D_U(M, U, Sp)); corr, _ = route(M, U, q, flat=True)
        pc = {b: vsub(Sp[b], corr[b]) for b in links}
        if not is_zero_fn(perp(M, D_U(M, U, pc))): fired = True
    rec("C1 flat routing at curved U: piece not cc_U", fired, ctl=True)
    # C2
    u = {z: rand_vec(rng) for z in M.sites}
    S2, _ = route(M, U, u, flat=True); D2 = perp(M, D_U(M, U, S2))
    rec("C2 D_U^perp(P_1^T u) != u^perp at curved U", any(D2[z] != u[z] for z in M.sites if z not in rts), ctl=True)
    # C3 non-cc source
    bad = {b: rand_vec(rng) for b in links}
    tot = {b: ZERO for b in links}
    for a in range(npc):
        p = P_cc(M, U, {b: vsc(chi[b][a], bad[b]) for b in links})
        for b in links: tot[b] = vadd(tot[b], p[b])
    rec("C3 non-cc source: sum of pieces != source", not eq_chain(tot, bad), ctl=True)
    # C4 wrong backward sign
    u = {z: rand_vec(rng) for z in M.sites}
    S4, Vk4 = route(M, U, u, wrong_back_sign=True); D4 = D_U(M, U, S4)
    rec("C4 wrong backward sign breaks A1", any(D4[z] != u[z] for z in M.sites if z not in rts), ctl=True)
    # C5 wrong side
    S5, Vk5 = route(M, U, u, wrong_side=True); D5 = D_U(M, U, S5)
    rec("C5 wrong-side transport breaks A1", any(D5[z] != u[z] for z in M.sites if z not in rts), ctl=True)

def main():
    results = []
    models = [("M1", 2, 3, 2, 1, 101), ("M2", 2, 3, 2, 2, 202), ("M3", 2, 3, 3, 1, 303), ("M4", 3, 3, 2, 1, 404)]
    for (name, d, L, k, T, seed) in models:
        print(f"== {name}: d={d} L={L} k={k} T={T} seed={seed}"); sys.stdout.flush()
        run(name, d, L, k, T, seed, results)
    npass = sum(1 for r in results if not r[3] and r[2]); nfail = sum(1 for r in results if not r[3] and not r[2])
    nfire = sum(1 for r in results if r[3] and r[2]); nnot = sum(1 for r in results if r[3] and not r[2])
    print(f"SUMMARY: A-items PASS {npass}, FAIL {nfail}; controls FIRE {nfire}, DO-NOT-FIRE {nnot}")
    print("OVERALL", "PASS" if (nfail == 0 and nnot == 0) else "FAIL")
main()
