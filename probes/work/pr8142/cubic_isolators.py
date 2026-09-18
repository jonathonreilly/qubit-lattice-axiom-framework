#!/usr/bin/env python3
"""J:attack:PR8142 — pattern (c) EXECUTED NUMBERS: t*, rho, sextic isolating intervals.

Note: t* in (4,5) for t^3-3t^2-6t-1; rho in (6,7) for x^3-3x^2-15x-19;
sextic roots in (1,2) and (6,7). HIT if integer sign changes fail.
"""


def main() -> None:
    def ct(t):
        return t**3 - 3 * t**2 - 6 * t - 1

    def cr(x):
        return x**3 - 3 * x**2 - 15 * x - 19

    def s(x):
        return x**6 - 6 * x**5 - 3 * x**4 + 4 * x**3 - 3 * x**2 - 6 * x + 31

    print(f"cubic_t(4)={ct(4)} cubic_t(5)={ct(5)}")
    print(f"cubic_rho(6)={cr(6)} cubic_rho(7)={cr(7)}")
    print(f"sextic(1)={s(1)} sextic(2)={s(2)} sextic(6)={s(6)} sextic(7)={s(7)}")
    hits = []
    if not (ct(4) < 0 < ct(5)):
        hits.append("t* not isolated in (4,5)")
    if not (cr(6) < 0 < cr(7)):
        hits.append("rho not isolated in (6,7)")
    if not (s(1) > 0 and s(2) < 0 and s(6) < 0 and s(7) > 0):
        hits.append("sextic sign pattern failed")
    if hits:
        print("HIT: " + "; ".join(hits))
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS - " + "; ".join(hits))
    else:
        print(
            "SUMMARY: attack pattern (c) EXECUTED NUMBERS - t* in (4,5), rho in (6,7), "
            "sextic in (1,2) and (6,7); does not fire"
        )


if __name__ == "__main__":
    main()
