#!/usr/bin/env python3
# gt1_b.py -- (1) RE-RUN of clause gt1-A under the new id gt1b-A, with the gt1 criteria UNTOUCHED.
#                 gt1_green.py's d^* was MINUS the true adjoint (post-hoc diagnosis in GREENT.md section G4);
#                 that script and its output are kept unaltered.  Here d^* is the true adjoint.
#             (2) a POST-HOC probe (labelled as such; no criterion attached): the decay of the bare kernel
#                 column vs the zero-mean-source response along ONE fixed direction, on interior shells,
#                 which is what clause gt1-D should have measured.
# Exact integers for (1).  IEEE double for (2).  No numpy, no BLAS, single process.
import math, cmath, sys, random
from itertools import product

TWOCOS = {3: [2, -1, -1], 4: [2, 0, -2, 0], 6: [2, 1, -1, -2, -1, 1]}

def pairs(d):   return [(m, n) for m in range(d) for n in range(m + 1, d)]
def triples(d): return [(m, n, p) for m in range(d) for n in range(m + 1, d) for p in range(n + 1, d)]

class T0:
    def __init__(self, d, R):
        self.d, self.R = d, R
        self.pts = list(product(range(R), repeat=d))
    def shift(self, x, mu, h):
        y = list(x); y[mu] = (y[mu] + h) % self.R; return tuple(y)

def d1(T, A):
    return {(x, m, n): (A[(T.shift(x, m, 1), n)] - A[(x, n)] - A[(T.shift(x, n, 1), m)] + A[(x, m)])
            for x in T.pts for (m, n) in pairs(T.d)}

def d2(T, F):
    out = {}
    for x in T.pts:
        for (m, n, p) in triples(T.d):
            out[(x, m, n, p)] = ((F[(T.shift(x, m, 1), n, p)] - F[(x, n, p)])
                                 - (F[(T.shift(x, n, 1), m, p)] - F[(x, m, p)])
                                 + (F[(T.shift(x, p, 1), m, n)] - F[(x, m, n)]))
    return out

def dstar2(T, F):                 # TRUE adjoint:  (d*F)_n(x) = sum_m [F_{mn}(x-e_m) - F_{mn}(x)]
    out = {}
    for x in T.pts:
        for n in range(T.d):
            s = 0
            for m in range(T.d):
                if m == n:
                    continue
                a, b = (m, n) if m < n else (n, m)
                sg = 1 if m < n else -1
                s += sg * (F[(T.shift(x, m, -1), a, b)] - F[(x, a, b)])
            out[(x, n)] = s
    return out

def dstar3(T, H):                 # TRUE adjoint
    out = {}
    for x in T.pts:
        for (m, n) in pairs(T.d):
            s = 0
            for p in range(T.d):
                if p in (m, n):
                    continue
                key = tuple(sorted((p, m, n)))
                perm = [p, m, n]; sg = 1
                for i in range(3):
                    for j in range(i + 1, 3):
                        if perm[i] > perm[j]:
                            sg = -sg
                s += sg * (H[(T.shift(x, p, -1),) + key] - H[(x,) + key])
            out[(x, m, n)] = s
    return out

def lap2(T, F):
    out = {}
    for x in T.pts:
        for (m, n) in pairs(T.d):
            s = 0
            for mu in range(T.d):
                s += 2 * F[(x, m, n)] - F[(T.shift(x, mu, 1), m, n)] - F[(T.shift(x, mu, -1), m, n)]
            out[(x, m, n)] = s
    return out

def rerun_A(outp):
    L = []
    L.append("gt1b-A : RE-RUN of clause gt1-A with the TRUE adjoint d^*.  gt1 criteria untouched.")
    rnd = random.Random(12345)
    allpass = True
    for (d, R) in [(3, 3), (3, 4), (3, 6), (4, 3), (4, 4), (4, 6)]:
        T = T0(d, R)
        bad = tot = 0
        for _ in range(3):
            F = {(x, m, n): rnd.randint(-9, 9) for x in T.pts for (m, n) in pairs(d)}
            lhs = dstar3(T, d2(T, F)); A = dstar2(T, F); rhs = d1(T, A); Lp = lap2(T, F)
            for k in F:
                tot += 1
                if lhs[k] + rhs[k] != Lp[k]:
                    bad += 1
        adj = 0
        for _ in range(3):
            A = {(x, m): rnd.randint(-9, 9) for x in T.pts for m in range(d)}
            F = {(x, m, n): rnd.randint(-9, 9) for x in T.pts for (m, n) in pairs(d)}
            H = {(x,) + tr: rnd.randint(-9, 9) for x in T.pts for tr in triples(d)}
            dA = d1(T, A); dsF = dstar2(T, F)
            if sum(dA[k] * F[k] for k in F) != sum(A[k] * dsF[k] for k in A):
                adj += 1
            if triples(d):
                dF = d2(T, F); dsH = dstar3(T, H)
                if sum(dF[k] * H[k] for k in H) != sum(F[k] * dsH[k] for k in F):
                    adj += 1
        ok = (bad == 0 and adj == 0)
        allpass = allpass and ok
        L.append("  d=%d R=%d : (dd*+d*d)F vs componentwise Laplacian: %d/%d discrepancies ; "
                 "adjointness failures: %d  -> %s" % (d, R, bad, tot, adj, "PASS" if ok else "FAIL"))
    L.append("gt1b-A overall: %s" % ("PASS" if allpass else "FAIL"))
    txt = "\n".join(L); print(txt)
    open(outp, "w").write(txt + "\n")

# ---------------- POST-HOC probe ----------------
def green(d, R):
    N = R ** d
    c = [2.0 - 2.0 * math.cos(2.0 * math.pi * m / R) for m in range(R)]
    phi = [0.0] * N
    for i in range(N):
        t = i; s = 0.0
        for _ in range(d):
            s += c[t % R]; t //= R
        phi[i] = s
    A = [(1.0 / phi[i]) + 0j if phi[i] > 1e-12 else 0j for i in range(N)]
    W = [[cmath.exp(2j * math.pi * (a * b % R) / R) for b in range(R)] for a in range(R)]
    stride = 1
    for mu in range(d):
        blk = stride * R
        for base in range(0, N, blk):
            for off in range(stride):
                idx = [base + off + j * stride for j in range(R)]
                vals = [A[t] for t in idx]
                for a in range(R):
                    Wa = W[a]; tot = 0j
                    for b in range(R):
                        tot += vals[b] * Wa[b]
                    A[idx[a]] = tot
        stride = blk
    f = 1.0 / N
    return [v.real * f for v in A]

def posthoc(outp):
    d = 4
    L = []
    L.append("POST-HOC (no criterion attached; run after seeing gt1-D / gt1b-D FAIL).")
    L.append("Fixed direction x = (s,0,0,0), interior shells only.  |b| = max over the 1-form components.")
    for R in (24, 32):
        G = green(d, R)
        Rp = [R ** (d - 1 - mu) for mu in range(d)]
        def ix(x): return sum((x[mu] % R) * Rp[mu] for mu in range(d))
        src = {}
        z0 = (0, 0, 0, 0)
        for nu in range(1, d):
            e = [0] * d; e[nu] = 1
            src[(z0, 0, nu)] = src.get((z0, 0, nu), 0.0) + 1.0
            key = tuple((-e[k]) % R for k in range(d))
            src[(key, 0, nu)] = src.get((key, 0, nu), 0.0) - 1.0
        def potA(x, m, n):
            s = 0.0
            for ((z, mm, nn), v) in src.items():
                if (mm, nn) == (m, n):
                    s += G[ix([x[k] - z[k] for k in range(d)])] * v
            return s
        def potB(x, m, n):
            return G[ix(x)] if (m, n) == (0, 1) else 0.0
        def dst(pot, x):
            o = []
            for n in range(d):
                s = 0.0
                for m in range(d):
                    if m == n:
                        continue
                    a, b = (m, n) if m < n else (n, m)
                    sg = 1.0 if m < n else -1.0
                    em = [0] * d; em[m] = 1
                    s += sg * (pot([x[k] - em[k] for k in range(d)], a, b) - pot(x, a, b))
                o.append(s)
            return o
        L.append("")
        L.append("  R=%d :  s | s^3|b_B| | s^4|b_B| | s^3|b_A| | s^4|b_A| | local exp b_B | local exp b_A" % R)
        prev = None
        for s in range(2, R // 3 + 1):
            x = [s, 0, 0, 0]
            vB = max(abs(v) for v in dst(potB, x))
            vA = max(abs(v) for v in dst(potA, x))
            eB = eA = float('nan')
            if prev is not None:
                ps, pB, pA = prev
                eB = -math.log(vB / pB) / math.log(s / ps)
                eA = -math.log(vA / pA) / math.log(s / ps)
            L.append("        %2d | %8.5f | %8.5f | %8.5f | %8.5f | %11.4f | %11.4f"
                     % (s, s ** 3 * vB, s ** 4 * vB, s ** 3 * vA, s ** 4 * vA, eB, eA))
            prev = (s, vB, vA)
    txt = "\n".join(L); print(txt)
    open(outp, "w").write(txt + "\n")

if __name__ == "__main__":
    if sys.argv[1] == "A":
        rerun_A(sys.argv[2])
    else:
        posthoc(sys.argv[2])
