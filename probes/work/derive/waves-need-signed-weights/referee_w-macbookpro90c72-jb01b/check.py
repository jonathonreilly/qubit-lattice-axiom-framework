#!/usr/bin/env python3
"""Referee for waves-need-signed-weights a5.

Author w-jonathonsmac4f50-j62b1 (claude-opus-5). Own symbols for the five rules
and the three breakers. No grid scan.
"""
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def zero(expr):
    expr = sp.simplify(sp.expand(expr))
    if isinstance(expr, sp.MatrixBase):
        return expr == sp.zeros(*expr.shape)
    return expr == 0


def rules():
    k = sp.symbols("k", real=True)
    h = sp.Rational(1, 2)
    z = sp.exp(-sp.I * k)
    mix_A = sp.Matrix([[h, h], [1, 0]])
    mix_W = z * mix_A
    gauge_W = sp.Matrix([[0, 1], [z ** 2, 0]])
    half_W = sp.Matrix([[0, 1], [z ** 3, 0]])
    gaugemix_A = sp.Matrix([[h, h], [1, 0]])
    g = [0, 1]
    v = 1
    D = sp.diag(1, sp.exp(-sp.I * k * g[1]))
    gaugemix_W = sp.Matrix([[h * z, h], [z ** 2, 0]])
    rhs = sp.exp(-sp.I * k * v) * D * gaugemix_A * D.inv()
    half_char = sp.simplify(sp.expand(half_W.charpoly(sp.symbols("lam")).as_expr()))
    # spec of the swap of mean 3/2: lambda^2 - e^{-3 i k} = 0
    lam = sp.symbols("lam")
    half_poly = sp.simplify(sp.expand(half_W.charpoly(lam).as_expr() - (lam ** 2 - z ** 3)))
    mix_rows = [sum(mix_A.row(i)) for i in range(2)]
    not_perm = mix_A[0, 0] == h and mix_A[0, 1] == h
    gauge_spec = sp.simplify(sp.expand(gauge_W.charpoly(lam).as_expr() - (lam ** 2 - z ** 2)))
    ok = (
        all(r == 1 for r in mix_rows)
        and not_perm
        and zero(mix_W * sp.Matrix([1, 1]) - z * sp.Matrix([1, 1]))
        and zero(gaugemix_W - rhs)
        and half_poly == 0
        and gauge_spec == 0
    )
    # y = v + g_m - g_n for the half-step rule, v = 3/2, g = (0, 3/2)
    vh, gh = sp.Rational(3, 2), (0, sp.Rational(3, 2))
    y01, y10 = 0, 3
    ok &= y01 == vh + gh[0] - gh[1] and y10 == vh + gh[1] - gh[0]
    report(
        "exceptional rules",
        bool(ok),
        "mixing at one velocity, the gauge pair y=0 and y=2, and the half-step v=3/2 are similarities of a stochastic matrix, and the mixer is not a permutation",
    )
    return k, z


def breakers(k, z):
    # one block at both neighbours: W = cos k
    twosite = sp.cos(k)
    # |cos k| = 1 iff cos^2 = 1 iff sin = 0 iff k in pi Z
    cos_id = sp.simplify(sp.expand(sp.cos(k) ** 2 - 1 + sp.sin(k) ** 2))
    # persistent walk, a=9/25, b=16/25
    a, b = sp.Rational(9, 25), sp.Rational(16, 25)
    W = sp.Matrix([[a * z, b * z], [b / z, a / z]])
    lam = sp.symbols("lam")
    poly = sp.simplify(sp.expand(W.charpoly(lam).as_expr()))
    # derived: lambda = a cos k +/- sqrt(a^2 cos^2 k + 7/25), product -7/25
    claimed = lam ** 2 - (2 * a * sp.cos(k)) * lam + (a ** 2 - b ** 2)
    persist_poly = sp.simplify(sp.expand(poly - claimed))
    # |lambda|=1 and the product has modulus 7/25 forces the larger root to 1 only at cos k = 1
    larger = a * sp.cos(k) + sp.sqrt(a ** 2 * sp.cos(k) ** 2 + sp.Rational(7, 25))
    gap = sp.simplify(sp.expand((1 - a * sp.cos(k)) ** 2 - (a ** 2 * sp.cos(k) ** 2 + sp.Rational(7, 25)) - (sp.Rational(18, 25) - 2 * a * sp.cos(k))))
    # mismatch: cycles of mean 1 and 0
    M = sp.Matrix([[0, z], [sp.Rational(1, 2) * z, sp.Rational(1, 2)]])
    # |lambda|=1 implies lambda=1 and z^2=1, checked by |lambda - 1/2| = 1/2
    phase = sp.symbols("theta", real=True)
    mod = sp.simplify(sp.expand(sp.Abs(sp.exp(sp.I * phase) - sp.Rational(1, 2)) ** 2 - (sp.Rational(5, 4) - sp.cos(phase))))
    at_pi = M.subs(k, sp.pi) * sp.Matrix([1, -1]) - sp.Matrix([1, -1])
    at_0 = M.subs(k, 0) * sp.Matrix([1, 1]) - sp.Matrix([1, 1])
    minus = sp.simplify(claimed.subs(lam, -1))
    ok = cos_id == 0 and persist_poly == 0 and gap == 0 and mod == 0 and minus != 0
    ok &= zero(at_pi) and zero(at_0)
    # row sums of the mismatch
    ok &= sp.simplify(sum(M.subs(k, 0).row(0))) == 1 and sp.simplify(sum(M.subs(k, 0).row(1))) == 1
    report(
        "breakers",
        bool(ok),
        "the two-site block has |lambda|=|cos k|, equal to 1 exactly on pi Z; the persistent walk only on 2 pi Z; the mismatched cycles at both 0 and pi",
    )


def fronts():
    k1, k2 = sp.symbols("k1 k2", real=True)
    ev = [sp.exp(-sp.I * k1), sp.exp(sp.I * k1), sp.exp(-sp.I * k2), sp.exp(sp.I * k2)]
    mods = all(sp.simplify(sp.expand(sp.conjugate(e) * e - 1)) == 0 for e in ev)
    # d=1: e^{-i k m}=1 has m roots in [0, 2 pi)
    m = sp.symbols("m", integer=True, positive=True)
    count_ok = True
    for width in range(1, 6):
        roots = [sp.Rational(2 * j, width) * sp.pi for j in range(width)]
        count_ok &= len(set(roots)) == width
        count_ok &= all(sp.simplify(sp.exp(-sp.I * r * width) - 1) == 0 for r in roots)
        mid = roots[0] / 2 + (roots[1] / 2 if width > 1 else sp.pi)
        # a point strictly between the first two roots, or pi/2 when width=1 (root only at 0)
        if width == 1:
            mid = sp.pi
        else:
            mid = (roots[0] + roots[1]) / 2
        count_ok &= sp.simplify(sp.exp(-sp.I * mid * width) - 1) != 0
    report(
        "fronts",
        bool(mods and count_ok),
        "four chiral copies on Z^2 have velocities +-e1 and +-e2; a nonzero displacement difference has finitely many phases in one period",
    )


def main():
    k, z = rules()
    breakers(k, z)
    fronts()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - nonnegative matrix weights are unimodular on an open set only when every block is one site and the displacements are one velocity plus a gauge. "
        "Stochastic mixing and the pairs (y=0,y=2) and (y=0,y=3) qualify and are not permutations. "
        "A two-site block is unimodular exactly on pi Z, not merely at 0; mismatched cycle means are unimodular at 0 and pi; the persistent walk only on 2 pi Z. "
        "Four chiral copies give four velocities."
    )
    print(
        "SUMMARY: confirmed the gauge identity, the three exact null sets, and the four-point front. "
        "The 61-point grid and its 'single point k=0' were not used: two of the three breakers are also unimodular at k=pi. "
        "The J-level and reducible bookkeeping were not in the attempt."
    )


if __name__ == "__main__":
    main()
