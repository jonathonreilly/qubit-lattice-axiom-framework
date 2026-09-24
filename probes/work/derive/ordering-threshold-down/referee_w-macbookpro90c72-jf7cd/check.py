#!/usr/bin/env python3
"""Independent referee for ordering-threshold-down a2.

The three deviations and their differences, factored in sympy. The author's script is not called.
"""
import sympy as sp

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


def main():
    p, q, r = sp.symbols("p q r", positive=True)
    d1 = (q ** 3 + 4 * r ** 3) / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = (p * q ** 2 + 4 * r ** 3) / (p ** 2 * q + p * q ** 2 + 4 * r ** 3)
    d3 = (q ** 2 * r + p * r ** 2 + q * r ** 2 + 2 * r ** 3) / (
        p ** 2 * r + q ** 2 * r + p * r ** 2 + q * r ** 2 + 2 * r ** 3
    )
    check("at p=q=r every deviation is 5/6",
          all(sp.simplify(d.subs({q: p, r: p}) - sp.Rational(5, 6)) == 0 for d in (d1, d2, d3)))

    n21 = sp.factor(sp.numer(sp.together(d2 - d1)))
    claimed21 = p ** 2 * (p - q) * (p * q ** 2 + q ** 3 + 4 * r ** 3)
    check("numerator of d2-d1 is p^2 (p-q)(p q^2 + q^3 + 4 r^3)",
          sp.expand(n21 - claimed21) == 0, str(n21))
    # denominators of d1 and d2 are positive, so the difference has the sign of p-q
    den1 = p ** 3 + q ** 3 + 4 * r ** 3
    den2 = p ** 2 * q + p * q ** 2 + 4 * r ** 3
    cof = p ** 2 * (p * q ** 2 + q ** 3 + 4 * r ** 3)
    check("d2-d1 = (p-q) times a ratio of positive polynomials, so it has the sign of p-q",
          sp.expand(sp.together((d2 - d1) * den1 * den2 - (p - q) * cof)) == 0
          and all(c > 0 for c in sp.Poly(sp.expand(cof), p, q, r).coeffs())
          and all(c > 0 for c in sp.Poly(den1, p, q, r).coeffs())
          and all(c > 0 for c in sp.Poly(den2, p, q, r).coeffs()))

    n32 = sp.factor(sp.numer(sp.together(d3 - d2)))
    claimed32 = -p ** 2 * (q - r) * (p * q - q ** 2 - 2 * q * r - 4 * r ** 2)
    check("numerator of d3-d2 is -p^2 (q-r)(p q - q^2 - 2 q r - 4 r^2)",
          sp.expand(n32 - claimed32) == 0, str(n32))

    def at(trip):
        s = {p: trip[0], q: trip[1], r: trip[2]}
        return [sp.simplify(d.subs(s)) for d in (d1, d2, d3)]

    witnesses = {
        (3, 1, 2): 1,  # d2
        (3, 2, 1): 2,  # d3
        (1, 3, 2): 0,  # d1
    }
    ok_w = True
    bits = []
    for trip, who in witnesses.items():
        v = at(trip)
        mx = max(range(3), key=lambda i: v[i])
        strict = v[mx] > v[(mx + 1) % 3] and v[mx] > v[(mx + 2) % 3]
        ok_w &= mx == who and strict
        bits.append(f"{trip}->d{mx+1} {[float(x) for x in v]}")
    check("strict maxima: d2 at (3,1,2), d3 at (3,2,1), d1 at (1,3,2)", ok_w, "; ".join(bits))

    for trip in ((10, 1, 1), (4, 1, 1), (7, 1, 1)):
        v = at(trip)
        # (7,1,1) is on the surface p q = q^2 + 2 q r + 4 r^2
        check(f"d2 = d3 at {trip}", sp.simplify(v[1] - v[2]) == 0, str(v[1]))

    check("the cofactor of (p-q) has only positive coefficients, so p>q puts d1 strictly below d2",
          all(c > 0 for c in sp.Poly(sp.expand(p ** 2 * (p * q ** 2 + q ** 3 + 4 * r ** 3)), p, q, r).coeffs()))

    print()
    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0])
        raise SystemExit(1)
    print("SUMMARY: confirmed - d2-d1 has numerator p^2(p-q)(pq^2+q^3+4r^3) and d3-d2 has numerator -p^2(q-r)(pq-q^2-2qr-4r^2); each deviation is the strict maximum at an explicit triple.")
    print("HIT: confirmed - d2 > d1 exactly when p > q, d2 = d3 exactly on q = r or pq = q^2+2qr+4r^2, and the three deviations are the strict maximum at (3,1,2), (3,2,1) and (1,3,2).")


if __name__ == "__main__":
    main()
