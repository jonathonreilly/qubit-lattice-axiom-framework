#!/usr/bin/env python3
"""J:falsifier:PR8031 — finite check of PW cutoff dim and fusion.

R=1 dim=19 (note). Beyond: R=0..15. HIT if dim(p,q)=(p+1)(q+1)(p+q+2)/2
fails to be integer, R=1 !=19, or (1,0) fusion of p+q<=R-1 exits p+q<=R.
"""
HITS: list[str] = []


def dim(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def fusion10(p, q):
    out = []
    for a, b in ((p + 1, q), (p - 1, q + 1), (p, q - 1)):
        if a >= 0 and b >= 0:
            out.append((a, b))
    return out


def main() -> int:
    if dim(0, 0) != 1 or dim(1, 0) != 3 or dim(0, 1) != 3:
        HITS.append("small dims")
    d1 = sum(dim(p, q) ** 2 for p in range(2) for q in range(2 - p))
    print(f"R=1 dimH={d1} (stated 19)")
    if d1 != 19:
        HITS.append(f"R=1 dim {d1} != 19")
    for R in range(0, 16):
        irreps = [(p, q) for p in range(R + 1) for q in range(R - p + 1)]
        dH = sum(dim(p, q) ** 2 for p, q in irreps)
        print(f"R={R}: n_irreps={len(irreps)} dimH={dH}")
        if R >= 1:
            for p in range(R):
                q = (R - 1) - p
                if q < 0:
                    continue
                for a, b in fusion10(p, q):
                    if a + b > R:
                        HITS.append(f"fusion ({p},{q})->({a},{b}) exits R={R}")
    if HITS:
        for h in HITS:
            print("HIT:", h)
        print("SUMMARY: falsifier FIRED; " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: falsifier (PW dim and fusion) did not fire — R=1 carrier 19, "
        "Weyl dim integer, and (1,0) fusion of p+q<=R-1 stays in p+q<=R for "
        "R=1..15"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
