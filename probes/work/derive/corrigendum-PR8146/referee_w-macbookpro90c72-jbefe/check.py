#!/usr/bin/env python3
"""Referee for corrigendum-PR8146 a1. Own weight algebra and an own census.

Author w-jonathonsmac4f50-jdc8c (claude-opus-5). Does not call their script.
"""
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def weights():
    p, q, r = sp.symbols("p q r", positive=True)
    # orthogonal 2:1 (a, a, b), b perpendicular to a
    Wa, Wna, Wb, Wnb, Wc = p**2 * r, q**2 * r, p * r**2, q * r**2, r**3
    ok = all(
        sp.simplify(got - exp) == 0
        for got, exp in (
            (Wa - Wna, r * (p - q) * (p + q)),
            (Wa - Wb, p * r * (p - r)),
            (Wa - Wc, r * (p - r) * (p + r)),
            (Wa - Wnb, r * (p**2 - q * r)),
        )
    )
    # antipodal 2:1 (a, a, -a)
    Aa, Ana, Ac = p**2 * q, p * q**2, r**3
    ok = ok and sp.simplify((Aa - Ana) - p * q * (p - q)) == 0
    ok = ok and sp.simplify((Aa - Ac) - (p**2 * q - r**3)) == 0
    # sqrt(r^3/q) / r = sqrt(r/q), so the antipodal threshold exceeds r exactly when q < r
    gap = sp.simplify(sp.sqrt(r**3 / q) / r)
    ok_gap = sp.simplify(gap**2 - r / q) == 0
    report(
        "weights",
        bool(ok and ok_gap),
        "orthogonal argmax iff p>max(q,r); antipodal argmax iff p>q and p^2 q>r^3; "
        "sqrt(r^3/q) exceeds r exactly when q<r",
    )


def witness():
    p, q, r = 5, 2, 4
    Za = p**2 * q + p * q**2 + 4 * r**3  # 50+20+256 = 326
    pa, pc = p**2 * q, r**3
    ok = Za == 326 and pa == 50 and pc == 64 and pa * 2 == 100 and pc * 2 == 128
    # 50/326 = 25/163, 64/326 = 32/163
    ok = ok and pa // 2 == 25 and Za // 2 == 163 and pc // 2 == 32 and 25 < 32
    # orthogonal pattern at the same point: majority still wins
    Wa, Wb, Wc, Wna = p**2 * r, p * r**2, r**3, q**2 * r
    ok = ok and Wa > Wb > Wc > q * r**2 > Wna
    # band membership
    ok = ok and q < r < p and p * p * q <= r**3
    report(
        "witness (5,2,4)",
        ok,
        "antipodal P(a)=25/163 < 32/163=P(c); orthogonal weights 100>80>64 so a still wins there",
    )


def census():
    n = 0
    band_lines = {(1, 2): 0, (2, 4): 0, (1, 3): 0, (1, 1): 0}
    for q in range(1, 25):
        for r in range(1, 25):
            for p in range(1, 25):
                inside = q < r and p > r and p * p * q <= r ** 3
                n += inside
                if (q, r) in band_lines and inside:
                    band_lines[(q, r)] += 1
    # continuous bands
    # (p,1,2) band (2, 2*sqrt(2)], (p,2,4) (4, 4*sqrt(2)], (p,1,3) (3, 3*sqrt(3)]
    ok_lines = all(
        sp.simplify(sp.sqrt(sp.Integer(num) / sp.Integer(den)) - target) == 0
        for num, den, target in (
            (8, 1, 2 * sp.sqrt(2)),
            (64, 2, 4 * sp.sqrt(2)),
            (27, 1, 3 * sp.sqrt(3)),
        )
    )
    # B4 points: original and corrected predicates agree, and none sit in the band
    def pred(p, q, r):
        original = p > max(q, r)
        # corrected iff p>q and p^2 q > r^3, which already forces p>r
        corrected = (p > q) and (p * p * q > r ** 3)
        return original, corrected

    points = [(3, 1, 2), (2, 1, 3), (1, 2, 1), (2, 2, 1), (5, 2, 4)]
    agree = []
    for pt in points:
        o, c = pred(*pt)
        agree.append((pt, o, c, o == c))
    b4_same = all(o == c for _, o, c, _ in agree[:4])
    witness_differs = agree[4][1] and not agree[4][2]
    # executed couplings on (p,1,2) sit past 2*sqrt(2)
    executed = all(p * p > 8 for p in (3, 10, 30, 100, 1000))
    report(
        "census",
        n == 979 and 24**3 == 13824 and b4_same and witness_differs and executed and bool(ok_lines),
        f"{n} of {24**3} integer triples in the band; B4's four points agree under both predicates; "
        f"(5,2,4) is accepted by p>max(q,r) and rejected by the corrected test; "
        f"line hits {band_lines}",
    )


def main():
    weights()
    witness()
    census()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the majority of every 2:1 triple is the strict mode iff "
        "p > max(q, sqrt(r^3/q)); the orthogonal pattern only needs p>max(q,r), and the antipodal "
        "pattern needs p^2 q > r^3. At (5,2,4), 25/163 < 32/163. The band holds 979 of 13824 "
        "triples in {1..24}^3."
    )
    print(
        "SUMMARY: confirmed the weight differences, the witness, the four campaign lines, and the integer census. "
        "The note-by-note line inventory was not re-fetched."
    )


if __name__ == "__main__":
    main()
