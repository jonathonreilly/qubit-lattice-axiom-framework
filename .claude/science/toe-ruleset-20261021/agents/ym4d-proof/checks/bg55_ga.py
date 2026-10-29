# bg55_ga.py -- exact algebra check of BGT55 Theorem GA (gauge-aligned transfer). Criteria: checks/bg55_ga_criteria.md
# (written 2026-10-29T01:05Z, before this script). Exact integer / Fraction arithmetic only. No floats, no numpy.
import random, itertools, sys
from fractions import Fraction

D = 2; Lb = 3   # dimension, block factor

# ---------------- octahedral rotations (integer SO(3)) ----------------
def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1]) - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
OCT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        m = [[0]*3 for _ in range(3)]
        for i in range(3):
            m[i][perm[i]] = sg[i]
        if det3(m) == 1:
            OCT.append(tuple(tuple(r) for r in m))
assert len(OCT) == 24
I3 = ((1,0,0),(0,1,0),(0,0,1))
def mm(a, b):
    return tuple(tuple(sum(a[i][t]*b[t][j] for t in range(3)) for j in range(3)) for i in range(3))
def tr(a):
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))

# ---------------- sparse matrices: dict row -> dict col -> int ----------------
class SM:
    def __init__(self, nr, nc):
        self.nr, self.nc, self.r = nr, nc, {}
    def add(self, i, j, v):
        if v == 0: return
        row = self.r.setdefault(i, {})
        nv = row.get(j, 0) + v
        if nv == 0:
            del row[j]
            if not row: del self.r[i]
        else:
            row[j] = nv
    def T(self):
        out = SM(self.nc, self.nr)
        for i, row in self.r.items():
            for j, v in row.items():
                out.add(j, i, v)
        return out
    def mul(self, other):
        assert self.nc == other.nr
        out = SM(self.nr, other.nc)
        for i, row in self.r.items():
            acc = {}
            for t, v in row.items():
                orow = other.r.get(t)
                if orow:
                    for j, w in orow.items():
                        acc[j] = acc.get(j, 0) + v*w
            acc = {j: v for j, v in acc.items() if v != 0}
            if acc: out.r[i] = acc
        return out
    def plus(self, other, c=1):
        assert (self.nr, self.nc) == (other.nr, other.nc)
        out = SM(self.nr, self.nc)
        for i, row in self.r.items():
            for j, v in row.items(): out.add(i, j, v)
        for i, row in other.r.items():
            for j, v in row.items(): out.add(i, j, c*v)
        return out
    def scale(self, c):
        out = SM(self.nr, self.nc)
        for i, row in self.r.items():
            for j, v in row.items(): out.add(i, j, c*v)
        return out
    def vec(self, x):
        y = [0]*self.nr
        for i, row in self.r.items():
            y[i] = sum(v*x[j] for j, v in row.items())
        return y
    def iszero(self):
        return len(self.r) == 0
    def nnz(self):
        return sum(len(r) for r in self.r.values())
    def dense(self):
        m = [[0]*self.nc for _ in range(self.nr)]
        for i, row in self.r.items():
            for j, v in row.items(): m[i][j] = v
        return m
def eye(n):
    m = SM(n, n)
    for i in range(n): m.add(i, i, 1)
    return m

# ---------------- exact Bareiss elimination ----------------
def bareiss_rank(A):
    M = [row[:] for row in A]; n, m = len(M), len(M[0]); r = 0; prev = 1
    for c in range(m):
        piv = next((i for i in range(r, n) if M[i][c] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(r+1, n):
            if M[i][c] != 0 or True:
                Mi, Mr = M[i], M[r]
                a, b = Mr[c], Mi[c]
                for j in range(c+1, m):
                    Mi[j] = (Mi[j]*a - b*Mr[j]) // prev
                Mi[c] = 0
        prev = M[r][c]; r += 1
        if r == n: break
    return r
def solve_exact(A, Bcols):
    # A square n x n integer, nonsingular; Bcols: list of integer RHS vectors. Fraction-free forward, Fraction back-sub.
    n = len(A); k = len(Bcols)
    M = [A[i][:] + [b[i] for b in Bcols] for i in range(n)]
    prev = 1
    for c in range(n):
        piv = next((i for i in range(c, n) if M[i][c] != 0), None)
        if piv is None: raise ValueError("singular")
        M[c], M[piv] = M[piv], M[c]
        a = M[c][c]
        for i in range(c+1, n):
            Mi, Mc = M[i], M[c]; b = Mi[c]
            for j in range(c+1, n+k):
                Mi[j] = (Mi[j]*a - b*Mc[j]) // prev
            Mi[c] = 0
        prev = a
    sols = []
    for t in range(k):
        x = [Fraction(0)]*n
        for i in range(n-1, -1, -1):
            s = Fraction(M[i][n+t]) - sum(Fraction(M[i][j])*x[j] for j in range(i+1, n) if M[i][j] != 0)
            x[i] = s / M[i][i]
        sols.append(x)
    return sols

# ---------------- model ----------------
class Model:
    def __init__(self, k, Tc, kap):
        self.k, self.Tc, self.kap = k, Tc, kap
        self.S = [Tc*Lb**(k-l) for l in range(k+1)]
        self.nsite = [s**D for s in self.S]
        self.nlink = [D*s**D for s in self.S]
        self.off = [0]
        for l in range(k):
            self.off.append(self.off[-1] + 3*self.nlink[l])
        self.nX = self.off[k]
        roots_k = set(self.root0(k, X) for X in self.sites(k))
        self.roots_k = roots_k
        self.lam_sites = [s for s in self.sites(0) if s not in roots_k]
        self.lam_index = {s: i for i, s in enumerate(self.lam_sites)}
        self.nL = 3*len(self.lam_sites)
    def sites(self, l):
        S = self.S[l]
        return [(i, j) for i in range(S) for j in range(S)]
    def sidx(self, l, s):
        S = self.S[l]; return (s[0] % S)*S + (s[1] % S)
    def norm(self, l, s):
        S = self.S[l]; return (s[0] % S, s[1] % S)
    def lidx(self, l, s, mu):
        return self.off[l] + 3*(self.sidx(l, s)*D + mu) if l < self.k else None
    def rootdown(self, Y):
        return (Lb*Y[0] + (Lb-1)//2, Lb*Y[1] + (Lb-1)//2)
    def root0(self, l, Y):
        for _ in range(l): Y = self.rootdown(Y)
        return self.norm(0, Y)
    def rootat(self, l, Y):   # level-l root (site at level l) of level-(l+1) site Y
        return self.norm(l, self.rootdown(Y))
    def e(self, mu):
        return (1, 0) if mu == 0 else (0, 1)
    def add(self, s, v):
        return (s[0]+v[0], s[1]+v[1])

def build_ops(M, Z):
    """Z[l][(site,mu)] = 3x3 rotation for l < k. Returns dict of sparse operators."""
    k = M.k
    # Xi_Z : Lambda_0 -> X
    Xi = SM(M.nX, M.nL)
    for l in range(k):
        for Y in M.sites(l):
            for mu in range(D):
                Yp = M.norm(l, M.add(Y, M.e(mu)))
                R = Z[l][(Y, mu)]
                r0p, r0 = M.root0(l, Yp), M.root0(l, Y)
                row0 = M.lidx(l, Y, mu)
                for a in range(3):
                    if r0p in M.lam_index:
                        for c in range(3):
                            Xi.add(row0+a, 3*M.lam_index[r0p]+c, R[a][c])
                    if r0 in M.lam_index:
                        Xi.add(row0+a, 3*M.lam_index[r0]+a, -1)
    # level-0 covariant curl: X -> 2-forms (3*nsite0)
    Dc = SM(3*M.nsite[0], M.nX)
    for y in M.sites(0):
        b1 = (y, 0); b2 = (M.norm(0, M.add(y, M.e(0))), 1); b3 = (M.norm(0, M.add(y, M.e(1))), 0); b4 = (y, 1)
        R1, R4 = Z[0][b1], Z[0][b4]
        prow = 3*M.sidx(0, y)
        for a in range(3):
            Dc.add(prow+a, M.lidx(0, *b1)+a, 1)
            Dc.add(prow+a, M.lidx(0, *b4)+a, -1)
            for c in range(3):
                Dc.add(prow+a, M.lidx(0, *b2)+c, R1[a][c])
                Dc.add(prow+a, M.lidx(0, *b3)+c, -R4[a][c])
    # residual maps Res_l : X -> level-(l+1) 1-forms, Res_l x = Q^Z_l x_l - x_{l+1} (x_k = 0)
    Res = []
    for l in range(k):
        R_ = SM(3*M.nlink[l+1], M.nX)
        for Y in M.sites(l+1):
            for mu in range(D):
                row0 = 3*(M.sidx(l+1, Y)*D + mu)
                cY = M.rootat(l, Y)
                Tr = I3
                for i in range(Lb):
                    yi = M.norm(l, (cY[0] + i*M.e(mu)[0], cY[1] + i*M.e(mu)[1]))
                    col0 = M.lidx(l, yi, mu)
                    for a in range(3):
                        for c in range(3):
                            R_.add(row0+a, col0+c, Tr[a][c])
                    Tr = mm(Tr, Z[l][(yi, mu)])
                if l+1 < k:
                    col0 = M.lidx(l+1, Y, mu)
                    for a in range(3):
                        R_.add(row0+a, col0+a, -1)
        Res.append(R_)
    H = Dc.T().mul(Dc)
    for l in range(k):
        H = H.plus(Res[l].T().mul(Res[l]).scale(M.kap[l]))
    return {'Xi': Xi, 'Dc': Dc, 'Res': Res, 'H': H}

def tree_left_inverse(M, Z0):
    """P' : X -> Lambda_0 with P' Xi_Z = 1 (covariant spanning-tree integration on level 0 from one level-k root)."""
    r = sorted(M.roots_k)[0]
    coef = {r: {}}   # site -> dict x_index -> 3x3 coefficient rows (list of 3 lists over x components handled per index)
    # represent lambda(s)[a] = sum_{col} C[a][col] * x[col]; store as list of 3 dicts
    coef = {r: [dict(), dict(), dict()]}
    from collections import deque
    dq = deque([r]); seen = {r}
    while dq:
        p = dq.popleft()
        for mu in range(D):
            for sgn in (1, -1):
                c = M.norm(0, (p[0] + sgn*M.e(mu)[0], p[1] + sgn*M.e(mu)[1]))
                if c in seen: continue
                seen.add(c)
                lp = coef[p]
                new = [dict(), dict(), dict()]
                if sgn == 1:   # link b = (p, mu), x(b) = R lam(c) - lam(p) => lam(c) = R^T (x(b) + lam(p))
                    R = Z0[(p, mu)]; RT = tr(R); col0 = M.lidx(0, p, mu)
                    for a in range(3):
                        for cc in range(3):
                            w = RT[a][cc]
                            if w == 0: continue
                            new[a][col0+cc] = new[a].get(col0+cc, 0) + w
                            for j, v in lp[cc].items():
                                new[a][j] = new[a].get(j, 0) + w*v
                else:          # link b = (c, mu), x(b) = R lam(p) - lam(c) => lam(c) = R lam(p) - x(b)
                    R = Z0[(c, mu)]; col0 = M.lidx(0, c, mu)
                    for a in range(3):
                        new[a][col0+a] = new[a].get(col0+a, 0) - 1
                        for cc in range(3):
                            w = R[a][cc]
                            if w == 0: continue
                            for j, v in lp[cc].items():
                                new[a][j] = new[a].get(j, 0) + w*v
                for a in range(3):
                    new[a] = {j: v for j, v in new[a].items() if v != 0}
                coef[c] = new
                dq.append(c)
    P = SM(M.nL, M.nX)
    for s, i in M.lam_index.items():
        for a in range(3):
            for j, v in coef[s][a].items():
                P.add(3*i+a, j, v)
    return P

def MG_ops(M, G):
    """M_G on chains (base-site Ad, level-l via level-0 root) and on Lambda_0."""
    MX = SM(M.nX, M.nX)
    for l in range(M.k):
        for Y in M.sites(l):
            g = G[M.root0(l, Y)]
            for mu in range(D):
                r0 = M.lidx(l, Y, mu)
                for a in range(3):
                    for c in range(3):
                        MX.add(r0+a, r0+c, g[a][c])
    ML = SM(M.nL, M.nL)
    for s, i in M.lam_index.items():
        g = G[s]
        for a in range(3):
            for c in range(3):
                ML.add(3*i+a, 3*i+c, g[a][c])
    return MX, ML

def pure_gauge_Z(M, G):
    Z = []
    for l in range(M.k):
        Zl = {}
        for Y in M.sites(l):
            for mu in range(D):
                Yp = M.norm(l, M.add(Y, M.e(mu)))
                Zl[(Y, mu)] = mm(G[M.root0(l, Y)], tr(G[M.root0(l, Yp)]))
        Z.append(Zl)
    return Z
def trivial_Z(M):
    return [{(Y, mu): I3 for Y in M.sites(l) for mu in range(D)} for l in range(M.k)]
def curved_Z(M, rng):
    return [{(Y, mu): rng.choice(OCT) for Y in M.sites(l) for mu in range(D)} for l in range(M.k)]

def plaquette_hol_identity(M, Z0):
    for y in M.sites(0):
        b1 = (y, 0); b2 = (M.norm(0, M.add(y, M.e(0))), 1); b3 = (M.norm(0, M.add(y, M.e(1))), 0); b4 = (y, 1)
        h = mm(mm(Z0[b1], Z0[b2]), tr(mm(Z0[b4], Z0[b3])))
        if h != I3: return False
    return True

out = []
def rep(tag, ok, extra=""):
    out.append(f"{tag}: {'PASS' if ok else 'FAIL'} {extra}".rstrip())
    print(out[-1]); sys.stdout.flush()
def ctl(tag, fired, extra=""):
    out.append(f"{tag}: {'FIRES' if fired else 'DOES-NOT-FIRE'} {extra}".rstrip())
    print(out[-1]); sys.stdout.flush()

def run_model(name, M, seed, do_solve):
    rng = random.Random(seed)
    print(f"== {name}: k={M.k} Tc={M.Tc} dimX={M.nX} dimLambda0={M.nL}"); sys.stdout.flush()
    out.append(f"== {name}: k={M.k} Tc={M.Tc} dimX={M.nX} dimLambda0={M.nL}")
    Z1 = trivial_Z(M); O1 = build_ops(M, Z1)
    H1, Xi1 = O1['H'], O1['Xi']
    P = tree_left_inverse(M, Z1[0])
    rep(f"{name} pre P Xi_1 = 1", P.mul(Xi1).plus(eye(M.nL), -1).iszero())
    rep(f"{name} pre H_1 Xi_1 = 0", H1.mul(Xi1).iszero())
    # ---- PG ----
    G = {s: rng.choice(OCT) for s in M.sites(0)}
    Zp = pure_gauge_Z(M, G); Op = build_ops(M, Zp)
    MX, ML = MG_ops(M, G)
    # A1: d_Z M_G = M_G d on functions at every level: check via Xi: Xi_Z M_G^fn = M_G Xi_1 (covers every level's d on roots-fns)
    a1a = Op['Xi'].mul(ML).plus(MX.mul(Xi1), -1).iszero()
    a1b = Op['H'].plus(MX.mul(H1).mul(MX.T()), -1).iszero()
    rep(f"{name} A1 (PG) Xi_Z M_G = M_G Xi_1 and H^cov_Z = M_G H_1 M_G^T", a1a and a1b, f"[{a1a},{a1b}]")
    HZp = Op['H']
    rep(f"{name} A2 (PG) H_Z Xi_Z = 0", HZp.mul(Op['Xi']).iszero())
    # alignments at PG
    TG = MX
    TNp = eye(M.nX).plus(Op['Xi'].plus(Xi1, -1).mul(P))
    a3a = TG.mul(Xi1).plus(Op['Xi'].mul(ML), -1).iszero()
    a3b = TNp.mul(Xi1).plus(Op['Xi'], -1).iszero()
    rep(f"{name} A3 (PG) T_G Xi_1 = Xi_Z M_G^fn ; T_N Xi_1 = Xi_Z", a3a and a3b, f"[{a3a},{a3b}]")
    E_G = TG.T().mul(HZp).mul(TG).plus(H1, -1)
    E_Np = TNp.T().mul(HZp).mul(TNp).plus(H1, -1)
    a4 = all(E.mul(Xi1).iszero() and Xi1.T().mul(E).iszero() for E in (E_G, E_Np))
    rep(f"{name} A4 (PG) E_T Xi_1 = 0 and Xi_1^T E_T = 0 for T in (T_G, T_N)", a4)
    rep(f"{name} A6 (PG) E_(T_G) = 0", E_G.iszero(), f"(nnz E_TG = {E_G.nnz()})")
    ctl(f"{name} C2 (PG) E_(T_N) != 0", not E_Np.iszero(), f"(nnz = {E_Np.nnz()})")
    E1p = HZp.plus(H1, -1)
    ctl(f"{name} C3a (PG) (H_Z - H_1) Xi_1 != 0", not E1p.mul(Xi1).iszero())
    ctl(f"{name} C4 (PG) H_Z - H_1 != 0 with all plaquette holonomies = 1", (not E1p.iszero()) and plaquette_hol_identity(M, Zp[0]),
        f"(nnz H_Z-H_1 = {E1p.nnz()}, flat = {plaquette_hol_identity(M, Zp[0])})")
    # A5 at PG
    ok5 = True
    for t in range(6):
        x = [rng.randint(-3, 3) for _ in range(M.nX)]
        S = HZp.vec(x)
        for T_ in (TG, TNp):
            if any(v != 0 for v in Xi1.T().vec(T_.T().vec(S))): ok5 = False
    rep(f"{name} A5 (PG) Xi_1^T T^T S = 0 for 6 random S in cc_Z, T in (T_G, T_N)", ok5)
    # ---- CV ----
    Zc = curved_Z(M, rng); Oc = build_ops(M, Zc)
    ctl(f"{name} C1 (CV) H^cov_Z Xi_Z != 0", not Oc['H'].mul(Oc['Xi']).iszero())
    Pz = tree_left_inverse(M, Zc[0])
    rep(f"{name} pre P'_Z Xi_Z = 1 (CV)", Pz.mul(Oc['Xi']).plus(eye(M.nL), -1).iszero())
    XiZ, Hc = Oc['Xi'], Oc['H']
    PzT, XiZT = Pz.T(), XiZ.T()
    def PZ_mul(B):    # (1 - Xi_Z P'_Z) B
        return B.plus(XiZ.mul(Pz.mul(B)), -1)
    def PZT_mul(B):   # (1 - P'_Z^T Xi_Z^T) B
        return B.plus(PzT.mul(XiZT.mul(B)), -1)
    def HZ_mul(B):    # H_Z B with H_Z := P_Z^T H^cov_Z P_Z
        return PZT_mul(Hc.mul(PZ_mul(B)))
    def PZ_vec(x):
        y = Pz.vec(x); z = XiZ.vec(y); return [a - b for a, b in zip(x, z)]
    def PZT_vec(x):
        y = XiZT.vec(x); z = PzT.vec(y); return [a - b for a, b in zip(x, z)]
    def HZ_vec(x):
        return PZT_vec(Hc.vec(PZ_vec(x)))
    rep(f"{name} A2 (CV) H_Z Xi_Z = 0 (projected H_Z)", HZ_mul(XiZ).iszero())
    TNc = eye(M.nX).plus(XiZ.plus(Xi1, -1).mul(P))
    rep(f"{name} A3 (CV) T_N Xi_1 = Xi_Z", TNc.mul(Xi1).plus(XiZ, -1).iszero())
    TNcT = TNc.T()
    EXi = TNcT.mul(HZ_mul(TNc.mul(Xi1))).plus(H1.mul(Xi1), -1)
    # Xi_1^T E_T = (E_T Xi_1)^T because E_T = T^T H_Z T - H_1 is symmetric (H_Z, H_1 symmetric); in M1 it is also checked directly.
    rep(f"{name} A4 (CV) E_(T_N) Xi_1 = 0 (and its transpose)", EXi.iszero())
    C3b = HZ_mul(Xi1).plus(H1.mul(Xi1), -1)
    ctl(f"{name} C3b (CV) (H_Z - H_1) Xi_1 != 0", not C3b.iszero())
    ok5 = True
    for t in range(6):
        x = [rng.randint(-3, 3) for _ in range(M.nX)]
        S = HZ_vec(x)
        if any(v != 0 for v in Xi1.T().vec(TNcT.vec(S))): ok5 = False
    rep(f"{name} A5 (CV) Xi_1^T T_N^T S = 0 for 6 random S in cc_Z", ok5)
    Sbad = [rng.randint(-3, 3) for _ in range(M.nX)]
    ctl(f"{name} C5 (CV) random non-cc S_bad: Xi_1^T T_N^T S_bad != 0", any(v != 0 for v in Xi1.T().vec(TNcT.vec(Sbad))))
    Tt = eye(M.nX).plus(XiZ.plus(Xi1, -1).mul(P.scale(2)))
    c6a = not Tt.mul(Xi1).plus(XiZ, -1).iszero()
    c6b = not Tt.T().mul(HZ_mul(Tt.mul(Xi1))).plus(H1.mul(Xi1), -1).iszero()
    ctl(f"{name} C6 (CV) T~ = 1 + (Xi_Z - Xi_1)(2P): T~ Xi_1 != Xi_Z and E_T~ Xi_1 != 0", c6a and c6b, f"[{c6a},{c6b}]")
    if do_solve:
        PZm = eye(M.nX).plus(XiZ.mul(Pz), -1)
        HZc = PZm.T().mul(Hc).mul(PZm)
        E_Nc = TNcT.mul(HZc).mul(TNc).plus(H1, -1)
        rep(f"{name} A4' (CV, full) E_(T_N) Xi_1 = 0 and Xi_1^T E_(T_N) = 0 (full matrices)",
            E_Nc.mul(Xi1).iszero() and Xi1.T().mul(E_Nc).iszero(), f"(nnz E = {E_Nc.nnz()}, nnz H_Z = {HZc.nnz()})")
    if do_solve:
        for bgname, HZ, TN in (("PG", HZp, TNp), ("CV", HZc, TNc)):
            Td = TN.dense()
            rk = bareiss_rank(Td)
            inv_ok = (rk == M.nX)
            Hp = TN.T().mul(HZ).mul(TN)
            A = Hp.plus(P.T().mul(P)).dense()
            sols_ok = inv_ok
            if inv_ok:
                rhs = []; Ss = []
                for t in range(3):
                    x = [rng.randint(-3, 3) for _ in range(M.nX)]
                    S = HZ.vec(x); Ss.append(S); rhs.append(TN.T().vec(S))
                us = solve_exact(A, rhs)
                for S, u in zip(Ss, us):
                    xx = [sum(Fraction(v)*u[j] for j, v in TN.r.get(i, {}).items()) for i in range(M.nX)]
                    HZx = [sum(Fraction(v)*xx[j] for j, v in HZ.r.get(i, {}).items()) for i in range(M.nX)]
                    if any(HZx[i] != S[i] for i in range(M.nX)): sols_ok = False
                    Pu = [sum(Fraction(v)*u[j] for j, v in P.r.get(i, {}).items()) for i in range(M.nL)]
                    if any(p != 0 for p in Pu): sols_ok = False
            rep(f"{name} A7 ({bgname}) T_N invertible and x = T_N u solves H_Z x = S (3 random S in cc_Z)", inv_ok and sols_ok,
                f"(rank T_N = {rk}/{M.nX})")
            rkH = bareiss_rank(HZ.dense())
            out.append(f"{name} I1 ({bgname}) rank H_Z = {rkH}; dimX - dimLambda0 = {M.nX - M.nL}")
            print(out[-1]); sys.stdout.flush()

M1 = Model(k=1, Tc=2, kap=[2])
run_model("M1", M1, seed=20261029, do_solve=True)
M2 = Model(k=2, Tc=1, kap=[2, 3])
run_model("M2", M2, seed=20261030, do_solve=False)
print("\n".join(["", "SUMMARY:"] + [ln for ln in out if (": PASS" in ln or ": FAIL" in ln or "FIRE" in ln)]))
