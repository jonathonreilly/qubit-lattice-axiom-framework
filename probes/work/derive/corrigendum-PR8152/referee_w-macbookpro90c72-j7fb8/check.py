#!/usr/bin/env python3
"""Independent check of the block 18 frame as written."""
from fractions import Fraction as F


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def main():
    q1 = (F(1), F(0), F(0))
    q2 = (F(3, 5), F(4, 5), F(0))
    t = dot(q1, q2)
    s2 = 1 - t * t
    s = F(4, 5)  # sqrt(1-t^2) = 4/5
    ok = t == F(3, 5) and s * s == s2
    e2_num = tuple(q2[i] - t * q1[i] for i in range(3))
    e2 = tuple(x / s for x in e2_num)
    third = cross(q1, q2)
    # W columns
    cols = (q1, e2, third)
    # Gram W^T W
    gram = [[dot(cols[i], cols[j]) for j in range(3)] for i in range(3)]
    ok &= gram == [[1, 0, 0], [0, 1, 0], [0, 0, F(16, 25)]]
    # det = scalar triple q1 · (e2 × third)
    det = dot(q1, cross(e2, third))
    ok &= det == F(4, 5)
    ok &= third == (0, 0, F(4, 5))
    # orthogonal locus: t=0, third has length 1
    q2o = (F(0), F(1), F(0))
    th = cross(q1, q2o)
    ok &= dot(th, th) == 1
    print(f"t={t} det={det} third={third} gram={gram}")
    if ok:
        print(
            "HIT: confirmed - the written frame at q2=(3/5,4/5,0) has det 4/5 and sends e_z to (0,0,4/5), "
            "so it is a rotation only when q1·q2=0"
        )
        print(
            "SUMMARY: confirmed the corrigendum: line 91's third column is short by sqrt(1-t^2); "
            "the corrected column is the unit cross product"
        )
    else:
        print("SUMMARY: fails at the executed pair")


if __name__ == "__main__":
    main()
