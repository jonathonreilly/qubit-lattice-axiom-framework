#!/usr/bin/env python3
"""Relational letters under the static reading are globally rigid: every
static record is a spiral on its core, exactly when the three angles form a
Sidon set, which is conditions (a) and (c) of open PR 8729.

Open PR 8691 left rigidity open ("every stationary record a spiral" is not
established); open PRs 8717 and 8724 showed linear and local nonlinear
rigidity under the static reading.  Under the static reading each core site
is a covariant completion of its three back neighbours and of its three
forward neighbours.  A completion needs the values on one great circle, and
neighbouring completions share two points of it, so every core value lies on
one circle; there each completion is additive: the three differences to the
back neighbours are a common-sign permutation of the angles, and likewise to
the forward neighbours.  Then:
  * plaquette lemma: if the angles form a Sidon set (all six sums
    theta_i + theta_j, i <= j, distinct), every elementary square of links
    is straight (opposite links equal) or folded (opposite links negated);
  * signs depend only on the level x_1 + x_2 + x_3, and a fold at any level
    would give one site two equal outgoing differences, or a link two
    different values;
  * so every square is straight and every link difference is constant
    along its axis: the record is a spiral on the core.
The Sidon property is exactly conditions (a) and (c) of open PR 8729.  The
runner checks the identification, the plaquette lemma, and the theorem by
complete search on cores of side 2, 3 and 4 for the seven letters
(1, 2, 4) x 360/7 and the letters (30, 60, 150) degrees; two angle sets
that break condition (c) have many more static records (48, 384, 3072 on
cores of side 2, 3, 4), and the sweep reading (back neighbours only) is
flexible.  On a cubic torus every site is a core site, so a static record
is a spiral that must wrap consistently: the seven letters have static records on the
side-L torus only for L = 7 among L = 2 to 7, and neither letter set has
one on the tori of side 2 and 4 that carry the landed ice measure (2 x 2 x 2
cells; 4 x 4 x 4 sites with links, plaquettes and cube sites).  Every core
site of a static record sees the same differences to its neighbours, so the
record carries the frame but no role pattern.  The rigidity uses the
reading's fixed octant (back neighbours x - e_i, forward x + e_i), which
supplies the orientation of each axis: if each core site may use its own
octant, the seven letters are not rigid.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.

Declared objects
  * angles as residues modulo m in units of 360/m degrees; a static record
    on a box is an assignment of residues such that at every core site (all
    six neighbours in the box) the back differences and the forward
    differences are each a common-sign permutation of the angles;
  * the core-only search fixes one core value (a global rotation) and
    leaves the values outside the core free; a full search on the side-4
    box, face values included, is its cross-check;
  * budget guards: a search stops at a declared number of records (5000
    core records, 500000 full records, 2000 torus records, 20000 octant
    records) or of search steps (200000, 8000000, 1200000, 100000, about
    three times the most the true run uses), and all searches together stop
    after 240000000 comparisons with a triple (the true run makes about
    80000000); a stopped search returns None, which fails its check;
  * exact modular arithmetic.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
from itertools import combinations, permutations, product

RESULTS = []
WORK, WORK_CAP = [0], 240000000


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


def sidon(th, m):
    return len({(th[i] + th[j]) % m for i in range(3) for j in range(i, 3)}) == 6


def cond_a(th, m):
    return all((2 * th[i] - 2 * th[j]) % m for i in range(3) for j in range(i + 1, 3))


def cond_c(th, m):
    return all((2 * th[k] - sum(th[i] for i in range(3) if i != k)) % m for k in range(3))


def six_signed(th, m):
    return len({(s * t) % m for t in th for s in (1, -1)}) == 6


def triples(th, m):
    return [tuple((s * th[p[i]]) % m for i in range(3)) for p in permutations(range(3)) for s in (1, -1)]


def fits(ins, th, m):
    outs = set()
    for sigma in permutations(range(3)):
        for sgn in (1, -1):
            b = (ins[0] + sgn * th[sigma[0]]) % m
            if all((b - sgn * th[sigma[i]]) % m == ins[i] % m for i in range(3)):
                outs.add(b)
    return outs


SETS = [("seven letters (1, 2, 4) mod 7", (1, 2, 4), 7), ("30, 60, 150 degrees (1, 2, 5) mod 12", (1, 2, 5), 12),
        ("contrast (1, 3, 5) mod 12", (1, 3, 5), 12), ("contrast (1, 2, 3) mod 7", (1, 2, 3), 7)]

print("A. the Sidon property is conditions (a) and (c)")
ident_ok, n_triples, n_sidon = True, 0, 0
for m in range(5, 13):
    for th in combinations(range(1, m), 3):
        n_triples += 1
        n_sidon += sidon(th, m)
        ident_ok = ident_ok and sidon(th, m) == (cond_a(th, m) and cond_c(th, m))
flags = [(sidon(th, m), six_signed(th, m), cond_c(th, m)) for name, th, m in SETS]
check("over every triple of distinct angle multiples modulo m = 5 to 12, the angles are Sidon exactly when (a) and (c) hold",
      ident_ok and n_triples == 494 and n_sidon == 252
      and flags == [(True, True, True), (True, True, True), (False, True, False), (False, True, False)],
      f"{n_triples} triples, {n_sidon} Sidon; the seven letters and 30, 60, 150 degrees are Sidon with six distinct "
      "signed angles; (1, 3, 5) mod 12 and (1, 2, 3) mod 7 break (c): 1 + 5 = 3 + 3 and 1 + 3 = 2 + 2")


def plaquette_classes(th, m):
    T = triples(th, m)
    pairs = {(t[i], t[j]) for t in T for i in range(3) for j in range(3) if i != j}
    straight = folded = other = 0
    for a, c in pairs:
        for b, e in pairs:
            if (a + b - c - e) % m:
                continue
            if a == e and b == c:
                straight += 1
            elif b == (-a) % m and e == (-c) % m:
                folded += 1
            else:
                other += 1
    return straight, folded, other


print("B. the plaquette lemma")
pl = [plaquette_classes(th, m) for name, th, m in SETS]
check("with Sidon angles every elementary square is straight or folded; the contrast sets have other squares",
      pl[0][2] == 0 and pl[1][2] == 0 and pl[2][2] > 0 and pl[3][2] > 0 and all(p[0] > 0 and p[1] > 0 for p in pl),
      "; ".join(f"{name}: {p[0]} straight, {p[1]} folded, {p[2]} other" for (name, th, m), p in zip(SETS, pl)))


def core_records(L, th, m, dirs=(-1, 1), cap=5000, node_cap=200000):
    core = sorted(product(range(1, L - 1), repeat=3), key=lambda x: (sum(x), x))
    cs = set(core)
    T = triples(th, m)
    sh = lambda x, i, s: tuple(x[k] + s * (k == i) for k in range(3))
    nbrs = {x: [y for i in range(3) for s in (1, -1) for y in [sh(x, i, s)] if y in cs] for x in core}

    def ok_at(z, A):
        WORK[0] += len(T)
        if WORK[0] > WORK_CAP:
            raise OverflowError
        for s in dirs:
            known = {}
            for i in range(3):
                y = sh(z, i, s)
                if y in cs:
                    if y not in A:
                        return True
                    known[i] = (s * (A[y] - A[z])) % m
            if not any(all(t[i] == v for i, v in known.items()) for t in T):
                return False
        return True

    out = []

    nodes = [0]

    def rec(idx, A):
        nodes[0] += 1
        if nodes[0] > node_cap:
            raise OverflowError
        if len(out) >= cap:
            raise OverflowError
        if idx == len(core):
            out.append(tuple(A[x] for x in core))
            return
        x = core[idx]
        for v in ([0] if idx == 0 else range(m)):
            A[x] = v
            if ok_at(x, A) and all(ok_at(z, A) for z in nbrs[x] if z in A):
                rec(idx + 1, A)
            del A[x]

    try:
        rec(0, {})
    except OverflowError:
        return None, core
    return out, core


def is_spiral(vals, core, m):
    A = dict(zip(core, vals))
    x0 = core[0]
    d = [(A[tuple(x0[k] + (k == i) for k in range(3))] - A[x0]) % m for i in range(3)]
    return all((A[x] - A[x0] - sum(d[i] * (x[i] - x0[i]) for i in range(3))) % m == 0 for x in core)


print("C. every static record is a spiral on its core, for Sidon angles")
table = {}
for name, th, m in SETS:
    for side in (2, 3, 4):
        recs, core = core_records(side + 2, th, m)
        table[(name, side)] = (None, None) if recs is None else (len(recs), sum(is_spiral(r, core, m) for r in recs))
rigid = all(table[(SETS[k][0], s)] == (12, 12) for k in (0, 1) for s in (2, 3, 4))
soft = all(table[(SETS[k][0], s)] == (n, 12) for k in (2, 3) for s, n in ((2, 48), (3, 384), (4, 3072)))
check("cores of side 2, 3, 4: Sidon angles give exactly the 12 spirals; the contrast sets give 48, 384, 3072 records",
      rigid and soft,
      "; ".join(f"{name.split(' (')[0] if 'contrast' not in name else name}: "
                + ", ".join(f"{table[(name, s)][0]}" for s in (2, 3, 4)) for name, th, m in SETS)
      + "; one core value fixed, 12 = six angle assignments times two senses")

print("D. the sweep reading is flexible")
sweep = {name: core_records(4, th, m, dirs=(-1,))[0] for name, th, m in SETS[:2]}
sweep_counts = {name: (None, None) if r is None else
                (len(r), sum(is_spiral(x, sorted(product(range(1, 3), repeat=3), key=lambda y: (sum(y), y)), m) for x in r))
                for (name, th, m), r in zip(SETS[:2], sweep.values())}
check("with back neighbours only, the same Sidon angles admit records on the core of side 2 that are not spirals",
      all(n is not None and n > 12 and s == 12 for n, s in sweep_counts.values()),
      "; ".join(f"{name.split(' (')[0]}: {n} records, {s} spirals" for name, (n, s) in sweep_counts.items())
      + "; the forward completions are what fix the frame")

print("E. spirals are static records with unique completions")
uniq_ok, n_sites = True, 0
for name, th, m in SETS[:2]:
    for t in triples(th, m):
        A = {x: sum(t[i] * x[i] for i in range(3)) % m for x in product(range(5), repeat=3)}
        for x in product(range(1, 4), repeat=3):
            back = [A[tuple(x[k] - (k == i) for k in range(3))] for i in range(3)]
            fwd = [A[tuple(x[k] + (k == i) for k in range(3))] for i in range(3)]
            uniq_ok = uniq_ok and fits(back, th, m) == {A[x]} and fits(fwd, th, m) == {A[x]}
            n_sites += 1
check("every spiral is the unique completion of its back and of its forward neighbours at every core site",
      uniq_ok and n_sites == 2 * 12 * 27,
      f"{n_sites} core sites over the 12 spirals of both Sidon sets on the side-5 box; so the static records are "
      "exactly the spirals, up to a global rotation")


def full_records(L, th, m, cap=500000, node_cap=8000000):
    core = sorted(product(range(1, L - 1), repeat=3), key=lambda x: (sum(x), x))
    T = triples(th, m)
    sh = lambda x, i, s: tuple(x[k] + s * (k == i) for k in range(3))
    cores, leaves = set(), [0]

    nodes = [0]

    def rec(idx, A):
        nodes[0] += 1
        if nodes[0] > node_cap:
            raise OverflowError
        if idx == len(core):
            leaves[0] += 1
            if leaves[0] > cap:
                raise OverflowError
            cores.add(tuple(A[x] for x in core))
            return
        x = core[idx]
        v = A[x]
        for tin in T:
            new1 = {}
            if any(A.get(sh(x, i, -1), (v - tin[i]) % m) != (v - tin[i]) % m for i in range(3)):
                continue
            for i in range(3):
                if sh(x, i, -1) not in A:
                    new1[sh(x, i, -1)] = (v - tin[i]) % m
            A.update(new1)
            for tout in T:
                nodes[0] += 1
                if nodes[0] > node_cap:
                    raise OverflowError
                if any(A.get(sh(x, i, 1), (v + tout[i]) % m) != (v + tout[i]) % m for i in range(3)):
                    continue
                new2 = {sh(x, i, 1): (v + tout[i]) % m for i in range(3) if sh(x, i, 1) not in A}
                A.update(new2)
                rec(idx + 1, A)
                for y in new2:
                    del A[y]
            for y in new1:
                del A[y]

    try:
        rec(0, {core[0]: 0})
    except OverflowError:
        return None
    return cores


print("F. cross-check with face values included")
fc = {name: len(r) if r is not None else None for name, th, m in (SETS[0], SETS[2]) for r in [full_records(4, th, m)]}
check("a full search on the side-4 box, face values included, finds the same core records",
      fc == {SETS[0][0]: 12, SETS[2][0]: 48},
      f"seven letters {fc[SETS[0][0]]} cores, contrast (1, 3, 5) mod 12 {fc[SETS[2][0]]} cores")


def torus_records(L, th, m, cap=2000, node_cap=1200000):
    sites = sorted(product(range(L), repeat=3))
    T = triples(th, m)
    sh = lambda x, i, s: tuple((x[k] + s * (k == i)) % L for k in range(3))
    nbrs = {x: {sh(x, i, s) for i in range(3) for s in (1, -1)} - {x} for x in sites}

    def ok_at(z, A):
        WORK[0] += len(T)
        if WORK[0] > WORK_CAP:
            raise OverflowError
        for s in (-1, 1):
            known = {}
            for i in range(3):
                y = sh(z, i, s)
                if y in A:
                    known[i] = (s * (A[y] - A[z])) % m
            if not any(all(t[i] == v for i, v in known.items()) for t in T):
                return False
        return True

    out = []

    nodes = [0]

    def rec(idx, A):
        nodes[0] += 1
        if nodes[0] > node_cap:
            raise OverflowError
        if len(out) >= cap:
            raise OverflowError
        if idx == len(sites):
            out.append(tuple(A[x] for x in sites))
            return
        x = sites[idx]
        for v in ([0] if idx == 0 else range(m)):
            A[x] = v
            if ok_at(x, A) and all(ok_at(z, A) for z in nbrs[x] if z in A):
                rec(idx + 1, A)
            del A[x]

    try:
        rec(0, {})
    except OverflowError:
        return None
    return out, sites


print("G. on a torus the frame must wrap consistently")
tor = {}
for name, th, m, Ls in ((SETS[0][0], (1, 2, 4), 7, (2, 3, 4, 5, 6, 7)), (SETS[1][0], (1, 2, 5), 12, (2, 3, 4))):
    for L in Ls:
        r = torus_records(L, th, m)
        tor[(name, L)] = None if r is None else (len(r[0]), sum(is_spiral(v, r[1], m) for v in r[0]))
seven = {L: tor[(SETS[0][0], L)] for L in (2, 3, 4, 5, 6, 7)}
check("on the cubic torus of side L the seven letters have static records only for L = 7 among L = 2 to 7, exactly the 12 spirals; none on the side-2 or side-4 torus for either set",
      seven == {2: (0, 0), 3: (0, 0), 4: (0, 0), 5: (0, 0), 6: (0, 0), 7: (12, 12)}
      and all(tor[(SETS[1][0], L)] == (0, 0) for L in (2, 3, 4)),
      "seven letters, records for L = 2..7: " + ", ".join(str(seven[L][0]) if seven[L] else "cap" for L in range(2, 8))
      + "; 30, 60, 150 degrees, L = 2, 3, 4: none; every site is a core site, a spiral wraps consistently only if L d = 0 mod m")

print("H. the record carries the frame and nothing positional")
one_view, roles_vary, same_value, n_sites = True, True, True, 0
for name, th, m in SETS[:2]:
    for t in triples(th, m):
        A = {x: sum(t[i] * x[i] for i in range(3)) % m for x in product(range(6), repeat=3)}
        core6 = list(product(range(1, 5), repeat=3))
        views = {tuple((A[tuple(x[k] + s * (k == i) for k in range(3))] - A[x]) % m for i in range(3) for s in (1, -1))
                 for x in core6}
        one_view = one_view and len(views) == 1
        roles_vary = roles_vary and len({tuple(c % 2 for c in x) for x in core6}) == 8
        kernel = [v for v in product(range(3), repeat=3) if any(c % 2 for c in v) and sum(t[i] * v[i] for i in range(3)) % m == 0]
        same_value = same_value and len(kernel) > 0
        n_sites += len(core6)
diag = all(sum(t) % 7 == 0 for t in triples((1, 2, 4), 7))
check("every core site of a static record sees the same differences, so no covariant local readout carries the role pattern",
      one_view and roles_vary and same_value and diag and n_sites == 2 * 12 * 64,
      "one view per spiral at all 64 core sites of the side-6 box, while the parity vector takes 8 values; even with the "
      "global rotation fixed, sites of different parity share a value (seven letters: x and x + (1, 1, 1), as 1 + 2 + 4 = 7)")

print("I. the rigidity uses the reading's octant")


def octant_records(L, th, m, cap=20000, node_cap=100000):
    core = sorted(product(range(1, L - 1), repeat=3), key=lambda x: (sum(x), x))
    cs = set(core)
    T = triples(th, m)
    sh = lambda x, i, s: tuple(x[k] + s * (k == i) for k in range(3))
    nbrs = {x: [y for i in range(3) for s in (1, -1) for y in [sh(x, i, s)] if y in cs] for x in core}

    def ok_at(z, A):
        WORK[0] += len(T)
        if WORK[0] > WORK_CAP:
            raise OverflowError
        for sg in product((1, -1), repeat=3):
            good = True
            for side in (-1, 1):
                known = {i: (side * (A[y] - A[z])) % m for i in range(3) for y in [sh(z, i, side * sg[i])] if y in cs and y in A}
                if not any(all(t[i] == v for i, v in known.items()) for t in T):
                    good = False
                    break
            if good:
                return True
        return False

    out = []

    nodes = [0]

    def rec(idx, A):
        nodes[0] += 1
        if nodes[0] > node_cap:
            raise OverflowError
        if len(out) >= cap:
            raise OverflowError
        if idx == len(core):
            out.append(tuple(A[x] for x in core))
            return
        x = core[idx]
        for v in ([0] if idx == 0 else range(m)):
            A[x] = v
            if ok_at(x, A) and all(ok_at(z, A) for z in nbrs[x] if z in A):
                rec(idx + 1, A)
            del A[x]

    try:
        rec(0, {})
    except OverflowError:
        return None, core
    return out, core


oc, ocore = octant_records(4, (1, 2, 4), 7)
oc_counts = None if oc is None else (len(oc), sum(is_spiral(v, ocore, 7) for v in oc))
check("if each core site may use its own octant, the seven letters are not rigid: the fixed octant carries the rigidity",
      oc_counts == (15024, 48),
      f"core of side 2: {oc_counts[0] if oc_counts else 'cap'} records, {oc_counts[1] if oc_counts else '-'} of them "
      "spirals (six assignments, eight sign patterns); with the octant fixed, 12")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
