"""hg55_1 -- CEN2 (second-order cancellation of the S4' average) on the actual d=4, L=3 contours.

Exact integer / Fraction arithmetic only.  Criteria: checks/hg55_1_criteria.md (written first).
Lie algebra: (Z^3 or Q^3, cross product) = so(3) = su(2).  Norm: l1.
"""
import itertools
import random
import sys
from fractions import Fraction

D = 4
L = 3
O = (L - 1) // 2
P_L = 5 * L - 4  # 11


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scal(c, a):
    return tuple(c * x for x in a)


def l1(a):
    return sum(abs(x) for x in a)


ZERO = (0, 0, 0)


def axial_steps(start, end, order):
    """List of (site_from, direction, sign) for the axial path start->end moving coordinates in `order`."""
    steps = []
    cur = list(start)
    for nu in order:
        while cur[nu] != end[nu]:
            if end[nu] > cur[nu]:
                steps.append((tuple(cur), nu, +1))
                cur[nu] += 1
            else:
                steps.append((tuple(cur), nu, -1))
                cur[nu] -= 1
    assert tuple(cur) == tuple(end)
    return steps


def step_letter(step):
    """Return (link, sign): link = (lower endpoint, direction)."""
    site, nu, sgn = step
    if sgn > 0:
        return ((site, nu), +1)
    lower = list(site)
    lower[nu] -= 1
    return ((tuple(lower), nu), -1)


def contour_letters(mu, order, y):
    cX = tuple([O] * D)
    cY = tuple(cX[i] + (L if i == mu else 0) for i in range(D))
    yL = tuple(y[i] + (L if i == mu else 0) for i in range(D))
    letters = []
    for st in axial_steps(cX, y, order):
        letters.append(step_letter(st))
    cur = list(y)
    for _ in range(L):
        letters.append(step_letter((tuple(cur), mu, +1)))
        cur[mu] += 1
    back = axial_steps(cY, yL, order)
    # reverse path: from yL to cY, each step reversed
    for st in reversed(back):
        (link, sgn) = step_letter(st)
        letters.append((link, -sgn))
    return letters


def all_contours(mu, y_list=None, orders=None):
    if orders is None:
        orders = list(itertools.permutations(range(D)))
    if y_list is None:
        y_list = list(itertools.product(range(L), repeat=D))
    out = []
    for order in orders:
        for y in y_list:
            out.append(contour_letters(mu, order, y))
    return out


def b2_twice(word_vals):
    """2*B_2 = sum_{a<b} [z_a, z_b], via prefix sums (exact)."""
    acc = ZERO
    pref = ZERO
    for z in word_vals:
        acc = add(acc, cross(pref, z))
        pref = add(pref, z)
    return acc


# ---------- polynomial-in-eps helpers (vectors with coefficient lists) ----------
def padd(p, q):
    n = max(len(p), len(q))
    out = []
    for i in range(n):
        a = p[i] if i < len(p) else ZERO
        b = q[i] if i < len(q) else ZERO
        out.append(add(a, b))
    return out


def pcross(p, q):
    out = [ZERO] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = add(out[i + j], cross(a, b))
    return out


def pscal(c, p):
    return [scal(c, a) for a in p]


def b2_twice_poly(word_polys):
    acc = [ZERO]
    pref = [ZERO]
    for z in word_polys:
        acc = padd(acc, pcross(pref, z))
        pref = padd(pref, z)
    return acc


def rand_vec(rng, lo, hi, nonzero=False):
    while True:
        v = tuple(rng.randint(lo, hi) for _ in range(3))
        if not nonzero or v != ZERO:
            return v


def main():
    rng = random.Random(55001)
    results = {}
    log = []

    def say(*a):
        s = " ".join(str(x) for x in a)
        log.append(s)
        print(s)

    contours = {mu: all_contours(mu) for mu in range(D)}
    for mu in range(D):
        assert len(contours[mu]) == 24 * 81
        assert max(len(w) for w in contours[mu]) <= P_L
    say("contours per mu:", len(contours[0]), " max word length:", max(len(w) for w in contours[0]), "(p_L = 11)")

    NF = 6
    A1 = A2 = A3 = A6 = True
    A4_zero = True
    A4_nonzero_cubic = False
    A5_fires = False
    a3_margins = []

    for f in range(NF):
        xbar = [rand_vec(rng, -5, 5, nonzero=True) for _ in range(D)]
        # ---------- A1, A2, A6 : direction-constant ----------
        for mu in range(D):
            tot = ZERO
            lin = ZERO
            some_nonzero = False
            for w in contours[mu]:
                vals = [scal(sgn, xbar[link[1]]) for (link, sgn) in w]
                b = b2_twice(vals)
                if b != ZERO:
                    some_nonzero = True
                tot = add(tot, b)
                s = ZERO
                for v in vals:
                    s = add(s, v)
                lin = add(lin, s)
            ncont = len(contours[mu])
            if tot != ZERO:
                A1 = False
                say("A1 FAIL field", f, "mu", mu, "sum 2*B2 =", tot)
            if not some_nonzero:
                A2 = False
                say("A2 FAIL field", f, "mu", mu)
            # avg of letters sum == 3 * xbar_mu
            if scal(Fraction(1, ncont), lin) != scal(L, xbar[mu]):
                A6 = False
                say("A6 FAIL field", f, "mu", mu, lin)
        # ---------- A3 : general field, BA-4 bound ----------
        delta = {}

        def xval(link):
            if link not in delta:
                delta[link] = rand_vec(rng, -1, 1)
            return add(scal(100, xbar[link[1]]), delta[link])

        for mu in range(D):
            tot = ZERO
            for w in contours[mu]:
                vals = [scal(sgn, xval(link)) for (link, sgn) in w]
                tot = add(tot, b2_twice(vals))
            ncont = len(contours[mu])
            avg_b2 = scal(Fraction(1, 2 * ncont), tot)  # B_2 = (1/2)*(2B_2); avg = /ncont
            Dm = max(l1(delta[link]) for w in contours[mu] for (link, _) in w)
            Xm = max(l1(scal(100, xbar[nu])) for nu in range(D))
            bound = Fraction(P_L * (P_L - 1), 4) * Dm * (2 * Xm + Dm)
            lhs = l1(avg_b2)
            if not (lhs <= bound):
                A3 = False
                say("A3 FAIL field", f, "mu", mu, "lhs", lhs, "bound", bound)
            a3_margins.append((lhs, bound))
        # ---------- A4 : eps-scaling ; A5 : control without y-average ----------
        g = {}

        def xpoly(link):
            if link not in g:
                g[link] = rand_vec(rng, -3, 3)
            # coefficients of eps^0, eps^1, eps^2
            return [ZERO, xbar[link[1]], g[link]]

        for mu in range(D):
            tot = [ZERO]
            for w in contours[mu]:
                polys = [pscal(sgn, xpoly(link)) for (link, sgn) in w]
                tot = padd(tot, b2_twice_poly(polys))
            tot = tot + [ZERO] * (6 - len(tot))
            if tot[2] != ZERO:
                A4_zero = False
                say("A4 FAIL (eps^2 coefficient nonzero) field", f, "mu", mu, tot[2])
            if tot[3] != ZERO:
                A4_nonzero_cubic = True
            # control: no y-average (one y = c_X + e_nu, nu != mu), all sigma
            nu = (mu + 1) % D
            ysel = tuple(O + (1 if i == nu else 0) for i in range(D))
            ctrl = all_contours(mu, y_list=[ysel])
            ctot = [ZERO]
            for w in ctrl:
                polys = [pscal(sgn, xpoly(link)) for (link, sgn) in w]
                ctot = padd(ctot, b2_twice_poly(polys))
            ctot = ctot + [ZERO] * (6 - len(ctot))
            if ctot[2] != ZERO:
                A5_fires = True

    say("A1 (avg B2 == 0 exactly, direction-constant, 24 cases):", "PASS" if A1 else "FAIL")
    say("A2 (some single contour has B2 != 0, 24 cases):", "PASS" if A2 else "FAIL")
    worst = max(a3_margins, key=lambda t: t[0] / t[1])
    say("A3 (BA-4 l1 bound, 24 cases):", "PASS" if A3 else "FAIL",
        " max lhs/bound (exact) =", worst[0] / worst[1])
    A4 = A4_zero and A4_nonzero_cubic
    say("A4 (eps^2 coeff == 0 in all 24; eps^3 coeff != 0 somewhere):", "PASS" if A4 else "FAIL",
        " [eps2 zero:", A4_zero, " cubic nonzero somewhere:", A4_nonzero_cubic, "]")
    say("A5 (control: no y-average -> eps^2 coeff != 0 somewhere):", "FIRES" if A5_fires else "DOES NOT FIRE")
    say("A6 (avg letter sum == 3*xbar_mu, 24 cases):", "PASS" if A6 else "FAIL")
    overall = A1 and A2 and A3 and A4 and A6 and A5_fires
    say("OVERALL hg55_1:", "PASS" if overall else "FAIL")
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
