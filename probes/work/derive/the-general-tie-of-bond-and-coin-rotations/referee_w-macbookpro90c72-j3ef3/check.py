#!/usr/bin/env python3
"""Independent referee for the general tie of bond and coin rotations, a1.

The constraint matrix is rebuilt from the stated current symbol and ranked
over a different prime from the author's. The quadratic form is expanded
again in sympy. The author's script is not called.
"""
import itertools

import numpy as np
import sympy as sp
from sympy import isprime
from sympy.ntheory import sqrt_mod

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


def second_prime():
    found = []
    q = 1 << 20
    while len(found) < 2:
        if q % 24 == 1 and isprime(q):
            found.append(q)
        q += 1
    return found[1]


def build(Lt, p, Ii, R2, R3):
    inv = lambda a: pow(int(a) % p, p - 2, p)
    z6 = (1 + Ii * R3) * inv(2) % p
    z = Ii if Lt == 4 else z6
    E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

    def l1(v):
        return abs(v[0]) + abs(v[1]) + abs(v[2])

    Dl = []
    for a in range(3):
        offs = []
        for d in itertools.product(range(-2, 4), repeat=3):
            shifted = tuple(d[i] - E[a][i] for i in range(3))
            if min(l1(d), l1(shifted)) <= 1:
                offs.append(d)
        Dl.append(offs)
    cols = [(a, j, d) for a in range(3) for j in range(3) for d in Dl[a]]
    cidx = {c: i for i, c in enumerate(cols)}
    nc = len(cols)
    SIG = [
        [[0, 1], [1, 0]],
        [[0, (p - Ii) % p], [Ii, 0]],
        [[1, 0], [0, p - 1]],
    ]
    ID = [[1, 0], [0, 1]]

    def mm(A, B):
        return [[(A[i][0] * B[0][j] + A[i][1] * B[1][j]) % p for j in range(2)] for i in range(2)]

    def madd(A, B):
        return [[(A[i][j] + B[i][j]) % p for j in range(2)] for i in range(2)]

    def msc(c, A):
        return [[c * A[i][j] % p for j in range(2)] for i in range(2)]

    def ep(n):
        return pow(z, n % Lt, p)

    def sn(n):
        return (ep(n) - ep(-n)) * inv(2 * Ii) % p

    ks = list(itertools.product(range(Lt), repeat=3))
    shell = {}
    for kk in ks:
        cnt = sum(1 for n in kk if (2 * n) % Lt != 0)
        shell.setdefault(cnt, []).append((kk, [sn(n) for n in kk]))
    rows = []
    for cnt, lst in shell.items():
        if cnt == 0:
            branches = [None]
        elif Lt == 4:
            branches = [{1: 1, 2: R2, 3: R3}[cnt]]
            branches = [branches[0], (p - branches[0]) % p]
        else:
            rad = {1: R3 * inv(2) % p, 2: R2 * R3 * inv(2) % p, 3: 3 * inv(2) % p}[cnt]
            branches = [rad, (p - rad) % p]
        projectors = {}
        for br in branches:
            for kk, s in lst:
                if br is None:
                    projectors[(kk, br)] = ID
                else:
                    acc = msc(br, ID)
                    for t in range(3):
                        acc = madd(acc, msc(s[t], SIG[t]))
                    projectors[(kk, br)] = acc
        for br in branches:
            for (k1, s1), (k2, s2) in itertools.product(lst, repeat=2):
                q = tuple((k2[i] - k1[i]) % Lt for i in range(3))
                row = np.zeros((4, nc), dtype=np.int64)
                P1, P2 = projectors[(k1, br)], projectors[(k2, br)]
                XA = [mm(mm(P1, SIG[a]), P2) for a in range(3)]
                phase = pow(z, (-sum(q[i] * 0 for i in range(3))) % Lt, p)
                for c, (a, j, d) in enumerate(cols):
                    qd = sum(q[i] * d[i] for i in range(3))
                    f = pow(z, (-qd) % Lt, p)
                    f = f * ((ep(k2[a]) + ep(-k1[a])) % p) % p
                    f = f * ((s2[j] + s1[j]) % p) % p
                    mat = XA[a]
                    row[0, c] = f * mat[0][0] % p
                    row[1, c] = f * mat[0][1] % p
                    row[2, c] = f * mat[1][0] % p
                    row[3, c] = f * mat[1][1] % p
                rows.append(row)
    return np.concatenate(rows), cols, cidx, nc, Dl


def modrank(A, p):
    inv = lambda a: pow(int(a) % p, p - 2, p)
    A = A % p
    basis, piv = [], []
    for s0 in range(0, A.shape[0], 5000):
        block = A[s0:s0 + 5000].copy()
        for b, pc in zip(basis, piv):
            block = (block - np.outer(block[:, pc], b)) % p
        for col in range(block.shape[1]):
            if col in piv:
                continue
            nz = np.flatnonzero(block[:, col])
            if len(nz) == 0:
                continue
            r = block[nz[0]] * inv(int(block[nz[0], col])) % p
            for i, b in enumerate(basis):
                if b[col]:
                    basis[i] = (b - int(b[col]) * r) % p
            block = (block - np.outer(block[:, col], r)) % p
            basis.append(r)
            piv.append(col)
    return len(basis)


def main():
    p = second_prime()
    Ii, R2, R3 = sqrt_mod(p - 1, p), sqrt_mod(2, p), sqrt_mod(3, p)
    inv = lambda a: pow(int(a) % p, p - 2, p)
    z6 = (1 + Ii * R3) * inv(2) % p
    check("a second prime 1 mod 24 embeds i, sqrt2, sqrt3, and a primitive sixth root",
          p % 24 == 1 and (Ii * Ii) % p == p - 1 and (R2 * R2) % p == 2 and (R3 * R3) % p == 3
          and pow(z6, 6, p) == 1 and pow(z6, 2, p) != 1,
          f"p={p}")

    A6, cols, cidx, nc, Dl = build(6, p, Ii, R2, R3)
    check("twelve sites within one step of either bond end, 108 unknowns",
          all(len(x) == 12 for x in Dl) and nc == 108 and A6.shape[0] == 125184,
          f"rows {A6.shape[0]}")
    r6 = modrank(A6, p)
    A4, _, _, _, _ = build(4, p, Ii, R2, R3)
    r4 = modrank(A4, p)

    E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    star = [(0, 0, 0)] + [tuple(s * E[a][i] for i in range(3)) for a in range(3) for s in (1, -1)]
    rel = []
    for j0 in range(3):
        for dp in star:
            t = np.zeros(nc, dtype=np.int64)
            for a in range(3):
                far = tuple(E[a][i] + dp[i] for i in range(3))
                t[cidx[(a, j0, far)]] += 1
                t[cidx[(a, j0, dp)]] -= 1
            rel.append(t % p)
    rel = np.array(rel) % p
    # integer rank of the 21 generators, lifted to small integers
    lifted = [[int(v) if v < p // 2 else int(v) - p for v in row] for row in rel]
    rel_rank = sp.Matrix(lifted).rank()
    in_kernel = int(np.count_nonzero((A6 @ rel.T) % p)) == 0
    check("21 independent relabelling ties lie in the 6^3 kernel, and the mod-p rank is 87",
          rel_rank == 21 and in_kernel and r6 == 87 and r4 == 81,
          f"rel {rel_rank} rank6 {r6} rank4 {r4}")

    # forward-bond tie is not a relabelling
    def levi(a, b, c):
        return int(round(np.linalg.det(np.eye(3)[[a, b, c]])))

    bad = []
    for b in range(3):
        t = np.zeros(nc, dtype=np.int64)
        for a in range(3):
            for j in range(3):
                e = levi(a, b, j)
                if e:
                    t[cidx[(a, j, (0, 0, 0))]] += e
        bad.append(int(np.count_nonzero((A6 @ (t % p)) % p)))
    check("the forward-bond tie of issue 8659 is not in the kernel", all(v > 0 for v in bad), str(bad))

    # (b) quadratic form
    k = sp.symbols("k1:4", real=True)
    c1, c2, c3 = sp.symbols("c1 c2 c3", real=True)

    def pieces(B, kv):
        Tt = {(j, a, b): sp.I * (kv[a] * B[b, j] - kv[b] * B[a, j]) for j in range(3) for a in range(3) for b in range(3)}
        T1 = sum(Tt[(j, a, b)] * sp.conjugate(Tt[(j, a, b)]) for j in range(3) for a in range(3) for b in range(3))
        T2 = sum(Tt[(j, a, b)] * sp.conjugate(Tt[(b, a, j)]) for j in range(3) for a in range(3) for b in range(3))
        V = [sum(Tt[(a, a, b)] for a in range(3)) for b in range(3)]
        T3 = sum(V[b] * sp.conjugate(V[b]) for b in range(3))
        return [sp.expand(sp.re(sp.expand(z))) for z in (T1, T2, T3)]

    Sr = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"s{min(i, j)}{max(i, j)}", real=True))
    al = sp.Matrix(sp.symbols("al1:4", real=True))
    Aa = sp.Matrix(3, 3, lambda a, j: sum(sp.LeviCivita(a, j, b) * al[b] for b in range(3)))
    fam = lambda q: c1 * q[0] + c2 * q[1] + c3 * q[2]
    dA = sp.expand(fam(pieces(Sr + Aa, k)) - fam(pieces(Sr, k)))
    syms = [c1, c2, c3]
    sol = sp.solve(sp.Poly(dA, *k, *al, *list(set(Sr))).coeffs(), syms, dict=True)
    check("bond rotations drop out of the density iff (c1,c2,c3) is along (1,2,-4)",
          sol == [{c1: -c3 / 4, c2: -c3 / 2}])

    kap = sp.symbols("kappa", positive=True)
    xs = sp.symbols("x1:7", real=True)
    Bt = sp.zeros(3, 3)
    Bt[0, 0], Bt[0, 1], Bt[0, 2], Bt[1, 0], Bt[1, 1], Bt[1, 2] = xs
    M6 = sp.hessian(fam(pieces(Bt, (0, 0, kap))), xs) / 2
    lam = sp.Symbol("lam")
    cp = sp.factor(M6.charpoly(lam).as_expr())
    target = ((lam - kap ** 2 * (2 * c1 - c2))
              * (lam - kap ** 2 * (2 * c1 + c2)) ** 2
              * (lam - kap ** 2 * (2 * c1 + c2 + c3)) ** 2
              * (lam - kap ** 2 * (2 * c1 + c2 + 2 * c3)))
    check("static eigenvalues are kappa^2 times 2c1-c2, 2c1+c2 twice, 2c1+c2+c3 twice, 2c1+c2+2c3",
          sp.expand(cp - target) == 0)
    blind = M6.subs({c1: -c3 / 4, c2: -c3 / 2})
    check("the blind ratio has rank 3", blind.rank() == 3)
    c4 = sp.symbols("c4", real=True)
    beta = c4 / (4 * c1 + 2 * c2 + 4 * c3)
    check("beta = c4/(2(2c1+c2+2c3)) and beta=1 is one hyperplane",
          sp.simplify(beta - c4 / (2 * (2 * c1 + c2 + 2 * c3))) == 0
          and sp.solve(sp.Eq(beta, 1), c4) == [2 * (2 * c1 + c2 + 2 * c3)])

    print()
    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0])
        raise SystemExit(1)
    print("SUMMARY: confirmed - over a second prime the 6^3 constraint rank is 87 against 21 relabelling solutions, and the 4^3 rank is 81; beta stays free.")
    print("HIT: confirmed - the only reach-one ties with T dagger J = 0 on stationary states of the 6^3 torus are the 21 relabellings per component; the quadratic form sees bond rotations off (1,2,-4) and is nondegenerate iff (2c1-c2)(2c1+c2)(2c1+c2+c3)(2c1+c2+2c3) != 0, with beta free.")


if __name__ == "__main__":
    main()
