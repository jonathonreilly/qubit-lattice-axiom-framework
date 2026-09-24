#!/usr/bin/env python3
"""Referee for the-blind-walk-beyond-first-order a1.

Author w-jonathonsmac4f50-jd491 (claude-opus-5-5). Own Pauli arithmetic.
"""
import itertools
import sympy as sp

fails = []
I2 = sp.eye(2)
S = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def dot_sigma(v):
    return v[0] * S[0] + v[1] * S[1] + v[2] * S[2]


def series_U(theta, n=3):
    """exp(-i theta·sigma/2) through order n, theta already carrying the bookkeeping parameter."""
    A = -sp.I * dot_sigma(theta) / 2
    U = I2
    term = I2
    for p in range(1, n + 1):
        term = sp.expand(term * A / p)
        U += term
    return sp.expand(U)


def conjugation():
    # (Ux M Ux†)(Ux V Uy†) = Ux (M V) Uy†
    entries = sp.symbols("m00 m01 m10 m11 v00 v01 v10 v11 u00 u01 u10 u11 w00 w01 w10 w11")
    M = sp.Matrix(2, 2, entries[0:4])
    V = sp.Matrix(2, 2, entries[4:8])
    Ux = sp.Matrix(2, 2, entries[8:12])
    Uy = sp.Matrix(2, 2, entries[12:16])
    left = (Ux * M * Ux.H) * (Ux * V * Uy.H)
    right = Ux * (M * V) * Uy.H
    # dagger of a generic matrix is not U.H if symbols are not conjugated; use inverse-free algebraic identity
    # with unitary symbols replaced by explicit SU(2) rationals
    def quat(a, b, c, d):
        # a+bi, c+di with a^2+b^2+c^2+d^2 = 1
        return sp.Matrix([[a + sp.I * b, c + sp.I * d], [-c + sp.I * d, a - sp.I * b]])
    U1 = quat(sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(2, 3), sp.Rational(0))
    # 1/9+4/9+4/9=1
    U2 = quat(sp.Rational(2, 3), sp.Rational(1, 3), sp.Rational(0), sp.Rational(2, 3))
    M2 = S[0] + 2 * S[2]
    V2 = S[1]
    left = sp.expand((U1 * M2 * U1.H) * (U1 * V2 * U2.H))
    right = sp.expand(U1 * (M2 * V2) * U2.H)
    exact = sp.expand(U1 * S[0] * U2.H - (U1 * S[0] * U1.H) * (U1 * U2.H)) == sp.zeros(2)
    report(
        "conjugation",
        left == right and exact,
        "bond matrix transforms as Ux (M V) Uy†, and Mx Vx = Ux sigma Uy†",
    )


def second_order():
    t = sp.symbols("t", real=True)
    vx = sp.Matrix(sp.symbols("x0:3", real=True))
    vy = sp.Matrix(sp.symbols("y0:3", real=True))
    a = 0
    Ux = series_U(t * vx, 2)
    Uy = series_U(t * vy, 2)
    prod = sp.expand(Ux * S[a] * Uy.H)
    got = prod.applyfunc(lambda e: e.subs(t, 0) + t * sp.diff(e, t).subs(t, 0) + t ** 2 * sp.diff(e, t, 2).subs(t, 0) / 2)
    cross = ((vx + vy) / 2).cross(sp.Matrix([1, 0, 0]))
    first = S[a] + t * dot_sigma(cross) + t * (sp.I / 2) * (vy - vx)[a] * I2
    second = (t ** 2 / 4) * dot_sigma(vx) * S[a] * dot_sigma(vy) - t ** 2 * (vx.dot(vx) + vy.dot(vy)) / 8 * S[a]
    claimed = sp.expand(first + second)
    report(
        "second order",
        sp.expand(got - claimed) == sp.zeros(2),
        "Ux sigma_a Uy† through t^2 is the bond-averaged cross product, the scalar (i/2)(theta_y-theta_x)_a, and (1/4)(theta_x·sigma) sigma_a (theta_y·sigma) minus the quadratic term",
    )


def varying_frame():
    t = sp.symbols("t", real=True)
    Ex = sp.Matrix(sp.symbols("e0:3", real=True))
    Ey = sp.Matrix(sp.symbols("f0:3", real=True))
    thx = t * sp.Matrix(sp.symbols("p0:3", real=True))
    thy = t * sp.Matrix(sp.symbols("q0:3", real=True))
    Ux = series_U(thx, 1)
    Uy = series_U(thy, 1)
    raw = sp.expand(Ux * dot_sigma(Ex) * Uy.H)
    bond = raw.applyfunc(lambda e: e.subs(t, 0) + t * sp.diff(e, t).subs(t, 0))
    # scalar part is half the trace
    scalar = sp.expand(sp.trace(bond) / 2)
    qv = sp.Matrix(sp.symbols("q0:3", real=True))
    pv = sp.Matrix(sp.symbols("p0:3", real=True))
    claimed = sp.expand((sp.I / 2) * Ex.dot(qv - pv) * t)
    naive = sp.expand((sp.I / 2) * (Ey.dot(qv) - Ex.dot(pv)) * t)
    extra = sp.expand(naive - claimed)
    expect = sp.expand((sp.I / 2) * t * qv.dot(Ey - Ex))
    report(
        "varying frame",
        sp.expand(scalar - claimed) == 0 and sp.expand(extra - expect) == 0,
        "the scalar weight is E(x)·(theta_y-theta_x); the naive difference of theta·E exceeds it by theta_y·(E(y)-E(x))",
    )


def curl_holonomy():
    k0, k1 = sp.symbols("k0 k1")
    s = sp.Matrix(3, 3, lambda i, j: sp.symbols(f"s{i}{j}"))
    s = (s + s.T) / 2
    # Fourier derivative ∂_j -> I*k_j. curl of column a: (curl v)_i = eps_ijk ∂_j v_k
    eps = lambda i, j, k: (j - i) * (k - j) * (i - k) // 2 if len({i, j, k}) == 3 else 0

    def curl_col(a):
        v = [s[i, a] for i in range(3)]
        out = []
        for i in range(3):
            acc = 0
            for j in range(3):
                for kk in range(3):
                    sign = { (0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1 }.get((i, j, kk), 0)
                    if sign:
                        acc += sign * sp.I * sp.symbols(f"k{j}") * v[kk]
            out.append(acc)
        return out

    # only k0, k1 nonzero
    subs = {sp.symbols("k2"): 0}
    w0 = [c.subs(subs) for c in curl_col(0)]
    w1 = [c.subs(subs) for c in curl_col(1)]
    # holonomy normal (axis 2) of i k0 ω1 - i k1 ω0 with ω = -curl
    hol = sp.expand((-sp.I * k0 * w1[2] + sp.I * k1 * w0[2]).subs(subs))
    # linearized R_0101 of g = 1+2s: k0^2 s11 - 2 k0 k1 s01 + k1^2 s00
    R = sp.expand(k0 ** 2 * s[1, 1] - 2 * k0 * k1 * s[0, 1] + k1 ** 2 * s[0, 0])
    # compare up to a sign convention of the curl; the attempt states the normal component equals that polynomial
    report(
        "curl",
        sp.expand(hol - R) == 0,
        "normal holonomy of omega=-curl(s e_a) equals k0^2 s11 - 2 k0 k1 s01 + k1^2 s00",
    )


def main():
    conjugation()
    second_order()
    varying_frame()
    curl_holonomy()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the bond form with SU(2) links is exactly covariant, links built from the sites' rotations "
        "reproduce U H U†, and the second-order term is (1/4)(theta_x·sigma) sigma_a (theta_y·sigma) minus the quadratic piece. "
        "A varying frame weights the scalar hop by E(x)·(theta_y-theta_x). The curl omega_a=-curl(s e_a) has the linearized curvature of g=1+2s as its holonomy."
    )
    print(
        "SUMMARY: confirmed conjugation, the second-order expansion, the frame-weight correction, and the curl holonomy. "
        "A lattice holonomy beyond the long-wavelength symbol was not constructed, as the attempt says."
    )


if __name__ == "__main__":
    main()
