"""GUIDE run for gap-es1-opus.md (a run can refute or guide; it proves nothing).
Pure Python (no numpy on this machine). Run with python3 -I.

2D Ising, isotropic coupling K, exact transfer matrices on rings of n sites,
periodic (m=0) or antiperiodic (m=1) closing, parity sectors chi (global flip).
Sector sums Z_{chi,m}(t; n) = Tr(T_m^t P_chi). Even sector 0 = (chi=0, m=0).

Criteria written before the run (2D forms; sum p = 2, four sectors):
 C1 identity:  exp(-D) = (1/2) sum_z Z_z(2a; a)/lam0(a)^(2a) / (1 + S')
               D = a(2 e(a) - e(2a)), S' = S_ev(a; 2a).       (rel. err < 1e-8)
 C2 Theorem V lower: D >= -log(1 - Q/2) - 2 log(1+eps) + log(1+S')
 C3 Theorem V upper: D <= -log(1 - H_L - sum_L s_z) + log(1+S') - 2 log(1+eps)
 C4 long-box form, b = 2a: D <= (2a/(b-a)) [log 2 + log(1 + S_ev(a; b))]
 FAIL at any point means the algebra of Sections 2-3 is wrong (in 2D form).
Printed without criterion: eps, D, D/eps, D/sqrt(eps), max heavy p^2/eps.
"""
import math


def build(n, K, m):
    N = 1 << n
    dh = []
    for i in range(N):
        s = [1 - 2 * ((i >> j) & 1) for j in range(n)]
        b = sum(s[j] * s[(j + 1) % n] * (-1 if (m == 1 and j == n - 1) else 1) for j in range(n))
        dh.append(math.exp(0.5 * K * b))
    return dh


def matvec(v, n, K, dh):
    N = 1 << n
    w = [v[i] * dh[i] for i in range(N)]
    a, b = math.exp(K), math.exp(-K)
    for j in range(n):
        bit = 1 << j
        for i in range(N):
            if not i & bit:
                x, y = w[i], w[i | bit]
                w[i], w[i | bit] = a * x + b * y, b * x + a * y
    return [w[i] * dh[i] for i in range(N)]


def proj(v, chi, N):
    sg = 1 if chi == 0 else -1
    return [0.5 * (v[i] + sg * v[(N - 1) ^ i]) for i in range(N)]


def dense(n, K, m, chi):
    N = 1 << n
    dh = build(n, K, m)
    cols = []
    for i in range(N):
        e = [0.0] * N
        e[i] = 1.0
        cols.append(matvec(proj(e, chi, N), n, K, dh))
    return [[cols[j][i] for j in range(N)] for i in range(N)]  # A = T P


def mm(A, B):
    N = len(A)
    Bt = list(zip(*B))
    return [[sum(x * y for x, y in zip(A[i], Bt[j])) for j in range(N)] for i in range(N)]


def trpow(A, t):
    R = A
    for _ in range(t - 1):
        R = mm(R, A)
    return sum(R[i][i] for i in range(len(A)))


def topeig(n, K, m, chi, it=3000):
    N = 1 << n
    dh = build(n, K, m)
    v = proj([1.0 + 0.001 * ((i * 7919) % 13) for i in range(N)], chi, N)
    lam = 0.0
    for k in range(it):
        w = proj(matvec(v, n, K, dh), chi, N)
        nv = math.sqrt(sum(x * x for x in w))
        if nv == 0:
            return 0.0
        new = sum(x * y for x, y in zip(v, w)) / sum(x * x for x in v)
        v = [x / nv for x in w]
        if k > 50 and abs(new - lam) < 1e-15 * abs(new):
            lam = new
            break
        lam = new
    return lam


def trace_matvec(n, K, m, chi, t):
    N = 1 << n
    dh = build(n, K, m)
    tot = 0.0
    for i in range(N):
        e = [0.0] * N
        e[i] = 1.0
        v = proj(e, chi, N)
        for _ in range(t):
            v = matvec(v, n, K, dh)
        tot += v[i]
    return tot


def run(alist, Klist):
    fails = 0
    print("K a eps Delta lowV upV Delta/eps Delta/sqrt(eps) maxheavy_p2/eps relerrC1 PASS light")
    for K in Klist:
        for a in alist:
            Z, Z2, mu = {}, {}, {}
            for m in (0, 1):
                for chi in (0, 1):
                    A = dense(a, K, m, chi)
                    Z[(chi, m)] = trpow(A, a)
                    Z2[(chi, m)] = trpow(A, 2 * a)
                    mu[(chi, m)] = topeig(a, K, m, chi)
            lam = mu[(0, 0)]
            lam2 = topeig(2 * a, K, 0, 0)
            D = a * (2 * math.log(lam) - math.log(lam2))
            eps = Z[(0, 0)] / lam ** a - 1
            Sp = trace_matvec(2 * a, K, 0, 0, a) / lam2 ** a - 1
            p = {z: Z[z] / Z[(0, 0)] for z in Z}
            s = {z: (Z[z] / mu[z] ** a - 1) if mu[z] > 0 else 0.0 for z in Z}
            rhs = 0.5 * sum(Z2.values()) / lam ** (2 * a) / (1 + Sp)
            c1 = abs(math.exp(-D) - rhs) / rhs
            Q = sum(p[z] * (1 - p[z]) for z in p)
            low = -math.log(1 - Q / 2) - 2 * math.log1p(eps) + math.log1p(Sp)
            L = sorted(p, key=lambda z: -p[z])[:2]
            HL = sum(p[z] for z in p if z not in L)
            sL = sum(s[z] for z in L)
            up = -math.log(1 - HL - sL) + math.log1p(Sp) - 2 * math.log1p(eps)
            c4b = 2.0 * (math.log(2) + math.log1p(Sp))
            ok = c1 < 1e-8 and D >= low - 1e-12 and D <= up + 1e-12 and D <= c4b
            fails += (not ok)
            heavy = [z for z in p if z not in L]
            fuse = max(p[z] ** 2 for z in heavy) / eps
            print("%.4f %d %.3e %.3e %.3e %.3e %.2e %.3f %.3f %.1e %s %s" % (
                K, a, eps, D, low, up, D / eps, D / math.sqrt(eps), fuse, c1, ok, L), flush=True)
    print("FAILS:", fails)


if __name__ == "__main__":
    import sys
    alist = [int(x) for x in sys.argv[1].split(",")] if len(sys.argv) > 1 else [3, 4]
    run(alist, (0.2, 0.3, 0.38, 0.4406868, 0.5, 0.6, 0.8))
