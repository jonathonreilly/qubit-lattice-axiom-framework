#!/usr/bin/env python3
"""J:attack-g:PR8025 — brute-force §1–3 finite geometry, D_R, Theta identities.

Cubic link metric: each link in <=4 plaquettes, each face 4 links of diameter 1;
N<=3|X|(2r+1)^3; internal F<=N; crossing faces of B_r(X) have dist>=r.
SU(3) PW cutoff dim D_R equals the stated closed form.
Theta_d(z)=sum_{n>=d} z^n/n!, Theta_{d}'=Theta_{d-1}, integral identity for (S),
and Theta_d(z)<=exp(e z-d). Weighted plaquette choices: <=4 per link, <=16 from a face.
"""
from __future__ import annotations

import itertools
import math
import sys
from collections import defaultdict
from fractions import Fraction as Fr

import sympy as sp


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def dim_pq(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def D_closed(R: int) -> Fr:
    return Fr(
        (R + 2) ** 2
        * (R + 3) ** 2
        * (R + 1)
        * (R + 4)
        * (3 * (R + 2) ** 2 + 3 * (R + 2) + 2),
        2880,
    )


def main() -> int:
    for R in range(0, 16):
        s = sum(dim_pq(p, q) ** 2 for p in range(R + 1) for q in range(R + 1 - p))
        cl = D_closed(R)
        if cl.denominator != 1 or cl.numerator != s:
            return hits(f"D_R closed form fails at R={R}: sum={s} closed={cl}")
    print("D_R closed form = sum_{p+q<=R} dim(p,q)^2 for R=0..15: True")

    # g_R = [ceil(3(R+1)^2/4) + 3(R+1)] / a  — integer numerator as written
    a = sp.symbols("a", positive=True)
    for R in range(0, 12):
        num = math.ceil(3 * (R + 1) ** 2 / 4) + 3 * (R + 1)
        # ceil(3 m^2 / 4) for m=R+1
        m = R + 1
        c = (3 * m * m + 3) // 4  # 3m^2/4 ceil: 3m^2 = 4q+r, r=0 => q, else q+1
        # check via integers
        if 3 * m * m % 4 == 0:
            ceil_q = 3 * m * m // 4
        else:
            ceil_q = 3 * m * m // 4 + 1
        if ceil_q + 3 * m != num:
            return hits(f"g_R numerator mismatch at R={R}")
        _ = num / a  # formula shape
    print("g_R numerator ceil(3(R+1)^2/4)+3(R+1) for R=0..11: True")

    z, d = sp.symbols("z d", nonnegative=True, integer=True)
    # Theta_n'(z) = Theta_{n-1}(z) as formal series, checked at integer n, truncated
    zz = sp.symbols("zz")
    for n in range(1, 8):
        Th_n = sum(zz**k / sp.factorial(k) for k in range(n, 24))
        Th_nm = sum(zz**k / sp.factorial(k) for k in range(n - 1, 24))
        deriv = sp.diff(Th_n, zz)
        # agree through degree 22
        if sp.series(deriv - Th_nm, zz, 0, 22).removeO() != 0:
            return hits(f"Theta_{n}' != Theta_{n-1}")
    print("Theta_n' = Theta_{n-1} (truncated series n=1..7): True")

    # integral_0^T Theta_r(c s) ds = Theta_{r+1}(c T)/c  (r>=0, Theta_{r+1}(0)=0)
    c, T, s = sp.symbols("c T s", positive=True)
    for r in range(0, 5):
        Th_r = sum((c * s) ** k / sp.factorial(k) for k in range(r, 18))
        integ = sp.integrate(Th_r, (s, 0, T))
        Th_rp = sum((c * T) ** k / sp.factorial(k) for k in range(r + 1, 18))
        # remainder O(T^18); compare polynomials through degree 16
        diff = sp.expand(integ - Th_rp / c)
        coeffs = sp.Poly(sp.series(diff, T, 0, 16).removeO(), T).coeffs()
        if any(sp.simplify(cf) != 0 for cf in coeffs):
            return hits(f"integral Theta_{r} identity fails")
    print("integral_0^T Theta_r(c s) ds = Theta_{r+1}(c T)/c : True")

    # (S) factor: 2 v N_cross / (32 v) * N_cross<=4N => N/4
    v, N, NX, NA = sp.symbols("v N N_cross AbsA", positive=True)
    N_cross = 4 * N
    factor = 2 * v * N_cross / (32 * v)
    if sp.simplify(factor - N / 4) != 0:
        return hits("(S) prefactor 2 v N_cross/(32 v) with N_cross=4N is not N/4")
    print("(S) prefactor N/4 from N_cross<=4N: True")

    # Theta_d(z) <= exp(e z - d): 1_{n>=d} <= exp(n-d)
    for n, dd in itertools.product(range(0, 12), range(0, 8)):
        lhs = 1 if n >= dd else 0
        rhs = math.exp(n - dd)
        if lhs > rhs + 1e-12:
            return hits(f"1_{{n>={dd}}} <= exp(n-{dd}) fails at n={n}")
    print("1_{n>=d} <= exp(n-d) on n,d in 0..11: True")

    # cubic lattice geometry in a vertex box
    L = 6
    verts = list(itertools.product(range(L), repeat=3))

    def wrap(x):
        return tuple(c % L for c in x)

    links = []
    for v0 in verts:
        for d in range(3):
            links.append((v0, d))
    # plaquettes: vertex + two distinct directions, two orientations of the square
    plaquettes = []
    for v0 in verts:
        for d1, d2 in itertools.combinations(range(3), 2):
            e1 = tuple(1 if i == d1 else 0 for i in range(3))
            e2 = tuple(1 if i == d2 else 0 for i in range(3))
            a = v0
            b = wrap(tuple(v0[i] + e1[i] for i in range(3)))
            c = wrap(tuple(v0[i] + e2[i] for i in range(3)))
            # four links: (a,d1), (a,d2), (c,d1), (b,d2)
            face = ((a, d1), (a, d2), (c, d1), (b, d2))
            plaquettes.append(face)

    link_to_faces = defaultdict(list)
    for fi, face in enumerate(plaquettes):
        if len(set(face)) != 4:
            return hits("a plaquette does not have 4 distinct links")
        for ln in face:
            link_to_faces[ln].append(fi)
    for ln, fs in link_to_faces.items():
        if len(fs) != 4:
            return hits(f"link {ln} incident to {len(fs)} != 4 plaquettes")
    print(f"torus {L}^3: {len(links)} links, {len(plaquettes)} faces, 4+4 incidence: True")

    # diameter 1: any two distinct links of a face share a plaquette (are adjacent)
    for face in plaquettes:
        for u, w in itertools.combinations(face, 2):
            if not set(link_to_faces[u]) & set(link_to_faces[w]):
                return hits("two links of a face are not adjacent in the link metric")
    print("every face has diameter 1: True")

    # weighted choice: from a 4-link face, multiplicity-count of incident plaquettes
    for face in plaquettes[:20]:
        m = sum(len(link_to_faces[ln]) for ln in face)
        if m > 16:
            return hits(f"face weighted plaquette count {m} > 16")
        if m != 16:
            # each of 4 links has exactly 4 on the torus
            return hits(f"torus face multiplicity {m} != 16")
    print("subsequent-face weighted choice sum = 16 (torus): True")

    # adjacency graph and balls around one link, unwrapped in a large padded box
    # use non-periodic 7^3 vertices to avoid wrap artifacts for small r
    L2 = 7
    links2 = []
    for v0 in itertools.product(range(L2), repeat=3):
        for d in range(3):
            nxt = tuple(v0[i] + (1 if i == d else 0) for i in range(3))
            if all(0 <= nxt[i] < L2 for i in range(3)):
                links2.append((v0, d))
    pla2 = []
    for v0 in itertools.product(range(L2), repeat=3):
        for d1, d2 in itertools.combinations(range(3), 2):
            e1 = tuple(1 if i == d1 else 0 for i in range(3))
            e2 = tuple(1 if i == d2 else 0 for i in range(3))
            b = tuple(v0[i] + e1[i] for i in range(3))
            c = tuple(v0[i] + e2[i] for i in range(3))
            d = tuple(v0[i] + e1[i] + e2[i] for i in range(3))
            if not all(0 <= x < L2 for x in d):
                continue
            face = ((v0, d1), (v0, d2), (c, d1), (b, d2))
            if all(ln in set(links2) for ln in face):  # noqa: slow but L2=7 is ok
                pla2.append(face)
    lset = set(links2)
    l2f = defaultdict(list)
    for fi, face in enumerate(pla2):
        for ln in face:
            l2f[ln].append(fi)

    # pick an interior link
    seed = ((3, 3, 3), 0)
    if seed not in lset:
        return hits("interior seed missing")
    # BFS in the link metric
    dist = {seed: 0}
    q = [seed]
    qi = 0
    while qi < len(q):
        u = q[qi]
        qi += 1
        nbrs = set()
        for fi in l2f[u]:
            for w in pla2[fi]:
                if w != u:
                    nbrs.add(w)
        for w in nbrs:
            if w not in dist:
                dist[w] = dist[u] + 1
                q.append(w)
    for r in range(0, 4):
        ball = [ln for ln, dd in dist.items() if dd <= r]
        N = len(ball)
        bound = 3 * (2 * r + 1) ** 3
        print(f"|X|=1 r={r} N={N} bound 3(2r+1)^3={bound}")
        if N > bound:
            return hits(f"N={N} > 3(2r+1)^3={bound} at r={r}")
        # internal faces of Omega=ball (all 4 links in ball)
        F = sum(1 for face in pla2 if all(ln in dist and dist[ln] <= r for ln in face))
        if F > N:
            return hits(f"internal F={F} > N={N} at r={r}")
        # crossing: some but not all links in ball
        for face in pla2:
            insides = [ln for ln in face if ln in dist and dist[ln] <= r]
            if 0 < len(insides) < 4:
                dface = min(dist.get(ln, 10**9) for ln in face)
                if dface < r:
                    return hits(f"crossing face at dist {dface} < r={r}: {face}")
    print("ball sizes, F<=N, crossing dist>=r for r=0..3: True")

    print(
        "SUMMARY: pattern has no purchase on this note: D_R closed form, g_R numerator, "
        "Theta derivative/integral/(S) prefactor, cubic 4+4 incidence, face diameter 1, "
        "weighted choice 16, and N<=3(2r+1)^3 with F<=N and crossing dist>=r all hold "
        "as written on the enumerated boxes"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
