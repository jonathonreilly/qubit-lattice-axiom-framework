# GUIDE only (row 1156 check). Pure-Python toy checks of exact identities; not a proof.
import math, random, itertools
random.seed(1156)

def mm(A, B):
    n, k, m = len(A), len(B), len(B[0]); Bt = list(zip(*B))
    return [[sum(a*b for a, b in zip(A[i], Bt[j])) for j in range(m)] for i in range(n)]
def mpow(A, p):
    R = A
    for _ in range(p-1): R = mm(R, A)
    return R
def tr(A): return sum(A[i][i] for i in range(len(A)))
def topeig(A, it=4000):
    v = [1.0]*len(A); lam = 0.0
    for _ in range(it):
        w = [sum(a*b for a, b in zip(row, v)) for row in A]
        lam = math.sqrt(sum(x*x for x in w)); v = [x/lam for x in w]
    return lam

def toy(kbits, m, T):
    G = 2**kbits; X = G*m
    f = [[[random.random()+0.05 for _ in range(m)] for _ in range(m)] for _ in range(G)]
    M = [[f[(i//m) ^ (j//m)][i % m][j % m] for j in range(X)] for i in range(X)]
    Mt = [list(r) for r in zip(*M)]
    F = mm(M, Mt)                      # symmetric, PSD, positive, G-equivariant
    s = topeig(F); F = [[(1.0 if i == j else 0.0) + F[i][j]/s for j in range(X)] for i in range(X)]
    lam = topeig(F)
    perm = lambda b: [((i//m) ^ b)*m + (i % m) for i in range(X)]
    pw = {}
    def P(p):
        if p not in pw: pw[p] = mpow(F, p)
        return pw[p]
    def Zb(p): return [sum(P(p)[i][perm(b)[i]] for i in range(X)) for b in range(G)]
    g = lambda p: math.log(tr(P(p))/lam**p)
    th = lambda p: Zb(p)[0]/sum(Zb(p))
    t = T//2; Ft = P(t)
    Pq = [[0.0]*m for _ in range(m)]
    for b in range(G):
        pb = perm(b)
        for x in range(X):
            for y in range(X):
                Pq[x % m][y % m] += Ft[x][y]*Ft[y][pb[x]]
    S = sum(map(sum, Pq)); Q = [[math.sqrt(v/S) for v in r] for r in Pq]
    QQ = mm(Q, [list(r) for r in zip(*Q)])
    op2 = topeig(QQ); Arect = tr(mm(QQ, QQ))
    eg = math.exp(-g(T)); eJ = math.exp(-(2*g(T) - g(2*T)))
    print(f"G=2^{kbits} m={m} T={T}")
    print(f"  e^-g_T = {eg:.12f}   ||K||^2/(|G| th0(T)) = {op2/(G*th(T)):.12f}")
    print(f"  e^-J_T = {eJ:.12f}   A th0(2T)/(|G| th0(T)^2) = {Arect*th(2*T)/(G*th(T)**2):.12f}")
    # untwisted cylinder quotient (remark at L515): generally different
    P0 = [[0.0]*m for _ in range(m)]
    for x in range(X):
        for y in range(X): P0[x % m][y % m] += Ft[x][y]**2
    S0 = sum(map(sum, P0)); Q0 = [[math.sqrt(v/S0) for v in r] for r in P0]
    print(f"  untwisted quotient ||K0||^2/(|G| th0) = {topeig(mm(Q0, [list(r) for r in zip(*Q0)]))/(G*th(T)):.12f}")
    # (10), (11), (28) for the full untwisted pair law
    SL = sum(Ft[x][y]**2 for x in range(X) for y in range(X))
    PL = [[Ft[x][y]**2/SL for y in range(X)] for x in range(X)]
    pi = [sum(r) for r in PL]
    QL = [[math.sqrt(v) for v in r] for r in PL]; QQL = mm(QL, [list(r) for r in zip(*QL)])
    HL = sum(math.sqrt(PL[x][y]*pi[x]*pi[y]) for x in range(X) for y in range(X))
    Pb = [[0.0]*m for _ in range(m)]
    for x in range(X):
        for y in range(X): Pb[x % m][y % m] += PL[x][y]
    pib = [sum(r) for r in Pb]
    Hb = sum(math.sqrt(Pb[a][c]*pib[a]*pib[c]) for a in range(m) for c in range(m))
    print(f"  (10) A(P_L) = {tr(mm(QQL, QQL)):.12f} vs e^-J_T")
    print(f"  (11) {math.exp(-1.5*g(T)):.6f} <= H={HL:.6f} <= {math.exp(-0.5*g(T)):.6f}")
    print(f"  (28) H(Pbar)/sqrt|G| = {Hb/math.sqrt(G):.6f} <= H(P_L) = {HL:.6f} <= H(Pbar) = {Hb:.6f}")

toy(3, 3, 4); toy(2, 3, 6); toy(1, 4, 8)

# pi^2/15 = 6 (2 pi)^-3 * 4 pi * int r^2 (-log(1-e^-r)) dr  (Simpson)
N = 200000; a, b = 1e-9, 60.0; hstep = (b-a)/N
fr = lambda r: r*r*(-math.log1p(-math.exp(-r)))
sim = fr(a) + fr(b) + sum((4 if i % 2 else 2)*fr(a+i*hstep) for i in range(1, N))
print("gas constant", 6/(2*math.pi)**3*4*math.pi*sim*hstep/3, "pi^2/15", math.pi**2/15)
for D in [2.0, 10.0, 1e3]:
    best = max(((1+(D-1)*k/100000)-1)*(D-(1+(D-1)*k/100000))/((1+(D-1)*k/100000)*(D-1)) for k in range(100001))
    print("tilt bound D", D, best, (math.sqrt(D)-1)/(math.sqrt(D)+1))
print("q_*", (math.exp(.5)-1)/(math.exp(.5)+1), "tanh(1/4)", math.tanh(.25))
def det(A):
    A = [r[:] for r in A]; n = len(A); dv = 1.0
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(A[r][c]))
        if p != c: A[c], A[p] = A[p], A[c]; dv = -dv
        dv *= A[c][c]
        for r in range(c+1, n):
            fct = A[r][c]/A[c][c]
            for k in range(c, n): A[r][k] -= fct*A[c][k]
    return dv
d = 5; xs = sorted(random.random() for _ in range(d-1))
vdm = math.prod(xs[j]-xs[i] for i in range(d-1) for j in range(i+1, d-1))
for srem in range(d):
    rows = [k for k in range(d) if k != srem]
    alt = det([[x**k for x in xs] for k in rows])
    kk = d-1-srem; e = sum(math.prod(c) for c in itertools.combinations(xs, kk)) if kk > 0 else 1.0
    print("alternant/vdm", srem, round(alt/vdm, 10), "e_k", round(e, 10))
for n in [1e4, 1e8, 1e12]:
    ST = n**-0.5 + n*n**-0.5/2; S2T = n**-1 + n*n**-1/4
    print("n", n, "J_T", 2*math.log1p(ST) - math.log1p(S2T), "log n - log 5", math.log(n) - math.log(5))
print("11/(3 pi^2)", 11/(3*math.pi**2), "internal comp", math.cos(math.pi/4+0.1)+15/4-1, "arcsin(8/15)", math.asin(8/15), "pi/4", math.pi/4)
