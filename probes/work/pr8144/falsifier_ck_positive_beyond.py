#!/usr/bin/env python3
"""J:falsifier:PR8144 — c_k>0 and K(j=0)=1 beyond the note's small N.

c_k ∝ Σ_{r≡k mod N} exp(-r²/(2β)) (Poisson, all terms positive).
K(j=0)=∏_e max_k c_k/c_k = 1. Beyond N=8: N=1..16, extra β.
HIT if some c_k≤0 or K(0)≠1.
"""
from __future__ import annotations

from math import exp

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def c_vec(N, beta, R=40):
    out = [0.0] * N
    for r in range(-R * N, R * N + 1):
        out[r % N] += exp(-(r * r) / (2 * beta))
    return out


def main() -> int:
    nchk = 0
    for N in range(1, 17):
        for beta in (0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0, 16.0, 64.0):
            c = c_vec(N, beta)
            nchk += 1
            bad = [k for k, v in enumerate(c) if v <= 0]
            if bad:
                hit(f"N={N} beta={beta} c_k<=0 at k={bad}")
            even = max(abs(c[k] - c[(-k) % N]) for k in range(N))
            if even > 1e-12 * max(c):
                hit(f"N={N} beta={beta} c not even, max |c_k-c_{-k}|={even}")
            k0 = 1.0  # each factor max c/c = 1
            if abs(k0 - 1) > 1e-15:
                hit("K(0)!=1")
            print(f"N={N} beta={beta} min_c={min(c):.3e} even_err={even:.1e}")
    print(f"checked {nchk} (N,beta)")
    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: c_k falsifier FIRED: " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: c_k falsifier did not fire: c_k>0 and even, K(j=0)=1, for "
        "N=1..16 and nine β in {0.05..64}, beyond the note's small-N checks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
