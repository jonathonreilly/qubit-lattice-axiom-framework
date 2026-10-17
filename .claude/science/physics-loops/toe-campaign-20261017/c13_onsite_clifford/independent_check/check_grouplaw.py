"""C13 independent check, part (3): admissible sign choices and group law.

For a code rep of each orbit type (L=4, both uniform sectors):
 - enumerate all 4096 (eps, eps') for every rotation; record which preserve
   the signed group (exact, via Majorana content of each generator, with a
   direct cross-check on random sign choices);
 - choose lifts for a C4 and a C3 and generate the group of signed
   permutations of the 12 Majoranas; classify which choices give an action
   of O up to fermion parity (kernel within {1, -1}, -1 = flip all 12).
"""
import itertools, json, random
from collections import Counter
import numpy as np
from model import HalfEdge, ROTS, rot_dir, classify_rotation
from paulialg import apply_clifford, mul, bits, SignedGroup

random.seed(2)
info = json.load(open("codes.json"))["info"]
REPS = {sz: next(x for x in info if x["orbit_size"] == sz) for sz in (4, 6, 12)}
SECTORS = [(0, 0, 0), (1, 1, 1)]
out = {}


def local_majoranas(H, s):
    return [H.mu(s, d) for d in range(6)] + [H.nu(s, d) for d in range(6)]


def content(H, P):
    """Set of (site, majorana index 0..11) in P, by GF(2) decomposition per site."""
    res = []
    sites = set(q // 6 for q in bits(P[0] | P[1]))
    for s in sites:
        ms = local_majoranas(H, s)
        target = (P[0] >> (6 * s) & 63, P[1] >> (6 * s) & 63)
        vecs = [(m[0] >> (6 * s) & 63, m[1] >> (6 * s) & 63) for m in ms]
        found = None
        for T in range(1 << 12):
            x = z = 0
            for i in range(12):
                if T >> i & 1:
                    x ^= vecs[i][0]; z ^= vecs[i][1]
            if (x, z) == target:
                found = T; break
        assert found is not None
        res += [(s, i) for i in range(12) if found >> i & 1]
    return res


admissible_by = {}
for sz, rep in REPS.items():
    o = tuple(rep["rep"])
    H = HalfEdge(4, o)
    for sec in SECTORS:
        G = H.group(sec)
        gens = [g for _, _, g in H.generators(sec, sites=[0])]
        cont = [Counter(i for _, i in content(H, g)) for g in gens]
        per_R = []
        for j, M in enumerate(ROTS):
            base = [G.status(apply_clifford(g, *H.majorana_images(M))) for g in gens]
            assert all(b == "in" for b in base)
            adm = []
            for T in range(1 << 12):
                e = [(-1) ** (T >> i & 1) for i in range(12)]
                ok = True
                for cc in cont:
                    sgn = 1
                    for i, mlt in cc.items():
                        if mlt % 2:
                            sgn *= e[i]
                    if sgn < 0:
                        ok = False; break
                if ok:
                    adm.append(T)
            # direct cross-check on 6 random choices
            for _ in range(6):
                T = random.randrange(1 << 12)
                e = [(-1) ** (T >> i & 1) for i in range(12)]
                imgs = H.majorana_images(M, e[:6], e[6:])
                direct = all(G.status(apply_clifford(g, *imgs)) == "in" for g in gens)
                assert direct == (T in set(adm)), (sz, sec, j, T)
            per_R.append(frozenset(adm))
        sizes = Counter(len(a) for a in per_R)
        same = len(set(per_R)) == 1
        # predicted rule: (eps eps')_{+a} == (eps eps')_{-a} for each axis a
        pred = frozenset(T for T in range(1 << 12)
                         if all(((T >> a) ^ (T >> (a + 6)) ^ (T >> (a + 3)) ^ (T >> (a + 9))) & 1 == 0
                                for a in range(3)))
        print(f"orbit{sz} sector{sec}: admissible counts per rotation {dict(sizes)}; "
              f"same set for all R: {same}; equals rule (ee')_+a=(ee')_-a: {per_R[0] == pred}", flush=True)
        out[f"orb{sz}_sec{sec}"] = dict(counts=dict(sizes), same=same, rule=per_R[0] == pred)
        admissible_by[(sz, sec)] = per_R

# ---------------------------------------------------------------- group law
# signed permutation of 12 Majoranas: (perm p[i], sign bitmask T): m_i -> (-1)^{T_i} m_{p[i]}
perm_of = []
for M in ROTS:
    pd = [rot_dir(M, d) for d in range(6)]
    perm_of.append(tuple(pd + [6 + x for x in pd]))


def compose(a, b):
    """b after a: m_i -> s_a(i) m_{pa(i)} -> s_a(i) s_b(pa(i)) m_{pb(pa(i))}"""
    pa, Ta = a
    pb, Tb = b
    p = tuple(pb[pa[i]] for i in range(12))
    T = 0
    for i in range(12):
        if ((Ta >> i) ^ (Tb >> pa[i])) & 1:
            T |= 1 << i
    return (p, T)


IDP = tuple(range(12))
MINUS = (IDP, (1 << 12) - 1)


def closure(gens, cap=48):
    elems = {(IDP, 0)}
    frontier = [(IDP, 0)]
    while frontier:
        nf = []
        for e in frontier:
            for g in gens:
                h = compose(e, g)
                if h not in elems:
                    elems.add(h)
                    nf.append(h)
                    if len(elems) > cap:
                        return None
        frontier = nf
    return elems


kinds = [classify_rotation(M) for M in ROTS]
jC4 = next(j for j, M in enumerate(ROTS) if kinds[j] == "C4" and M[2, 2] == 1)
jC3 = next(j for j, M in enumerate(ROTS) if kinds[j] == "C3" and np.array_equal(M @ np.array([1, 1, 1]), np.array([1, 1, 1])))
for key, per_R in admissible_by.items():
    A4, A3 = sorted(per_R[jC4]), sorted(per_R[jC3])
    tally = Counter()
    squares = Counter()
    for T4 in A4:
        for T3 in A3:
            Gp = closure([(perm_of[jC4], T4), (perm_of[jC3], T3)])
            if Gp is None:
                tally["order>48"] += 1
                continue
            ker = [e for e in Gp if e[0] == IDP]
            kerset = set(ker)
            if len(Gp) == 24 and len(ker) == 1:
                tally["24 honest"] += 1
            elif len(Gp) == 48 and kerset == {(IDP, 0), MINUS}:
                tally["48 with -1 (fermion parity)"] += 1
            else:
                tally[f"{len(Gp)} other kernel"] += 1
                continue
            # squares of C2 lifts
            for e in Gp:
                if e[0] == IDP:
                    continue
                j = perm_of.index(e[0])
                if kinds[j].startswith("C2"):
                    sq = compose(e, e)
                    squares[(len(Gp), kinds[j], "+1" if sq == (IDP, 0) else ("-1" if sq == MINUS else "other"))] += 1
    print(f"{key}: lift choices (C4 x C3) = {len(A4)} x {len(A3)}: {dict(tally)}", flush=True)
    print(f"   C2-lift squares in consistent groups: {dict(squares)}", flush=True)
    out[f"grouplaw_{key}"] = dict(tally=dict(tally), squares={str(k): v for k, v in squares.items()})
    # only need to do one code-sector for the full enumeration if the admissible sets agree
json.dump(out, open("check_grouplaw_results.json", "w"), indent=1)
