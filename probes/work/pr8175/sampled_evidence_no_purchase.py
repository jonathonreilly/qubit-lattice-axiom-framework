#!/usr/bin/env python3
"""J:attack-e:PR8175 — pattern (e) SAMPLED EVIDENCE.

The note is itself the adversarial construction: explicit witnesses W1/W2/W3
refute the sharper budget E <= 3(|S|-1)+|A|. There is no 'never/always
observed' resting on random sampling. Confirm the stated ratios still beat
the sharper budget (not more samples). Not the grok provenance HIT.
"""
from __future__ import annotations

W = {
    "W1": (16, 10, 1),
    "W2": (20, 12, 1),
    "W3": (23, 12, 2),
}

HITS: list[str] = []


def main() -> int:
    for name, (E, A, S) in W.items():
        sharp = 3 * (S - 1) + A
        loose = 3 * (S - 1) + 2 * A
        print(f"{name}: E={E} sharp={sharp} E>sharp {E > sharp} loose={loose} E<=loose {E <= loose}")
        if E <= sharp:
            HITS.append(f"{name} does not refute the sharper budget")
        if E > loose:
            HITS.append(f"{name} also exceeds block 30's budget")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (e) SAMPLED EVIDENCE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the sharper-budget "
        "refutation is already an explicit adversarial construction (W1/W2/W3 "
        "ratios 8/5, 5/3, 23/12), not a sampled never; extra sampling is not "
        "the load-bearing claim"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
