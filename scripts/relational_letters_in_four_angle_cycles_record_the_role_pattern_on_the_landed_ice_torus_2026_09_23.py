#!/usr/bin/env python3
"""Relational letters in four-angle cycles record the role pattern on the landed ice torus.

Open PR #8750 found that relational letters in alternating pairs record the
role pattern under the static reading, but not on the landed ice torus of
side 4. There the pairs must sum to 180 degrees, and a site is fixed by its
neighbours only up to its antipode. This runner lets each lattice line cycle
through four angles (c_0, c_1, c_2, c_3) whose sum is 0 mod m. It uses one
fixed nearest-neighbour rule, the cycle rule, in the planar form of open PR
#8729. With back differences B_i = a(x) - a(x - e_i) and forward differences
F_i = a(x + e_i) - a(x), a core site satisfies the cycle rule when:

- all six differences are signed angles with one common sense;
- on each lattice line, the back and forward differences are consecutive
  angles c_k, c_{k+1} of one cycle;
- the three lines use the three cycles.

Checks, with exact integer arithmetic:

A. The letters: m = 211 (odd, so no residue is 180 degrees), cycles
   (19, 31, 132, 29), (108, 43, 194, 77), (88, 39, 126, 169), each summing to
   0 mod m. Every difference decodes, and every solution of the square
   relation is straight. (U): no two allowed stars share their six
   neighbours, with a positive control.
B. A complete search on cores of side 2, 3 and 4 finds exactly the 768
   cycle spirals: 6 frames, 2 senses and 4^3 phases.
C. Tori of side 2 to 8: records exist exactly when 4 divides L, and then they
   are the 768 spirals. This includes the landed ice torus of side 4.
D. Roles on the side-4 torus. Each site reads the frame and its phase
   x mod 4 on each line, hence its parity vector up to one global phase. The
   readout is unchanged by rotations of the circle, and the rule admits one
   value at each site given its neighbours.
E. Contrasts: a random cycle set mod 37 with (U) but with bent squares has
   records that are not spirals on the core of side 2; with one octant per
   site the side-4 torus has 24576 records.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import random
import sys
import time

PASS = FAIL = 0
T0 = time.time()
NODES = [0]
NODE_CAP = 7_100_000


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))


M, CYC = 211, ((19, 31, 132, 29), (108, 43, 194, 77), (88, 39, 126, 169))


def table(m, cyc):
    """residue -> (sense, cycle, phase); None unless the signed angles are distinct and nonzero."""
    tab = {}
    for j, c in enumerate(cyc):
        for k, g in enumerate(c):
            for s in (1, -1):
                r = (s * g) % m
                if r == 0 or r in tab:
                    return None
                tab[r] = (s, j, k)
    return tab


def site_ok(Bd, Fd, rule="cycle"):
    """Bd, Fd: decoded (sense, cycle, phase) per lattice axis, or None where unknown.
    rule "octant": each site may use its own octant, so each line has its own sense and its phase may step by -1."""
    js, senses = [], set()
    steps = (1, 3) if rule == "octant" else (1,)
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
        if b and f and (b[1] != f[1] or (f[2] - b[2]) % 4 not in steps):
            return False
        d = b or f
        if d:
            js.append(d[1])
    return len(senses) <= 1 and len(js) == len(set(js))


def stars(m, cyc):
    out = set()
    for s in (1, -1):
        for sig in itertools.permutations(range(3)):
            for k in itertools.product(range(4), repeat=3):
                out.add((tuple((s * cyc[sig[i]][k[i]]) % m for i in range(3)),
                         tuple((s * cyc[sig[i]][(k[i] + 1) % 4]) % m for i in range(3))))
    return out


def shared_stars(m, cyc):
    """(U) fails when moving the centre by d != 0 turns one allowed star into another: same six neighbours."""
    st = stars(m, cyc)
    return sum(1 for B, F in st for d in range(1, m)
               if (tuple((b + d) % m for b in B), tuple((f - d) % m for f in F)) in st)


def square_solutions(m, cyc):
    """a = F_i(y) (cycle A), c = F_j(y) (cycle B), b = F_j(y + e_i) (X != A), e = F_i(y + e_j) (Y != B), X != Y."""
    straight = bent = 0
    for A, B in itertools.permutations(range(3), 2):
        for X in range(3):
            for Y in range(3):
                if X == A or Y == B or X == Y:
                    continue
                for p, q, r, u in itertools.product(range(4), repeat=4):
                    if (cyc[A][p] + cyc[X][q] - cyc[B][r] - cyc[Y][u]) % m == 0:
                        if X == B and Y == A and q == r and u == p:
                            straight += 1
                        else:
                            bent += 1
    return straight, bent


def search(m, cyc, sites, core, nb, dist, fixed, cap, rule="cycle"):
    tab = table(m, cyc)
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
            if (z not in coreset or star_ok(z)) and all(
                    star_ok(y) for (y, i, sg) in touching[z] if y in val and y != z):
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


def spirals(m, cyc, sites, origin):
    """cycle spirals: line i carries cycle perm[i], sense s, phase ph[i] at the origin."""
    out = set()
    for perm in itertools.permutations(range(3)):
        for s in (1, -1):
            for ph in itertools.product(range(4), repeat=3):
                rec = []
                for x in sites:
                    v = 0
                    for i in range(3):
                        c, lo = cyc[perm[i]], origin[i]
                        if x[i] >= lo:
                            v += sum(c[(ph[i] + u - lo) % 4] for u in range(lo, x[i]))
                        else:
                            v -= sum(c[(ph[i] + u - lo) % 4] for u in range(x[i], lo))
                    rec.append((s * v) % m)
                out.add(tuple(rec))
    return out


def cores_of(recs, core):
    return {tuple(r[x] for x in core) for r in recs}


# ---------------------------------------------------------------- A. the letters
print("== A. The letters ==")
TAB = table(M, CYC)
check("m = 211, three cycles of four angles: the 24 signed angles are distinct and nonzero, and each cycle sums to 0 mod m",
      TAB is not None and len(TAB) == 24 and all(sum(c) % M == 0 for c in CYC), "m odd, so no residue is 180 degrees")
st, bt = square_solutions(M, CYC)
check("every solution of the square relation is straight: the same cycle and phase on opposite sides",
      bt == 0 and st == 6 * 16, f"{st} straight, {bt} bent")
check("(U): no two allowed stars share their six neighbours", shared_stars(M, CYC) == 0 and len(stars(M, CYC)) == 768,
      "768 stars at a centre; so every site is a function of its six neighbours")
C0 = ((34, 13, 35, 29), (11, 4, 23, 36), (20, 15, 18, 21))
n0 = shared_stars(37, C0)
check("the (U) test is not vacuous: the decodable cycle set mod 37 below has 24 stars that a shift of the centre turns into others",
      table(37, C0) is not None and n0 == 24, f"{C0}: {n0} shared stars")
print()

# ---------------------------------------------------------------- B. cores
print("== B. Complete search on cores of side 2, 3 and 4 ==")
core_counts = {}
for c in (2, 3, 4):
    sites, core, nb, dist = box(c)
    recs = search(M, CYC, sites, core, nb, dist, {(1, 1, 1): 0}, cap=5000)
    core_counts[c] = (len(recs), cores_of(recs, core) == spirals(M, CYC, core, (1, 1, 1)))
check("cores of side 2, 3, 4 (one core value fixed): exactly the 768 cycle spirals, each with one completion on the faces",
      all(v == (768, True) for v in core_counts.values()),
      "; ".join(f"side {c}: {v[0]}" for c, v in core_counts.items()) + " = 6 frames x 2 senses x 4^3 phases")
print()

# ---------------------------------------------------------------- C. tori
print("== C. Tori ==")
tor, TORUS4 = {}, None
for L in range(2, 9):
    s_, c_, n_, d_ = torus(L)
    r_ = search(M, CYC, s_, c_, n_, d_, {(0, 0, 0): 0}, cap=5000)
    ok = cores_of(r_, s_) == spirals(M, CYC, s_, (0, 0, 0)) if r_ else True
    tor[L] = (len(r_), ok)
    if L == 4:
        TORUS4 = (r_, s_, n_)
check("tori of side 2 to 8: static records exist exactly when 4 divides L, and they are the 768 cycle spirals",
      all(tor[L] == ((768, True) if L % 4 == 0 else (0, True)) for L in tor), ", ".join(f"L={L}: {tor[L][0]}" for L in tor))
print()

# ---------------------------------------------------------------- D. roles
print("== D. Roles on the landed ice torus (side 4) ==")
recs4, sites4, nb4 = TORUS4
frame_global = phase_ok = True
parity_phases, phases4 = set(), set()
for r in recs4:
    frames, kk = set(), {}
    for x in sites4:
        decs = [TAB[(r[nb4(x, i, 1)] - r[x]) % M] for i in range(3)]
        frames.add((tuple(d[1] for d in decs), decs[0][0]))
        kk[x] = tuple(d[2] for d in decs)
    frame_global &= len(frames) == 1
    ph = {tuple((kk[x][i] - x[i]) % 4 for i in range(3)) for x in sites4}
    phase_ok &= len(ph) == 1
    phases4 |= ph
    parity_phases |= {tuple(p % 2 for p in q) for q in ph}
check("every site reads the same frame (which line carries which cycle) and sense from its forward differences",
      frame_global, f"{len(recs4)} records x 64 sites")
check("each line's phase is x mod 4 plus one global phase, so the parity vector is read up to one global phase",
      phase_ok and len(phases4) == 64 and len(parity_phases) == 8, "all 64 cycle phases and all 8 parity phases occur")
cov = True
for r in recs4[:8]:
    base = {x: tuple(TAB[(r[nb4(x, i, 1)] - r[x]) % M][2] for i in range(3)) for x in sites4}
    for k in range(0, M, 7):
        for sg in (1, -1):
            r2 = {x: (sg * r[x] + k) % M for x in sites4}
            cov &= all(tuple(TAB[(r2[nb4(x, i, 1)] - r2[x]) % M][2] for i in range(3)) == base[x] for x in sites4)
check("the readout is unchanged by rotations of the circle, shifts and reflections", cov, "8 records x 31 shifts x 2")
uniq = True
for r in recs4[::16]:
    for x in sites4:
        n_ok = 0
        for v in range(M):
            Bd = [TAB.get((v - r[nb4(x, i, -1)]) % M) for i in range(3)]
            Fd = [TAB.get((r[nb4(x, i, 1)] - v) % M) for i in range(3)]
            n_ok += None not in Bd and None not in Fd and site_ok(Bd, Fd)
        uniq &= n_ok == 1
check("given its six neighbours, the cycle rule admits exactly one value at every site", uniq, "48 records x 64 sites x 211 values")
print()

# ---------------------------------------------------------------- E. contrast
print("== E. Contrast ==")
rng = random.Random(3)
while True:
    cyc37 = []
    for _ in range(3):
        a = rng.sample(range(1, 37), 3)
        cyc37.append(tuple(a + [(-sum(a)) % 37]))
    cyc37 = tuple(cyc37)
    if table(37, cyc37) is not None and shared_stars(37, cyc37) == 0 and square_solutions(37, cyc37)[1] > 0:
        break
sites, core, nb, dist = box(2)
r37 = search(37, cyc37, sites, core, nb, dist, {(1, 1, 1): 0}, cap=5000)
extra = cores_of(r37, core) - spirals(37, cyc37, core, (1, 1, 1))
check("a cycle set mod 37 with (U) but bent squares has core records that are not spirals",
      len(extra) > 0, f"{cyc37}: {len(r37)} records, {len(extra)} not spirals; bent squares {square_solutions(37, cyc37)[1]}")
s4, c4, n4, d4 = torus(4)
roct = search(M, CYC, s4, c4, n4, d4, {(0, 0, 0): 0}, cap=50000, rule="octant")
check("with one octant per site (a sense per line, phase steps of +1 or -1), the side-4 torus has 24576 records",
      len(roct) == 24576 and len(cores_of(roct, s4) & spirals(M, CYC, s4, (0, 0, 0))) == 768,
      "768 of them the spirals with every axis forward; the rest have axes reversed (open PR #8854)")
print()
check("budget: every search stayed under its node cap", NODES[0] < NODE_CAP, f"{NODES[0]} nodes, {time.time() - T0:.0f} s")
print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
