#!/usr/bin/env python3
"""Independent checks for kappa-from-the-rule a2. Fractions, not the author's script."""
import math
from fractions import Fraction as F

FAILS = []


def ok(step, good, msg):
    print(("ok " if good else "FAIL ") + step + ": " + msg, flush=True)
    if not good:
        FAILS.append(step)


def kappa_two(a, b):
    """Arithmetic-mean kappa for two non-adjacent neighbours with pair weights a, b. c is already in a, b."""
    return F(6) / (a + b + 4 * a * b)


def main():
    p, q, r = 3, 1, 2
    c0 = F(6, p + q + 4 * r)
    cp, cq, cr = c0 * p, c0 * q, c0 * r
    mean_w = (cp + cq + 4 * cr) / 6
    ok("1", c0 == F(1, 2) and cp == F(3, 2) and cq == F(1, 2) and cr == 1 and p + q == 2 * r and mean_w == 1,
       f"c0={c0}, weights {cp},{cq},{cr}, mean pair weight {mean_w}")

    one = {
        "equal": F(6) / (1 + 5 * cp),
        "opposite": F(6) / (1 + 5 * cq),
        "orthogonal": F(6) / (1 + 5 * cr),
    }
    ok("2", one["equal"] == F(12, 17) and one["opposite"] == F(12, 7) and one["orthogonal"] == 1,
       f"one neighbour {one['equal']}, {one['opposite']}, {one['orthogonal']}")

    two = {
        "ee": kappa_two(cp, cp),
        "eo": kappa_two(cp, cq),
        "er": kappa_two(cp, cr),
        "oo": kappa_two(cq, cq),
        "or": kappa_two(cq, cr),
        "rr": kappa_two(cr, cr),
    }
    ok("2b", two == {"ee": F(1, 2), "eo": F(6, 5), "er": F(12, 17), "oo": 3, "or": F(12, 7), "rr": 1},
       "two-neighbour table matches 1/2, 6/5, 12/17, 3, 12/7, 1")

    # below one only for equal partners, inside this menu
    below = (one["equal"] < 1) and (one["opposite"] > 1) and (one["orthogonal"] == 1)
    below &= two["ee"] < 1 and two["oo"] > 1 and two["rr"] == 1
    ok("2c", below, "at (3,1,2), kappa<1 only next to equal contents")

    uniform = (one["equal"] + one["opposite"] + 4 * one["orthogonal"]) / 6
    weighted = (cp * one["equal"] + cq * one["opposite"] + 4 * cr * one["orthogonal"]) / 6
    ok("3", uniform == F(382, 357) and weighted == F(352, 357) and uniform > 1 and weighted < 1,
       f"uniform average {uniform}, stationary-pair average {weighted}")

    # geometric-mean log kappa, uniform and stationary
    def logk(cw):
        return (-5 / 6) * math.log(float(cw))
    uni_log = (logk(cp) + logk(cq) + 4 * logk(cr)) / 6
    st_log = (float(cp) * logk(cp) + float(cq) * logk(cq) + 4 * float(cr) * logk(cr)) / 6
    ok("3b", abs(uni_log - 0.040) < 0.001 and abs(st_log + 0.036) < 0.001,
       f"mean log kappa geometric: uniform {uni_log:.3f}, stationary {st_log:.3f}")

    # torus: sum of (1-A)f is zero. 3^3, random integer field.
    L = 3
    field = {(x, y, z): (x * 3 + y * 5 + z * 7) % 11 for x in range(L) for y in range(L) for z in range(L)}
    acc = 0
    for x, y, z in field:
        nbr = 0
        for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            nbr += field[((x + dx) % L, (y + dy) % L, (z + dz) % L)]
        acc += 6 * field[(x, y, z)] - nbr
    ok("4", acc == 0, "sum of (1-A)f over the 3^3 torus is 0, so block 50 sources have no net monopole")

    # equal pulls: -(E_A S_B - E_B S_A) vanishes iff S/E agree
    EA, EB, SA, SB = 2, 5, -4, -10  # SA/EA = SB/EB = -2
    force = -(EA * SB - EB * SA)
    bad = -(EA * 3 - EB * SA)
    ok("5", force == 0 and bad != 0, "pulls cancel for every separation iff S/E is the same number")

    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0] + " - independent arithmetic did not match")
        return
    print(
        "HIT: confirmed - at (3,1,2) an isolated record has kappa 1; one neighbour gives 12/17, 12/7, 1; "
        "the torus sources of w=1/pi sum to 0, so this clock has no far field"
    )
    print(
        "SUMMARY: confirmed the pair weights, both neighbour tables, the two averages 382/357 and 352/357, "
        "and the zero total of the rate-field source; gamma remains a free positive coefficient of blocks 53-55"
    )


if __name__ == "__main__":
    main()
