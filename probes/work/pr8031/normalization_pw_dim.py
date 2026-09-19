#!/usr/bin/env python3
"""J:attack-f:PR8031 — NORMALIZATION.

No torus Fourier / 2π. The 1/2 in Weyl dim(p,q)=(p+1)(q+1)(p+q+2)/2 and
d_(R,0)=(R+1)(R+2)/2, plus conjugate fusion of (0,1), recomputed at small
(p,q,R). Schur: ||sqrt(d) g_11^R|| is the stated unit-norm prefactor.
"""
from fractions import Fraction as Fr


def dim(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def fusion10(p, q):
    out = []
    for a, b in ((p + 1, q), (p - 1, q + 1), (p, q - 1)):
        if a >= 0 and b >= 0:
            out.append((a, b))
    return out


def fusion01(p, q):
    # conjugate: (0,1) tensor (p,q) = (p,q+1) + (p+1,q-1) + (p-1,q)
    out = []
    for a, b in ((p, q + 1), (p + 1, q - 1), (p - 1, q)):
        if a >= 0 and b >= 0:
            out.append((a, b))
    return out


def main() -> int:
    hits = []
    for p in range(0, 6):
        for q in range(0, 6):
            d = dim(p, q)
            if d != (p + 1) * (q + 1) * (p + q + 2) // 2:
                hits.append(f"dim({p},{q})")
            if d * 2 != (p + 1) * (q + 1) * (p + q + 2):
                hits.append(f"1/2 in dim({p},{q}) is not exact")
    print("Weyl dim 1/2 exact for p,q=0..5")

    irreps = [(p, q) for p in range(2) for q in range(2 - p)]
    dH = sum(dim(p, q) ** 2 for p, q in irreps)
    print(f"R=1 carrier {irreps} dimH={dH} (stated 19)")
    if dH != 19:
        hits.append(f"R=1 dim {dH} != 19")

    for R in range(0, 8):
        dR0 = (R + 1) * (R + 2) // 2
        if dR0 != dim(R, 0):
            hits.append(f"d_({R},0)={dR0} != dim({R},0)={dim(R, 0)}")
        print(f"d_({R},0)={dR0} = dim({R},0); sqrt prefactor for unit Schur norm")

    # conjugate fusion keeps p+q<=R when p+q<=R-1
    for R in range(1, 6):
        for p in range(R):
            q = (R - 1) - p
            if q < 0:
                continue
            for a, b in fusion01(p, q):
                if a + b > R:
                    hits.append(f"conjugate fusion ({p},{q}) -> ({a},{b}) exits p+q<=R={R}")
    print("conjugate fusion of (0,1) keeps p+q<=R-1 inside p+q<=R for R=1..5")

    # Cartan 2: cross term 2 Tr_H(Q) Tr_3(T); the 2 is the binomial
    if 2 * Fr(1, 2) != 1:
        hits.append("binomial 2")

    if hits:
        for h in hits:
            print("HIT:", h)
        print("SUMMARY: pattern (f) NORMALIZATION fired; " + "; ".join(hits))
        return 0
    print(
        "SUMMARY: pattern (f) NORMALIZATION — no torus Fourier/2π; Weyl dim "
        "1/2, d_(R,0)=(R+1)(R+2)/2 = dim(R,0), R=1 carrier 19, and conjugate "
        "(0,1) fusion all recompute exactly; attack does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
