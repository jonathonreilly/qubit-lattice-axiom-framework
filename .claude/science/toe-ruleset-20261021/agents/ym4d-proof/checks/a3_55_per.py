# a3_55_per.py -- exact checks for ALIGN3_55 section 1 (periodic method-of-images path average; completion identity; CEN2 core).
# Criteria: a3_55_per_criteria.md (written before this script). Fractions/ints only; stdout only.
from fractions import Fraction as F
import itertools, random, sys, time
T0 = time.time()
RES = {}
def rec(name, ok, info=''):
    RES[name] = bool(ok); print(f'{name}: {"PASS" if ok else "FAIL"} {info}'); sys.stdout.flush()
def recC(name, fired, info=''):
    RES[name] = bool(fired); print(f'{name}: {"FIRES" if fired else "DOES NOT FIRE"} {info}'); sys.stdout.flush()
L = 3

# ---------------- exact dense linear algebra (small) ----------------
def mat_inv(A):
    n = len(A); M = [list(row) + [F(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]; M[c] = [v / pv for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]; M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [row[n:] for row in M]
def matvec(A, v): return [sum((a * b for a, b in zip(row, v) if a != 0), F(0)) for row in A]

# ================= Part I: 1D periodic cubic spline =================
def B3(x):
    ax = abs(x)
    if ax >= 2: return F(0)
    if ax >= 1: return (2 - ax) ** 3 / 6
    return F(2, 3) - ax ** 2 + ax ** 3 / 2
def spline_tables(P):
    N = 3 * P
    C = [[F(0)] * P for _ in range(P)]
    for J in range(P):
        C[J][J] += F(4, 6); C[J][(J + 1) % P] += F(1, 6); C[J][(J - 1) % P] += F(1, 6)
    Cp = [[F(0)] * P for _ in range(P)]          # d/dz at z = 1 of the Floquet-twisted circulant
    Cp[P - 1][0] += F(1, 6); Cp[0][P - 1] -= F(1, 6)
    Ci = mat_inv(C)
    a = [[F(0)] * P for _ in range(N)]; m1 = [[F(0)] * P for _ in range(N)]
    for J0 in range(P):
        c = matvec(Ci, [F(int(j == J0)) for j in range(P)])
        cp = [-v for v in matvec(Ci, matvec(Cp, c))]
        for y in range(N):
            t = F(y, 3); fl = y // 3; s = F(0); ds = F(0)
            for m in range(fl - 1, fl + 3):
                b = B3(t - m)
                if b == 0: continue
                q, r = divmod(m, P)
                s += c[r] * b; ds += (q * c[r] + cp[r]) * b
            a[y][J0] = s; m1[y][J0] = ds
    return a, m1
def psum(x, N, start, end):                      # signed sum of a 1D 1-form over the lifted path start -> end
    s = F(0)
    if end >= start:
        for i in range(start, end): s += x[i % N]
    else:
        for i in range(end, start): s -= x[i % N]
    return s
def shortest(N, delta):
    d = delta % N
    return d - N if d > N // 2 else d
def part1():
    ok0 = True; ok1 = ok2 = ok3 = ok4 = True; fire1 = True; fire2 = True
    codex5 = [F(238, 297), F(113, 297), F(-10, 99), F(2, 33), F(-14, 99)]
    codex9 = [F(v, 1377) for v in (1102, 521, -126, 34, -10, 6, -14, 50, -186)]
    for P in (3, 5, 9):
        N = 3 * P; a, m1 = spline_tables(P)
        Mm = lambda x, y: sum((a[y][J] * psum(x, N, y - shortest(N, y - 3 * J), y) for J in range(P)), F(0))
        M0 = lambda x, y: sum((a[y][J] * psum(x, N, 3 * J, y) for J in range(P)), F(0))
        Mi = lambda x, y: M0(x, y) - sum(m1[y], F(0)) * sum(x, F(0))
        one = [F(1)] * N
        vm = Mm(one, 1)
        if P == 3: ok0 &= (vm == F(-8, 9))
        if P == 5: ok0 &= (vm == F(40, 99)) and (a[1] == codex5)
        if P == 9: ok0 &= (a[1] == codex9) and vm != 0 and ((1377 * vm - 3960) / 27).denominator == 1
        print(f'  P={P}: merged M(1)(1) = {vm}; sum_J m1(1,J) = {sum(m1[1], F(0))}')
        for y in range(N):
            ok1 &= (sum((a[y][J] * (y - 3 * J) for J in range(P)), F(0)) - N * sum(m1[y], F(0)) == 0)
        fire2 &= any(M0(one, y) != 0 for y in range(N))
        S0 = lambda g: [sum((a[y][J] * g[J] for J in range(P)), F(0)) for y in range(N)]
        d = lambda nu: [nu[(i + 1) % N] - nu[i] for i in range(N)]
        B = lambda x: [x[3 * J] + x[3 * J + 1] + x[3 * J + 2] for J in range(P)]
        def S1(w):
            mean = sum(w, F(0)) / P; g = [F(0)] * P
            for J in range(1, P): g[J] = g[J - 1] + w[J - 1] - mean
            return [v + mean / 3 for v in d(S0(g))]
        for z in range(N):                       # I2: M d = 1 - S0 R on basis functions
            nu = [F(int(i == z)) for i in range(N)]; dn = d(nu); Rn = [nu[3 * J] for J in range(P)]; s0 = S0(Rn)
            ok2 &= all(Mi(dn, y) == nu[y] - s0[y] for y in range(N))
        anyfail_merged = False
        for i in range(N):                       # I3, I4, CI1 on basis 1-forms
            x = [F(int(j == i)) for j in range(N)]
            Mx = [Mi(x, y) for y in range(N)]; e = d(Mx); s1b = S1(B(x))
            ok3 &= all(e[j] - x[j] + s1b[j] == 0 for j in range(N))
            mean = sum(x, F(0)) / N; xh = [v - mean for v in x]
            ok4 &= all(Mx[y] == Mm(xh, y) for y in range(N))
            em = d([Mm(x, y) for y in range(N)])
            if any(em[j] - x[j] + s1b[j] != 0 for j in range(N)): anyfail_merged = True
        fire1 &= anyfail_merged
    rec('I0', ok0, '(Codex F5 rows and merged values reproduced)'); rec('I1', ok1); rec('I2', ok2); rec('I3', ok3); rec('I4', ok4)
    recC('CI1', fire1, '(merged operator fails dM - 1 + S1 B = 0)'); recC('CI2', fire2, '(n = 0 paths alone do not kill constants)')
part1()
print(f'  [Part I time {time.time() - T0:.2f}s]'); sys.stdout.flush()

# ================= Part II: d = 2, s3, image construction =================
S3 = {0: {0: F(1)}, 1: {-1: F(-5, 81), 0: F(60, 81), 1: F(30, 81), 2: F(-4, 81)},
      2: {-1: F(-4, 81), 0: F(30, 81), 1: F(60, 81), 2: F(-5, 81)}}
def derived(S):
    U = {}
    for r in range(3):
        u = {}
        nxt = S[r + 1] if r + 1 < 3 else {o + 1: w for o, w in S[0].items()}
        for o, w in nxt.items(): u[o] = u.get(o, F(0)) + w
        for o, w in S[r].items(): u[o] = u.get(o, F(0)) - w
        assert sum(u.values()) == 0
        lo, hi = min(u), max(u); acc = F(0); Ur = {}
        for j in range(lo, hi):
            acc += u.get(j, F(0))
            if acc != 0: Ur[j] = -acc
        U[r] = Ur
    return U
U3 = derived(S3)
E2 = ((1, 0), (0, 1))
def add(p, q): return (p[0] + q[0], p[1] + q[1])
def steps_axial(delta, order):
    st = []
    for nu in order:
        sg = 1 if delta[nu] > 0 else -1
        st += [(nu, sg)] * abs(delta[nu])
    return st
def chain_of(start, steps, coef, out, N=None):
    pos = start
    for nu, sg in steps:
        if sg > 0:
            key = (pos, nu); pos = add(pos, E2[nu]); c = coef
        else:
            pos = (pos[0] - E2[nu][0], pos[1] - E2[nu][1]); key = (pos, nu); c = -coef
        if N is not None: key = ((key[0][0] % N, key[0][1] % N), nu)
        out[key] = out.get(key, F(0)) + c
    return pos
def clean(d): return {k: v for k, v in d.items() if v != 0}
def M_row(y, N=None, merged=False):
    r = (y[0] % 3, y[1] % 3); I = (y[0] // 3, y[1] // 3); out = {}
    if r == (0, 0): return out
    if not merged:
        for o0, w0 in S3[r[0]].items():
            for o1, w1 in S3[r[1]].items():
                Y = (3 * (I[0] + o0), 3 * (I[1] + o1))
                end = chain_of(Y, steps_axial((y[0] - Y[0], y[1] - Y[1]), (0, 1)), w0 * w1, out, N)
                assert end == y
    else:
        Nc = N // 3; grp = {}
        for o0, w0 in S3[r[0]].items():
            for o1, w1 in S3[r[1]].items():
                node = ((I[0] + o0) % Nc, (I[1] + o1) % Nc); grp[node] = grp.get(node, F(0)) + w0 * w1
        for node, w in grp.items():
            dl = (shortest(N, y[0] - 3 * node[0]), shortest(N, y[1] - 3 * node[1]))
            chain_of((y[0] - dl[0], y[1] - dl[1]), steps_axial(dl, (0, 1)), w, out, N)
    return clean(out)
def S0_row(y, Nc=None):
    r = (y[0] % 3, y[1] % 3); I = (y[0] // 3, y[1] // 3); out = {}
    for o0, w0 in S3[r[0]].items():
        for o1, w1 in S3[r[1]].items():
            J = (I[0] + o0, I[1] + o1)
            if Nc is not None: J = (J[0] % Nc, J[1] % Nc)
            out[J] = out.get(J, F(0)) + w0 * w1
    return clean(out)
def S1_row(y, mu, Nc=None, wrong=False):
    r = (y[0] % 3, y[1] % 3); I = (y[0] // 3, y[1] // 3); out = {}
    A0 = (U3 if (mu == 0 and not wrong) else S3)[r[0]]; A1 = (U3 if (mu == 1 and not wrong) else S3)[r[1]]
    for o0, w0 in A0.items():
        for o1, w1 in A1.items():
            J = (I[0] + o0, I[1] + o1)
            if Nc is not None: J = (J[0] % Nc, J[1] % Nc)
            key = (J, mu); out[key] = out.get(key, F(0)) + w0 * w1
    return clean(out)
OFFS_C = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1)]
def B_row(J, mu, N=None):
    c = (3 * J[0], 3 * J[1]); cp = add(c, (3 * E2[mu][0], 3 * E2[mu][1])); out = {}
    w = F(1, 2 * len(OFFS_C))
    for order in ((0, 1), (1, 0)):
        for dlt in OFFS_C:
            st = steps_axial(dlt, order)
            p = chain_of(c, st, w, out, N); assert p == add(c, dlt)
            p = chain_of(p, [(mu, 1)] * 3, w, out, N)
            p = chain_of(p, [(nu, -sg) for (nu, sg) in reversed(st)], w, out, N); assert p == cp
    return clean(out)
def sites(N): return [(i, j) for i in range(N) for j in range(N)]
def links(N): return [((i, j), nu) for i in range(N) for j in range(N) for nu in (0, 1)]
def mul(A, Bm):
    out = {}
    for i, row in A.items():
        acc = {}
        for kk, a in row.items():
            for j, b in Bm.get(kk, {}).items(): acc[j] = acc.get(j, F(0)) + a * b
        out[i] = clean(acc)
    return out
def apply(A, v):
    return clean({i: sum((a * v.get(kk, F(0)) for kk, a in row.items()), F(0)) for i, row in A.items()})
def applyT(A, v):
    out = {}
    for i, row in A.items():
        vi = v.get(i, F(0))
        if vi == 0: continue
        for kk, a in row.items(): out[kk] = out.get(kk, F(0)) + a * vi
    return clean(out)
def eq(A, Bm):
    keys = set(A) | set(Bm)
    return all(clean(A.get(kk, {})) == clean(Bm.get(kk, {})) for kk in keys)
def lin(A, B, s):
    keys = set(A) | set(B); out = {}
    for kk in keys:
        r = dict(A.get(kk, {}))
        for j, v in B.get(kk, {}).items(): r[j] = r.get(j, F(0)) + s * v
        out[kk] = clean(r)
    return out
def pair(u, v): return sum((a * v.get(kk, F(0)) for kk, a in u.items()), F(0))
class Level:
    def __init__(self, N, merged=False):
        self.N = N; self.Nc = N // 3; N_, Nc = N, N // 3
        self.M = {y: M_row(y, N_, merged) for y in sites(N_)}
        self.S0 = {y: S0_row(y, Nc) for y in sites(N_)}
        self.R = {J: {(3 * J[0], 3 * J[1]): F(1)} for J in sites(Nc)}
        self.d0 = {(z, nu): clean({((z[0] + E2[nu][0]) % N_, (z[1] + E2[nu][1]) % N_): F(1), z: F(-1)}) for (z, nu) in links(N_)}
        self.d0c = {(z, nu): clean({((z[0] + E2[nu][0]) % Nc, (z[1] + E2[nu][1]) % Nc): F(1), z: F(-1)}) for (z, nu) in links(Nc)}
        self.S1 = {(y, mu): S1_row(y, mu, Nc) for (y, mu) in links(N_)}
        self.B = {(J, mu): B_row(J, mu, N_) for (J, mu) in links(Nc)}
        self.d1 = {z: clean({(z, 0): F(1), (((z[0] + 1) % N_, z[1]), 1): F(1), ((z[0], (z[1] + 1) % N_), 0): F(-1), (z, 1): F(-1)}) for z in sites(N_)}
        self._E = None
    @property
    def E(self):
        if self._E is None:
            I = {b: {b: F(1)} for b in links(self.N)}
            self._E = lin(lin(mul(self.d0, self.M), I, -1), mul(self.S1, self.B), 1)
        return self._E
def const_form(N, nu): return {((i, j), nu): F(1) for i in range(N) for j in range(N)}

def boundary(Z):   # 1-chain -> 0-chain
    out = {}
    for (z, nu), v in Z.items():
        h = add(z, E2[nu]); out[h] = out.get(h, F(0)) + v; out[z] = out.get(z, F(0)) - v
    return clean(out)
def Z_row(rep, wrongS1=False):   # row of E^inf at link rep (lifted, Z^2)
    (y, mu) = rep; h = add(y, E2[mu]); out = {}
    for kk, v in M_row(h).items(): out[kk] = out.get(kk, F(0)) + v
    for kk, v in M_row(y).items(): out[kk] = out.get(kk, F(0)) - v
    out[rep] = out.get(rep, F(0)) - 1
    for c, s in S1_row(y, mu, None, wrongS1).items():
        for kk, v in B_row(c[0], c[1]).items(): out[kk] = out.get(kk, F(0)) + s * v
    return clean(out)
def fill(Z):   # unique finite 2-chain F on Z^2 with dF = Z (plaquette (i,j): h(i,j) + v(i+1,j) - h(i,j+1) - v(i,j))
    xs = [z[0] for (z, nu) in Z]; ys = [z[1] for (z, nu) in Z]
    Fc = {}
    for i in range(min(xs) - 1, max(xs) + 2):
        acc = F(0)
        for j in range(min(ys) - 1, max(ys) + 2):
            acc += Z.get(((i, j), 0), F(0))
            if acc != 0: Fc[(i, j)] = acc
        assert acc == 0, 'non-finite filling'
    dF = {}
    for (i, j), v in Fc.items():
        for kk, s in ((((i, j), 0), 1), (((i + 1, j), 1), 1), (((i, j + 1), 0), -1), (((i, j), 1), -1)):
            dF[kk] = dF.get(kk, F(0)) + s * v
    return Fc, clean(dF) == Z
def Ntilde_per(N, table):
    out = {}
    for (y, mu) in links(N):
        r = (y[0] % 3, y[1] % 3); sh = (y[0] - r[0], y[1] - r[1]); row = {}
        for P, v in table[(r, mu)].items():
            Pk = ((P[0] + sh[0]) % N, (P[1] + sh[1]) % N); row[Pk] = row.get(Pk, F(0)) + v
        out[(y, mu)] = clean(row)
    return out
def part2():
    t1 = time.time()
    lv = {('T3', 1): Level(9), ('T3', 0): Level(27), ('T5', 1): Level(15), ('T5', 0): Level(45)}
    print(f'  [levels built {time.time() - t1:.1f}s]'); sys.stdout.flush()
    ok1 = ok2 = True
    for key, L_ in lv.items():
        N = L_.N
        for nu in (0, 1): ok1 &= (apply(L_.M, const_form(N, nu)) == {})
        Md = mul(L_.M, L_.d0); SR = mul(L_.S0, L_.R)
        ok1 &= eq(Md, lin({y: {y: F(1)} for y in sites(N)}, SR, -1))
        ok2 &= eq(mul(L_.B, L_.d0), mul(L_.d0c, L_.R)) and eq(mul(L_.d0, L_.S0), mul(L_.S1, L_.d0c))
        for nu in (0, 1): ok2 &= (apply(L_.S1, apply(L_.B, const_form(N, nu))) == const_form(N, nu))
    rec('II1', ok1, '(matrix identities at all four levels: stronger than registered)'); rec('II2', ok2)
    reps = [((r0, r1), mu) for r0 in range(3) for r1 in range(3) for mu in (0, 1)]
    table = {}; okc = True; okf = True; rad = 0
    for rep in reps:
        Z = Z_row(rep); okc &= (boundary(Z) == {})
        Fc, good = fill(Z); okf &= good; table[(rep[0], rep[1])] = Fc
        rad = max([rad] + [max(abs(P[0] - rep[0][0]), abs(P[1] - rep[0][1])) for P in Fc])
    print(f'  Z_b cycles: {okc}; fillings exact: {okf}; max l_inf radius of F_b about its link: {rad}')
    oke = True
    for key in (('T3', 1), ('T3', 0), ('T5', 1)):
        L_ = lv[key]; NtD = mul(Ntilde_per(L_.N, table), L_.d1); oke &= eq(L_.E, NtD)
        print(f'    E_torus == Ntilde_per d1 at side {L_.N}: {eq(L_.E, NtD)}')
    rec('II3', okc and okf and oke, f'(radius {rad})')
    fire4 = any(boundary(Z_row(rep, True)) != {} for rep in reps)
    recC('CF4', fire4, '(non-derived S1 breaks the cycle property)')
    # II4: hierarchical completion identity, T = 3, k = 2
    A0, A1 = lv[('T3', 0)], lv[('T3', 1)]
    Nt0, Nt1 = Ntilde_per(27, table), Ntilde_per(9, table)
    ok4 = True; fire3 = False
    for seed in (1, 2, 3):
        rng = random.Random(77 + seed); rnd = lambda: F(rng.randint(-9, 9), rng.randint(1, 6))
        x0 = clean({b: rnd() for b in links(27)}); x1 = clean({b: rnd() for b in links(9)})
        lam1 = {y: -v for y, v in apply(A1.M, x1).items()}
        lam0 = lin({0: apply(A0.S0, lam1)}, {0: apply(A0.M, x0)}, -1)[0]
        for l in (0, 1):
            if l == 0:
                w = clean({b: rnd() for b in links(27)}); lhs = pair(w, apply(A0.d0, lam0))
                w1 = applyT(A0.S1, w); w2 = applyT(A1.S1, w1)
                main = -pair(w, x0) + pair(w1, lin({0: apply(A0.B, x0)}, {0: x1}, -1)[0]) + pair(w2, apply(A1.B, x1))
                nt = pair(w, apply(Nt0, apply(A0.d1, x0))) + pair(w1, apply(Nt1, apply(A1.d1, x1)))
            else:
                w = clean({b: rnd() for b in links(9)}); lhs = pair(w, apply(A1.d0, lam1))
                w2 = applyT(A1.S1, w)
                main = -pair(w, x1) + pair(w2, apply(A1.B, x1)); nt = pair(w, apply(Nt1, apply(A1.d1, x1)))
            ok4 &= (lhs == main - nt); fire3 |= (lhs != main)
    rec('II4', ok4); recC('CF3', fire3, '(dropping the Ntilde term breaks the identity)')
    Lm = Level(9, merged=True)
    recC('CF1', apply(Lm.M, const_form(9, 0)) != {}, '(merged M on the wrapping torus does not kill constants)')
    recC('CF2', apply(Lm.E, const_form(9, 0)) != {}, '(merged E does not vanish on constants)')
    print(f'  [Part II time {time.time() - t1:.1f}s]'); sys.stdout.flush()
part2()

# ================= Part III: CEN2 core in a nilpotent algebra =================
def m_zero(): return [[F(0)] * 4 for _ in range(4)]
def m_id(): return [[F(int(i == j)) for j in range(4)] for i in range(4)]
def m_mul(A, B): return [[sum((A[i][k] * B[k][j] for k in range(4)), F(0)) for j in range(4)] for i in range(4)]
def m_add(A, B, s=1): return [[A[i][j] + s * B[i][j] for j in range(4)] for i in range(4)]
def m_scale(A, s): return [[s * v for v in row] for row in A]
def m_exp(X):
    X2 = m_mul(X, X); X3 = m_mul(X2, X)
    return m_add(m_add(m_add(m_id(), X), m_scale(X2, F(1, 2))), m_scale(X3, F(1, 6)))
def m_log(M):
    Y = m_add(M, m_id(), -1); Y2 = m_mul(Y, Y); Y3 = m_mul(Y2, Y)
    return m_add(m_add(Y, m_scale(Y2, F(-1, 2))), m_scale(Y3, F(1, 3)))
def comm(A, B): return m_add(m_mul(A, B), m_mul(B, A), -1)
def transport(steps, A):
    P = m_id()
    for nu, sg in steps: P = m_mul(P, m_exp(m_scale(A[nu], sg)))
    return P
def Mbar(A, offs, orders, mu=0):
    tot = m_zero(); cnt = 0
    for order in orders:
        for dlt in offs:
            st = steps_axial(dlt, order)
            T_ = m_mul(m_mul(transport(st, A), transport([(mu, 1)] * 3, A)), transport([(nu, -sg) for (nu, sg) in reversed(st)], A))
            tot = m_add(tot, T_); cnt += 1
    return m_scale(tot, F(1, cnt))
VI = mat_inv([[F(1), F(1), F(1)], [F(2), F(4), F(8)], [F(3), F(9), F(27)]])
def coeffs(fn):
    fs = [fn(F(t)) for t in (1, 2, 3)]
    return [m_add(m_add(m_scale(fs[0], row[0]), m_scale(fs[1], row[1])), m_scale(fs[2], row[2])) for row in VI]
def sut(rng): return [[F(rng.randint(-3, 3)) if j > i else F(0) for j in range(4)] for i in range(4)]
def part3():
    ok1 = ok2 = True; f1 = f2 = True
    OFF_K = [(a, b) for a in (0, 1, 2) for b in (0, 1, 2)]
    for seed in (5, 6):
        rng = random.Random(seed)
        A0, A1, V1 = sut(rng), sut(rng), sut(rng)
        while comm(A0, A1) == m_zero(): A1 = sut(rng)
        fn = lambda t: m_log(Mbar([m_scale(A0, t), m_scale(A1, t)], OFFS_C, ((0, 1), (1, 0))))
        c1, c2, c3 = coeffs(fn)
        ok1 &= (c1 == m_scale(A0, 3)) and (c2 == m_zero())
        for VV in (V1, c1):
            g = lambda t: m_log(m_mul(m_exp(m_scale(VV, -t)), Mbar([m_scale(A0, t), m_scale(A1, t)], OFFS_C, ((0, 1), (1, 0)))))
            d1, d2, d3 = coeffs(g)
            ok2 &= (d2 == m_scale(comm(VV, m_add(c1, VV, -1)), F(-1, 2)))
            if VV is c1: ok2 &= (d2 == m_zero())
        k1, k2, k3 = coeffs(lambda t: m_log(Mbar([m_scale(A0, t), m_scale(A1, t)], OFF_K, ((0, 1), (1, 0)))))
        f1 &= (k2 != m_zero())
        s1, s2, s3 = coeffs(lambda t: m_log(Mbar([m_scale(A0, t), m_scale(A1, t)], [(1, 1)], ((0, 1),))))
        f2 &= (s2 != m_zero())
    rec('III1', ok1); rec('III2', ok2)
    recC('CIII1', f1, '(lower-corner offsets leave a quadratic term)'); recC('CIII2', f2, '(a single contour leaves a quadratic term)')
part3()

passes = ['I0', 'I1', 'I2', 'I3', 'I4', 'II1', 'II2', 'II3', 'II4', 'III1', 'III2']
fires = ['CI1', 'CI2', 'CF1', 'CF2', 'CF3', 'CF4', 'CIII1', 'CIII2']
overall = all(RES.get(n, False) for n in passes + fires)
print('OVERALL', 'PASS' if overall else 'FAIL', f'(total time {time.time() - T0:.1f}s)')
