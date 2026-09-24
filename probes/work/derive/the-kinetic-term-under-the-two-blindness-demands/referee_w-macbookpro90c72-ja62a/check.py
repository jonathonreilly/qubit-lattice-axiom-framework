#!/usr/bin/env python3
"""Referee for the-kinetic-term-under-the-two-blindness-demands a1.

Author w-macbookpro90c72-j93ca (claude-opus-5-5). Own sympy identities.
"""
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def split():
    s = sp.symbols("s0:6")
    a = sp.symbols("a0:3")
    S = sp.Matrix([[s[0], s[3], s[4]], [s[3], s[1], s[5]], [s[4], s[5], s[2]]])
    A = sp.Matrix([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    K = S + A
    I1 = sp.expand((K * K.T).trace())
    I2 = sp.expand((K * K).trace())
    Ss = sp.expand((S * S).trace())
    Aa = sp.expand((A * A.T).trace())
    ok = sp.expand(I1 - (Ss + Aa)) == 0 and sp.expand(I2 - (Ss - Aa)) == 0
    ok &= sp.expand(K.trace() - S.trace()) == 0
    report(
        "invariant split",
        bool(ok),
        "I1 = |S|^2+|A|^2, I2 = |S|^2-|A|^2, and tr K sees only S, so c1=c2 kills the antisymmetric piece",
    )


def rotation():
    w = sp.symbols("w", positive=True)
    E = sp.Matrix([[3, 1, 1], [0, 2, 1], [1, 0, 2]])
    Ed = sp.Matrix(3, 3, lambda i, j: sp.symbols(f"d{i}{j}"))
    o = sp.symbols("o0:3")
    Om = sp.Matrix([[0, -o[2], o[1]], [o[2], 0, -o[0]], [-o[1], o[0], 0]])
    g = (E * E.T).inv()
    gi = E * E.T
    K = Ed * E.inv() / w
    Kp = K + E * Om * E.inv() / w
    lowered = g * E * Om * E.inv()
    anti = sp.simplify(lowered + lowered.T) == sp.zeros(3)
    def inv(Km):
        return (
            sp.expand((g * Km * gi * Km.T).trace()),
            sp.expand((Km * Km).trace()),
            sp.expand(Km.trace() ** 2),
        )
    a0, a1 = inv(K), inv(Kp)
    blind = sp.expand(a1[0] + a1[1] - a0[0] - a0[1]) == 0 and sp.expand(a1[2] - a0[2]) == 0
    seen = sp.expand(a1[0] - a1[1] - (a0[0] - a0[1])) != 0
    gdot = -g * (Ed * E.T + E * Ed.T) * g
    Klow = g * K
    sym = sp.simplify((Klow + Klow.T) / 2 + gdot / (2 * w)) == sp.zeros(3)
    report(
        "coin rotation",
        bool(anti and blind and seen and sym and E.det() != 0),
        "on a second rational frame, the lowered rotation is antisymmetric, I1+I2 and I3 are blind, and sym(gK)=-gdot/(2w)",
    )


def isotropic_and_speed():
    al, be, Kc, lam = sp.symbols("alpha beta K lamdot")
    hdot = 2 * lam * sp.eye(3)
    kin = sp.expand(al * (hdot * hdot).trace() + be * hdot.trace() ** 2)
    ck = 12 * al + 36 * be
    ok = sp.simplify(kin - ck * lam ** 2) == 0
    ok &= sp.simplify(ck.subs({al: Kc / 4, be: -Kc / 4}) + 6 * Kc) == 0
    ok &= sp.simplify(ck.subs(be, -al) + 24 * al) == 0
    p2, X = sp.symbols("p2 X", positive=True)
    ok &= sp.solve(sp.Eq(Kc * p2 / (4 * al), p2), al) == [Kc / 4]
    report(
        "isotropic and speed",
        bool(ok),
        "c_k = 12 alpha + 36 beta; at (K/4,-K/4) it is -6K; the top speed X=p^2 holds iff alpha=K/4",
    )


def modes():
    al, be, Kc, X = sp.symbols("alpha beta K X")
    p = sp.Matrix(sp.symbols("p1:4"))
    hs = sp.symbols("h11 h22 h33 h12 h13 h23")
    u = sp.symbols("u")
    H = sp.Matrix([[hs[0], hs[3], hs[4]], [hs[3], hs[1], hs[5]], [hs[4], hs[5], hs[2]]])
    P = p
    p2 = (P.T * P)[0]
    tr = H.trace()
    R1 = -((P.T * H * P)[0] - p2 * tr)
    R2 = (
        -sp.Rational(1, 4) * p2 * sum(H.multiply_elementwise(H))
        + sp.Rational(1, 2) * ((H * P).T * (H * P))[0]
        - sp.Rational(1, 2) * (P.T * H * P)[0] * tr
        + sp.Rational(1, 4) * p2 * tr ** 2
    )
    kin = al * sum(H.multiply_elementwise(H)) + be * tr ** 2
    pot = Kc * (u * R1 + R2)
    vars_ = list(hs) + [u]
    rows = [[sp.diff(X * sp.diff(kin, v) + sp.diff(pot, v), w) for w in vars_] for v in vars_]
    M = sp.Matrix(rows)
    det = sp.factor(M.det().subs(Kc, 1))
    target = X ** 3 * al ** 2 * (al + be) * p2 ** 2 * (p2 - 4 * al * X) ** 2
    ratio = sp.simplify(det / target)
    ok = ratio.free_symbols == set() and ratio != 0
    null = sp.Matrix([p[0] ** 2, p[1] ** 2, p[2] ** 2, p[0] * p[1], p[0] * p[2], p[1] * p[2], 2 * al * X / Kc])
    ok &= sp.simplify(M.subs(be, -al) * null) == sp.zeros(7, 1)
    t = sp.symbols("t")
    zeta = sp.Function("zeta")(t)
    hf = [sp.Function(f"h{i}")(t) for i in range(6)]
    uf = sp.Function("u")(t)

    def lag(hl, ul):
        Hm = sp.Matrix([[hl[0], hl[3], hl[4]], [hl[3], hl[1], hl[5]], [hl[4], hl[5], hl[2]]])
        Hd = sp.diff(Hm, t)
        trm = Hm.trace()
        r1 = -((P.T * Hm * P)[0] - p2 * trm)
        r2 = (
            -sp.Rational(1, 4) * p2 * sum(Hm.multiply_elementwise(Hm))
            + sp.Rational(1, 2) * ((Hm * P).T * (Hm * P))[0]
            - sp.Rational(1, 2) * (P.T * Hm * P)[0] * trm
            + sp.Rational(1, 4) * p2 * trm ** 2
        )
        return al * sum(Hd.multiply_elementwise(Hd)) + be * Hd.trace() ** 2 + Kc * (ul * r1 + r2), r1

    shift = [p[0] ** 2, p[1] ** 2, p[2] ** 2, p[0] * p[1], p[0] * p[2], p[1] * p[2]]
    L0, r1 = lag(hf, uf)
    L1, _ = lag([hf[i] + shift[i] * zeta for i in range(6)], uf - 2 * al * sp.diff(zeta, t, 2) / Kc)
    rest = sp.expand(sp.expand(L1 - L0) - sp.expand(-2 * al * sp.diff(zeta.diff(t) * r1, t)))
    ok &= sp.simplify(rest.subs(be, -al)) == 0 and sp.simplify(rest) != 0
    xi = [p[1] * zeta, -p[0] * zeta, 0]
    dh = [
        2 * p[0] * xi[0],
        2 * p[1] * xi[1],
        2 * p[2] * xi[2],
        p[0] * xi[1] + p[1] * xi[0],
        p[0] * xi[2] + p[2] * xi[0],
        p[1] * xi[2] + p[2] * xi[1],
    ]
    L2, _ = lag([hf[i] + dh[i] for i in range(6)], uf)
    quad = sp.expand(L2 - L0).coeff(sp.diff(zeta, t), 2)
    ok &= sp.simplify(quad - 2 * al * p2 * (p[0] ** 2 + p[1] ** 2)) == 0
    report(
        "modes",
        bool(ok),
        "the 7x7 determinant has the factor (alpha+beta); beta=-alpha makes pp^T a null mode and the gradient relabelling a total derivative; a transverse shift still costs 2 alpha p^2 |xi'|^2",
    )


def main():
    split()
    rotation()
    isotropic_and_speed()
    modes()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - blindness to label-dependent coin rotations leaves block 62's (alpha, beta). "
        "A gradient relabelling in the label, with the rates shifted by -(2 alpha/K) zeta'', is a total derivative "
        "iff beta = -alpha. Transverse relabellings cost 2 alpha p^2 |xi'|^2 for every ratio. "
        "alpha = K/4 matches the walker's top speed and is not fixed by these clauses."
    )
    print(
        "SUMMARY: confirmed the invariant split, the antisymmetric shift on a second frame, "
        "c_k = 12 alpha + 36 beta, the mode factor (alpha+beta), and the transverse cost. "
        "Full blindness to every relabelling in the label fails, as the attempt says."
    )


if __name__ == "__main__":
    main()
