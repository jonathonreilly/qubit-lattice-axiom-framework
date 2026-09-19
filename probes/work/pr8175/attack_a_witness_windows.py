#!/usr/bin/env python3
"""J:attack-a:PR8175 — witness realizability.

Declared setting: two-level noisy majority on Z^3 in level time, predecessors
x−e_j (one-sided), window exterior 0. Witnesses W1/W2/W3 as listed in the note
(W1 marks inlined; W2/W3 the runner lists cited by the note).
"""
from __future__ import annotations

from fractions import Fraction

HITS: list[str] = []
E_J = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

# Note T2: W1 window [0,4)^2×[0,7), root (3,3,4), eleven marks.
W1_ROOT, W1_WIN, W1_MARKS = (3, 3, 4), (4, 4, 7), [
    (0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 0, 2), (1, 2, 0),
    (1, 3, 1), (2, 0, 0), (2, 2, 3), (2, 3, 4), (3, 0, 2),
]
# Note: W2 same window, root (3,3,6), forty marks listed in the runner.
W2_ROOT, W2_WIN, W2_MARKS = (3, 3, 6), (4, 4, 7), [
    (0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 5), (0, 1, 0), (0, 1, 2),
    (0, 1, 3), (0, 2, 1), (0, 2, 2), (0, 2, 3), (0, 2, 5), (0, 2, 6),
    (0, 3, 1), (0, 3, 2), (0, 3, 5), (0, 3, 6), (1, 0, 0), (1, 0, 1),
    (1, 0, 2), (1, 1, 1), (1, 1, 3), (1, 2, 2), (1, 2, 3), (1, 3, 2),
    (2, 0, 3), (2, 1, 3), (2, 1, 4), (2, 2, 1), (2, 2, 2), (2, 2, 3),
    (2, 2, 4), (2, 2, 5), (2, 3, 1), (2, 3, 5), (2, 3, 6), (3, 0, 0),
    (3, 2, 2), (3, 3, 1), (3, 3, 2), (3, 3, 5),
]
# Note: W3 window [0,5)^2×[0,9), root (4,4,5), seventy-four marks in the runner.
W3_ROOT, W3_WIN, W3_MARKS = (4, 4, 5), (5, 5, 9), [
    (0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 4), (0, 1, 0), (0, 1, 5),
    (0, 2, 3), (0, 2, 8), (0, 3, 1), (0, 3, 3), (0, 3, 4), (0, 4, 3),
    (0, 4, 4), (0, 4, 5), (0, 4, 6), (0, 4, 7), (1, 0, 0), (1, 0, 1),
    (1, 0, 4), (1, 1, 0), (1, 1, 1), (1, 1, 5), (1, 1, 7), (1, 2, 8),
    (1, 3, 8), (2, 0, 0), (2, 1, 1), (2, 1, 5), (2, 1, 6), (2, 1, 8),
    (2, 2, 0), (2, 2, 1), (2, 2, 6), (2, 2, 7), (2, 2, 8), (2, 3, 1),
    (2, 3, 2), (2, 3, 3), (2, 3, 8), (2, 4, 0), (2, 4, 2), (3, 0, 2),
    (3, 0, 8), (3, 1, 6), (3, 1, 7), (3, 2, 0), (3, 2, 2), (3, 2, 6),
    (3, 2, 7), (3, 2, 8), (3, 3, 1), (3, 3, 2), (3, 3, 4), (3, 3, 7),
    (3, 4, 3), (3, 4, 5), (4, 0, 2), (4, 0, 4), (4, 0, 5), (4, 0, 6),
    (4, 1, 0), (4, 1, 4), (4, 1, 6), (4, 1, 7), (4, 1, 8), (4, 2, 0),
    (4, 2, 2), (4, 2, 6), (4, 3, 0), (4, 3, 1), (4, 3, 6), (4, 4, 2),
    (4, 4, 6), (4, 4, 8),
]


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def in_win(z, shape):
    return all(0 <= z[i] < shape[i] for i in range(3))


def pred(x, j):
    return tuple(x[i] - E_J[j][i] for i in range(3))


def automaton(shape, marks):
    zeta = set(marks)
    sites = [
        (x, y, z)
        for x in range(shape[0])
        for y in range(shape[1])
        for z in range(shape[2])
    ]
    sites.sort(key=lambda p: p[0] + p[1] + p[2])
    eta = {}
    for x in sites:
        ones = sum(1 for j in range(3) if eta.get(pred(x, j), 0) == 1)
        eta[x] = 1 if ones >= 2 or x in zeta else 0
    seed, amp, proc = [], [], []
    for x, v in eta.items():
        if v != 1:
            continue
        n1 = sum(1 for j in range(3) if eta.get(pred(x, j), 0) == 1)
        if n1 == 0:
            seed.append(x)
        elif n1 == 1:
            amp.append(x)
        else:
            proc.append(x)
    return eta, seed, amp, proc


def nn_triangle_in_window(shape):
    """Z^3 nearest-neighbour graph is bipartite: no 3-cycles."""
    verts = [
        (x, y, z)
        for x in range(shape[0])
        for y in range(shape[1])
        for z in range(shape[2])
    ]
    nbrs = {v: [] for v in verts}
    for v in verts:
        for j in range(3):
            w = tuple(v[i] + E_J[j][i] for i in range(3))
            if w in nbrs:
                nbrs[v].append(w)
                nbrs[w].append(v)
    for v in verts:
        for a in nbrs[v]:
            for b in nbrs[v]:
                if a < b and a in nbrs[b]:
                    return (v, a, b)
    return None


def check_one(name, root, shape, marks, n_marks, stated_EAS):
    if len(marks) != n_marks:
        hit(f"{name}: {len(marks)} marks, stated {n_marks}")
        return
    if len(set(marks)) != len(marks):
        hit(f"{name}: duplicate marks")
        return
    outside = [m for m in marks if not in_win(m, shape)]
    if outside:
        hit(f"{name}: marks outside window {shape}: {outside}")
        return
    if not in_win(root, shape):
        hit(f"{name}: root {root} outside window {shape}")
        return
    tri = nn_triangle_in_window(shape)
    if tri:
        hit(f"{name}: Z^3 NN triangle in the window: {tri}")
        return
    eta, seed, amp, proc = automaton(shape, marks)
    if eta.get(root) != 1:
        hit(f"{name}: root {root} is not 1 under the automaton")
        return
    E, A, S = stated_EAS
    if name == "W1":
        if set(marks) != set(seed) | set(amp):
            hit(
                f"W1 marks are not exactly seed∪amplified: "
                f"marks={sorted(marks)} seed={sorted(seed)} amp={sorted(amp)}"
            )
            return
        if len(seed) != 1 or len(amp) != 10:
            hit(f"W1 seed/amp counts {len(seed)},{len(amp)} != 1,10")
            return
    # ratios from stated tree counts (existence of the configuration + the
    # note's (E,A,S) arithmetic, checked as the claimed integers)
    if S < 1 or A < 1:
        hit(f"{name}: stated |S|={S} |A|={A}")
        return
    ratio = Fraction(E - 3 * (S - 1), A)
    sharp = E <= 3 * (S - 1) + A
    proved = E <= 3 * (S - 1) + 2 * A
    if sharp:
        hit(f"{name}: stated (E,A,S)={stated_EAS} does not refute the sharper budget")
        return
    if not proved:
        hit(f"{name}: stated (E,A,S)={stated_EAS} lies outside block 30's budget")
        return
    print(
        f"OK: {name} root {root} in window {shape}, {n_marks} marks inside, "
        f"eta[root]=1, seed={len(seed)} amp={len(amp)} proc={len(proc)}, "
        f"(E,A,S)={stated_EAS} ratio {ratio}, sharp={sharp} proved={proved}"
    )


def main():
    # sibling forks are √2 pairs in a level plane (triangular lattice), not
    # Z^3 NN edges; the note declares them separately from arrows {x, x−e_j}.
    check_one("W1", W1_ROOT, W1_WIN, W1_MARKS, 11, (16, 10, 1))
    check_one("W2", W2_ROOT, W2_WIN, W2_MARKS, 40, (20, 12, 1))
    check_one("W3", W3_ROOT, W3_WIN, W3_MARKS, 74, (23, 12, 2))
    if Fraction(16 - 0, 10) != Fraction(8, 5):
        hit("W1 ratio not 8/5")
    if Fraction(20 - 0, 12) != Fraction(5, 3) or Fraction(23 - 3, 12) != Fraction(5, 3):
        hit("W2/W3 ratio not 5/3")
    if HITS:
        print("SUMMARY: pattern (a) WITNESS REALIZABILITY fired; " + "; ".join(HITS))
    else:
        print(
            "SUMMARY: pattern (a) WITNESS REALIZABILITY — W1/W2/W3 marks lie in "
            "the stated Z^3 windows [0,4)^2×[0,7) and [0,5)^2×[0,9); the NN graph "
            "of each window is triangle-free (Z^3 bipartite); roots are 1 under "
            "the one-sided automaton; W1's 11 marks are exactly its seed and ten "
            "amplified 1-sites; stated (E,|A|,|S|) give ratios 8/5, 5/3, 5/3 "
            "inside block 30's budget and above the sharper one; 0 failures; "
            "attack does not fire"
        )


if __name__ == "__main__":
    main()
