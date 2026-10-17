"""(4) group law of the signed direction permutations.
Element = (p, s): gamma_d -> s[d] gamma_{p[d]}.  Compose g*h = g(h(.))."""
import itertools
from collections import Counter
from mpd_core import *

ID = (tuple(range(6)), (1,) * 6)
MINUS = (tuple(range(6)), (-1,) * 6)


def comp(g, h):
    pg, sg = g
    ph, sh = h
    return (tuple(pg[ph[d]] for d in range(6)), tuple(sh[d] * sg[ph[d]] for d in range(6)))


def closure(gens):
    G = {ID}
    frontier = [ID]
    while frontier:
        nf = []
        for x in frontier:
            for g in gens:
                y = comp(g, x)
                if y not in G:
                    G.add(y)
                    nf.append(y)
        frontier = nf
        if len(G) > 5000:
            break
    return G


def order(g):
    x, k = g, 1
    while x != ID:
        x = comp(g, x)
        k += 1
    return k


def mat_of_dirperm(p):
    for M in rotations() + improper():
        if dir_perm(M) == p:
            return M


R = rotations()
C4 = ((0, -1, 0), (1, 0, 0), (0, 0, 1))      # x->y->-x->-y about z
C3 = ((0, 0, 1), (1, 0, 0), (0, 1, 0))       # x->y->z->x about (111)
assert C4 in R and C3 in R
assert dir_perm(C4) == (1, 3, 2, 4, 0, 5)
pC4, pC3 = dir_perm(C4), dir_perm(C3)
print("dir perm C4", pC4, "sign", perm_sign(pC4), "; C3", pC3, "sign", perm_sign(pC3))

axisC2 = [M for M in R if all(M[i][i] != 0 for i in range(3)) and M != ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
edgeC2 = []
for M in R:
    sq = tuple(tuple(sum(M[i][k] * M[k][j] for k in range(3)) for j in range(3)) for i in range(3))
    if sq == ((1, 0, 0), (0, 1, 0), (0, 0, 1)) and M not in axisC2 and M != sq:
        edgeC2.append(M)
assert len(axisC2) == 3 and len(edgeC2) == 6

sizes = Counter()
good = []
for e4 in admissible_eps(C4):
    for e3 in admissible_eps(C3):
        G = closure([(pC4, e4), (pC3, e3)])
        has_m1 = MINUS in G
        sizes[(len(G), has_m1)] += 1
        if len(G) == 48 and has_m1:
            good.append((e4, e3, G))
print("group sizes over 1024 (size, contains -1):", dict(sizes))
print("order-48 groups containing -1:", len(good))

ok = len(good) == 128
sig = Counter()
structs = Counter()
for e4, e3, G in good:
    # kernel of projection to direction permutations
    ker = [g for g in G if g[0] == tuple(range(6))]
    ok &= sorted(ker) == sorted([ID, MINUS])
    images = {g[0] for g in G}
    ok &= len(images) == 24 and images == {dir_perm(M) for M in R}
    sq_ax = {comp(g, g) for g in G for M in axisC2 if g[0] == dir_perm(M)}
    sq_ed = {comp(g, g) for g in G for M in edgeC2 if g[0] == dir_perm(M)}
    sig[(tuple(sorted(sq_ax)) == (ID,), tuple(sorted(sq_ed)) == (MINUS,))] += 1
    structs[tuple(sorted(Counter(order(g) for g in G).items()))] += 1
print("(axis C2 lifts square to +1, edge C2 lifts square to -1):", dict(sig))
print("element-order profile(s) of the 128 groups:", dict(structs))
ok &= sig == Counter({(True, True): 128})

# 'forced' argument, checked over ALL admissible eps (not only inside good groups):
ax_sq = Counter(); ed_sq = Counter()
for M in axisC2:
    for e in admissible_eps(M):
        g = (dir_perm(M), e); s = comp(g, g)
        ax_sq["+1" if s == ID else ("-1" if s == MINUS else "other")] += 1
for M in edgeC2:
    for e in admissible_eps(M):
        g = (dir_perm(M), e); s = comp(g, g)
        ed_sq["+1" if s == ID else ("-1" if s == MINUS else "other")] += 1
print("all admissible lifts of axis C2: squares", dict(ax_sq), "; of edge C2:", dict(ed_sq))
ok &= ax_sq["-1"] == 0 and ed_sq["+1"] == 0

# Is the extension the spin double cover 2O?  In 2O every C2 lift squares to -1.
print("Comparison: binary octahedral 2O has order profile",
      sorted({1: 1, 2: 1, 3: 8, 4: 18, 6: 8, 8: 12}.items()),
      "; GL(2,3):", sorted({1: 1, 2: 13, 3: 8, 4: 6, 6: 8, 8: 12}.items()),
      "; S4 x Z2:", sorted({1: 1, 2: 19, 3: 8, 4: 12, 6: 8}.items()))
# A4 sub-extension splits?  lifts of the A4 subgroup (even dir perms)
e4, e3, G = good[0]
evenG = [g for g in G if perm_sign(g[0]) == 1]
c3lifts = [g for g in G if g[0] == pC3]
print("lifts of C3 have orders", sorted(order(g) for g in c3lifts),
      "; even part order", len(evenG), "orders", dict(Counter(order(g) for g in evenG)))
print("OVERALL", "PASS" if ok else "FAIL")
