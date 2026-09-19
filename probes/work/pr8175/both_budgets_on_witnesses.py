#!/usr/bin/env python3
"""J:attack-b:PR8175 — SAME TEST, BOTH SIDES on the two budgets.

Note: sharper E <= 3(|S|-1)+|A| fails; block 30 E <= 3(|S|-1)+2|A| holds.
Identical test: the two inequalities on the same stated witness triples
(W1, W2, W3). HIT if both hold or both fail on a witness (no separation).
"""
from __future__ import annotations

# (E, |A|, |S|) as stated T2
W = {
    "W1": (16, 10, 1),
    "W2": (20, 12, 1),
    "W3": (23, 12, 2),
}


def main():
    hits = []
    for name, (E, A, S) in W.items():
        sharp = 3 * (S - 1) + A
        loose = 3 * (S - 1) + 2 * A
        s_ok = E <= sharp
        l_ok = E <= loose
        print(f"{name}: E={E} |A|={A} |S|={S} sharp_rhs={sharp} hold={s_ok} loose_rhs={loose} hold={l_ok}")
        if s_ok == l_ok:
            hits.append(f"{name} both {s_ok} (no separation)")
        if name == "W1" and (E, A, S) != (16, 10, 1):
            hits.append("W1 numbers")
    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: SAME TEST BOTH SIDES (PR #8175): " + "; ".join(hits))
    else:
        print(
            "SUMMARY: SAME TEST BOTH SIDES on the two budgets (PR #8175): on W1/W2/W3 "
            "the identical E vs rhs test finds the sharper bound false and block 30's "
            "E<=3(|S|-1)+2|A| true; the separation holds as written"
        )


if __name__ == "__main__":
    main()
