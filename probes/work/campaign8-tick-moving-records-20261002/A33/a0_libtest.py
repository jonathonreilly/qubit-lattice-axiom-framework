"""A33 a0: library self-test against known facts.
 - A20: star S_0 and face F_0 are exactly fixed by all 24 soldered rotations.
 - invariant-shape dimensions per shell (hand counts in the report).
 - group sizes: O 24, D4 8, C4 4, C3 3, T 12.
"""
import signal
signal.alarm(55)
from p2lib import (group, invariant_basis, ball_sites, exact_invariant, pat_str, rot_pattern,
                   act, ROT)

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
star = {}
for a in range(3):
    for s in (1, -1):
        star[tuple(s * E[a][i] for i in range(3))] = a + 1
face = {}
for a in range(3):
    for b in range(a + 1, 3):
        c = 3 - a - b
        for s in (1, -1):
            for t in (1, -1):
                y = tuple(s * E[a][i] + t * E[b][i] for i in range(3))
                face[y] = c + 1
O = group("O")
print("group sizes O,D4z,C4z,C3,T:", len(O), len(group("D4")), len(group("C4")), len(group("C3")), len(group("T")))
print("star exactly O-invariant:", exact_invariant(star, O), "; face exactly O-invariant:", exact_invariant(face, O))
print("face =", pat_str(face))
for r2 in (1, 2, 3, 4, 5, 6):
    B = ball_sites(r2)
    bO, orbO = invariant_basis(B, O)
    bD, orbD = invariant_basis(B, group("D4", 2))
    print(f"site-centred ball r^2<={r2}: |B|={len(B)}  dim O-invariant={len(bO)}  dim D4z-invariant={len(bD)}")
c2 = (1, 1, 1)
for r2 in (0.75, 2.75, 4.75, 6.75):
    B = ball_sites(r2, c2)
    bO, _ = invariant_basis(B, O, c2)
    bC3, _ = invariant_basis(B, group("C3"), c2)
    print(f"cube-centred ball |y-c|^2<={r2}: |B|={len(B)}  dim O-invariant={len(bO)}  dim C3-invariant={len(bC3)}")
# star is the unique nonzero O-invariant pattern on the 7-site star
bS, _ = invariant_basis(ball_sites(1), O)
print("O-invariant basis on the star:", [pat_str(b) for b in bS], "equals star:", bS[0] == star)
