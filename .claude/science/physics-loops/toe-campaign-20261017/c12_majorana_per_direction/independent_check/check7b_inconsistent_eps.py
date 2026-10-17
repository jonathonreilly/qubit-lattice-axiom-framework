"""Control for (7): with an admissible but group-inconsistent eps for an edge C2
(lift whose square is neither +1 nor -1), lambda depends on the pair / path,
so the consistent-group requirement is load-bearing."""
import itertools
from collections import Counter
from mpd_core import *
import check7_fractionalization as c7  # builds L=10 tableaux (argv default)
lat = c7.lat
M = ((0, 1, 0), (1, 0, 0), (0, 0, -1))   # edge C2 about (1,1,0)
res = Counter()
for eps in admissible_eps(M):
    g = (dir_perm(M), eps)
    from check4_grouplaw import comp, ID, MINUS
    sq = comp(g, g)
    kind = "+1" if sq == ID else ("-1" if sq == MINUS else "other")
    lams = set()
    for x in c7.xs_edge:
        y = apply(M, x)
        for o in itertools.permutations(range(3)):
            labs = c7.path_labels(x, y, o)
            S = lat.to_pauli((0, labs))
            SR = lat.to_pauli(act_mono(lat, M, eps, (0, labs)))
            lams.add(c7.tabs[(1, 1, 1)].sign_of(mul(dag(S), SR)))
    res[(kind, tuple(sorted(lams)))] += 1
print("edge C2 eps classes (square kind, set of lambda over pairs/paths):", dict(res))
