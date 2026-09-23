#!/usr/bin/env python3
"""Registered frames: an unsoldered rule whose letters carry coordinate
labels modulo 4 makes the finished record carry the lattice frame.  In a
sweep the stationary records are exactly the frames aligned with the sweep;
at a first formation the frame costs a sharp price that depends on the
order; a record with a frame carries the ice support and the parity-role
skeleton and emulates a soldered rule.  Exact and finite.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.  Exact rational arithmetic; no floating point.

Declared objects
  * formation reading with the text's hole semantics, unsoldered reading:
    a rule sees its formed neighbours' values and their relative geometry,
    never their absolute directions (invariance under the 24 rotations
    acting on positions with values fixed);
  * coordinate letters (c, t): c in Z_4^K, t a tag.  A record carries a
    frame when c(x) = c0 + sigma(x) mod 4 for a map sigma sending the
    three lattice directions to generators of three different axes;
  * the corner rule (tags N, axis i, B) and the designed rule (tags N, T12,
    T23, Z, S12, S23, S31, A, B) defined below;
  * orders: corner growth from the corner of a box (every site after its
    back-neighbours and before its forward neighbours), broadcast from a
    centre, a designed order, and the sweep on the torus Z_4^3 read as a
    stationary condition (each site equals the rule's output on its three
    sweep back-neighbours);
  * the superlattice roles (parity vectors) and the soldered ice
    vertex-record rule of open PR 8667 on the star of one vertex.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
from fractions import Fraction as Fr
from itertools import combinations, permutations, product

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


H = "unrecorded"
DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


SIGNED = [tuple(tuple(s[i] if j == p[i] else 0 for j in range(3)) for i in range(3))
          for p in permutations(range(3)) for s in product((1, -1), repeat=3)]
ROT = [g for g in SIGNED if det3(g) == 1]


def act(g, v):
    return tuple(sum(g[i][j] * v[j] for j in range(3)) for i in range(3))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def vadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def u(K, i):
    return tuple(1 if j == i else 0 for j in range(K))


def ladd(a, b):
    return tuple((x + y) % 4 for x, y in zip(a, b))


def lsub(a, b):
    return tuple((x - y) % 4 for x, y in zip(a, b))


def lneg(a):
    return tuple((-x) % 4 for x in a)


def positive_completion(K, labels):
    """The unique c with c - L_m distinct positive generators, else None."""
    if not labels:
        return None
    cands = set()
    for a in permutations(range(K), len(labels)):
        c = ladd(labels[0], u(K, a[0]))
        if all(lsub(c, L) == u(K, a[m]) for m, L in enumerate(labels)):
            cands.add(c)
    return next(iter(cands)) if len(cands) == 1 else None


def perpendicular(config):
    return all(dot(a, b) == 0 for a, b in combinations(config, 2))


def corner_rule(K, signed=False):
    first = [u(K, i) for i in range(K)] + ([lneg(u(K, i)) for i in range(K)] if signed else [])

    def R(config):
        vals = list(config.values())
        n = len(vals)
        if n == 0:
            return {((0,) * K, "N"): Fr(1)}
        if n == 1:
            c, t = vals[0]
            if t == "N":
                return {(g, g.index(1) if 1 in g else ("-", g.index(3))): Fr(1, len(first)) for g in first}
            if isinstance(t, int):
                return {(ladd(c, u(K, t)), t): Fr(1)}
            return {}
        if n in (2, 3) and perpendicular(config):
            c = positive_completion(K, [v[0] for v in vals])
            return {(c, "B"): Fr(1)} if c is not None else {}
        return {}
    return R


def form(order, rule, site_aware=False, seen=None, keep_holes=True):
    idx = {s: k for k, s in enumerate(order)}
    nbrs = [[(d, idx[vadd(s, d)]) for d in DIRS if vadd(s, d) in idx and idx[vadd(s, d)] < k]
            for k, s in enumerate(order)]
    layer = {(): Fr(1)}
    for k, s in enumerate(order):
        nxt = {}
        for part, mass in layer.items():
            config = {d: part[j] for d, j in nbrs[k] if part[j] != H}
            if seen is not None:
                seen.add(tuple(sorted(config.items(), key=repr)))
            probs = rule(config, s) if site_aware else rule(config)
            tot = Fr(0)
            for v, p in probs.items():
                key = part + (v,)
                nxt[key] = nxt.get(key, Fr(0)) + mass * p
                tot += p
            if tot < 1 and keep_holes:
                key = part + (H,)
                nxt[key] = nxt.get(key, Fr(0)) + mass * (1 - tot)
        layer = nxt
    return layer


def box(Lx, Ly, Lz):
    return [(x, y, z) for x in range(Lx) for y in range(Ly) for z in range(Lz)]


def lex_x(sites):
    return sorted(sites, key=lambda s: (s[2], s[1], s[0]))


def frame_of(order, state, K):
    """sigma(e_i) if the record is c0 + sigma(x) with generators of distinct axes."""
    if H in state:
        return None
    lab = {s: v[0] for s, v in zip(order, state)}
    c0 = lab[(0, 0, 0)]
    img = [lsub(lab[e], c0) for e in E3]
    axis = [next((a for a in range(K) if g in (u(K, a), lneg(u(K, a)))), None) for g in img]
    if None in axis or len(set(axis)) != 3:
        return None
    for s, c in lab.items():
        pred = c0
        for i in range(3):
            for _ in range(s[i]):
                pred = ladd(pred, img[i])
        if c != pred:
            return None
    return tuple(img)


def covariant(rule, configs):
    for cfg in configs:
        config = dict(cfg)
        base = rule(config)
        for g in ROT:
            if rule({act(g, d): v for d, v in config.items()}) != base:
                return False
    return True


# ---------- A. sweeps: stationary records are the aligned frames ----------
print("A. sweeps with no first formation")
plaq = all((ladd(u(3, a), u(3, b)) == ladd(u(3, c), u(3, d))) == (sorted((a, b)) == sorted((c, d)))
           for a, b, c, d in product(range(3), repeat=4))
check("plaquette lemma: u_a+u_b = u_c+u_d mod 4 iff {a,b} = {c,d}", plaq, "81 cases")
fs = list(product(range(3), repeat=3))
good = [(f1, f2, f3) for f1 in fs for f2 in fs for f3 in fs
        if all(len({f1[x], f2[y], f3[z]}) == 3 for x in range(3) for y in range(3) for z in range(3))]
check("frame lemma: (f1(a), f2(b), f3(c)) a permutation for all a, b, c forces every f_i constant",
      len(good) == 6 and all(len(set(f)) == 1 for g in good for f in g), f"{len(fs) ** 3} triples on Z_3")
L4 = 4
tsites = [(x, y, z) for z in range(L4) for y in range(L4) for x in range(L4)]
tback = {s: [((s[0] - 1) % L4, s[1], s[2]), (s[0], (s[1] - 1) % L4, s[2]), (s[0], s[1], (s[2] - 1) % L4)]
         for s in tsites}
sols, leaves = [], [0]


def torus_search(i, lab):
    if i == len(tsites):
        leaves[0] += 1
        if all(positive_completion(3, [lab[b] for b in tback[s]]) == lab[s] for s in tsites):
            sols.append(dict(lab))
        return
    s = tsites[i]
    known = [lab[b] for b in tback[s] if b in lab]
    if i == 0:
        cands = [(0, 0, 0)]
    elif len(known) == 1:
        cands = [ladd(known[0], u(3, a)) for a in range(3)]
    else:
        c = positive_completion(3, known)
        cands = [] if c is None else [c]
    for c in cands:
        lab[s] = c
        torus_search(i + 1, lab)
        del lab[s]


torus_search(0, {})
aligned = {tuple(lab[e] for e in E3) for lab in sols}
is_affine = all(lab[s] == ladd(ladd(tuple((s[0] * x) % 4 for x in lab[E3[0]]),
                                    tuple((s[1] * x) % 4 for x in lab[E3[1]])),
                               tuple((s[2] * x) % 4 for x in lab[E3[2]])) for lab in sols for s in tsites)
check("torus Z_4^3 sweep: stationary hole-free records with c(0)=0 are exactly 6",
      len(sols) == 6 and len(aligned) == 6 and is_affine
      and aligned == {tuple(u(3, p[i]) for i in range(3)) for p in permutations(range(3))},
      f"{leaves[0]} complete candidates searched; all affine, sigma(e_i) = u_pi(i)")


def ice_ok(lab, vertices, nb):
    def occ(c):
        odd = [x for x in c if x % 2]
        return 1 if len(odd) == 1 and odd[0] == 1 else 0
    return all(sum(occ(lab[t]) for t in nb(v)) == 3 for v in vertices)


def roles_ok(lab, phase=(0, 0, 0)):
    return all(sum(x % 2 for x in c) == sum((a + p) % 2 for a, p in zip(s, phase)) for s, c in lab.items())


tor_nb = lambda v: [tuple((a + b) % L4 for a, b in zip(v, d)) for d in DIRS]
tverts = [s for s in tsites if all(x % 2 == 0 for x in s)]
check("sweep records carry ice (label rule) at all 8 torus vertices and the role letters at all 64 sites",
      all(ice_ok(lab, tverts, tor_nb) and roles_ok(lab) for lab in sols),
      "link occupied iff its odd label coordinate is 1")

# ---------- B. corner growth: the sharp price ----------
print("B. corner growth from a first formation")
cfgs = set()
laws = {}
for dims in [(2, 2, 2), (3, 3, 3), (6, 3, 2), (4, 4, 4)]:
    order = lex_x(box(*dims))
    law = form(order, corner_rule(3), seen=cfgs)
    fr = {}
    for st, m in law.items():
        f = frame_of(order, st, 3)
        if f is not None:
            fr[f] = fr.get(f, Fr(0)) + m
    hole_free = sum(m for st, m in law.items() if H not in st)
    laws[dims] = (hole_free, sum(fr.values()), len(fr), set(fr.values()), len(law))
ok = all(v[0] == v[1] == Fr(2, 9) and v[2] == 6 and v[3] == {Fr(1, 27)} for v in laws.values())
check("K=3: P(hole-free) = P(frame) = 2/9 on boxes 2x2x2, 3x3x3, 6x3x2, 4x4x4",
      ok, f"6 frames of mass 1/27 each; finished states {[v[4] for v in laws.values()]}")


def law_by_site(order, law):
    out = {}
    for st, m in law.items():
        key = tuple(sorted(zip(order, st), key=repr))
        out[key] = out.get(key, Fr(0)) + m
    return out


sites = box(3, 3, 2)
orders = [lex_x(sites), sorted(sites, key=lambda s: (s[0], s[1], s[2])), sorted(sites, key=lambda s: (sum(s), s))]
lb = [law_by_site(o, form(o, corner_rule(3))) for o in orders]
check("the finished law is the same for three corner-growth orders (x-fastest, z-fastest, diagonal)",
      lb[0] == lb[1] == lb[2], f"{len(lb[0])} finished states on 3x3x2")
p4 = []
for dims in [(2, 2, 2), (3, 3, 2)]:
    order = lex_x(box(*dims))
    law = form(order, corner_rule(4), seen=None)
    p4.append(sum(m for st, m in law.items() if frame_of(order, st, 4) is not None))
check("K=4 axes: P(frame) = 3/8 = (K-1)(K-2)/K^2", p4 == [Fr(3, 8)] * 2, f"{p4}")
first = []
for o in orders:
    idx = {s: k for k, s in enumerate(o)}
    first.append(sorted(s for s in o if s != (0, 0, 0) and
                        [t for t in (vadd(s, d) for d in DIRS) if t in idx and idx[t] < idx[s]] == [(0, 0, 0)]))
rot_maps = all(any(act(g, (-1, 0, 0)) == d for g in ROT) for d in [(0, -1, 0), (0, 0, -1)])
check("in corner growth the sites seeing only the corner are exactly its 3 forward neighbours, related by rotations",
      all(f == sorted(E3) for f in first) and rot_maps, "so their values are i.i.d. given the corner")


def rng(seed):
    x = seed
    while True:
        x = (1103515245 * x + 12345) % 2147483648
        yield x


gen = rng(8672)
samples = []
for m in (3, 4, 5, 6, 8):
    for _ in range(40):
        w = [1 + next(gen) % 97 for _ in range(m)]
        samples.append([Fr(x, sum(w)) for x in w])
    samples.append([Fr(1, m)] * m)


def e3(p):
    return sum(p[a] * p[b] * p[c] for a, b, c in combinations(range(len(p)), 3))


mac = all(6 * e3(p) <= Fr((len(p) - 1) * (len(p) - 2), len(p) ** 2) for p in samples)
eq = all(6 * e3([Fr(1, m)] * m) == Fr((m - 1) * (m - 2), m * m) for m in (3, 4, 5, 6, 8))
brute = []
for q6 in samples[123:126]:
    tot = sum(q6[a] * q6[b] * q6[c] for a, b, c in product(range(6), repeat=3) if len({a % 3, b % 3, c % 3}) == 3)
    q = [q6[i] + q6[i + 3] for i in range(3)]
    brute.append(tot == 6 * q[0] * q[1] * q[2])
check("price bound: P(3 i.i.d. first-shell values pairwise distinct) = 6 e3(p) <= (m-1)(m-2)/m^2",
      mac and eq and all(brute), f"{len(samples)} rational laws, equality at uniform; distinct axes = 6 q1 q2 q3 <= 2/9")

# ---------- C. broadcast from a centre ----------
print("C. broadcast from a centre")
star = [(0, 0, 0)] + DIRS
law = form(star, corner_rule(3, signed=True))
lab_frame = Fr(0)
for st, m in law.items():
    if H in st:
        continue
    img = {d: v[0] for d, v in zip(DIRS, st[1:])}
    gens = set(img.values())
    if len(gens) == 6 and all(img[(-d[0], -d[1], -d[2])] == lneg(img[d]) for d in DIRS):
        lab_frame += m
pbar = [Fr(3, 21), Fr(2, 21), Fr(4, 21), Fr(5, 21), Fr(1, 21), Fr(6, 21)]
gens6 = list(range(6))
opp = {0: 3, 1: 4, 2: 5, 3: 0, 4: 1, 5: 2}
tot = sum(pbar[a[0]] * pbar[a[1]] * pbar[a[2]] * pbar[a[3]] * pbar[a[4]] * pbar[a[5]]
          for a in product(gens6, repeat=6)
          if len(set(a)) == 6 and all(a[2 * i + 1] == opp[a[2 * i]] for i in range(3)))
prod6 = pbar[0] * pbar[1] * pbar[2] * pbar[3] * pbar[4] * pbar[5]
check("broadcast: P(frame at the centre) = 48 prod(p) <= 48/6^6 = 1/972",
      lab_frame == Fr(1, 972) and tot == 48 * prod6 and tot < Fr(1, 972),
      f"uniform exact {lab_frame}; skewed law {tot}")

# ---------- D. a designed order pays nothing ----------
print("D. a designed order")
U3 = [u(3, i) for i in range(3)]
RAIL = {"S12": (0, 1), "S23": (1, 2), "S31": (2, 0)}


def designed_rule(config):
    vals = list(config.values())
    n = len(vals)
    if n == 0:
        return {((0, 0, 0), "N"): Fr(1)}
    if n == 1:
        c, t = vals[0]
        if t == "N":
            return {(U3[0], "T12"): Fr(1)}
        if t == "T12":
            return {(ladd(c, U3[1]), "S12"): Fr(1)}
        if t == "T23":
            return {(ladd(c, U3[2]), "S23"): Fr(1)}
        if t in RAIL:
            return {(ladd(c, U3[RAIL[t][0]]), t): Fr(1)}
        return {}
    if n == 2 and perpendicular(config):
        pairs = [(vals[0], vals[1]), (vals[1], vals[0])]
        outs = {(lsub(cb, U3[RAIL[tb][0]]), {"S12": "T23", "S23": "Z"}.get(tb, "B"))
                for (ca, ta), (cb, tb) in pairs if ta == "N" and tb in RAIL}
        if not outs and {vals[0][1], vals[1][1]} == {"T12", "Z"}:
            c = positive_completion(3, [vals[0][0], vals[1][0]])
            outs = {(c, "S31")} if c is not None else set()
        if not outs:
            outs = {(lsub(cb, U3[RAIL[tb][1]]), "A") for (ca, ta), (cb, tb) in pairs
                    if tb in RAIL and ca == lsub(lsub(cb, U3[RAIL[tb][0]]), U3[RAIL[tb][1]])}
        if not outs:
            c = positive_completion(3, [vals[0][0], vals[1][0]])
            outs = {(c, "B")} if c is not None else set()
        return {outs.pop(): Fr(1)} if len(outs) == 1 else {}
    if n == 3 and perpendicular(config):
        c = positive_completion(3, [v[0] for v in vals])
        return {(c, "B"): Fr(1)} if c is not None else {}
    return {}


def designed_order(Lx, Ly, Lz):
    seed = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1), (1, 1, 1)]
    lad = [s for k in range(2, Lx) for s in ((k, 1, 0), (k, 0, 0))]
    lad += [s for k in range(2, Ly) for s in ((0, k, 1), (0, k, 0))]
    lad += [s for k in range(2, Lz) for s in ((1, 0, k), (0, 0, k))]
    done = set(seed + lad)
    return seed + lad + [s for s in lex_x(box(Lx, Ly, Lz)) if s not in done]


dcfg = set()
dres = []
for dims in [(2, 2, 2), (3, 3, 3), (5, 3, 2), (4, 4, 4), (6, 5, 4)]:
    order = designed_order(*dims)
    law = form(order, designed_rule, seen=dcfg)
    only = list(law.items())
    dres.append(len(only) == 1 and only[0][1] == 1 and frame_of(order, only[0][0], 3) == tuple(U3))
idx = {s: k for k, s in enumerate(designed_order(3, 3, 3))}
shapes = [len([t for t in (vadd(e, d) for d in DIRS) if t in idx and idx[t] < idx[e]]) for e in E3]
check("designed order: the record is the frame sigma = identity with probability 1",
      all(dres), "boxes 2x2x2, 3x3x3, 5x3x2, 4x4x4, 6x5x4; the order fixes the frame")
check("designed order: the corner's forward neighbours see different configurations",
      shapes == [1, 2, 2], f"formed neighbours {shapes}; one lone child, two closings")
check("corner rule and designed rule are unsoldered: invariant under the 24 rotations on every arising configuration",
      covariant(corner_rule(3), cfgs) and covariant(designed_rule, dcfg), f"{len(cfgs)} + {len(dcfg)} configurations")

# ---------- E. what a record with a frame carries ----------
print("E. ice, roles and emulation")
order7 = lex_x(box(7, 7, 7))
law7 = form(order7, corner_rule(3), keep_holes=False)
ok7, occs = True, set()
verts7 = [s for s in order7 if all(x % 2 == 0 for x in s) and all(0 < x < 6 for x in s)]
for st, m in law7.items():
    if frame_of(order7, st, 3) is None:
        continue
    lab = {s: v[0] for s, v in zip(order7, st)}
    ok7 = ok7 and ice_ok(lab, verts7, lambda v: [vadd(v, d) for d in DIRS]) and roles_ok(lab)
    occs.add(tuple(1 if (lambda odd: len(odd) == 1 and odd[0] == 1)([x for x in lab[s] if x % 2]) else 0
                   for s in order7))
check("corner growth 7x7x7: every frame record has ice at the 8 interior vertices and correct role letters",
      ok7 and len(occs) == 1 and sum(law7.values()) == Fr(2, 9) and len(law7) == 6, "the carried ice configuration is the same for all 6 frames")


def role_of(w):
    return {3: "V", 2: "L", 1: "P", 0: "C"}[w]


ICE_D = [frozenset(S) for S in combinations(DIRS, 3)]
GEN6 = U3 + [lneg(g) for g in U3]
ICE_G = [frozenset(S) for S in combinations(GEN6, 3)]


def reference_rule(config, s):
    role = role_of(sum(x % 2 for x in s))
    if role == "V":
        cons = [S for S in ICE_D if all((d in S) == (x == 1) for d, x in config.items())]
        return {S: Fr(1, len(cons)) for S in cons}
    if role == "L":
        told = {1 if (-d[0], -d[1], -d[2]) in x else 0 for d, x in config.items() if isinstance(x, frozenset)}
        if len(told) > 1:
            return {}
        return {told.pop(): Fr(1)} if told else {0: Fr(1, 2), 1: Fr(1, 2)}
    return {".": Fr(1)}


def emulator(config):
    out = {}
    for (c, t), p in corner_rule(3)({d: v[:2] for d, v in config.items()}).items():
        role = role_of(sum(x % 2 for x in c))
        if role == "V":
            links = [(lsub(v[0], c), v[2]) for v in config.values() if role_of(sum(x % 2 for x in v[0])) == "L"]
            cons = [S for S in ICE_G if all(g in GEN6 and (g in S) == (x == 1) for g, x in links)]
            for S in cons:
                out[(c, t, S)] = out.get((c, t, S), Fr(0)) + p / len(cons)
        elif role == "L":
            told = {1 if lsub(c, v[0]) in v[2] else 0 for v in config.values() if isinstance(v[2], frozenset)}
            if len(told) > 1:
                continue
            for x, q in (((told.pop(), Fr(1)),) if told else ((0, Fr(1, 2)), (1, Fr(1, 2)))):
                out[(c, t, x)] = out.get((c, t, x), Fr(0)) + p * q
        else:
            out[(c, t, ".")] = out.get((c, t, "."), Fr(0)) + p
    return out


order3 = lex_x(box(3, 3, 3))
V = (1, 1, 1)
ref = {}
for st, m in form(order3, reference_rule, site_aware=True).items():
    val = dict(zip(order3, st))
    key = (val[V], tuple(val[vadd(V, d)] for d in DIRS))
    ref[key] = ref.get(key, Fr(0)) + m
ecfg = set()
emu, psucc = {}, Fr(0)
for st, m in form(order3, emulator, seen=ecfg).items():
    f = frame_of(order3, st, 3)
    if f is None:
        continue
    psucc += m
    val = dict(zip(order3, st))
    sig = {d: lsub(val[vadd(V, d)][0], val[V][0]) for d in DIRS}
    S = frozenset(d for d in DIRS if sig[d] in val[V][2])
    key = (S, tuple(val[vadd(V, d)][2] for d in DIRS))
    emu.setdefault(f, {})
    emu[f][key] = emu[f].get(key, Fr(0)) + m * 27
by_m = {k: v for k, v in ref.items()}
expect = all(v == Fr(1, 8) / {0: 1, 1: 3, 2: 3, 3: 1}[sum(k[1][1::2])] for k, v in by_m.items())
check("soldered ice vertex-record rule on the star, corner growth: exact law (1/8)/C(3,3-m)",
      len(ref) == 20 and sum(ref.values()) == 1 and expect, "m = occupied back-links; 20 ice configurations, no defect")
check("emulator (coordinate letters, unsoldered): P(frame) = 2/9 and the pulled-back law equals the soldered law in each frame",
      psucc == Fr(2, 9) and len(emu) == 6 and all(v == ref for v in emu.values())
      and covariant(lambda c: emulator(c), ecfg), f"{len(ecfg)} configurations invariant under 24 rotations")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
