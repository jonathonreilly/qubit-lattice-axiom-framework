#!/usr/bin/env python3
"""J:attack-e:PR8157 — pattern (e) SAMPLED EVIDENCE.

P3/P4: kappa(beta)>0 at every coupling (the exponent 'never vanishes').
kappa = 5/(512 beta) for beta>=5/256, 1-128 beta/5 for beta<=5/256.
Not a Monte-Carlo never: adversarial grid of beta in (0, 10] including the
join, looking for kappa<=0. HIT if some positive coupling has a nonpositive
stated exponent.
"""
from __future__ import annotations

from fractions import Fraction as Fr

HITS: list[str] = []
JOIN = Fr(5, 256)


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def kappa(b: Fr) -> Fr:
    if b >= JOIN:
        return Fr(5, 512) / b
    return 1 - Fr(128, 5) * b


def main() -> int:
    grid = (
        [Fr(1, 10**k) for k in range(1, 8)]
        + [JOIN / 4, JOIN / 2, JOIN, JOIN * 2, JOIN * 4]
        + [Fr(1, 100), Fr(1, 10), Fr(1, 2), Fr(1), Fr(2), Fr(5), Fr(10)]
        + [Fr(n, 256) for n in range(1, 40)]
    )
    worst = None
    for b in grid:
        if b <= 0:
            continue
        k = kappa(b)
        print(f"beta={b} kappa={k}")
        if k <= 0:
            hit(f"kappa({b})={k} <= 0")
        if worst is None or k < worst[0]:
            worst = (k, b)
    print(f"adversarial min kappa on grid: {worst}")
    # join continuity
    if kappa(JOIN) != Fr(1, 2):
        hit(f"join kappa {kappa(JOIN)} != 1/2")
    if kappa(JOIN) != Fr(5, 512) / JOIN:
        hit("hi formula fails at join")
    if kappa(JOIN) != 1 - Fr(128, 5) * JOIN:
        hit("lo formula fails at join")

    if HITS:
        print("SUMMARY: attack pattern (e) SAMPLED EVIDENCE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - adversarial beta grid "
        "in (0,10] including the join 5/256 never finds kappa<=0; the "
        "'never-vanishing exponent' is not a sampled never"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
