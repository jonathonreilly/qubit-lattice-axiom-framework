#!/usr/bin/env python3
"""Referee for the ledger force identity on the lattice, a2.

Author w-jonathonsmac4f50-j9041 (claude-opus-5-5). Own sparse operators on a 4x3x3 torus.
The continuum rational triple was not rebuilt.
"""
import itertools
import sympy as sp

fails = []
I2 = sp.eye(2)
Z2 = sp.zeros(2)
SIG = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
SITES = list(itertools.product(range(5), range(3), range(3)))


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def shift(x, j, s=1):
    y = list(x)
    y[j] = (y[j] + s) % (5 if j == 0 else 3)
    return tuple(y)


def clean(op):
    return {k: v for k, v in op.items() if v != Z2}


def add(*ops):
    out = {}
    for op in ops:
        for k, v in op.items():
            out[k] = out.get(k, Z2) + v
    return clean(out)


def scale(op, c):
    return clean({k: c * v for k, v in op.items()})


def mul(a, b):
    out = {}
    for (x, y), v in a.items():
        for (y2, z), w in b.items():
            if y == y2:
                out[(x, z)] = out.get((x, z), Z2) + v * w
    return clean(out)


def adj(op):
    return clean({(y, x): v.H for x, y, v in ((p, q, m) for (p, q), m in op.items())})


def eq(a, b):
    keys = set(a) | set(b)
    return all(sp.simplify(a.get(k, Z2) - b.get(k, Z2)) == Z2 for k in keys)


def phiv(x):
    return 2 + sp.Rational((x[0] + 3 * x[1] + 5 * x[2]) % 5, 4)


def T(j, step=1):
    return {(x, shift(x, j, step)): I2 for x in SITES}


def diag(f):
    return { (x, x): f(x) * I2 for x in SITES }


def proj(x):
    return {(x, x): I2}


def coin(M, op):
    return clean({k: M * v for k, v in op.items()})


def sym(op):
    return scale(add(op, adj(op)), sp.Rational(1, 2))


def Cw(j, v, step=1):
    out = {}
    for x in SITES:
        out[(x, shift(x, j, step))] = out.get((x, shift(x, j, step)), Z2) + v(x) / 2 * I2
        xm = shift(x, j, -step)
        out[(x, xm)] = out.get((x, xm), Z2) + v(xm) / 2 * I2
    return clean(out)


J = 0
Tj = [T(j) for j in range(3)]
Sj = [scale(add(Tj[j], scale(adj(Tj[j]), -1)), 1 / (2 * sp.I)) for j in range(3)]
Cj = [scale(add(Tj[j], adj(Tj[j])), sp.Rational(1, 2)) for j in range(3)]
H = add(*[coin(SIG[j], Sj[j]) for j in range(3)])
PHI = diag(phiv)


def bond():
    dphi = lambda x: phiv(shift(x, J, 1)) - phiv(x)
    comm = add(mul(PHI, Sj[J]), scale(mul(Sj[J], PHI), -1))
    comm_ok = eq(scale(comm, sp.I), scale(Cw(J, dphi), -1))
    x0 = (1, 1, 1)
    Cv = Cw(J, dphi)
    Fx = sym(mul(add(mul(proj(x0), Cv), mul(Cv, proj(x0))), mul(H, PHI)))

    def beta(y):
        yp = shift(y, J, 1)
        return sym(add(mul(mul(proj(y), Tj[J]), mul(H, PHI)), mul(mul(proj(yp), adj(Tj[J])), mul(H, PHI))))

    xm = shift(x0, J, -1)
    form = add(scale(beta(x0), dphi(x0) / 2), scale(beta(xm), dphi(xm) / 2))
    # energies are nearest-neighbour; the force reaches two steps
    HW = mul(mul(PHI, H), PHI)

    def energy(y):
        return sym(mul(proj(y), HW))

    def dist(p, q):
        return sum(min(abs(p[i] - q[i]), (5 if i == 0 else 3) - abs(p[i] - q[i])) for i in range(3))

    nn = all(dist(p, q) == 1 for y in SITES for (p, q) in energy(y))
    blk = Fx.get((x0, shift(x0, J, 2)), Z2)
    weight = add(scale(energy(shift(x0, J, 1)), 1), scale(energy(x0), 1))
    weight_blk = weight.get((x0, shift(x0, J, 2)), Z2)
    ratio = phiv(shift(x0, J, 1)) / phiv(x0)
    du = sp.log(phiv(shift(x0, J, 1)) ** 2) - sp.log(phiv(x0) ** 2)
    factors = sp.simplify(sp.exp(du / 2) - ratio) == 0 and sp.simplify(dphi(x0) / phiv(x0) - (ratio - 1)) == 0
    report(
        "bond force",
        comm_ok and eq(Fx, form) and nn and sp.simplify(blk) != Z2 and sp.simplify(weight_blk) == Z2 and factors,
        "f_j is the average of (d phi) times the bond cross-energy; site energies stop at one step and the force reaches two",
    )


def reach():
    Pj = mul(Sj[J], Cj[J])
    T2 = mul(Tj[J], Tj[J])
    ident = eq(Pj, scale(add(T2, scale(adj(T2), -1)), 1 / (4 * sp.I)))
    d2 = lambda x: phiv(shift(x, J, 2)) - phiv(x)
    comm = scale(add(mul(PHI, Pj), scale(mul(Pj, PHI), -1)), sp.I)
    comm_ok = eq(comm, scale(Cw(J, d2, 2), -sp.Rational(1, 2)))
    x0 = (1, 1, 1)
    C2 = Cw(J, d2, 2)
    Fx = scale(sym(mul(add(mul(proj(x0), C2), mul(C2, proj(x0))), mul(H, PHI))), sp.Rational(1, 2))
    blk = Fx.get((x0, shift(x0, J, 3)), Z2)
    report(
        "reach three",
        ident and comm_ok and sp.simplify(blk) != Z2,
        "P_j=(T^2-T^{-2})/(4i) and the reach-three force has a block three steps away",
    )


def curls():
    S3 = list(itertools.product(range(3), repeat=3))

    def s3(x, j, s=1):
        y = list(x)
        y[j] = (y[j] + s) % 3
        return tuple(y)

    B = {(x, a, j): sp.Symbol(f"B{x[0]}{x[1]}{x[2]}{a}{j}") for x in S3 for a in range(3) for j in range(3)}

    def curl(Bf, x, a, b, j):
        return (Bf(s3(x, a), b, j) - Bf(x, b, j)) - (Bf(s3(x, b), a, j) - Bf(x, a, j))

    xi = lambda x, j: sp.Rational((x[0] + 2 * x[1] + 4 * x[2] + j) % 3, 2)
    plus = lambda x, a, j: B[(x, a, j)] + (xi(s3(x, a), j) - xi(x, j))
    plain = lambda x, a, j: B[(x, a, j)]
    same = all(
        sp.expand(curl(plus, x, a, b, j) - curl(plain, x, a, b, j)) == 0
        for x in S3 for a in range(3) for b in range(a) for j in range(3)
    )

    def D(Bf, x):
        c01 = curl(Bf, x, 0, 1, 0)
        div = sum(curl(Bf, x, a, b, a) for a in range(3) for b in range(3))
        return c01 ** 2 + sp.Rational(2, 3) * div

    w = lambda x: 1 + sp.Rational((x[0] + x[1] + 2 * x[2]) % 3, 5)
    gap = sp.expand(sum(w(x) * (D(plus, x) - D(plain, x)) for x in S3))
    E = {k: sp.diff(sum(w(x) * D(plain, x) for x in S3), s) for k, s in B.items()}
    paired = sp.expand(sum(E[(x, a, j)] * (xi(s3(x, a), j) - xi(x, j)) for x in S3 for a in range(3) for j in range(3)))
    report(
        "curl ledger",
        same and gap == 0 and paired == 0,
        "curls ignore B -> B+d xi, so a weighted curl density is invariant and sum E d xi vanishes for every rate field",
    )


def main():
    bond()
    reach()
    curls()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the force density is the average of (difference of phi) times a bond cross-energy. "
        "Site energies reach only one step, so they cannot reproduce the two-step block. "
        "A per-tick curl ledger changes by nothing under B -> B+d xi, for every rate field."
    )
    print(
        "SUMMARY: confirmed the bond form, the two-step obstruction, the reach-three block, and the curl identity. "
        "The continuum second-order triple was not rebuilt."
    )


if __name__ == "__main__":
    main()
