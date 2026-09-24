#!/usr/bin/env python3
"""Independent counterexample: a pass-through pushes the other content backward."""
from fractions import Fraction as F

PX, NX, PY, NY, PZ, NZ, EMPTY = range(7)
OPP = {PX: NX, NX: PX, PY: NY, NY: PY, PZ: NZ, NZ: PZ}
AXIS = {PX: 1, NX: -1, PY: 0, NY: 0, PZ: 0, NZ: 0}


def exchange(left, right):
    return right, left


def main():
    # A: +x at 000, +y at 100. The +x attempt exchanges.
    a_left, a_right = PX, PY
    a2 = exchange(a_left, a_right)
    # +y has moved from the right site to the left: a step of -e_x
    ok = a2 == (PY, PX)
    # B: +z at 000, +y at 100. No +x attempt. The +y record's own attempt is along +y, not -x.
    b_left, b_right = PZ, PY
    # the only x-directed attempt here would be a -x content, which neither site has
    moves_py_along_x = False
    for who, content, other in ((0, b_left, b_right), (1, b_right, b_left)):
        if AXIS[content] == 0:
            continue
        # an x-axis content attempts along x
        if content in (PX, NX):
            moves_py_along_x = True
    ok &= not moves_py_along_x
    print("A after +x pass", a2, "B has no x-push of +y", not moves_py_along_x)

    # product currents across an x-bond, densities rho[content], empty = 1-sum
    # enumerate
    def currents(rho):
        empty = 1 - sum(rho.values())
        p = dict(rho)
        p[EMPTY] = empty
        J = {c: F(0) for c in range(6)}
        for L in range(7):
            for R in range(7):
                w = p[L] * p[R]
                # +x at left attempts toward right
                if L == PX and R != PX:
                    J[PX] += w * 1
                    if R != EMPTY:
                        J[R] -= w * 1
                # -x at right attempts toward left (its direction is -e_x)
                if R == NX and L != NX:
                    J[NX] -= w * 1  # -x content moves to the left, so its +x-current is -1
                    if L != EMPTY:
                        J[L] += w * 1  # the passed content is pushed to the right
        return J

    rho = {PX: F(1, 5), NX: F(1, 7), PY: F(1, 11), NY: F(0), PZ: F(0), NZ: F(0)}
    J = currents(rho)
    rp, rm = rho[PX], rho[NX]
    pred_px = rp * (1 - rp + rm)
    pred_nx = -rm * (1 - rm + rp)
    pred_py = -rho[PY] * (rp - rm)  # -r_d g_x with g_x = rp - rm? 
    # author's -r_d g_x. g_x might be the net x-momentum density rp - rm.
    print("J+x", J[PX], "pred", pred_px)
    print("J-x", J[NX], "pred", pred_nx)
    print("J+y", J[PY], "pred", pred_py)
    ok &= J[PX] == pred_px and J[NX] == pred_nx and J[PY] == pred_py
    if ok:
        print(
            "HIT: confirmed - a +x record passing a +y record moves +y one step backward, "
            "and the product currents are r+(1-r++r-), -r-(1-r-+r+), and -r_d(r+-r-)"
        )
        print(
            "SUMMARY: confirmed (a) is false as six independent streams; the streams are coupled by the exchange"
        )
    else:
        print("SUMMARY: fails at the counterexample or the current formula")


if __name__ == "__main__":
    main()
