"""(7) pair test for eta_f(C2,C2) of the B-violation fermion, under a
consistent group action (eps taken from one of the 128 order-48 groups).

S = product of edge operators along a lattice path x -> Rx (excitations at x, Rx).
S^R = image of S under gamma_{v,d} -> eps(d) gamma_{Rv,Rd} (R a site-centred C2).
lambda = sign of S^dag S^R in the signed stabilizer group;  eta_f = -lambda
(theta_f = -1).
"""
import sys, time, itertools
from collections import Counter, defaultdict
from mpd_core import *
from check4_grouplaw import closure, comp, ID, MINUS, C4, C3, axisC2, edgeC2  # noqa (runs check4 prints)

L = int(sys.argv[1]) if len(sys.argv) > 1 else 10
lat = Lattice(L)
R = rotations()


def path_labels(x, y, order):
    labs = []
    cur = list(x)
    for a in order:
        while cur[a] != y[a]:
            step = 1 if y[a] > cur[a] else -1
            if step == 1:
                labs += lat.edge_labels(tuple(cur), a)
            else:
                v = list(cur); v[a] -= 1
                labs += lat.edge_labels(tuple(v), a)
            cur[a] += step
    return labs


def detour_labels(x, y, order, off_axis, off):
    """go off by `off` along off_axis, then Manhattan, then back."""
    x2 = list(x); x2[off_axis] += off
    y2 = list(y); y2[off_axis] += off
    return path_labels(x, tuple(x2), [off_axis]) + path_labels(tuple(x2), tuple(y2), order) \
        + path_labels(tuple(y2), y, [off_axis])


t0 = time.time()
tabs = {}
for lab in [(1, 1, 1), (-1, -1, -1)]:
    sec = dict(zip(ORIENTS, lab))
    T = Tableau(lat.n)
    for m in lat.generators(sec):
        T.insert(lat.to_pauli(m))
    assert T.consistent and lat.n - T.rank() == 3
    tabs[lab] = T
print("L=%d tableaux built (%.1fs)" % (L, time.time() - t0), flush=True)
Bs = {v: lat.to_pauli(lat.B_mono(v)) for v in lat.all_sites()}
Sp = [lat.to_pauli(lat.plaq_mono(v, a, b)) for v in lat.all_sites() for (a, b) in ORIENTS]

# the 128 consistent groups
pC4, pC3 = dir_perm(C4), dir_perm(C3)
good = []
for e4 in admissible_eps(C4):
    for e3 in admissible_eps(C3):
        G = closure([(pC4, e4), (pC3, e3)])
        if len(G) == 48 and MINUS in G:
            good.append(G)
assert len(good) == 128

xs_axis = [(1, 0, 0), (2, 1, 0), (1, 1, 1), (1, 2, -1), (2, -1, 2)]
xs_edge = [(1, 0, 0), (0, 0, 1), (2, 0, 1), (1, -1, 2), (2, 1, -1)]


def syndrome_ok(P, pts):
    if any(anticommute(P, s) for s in Sp):
        return False
    fl = {v for v, b in Bs.items() if anticommute(P, b)}
    return fl == {tuple(c % L for c in p) for p in pts}


summary = defaultdict(Counter)
checked_syn = 0
for gi, G in enumerate(good):
    lifts_of = defaultdict(list)
    for g in G:
        lifts_of[g[0]].append(g[1])
    for cls, Ms, xs in [("axis", axisC2, xs_axis), ("edge", edgeC2, xs_edge)]:
        for M in Ms:
            for x in xs:
                # put x generically: rotate a template into a non-fixed point of M
                y = apply(M, x)
                if y == x:
                    continue
                paths = [path_labels(x, y, o) for o in itertools.permutations(range(3))]
                paths.append(detour_labels(x, y, [0, 1, 2], 2, 1))
                paths.append(detour_labels(x, y, [2, 1, 0], 0, -2))
                for labs in paths:
                    Smono = (0, labs)
                    S = lat.to_pauli(Smono)
                    for eps in lifts_of[dir_perm(M)]:
                        SR_m = act_mono(lat, M, eps, Smono)
                        SR = lat.to_pauli(SR_m)
                        if gi < 2:  # full syndrome check (expensive) on two groups
                            assert syndrome_ok(S, [x, y]) and syndrome_ok(SR, [x, y])
                            checked_syn += 1
                        for lab, T in tabs.items():
                            lam = T.sign_of(mul(dag(S), SR))
                            summary[(cls, lab)][lam] += 1
                            summary[(cls, lab, M, x)][lam] += 1
    if gi == 0:
        print("first group done (%.1fs)" % (time.time() - t0), flush=True)

print("syndrome checks passed:", checked_syn)
for key in sorted(k for k in summary if len(k) == 2):
    c = summary[key]
    print("C2 class %-4s sector %s: lambda counts %s  -> eta_f = %s"
          % (key[0], key[1], dict(c), sorted({-l for l in c})))
# per-element breakdown (conjugate elements must agree)
for cls, Ms in [("axis", axisC2), ("edge", edgeC2)]:
    for M in Ms:
        vals = set()
        for key, c in summary.items():
            if len(key) == 4 and key[2] == M:
                vals |= set(c)
        print("  %s C2 %s: lambda values %s" % (cls, M, sorted(vals)))
print("time %.1fs" % (time.time() - t0))
