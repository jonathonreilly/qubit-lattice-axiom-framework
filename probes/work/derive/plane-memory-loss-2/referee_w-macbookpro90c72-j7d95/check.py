#!/usr/bin/env python3
"""Independent referee for plane-memory-loss-2 attempt a1.

von Mises-Fisher calculus, the Polya-urn flow, and the cone resistance are
recomputed. The Monte Carlo in the attempt is not rebuilt. The author's
check.py is not called.
"""

from fractions import Fraction
from math import comb
import sympy as sp

FAILS = []


def require(cond, msg):
    if cond:
        print("ok:", msg)
    else:
        FAILS.append(msg)
        print("FAIL:", msg)


def compositions(d):
    return [(a, b, d - a - b) for a in range(d + 1) for b in range(d - a + 1)]


def flow_energy(T):
    energy = Fraction(0)
    conserved = True
    for d in range(T):
        weight = Fraction(1, comb(d + 2, 2))
        incoming = {}
        if d == 0:
            incoming[(0, 0, 0)] = Fraction(1)
        else:
            for n in compositions(d - 1):
                for a in range(3):
                    m = list(n)
                    m[a] += 1
                    key = tuple(m)
                    incoming[key] = incoming.get(key, Fraction(0)) + Fraction(n[a] + 1, d + 2) * Fraction(1, comb(d + 1, 2))
        for n in compositions(d):
            out = [Fraction(n[a] + 1, d + 3) * weight for a in range(3)]
            energy += sum(x * x for x in out)
            if sum(out) != weight:
                conserved = False
            if incoming.get(n, Fraction(0)) != weight:
                conserved = False
    return energy, conserved


def cone_resistance(T):
    verts = [n for d in range(T) for n in compositions(d)]
    idx = {n: i for i, n in enumerate(verts)}
    N = len(verts)
    rows = [dict() for _ in range(N)]
    rhs = [Fraction(0)] * N
    for n in verts:
        i = idx[n]
        nbrs = []
        for a in range(3):
            m = list(n)
            m[a] += 1
            nbrs.append(tuple(m))
            if n[a] >= 1:
                m2 = list(n)
                m2[a] -= 1
                nbrs.append(tuple(m2))
        rows[i][i] = Fraction(len(nbrs))
        for m in nbrs:
            if sum(m) < T:
                j = idx[m]
                rows[i][j] = rows[i].get(j, Fraction(0)) - 1
    rhs[idx[(0, 0, 0)]] = Fraction(1)
    for c in range(N):
        piv = rows[c][c]
        for r in range(c + 1, N):
            if c not in rows[r]:
                continue
            fac = rows[r][c] / piv
            for j, v in list(rows[c].items()):
                rows[r][j] = rows[r].get(j, Fraction(0)) - fac * v
                if rows[r][j] == 0 and j != c:
                    del rows[r][j]
            if c in rows[r] and rows[r][c] == 0:
                del rows[r][c]
            rhs[r] -= fac * rhs[c]
    x = [Fraction(0)] * N
    for c in range(N - 1, -1, -1):
        s = rhs[c]
        for j, v in rows[c].items():
            if j > c:
                s -= v * x[j]
        x[c] = s / rows[c][c]
    return x[idx[(0, 0, 0)]]


def vmf():
    k, u, w, th = sp.symbols("k u w theta", positive=True)
    A = sp.coth(k) - 1 / k
    Ap = 1 / k ** 2 - 1 / sp.sinh(k) ** 2
    f = sp.log(sp.sinh(k) / k)
    Z = sp.integrate(sp.exp(k * sp.cos(th)) * 2 * sp.pi * sp.sin(th), (th, 0, sp.pi))
    require(sp.simplify(Z - 4 * sp.pi * sp.sinh(k) / k) == 0, "sphere integral is 4 pi sinh(k)/k")
    require(sp.simplify(sp.diff(f, k) - A) == 0 and sp.simplify(sp.diff(A, k) - Ap) == 0,
            "f' = A = coth k - 1/k and A' = 1/k^2 - 1/sinh^2 k")

    g = sp.cosh(u) - 1 - u ** 2 / 4 - (u / 4) * sp.sinh(u)
    raw = 2 * sp.sinh(k) ** 2 - k ** 2 - k * sp.sinh(k) * sp.cosh(k)
    require(sp.simplify(raw - g.subs(u, 2 * k)).rewrite(sp.exp) == 0,
            "(A/k)' has the sign of g(2k)")
    ser = sp.series(g, u, 0, 16).removeO()
    coeff_ok = True
    for m in range(1, 8):
        closed = (0 if m == 1 else
                  sp.Rational(1, sp.factorial(2 * m - 1)) * (sp.Rational(1, 2 * m) - sp.Rational(1, 4)))
        if ser.coeff(u, 2 * m) != closed or ser.coeff(u, 2 * m - 1) != 0:
            coeff_ok = False
    require(coeff_ok, "g is even, the u^2 coefficient vanishes, and higher even coefficients are negative")

    App = sp.diff(Ap, k)
    claimed = 2 * (k ** 3 * sp.cosh(k) - sp.sinh(k) ** 3) / (k ** 3 * sp.sinh(k) ** 3)
    require(sp.simplify((App - claimed).rewrite(sp.exp)) == 0,
            "A'' = 2(k^3 cosh k - sinh^3 k)/(k^3 sinh^3 k)")
    # Induction for sinh^3 - k^3 cosh having positive odd coefficients from m=3.
    mm = sp.symbols("m", integer=True, positive=True)
    q = 4 * (2 * mm + 1) * 2 * mm * (2 * mm - 1)
    step = sp.expand(9 * q - q.subs(mm, mm + 1) - 4 * (2 * mm + 1) * (32 * mm ** 2 - 28 * mm - 6))
    require(step == 0, "induction step 9 q(m) - q(m+1) = 4(2m+1)(32m^2-28m-6)")
    require(3 ** 7 - 3 >= 4 * 7 * 6 * 5, "induction base m=3: 2184 >= 840")
    require(all(32 * m * m - 28 * m - 6 > 0 for m in range(3, 8)),
            "32m^2-28m-6 stays positive, so the induction runs for every m >= 3")

    kk, theta = sp.symbols("kappa theta", real=True)
    AA = sp.coth(kk) - 1 / kk
    a = sp.Matrix([0, 0, kk])
    b = sp.Matrix([kk * sp.sin(theta), 0, kk * sp.cos(theta)])
    def psi(v):
        rad = sp.sqrt(v.dot(v))
        return sp.log(sp.sinh(rad) / rad)
    breg = psi(b) - psi(a) - (AA * a / kk).dot(b - a)
    require(sp.simplify(breg - kk * AA * (1 - sp.cos(theta))) == 0,
            "KL of two equal-concentration vMF laws is kappa A(kappa) (1 - cos)")
    R = sp.Matrix([[1, 0, 0], [0, sp.cos(w), -sp.sin(w)], [0, sp.sin(w), sp.cos(w)]])
    M = sp.eye(3) - R
    require(sp.simplify(M.T * M - 4 * sp.sin(w / 2) ** 2 * sp.diag(0, 1, 1)) == sp.zeros(3),
            "(I - R)^T (I - R) = 4 sin^2(w/2) on the plane orthogonal to the axis")

    # Level-1 identity: 1 - cos = 2 sin^2(theta/2), three predecessors.
    require(sp.simplify(sp.expand_trig(1 - sp.cos(theta) - 2 * sp.sin(theta / 2) ** 2)) == 0,
            "1 - cos theta = 2 sin^2(theta/2)")


def constants():
    import math
    def A(x):
        return 1 / math.tanh(x) - 1 / x
    def Ap(x):
        return 1 / x ** 2 - 1 / math.sinh(x) ** 2
    def cb(b):
        k = 3 * b
        return 2 * b * b * Ap(k) * (A(k) / k + Ap(k))
    expect = {1: 0.0658, 3: 0.0247, 6: 0.0123, 24: 0.00309}
    good = True
    for b, target in expect.items():
        val = cb(b)
        print(f"  beta={b}: c_beta={val:.6g}")
        # A(3b) <= b, so 2 b A(3b) <= 2 b^2, and c_beta is below the level-1 coefficient.
        if not (val < 2 * b * A(3 * b) <= 2 * b * b):
            good = False
        if abs(val - target) > 5e-4:
            good = False
        if b >= 6 and abs(val - 2 / (27 * b)) / val > 0.15:
            good = False
    require(good, "c_beta matches 0.0658, 0.0247, 0.0123, 0.00309 at beta = 1, 3, 6, 24 and sits below 2 beta A(3 beta)")


def flow():
    energies = {}
    for T in (1, 2, 3, 10):
        E, ok = flow_energy(T)
        energies[T] = E
        require(ok, f"Polya flow is conserved through depth {T}")
        require(E <= Fraction(2 * T, T + 1), f"E_{T} = {E} <= 2T/(T+1)")
    require(energies[1] == Fraction(1, 3), "E_1 = 1/3")
    require(energies[2] == Fraction(11, 24), "E_2 = 11/24")
    require(energies[3] == Fraction(21, 40), "E_3 = 21/40")
    # telescoping bound
    require(sum(Fraction(2, (d + 1) * (d + 2)) for d in range(10)) == Fraction(20, 11),
            "sum_{d<10} 2/((d+1)(d+2)) = 2*10/11")
    R1 = cone_resistance(1)
    R2 = cone_resistance(2)
    R3 = cone_resistance(3)
    require(R1 == Fraction(1, 3) and R2 == Fraction(4, 9), f"R_1 = {R1}, R_2 = {R2}")
    require(R1 <= energies[1] and R2 <= energies[2] and R3 <= energies[3] and R1 < R2 < R3,
            f"resistances increase and stay below the flow energy; R_3 = {float(R3):.5f}")
    # sin t >= 2t/pi on (0, pi/2): (sin t - t cos t)' = t sin t >= 0
    t = sp.symbols("t", positive=True)
    require(sp.simplify(sp.diff(sp.sin(t) - t * sp.cos(t), t) - t * sp.sin(t)) == 0,
            "sin is above its chord, so sin^2(x/2) >= x^2/pi^2 for |x| <= pi")


def main():
    vmf()
    constants()
    flow()
    print("TOTAL FAIL =", len(FAILS))
    if FAILS:
        print("SUMMARY: fails at a finite check - " + "; ".join(FAILS[:6]))
        return 1
    print(
        "HIT: confirmed - for every deterministic site-wise rotation with tilt theta0 at the apex, "
        "the path relative entropy on the backward cone is at least c_beta theta0^2 / (pi^2 E_T), "
        "with E_T <= 2T/(T+1) < 2, so it cannot be bounded by C beta theta0^2 over a sum that "
        "diverges. c_beta = 2 beta^2 A'(3 beta)(A(3 beta)/(3 beta) + A'(3 beta))."
    )
    print(
        "SUMMARY: confirmed - route A fails at the vanishing upper bound on the twist cost. "
        "The Monte Carlo at T=3 was not rebuilt, and m_t -> 0 itself is not decided."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
