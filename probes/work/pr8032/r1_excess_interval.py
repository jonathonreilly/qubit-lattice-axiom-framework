#!/usr/bin/env python3
"""J:attack:PR8032 — pattern (c) EXECUTED NUMBERS: R1 trial excess in (4, 4.01).

Note: t=1/100, N=1+2t^2, Qn=1+4t^2/9, v=96t/(1+t-2t^2),
E0=v-v t/3, Etrial=[4+(20/3)t^2+v(Qn-(4t+t^2)/27)]/Qn.
HIT if the exact excess is not strictly between 4 and 4.01, or if 36/1944 != 1/54.
"""
from fractions import Fraction as F


def main() -> None:
    t = F(1, 100)
    N = 1 + 2 * t * t
    Qn = 1 + F(4, 9) * t * t
    v = 96 * t / (1 + t - 2 * t * t)
    E0 = v - v * t / 3
    Etrial = (4 + F(20, 3) * t * t + v * (Qn - (4 * t + t * t) / 27)) / Qn
    excess = Etrial - E0
    print(f"t={t} N={N} Qn={Qn} v={v}")
    print(f"E0={E0} Etrial={Etrial} excess={excess} ~ {float(excess)}")
    print(f"36/1944={F(36,1944)} 1/54={F(1,54)}")
    hits = []
    if not (F(4) < excess < F(401, 100)):
        hits.append(f"excess {excess} not in (4, 4.01)")
    if F(36, 1944) != F(1, 54):
        hits.append("36/1944 != 1/54")
    e_R = 1 * 1 - (1 * 1) // 4 + 3 * 1  # R=1, a=1
    print(f"e_R(R=1,a=1) numerator {e_R}")
    if e_R != 4:
        hits.append(f"e_R={e_R}")
    if hits:
        print("HIT: " + "; ".join(hits))
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS - " + "; ".join(hits))
    else:
        print(
            "SUMMARY: attack pattern (c) EXECUTED NUMBERS - R1 excess "
            f"{float(excess):.8f} is in (4, 4.01); 36/1944=1/54; e_R=4; does not fire"
        )


if __name__ == "__main__":
    main()
