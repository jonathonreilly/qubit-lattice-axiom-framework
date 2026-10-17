"""(1) all 8 sectors: valid commuting signed groups, log2 code dim, L=4,6 (and 5).
Also basic Majorana sanity and per-generator Hermiticity."""
import sys, time, itertools
from mpd_core import *

ok_all = True


def report(name, ok):
    global ok_all
    ok_all &= ok
    print(("PASS " if ok else "FAIL ") + name, flush=True)


# Majorana sanity on L=2
lat = Lattice(2)
gs = [(v, d) for v in [(0, 0, 0), (1, 0, 0)] for d in range(6)]
ok = True
for a, b in itertools.product(gs, gs):
    pa, pb = lat.gamma(*a), lat.gamma(*b)
    prod = mul(pa, pa)
    ok &= is_identity(prod) and prod[2] == 0
    ac = anticommute(pa, pb)
    want = 1 if (a[0] == b[0] and a[1] != b[1]) else 0
    ok &= (ac == want)
    ok &= dag(pa) == pa
report("Majoranas: square +1, Hermitian, anticommute on-site, commute off-site", ok)
B = lat.to_pauli(lat.B_mono((0, 0, 0)))
report("B_v = Z1 Z2 Z3 exactly (+ sign): %s" % (B,), B == (0, 0b111, 0))

for L in [4, 5, 6]:
    lat = Lattice(L)
    for sec in all_sectors():
        t0 = time.time()
        gens = [lat.to_pauli(m) for m in lat.generators(sec)]
        herm = all(dag(g) == g and mul(g, g) == (0, 0, 0) for g in gens)
        # commutation: generators are local; test all pairs via local neighborhoods
        # (exact: all pairs, using symplectic bit test -- feasible)
        comm = True
        # bucket by site support to keep it fast but exhaustive over overlapping pairs
        supp = []
        for g in gens:
            s = set()
            m = g[0] | g[1]
            while m:
                b = m & -m
                s.add((b.bit_length() - 1) // 3)
                m ^= b
            supp.append(s)
        bysite = {}
        for i, s in enumerate(supp):
            for x in s:
                bysite.setdefault(x, []).append(i)
        for x, lst in bysite.items():
            for i in lst:
                for j in lst:
                    if i < j and anticommute(gens[i], gens[j]):
                        comm = False
        T = Tableau(lat.n)
        for g in gens:
            T.insert(g)
        k = lat.n - T.rank()
        lab = "".join("+" if sec[o] > 0 else "-" for o in ORIENTS)
        good = herm and comm and T.consistent
        print("  L=%d sector(yz,zx,xy)=%s herm=%s commute=%s no(-I)=%s log2dim=%d  (%.1fs)"
              % (L, lab, herm, comm, T.consistent, k, time.time() - t0), flush=True)
        if L in (4, 6):
            report("L=%d sector %s valid with log2 dim 3" % (L, lab), good and k == 3)
print("OVERALL", "PASS" if ok_all else "FAIL")
