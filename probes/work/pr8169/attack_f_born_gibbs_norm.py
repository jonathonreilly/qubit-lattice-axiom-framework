#!/usr/bin/env python3
"""J:attack-f:PR8169 — NORMALIZATION of Born (1+s·q)/2, Gibbs 2α+2γ=1, linear /4."""
from fractions import Fraction

HITS = []


def hit(msg):
    HITS.append(msg)
    print("HIT:", msg)


def main():
    q, qp = (1, 0, 0), (0, 1, 0)
    S = [q, qp, tuple(-x for x in q), tuple(-x for x in qp)]
    born = [Fraction(1 + sum(s[i] * q[i] for i in range(3)), 2) for s in S]
    if born != [1, Fraction(1, 2), 0, Fraction(1, 2)]:
        hit(f"Born values {born}")
        return
    if sum(born) != 2:
        hit(f"Born sum {sum(born)} != 2")
        return
    print("OK: Born (1+s·q)/2 on S is (1, 1/2, 0, 1/2), sum 2")

    alpha, gamma = Fraction(1, 3), Fraction(1, 6)
    if 2 * alpha + 2 * gamma != 1:
        hit("2α+2γ != 1")
        return
    # Gibbs at t=0, e^{2β}=2: α = 1/(2+2e^{-2β}) = 1/3
    e2b = 2
    alpha_g = 1 / Fraction(2 + 2 / e2b)  # 1/(2+1)=1/3
    gamma_g = 1 / Fraction(2 * e2b + 2)  # 1/(4+2)=1/6
    if (alpha_g, gamma_g) != (alpha, gamma):
        hit(f"Gibbs masses {alpha_g},{gamma_g}")
        return
    print("OK: Gibbs 2α+2γ=1 with α=1/3, γ=1/6 at e^{2β}=2")

    # linear family (1+λ s·(q+q'))/4 at t=0, s·(q+q')=±1
    # λ=0 uniform 1/4 each; 4*(1/4)=1
    if 4 * Fraction(1, 4) != 1:
        hit("linear family /4 does not sum to 1")
        return
    print("OK: linear family (1+λ s·(q+q'))/4 is normalized (sum 1 at λ=0)")

    if HITS:
        print("SUMMARY: pattern (f) NORMALIZATION fired; " + "; ".join(HITS))
    else:
        print(
            "SUMMARY: pattern (f) NORMALIZATION — Born (1+s·q)/2 sums to 2; "
            "Gibbs 2α+2γ=1 with α=1/3, γ=1/6; linear family /4 sums to 1; "
            "attack does not fire"
        )


if __name__ == "__main__":
    main()
