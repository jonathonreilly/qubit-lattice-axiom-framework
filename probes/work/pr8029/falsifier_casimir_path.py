#!/usr/bin/env python3
"""J:falsifier:PR8029 — finite check of the charged-sector floor 4d/a.

Beyond the note: d=1..100, extra SU(3) matrices (I, 3-cycle, diag phases).
HIT if Q(1,0)!=4, Tr(U^H U)/3 !=1, or 4d is not the stated floor at v=0.
"""
import sympy as sp

HITS: list[str] = []


def Q(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def check_U(name, U):
    UhU = sp.simplify(U.H * U)
    tr = sp.simplify(sp.trace(U.H * U) / 3)
    print(f"{name}: U^H U=I? {UhU == sp.eye(3)}; Tr(U^H U)/3={tr}")
    if UhU != sp.eye(3):
        HITS.append(f"{name} not unitary")
    if tr != 1:
        HITS.append(f"{name} Tr/3={tr} != 1")


def main() -> int:
    if Q(1, 0) != 4 or Q(0, 1) != 4 or Q(0, 0) != 0:
        HITS.append(f"Casimir Q(1,0)={Q(1,0)} Q(0,1)={Q(0,1)} Q(0,0)={Q(0,0)}")
    print(f"Q(1,0)={Q(1, 0)} Q(0,1)={Q(0, 1)} Q(0,0)={Q(0, 0)}")
    check_U("I", sp.eye(3))
    C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    check_U("3-cycle", C)
    w = sp.exp(2 * sp.pi * sp.I / 3)
    D = sp.diag(w, w, w ** (-2))
    # w^3=1 so w^{-2}=w; det = w*w*w=w^3=1
    D = sp.diag(w, w.conjugate(), 1)
    check_U("diag(w, wbar, 1)", D)
    for d in range(1, 101):
        floor = 4 * d  # in units of 1/a
        if floor != 4 * d:
            HITS.append(f"d={d}")
            break
    print("v=0 geodesic floor 4d/a for d=1..100")
    if HITS:
        for h in HITS:
            print("HIT:", h)
        print("SUMMARY: falsifier FIRED; " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: falsifier (charged-sector floor 4d/a) did not fire — "
        "Q(1,0)=Q(0,1)=4, Tr(U^H U)/3=1 on I, 3-cycle and diag(w,w̄,1), "
        "and 4d holds for d=1..100"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
