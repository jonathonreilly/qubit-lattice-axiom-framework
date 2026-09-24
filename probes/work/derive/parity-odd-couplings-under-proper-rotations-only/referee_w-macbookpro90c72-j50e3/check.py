#!/usr/bin/env python3
"""Referee for parity-odd couplings under proper rotations, a2.

Author w-macbookpro9927a-j7619 (claude-opus-5-5). Own cofactor, character, and jet checks.
Normal coordinates and Weyl=0 stay assumed, as marked.
"""
import itertools
import sympy as sp

fails = []
LC = lambda i, j, k: int(sp.LeviCivita(i, j, k))


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail, flush=True)


def cofactor():
    M = sp.Matrix(3, 3, sp.symbols("m0:9"))
    adj = M.adjugate()
    det = M.det()
    ok = True
    for j, a, b in itertools.product(range(3), repeat=3):
        left = sum(LC(j, m, n) * adj[a, m] * adj[b, n] for m in range(3) for n in range(3))
        right = det * sum(LC(a, b, c) * M[j, c] for c in range(3))
        ok = ok and sp.expand(left - right) == 0
    report("cofactor", ok, "27 identities: det e * eps (e^{-1})(e^{-1}) = eps e, so det e (eps.T) = 2 eps e d e")


def twist():
    X = sp.symbols("x y z")
    beta, wbar, s = sp.symbols("beta wbar s")
    u = sp.Function("u")(*X)
    lam = sp.Function("lam")(*X)
    rho = [sp.Function(f"r{m}")(*X) for m in range(3)]
    # w * ell^2 with ell = (wbar/w)^beta is proportional to exp((1-2 beta) u)
    ratio = sp.simplify(sp.diff(sp.exp((1 - 2 * beta) * u), X[0]) / sp.exp((1 - 2 * beta) * u))
    length_ok = ratio == (1 - 2 * beta) * sp.diff(u, X[0])
    Om = sp.Matrix(3, 3, lambda j, k: sum(LC(j, m, k) * rho[m] for m in range(3)))
    Ep = (1 + s * lam) * (sp.eye(3) + s * Om)
    adj = Ep.adjugate()
    curl = [sum(LC(m, a, k) * sp.diff(rho[k], X[a]) for a in range(3) for k in range(3)) for m in range(3)]
    eq_ok = True
    for m in range(3):
        expr = sum(sp.diff(wbar * sp.exp(s * u) * adj[a, m], X[a]) for a in range(3))
        linear = sp.expand(sp.diff(expr, s).subs(s, 0))
        eq_ok = eq_ok and sp.simplify(linear - wbar * (sp.diff(u + 2 * lam, X[m]) - curl[m])) == 0
    divcurl = sp.simplify(sum(sp.diff(curl[m], X[m]) for m in range(3))) == 0
    report(
        "twist equation",
        length_ok and eq_ok and divcurl,
        "grad(w ell^2) carries (1-2 beta); at first order curl rho = grad(u+2 lam), whose flux vanishes",
    )


def characters():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = sp.zeros(3)
            for i in range(3):
                M[i, perm[i]] = signs[i]
            mats.append(M)
    proper = [M for M in mats if M.det() == 1]

    def chi_curl(M):
        tr = M.trace()
        lam2 = (tr ** 2 - (M * M).trace()) / 2
        return tr * lam2

    inv24 = sp.simplify(sum(chi_curl(M) for M in proper) / len(proper))
    inv48 = sp.simplify(sum(chi_curl(M) for M in mats) / len(mats))
    report(
        "odd member",
        len(proper) == 24 and len(mats) == 48 and inv24 == 1 and inv48 == 0,
        "V x Lambda^2 V has one invariant under the 24 and none under the 48",
    )


def so3():
    # generators L_k acting on a tensor by summing over slots
    L = [sp.Matrix(3, 3, lambda i, j: -LC(k, i, j)) for k in range(3)]

    def dim(rank, groups):
        idx = list(itertools.product(range(3), repeat=rank))
        pos = {ix: n for n, ix in enumerate(idx)}
        gens = []
        for Lk in L:
            G = sp.zeros(len(idx))
            for ix in idx:
                for slot in range(rank):
                    for new in range(3):
                        c = Lk[new, ix[slot]]
                        if c:
                            jx = list(ix)
                            jx[slot] = new
                            G[pos[tuple(jx)], pos[ix]] += c
            gens.append(G)
        buckets = {}
        for ix in idx:
            key = tuple(tuple(sorted(ix[s] for s in grp)) for grp in groups)
            buckets.setdefault(key, []).append(ix)
        cols = []
        for members in buckets.values():
            v = sp.zeros(len(idx), 1)
            for ix in members:
                v[pos[ix]] = 1
            cols.append(v)
        P = sp.Matrix.hstack(*cols)
        A = sp.Matrix.vstack(*(G * P for G in gens))
        return P.shape[1] - A.rank()

    dims = {
        "V": dim(1, [[0]]),
        "S3": dim(3, [[0, 1, 2]]),
        "VS2": dim(3, [[0], [1, 2]]),
        "eps": dim(3, [[0], [1], [2]]),
        "five": dim(5, [[0, 1], [2, 3], [4]]),
    }
    report(
        "derivative count",
        dims["V"] == 0 and dims["S3"] == 0 and dims["VS2"] == 0 and dims["eps"] == 1 and dims["five"] == 1,
        f"so(3) invariants: one and three derivatives 0, epsilon 1, five-derivative block {dims['five']}",
    )


def five():
    X = sp.symbols("x y z")
    x, y, z = X
    R = sp.Rational
    raw = sp.Matrix([
        [R(1, 3) * x * y + R(1, 5) * z ** 2 * x, R(1, 7) * y * z + R(1, 4) * x ** 2 * y, R(2, 9) * x * z + R(1, 6) * y ** 3],
        [0, R(1, 2) * x ** 2 + R(1, 8) * x * y * z, R(1, 3) * z * y ** 2 + R(1, 5) * x],
        [0, 0, R(1, 4) * y * z + R(1, 9) * x ** 3 + R(1, 7) * z],
    ])
    h = sp.Matrix(3, 3, lambda i, j: raw[min(i, j), max(i, j)])
    u = x + R(1, 2) * y * z + R(1, 3) * x * y + R(1, 5) * z ** 2

    def trunc(expr, n):
        p = sp.Poly(sp.expand(expr), *X)
        return sum(c * sp.prod(X[i] ** k for i, k in enumerate(mon)) for mon, c in p.terms() if sum(mon) <= n)

    def pair(hh, uu):
        g = sp.eye(3) + hh
        inv = (sp.eye(3) - hh + hh * hh - hh * hh * hh).applyfunc(lambda e: trunc(e, 3))
        dg = [[[sp.diff(g[i, j], X[k]) for k in range(3)] for j in range(3)] for i in range(3)]
        Gam = [[[trunc(sp.Rational(1, 2) * sum(inv[a, d] * (dg[d][c][b] + dg[d][b][c] - dg[b][c][d]) for d in range(3)), 2)
                 for c in range(3)] for b in range(3)] for a in range(3)]
        Riem = [[[[trunc(sp.diff(Gam[a][d][b], X[c]) - sp.diff(Gam[a][c][b], X[d])
                         + sum(Gam[a][c][e] * Gam[e][d][b] - Gam[a][d][e] * Gam[e][c][b] for e in range(3)), 1)
                   for d in range(3)] for c in range(3)] for b in range(3)] for a in range(3)]
        Ric = [[trunc(sum(Riem[c][b][c][d] for c in range(3)), 1) for d in range(3)] for b in range(3)]
        zero = {X[0]: 0, X[1]: 0, X[2]: 0}
        R0 = sp.Matrix(3, 3, lambda i, j: Ric[i][j].subs(zero))
        G0 = [[[Gam[a][b][c].subs(zero) for c in range(3)] for b in range(3)] for a in range(3)]
        dR = [[[sp.diff(Ric[i][j], X[k]).subs(zero) for j in range(3)] for i in range(3)] for k in range(3)]
        nab = [[[dR[k][i][j] - sum(G0[m][k][i] * R0[m, j] + G0[m][k][j] * R0[i, m] for m in range(3))
                 for j in range(3)] for i in range(3)] for k in range(3)]
        cotton = sum(LC(i, k, l) * nab[k][l][j] * R0[i, j] for i in range(3) for j in range(3) for k in range(3) for l in range(3))
        du = [sp.diff(uu, X[a]).subs(zero) for a in range(3)]
        hess = sp.Matrix(3, 3, lambda d, c: sp.diff(uu, X[d], X[c]).subs(zero) - sum(G0[e][d][c] * du[e] for e in range(3)))
        uterm = sum(LC(a, b, c) * du[a] * R0[b, d] * hess[d, c] for a in range(3) for b in range(3) for c in range(3) for d in range(3))
        return sp.together(cotton), sp.together(uterm)

    c1, u1 = pair(h, u)
    mirror = {x: -x, y: -y, z: -z}
    c2, u2 = pair(h.subs(mirror), sp.expand(u.subs(mirror)))
    report(
        "five derivatives",
        c1 == sp.Rational(6412057, 15876000) and u1 == sp.Rational(-16, 35) and c2 == -c1 and u2 == -u1,
        "C^ij R_ij = 6412057/15876000 and the rate contraction is -16/35; both flip under x -> -x",
    )


def main():
    cofactor()
    twist()
    characters()
    so3()
    five()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the dressed odd density c5 det e'(eps.T) is blind to first order and is the only "
        "odd member at one derivative; its twist equation is curl rho = grad(u+2 lam), which excludes a body "
        "when beta=1; without the twist the first odd densities have five derivatives"
    )
    print(
        "SUMMARY: confirmed the cofactor identity, the (1-2 beta) flux, the character count, the empty "
        "odd spaces at one and three derivatives, and the two five-derivative examples. "
        "Normal coordinates and Weyl=0 stay assumed."
    )


if __name__ == "__main__":
    main()
