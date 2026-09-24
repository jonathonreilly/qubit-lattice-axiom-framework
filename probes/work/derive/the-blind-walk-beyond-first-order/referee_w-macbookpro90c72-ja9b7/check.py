#!/usr/bin/env python3
"""Independent checks for the blind walk beyond first order, a1.

Pauli arithmetic for the bond expansion, and the plaquette symbol for the curl rule.
"""
import itertools
import sympy as sp

FAILS = []


def ok(name, good, msg):
    print(("ok " if good else "FAIL ") + name + ": " + msg, flush=True)
    if not good:
        FAILS.append(name)


def pauli():
    I = sp.eye(2)
    x = sp.Matrix([[0, 1], [1, 0]])
    y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    z = sp.Matrix([[1, 0], [0, -1]])
    return I, (x, y, z)


def dot(theta, sig):
    acc = sp.zeros(2)
    for i in range(3):
        acc += theta[i] * sig[i]
    return acc


def main():
    I, sig = pauli()
    # covariance: (U M U^dag)(U V W^dag) = U (M V) W^dag
    a, b, c, d = sp.symbols("a b c d")
    U = sp.Matrix([[a, b], [-sp.conjugate(b), sp.conjugate(a)]])
    # use a concrete unitary instead of a symbolic conjugate mess
    Ux = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5)], [sp.Rational(-4, 5), sp.Rational(3, 5)]])
    Uy = sp.Matrix([[sp.Rational(5, 13), sp.Rational(12, 13)], [sp.Rational(-12, 13), sp.Rational(5, 13)]])
    M = sig[0] + 2 * sig[2]
    V = sig[1]
    left = (Ux * M * Ux.T) * (Ux * V * Uy.T)
    right = Ux * (M * V) * Uy.T
    ok("cov", sp.simplify(left - right) == sp.zeros(2), "bond matrix transforms as U_x (M V) U_y^T")

    # V = Ux Uy^dag, M = Ux sig Ux^dag => M V = Ux sig Uy^dag
    MV = (Ux * sig[0] * Ux.T) * (Ux * Uy.T)
    direct = Ux * sig[0] * Uy.T
    ok("exact", sp.simplify(MV - direct) == sp.zeros(2), "M V = U_x sigma_a U_y^dag exactly")

    # second-order expansion
    tx = sp.symbols("tx0 tx1 tx2")
    ty = sp.symbols("ty0 ty1 ty2")
    A = dot(tx, sig) / 2
    B = dot(ty, sig) / 2
    Ux_s = I - sp.I * A - A * A / 2
    Uy_d = I + sp.I * B - B * B / 2
    prod = sp.expand(Ux_s * sig[0] * Uy_d)
    # drop cubic terms: any product of three thetas
    def drop_cubic(expr):
        expr = sp.expand(expr)
        if expr == 0:
            return expr
        out = 0
        for mon, coeff in expr.as_poly(*(tx + ty)).terms():
            if sum(mon) <= 2:
                out += coeff * sp.prod((tx + ty)[i] ** mon[i] for i in range(6))
        return sp.expand(out)
    prod = prod.applyfunc(drop_cubic)
    claimed_2 = (dot(tx, sig) * sig[0] * dot(ty, sig)) / 4 - (sum(t ** 2 for t in tx) + sum(t ** 2 for t in ty)) * sig[0] / 8
    # first-order piece to subtract from prod before comparing second order
    # prod = sig + first + second. Compare full claimed through order 2.
    cross = ((sp.Matrix(tx) + sp.Matrix(ty)) / 2).cross(sp.Matrix([1, 0, 0]))
    first = sig[0] + dot(cross, sig) + sp.I * (ty[0] - tx[0]) / 2 * I
    # (i/2)(ty-tx)_0 is a scalar times the 2x2 identity
    claimed = sp.expand(first + claimed_2).applyfunc(drop_cubic)
    diff = sp.expand(prod - claimed)
    ok("order2", diff == sp.zeros(2), "expansion through second order matches the bond-averaged frame plus the stated quadratic term")

    # varying frame: actual scalar E·(ty-tx), naive differs by ty·(Ey-Ex)
    Ex, Ey = sp.symbols("Ex0 Ex1 Ex2"), sp.symbols("Ey0 Ey1 Ey2")
    actual = sum(Ex[i] * (ty[i] - tx[i]) for i in range(3))
    naive = sum(ty[i] * Ey[i] - tx[i] * Ex[i] for i in range(3))
    gap = sp.expand(naive - actual - sum(ty[i] * (Ey[i] - Ex[i]) for i in range(3)))
    ok("frame", gap == 0, "naive theta·E difference exceeds E(x)·(theta_y-theta_x) by theta_y·(E(y)-E(x))")

    # curl rule vs linearized R_0101, derivative symbol i k
    k0, k1 = sp.symbols("k0 k1")
    s00, s01, s11 = sp.symbols("s00 s01 s11")
    # (omega_a)_c = -eps_cbd * i k_b * s_da
    # holonomy normal component 2 of i k0 omega_1 - i k1 omega_0
    def eps(c, b, d):
        sign = 1
        seq = [c, b, d]
        for p, q in itertools.combinations(range(3), 2):
            if seq[p] > seq[q]:
                seq[p], seq[q] = seq[q], seq[p]
                sign = -sign
        return sign if seq == [0, 1, 2] else 0
    s = sp.zeros(3)
    s[0, 0], s[0, 1], s[1, 0], s[1, 1] = s00, s01, s01, s11
    def omega(a):
        out = [0, 0, 0]
        for c, b, d in itertools.product(range(3), repeat=3):
            e = eps(c, b, d)
            if e:
                out[c] += -e * sp.I * (k0 if b == 0 else (k1 if b == 1 else 0)) * s[d, a]
        return out
    w1, w0 = omega(1), omega(0)
    hol = sp.simplify(sp.I * k0 * w1[2] - sp.I * k1 * w0[2])
    R = sp.expand(k0 ** 2 * s11 - 2 * k0 * k1 * s01 + k1 ** 2 * s00)
    ok("curl", sp.expand(hol - R) == 0, f"plaquette normal equals linearized R_0101 ({hol})")

    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0] + " - independent algebra did not match")
        return
    print(
        "HIT: confirmed - the site-link bond is exactly U H Udag, its second-order term is "
        "(1/4)(theta_x·sigma) sigma_a (theta_y·sigma) minus the squared-angle piece, "
        "and -curl(s e_a) reproduces R_0101"
    )
    print(
        "SUMMARY: confirmed covariance, the exact conjugation, the order-2 expansion, the frame-weight gap, "
        "and the curl holonomy; the bond-reach parameter count was not re-enumerated"
    )


if __name__ == "__main__":
    main()
