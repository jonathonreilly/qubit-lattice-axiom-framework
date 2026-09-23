#!/usr/bin/env python3
"""Relational cycle letters record their octant under the rotation-covariant static rule.

The Admissibility axiom asks for one fixed nearest-neighbour rule, covariant
under lattice translations and proper cubic rotations. The static cycle rule
of open PR #8752 fixes back neighbours x - e_i and forward neighbours
x + e_i, a supplied octant, so it is not rotation covariant. Its covariant
form lets each site read each lattice line in either orientation. On each
line, the two differences must have one raw sense and one cycle, with phases
one step apart in either direction; the three lines use the three cycles.

This runner uses the letters of open PR #8752: m = 211, cycles
(19, 31, 132, 29), (108, 43, 194, 77), (88, 39, 126, 169). Checks:

A. The letters decode every difference, and each cycle sums to 0.
B. Covariance: the covariant rule's 24576 stars are closed under all 48
   signed permutations of the axes; the fixed-octant rule's 768 stars are
   not closed under a quarter turn.
C. On the landed ice torus (side 4), the covariant rule's static records are
   exactly the 24576 oriented cycle spirals: each axis carries one cycle,
   one raw sense, one orientation and one phase.
D. Readouts: each site reads the frame, the orientation of each axis and its
   parity vector; all are global, and all 8 octants occur. So the records
   carry their own octant and the role pattern.
E. (U) under the covariant rule: no two allowed stars share their six
   neighbours, and on sampled records the rule admits one value per site.
F. The fixed-octant rule's records (open PR #8752) are the covariant
   records with every axis forward and one common sense: 768 of 24576.
G. Contrast: on the side-2 box the covariant rule leaves each boundary step
   free, so the box has far more records than oriented spirals.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
import time

PASS = FAIL = 0
T0 = time.time()
NODES = [0]
NODE_CAP = 5_700_000


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))


M, CYC = 211, ((19, 31, 132, 29), (108, 43, 194, 77), (88, 39, 126, 169))


def table(m, cyc):
    tab = {}
    for j, c in enumerate(cyc):
        for k, g in enumerate(c):
            for s in (1, -1):
                r = (s * g) % m
                if r == 0 or r in tab:
                    return None
                tab[r] = (s, j, k)
    return tab


TAB = table(M, CYC)


def site_ok(Bd, Fd, rule="covariant"):
    """Bd, Fd: decoded (raw sense, cycle, phase) per lattice axis, or None where unknown.
    covariant: per line one raw sense, one cycle, phases one step apart either way; distinct cycles.
    fixed: the rule of open PR #8752 with the supplied octant: one common sense, phase steps +1."""
    js, senses = [], set()
    steps = (1, 3) if rule == "covariant" else (1,)
    for i in range(3):
        b, f = Bd[i], Fd[i]
        if rule == "fixed":
            if b:
                senses.add(b[0])
            if f:
                senses.add(f[0])
        elif b and f and b[0] != f[0]:
            return False
        if b and f and (b[1] != f[1] or (f[2] - b[2]) % 4 not in steps):
            return False
        d = b or f
        if d:
            js.append(d[1])
    return len(senses) <= 1 and len(js) == len(set(js))


def stars(rule, m=M, cyc=CYC):
    out = set()
    steps = (1, -1) if rule == "covariant" else (1,)
    senses = list(itertools.product((1, -1), repeat=3)) if rule == "covariant" else [(1, 1, 1), (-1, -1, -1)]
    for sig in itertools.permutations(range(3)):
        for sens in senses:
            for k in itertools.product(range(4), repeat=3):
                for dirs in itertools.product(steps, repeat=3):
                    out.add((tuple((sens[i] * cyc[sig[i]][k[i]]) % m for i in range(3)),
                             tuple((sens[i] * cyc[sig[i]][(k[i] + dirs[i]) % 4]) % m for i in range(3))))
    return out


def act(g, star):
    """signed permutation g = (perm, signs): new axis i is old axis perm[i], reversed when signs[i] = -1."""
    perm, signs = g
    B, F = star
    nb_, nf_ = [], []
    for i in range(3):
        b, f = B[perm[i]], F[perm[i]]
        if signs[i] == 1:
            nb_.append(b)
            nf_.append(f)
        else:
            nb_.append((-f) % M)
            nf_.append((-b) % M)
    return tuple(nb_), tuple(nf_)


def parity(perm):
    return sum(1 for a in range(3) for b in range(a + 1, 3) if perm[a] > perm[b]) % 2


def search(sites, core, nb, dist, fixed, cap, rule="covariant"):
    coreset = set(core)
    val = dict(fixed)
    order = sorted((x for x in sites if x not in val), key=lambda x: (x not in coreset, dist(x), x))
    touching = {x: [] for x in sites}
    for y in core:
        for i in range(3):
            for sg in (1, -1):
                touching[nb(y, i, sg)].append((y, i, sg))
    recs = []

    def decode(y):
        Bd, Fd = [None] * 3, [None] * 3
        for i in range(3):
            zb, zf = nb(y, i, -1), nb(y, i, 1)
            if zb in val:
                Bd[i] = TAB.get((val[y] - val[zb]) % M)
                if Bd[i] is None:
                    return None
            if zf in val:
                Fd[i] = TAB.get((val[zf] - val[y]) % M)
                if Fd[i] is None:
                    return None
        return Bd, Fd

    def star_ok(y):
        d = decode(y)
        return d is not None and site_ok(d[0], d[1], rule)

    def allowed(y, i, sg):
        d = decode(y)
        if d is None:
            return set()
        out = set()
        for r, dec in TAB.items():
            B2, F2 = list(d[0]), list(d[1])
            if sg == 1:
                F2[i] = dec
            else:
                B2[i] = dec
            if site_ok(B2, F2, rule):
                out.add((val[y] + sg * r) % M)
        return out

    def rec(k):
        if len(recs) >= cap or NODES[0] >= NODE_CAP:
            return
        NODES[0] += 1
        if k == len(order):
            recs.append(dict(val))
            return
        z = order[k]
        cands = None
        for (y, i, sg) in touching[z]:
            if y in val:
                c = allowed(y, i, sg)
                cands = c if cands is None else cands & c
                if not cands:
                    return
        for v in sorted(cands if cands is not None else range(M)):
            val[z] = v
            if (z not in coreset or star_ok(z)) and all(
                    star_ok(y) for (y, i, sg) in touching[z] if y in val and y != z):
                rec(k + 1)
            del val[z]

    rec(0)
    return recs


def torus(L):
    sites = list(itertools.product(range(L), repeat=3))
    nb = lambda y, i, sg: tuple((u + sg * (k == i)) % L for k, u in enumerate(y))
    return sites, sites, nb, (lambda x: sum(min(u, L - u) for u in x))


def box(c):
    n = c + 2
    core = list(itertools.product(range(1, c + 1), repeat=3))
    sites = [x for x in itertools.product(range(n), repeat=3) if sum(u in (0, n - 1) for u in x) <= 1]
    nb = lambda y, i, sg: tuple(u + sg * (k == i) for k, u in enumerate(y))
    return sites, core, nb, (lambda x: sum(abs(u - 1) for u in x))


def oriented_spirals(sites):
    """axis i carries cycle perm[i], raw sense sens[i], orientation ori[i] and phase ph[i]; value 0 at the origin."""
    out = {}
    for perm in itertools.permutations(range(3)):
        for sens in itertools.product((1, -1), repeat=3):
            for ori in itertools.product((1, -1), repeat=3):
                for ph in itertools.product(range(4), repeat=3):
                    rec = []
                    for x in sites:
                        v = 0
                        for i in range(3):
                            c = CYC[perm[i]]
                            for u in range(x[i]):
                                v += sens[i] * c[(ph[i] + u) % 4] if ori[i] == 1 else -sens[i] * c[(ph[i] - u - 1) % 4]
                        rec.append(v % M)
                    out[tuple(rec)] = (perm, sens, ori, ph)
    return out


print("== A. The letters ==")
check("the letters of open PR #8752 decode every difference, and each cycle sums to 0 mod 211",
      TAB is not None and len(TAB) == 24 and all(sum(c) % M == 0 for c in CYC))
print()

print("== B. Covariance ==")
SC, SF = stars("covariant"), stars("fixed")
G48 = [(p, s) for p in itertools.permutations(range(3)) for s in itertools.product((1, -1), repeat=3)]
proper = [(p, s) for (p, s) in G48 if (parity(p) + sum(1 for e in s if e == -1)) % 2 == 0]
closed_cov = all(act(g, st) in SC for g in G48 for st in SC)
quarter = ((1, 0, 2), (1, -1, 1))
open_fixed = any(act(quarter, st) not in SF for st in SF)
check("the covariant rule's stars are closed under all 48 signed axis permutations; the fixed-octant rule's are not closed under a quarter turn",
      len(SC) == 24576 and len(SF) == 768 and len(proper) == 24 and quarter in proper and closed_cov and open_fixed,
      "24576 covariant stars, 768 fixed-octant stars")
print()

print("== C. The landed ice torus (side 4) ==")
S4, C4, N4, D4 = torus(4)
R4 = search(S4, C4, N4, D4, {(0, 0, 0): 0}, 60000)
OSP = oriented_spirals(S4)
got = {tuple(r[x] for x in S4) for r in R4}
check("the covariant rule's static records are exactly the 24576 oriented cycle spirals",
      len(R4) == 24576 and got == set(OSP), "6 frames x 8 raw senses x 8 orientations x 64 phases")
print()

print("== D. Readouts ==")
frame_ok = ori_ok = par_ok = True
octants = set()
for r in R4:
    frames, oris, pars = set(), set(), set()
    for x in S4:
        B = [TAB[(r[x] - r[N4(x, i, -1)]) % M] for i in range(3)]
        F = [TAB[(r[N4(x, i, 1)] - r[x]) % M] for i in range(3)]
        frames.add(tuple(F[i][1] for i in range(3)))
        oris.add(tuple(1 if (F[i][2] - B[i][2]) % 4 == 1 else -1 for i in range(3)))
        pars.add(tuple((F[i][2] - x[i]) % 2 for i in range(3)))
    frame_ok &= len(frames) == 1
    ori_ok &= len(oris) == 1
    par_ok &= len(pars) == 1
    octants |= oris
check("every site reads the same frame and the same orientation of each axis, and all 8 octants occur",
      frame_ok and ori_ok and len(octants) == 8, "the records carry their own octant")
check("every site reads its parity vector x mod 2 up to one global phase: the role pattern", par_ok)
print()

print("== E. Nearest-neighbour form ==")
def shared_stars(st, m):
    return sum(1 for B, F in st for d in range(1, m) if (tuple((b + d) % m for b in B), tuple((f - d) % m for f in F)) in st)


shared = shared_stars(SC, M)
C0 = ((34, 13, 35, 29), (11, 4, 23, 36), (20, 15, 18, 21))
n0 = shared_stars(stars("covariant", 37, C0), 37)
uniq = True
for r in R4[::512]:
    for x in S4:
        n_ok = 0
        for v in range(M):
            Bd = [TAB.get((v - r[N4(x, i, -1)]) % M) for i in range(3)]
            Fd = [TAB.get((r[N4(x, i, 1)] - v) % M) for i in range(3)]
            n_ok += None not in Bd and None not in Fd and site_ok(Bd, Fd)
        uniq &= n_ok == 1
check("(U) under the covariant rule: no two allowed stars share their six neighbours; the rule admits one value per site",
      shared == 0 and uniq and n0 == 864, f"48 sampled records x 64 sites x 211 values; positive control mod 37: {n0} shared stars")
print()

print("== F. The fixed-octant records ==")
fixed_like = {rec for rec, (perm, sens, ori, ph) in OSP.items() if ori == (1, 1, 1) and len(set(sens)) == 1}
RF = search(S4, C4, N4, D4, {(0, 0, 0): 0}, 5000, rule="fixed")
check("the fixed-octant rule's records are the covariant records with every axis forward and one common sense",
      len(RF) == 768 and {tuple(r[x] for x in S4) for r in RF} == fixed_like, "768 of 24576")
print()

print("== G. Contrast: an open box ==")
SB, CB, NB, DB = box(2)
RB = search(SB, CB, NB, DB, {(1, 1, 1): 0}, 100000)
check("on the side-2 box each boundary step may go either way, so the covariant rule has more than 100000 records",
      len(RB) == 100000, "the octant is recorded where the lines close, as on the torus")
print()
check("budget: every search stayed under its node cap", NODES[0] < NODE_CAP, f"{NODES[0]} nodes, {time.time() - T0:.0f} s")
print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
