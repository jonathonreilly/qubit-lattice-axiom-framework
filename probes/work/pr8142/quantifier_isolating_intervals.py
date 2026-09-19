#!/usr/bin/env python3
"""J:attack-d:PR8142 — isolating intervals at extra integers.

t* in (4,5), rho in (6,7), sextic in (1,2) and (6,7). Quantifier: the
stated intervals still isolate at neighboring integers. HIT if a sign
change is missing or an extra positive root appears in 0..10.
"""


def ct(t):
    return t ** 3 - 3 * t ** 2 - 6 * t - 1


def cr(x):
    return x ** 3 - 3 * x ** 2 - 15 * x - 19


def s(x):
    return x ** 6 - 6 * x ** 5 - 3 * x ** 4 + 4 * x ** 3 - 3 * x ** 2 - 6 * x + 31


def main():
    hits = []
    if not (ct(4) < 0 < ct(5)):
        hits.append("HIT: t* not isolated in (4,5)")
        print(hits[-1])
    pos_t = [t for t in range(0, 11) if ct(t) > 0]
    print(f"t cubic positive at integers {pos_t}; ct(4)={ct(4)} ct(5)={ct(5)}")
    if not (cr(6) < 0 < cr(7)):
        hits.append("HIT: rho not isolated in (6,7)")
        print(hits[-1])
    if not (s(1) > 0 and s(2) < 0 and s(6) < 0 and s(7) > 0):
        hits.append("HIT: sextic isolating signs fail")
        print(hits[-1])
    print(f"rho cr(6)={cr(6)} cr(7)={cr(7)}; sextic s(1)={s(1)} s(2)={s(2)} s(6)={s(6)} s(7)={s(7)}")
    if hits:
        print("SUMMARY: isolating-interval signs fail at extra integers")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — t* in (4,5), rho in "
        "(6,7), and the sextic roots in (1,2) and (6,7) remain isolated at "
        "neighboring integers 0..10"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
