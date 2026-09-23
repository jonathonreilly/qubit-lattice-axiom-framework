#!/usr/bin/env python3
"""Strong cycle letters fix core frames and parity with possible folds.

Shared walks describe internal core links. Outer-face steps at distinct boundary sites can choose ±1 independently; their phase parity is nevertheless the opposite of the adjacent internal phase, so the same parity offset extends to each boundary readout. A canonical folded extension chooses shared outer steps, but not all extensions do. The theorem is for cubic cores and the stated compatible tori, not arbitrary window shapes. Orientation is not generally constant, and no physical role encoding is derived.

See the companion note for proofs and exact execution scope.
"""
import itertools
import sys

AUDIT_TIMEOUT_SEC = 900
import time

PASS = FAIL = 0
T0 = time.time()
NODES = [0]
NODE_CAP = 4_000_000


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))


STRONG = (100003, ((17612, 74607, 8272, 99515), (33433, 15456, 64938, 86179), (99741, 58916, 61899, 79453)))
WEAK = (211, ((19, 31, 132, 29), (108, 43, 194, 77), (88, 39, 126, 169)))
C37 = (37, ((34, 13, 35, 29), (11, 4, 23, 36), (20, 15, 18, 21)))


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


def bent_squares(m, cyc):
    """square a + b = c + e with a = F_i(y) (cycle A), c = F_j(y) (cycle B), b = F_j(y + e_i) (X != A),
    e = F_i(y + e_j) (Y != B), X != Y, any raw senses; straight means b = c and e = a."""
    bent = 0
    for A, B in itertools.permutations(range(3), 2):
        for X in range(3):
            for Y in range(3):
                if X == A or Y == B or X == Y:
                    continue
                for p, q, r, u in itertools.product(range(4), repeat=4):
                    for sa, sb, sc, se in itertools.product((1, -1), repeat=4):
                        if (sa * cyc[A][p] + sb * cyc[X][q] - sc * cyc[B][r] - se * cyc[Y][u]) % m == 0:
                            if not (X == B and Y == A and q == r and u == p and sb == sc and se == sa):
                                bent += 1
    return bent


def u_collisions(m, cyc):
    """covariant stars that share their six neighbours up to a shift of the centre fall in one class."""
    classes = {}
    for sig in itertools.permutations(range(3)):
        for sens in itertools.product((1, -1), repeat=3):
            for k in itertools.product(range(4), repeat=3):
                for dirs in itertools.product((1, -1), repeat=3):
                    B = tuple((sens[i] * cyc[sig[i]][k[i]]) % m for i in range(3))
                    F = tuple((sens[i] * cyc[sig[i]][(k[i] + dirs[i]) % 4]) % m for i in range(3))
                    key = ((B[1] - B[0]) % m, (B[2] - B[0]) % m) + tuple((F[i] + B[0]) % m for i in range(3))
                    classes.setdefault(key, set()).add((B, F))
    return sum(1 for v in classes.values() if len(v) > 1), len(classes)


def site_ok(Bd, Fd):
    js = []
    for i in range(3):
        b, f = Bd[i], Fd[i]
        if b and f and (b[0] != f[0] or b[1] != f[1] or (f[2] - b[2]) % 4 not in (1, 3)):
            return False
        d = b or f
        if d:
            js.append(d[1])
    return len(js) == len(set(js))


def nbr(y, i, sg):
    return tuple(u + sg * (k == i) for k, u in enumerate(y))


def core_records(m, cyc, c, cap=200000):
    """covariant records on the core of side c, one value fixed; faces are omitted, since a boundary line
    can always be completed by a face step of its sense and cycle, one phase away."""
    tab = table(m, cyc)
    core = list(itertools.product(range(1, c + 1), repeat=3))
    cs = set(core)
    order = sorted((x for x in core if x != (1, 1, 1)), key=lambda x: (sum(x), x))
    val, recs = {(1, 1, 1): 0}, []

    def star(y):
        Bd, Fd = [None] * 3, [None] * 3
        for i in range(3):
            zb, zf = nbr(y, i, -1), nbr(y, i, 1)
            if zb in val and zb in cs:
                Bd[i] = tab.get((val[y] - val[zb]) % m)
                if Bd[i] is None:
                    return False
            if zf in val and zf in cs:
                Fd[i] = tab.get((val[zf] - val[y]) % m)
                if Fd[i] is None:
                    return False
        return site_ok(Bd, Fd)

    def rec(k):
        if len(recs) >= cap or NODES[0] >= NODE_CAP:
            return
        NODES[0] += 1
        if k == len(order):
            recs.append(tuple(val[x] for x in core))
            return
        z = order[k]
        y = [nbr(z, i, -1) for i in range(3) if nbr(z, i, -1) in cs][0]
        for r in tab:
            val[z] = (val[y] + r) % m
            if star(z) and all(star(w) for w in (nbr(z, i, sg) for i in range(3) for sg in (1, -1)) if w in val and w in cs):
                rec(k + 1)
            del val[z]

    rec(0)
    return core, recs


def folded_on_core(m, cyc, c):
    """folded cycle spirals on the core of side c: per axis a cycle, a raw sense and a +-1 phase walk."""
    core = list(itertools.product(range(1, c + 1), repeat=3))
    walks = []
    for p0 in range(4):
        for dirs in itertools.product((1, -1), repeat=c - 2):
            w = [p0]
            for dd in dirs:
                w.append((w[-1] + dd) % 4)
            walks.append(w)
    out = set()
    for perm in itertools.permutations(range(3)):
        for sens in itertools.product((1, -1), repeat=3):
            for ws in itertools.product(walks, repeat=3):
                rec = []
                for x in core:
                    v = 0
                    for i in range(3):
                        v += sum(sens[i] * cyc[perm[i]][ws[i][u - 1]] for u in range(1, x[i]))
                    rec.append(v % m)
                out.add(tuple(rec))
    return out


def readouts(m, cyc, core, recs):
    tab = table(m, cyc)
    cs = set(core)
    bad_par = bad_frame = 0
    for r in recs:
        v = dict(zip(core, r))
        par, frame = set(), set()
        for x in core:
            for i in range(3):
                z = nbr(x, i, 1)
                if z in cs:
                    d = tab[(v[z] - v[x]) % m]
                    par.add((i, (d[2] - x[i]) % 2))
                    frame.add((i, d[1]))
        bad_par += any(len({p for (a, p) in par if a == i}) > 1 for i in range(3))
        bad_frame += any(len({p for (a, p) in frame if a == i}) > 1 for i in range(3))
    return bad_par, bad_frame


def closed_walks(m, c, L):
    """closed +-1 phase walks of length L with zero sum of the cycle's angles: (monotone, folded) counts."""
    mono = fold = 0
    for p0 in range(4):
        for dirs in itertools.product((1, -1), repeat=L):
            if sum(dirs) % 4:
                continue
            w, p = [], p0
            for dd in dirs:
                w.append(p)
                p = (p + dd) % 4
            if p != p0 or sum(c[k] for k in w) % m:
                continue
            if len(set(dirs)) == 1:
                mono += 1
            else:
                fold += 1
    return mono, fold


print("== A. The letters ==")
M, CYC = STRONG
TAB = table(M, CYC)
bs, bw = bent_squares(M, CYC), bent_squares(*WEAK)
uc, ncls = u_collisions(M, CYC)
uc37, _ = u_collisions(*C37)
check("m = 100003: the cycles decode and sum to 0; every square solution is straight for every sign pattern; (U) holds",
      TAB is not None and all(sum(c) % M == 0 for c in CYC) and bs == 0 and uc == 0 and ncls == 24576,
      "24576 covariant stars, one per neighbour class")
check("controls: the letters of open PR #8752 have bent mixed-sign squares, and a set mod 37 has (U) collisions",
      bw == 240 and uc37 > 0, f"{bw} bent squares; {uc37} shared classes")
print()

print("== B. The core of side 3 ==")
CORE3, R3 = core_records(M, CYC, 3)
FOLD3 = folded_on_core(M, CYC, 3)
bp, bf = readouts(M, CYC, CORE3, R3)
check("the covariant records on the core are exactly the folded cycle spirals",
      len(R3) == 24576 and set(R3) == FOLD3, "6 frames x (2 senses x 4 phases x 2 turns)^3")
check("every record reads a global frame and a global parity vector: the role pattern", bp == 0 and bf == 0)
print()

print("== C. Closure ==")
w4 = [closed_walks(M, c, 4) for c in CYC]
w8 = [closed_walks(M, c, 8) for c in CYC]
check("side-4 torus: every closed zero-sum phase walk is monotone, so the records are oriented spirals",
      all(f == 0 and mo == 8 for mo, f in w4), f"monotone per cycle: {[mo for mo, f in w4]}")
check("side-8 torus: folded closed zero-sum walks exist on every cycle", all(f == 64 for mo, f in w8),
      f"folded per cycle: {[f for mo, f in w8]}")
print()

print("== D. A folded spiral on the side-8 torus ==")
L = 8
W = [[0, 1, 2, 3, 2, 1, 0, 3], [0, 1, 2, 3, 0, 1, 2, 3], [0, 1, 2, 3, 0, 1, 2, 3]]
SITES8 = list(itertools.product(range(L), repeat=3))


def val8(x):
    return sum(sum(CYC[i][W[i][u]] for u in range(x[i])) for i in range(3)) % M


def nb8(y, i, sg):
    return tuple((u + sg * (k == i)) % L for k, u in enumerate(y))


ok8, oris, pars, frames = True, set(), set(), set()
for x in SITES8:
    Bd = [TAB.get((val8(x) - val8(nb8(x, i, -1))) % M) for i in range(3)]
    Fd = [TAB.get((val8(nb8(x, i, 1)) - val8(x)) % M) for i in range(3)]
    ok8 &= None not in Bd and None not in Fd and site_ok(Bd, Fd)
    if None not in Bd and None not in Fd:
        oris.add((x[0], (Fd[0][2] - Bd[0][2]) % 4))
        pars.add(tuple((Fd[i][2] - x[i]) % 2 for i in range(3)))
        frames.add(tuple(Fd[i][1] for i in range(3)))
check("the folded spiral satisfies the covariant rule at all 512 sites", ok8 and all(sum(CYC[0][k] for k in W[0]) % M == 0 for _ in [0]))
check("its orientation readout varies along the first axis, while its frame and parity readouts are global",
      len({o for (_, o) in oris}) == 2 and len(pars) == 1 and len(frames) == 1, "roles without an orientation")
print()

print("== E. Contrast ==")
CW, RW = core_records(*WEAK, 3)
bpw, bfw = readouts(*WEAK, CW, RW)
check("the letters of open PR #8752 on the core of side 3: 33792 covariant records, 9216 with a non-global parity readout",
      len(RW) == 33792 and bpw == 9216, "the mixed-sign square condition carries the role readout")
print()
check("budget: every search stayed under its node cap", NODES[0] < NODE_CAP, f"{NODES[0]} nodes, {time.time() - T0:.0f} s")
print()
print('per_element: Exact arithmetic tests the declared angle, star or linear-system objects; no physical qubit encoding is inferred.')
print('per_site: Site checks cover only the explicit finite boxes, tori and samples printed above; boundary freedoms remain as stated in the note.')
print('per_mode: Analytic mode or symmetry arguments are conditional source proofs; finite runner cases alone do not prove untested universality.')
print('per_block: This is one bounded support result in a supplied relational record model, with the controls and counts declared above.')
print('lattice_wide: No physical infinite-volume conclusion is inferred; any whole-lattice or all-size statement is limited to the explicit source theorem hypotheses.')
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
