# Guide only (pure Python). Toy check of (J), (T), (F), the pointwise bound and the converse
# on random reversible positive semidefinite Markov chains with a Z_2 symmetry R.
import random, math
random.seed(7)
def mm(A, B):
    n = len(A); m = len(B[0]); k = len(B)
    return [[sum(A[i][l]*B[l][j] for l in range(k)) for j in range(m)] for i in range(n)]
def mv(A, v): return [sum(a*b for a, b in zip(row, v)) for row in A]
def mpow(A, t):
    n = len(A); R = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(t): R = mm(R, A)
    return R
def trial(n, wells):
    N = 2*n
    A = [[random.random() for _ in range(n)] for _ in range(n)]
    A = [[A[i][j]+A[j][i] for j in range(n)] for i in range(n)]
    B = [[random.random() for _ in range(n)] for _ in range(n)]
    B = [[(B[i][j]+B[j][i])*wells for j in range(n)] for i in range(n)]
    W = [[(A[i % n][j % n] if (i < n) == (j < n) else B[i % n][j % n]) for j in range(N)] for i in range(N)]
    rs = [sum(r) for r in W]; tot = sum(rs); pi = [r/tot for r in rs]
    P = [[W[i][j]/rs[i] for j in range(N)] for i in range(N)]
    Q = mm(P, P)
    Rm = lambda i: (i+n) % N
    ip = lambda u, v: sum(p*a*b for p, a, b in zip(pi, u, v))
    # top odd eigenfunction by power iteration on odd functions
    f = [random.random() for _ in range(n)]; f = f + [-a for a in f]
    for _ in range(4000):
        f = mv(Q, f); nr = math.sqrt(ip(f, f)); f = [a/nr for a in f]
    lam_o = ip(f, mv(Q, f))
    # second even eigenvalue: power iteration on even functions orthogonal to constants
    g = [random.random() for _ in range(n)]; g = g + g
    for _ in range(4000):
        m0 = ip(g, [1.0]*N); g = [a-m0 for a in g]
        g = mv(Q, g); nr = math.sqrt(ip(g, g)); g = [a/nr for a in g]
    lam_e = ip(g, mv(Q, g))
    kappa = sum(p*a**4 for p, a in zip(pi, f))
    out = []
    for t in (1, 2, 5, 20):
        Qt = mpow(Q, t)
        tau = [1 - 0.5*sum(abs(Qt[i][j]-Qt[i][Rm(j)]) for j in range(N)) for i in range(N)]
        tb = sum(p*a for p, a in zip(pi, tau))
        lhs = 1 - lam_o**(2*t)
        J = (1-1/kappa)*(1-lam_e**t)
        T_ = tb - 0.5*lam_e**t*math.sqrt(max(kappa-1, 0.0))
        Fb = 0.5*tb*tb*(1-lam_e**t)
        Qf = mv(Qt, f); Qf2 = mv(Qt, [a*a for a in f])
        pw = all(Qf[i]**2 <= (1-tau[i])*Qf2[i] + 1e-10 for i in range(N))
        # S_odd(2t) = trace of Q^{2t} on odd functions = (1/2)(Tr Q^{2t} - Tr R Q^{2t})
        Q2t = mm(Qt, Qt)
        Sodd = 0.5*(sum(Q2t[i][i] for i in range(N)) - sum(Q2t[i][Rm(i)] for i in range(N)))
        conv = tb >= 1 - math.sqrt(max(Sodd, 0.0)) - 1e-6
        out.append((lhs >= J-1e-9, lhs >= T_-1e-9, lhs >= Fb-1e-9, pw, conv, round(lhs, 5), round(Fb, 5), round(tb, 5), round(kappa, 4)))
    return out
bad = 0; tot = 0
for wells in (1.0, 0.1, 1e-3, 1e-6):
    last = None
    for _ in range(40):
        for o in trial(5, wells):
            tot += 1
            if not all(o[:5]): bad += 1; print("VIOLATION", wells, o)
            last = o
    print("wells", wells, "sample (J ok, T ok, F ok, pointwise ok, converse ok, lhs, F bound, taubar, kappa):", last)
print("violations", bad, "of", tot)
