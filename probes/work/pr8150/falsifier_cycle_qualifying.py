#!/usr/bin/env python3
"""J:falsifier:PR8150 — cycle lemma: no order qualifies on a cycle.

Beyond the note's plaquette: C4, C6, C8. Qualifying = every site records
at most one already-recorded neighbour. HIT if a cycle has a qualifying
order. Path3 is the contrast (some orders qualify).
"""
from itertools import permutations

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def n_qual(n, edges):
    """n sites 0..n-1, undirected edges."""
    nbr = {i: [] for i in range(n)}
    for a, b in edges:
        nbr[a].append(b)
        nbr[b].append(a)
    c = 0
    for perm in permutations(range(n)):
        pos = [0] * n
        for t, i in enumerate(perm):
            pos[i] = t
        ok = True
        for s in range(n):
            rec = sum(1 for u in nbr[s] if pos[u] < pos[s])
            if rec >= 2:
                ok = False
                break
        if ok:
            c += 1
    return c


def main() -> int:
    # cycles
    for n in (4, 6, 8):
        edges = [(i, (i + 1) % n) for i in range(n)]
        q = n_qual(n, edges)
        print(f"C{n}: qualifying orders {q} / {n}!")
        if q != 0:
            hit(f"C{n} has {q} qualifying orders (stated 0 on a cycle)")
    # path3 contrast
    qP = n_qual(3, [(0, 1), (1, 2)])
    print(f"path3: qualifying {qP} / 6 (stated some, 4)")
    if qP == 0:
        hit("path3 has 0 qualifying (cycle/path would not separate)")
    if HITS:
        print("SUMMARY: falsifier FIRED; " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: falsifier (cycle lemma) did not fire — C4, C6, C8 have 0 "
        f"qualifying orders; path3 has {qP}/6; beyond the note's plaquette"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
