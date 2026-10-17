"""C8 support: classify the 720 BKSF orderings into codes (L=4), rotation
stabilizers, (code, C2) pairs, 'covered' pairs (some ordering of the class whose
plaquette span P_R preserves), and signed preservation of the two uniform
sectors.  Saves c8_pairs.pkl for c8_pairtest.py."""
import itertools, pickle
from collections import Counter
from mpd_core import Tableau, rotations
from bksf_core import BKSF, edge_perm_map, permute, kind

L = 4
R = rotations()
imgs = {M: edge_perm_map(L, M) for M in R}
orders = list(itertools.permutations(range(6)))


def tab_of(gs):
    T = Tableau(3 * L ** 3)
    for g in gs:
        T.insert(g)
    return T


def in_span(T, P):
    q = T.reduce(P)
    return q[0] == 0 and q[1] == 0


reps, rep_tab, cls_of = [], [], {}
codes = {}
for o in orders:
    b = BKSF(L, o)
    org = [b.plaq((0, 0, 0), c) for c in range(3)]
    found = None
    for i, T in enumerate(rep_tab):
        if all(in_span(T, P) for P in org):
            found = i
            break
    if found is None:
        rep_tab.append(tab_of([g[3] for g in b.gens(1)]))
        reps.append(o)
        found = len(reps) - 1
    cls_of[o] = found
classes = Counter(cls_of.values())
print("distinct codes:", len(reps), " class sizes:", sorted(set(classes.values())))
# symmetric check of containment (rep in each member) for safety
ok = True
for o, i in cls_of.items():
    T = tab_of([g[3] for g in BKSF(L, o).gens(1)])
    ok &= all(in_span(T, BKSF(L, reps[i]).plaq((0, 0, 0), c)) for c in range(3))
print("class membership symmetric:", ok)

stab = {}
for i, o in enumerate(reps):
    b = BKSF(L, o)
    org = [b.B((0, 0, 0))] + [b.plaq((0, 0, 0), c) for c in range(3)]
    stab[i] = [M for M in R if all(in_span(rep_tab[i], permute(P, imgs[M])) for P in org)]
print("stabilizer orders:", Counter(len(s) for s in stab.values()))

pairs = []
for i in range(len(reps)):
    for M in stab[i]:
        if kind(M) in ("C2axis", "C2edge"):
            pairs.append((i, M))
print("(code, C2) pairs:", len(pairs), Counter(kind(M) for _, M in pairs))

# covered: some ordering o in the class has P_R(span S^o) = span S^o (plaquettes only)
plaqtab = {}
def ptab(o):
    if o not in plaqtab:
        b = BKSF(L, o)
        plaqtab[o] = tab_of([g[3] for g in b.gens(1) if g[0] == "S"])
    return plaqtab[o]
members = {i: [o for o, j in cls_of.items() if j == i] for i in range(len(reps))}
covered = {}
for (i, M) in pairs:
    cov = None
    for o in members[i]:
        b = BKSF(L, o)
        if all(in_span(ptab(o), permute(b.plaq((0, 0, 0), c), imgs[M])) for c in range(3)):
            cov = o
            break
    covered[(i, tuple(map(tuple, M)))] = cov
ncov = sum(1 for v in covered.values() if v is not None)
print("covered pairs:", ncov, " uncovered:", len(pairs) - ncov)
unc_by = Counter((len(stab[i]), kind(M)) for (i, M) in pairs if covered[(i, M)] is None)
print("uncovered by (stabilizer order, C2 kind):", dict(unc_by))

# signed preservation of the two uniform sectors, and ordering-independence of the signed groups
okp, okind = True, True
for i, o in enumerate(reps):
    for s in (1, -1):
        b = BKSF(L, o)
        T = tab_of([g[3] for g in b.gens(s)])
        assert T.consistent
        org = [b.B((0, 0, 0))] + [b.plaq((0, 0, 0), c, s) for c in range(3)]
        for M in stab[i]:
            okp &= all(T.sign_of(permute(P, imgs[M])) == 1 for P in org)
        for o2 in members[i][:6]:
            b2 = BKSF(L, o2)
            okind &= all(T.sign_of(b2.plaq((0, 0, 0), c, s)) == 1 for c in range(3))
print("P_R preserves both uniform signed groups for every stabilizing R:", okp)
print("uniform signed groups independent of ordering within class (6 members tested each):", okind)
pickle.dump({"reps": reps, "stab": stab, "pairs": pairs, "covered": covered}, open("c8_pairs.pkl", "wb"))
