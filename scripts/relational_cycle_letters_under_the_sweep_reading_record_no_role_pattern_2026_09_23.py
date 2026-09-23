#!/usr/bin/env python3
"""Relational cycle letters under the sweep reading record no role pattern.

Open PR #8752 found that relational letters in four-angle cycles are rigid
under the static reading, with its global octant: every static record is a
cycle spiral, and each site reads its position mod 4 on every line, hence
its role. The static reading reads both the back and the forward neighbours
of a site. The sweep reading of open PR #8743 reads only the three back
neighbours: each core site is a covariant completion of x - e_i, i = 1, 2, 3.
Here the completion is the cycle rule's back half, in the planar form of
open PR #8729: the three back differences are signed angles with one common
sense, from the three different cycles.

This runner exhibits a witness of flexibility on the core of side 3.

A. The letters of open PR #8752 decode every difference, and the sweep rule
   accepts and rejects as declared.
B. A search over core values, candidates in the table's order, finds sweep
   records on the side-3 core; the first is completed on the faces, and
   every core site of the completed record satisfies the sweep rule.
C. The witness is not a cycle spiral: its core values differ from all 768.
D. The witnesses break the static reading at (2, 2, 2), the core site whose
   six neighbours all lie in the core, whatever the face values.
E. Its phase readout is not the position mod 4 plus one global phase, so
   the role pattern is not read from it.
F. The first 40 sweep records found are distinct, and none is a spiral.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys

PASS = FAIL = 0


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
C = 3
CORE = list(itertools.product(range(1, C + 1), repeat=3))
CORESET = set(CORE)


def nb(y, i, sg):
    return tuple(u + sg * (k == i) for k, u in enumerate(y))


def back_ok(decs):
    """sweep rule: known back differences share one sense and use distinct cycles."""
    decs = [d for d in decs if d]
    return len({d[0] for d in decs}) <= 1 and len({d[1] for d in decs}) == len(decs)


def static_ok(Bd, Fd):
    """static cycle rule of open PR #8752 at a site with all six differences known."""
    if None in Bd or None in Fd:
        return False
    senses = {d[0] for d in Bd + Fd}
    lines = all(Bd[i][1] == Fd[i][1] and (Fd[i][2] - Bd[i][2]) % 4 == 1 for i in range(3))
    return len(senses) == 1 and lines and len({d[1] for d in Bd}) == 3


def sweep_records(limit, node_cap=3_400_000):
    order = sorted((x for x in CORE if x != (1, 1, 1)), key=lambda x: (sum(x), x))
    val, recs, nodes = {(1, 1, 1): 0}, [], [0]

    def ok(y):
        decs = []
        for i in range(3):
            z = nb(y, i, -1)
            if z in val and z in CORESET:
                d = TAB.get((val[y] - val[z]) % M)
                if d is None:
                    return False
                decs.append(d)
        return back_ok(decs)

    def rec(k):
        if len(recs) >= limit or nodes[0] >= node_cap:
            return
        nodes[0] += 1
        if k == len(order):
            recs.append(dict(val))
            return
        z = order[k]
        y = [nb(z, i, -1) for i in range(3) if nb(z, i, -1) in CORESET][0]
        for r in TAB:
            val[z] = (val[y] + r) % M
            if ok(z):
                rec(k + 1)
            del val[z]

    rec(0)
    return recs, nodes[0]


def spirals_core():
    out = set()
    for perm in itertools.permutations(range(3)):
        for s in (1, -1):
            for ph in itertools.product(range(4), repeat=3):
                rec = []
                for x in CORE:
                    v = sum(sum(CYC[perm[i]][(ph[i] + u - 1) % 4] for u in range(1, x[i])) for i in range(3))
                    rec.append((s * v) % M)
                out.add(tuple(rec))
    return out


def complete_faces(core_vals):
    """give every low face x - e_i of a core site a value that completes its back triple."""
    val = dict(core_vals)
    for x in CORE:
        known = [TAB[(val[x] - val[nb(x, i, -1)]) % M] for i in range(3) if nb(x, i, -1) in CORESET]
        s = known[0][0] if known else 1
        free = [j for j in range(3) if j not in {d[1] for d in known}]
        for i in range(3):
            z = nb(x, i, -1)
            if z not in CORESET:
                j = free.pop(0)
                val[z] = (val[x] - s * CYC[j][0]) % M
    return val


def spiral_value(x):
    """the control spiral: axis i carries cycle i, sense +1, phase 0 on the step from x_i = 1."""
    return sum(sum(CYC[i][(u - 1) % 4] for u in range(1, x[i])) if x[i] >= 1 else -CYC[i][3] for i in range(3)) % M


def back_phases(value):
    """(axis, back-step phase minus position mod 4) over the core, for a value function."""
    out = set()
    for x in CORE:
        for i in range(3):
            d = TAB.get((value(x) - value(nb(x, i, -1))) % M)
            if d:
                out.add((i, (d[2] - x[i]) % 4))
    return out


print("== A. The letters ==")
check("the letters of open PR #8752 decode every difference: 24 distinct nonzero signed angles, cycles summing to 0",
      TAB is not None and len(TAB) == 24 and all(sum(c) % M == 0 for c in CYC))
one_sense = [TAB[CYC[j][1] % M] for j in range(3)]
mixed = [TAB[CYC[0][1] % M], TAB[(-CYC[1][1]) % M], TAB[CYC[2][1] % M]]
repeat = [TAB[CYC[0][1] % M], TAB[CYC[0][2] % M], TAB[CYC[2][1] % M]]
check("the sweep rule accepts one sense with three cycles, and rejects mixed senses or a repeated cycle",
      back_ok(one_sense) and not back_ok(mixed) and not back_ok(repeat))
print()

print("== B. A sweep record on the core of side 3 ==")
RECS, NODES = sweep_records(40)
W = complete_faces(RECS[0]) if RECS else {}
sweep_holds = bool(W) and all(back_ok([TAB.get((W[x] - W[nb(x, i, -1)]) % M) for i in range(3)])
                              and None not in [TAB.get((W[x] - W[nb(x, i, -1)]) % M) for i in range(3)] for x in CORE)
check("the first sweep record, completed on the faces, satisfies the sweep rule at all 27 core sites",
      sweep_holds, f"{len(RECS)} records found within {NODES} search nodes")
print()

print("== C. Not a spiral ==")
SP = spirals_core()
wcore = tuple(W[x] for x in CORE) if W else ()
CTRL = tuple((spiral_value(x) - spiral_value((1, 1, 1))) % M for x in CORE)
check("the witness is not one of the 768 cycle spirals, a set that contains the control spiral",
      bool(W) and len(SP) == 768 and wcore not in SP and CTRL in SP)
print()

print("== D. The static reading fails on it ==")
X0 = (2, 2, 2)


def static_at_centre(r):
    Bd = [TAB.get((r[X0] - r[nb(X0, i, -1)]) % M) for i in range(3)]
    Fd = [TAB.get((r[nb(X0, i, 1)] - r[X0]) % M) for i in range(3)]
    return static_ok(Bd, Fd)


nfail = sum(1 for r in RECS if not static_at_centre(r))
cB = [TAB[(spiral_value(X0) - spiral_value(nb(X0, i, -1))) % M] for i in range(3)]
cF = [TAB[(spiral_value(nb(X0, i, 1)) - spiral_value(X0)) % M] for i in range(3)]
cF_switched = [(cF[0][0], 1, cF[0][2])] + cF[1:]
ctrl_ok = static_ok(cB, cF) and not static_ok(cB, cF_switched)
check("at (2, 2, 2), whose six neighbours all lie in the core, all 40 records break the static cycle rule",
      len(RECS) == 40 and nfail == 40 and ctrl_ok,
      "so none extends to a static record, whatever the face values; the rule accepts the control spiral there")
print()

print("== E. No role readout ==")
phases = back_phases(lambda x: W[x]) if W else set()
per_axis = {i: {p for (a, p) in phases if a == i} for i in range(3)}


ctrl = back_phases(spiral_value)
check("the back-step phases are not the position mod 4 plus one global phase on every line, while a spiral's are",
      any(len(v) > 1 for v in per_axis.values()) and all(len({p for (a, p) in ctrl if a == i}) == 1 for i in range(3)),
      f"witness phases per axis: {[len(per_axis[i]) for i in range(3)]}; spiral control: 1, 1, 1")
print()

print("== F. Many witnesses ==")
cores = {tuple(r[x] for x in CORE) for r in RECS}
check("the first 40 sweep records found are distinct and none is a spiral",
      len(RECS) == 40 and len(cores) == 40 and not (cores & SP))
print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
