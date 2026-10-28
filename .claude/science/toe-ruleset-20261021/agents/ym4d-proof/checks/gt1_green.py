#!/usr/bin/env python3
# gt1_green.py -- EXACT (integer/rational) lattice Green's function on (Z/R)^d, d in {3,4}, R in {3,4,6}.
# Criteria: checks/gt1_criteria.md, written BEFORE this file existed.
# Clauses: gt1-A (Hodge Laplacian = componentwise scalar Laplacian, on 2-forms)
#          gt1-B (solver validation: Delta G = delta_0 - R^-d exactly, sum G = 0)
#          gt1-C (max of r^(d-1)|grad G| and r^d|grad grad G|; compared against the PROVEN constants
#                 that gt1_const.py computes from GREENT.md section G2 -- separate code path, no shared state)
#          gt1-D (moment-cancellation separation: zero-mean source vs bare kernel)
# Plain python, integers + fractions only.  No numpy, no BLAS, single process.  No numeric lock taken.
from fractions import Fraction
from itertools import product
import math, sys

# cos(2*pi*m/R) is rational exactly for R | 1,2,3,4,6 (Niven).  Store 2*cos as an integer.
TWOCOS = {
    3: [2, -1, -1],
    4: [2, 0, -2, 0],
    6: [2, 1, -1, -2, -1, 1],
}

def lcm(a, b):
    return a * b // math.gcd(a, b)

def rep(m, R):
    "representative of m mod R in (-R/2, R/2]"
    m %= R
    return m - R if 2 * m > R else m

class Torus:
    def __init__(self, d, R):
        assert R in TWOCOS
        self.d, self.R = d, R
        self.c2 = TWOCOS[R]
        self.pts = list(product(range(R), repeat=d))
        self.idx = {p: i for i, p in enumerate(self.pts)}
        self.N = len(self.pts)
        # phi(k) = sum_mu (2 - 2cos(2 pi k_mu / R))  -- an integer
        self.phi = [sum(2 - self.c2[k[mu]] for mu in range(d)) for k in self.pts]
        D = 1
        for v in self.phi:
            if v:
                D = lcm(D, 2 * v)
        self.D = D
        self.scale = Fraction(1, (R ** d) * D)     # G(x) = Gnum[x] * scale
        # Gnum[x] = sum_{k != 0} 2cos(2 pi k.x/R) * (D / (2 phi(k)))     (integers)
        w = [0] * self.N
        for i, v in enumerate(self.phi):
            if v:
                w[i] = D // (2 * v)
        self.Gnum = [0] * self.N
        for j, x in enumerate(self.pts):
            tot = 0
            for i, k in enumerate(self.pts):
                wi = w[i]
                if wi:
                    s = 0
                    for mu in range(d):
                        s += k[mu] * x[mu]
                    tot += self.c2[s % R] * wi
            self.Gnum[j] = tot
        self.r2 = [sum(rep(m, R) ** 2 for m in x) for x in self.pts]

    def shift(self, x, mu, h):
        y = list(x)
        y[mu] = (y[mu] + h) % self.R
        return tuple(y)

    def G(self, x):
        return Fraction(self.Gnum[self.idx[x]]) * self.scale

    def gradG_num(self, x, mu):
        "integer numerator of grad_mu G(x) (times scale)"
        return self.Gnum[self.idx[self.shift(x, mu, 1)]] - self.Gnum[self.idx[x]]

    def grad2G_num(self, x, mu, nu):
        a = self.shift(x, mu, 1)
        return (self.Gnum[self.idx[self.shift(a, nu, 1)]] - self.Gnum[self.idx[a]]
                - self.Gnum[self.idx[self.shift(x, nu, 1)]] + self.Gnum[self.idx[x]])


# ---------- combinatorial exterior derivative / coderivative (independent of the Laplacian formula) ----
def pairs(d):
    return [(m, n) for m in range(d) for n in range(m + 1, d)]

def triples(d):
    return [(m, n, p) for m in range(d) for n in range(m + 1, d) for p in range(n + 1, d)]

def d1(T, A):                       # 1-forms -> 2-forms
    out = {}
    for x in T.pts:
        for (m, n) in pairs(T.d):
            out[(x, m, n)] = (A[(T.shift(x, m, 1), n)] - A[(x, n)]
                              - A[(T.shift(x, n, 1), m)] + A[(x, m)])
    return out

def d2(T, F):                       # 2-forms -> 3-forms
    out = {}
    for x in T.pts:
        for (m, n, p) in triples(T.d):
            out[(x, m, n, p)] = ((F[(T.shift(x, m, 1), n, p)] - F[(x, n, p)])
                                 - (F[(T.shift(x, n, 1), m, p)] - F[(x, m, p)])
                                 + (F[(T.shift(x, p, 1), m, n)] - F[(x, m, n)]))
    return out

def dstar2(T, F):                   # 2-forms -> 1-forms
    out = {}
    for x in T.pts:
        for n in range(T.d):
            s = 0
            for m in range(T.d):
                if m == n:
                    continue
                a, b = (m, n) if m < n else (n, m)
                sg = 1 if m < n else -1
                s += sg * (F[(x, a, b)] - F[(T.shift(x, m, -1), a, b)])
            out[(x, n)] = s
    return out

def dstar3(T, H):                   # 3-forms -> 2-forms
    out = {}
    for x in T.pts:
        for (m, n) in pairs(T.d):
            s = 0
            for p in range(T.d):
                if p in (m, n):
                    continue
                key = tuple(sorted((p, m, n)))
                # sign of the permutation (p,m,n) -> sorted
                perm = [p, m, n]
                sg = 1
                for i in range(3):
                    for j in range(i + 1, 3):
                        if perm[i] > perm[j]:
                            sg = -sg
                s += sg * (H[(x,) + key] - H[(T.shift(x, p, -1),) + key])
            out[(x, m, n)] = s
    return out

def lap2(T, F):                     # componentwise scalar Laplacian on 2-forms
    out = {}
    for x in T.pts:
        for (m, n) in pairs(T.d):
            s = 0
            for mu in range(T.d):
                s += 2 * F[(x, m, n)] - F[(T.shift(x, mu, 1), m, n)] - F[(T.shift(x, mu, -1), m, n)]
            out[(x, m, n)] = s
    return out


def clause_A(T, rng_seed=12345):
    "gt1-A: (d d* + d* d) F == Delta F componentwise, exactly, on random integer 2-forms; plus adjointness."
    import random
    rnd = random.Random(rng_seed)
    bad = 0
    tot = 0
    for _ in range(3):
        F = {(x, m, n): rnd.randint(-9, 9) for x in T.pts for (m, n) in pairs(T.d)}
        lhs = dstar3(T, d2(T, F))
        A = dstar2(T, F)
        rhs2 = d1(T, A)
        L = lap2(T, F)
        for key in F:
            tot += 1
            if lhs[key] + rhs2[key] != L[key]:
                bad += 1
    # adjointness <dA,F> == <A,d*F> and <dF,H> == <F,d*H>
    adj_bad = 0
    for _ in range(3):
        A = {(x, m): rnd.randint(-9, 9) for x in T.pts for m in range(T.d)}
        F = {(x, m, n): rnd.randint(-9, 9) for x in T.pts for (m, n) in pairs(T.d)}
        H = {(x,) + tr: rnd.randint(-9, 9) for x in T.pts for tr in triples(T.d)}
        l = sum(d1(T, A)[k] * F[k] for k in F)
        r = sum(A[k] * dstar2(T, F)[k] for k in A)
        if l != r:
            adj_bad += 1
        if triples(T.d):
            l2 = sum(d2(T, F)[k] * H[k] for k in H)
            r2 = sum(F[k] * dstar3(T, H)[k] for k in F)
            if l2 != r2:
                adj_bad += 1
    return bad, tot, adj_bad


def clause_B(T):
    "gt1-B: Delta Gnum == (R^d delta_0 - 1) * D exactly, and sum_x Gnum == 0."
    bad = 0
    Rd = T.R ** T.d
    for x in T.pts:
        s = 0
        for mu in range(T.d):
            s += 2 * T.Gnum[T.idx[x]] - T.Gnum[T.idx[T.shift(x, mu, 1)]] - T.Gnum[T.idx[T.shift(x, mu, -1)]]
        want = (Rd - 1) * T.D if all(m == 0 for m in x) else (-1) * T.D
        if s != want:
            bad += 1
    return bad, sum(T.Gnum)


def clause_C(T):
    "gt1-C: m1 = max r^(d-1)|grad G|, m2 = max_{r>=2} r^d|grad grad G|.  Returned as exact squares."
    d = T.d
    best1 = Fraction(0); arg1 = None
    best2 = Fraction(0); arg2 = None
    for x in T.pts:
        r2 = Fraction(T.r2[T.idx[x]])
        if r2 == 0:
            continue
        for mu in range(d):
            g = Fraction(T.gradG_num(x, mu)) * T.scale
            v = r2 ** (d - 1) * g * g
            if v > best1:
                best1, arg1 = v, (x, mu, g)
        if r2 >= 4:
            for mu in range(d):
                for nu in range(d):
                    h = Fraction(T.grad2G_num(x, mu, nu)) * T.scale
                    v = r2 ** d * h * h
                    if v > best2:
                        best2, arg2 = v, (x, mu, nu, h)
    return best1, arg1, best2, arg2


def conv_then_dstar(T, src):
    """src: dict (x,m,n)->Fraction, zero mean in every component.  Returns d* Delta^{-1} src as 1-form."
    Delta^{-1} acts componentwise: (Delta^{-1} s)(x) = sum_z G(x-z) s(z)."""
    d = T.d
    pot = {}
    sup = [(z, m, n) for (z, m, n) in src if src[(z, m, n)] != 0]
    for x in T.pts:
        for (m, n) in pairs(d):
            s = Fraction(0)
            for (z, mm, nn) in sup:
                if (mm, nn) != (m, n):
                    continue
                w = tuple((x[i] - z[i]) % T.R for i in range(d))
                s += Fraction(T.Gnum[T.idx[w]]) * T.scale * src[(z, mm, nn)]
            pot[(x, m, n)] = s
    return dstar2(T, pot)


def clause_D(T):
    "gt1-D: zero-mean (exact) source vs bare kernel column.  rho(s) = max over shell of r^d |b|."
    d, R = T.d, T.R
    zero = tuple([0] * d)
    # bare: single plaquette (12) delta minus its mean.  Delta^{-1}(delta_0 - R^-d) = G exactly, so the
    # potential is G on component (0,1) and 0 elsewhere -- no convolution needed.
    potB = {(x, m, n): (Fraction(T.Gnum[T.idx[x]]) * T.scale if (m, n) == (0, 1) else Fraction(0))
            for x in T.pts for (m, n) in pairs(d)}
    bB = dstar2(T, potB)
    # cancelling: dB for B a single-link 1-form -> exact, hence zero mean componentwise
    B = {(x, m): Fraction(0) for x in T.pts for m in range(d)}
    B[(zero, 0)] = Fraction(1)
    srcA = d1(T, B)
    for (m, n) in pairs(d):
        tot = sum(srcA[(x, m, n)] for x in T.pts)
        assert tot == 0, ("exact source not mean-zero", m, n, tot)
    bA = conv_then_dstar(T, srcA)
    def shells(b):
        out = {}
        for x in T.pts:
            r2 = T.r2[T.idx[x]]
            if r2 == 0:
                continue
            r = math.sqrt(r2)
            s = int(math.floor(r))
            v = max(abs(float(b[(x, nu)])) for nu in range(d))
            out[s] = max(out.get(s, 0.0), v * r ** d)
        return out
    return shells(bB), shells(bA)


def main():
    out = []
    P = out.append
    P("gt1_green.py -- exact integer/rational lattice Green's function checks")
    P("criteria: checks/gt1_criteria.md (written first).  No numeric lock; integer/Fraction arithmetic only.")
    results = {}
    for (d, R) in [(3, 3), (3, 4), (3, 6), (4, 3), (4, 4), (4, 6)]:
        P("")
        P("=== d=%d R=%d ===" % (d, R))
        T = Torus(d, R)
        bad, tot, adjbad = clause_A(T)
        P("gt1-A  Hodge(2-form) vs componentwise scalar Laplacian: %d discrepancies out of %d entries; "
          "adjointness failures: %d  -> %s" % (bad, tot, adjbad, "PASS" if bad == 0 and adjbad == 0 else "FAIL"))
        b, gsum = clause_B(T)
        P("gt1-B  solver validation: Delta G = delta_0 - R^-d residual-nonzero sites: %d ; sum_x G = %s  -> %s"
          % (b, "0" if gsum == 0 else str(gsum), "PASS" if (b == 0 and gsum == 0) else "FAIL"))
        m1sq, a1, m2sq, a2 = clause_C(T)
        m1 = math.sqrt(float(m1sq)); m2 = math.sqrt(float(m2sq))
        P("gt1-C  m1 = max r^(d-1)|grad G|      = %.8f   at x=%s mu=%d  (grad G = %s)"
          % (m1, tuple(rep(v, R) for v in a1[0]), a1[1], float(a1[2])))
        if a2 is not None:
            P("gt1-C  m2 = max_{r>=2} r^d|grad^2 G| = %.8f   at x=%s (mu,nu)=(%d,%d)  (val = %s)"
              % (m2, tuple(rep(v, R) for v in a2[0]), a2[1], a2[2], float(a2[3])))
        else:
            P("gt1-C  m2: no x with r>=2 on this torus")
        results[(d, R)] = (m1, m2)
        if R == 6:
            sB, sA = clause_D(T)
            ks = sorted(set(sB) | set(sA))
            P("gt1-D  shell s : rho_B (bare, no cancellation) | rho_A (exact, zero-mean source)")
            for s in ks:
                P("gt1-D    s=%d : %14.8f | %14.8f" % (s, sB.get(s, float('nan')), sA.get(s, float('nan'))))
            seqB = [sB[s] for s in ks if s in sB]
            seqA = [sA[s] for s in ks if s in sA]
            incB = all(seqB[i + 1] > seqB[i] for i in range(len(seqB) - 1))
            incA = all(seqA[i + 1] > seqA[i] for i in range(len(seqA) - 1))
            P("gt1-D  rho_B strictly increasing: %s ; rho_A strictly increasing: %s  -> %s"
              % (incB, incA, "PASS" if (incB and not incA) else "FAIL"))
    P("")
    P("SUMMARY of gt1-C maxima (to be compared with the proven C_1, C_2 of GREENT.md section G2):")
    for k in sorted(results):
        P("  d=%d R=%d : m1 = %.8f   m2 = %.8f" % (k[0], k[1], results[k][0], results[k][1]))
    txt = "\n".join(out)
    print(txt)
    with open(sys.argv[1] if len(sys.argv) > 1 else "gt1_out.txt", "w") as f:
        f.write(txt + "\n")

if __name__ == "__main__":
    main()
