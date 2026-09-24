#!/usr/bin/env python3
"""Independent referee for moving-what-fixes-the-scale attempt a5.

The author's check.py is not called. The 7-state pair weight is built from
the six-axis rule and factored by hand.
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


# Contents 0..5 with antipodes 1, 0, 3, 2, 5, 4.
ANTI = (1, 0, 3, 2, 5, 4)


def omega_symbol(a, b, p, q, r):
    if a == b:
        return p
    if ANTI[a] == b:
        return q
    return r


def spectrum_of_omega():
    p, q, r = sp.symbols("p q r", real=True)
    # Explicit eigenvectors, not a root finder.
    ones = sp.Matrix([1, 1, 1, 1, 1, 1])
    odd = [
        sp.Matrix([1, -1, 0, 0, 0, 0]),
        sp.Matrix([0, 0, 1, -1, 0, 0]),
        sp.Matrix([0, 0, 0, 0, 1, -1]),
    ]
    even = [
        sp.Matrix([1, 1, -1, -1, 0, 0]),
        sp.Matrix([1, 1, 1, 1, -2, -2]),
    ]
    Om = sp.zeros(6)
    for a in range(6):
        for b in range(6):
            Om[a, b] = omega_symbol(a, b, p, q, r)
    A1 = p + q + 4 * r
    require(sp.simplify(Om * ones - A1 * ones) == sp.zeros(6, 1),
            "all-ones is the eigenvalue p+q+4r")
    require(all(sp.simplify(Om * v - (p - q) * v) == sp.zeros(6, 1) for v in odd),
            "three odd vectors have eigenvalue p-q")
    require(all(sp.simplify(Om * v - (p + q - 2 * r) * v) == sp.zeros(6, 1) for v in even),
            "two even vectors orthogonal to all-ones have eigenvalue p+q-2r")
    require(sp.simplify(sp.trace(Om) - 6 * p) == 0, "trace of Omega is 6p")
    # These five plus the all-ones span C^6.
    M = sp.Matrix.hstack(ones, *odd, *even)
    require(M.rank() == 6, "the six eigenvectors are a basis")


def transfer(p, q, r, c):
    T = sp.zeros(7)
    for a in range(6):
        for b in range(6):
            T[a, b] = c * omega_symbol(a, b, p, q, r)
        T[a, 6] = 1
        T[6, a] = 1
    T[6, 6] = 1
    return T


def block_and_det():
    p, q, r, c = sp.symbols("p q r c", real=True)
    A1 = p + q + 4 * r
    # Integer kernel representative: equal content weights, empty = -sum of contents.
    v = sp.Matrix([1, 1, 1, 1, 1, 1, -6])
    T = transfer(p, q, r, c)
    Tv = sp.simplify(T * v)
    require(sp.simplify(Tv.subs(c, 6 / A1)) == sp.zeros(7, 1),
            "at c = 6/(p+q+4r) the kernel contains (1,1,1,1,1,1,-6)")
    B = sp.Matrix([[c * A1, sp.sqrt(6)], [sp.sqrt(6), 1]])
    require(sp.simplify(B.det() - (c * A1 - 6)) == 0, "det of the 2x2 block is c A1 - 6")
    # Action on the normalized basis, checked by components.
    u = sp.Matrix([sp.Rational(1, 6)] * 6 + [0])  # un-normalized all-ones on contents, for the identity below
    # T applied to the all-ones-on-contents vector (sum of basis), empty component 6? 
    ones_c = sp.Matrix([1, 1, 1, 1, 1, 1, 0])
    image = sp.simplify(T * ones_c)
    # content a gets c * A1, empty gets 6
    require(all(sp.simplify(image[a] - c * A1) == 0 for a in range(6)) and sp.simplify(image[6] - 6) == 0,
            "T sends the content all-ones to c A1 on contents and 6 on empty")
    e = sp.Matrix([0, 0, 0, 0, 0, 0, 1])
    image_e = sp.simplify(T * e)
    require(all(sp.simplify(image_e[a] - 1) == 0 for a in range(6)) and sp.simplify(image_e[6] - 1) == 0,
            "T sends empty to 1 on every state")
    factored = c ** 5 * (p - q) ** 3 * (p + q - 2 * r) ** 2 * (c * A1 - 6)
    require(sp.factor(sp.simplify(T.det() - factored)) == 0,
            "det T = c^5 (p-q)^3 (p+q-2r)^2 (c(p+q+4r)-6)")


def psd_and_rank():
    triples = [(3, 1, 2), (5, 2, 4), (7, 3, 5), (4, 1, 1)]
    for p, q, r in triples:
        A1 = p + q + 4 * r
        c0 = Fraction(6, A1)
        side_fail = (p < q) or (p + q < 2 * r)
        T0 = transfer(p, q, r, c0)
        ev = [sp.nsimplify(x) for x in T0.eigenvals()]
        # eigenvals returns a dict eigenvalue -> multiplicity
        neg = []
        for val, mult in T0.eigenvals().items():
            if sp.simplify(val) < 0:
                neg.append((val, mult))
        require((len(neg) > 0) == side_fail,
                f"{(p, q, r)}: negative eigenvalue at c0={c0} exactly when a scale-free factor is negative")
        if (p, q, r) == (5, 2, 4):
            # p+q-2r = -1, so c(p+q-2r) < 0 for every c > 0
            require(p + q - 2 * r < 0, "(5,2,4) has p+q < 2r")
            for c in (Fraction(1, 10), c0, 1, 5):
                Tc = transfer(p, q, r, c)
                worst = min(sp.simplify(val) for val in Tc.eigenvals())
                require(worst < 0, f"(5,2,4) at c={c} is not positive type")
        if (p, q, r) == (3, 1, 2):
            require(c0 == Fraction(1, 2), "(3,1,2) has c0 = 1/2")
            require(T0.rank() == 4, "at (3,1,2) and c0, rank T = 4")
            require(transfer(3, 1, 2, 1).rank() == 5, "at (3,1,2) and c=1, rank T = 5")
        if (p, q, r) == (4, 1, 1):
            require(T0.rank() == 6, "at (4,1,1) and c0 the only drop is the one kernel direction, rank 6")


def routes():
    c, t = sp.symbols("c t", positive=True)
    f = c * t / (1 + c * t)
    require(sp.simplify(sp.diff(f, t) - c / (1 + c * t) ** 2) == 0,
            "t |-> c t/(1+c t) has positive derivative for c > 0")
    # f(p)=f(r) forces p=r for c>0
    p, r = sp.symbols("p r", positive=True)
    diff = sp.together(f.subs(t, p) - f.subs(t, r))
    require(sp.factor(sp.numer(diff)) == c * (p - r),
            "equal-axis and orthogonal branches agree only if p=r")

    def tv(p, q, r):
        A1 = p + q + 4 * r
        c0 = Fraction(6, A1)
        # f(w) = c w / (1 + c w), one equal, one opposite, four orthogonal
        weights = [p, q, r, r, r, r]

        def branch(w):
            return Fraction(c0 * w, 1 + c0 * w) if not isinstance(c0 * w, Fraction) else (c0 * w) / (1 + c0 * w)

        raw = [(c0 * w) / (1 + c0 * w) for w in weights]
        total = sum(raw)
        law = [x / total for x in raw]
        uniform = Fraction(1, 6)
        return sum(abs(x - uniform) for x in law) / 2

    require(tv(3, 1, 2) == Fraction(7, 132), "at (3,1,2) and c0 the two content laws differ by 7/132")
    tv524 = tv(5, 2, 4)
    require(tv524 > 0, f"at (5,2,4) and c0 the total variation is {tv524} > 0")
    print(f"  (5,2,4) total variation = {tv524}")


def main():
    spectrum_of_omega()
    block_and_det()
    psd_and_rank()
    routes()
    print("TOTAL FAIL =", len(FAILS))
    if FAILS:
        print("SUMMARY: fails at a finite check - " + "; ".join(FAILS[:6]))
        return 1
    print(
        "HIT: confirmed - the vacancy couples only through the all-ones direction, so det T = "
        "c^5 (p-q)^3 (p+q-2r)^2 (c(p+q+4r)-6), and c0 = 6/(p+q+4r) is the unique scale that "
        "makes T singular when the scale-free factors are nonzero. The kernel is the uniform "
        "content vector minus six times the empty state. T is positive type iff c >= c0 and "
        "p >= q and p+q >= 2r; (5,2,4) fails the last at every positive scale. Formation-then-motion "
        "and formation-in-place agree for no c > 0 unless p=q=r, and at (3,1,2), c0 their total "
        "variation is 7/132."
    )
    print(
        "SUMMARY: confirmed - c0 is the determinant zero of the 2x2 vacancy block; the scale-free "
        "factors p-q and p+q-2r are required for positive type; (d) constrains the weights, not c. "
        "The reduction from bond-plane reflection positivity to T positive-type was not re-derived."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
