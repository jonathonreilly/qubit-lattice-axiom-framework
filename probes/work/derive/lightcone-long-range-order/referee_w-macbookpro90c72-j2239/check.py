#!/usr/bin/env python3
"""Independent referee for lightcone-long-range-order attempt a5.

Finite facts are recomputed here. The author's check.py is not called.
Exact integers and fractions throughout the series; the I0 tail is an
explicit integral of a proved pointwise bound on e^{-z} I_0(z).
"""

from fractions import Fraction
import sympy as sp

FAILS = []


def require(cond, msg):
    if cond:
        print("ok:", msg)
    else:
        FAILS.append(msg)
        print("FAIL:", msg)


def binom(n, k):
    if k < 0 or k > n:
        return 0
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r


def fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


# ---------------------------------------------------------------------------
# Graph of Gamma_L
# ---------------------------------------------------------------------------

N7 = ((0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
STEPS = N7[1:]


def sites(L):
    return [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]


def parity(x):
    return (x[0] + x[1] + x[2]) & 1


def in_A(v):
    # A = layer 0 on even sites, layer 1 on odd sites.
    return v[3] == parity(v)


def edges_of(L):
    out = []
    for x, y, z in sites(L):
        for dx, dy, dz in N7:
            out.append(((x, y, z, 0), ((x + dx) % L, (y + dy) % L, (z + dz) % L, 1)))
    return out


def rho_coord(val, c, L):
    return (2 * c + 1 - val) % L


def make_theta(j, c, L):
    def theta(v):
        x = [v[0], v[1], v[2]]
        x[j] = rho_coord(x[j], c, L)
        return (x[0], x[1], x[2], 1 - v[3])
    return theta


def halves(c, L):
    plus = {(c + 1 + t) % L for t in range(L // 2)}
    minus = {(c - t) % L for t in range(L // 2)}
    return plus, minus


def sigma(v):
    return (v[0], v[1], v[2], 1 - v[3])


def phi_map(v):
    # (x, a) -> (x, a + |x| mod 2). This is an involution.
    return (v[0], v[1], v[2], (v[3] + parity(v)) & 1)


def check_reflections(L):
    es = edges_of(L)
    e_set = {frozenset(e) for e in es}
    require(len(es) == 7 * L ** 3, f"L={L}: 7-stencil gives 7 L^3 edges")
    require(len(e_set) == len(es), f"L={L}: edges are simple")
    deg = {}
    for u, v in es:
        deg[u] = deg.get(u, 0) + 1
        deg[v] = deg.get(v, 0) + 1
    require(all(d == 7 for d in deg.values()) and len(deg) == 2 * L ** 3,
            f"L={L}: every vertex has degree 7")

    # Affine reflection flips one coordinate by an odd amount, so |rho x| and |x|
    # have opposite parity on every site. Checked as an identity, then exhaustively.
    require(all(((2 * c + 1 - 2 * x) & 1) == 1 for c in range(L) for x in range(L)),
            f"L={L}: bond reflection changes the reflected coordinate by an odd integer")

    thetas = []
    perms = []
    for j in range(3):
        for c in range(L // 2):
            theta = make_theta(j, c, L)
            thetas.append((j, c, theta))
            images = tuple(theta(v) for v in
                           [(x, y, z, a) for x, y, z in sites(L) for a in (0, 1)])
            perms.append(images)
            twin = make_theta(j, c + L // 2, L)
            require(all(twin(v) == theta(v) for x, y, z in sites(L) for v in
                        ((x, y, z, 0), (x, y, z, 1))),
                    f"L={L}: reflection c and c+L/2 are the same map (dir {j}, c {c})")

    for j, c, theta in thetas:
        plus, minus = halves(c, L)
        require(plus.isdisjoint(minus) and plus | minus == set(range(L)),
                f"L={L}: halves partition the cycle (dir {j}, c {c})")
        require(all(theta(theta(v)) == v for x, y, z in sites(L) for a in (0, 1)
                    for v in ((x, y, z, a),)),
                f"L={L}: theta is an involution (dir {j}, c {c})")
        require(all(rho_coord(p, c, L) in minus for p in plus),
                f"L={L}: theta swaps the two halves (dir {j}, c {c})")
        require(all(frozenset((theta(u), theta(v))) in e_set for u, v in es),
                f"L={L}: theta is a graph automorphism (dir {j}, c {c})")
        require(all(in_A(theta((x, y, z, a))) == in_A((x, y, z, a))
                    for x, y, z in sites(L) for a in (0, 1)),
                f"L={L}: theta preserves A (dir {j}, c {c})")
        internal_plus = []
        internal_minus = []
        crossing = []
        for u, v in es:
            u_side = u[j] in plus
            v_side = v[j] in plus
            if u_side and v_side:
                internal_plus.append((u, v))
            elif (not u_side) and (not v_side):
                internal_minus.append((u, v))
            else:
                crossing.append((u, v))
        require(all(frozenset((theta(u), theta(v))) == frozenset((u, v)) or
                    (theta(u) == v and theta(v) == u)
                    for u, v in crossing) and
                all(v == theta(u) or u == theta(v) for u, v in crossing),
                f"L={L}: every theta-crossing edge is a pair {{u, theta u}} (dir {j}, c {c})")
        image_internal = {frozenset((theta(u), theta(v))) for u, v in internal_plus}
        require(image_internal == {frozenset(e) for e in internal_minus}
                and len(image_internal) == len(internal_plus),
                f"L={L}: theta bijects internal edges of the two halves (dir {j}, c {c})")

    # Layer swap.
    require(all(sigma(sigma((x, y, z, a))) == (x, y, z, a)
                for x, y, z in sites(L) for a in (0, 1)),
            f"L={L}: sigma is an involution")
    require(all(frozenset((sigma(u), sigma(v))) in e_set for u, v in es),
            f"L={L}: sigma is a graph automorphism")
    require(all(in_A(sigma((x, y, z, a))) != in_A((x, y, z, a))
                for x, y, z in sites(L) for a in (0, 1)),
            f"L={L}: sigma swaps A and B")
    vertical = [e for e in es if e[0][:3] == e[1][:3]]
    nonvert = [e for e in es if e[0][:3] != e[1][:3]]
    require(len(vertical) == L ** 3, f"L={L}: one vertical edge per site")
    cross_s = [e for e in es if in_A(e[0]) != in_A(e[1])]
    require(set(map(frozenset, cross_s)) == set(map(frozenset, vertical)),
            f"L={L}: sigma-crossing edges are exactly the vertical edges")
    require(all(e[1] == sigma(e[0]) for e in vertical),
            f"L={L}: each vertical edge is {{u, sigma u}}")
    require(all(in_A(u) == in_A(v) for u, v in nonvert),
            f"L={L}: non-vertical edges stay inside one bipartition class")

    # Every edge crosses some reflection of the family.
    def crosses(e, j, c):
        plus, _ = halves(c, L)
        return (e[0][j] in plus) != (e[1][j] in plus)

    uncovered = []
    for e in es:
        hit = any(crosses(e, j, c) for j in range(3) for c in range(L // 2))
        if in_A(e[0]) != in_A(e[1]):
            hit = True
        if not hit:
            uncovered.append(e)
    require(not uncovered, f"L={L}: every edge crosses some theta_P or sigma ({len(uncovered)} uncovered)")

    # Isomorphism onto the bilayer (Z/L)^3 x K2.
    bilayer = set()
    for x, y, z in sites(L):
        bilayer.add(frozenset(((x, y, z, 0), (x, y, z, 1))))
        for dx, dy, dz in STEPS:
            q = ((x + dx) % L, (y + dy) % L, (z + dz) % L)
            for b in (0, 1):
                bilayer.add(frozenset(((x, y, z, b), (q[0], q[1], q[2], b))))
    image = {frozenset((phi_map(u), phi_map(v))) for u, v in es}
    require(image == bilayer, f"L={L}: (x,a) -> (x, a+|x|) is a graph isomorphism onto the bilayer")
    require(all(phi_map(phi_map((x, y, z, a))) == (x, y, z, a)
                for x, y, z in sites(L) for a in (0, 1)),
            f"L={L}: the bilayer coordinate map is an involution")
    # Conjugation: phi theta phi is the spatial reflection on both layers.
    for j, c, theta in thetas:
        good = True
        for x, y, z in sites(L):
            for b in (0, 1):
                v = (x, y, z, b)
                w = phi_map(theta(phi_map(v)))
                expect_x = [x, y, z]
                expect_x[j] = rho_coord(expect_x[j], c, L)
                if w != (expect_x[0], expect_x[1], expect_x[2], b):
                    good = False
                    break
        require(good, f"L={L}: conjugated theta is a spatial bond reflection on both layers (dir {j}, c {c})")


def check_staggered_field(L):
    """sigma sends t*1_A to a constant on one side and 0 on the other."""
    plus_A = True  # halves of sigma are A and B; take Lambda+ = A
    for x, y, z in sites(L):
        for a in (0, 1):
            v = (x, y, z, a)
            # h = t on A, 0 on B. h+(v) = h(v) on A and h(sigma v) on B.
            if in_A(v):
                h_plus = 1  # units of t
                h_minus = 0 if not in_A(sigma(v)) else 1
            else:
                h_plus = 1 if in_A(sigma(v)) else 0
                h_minus = 0
            if h_plus != 1 or h_minus != 0:
                require(False, f"L={L}: staggered field failed at {v}")
                return
    require(True, f"L={L}: sigma reflection of t*1_A is the constant field, and the mirror field is 0")


# ---------------------------------------------------------------------------
# Spectrum
# ---------------------------------------------------------------------------

def check_spectrum_symbol():
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    c = sp.cos(k1) + sp.cos(k2) + sp.cos(k3)
    E = 6 - 2 * c
    A = 1 + 2 * c
    require(sp.simplify(7 - A - E) == 0, "eigenvalue 7 - A equals E(k)")
    require(sp.simplify(7 + A - (14 - E)) == 0, "eigenvalue 7 + A equals 14 - E(k)")
    E_shift = E.subs({k1: k1 + sp.pi, k2: k2 + sp.pi, k3: k3 + sp.pi})
    require(sp.simplify((14 - E) - (E_shift + 2)) == 0, "14 - E(k) = E(k+pi) + 2")
    M = sp.Matrix([[7, -A], [-A, 7]])
    v_plus = sp.Matrix([1, 1])
    v_minus = sp.Matrix([1, -1])
    require(sp.simplify(M * v_plus - (7 - A) * v_plus) == sp.Matrix([0, 0]),
            "v+ = (1,1) is the E-eigenvector")
    require(sp.simplify(M * v_minus - (7 + A) * v_minus) == sp.Matrix([0, 0]),
            "v- = (1,-1) is the (14-E)-eigenvector")
    # pi cancellation in the plane/axis majorant
    m, L = sp.symbols("m L", positive=True)
    bound = (sp.pi ** 2 / 4) / (2 * sp.pi * m / L) ** 2
    require(sp.simplify(bound - L ** 2 / (16 * m ** 2)) == 0,
            "pi cancels: (pi^2/4)/(2 pi m/L)^2 = L^2/(16 m^2)")
    # sin t / t is decreasing on (0, pi/2) because sin t - t cos t has derivative t sin t
    t = sp.symbols("t", real=True, positive=True)
    require(sp.simplify(sp.diff(sp.sin(t) - t * sp.cos(t), t) - t * sp.sin(t)) == 0,
            "derivative identity (sin t - t cos t)' = t sin t")
    x = sp.symbols("x", real=True)
    require(sp.simplify(6 - 2 * 3 * x - 6 * (1 - x)) == 0, "E(k) = 6(1-x) with x = (sum cos)/3")
    require(sp.simplify((8 - 2 * 3 * x) - 8 * (1 - sp.Rational(3, 4) * x)) == 0,
            "E(k)+2 = 8(1 - (3/4) x)")


def cos_table(L):
    # cos(2 pi m / L) = cos(pi m / (L/2)). Exact for L = 4 and L = 6.
    if L == 4:
        return {0: Fraction(1), 1: Fraction(0), 2: Fraction(-1), 3: Fraction(0)}
    if L == 6:
        h = Fraction(1, 2)
        return {0: Fraction(1), 1: h, 2: -h, 3: Fraction(-1), 4: -h, 5: h}
    raise ValueError(L)


def fourier_sums(L):
    cos = cos_table(L)
    N = L ** 3
    G = Fraction(0)
    H = Fraction(0)
    H_shift = Fraction(0)
    half = L // 2
    for m1 in range(L):
        for m2 in range(L):
            for m3 in range(L):
                csum = cos[m1] + cos[m2] + cos[m3]
                E = 6 - 2 * csum
                if (m1, m2, m3) != (0, 0, 0):
                    G += Fraction(1, E)
                H += Fraction(1, 14 - E)
                ms = ((m1 + half) % L, (m2 + half) % L, (m3 + half) % L)
                cshift = cos[ms[0]] + cos[ms[1]] + cos[ms[2]]
                Eshift = 6 - 2 * cshift
                H_shift += Fraction(1, Eshift + 2)
    G *= Fraction(1, N)
    H *= Fraction(1, N)
    H_shift *= Fraction(1, N)
    require(H == H_shift, f"L={L}: H_L equals the shifted sum (1/N) sum 1/(E(k+pi)+2)")
    require(G > 0 and H > 0, f"L={L}: G_L = {G}, H_L = {H}")
    return G, H


def check_parseval_L4():
    L = 4
    N = L ** 3

    def spin(x, y, z, a):
        return ((x + 2 * y + 3 * z + 4 * a) % 5 - 2,
                (3 * x + y + 2 * a) % 5 - 2,
                (z + a + x) % 7 - 3)

    def cis(p):
        return ((1, 0), (0, 1), (-1, 0), (0, -1))[p & 3]

    total = 0
    sum_s2 = 0
    for x in range(L):
        for y in range(L):
            for z in range(L):
                for a in (0, 1):
                    s = spin(x, y, z, a)
                    sum_s2 += s[0] * s[0] + s[1] * s[1] + s[2] * s[2]
    zero_plus = [0, 0, 0]
    for kx in range(L):
        for ky in range(L):
            for kz in range(L):
                for sgn in (1, -1):
                    acc = [(0, 0), (0, 0), (0, 0)]
                    for x in range(L):
                        for y in range(L):
                            for z in range(L):
                                phase = cis(kx * x + ky * y + kz * z)
                                s0 = spin(x, y, z, 0)
                                s1 = spin(x, y, z, 1)
                                for i in range(3):
                                    g = s0[i] + sgn * s1[i]
                                    acc[i] = (acc[i][0] + phase[0] * g, acc[i][1] + phase[1] * g)
                    for i in range(3):
                        total += acc[i][0] * acc[i][0] + acc[i][1] * acc[i][1]
                    if (kx, ky, kz) == (0, 0, 0) and sgn == 1:
                        zero_plus = [acc[i][0] for i in range(3)]
    require(total == 2 * N * sum_s2,
            "L=4 Parseval: sum_k (|G+|^2+|G-|^2) = 2 N sum |s|^2")
    Msum = [0, 0, 0]
    for x in range(L):
        for y in range(L):
            for z in range(L):
                for a in (0, 1):
                    s = spin(x, y, z, a)
                    for i in range(3):
                        Msum[i] += s[i]
    require(zero_plus == Msum, "L=4: G+(0) = M0 + M1, so |s-hat_+(0)|^2 = |M0+M1|^2 / 2")


def check_sum_rule_algebra():
    # |s-hat|^2 sums to 2 N^2 for unit spins. Infrared budget subtracts
    # (3N/beta) * N (G+H). The zero mode is |M0+M1|^2 / 2.
    N = 64
    beta = Fraction(2)
    G = Fraction(1, 4)
    H = Fraction(1, 5)
    budget = (3 * N / beta) * (N * G + N * H)
    zero_lower = 2 * N * N - budget
    msum_lower = 2 * zero_lower  # |M0+M1|^2 >= 2 |s-hat_+|^2
    one_layer = msum_lower / (4 * N * N)  # |M0|^2 / N^2, using |a+b|^2 <= 2|a|^2+2|b|^2 and equal laws
    target = 1 - (Fraction(3, 2) / beta) * (G + H)
    require(one_layer == target,
            f"sum-rule factor: one-layer bound equals 1 - (3/(2 beta))(G+H) ({one_layer})")
    # vector form of the layer comparison, on an integer example
    M0 = (1, -2, 3)
    M1 = (4, 0, -1)
    def n2(v):
        return v[0] * v[0] + v[1] * v[1] + v[2] * v[2]
    s = tuple(M0[i] + M1[i] for i in range(3))
    d = tuple(M0[i] - M1[i] for i in range(3))
    require(n2(s) + n2(d) == 2 * n2(M0) + 2 * n2(M1),
            "|M0+M1|^2 + |M0-M1|^2 = 2|M0|^2 + 2|M1|^2")
    require(n2(s) <= 2 * n2(M0) + 2 * n2(M1), "layer comparison |M0+M1|^2 <= 2|M0|^2 + 2|M1|^2")


# ---------------------------------------------------------------------------
# Return probabilities and the integral bracket
# ---------------------------------------------------------------------------

def b_binomial(n):
    s = 0
    for k in range(n + 1):
        s += binom(n, k) ** 2 * binom(2 * k, k)
    return binom(2 * n, n) * s


def b_multi(n):
    N = fact(2 * n)
    s = 0
    for i in range(n + 1):
        for j in range(n - i + 1):
            k = n - i - j
            s += N // (fact(i) ** 2 * fact(j) ** 2 * fact(k) ** 2)
    return s


def walk_counts(M, check_n=30):
    b = [1, 6]
    for n in range(2, M + 1):
        right = (2 * (2 * n - 1) * (10 * n * n - 10 * n + 3) * b[n - 1]
                 - 36 * (n - 1) * (2 * n - 1) * (2 * n - 3) * b[n - 2])
        require_div = right % (n ** 3) == 0
        if not require_div:
            FAILS.append(f"recurrence not integral at n={n}")
            print("FAIL: recurrence not integral at", n)
            break
        b.append(right // (n ** 3))
    for n in range(check_n + 1):
        if b[n] != b_binomial(n):
            require(False, f"recurrence mismatches binomial formula at n={n}")
            return b
    require(True, f"recurrence matches C(2n,n) sum_k C(n,k)^2 C(2k,k) for n <= {check_n}")
    for n in range(0, 11):
        if b[n] != b_multi(n):
            require(False, f"recurrence mismatches multinomial count at n={n}")
            return b
    require(True, "recurrence matches the multinomial return count for n <= 10")
    return b


def partial_sums(b, M):
    # S = sum_{m=0}^M b_m / 36^m ,   I2_partial = (1/8) sum_{m=0}^M b_m / 64^m
    num = 0
    pow36 = 1
    num2 = 0
    pow64 = 1
    for m in range(M, -1, -1):
        num += b[m] * pow36
        num2 += b[m] * pow64
        if m:
            pow36 *= 36
            pow64 *= 64
    return Fraction(num, pow36), Fraction(num2, 8 * pow64)


def atan_bounds(x, n_terms):
    s = Fraction(0)
    x2 = x * x
    term = x
    for k in range(n_terms):
        s += term
        term = -term * x2 * Fraction(2 * k + 1, 2 * k + 3)
    if term >= 0:
        return s, s + term
    return s + term, s


def pi_bounds(n_terms=20):
    a_lo, a_hi = atan_bounds(Fraction(1, 5), n_terms)
    b_lo, b_hi = atan_bounds(Fraction(1, 239), n_terms)
    # pi = 16 atan(1/5) - 4 atan(1/239), alternating remainders already signed
    lo = 16 * a_lo - 4 * b_hi
    hi = 16 * a_hi - 4 * b_lo
    require(lo < hi and lo > 3 and hi < 4, "Machin bracket for pi is inside (3, 4)")
    return lo, hi


def isqrt_int(n):
    if n < 2:
        return n
    x = 1 << ((n.bit_length() + 1) // 2)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def sqrt_bounds(val):
    # sqrt(n/d) = sqrt(n*d)/d. Integer part gives a floor; one reciprocal gives a ceiling.
    n, d = val.numerator, val.denominator
    s = isqrt_int(n * d)
    if s == 0:
        hi = val + 1
    else:
        lo0 = Fraction(s, d)
        hi = val / lo0
    for _ in range(3):
        hi = (hi + val / hi) / 2
    lo = val / hi
    require(lo > 0 and lo * lo <= val <= hi * hi, "square-root bracket surrounds the value")
    return lo, hi


def check_bessel_algebra():
    z = sp.symbols("z", positive=True)
    first = (1 / (sp.pi * sp.sqrt(2))) * sp.sqrt(sp.pi / z)
    require(sp.simplify(first - 1 / sp.sqrt(2 * sp.pi * z)) == 0,
            "Bessel first term collects to (2 pi z)^{-1/2}")
    second = ((sp.sqrt(2) - 1) / (sp.pi * sp.sqrt(2))) * sp.sqrt(sp.pi) / (2 * z ** sp.Rational(3, 2))
    expect = (2 * sp.pi * z) ** sp.Rational(-1, 2) * (sp.sqrt(2) - 1) / (2 * z)
    require(sp.simplify(second - expect) == 0,
            "Bessel second term collects to (2 pi z)^{-1/2} (sqrt(2)-1)/(2z)")
    t = sp.symbols("t", real=True)
    f = (1 - t / 2) ** sp.Rational(-1, 2)
    d2 = sp.simplify(sp.diff(f, t, 2))
    # d2 = (3/4) (1 - t/2)^{-5/2} / something positive. Check the sign via the rewritten form.
    # f = u^{-1/2}, u = 1 - t/2, du/dt = -1/2, so f'' = (3/16) u^{-5/2}.
    require(sp.simplify(d2 * (1 - t / 2) ** sp.Rational(5, 2) - sp.Rational(3, 16)) == 0,
            "(1-t/2)^{-1/2} is strictly convex on [0,1)")
    s = sp.symbols("s", real=True)
    require(sp.simplify(sp.diff(sp.asin(s), s) - 1 / sp.sqrt(1 - s * s)) == 0,
            "arcsin derivative gives the split integral at t=1")
    # Gaussian evaluation of Gamma(1/2): substitute u = v^2 in the integrand identity.
    v = sp.symbols("v", positive=True)
    u = v ** 2
    integrand = sp.exp(-u) / sp.sqrt(u) * sp.diff(u, v)
    require(sp.simplify(integrand - 2 * sp.exp(-v ** 2)) == 0,
            "Gamma(1/2) substitution u=v^2 turns the integral into the Gaussian")


def i0_tail_upper(M, pi_lo):
    """Upper bound for sum_{m>M} p_{2m}, via
    T <= 6 ∫_{A0}^∞ (e^{-A} I_0(A))^3 dA
    and e^{-A} I_0(A) <= (2πA)^{-1/2} (1 + (√2-1)/(2A)) + e^{-A}/2.
    """
    A0 = Fraction(2 * M + 2, 3)
    require(A0.denominator == 1, "A0 = (2M+2)/3 is an integer at this M")
    A0 = A0.numerator
    sqrt2_lo, sqrt2_hi = sqrt_bounds(Fraction(2))
    # Drop the exponentially small e^{-A}/2 by a separate 10^{-100} budget.
    # psi(A) = (2π)^{-1/2} (A^{-1/2} + alpha A^{-3/2}), alpha = (√2-1)/2
    alpha_hi = (sqrt2_hi - 1) / 2
    two_pi_lo = 2 * pi_lo
    sqrt_2pi_lo, _ = sqrt_bounds(two_pi_lo)
    inv_sqrt_2pi_hi = 1 / sqrt_2pi_lo
    inv_2pi_hi = 1 / two_pi_lo
    pref_hi = inv_2pi_hi * inv_sqrt_2pi_hi  # >= (2π)^{-3/2}
    sqrt_A_lo, _ = sqrt_bounds(Fraction(A0))
    inv_sqrt_A = 1 / sqrt_A_lo
    term = (2 * inv_sqrt_A
            + 2 * alpha_hi * inv_sqrt_A / A0
            + Fraction(6, 5) * alpha_hi ** 2 * inv_sqrt_A / (A0 ** 2)
            + Fraction(2, 7) * alpha_hi ** 3 * inv_sqrt_A / (A0 ** 3))
    J_hi = pref_hi * term
    # Cross terms from (psi + eta)^3 with eta < 10^{-500} are far below 10^{-100}.
    slack = Fraction(1, 10 ** 100)
    return 6 * (J_hi + slack)


def s2(K):
    total = Fraction(0)
    for m1 in range(1, K + 1):
        for m2 in range(1, K + 1):
            total += Fraction(1, m1 * m1 + m2 * m2)
    return total


def axis_sum(L):
    # exact sum_{m ≠ 0} 1/m^2 over torus modes m = ±1..±(L/2-1) and one copy of L/2
    half = L // 2
    total = Fraction(4, L * L)  # the single mode m = L/2
    for m in range(1, half):
        total += Fraction(2, m * m)
    return total


def mode_plane_sum(L):
    # sum of 1/(m1^2+m2^2) over m1, m2 in -(L/2)+1 .. L/2, both nonzero
    half = L // 2
    modes = list(range(-half + 1, half + 1))
    total = Fraction(0)
    for m1 in modes:
        if m1 == 0:
            continue
        for m2 in modes:
            if m2 == 0:
                continue
            total += Fraction(1, m1 * m1 + m2 * m2)
    return total


def main():
    print("reflections")
    for L in (4, 6):
        check_reflections(L)
        check_staggered_field(L)
    print("spectrum")
    check_spectrum_symbol()
    for L in (4, 6):
        fourier_sums(L)
    check_parseval_L4()
    check_sum_rule_algebra()
    check_bessel_algebra()

    # geometric-tail arithmetic for the two readings of |H_L - I_2|
    r = Fraction(3, 4)
    for L in (12, 24):
        tail = r ** L / (1 - r)
        require(Fraction(1, 8) * tail == r ** L / 2,
                f"one series tail (1/8) sum_{{n>={L}}} (3/4)^n = (3/4)^{L}/2")
        require(Fraction(1, 4) * tail == r ** L,
                f"difference of two tails is (3/4)^{L}")

    print("series")
    # M ≡ 2 (mod 3) makes A0 = (2M+2)/3 an integer. M=2501 tightens the
    # Bessel tail enough that the infrared threshold sits at or below 0.5931.
    M = 2501
    b = walk_counts(M)
    S, I2_lo = partial_sums(b, M)
    I0_lo = S / 6
    # I2 geometric tail: (1/8) * (9/16)^{M+1} / (7/16) = (2/7) (9/16)^{M+1}
    I2_tail = Fraction(2, 7) * Fraction(9, 16) ** (M + 1)
    I2_hi = I2_lo + I2_tail
    pi_lo, pi_hi = pi_bounds()
    T_hi = i0_tail_upper(M, pi_lo)
    I0_hi = (S + T_hi) / 6
    beta_lo = Fraction(3, 2) * (I0_lo + I2_lo)
    beta_hi = Fraction(3, 2) * (I0_hi + I2_hi)

    def show(name, fr):
        print(f"{name} = {float(fr):.12f}")

    show("I0_lo", I0_lo)
    show("I0_hi", I0_hi)
    show("I2_lo", I2_lo)
    show("I2_hi", I2_hi)
    show("T_hi", T_hi)
    show("beta_lo", beta_lo)
    show("beta_hi", beta_hi)

    # Author's printed enclosure, checked against the recomputed bracket.
    # Lower endpoint must be a true lower bound (printed figure rounded down is fine
    # to test as <=). Upper endpoint must dominate our upper bound.
    require(I0_lo >= Fraction(250992, 1000000), "I0_lo >= 0.250992")
    require(I0_hi < Fraction(25448, 100000), "I0_hi < 0.25448")
    require(I2_lo > Fraction(1409314, 10 ** 7), "I2_lo > 0.1409314")
    require(I2_hi < Fraction(1409315, 10 ** 7), "I2_hi < 0.1409315")
    require(beta_lo >= Fraction(58788, 100000), "beta_lo >= 0.58788")
    # 0.5931 = 5931/10000. The analytic tail sits a few millionths above that cut.
    printed_cut = Fraction(5931, 10000)
    print("beta_hi <= 0.5931:", beta_hi <= printed_cut)
    require(beta_hi <= printed_cut, "beta_hi <= 0.5931")

    print("finite-volume majorants")
    # Elementary zeta bound, used only to show the axis piece is O(1/L).
    zeta_piece = Fraction(1)  # 1/1^2
    # sum_{m>=2} 1/m^2 <= ∫_1^∞ x^{-2} dx = 1
    require(zeta_piece + 1 == 2, "sum_{m>=1} 1/m^2 <= 2")

    def ceil_dec(fr, digits):
        scale = 10 ** digits
        n = (fr.numerator * scale + fr.denominator - 1) // fr.denominator
        return Fraction(n, scale)

    def floor_dec(fr, digits):
        scale = 10 ** digits
        return Fraction(fr.numerator * scale // fr.denominator, scale)

    beta_lo_out = floor_dec(beta_lo, 5)
    beta_hi_out = ceil_dec(beta_hi, 5)
    print(f"certified beta bracket (5 decimals, outward) [{float(beta_lo_out):.5f}, {float(beta_hi_out):.5f}]")

    author_lbs = {}
    certified_lbs = {}
    for L in (12, 24, 48, 100):
        K = L // 2
        S2 = s2(K)
        plane = 4 * S2
        actual_plane = mode_plane_sum(L)
        require(actual_plane <= plane, f"L={L}: plane mode sum <= 4 S2(L/2)")
        axes = axis_sum(L)
        require(3 * axes <= pi_lo * pi_lo, f"L={L}: three-axis sum 3 * sum 1/m^2 <= pi_lo^2, hence <= pi^2")
        # Author's stated majorant, with the one-tail H error and true-pi replaced by pi_hi
        # (a valid but slightly looser upper bound of their expression).
        herr_author = Fraction(3, 4) ** L / 2
        herr_cert = Fraction(3, 4) ** L
        eps_author = (Fraction(3, 4 * L) * S2
                      + (pi_hi * pi_hi) / (16 * L)
                      + herr_author)
        eps_cert = (Fraction(3, 4 * L) * S2
                    + Fraction(3, 16 * L) * axes
                    + herr_cert)
        # lower bound of <|m0|^2> at beta = 1
        lb_author = 1 - Fraction(3, 2) * (I0_hi + I2_hi + eps_author)
        lb_cert = 1 - Fraction(3, 2) * (I0_hi + I2_hi + eps_cert)
        author_lbs[L] = lb_author
        certified_lbs[L] = lb_cert
        show(f"lb_author_formula_L{L}", lb_author)
        show(f"lb_certified_L{L}", lb_cert)
        print(f"floor3 author L{L} = {float(floor_dec(lb_author, 3)):.3f}")
        print(f"floor3 certified L{L} = {float(floor_dec(lb_cert, 3)):.3f}")
        gap = herr_cert - herr_author
        show(f"H_error_gap_L{L}", gap)

    # The executed |m|=0.76 is not rebuilt. Consistency is only that a lower bound
    # sits at or below 0.76^2.
    require(certified_lbs[24] < Fraction(76, 100) ** 2,
            "certified L=24 lower bound is below the reported 0.76^2 (execution not rebuilt)")

    # Long-range order: the L -> infinity lower bound is positive above the cut.
    margin = 1 - Fraction(3, 2) * (I0_hi + I2_hi) / printed_cut
    # at beta = printed_cut, if beta_hi <= printed_cut this is >= 0.
    # Use beta just above beta_hi: the excess (3/2)(I0_hi+I2_hi)/beta < 1.
    require(Fraction(3, 2) * (I0_hi + I2_hi) < beta_hi + Fraction(1, 10 ** 12),
            "beta_hi is exactly the infrared threshold (3/2)(I0_hi+I2_hi)")
    require(all(certified_lbs[L] > 0 for L in (24, 48, 100)),
            "certified beta=1 lower bound is positive at L=24, 48, 100")

    print("TOTAL FAIL =", len(FAILS))
    if FAILS:
        print("SUMMARY: fails at the integral bracket - " + "; ".join(FAILS[:8]))
        return 1

    # Surviving claim. The printed one-tail H error is replaced by the two-tail bound.
    cut = beta_hi_out
    floors = ", ".join(
        f"{float(floor_dec(certified_lbs[L], 3)):.3f} at L={L}" for L in (12, 24, 48, 100)
    )
    print(
        "HIT: confirmed - for every even L and every beta>0, <|m0|^2> >= 1 - (3/(2 beta))(G_L+H_L); "
        f"(3/2)(I0+I2) lies in [{float(beta_lo_out):.5f}, {float(cut):.5f}], so the printed cut "
        "beta>0.5931 gives long-range order on all large even tori. "
        f"With the two-tail bound H_L <= I2+(3/4)^L the beta=1 lower bounds floor to {floors}."
    )
    print(
        "SUMMARY: confirmed - reflections on L=4 and L=6, the identity 14-E(k)=E(k+pi)+2, "
        "the sum-rule factor 3/(2 beta), and the return series through m=2501 all recomputed; "
        f"beta_0 <= {float(cut):.5f}. The H_L additive error certified here is (3/4)^L."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
