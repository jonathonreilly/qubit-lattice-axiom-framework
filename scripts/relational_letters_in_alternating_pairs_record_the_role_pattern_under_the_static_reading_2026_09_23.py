#!/usr/bin/env python3
"""Relational letters in alternating pairs record the role pattern under the static reading.

Open PR #8743 found that relational spiral letters under the static reading,
with its global octant, are globally rigid for Sidon angles. Each rigid record
gives every site the same view, so it carries the lattice frame but no role
pattern. This runner takes six angles in three pairs (alpha_j, beta_j) and one
fixed nearest-neighbour rule, the pair rule, in the planar form of open PR
#8729. Values are residues mod m. With back differences B_i = a(x) - a(x - e_i)
and forward differences F_i = a(x + e_i) - a(x), a core site satisfies the pair
rule when:

- all six differences are signed angles with one common sense;
- the two neighbours on one lattice line use the two angles of one pair, one
  each (complementary types);
- the three lines use the three pairs.

Checks, with exact integer arithmetic:

A. The letters: m = 16, pairs (1, 7), (2, 10), (3, 5), in steps of 22.5
   degrees. Every difference decodes, and conditions (D), (E) and (U) hold.
   Under (U) no two stars share a neighbour configuration, so every site is a
   function of its six neighbours; a decodable set that fails (U) is the
   positive control. No angle, and no difference of angles from different
   pairs, is 0 or 180 degrees.
B. The square lemma: under (D) and (E) every square of core links is
   straight. All local square configurations are enumerated.
C. A complete search on cores of side 2, 3 and 4 finds exactly the 96
   alternating spirals: 6 frames, 2 senses and 8 phases.
D. Tori of side 2 to 8: records exist exactly for L = 8, and they are the 96
   spirals.
E. Roles on the side-8 torus. Each site reads the frame and its parity vector,
   the role pattern up to its 8 global phases. The readout is unchanged by
   rotations of the circle, and each site value is fixed by its six
   neighbours.
F. The landed ice torus has side 4. Pair letters that wrap on it need pair
   sums of 180 degrees, and then (U) fails. With m = 20, pairs (1, 9), (2, 8),
   (4, 6), the records are the 96 spirals, but every site admits its antipode
   given its neighbours: shifting one parity class by 180 degrees gives
   another record.
G. Contrasts on those side-4 letters:
   - without complementary types, the readout misses the role pattern;
   - with one octant per site, the records are flexible.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
import time

PASS = FAIL = 0
T0 = time.time()
NODES = [0]
NODE_CAP = 2_500_000


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))


M, PAIRS = 16, ((1, 7), (2, 10), (3, 5))
M4, PAIRS4 = 20, ((1, 9), (2, 8), (4, 6))


def table(m, pairs):
    """residue -> (sense, pair index, type); None unless the twelve signed angles are distinct and nonzero."""
    tab = {}
    for j, pr in enumerate(pairs):
        for t, g in enumerate(pr):
            for s in (1, -1):
                r = (s * g) % m
                if r == 0 or r in tab:
                    return None
                tab[r] = (s, j, t)
    return tab


def conditions(m, pairs):
    """(D): within-pair differences distinct up to sign across pairs.
    (E): no within-pair difference equals a difference between angles of the other two pairs."""
    pm = lambda x: {x % m, (-x) % m}
    delta = [(p[0] - p[1]) % m for p in pairs]
    D = all(not (pm(delta[A]) & pm(delta[B])) for A in range(3) for B in range(3) if A != B)
    E = all(not (pm(delta[A]) & {(pairs[B][r] - pairs[C][q]) % m for r in (0, 1) for q in (0, 1)})
            for A, B, C in itertools.permutations(range(3)))
    return D, E


def stars(m, pairs):
    """every star allowed by the pair rule at a centre of value 0: (back differences, forward differences)."""
    out = set()
    for s in (1, -1):
        for sig in itertools.permutations(range(3)):
            for t in itertools.product((0, 1), repeat=3):
                out.add((tuple((s * pairs[sig[i]][t[i]]) % m for i in range(3)),
                         tuple((s * pairs[sig[i]][1 - t[i]]) % m for i in range(3))))
    return out


def shared_stars(m, pairs):
    """(U) fails when moving the centre by d != 0 turns one allowed star into another: same six neighbours."""
    st = stars(m, pairs)
    return sum(1 for B, F in st for d in range(1, m)
               if (tuple((b + d) % m for b in B), tuple((f - d) % m for f in F)) in st)


def site_ok(Bd, Fd, rule):
    """Bd, Fd: decoded (sense, pair, type) per lattice axis, or None where unknown."""
    js = []
    senses = set()
    for i in range(3):
        b, f = Bd[i], Fd[i]
        if rule == "octant":
            if b and f and b[0] != f[0]:
                return False
        else:
            if b:
                senses.add(b[0])
            if f:
                senses.add(f[0])
        if b and f:
            if b[1] != f[1]:
                return False
            if rule != "free" and b[2] == f[2]:
                return False
        d = b or f
        if d:
            js.append(d[1])
    return len(senses) <= 1 and len(js) == len(set(js))


def search(m, pairs, rule, sites, core, nb, dist, fixed, cap):
    tab = table(m, pairs)
    coreset = set(core)
    val = dict(fixed)
    order = sorted((x for x in sites if x not in val), key=lambda x: (dist(x), x))
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
                Bd[i] = tab.get((val[y] - val[zb]) % m)
                if Bd[i] is None:
                    return None
            if zf in val:
                Fd[i] = tab.get((val[zf] - val[y]) % m)
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
        for r, dec in tab.items():
            B2, F2 = list(d[0]), list(d[1])
            if sg == 1:
                F2[i] = dec
            else:
                B2[i] = dec
            if site_ok(B2, F2, rule):
                out.add((val[y] + sg * r) % m)
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
        for v in sorted(cands if cands is not None else range(m)):
            val[z] = v
            good = (z not in coreset or star_ok(z)) and all(
                star_ok(y) for (y, i, sg) in touching[z] if y in val and y != z)
            if good:
                rec(k + 1)
            del val[z]

    rec(0)
    return recs


def box(c):
    n = c + 2
    core = list(itertools.product(range(1, c + 1), repeat=3))
    sites = [x for x in itertools.product(range(n), repeat=3) if sum(u in (0, n - 1) for u in x) <= 1]
    nb = lambda y, i, sg: tuple(u + sg * (k == i) for k, u in enumerate(y))
    return sites, core, nb, (lambda x: sum(abs(u - 1) for u in x))


def torus(L):
    sites = list(itertools.product(range(L), repeat=3))
    nb = lambda y, i, sg: tuple((u + sg * (k == i)) % L for k, u in enumerate(y))
    return sites, sites, nb, (lambda x: sum(min(u, L - u) for u in x))


def spirals(m, pairs, sites, origin):
    """the alternating spirals: frame perm (lattice axis i carries pair perm[i]), sense s, phases ph."""
    out = {}
    for perm in itertools.permutations(range(3)):
        for s in (1, -1):
            for ph in itertools.product((0, 1), repeat=3):
                rec = []
                for x in sites:
                    v = 0
                    for i in range(3):
                        pr, lo = pairs[perm[i]], origin[i]
                        if x[i] >= lo:
                            v += sum(pr[(ph[i] + u - lo) % 2] for u in range(lo, x[i]))
                        else:
                            v -= sum(pr[(ph[i] + u - lo) % 2] for u in range(x[i], lo))
                    rec.append((s * v) % m)
                out[tuple(rec)] = (perm, s, ph)
    return out


def cores_of(recs, core):
    return {tuple(r[x] for x in core) for r in recs}


# ---------------------------------------------------------------- A. the letters
print("== A. The letters ==")
TAB = table(M, PAIRS)
D16, E16 = conditions(M, PAIRS)
check("m = 16, pairs (1,7), (2,10), (3,5): the twelve signed angles are distinct and nonzero, so every difference decodes",
      TAB is not None and len(TAB) == 12, "steps of 22.5 degrees; pair sums 180, 270, 180 degrees")
check("conditions (D) and (E) hold, and (U): no two allowed stars share their six neighbours",
      D16 and E16 and shared_stars(M, PAIRS) == 0 and len(stars(M, PAIRS)) == 96,
      "96 stars at a centre; so every site is a function of its six neighbours")
check("the (U) test is not vacuous: m = 13, pairs (1,2), (3,4), (7,8) decodes but has 24 stars that a shift of the centre turns into others",
      table(13, ((1, 2), (3, 4), (7, 8))) is not None and shared_stars(13, ((1, 2), (3, 4), (7, 8))) == 24)
half = M // 2
circle = all(g % M not in (0, half) for pr in PAIRS for g in pr) and all(
    (x - y) % M not in (0, half) for A, B in itertools.permutations(range(3), 2) for x in PAIRS[A] for y in PAIRS[B])
check("no angle, and no difference of angles from different pairs, is 0 or 180 degrees",
      circle, "the separations the one-great-circle step of open PR #8743 uses")
tor_ok = [L for L in range(2, 33) if L % 2 == 0 and all(((L // 2) * (a + b)) % M == 0 for a, b in PAIRS)]
check("records can wrap on the side-L torus only for 8 | L (alternation needs L even, and (L/2)(alpha + beta) = 0 on every pair)",
      tor_ok == [8, 16, 24, 32], f"L up to 32: {tor_ok}")
print()

# ---------------------------------------------------------------- B. square lemma
print("== B. The square lemma ==")


def square_solutions(m, pairs):
    """forward differences a = F_i(y) (pair A), c = F_j(y) (pair B); b = F_j(y + e_i) (pair X != A),
    e = F_i(y + e_j) (pair Y != B), X != Y at the far corner; one sense; a + b = c + e."""
    straight = bent = 0
    for A, B in itertools.permutations(range(3), 2):
        for X in range(3):
            for Y in range(3):
                if X == A or Y == B or X == Y:
                    continue
                for p, q, r, u in itertools.product((0, 1), repeat=4):
                    if (pairs[A][p] + pairs[X][q] - pairs[B][r] - pairs[Y][u]) % m == 0:
                        if X == B and Y == A and q == r and u == p:
                            straight += 1
                        else:
                            bent += 1
    return straight, bent


s16, b16 = square_solutions(M, PAIRS)
check("every solution of the square relation is straight: the same pair and type on opposite sides",
      b16 == 0 and s16 == 6 * 4, f"{s16} straight, {b16} bent")
print()

# ---------------------------------------------------------------- C. cores
print("== C. Complete search on cores ==")
core_counts = {}
for c in (2, 3, 4):
    sites, core, nb, dist = box(c)
    recs = search(M, PAIRS, "pairs", sites, core, nb, dist, {(1, 1, 1): 0}, cap=5000)
    sp = spirals(M, PAIRS, core, (1, 1, 1))
    core_counts[c] = (len(recs), len(cores_of(recs, core)), cores_of(recs, core) == set(sp))
check("cores of side 2, 3, 4 (one core value fixed): exactly the 96 alternating spirals, each with one completion on the faces",
      all(v == (96, 96, True) for v in core_counts.values()),
      "; ".join(f"side {c}: {v[0]} records" for c, v in core_counts.items()) + " = 6 frames x 2 senses x 8 phases")
print()

# ---------------------------------------------------------------- D. tori
print("== D. Tori ==")
tor = {}
TORUS8 = None
for L in range(2, 9):
    sites, core, nb, dist = torus(L)
    recs = search(M, PAIRS, "pairs", sites, core, nb, dist, {(0, 0, 0): 0}, cap=5000)
    ok = True
    if recs:
        ok = cores_of(recs, sites) == set(spirals(M, PAIRS, sites, (0, 0, 0)))
    tor[L] = (len(recs), ok)
    if L == 8:
        TORUS8 = (recs, sites, nb)
check("tori of side 2 to 8: static records exist only for L = 8, and they are the 96 spirals",
      all(tor[L] == ((96, True) if L == 8 else (0, True)) for L in tor), ", ".join(f"L={L}: {tor[L][0]}" for L in tor))
print()

# ---------------------------------------------------------------- E. roles
print("== E. Roles on the side-8 torus ==")


def readouts(recs, sites, nb, m, tab):
    frame_global = parity_ok = True
    phases, hist = set(), {}
    for r in recs:
        frames, rho = set(), {}
        for x in sites:
            decs = [tab[(r[nb(x, i, 1)] - r[x]) % m] for i in range(3)]
            frames.add((tuple(d[1] for d in decs), decs[0][0]))
            rho[x] = {d[1]: d[2] for d in decs}
        frame_global &= len(frames) == 1
        perm, s = next(iter(frames))
        phs = {tuple(rho[x][perm[i]] ^ (x[i] % 2) for i in range(3)) for x in sites}
        parity_ok &= len(phs) == 1
        phases |= phs
        for x in sites:
            w = sum(rho[x].values())
            hist[w] = hist.get(w, 0) + 1
    return frame_global, parity_ok, phases, hist


def admitted(r, x, nb, m, tab, rule="pairs"):
    """values the pair rule admits at x, given the record's six neighbours of x."""
    out = []
    for v in range(m):
        Bd = [tab.get((v - r[nb(x, i, -1)]) % m) for i in range(3)]
        Fd = [tab.get((r[nb(x, i, 1)] - v) % m) for i in range(3)]
        if None not in Bd and None not in Fd and site_ok(Bd, Fd, rule):
            out.append(v)
    return out


recs8, sites8, nb8 = TORUS8
fg, po, phs8, hist8 = readouts(recs8, sites8, nb8, M, TAB)
check("every site reads the same frame (which line carries which pair) and sense from its forward differences",
      fg, f"96 records x {len(sites8)} sites")
check("the type readout is the parity vector x mod 2 in the pair frame plus one global phase; all 8 phases occur",
      po and len(phs8) == 8, f"role weights V/L/P/C per record: {[hist8.get(w, 0) // max(len(recs8), 1) for w in range(4)]}")
cov = True
for r in recs8[:8]:
    base = {x: tuple(TAB[(r[nb8(x, i, 1)] - r[x]) % M][2] for i in range(3)) for x in sites8}
    for k in range(M):
        for sg in (1, -1):
            r2 = {x: (sg * r[x] + k) % M for x in sites8}
            cov &= all(tuple(TAB[(r2[nb8(x, i, 1)] - r2[x]) % M][2] for i in range(3)) == base[x] for x in sites8)
check("the readout is unchanged by every rotation of the circle, shifts and reflections", cov, "8 records x 16 shifts x 2")
uniq = all(admitted(r, x, nb8, M, TAB) == [r[x]] for r in recs8 for x in sites8)
check("given its six neighbours, the pair rule admits exactly one value at every site of every record",
      uniq, "each site is a function of its nearest neighbours")
print()

# ---------------------------------------------------------------- F. landed torus
print("== F. The landed ice torus (side 4) ==")
n4 = fail4 = 0
for m in range(3, 25):
    tp = [(a, b) for a in range(1, m) for b in range(a + 1, m) if (2 * (a + b)) % m == 0]
    for prs in itertools.combinations(tp, 3):
        if table(m, prs) is not None:
            n4 += 1
            fail4 += shared_stars(m, prs) > 0 and all((a + b) % m == m // 2 for a, b in prs)
check("every decoding pair set that can wrap on the side-4 torus has pair sums of 180 degrees and fails (U)",
      n4 > 0 and fail4 == n4, f"moduli 3 to 24: {n4} sets, all fail (U)")
TAB4 = table(M4, PAIRS4)
D20, E20 = conditions(M4, PAIRS4)
sites, core, nb, dist = torus(4)
recs4 = search(M4, PAIRS4, "pairs", sites, core, nb, dist, {(0, 0, 0): 0}, cap=5000)
sp4 = spirals(M4, PAIRS4, sites, (0, 0, 0))
check("m = 20, pairs (1,9), (2,8), (4,6): (D) and (E) hold, and the side-4 torus has exactly the 96 spirals as records",
      D20 and E20 and len(recs4) == 96 and cores_of(recs4, sites) == set(sp4))
anti = all(admitted(r, x, nb, M4, TAB4) == sorted([r[x], (r[x] + M4 // 2) % M4]) for r in recs4 for x in sites)
recset = cores_of(recs4, sites)
shift_ok = all(tuple((r[x] + (M4 // 2) * (sum(x) % 2)) % M4 for x in sites) in recset for r in recs4)
check("there every site admits exactly its value and its antipode given its neighbours, and moving one parity class by 180 degrees gives another record",
      anti and shift_ok, "so a site is not a function of its six neighbours on the landed torus")
print()

# ---------------------------------------------------------------- G. contrasts
print("== G. Contrasts on the side-4 letters ==")
free = search(M4, PAIRS4, "free", sites, core, nb, dist, {(0, 0, 0): 0}, cap=20000)
miss = sum(1 for r in free
           if len({tuple(TAB4[(r[nb(x, i, 1)] - r[x]) % M4][2] ^ (x[i] % 2) for i in range(3)) for x in sites}) > 1)
check("without complementary types: 2592 records, and the readout misses the role pattern on all but the 96 spirals",
      len(free) == 2592 and len(cores_of(free, sites) & set(sp4)) == 96 and miss == 2592 - 96,
      "12 frames and senses x 6^3 type orders")
octant = search(M4, PAIRS4, "octant", sites, core, nb, dist, {(0, 0, 0): 0}, cap=20000)
check("with one octant per site (a sense per line), the side-4 torus has 9216 records, of which 96 are spirals",
      len(octant) == 9216 and len(cores_of(octant, sites) & set(sp4)) == 96, "rigidity uses the reading's global octant")
print()
check("budget: every search stayed under its node cap", NODES[0] < NODE_CAP, f"{NODES[0]} nodes, {time.time() - T0:.0f} s")
print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
