#!/usr/bin/env python3
"""Large build summary: interacting matter dynamics generates b!=0 (wall moved) but r=1/2 stays
pinned to the matter-action coupling ratio; the eps-channel escape is generation-blind."""
import numpy as np, itertools


def main():
    # eps-channel generation-blindness (the build's proposed escape)
    corners = list(itertools.product([0, 1], repeat=3))
    hw1 = [c for c in corners if sum(c) == 1]
    print("eps(n)=(-1)^sum on hw=1 generation corners:", [(-1) ** sum(c) for c in hw1],
          "-> constant -> generation-BLIND (cannot split the C3 orbit).")
    print("eps as (pi,pi,pi) shift maps hw=1 ->", [sum(1 - x for x in c) for c in hw1], "(hw=2, out of triplet).")
    # the three builds' r at natural coupling vs off-self-dual
    print("\nr at natural (C3-symmetric/self-dual) coupling: all 3 builds -> r=0 (Q=1/3).")
    print("off-self-dual: SD/Fierz r=2/5 (Q=3/5, regulator artifact); two-channel onset r~0.535 (Q~0.69).")
    Q = lambda r: 1 / 3 + 2 / 3 * r
    for r in [0.0, 2 / 5, 0.535, 0.5]:
        print(f"   r={r:.3f} -> Q={Q(r):.4f}")
    print("\nGENUINE: interacting dynamics generates b!=0 (free b=0 was an exact selection rule;")
    print("Fierz exchange feeds b). r=1/2 dynamically ACCESSIBLE (onset ~0.535). BUT not forced:")
    print("value = continuous output of unsupplied coupling ratio; natural coupling -> r=0; no")
    print("dynamical symmetry pins exactly 1/2 (only algebraic Tr(I^2)/Tr((J-I)^2)=3/6=HS-equipartition).")
    print("A C3-SYMMETRIC interaction only makes the circulant b ([M,Gamma_chi]=0), never the orbit-")
    print("splitting anticommuting operator. eps-channel generation-blind. => converges on the one")
    print("generation-specific chiral import; framework reduces charged-lepton flavor to it + Planck.")


if __name__ == "__main__":
    main()
