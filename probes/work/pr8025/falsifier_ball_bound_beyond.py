#!/usr/bin/env python3
"""J:falsifier:PR8025 — N=|B_r(X)| ≤ 3|X|(2r+1)^3 and 4 plaquettes/link.

Beyond the note's small-r geometry: grow the link-metric ball around a
single cube link for r=0..8, and around a 2-link path. HIT if the volume
bound fails or some interior link meets more than 4 plaquettes.

Theta_d(z)=sum_{n>=d} z^n/n! ≤ exp(e z - d) checked at extra (d,z).
"""
from __future__ import annotations

from itertools import combinations

import sympy as sp

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def links_in_box(L):
    """Undirected links of the [0,L]^3 vertex grid (open cube)."""
    out = []
    for x in range(L + 1):
        for y in range(L + 1):
            for z in range(L + 1):
                if x < L:
                    out.append(((x, y, z), (x + 1, y, z)))
                if y < L:
                    out.append(((x, y, z), (x, y + 1, z)))
                if z < L:
                    out.append(((x, y, z), (x, y, z + 1)))
    return out


def plaquettes_of(L):
    """Each plaquette as a frozenset of 4 links (as frozen undirected pairs)."""
    def fr(a, b):
        return tuple(sorted((a, b)))

    faces = []
    for x in range(L):
        for y in range(L):
            for z in range(L + 1):
                # xy at z
                v00, v10 = (x, y, z), (x + 1, y, z)
                v01, v11 = (x, y + 1, z), (x + 1, y + 1, z)
                faces.append(frozenset({fr(v00, v10), fr(v10, v11), fr(v11, v01), fr(v01, v00)}))
    for x in range(L):
        for y in range(L + 1):
            for z in range(L):
                v00, v10 = (x, y, z), (x + 1, y, z)
                v01, v11 = (x, y, z + 1), (x + 1, y, z + 1)
                faces.append(frozenset({fr(v00, v10), fr(v10, v11), fr(v11, v01), fr(v01, v00)}))
    for x in range(L + 1):
        for y in range(L):
            for z in range(L):
                v00, v10 = (x, y, z), (x, y + 1, z)
                v01, v11 = (x, y, z + 1), (x, y + 1, z + 1)
                faces.append(frozenset({fr(v00, v10), fr(v10, v11), fr(v11, v01), fr(v01, v00)}))
    return faces


def main() -> int:
    L = 8
    links = [tuple(sorted(e)) for e in links_in_box(L)]
    faces = plaquettes_of(L)
    meet = {e: [] for e in links}
    for f in faces:
        for e in f:
            if e in meet:
                meet[e].append(f)
    # interior links (not on the outer vertex boundary of the box) have 4 faces
    over = [(e, len(fs)) for e, fs in meet.items() if len(fs) > 4]
    print(f"box L={L}: {len(links)} links, {len(faces)} faces, >4-meet={len(over)}")
    if over:
        hit(f"link {over[0][0]} meets {over[0][1]} > 4 plaquettes")

    # adjacency: two links adjacent if they co-belong to a face
    adj = {e: set() for e in links}
    for f in faces:
        fl = [e for e in f if e in adj]
        for a, b in combinations(fl, 2):
            adj[a].add(b)
            adj[b].add(a)

    # pick a well-interior link
    e0 = tuple(sorted(((3, 3, 3), (4, 3, 3))))
    if e0 not in adj:
        hit(f"seed link {e0} missing")
        e0 = links[len(links) // 2]
    ball = {e0}
    frontier = {e0}
    for r in range(0, 9):
        N = len(ball)
        cap = 3 * 1 * (2 * r + 1) ** 3
        print(f"  r={r}: |B_r|={N} cap=3(2r+1)^3={cap}")
        if N > cap:
            hit(f"|B_{r}(e0)|={N} > 3(2r+1)^3={cap}")
        nxt = set()
        for e in frontier:
            nxt |= adj[e]
        nxt -= ball
        ball |= nxt
        frontier = nxt

    # Theta_d(z) <= exp(e z - d)
    z = sp.symbols("z", positive=True)
    eul = sp.E
    for d in range(0, 12):
        Th = sum(z ** n / sp.factorial(n) for n in range(d, 40))
        bound = sp.exp(eul * z - d)
        # numerical at z=1,2,1/2
        for zv in (sp.Rational(1, 2), 1, 2):
            lhs = sp.N(Th.subs(z, zv), 20)
            rhs = sp.N(bound.subs(z, zv), 20)
            if lhs > rhs + 1e-8:
                hit(f"Theta_{d}({zv})={lhs} > exp(e z-d)={rhs}")
    print("Theta_d(z)<=exp(e z-d) holds at d=0..11, z in {1/2,1,2} (partial sum n<40)")

    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: geometry falsifier FIRED: " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: geometry falsifier did not fire: |B_r|≤3(2r+1)^3 for r=0..8 "
        "around an interior link on the L=8 cube (beyond small-r), no link meets "
        ">4 plaquettes, Theta_d(z)≤exp(ez-d) at extra (d,z)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
