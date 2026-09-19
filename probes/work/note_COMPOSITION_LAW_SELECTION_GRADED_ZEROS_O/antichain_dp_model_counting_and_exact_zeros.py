#!/usr/bin/env python3
"""Probe: COMPOSITION_LAW_SELECTION_GRADED_ZEROS_ORDER_BLIND_RULES_BOUNDED_THEOREM_NOTE_2026-09-13.

Machinery disjoint from the runner (subset enumeration of rules with a cap):

 Z  own Jordan-Wigner graded hopping builder; the ground vectors of the four
    sectors computed EXACTLY as the kernel of H - E over Q(sqrt 2) (own
    Fraction-pair arithmetic and elimination); energies, simplicity and the gap
    >= 1/4 cross-checked by float spectra; the zero sets against Theorem 1;
    the ungraded matrices' ground vectors strictly positive (falsifier 3).
 X  the fixed-point character mechanism with the Jordan-Wigner permutation
    sign: predicted zeros 3/3, 0/2, 12/12, 4/8 (falsifier 4).
 R  sequential support rules under exists-order semantics, counted WITHOUT
    enumerating orders or rule subsets: for each pattern, a DP over formed-site
    subsets yields the antichain of minimal step-class sets over all formation
    orders; a rule F reproduces a sector iff F hits every antichain member of
    every zero pattern and misses some member for every nonzero pattern; the
    rules are counted by a backtracking model counter with two-sided pruning
    and the closed 2^free completion.  Checked: Theorem 5 (fixed-N counts,
    used-class counts, forced/never classes, both conventions), Theorem 6
    (the joint counts 160, 1021, 384, 189, 0, 0 and 39, 0, 0, with forced/never
    classes) and falsifiers 1 and 2 (the two zero counts).
 B  beyond the note: the boundary-state class (v, u, e, m) counted exactly for the
    same-cluster pair (the note records existence at cap one).

Prints SUMMARY: lines; HIT: only when a falsifier of the note fires.
"""
import itertools
import math
import sys
import time
from fractions import Fraction as Fr

import numpy as np

HITS = []


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


# ------------------------------------------------------------------------------------------ clusters
def cluster(name):
    if name == "2x3":
        sites = [(r, c) for r in range(2) for c in range(3)]
    elif name == "3x3":
        sites = [(r, c) for r in range(3) for c in range(3)]
    else:
        sites = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
    n = len(sites)
    bonds = [(i, j) for i in range(n) for j in range(i + 1, n)
             if sum(abs(a - b) for a, b in zip(sites[i], sites[j])) == 1]
    nb = [[j for j in range(n) if (min(i, j), max(i, j)) in set(bonds)] for i in range(n)]
    return sites, bonds, nb


SECTORS = [("2x3", 2), ("2x3", 3), ("cube", 4), ("3x3", 3)]
LABEL = {("2x3", 2): "2x3 N=2", ("2x3", 3): "2x3 N=3", ("cube", 4): "cube N=4", ("3x3", 3): "3x3 N=3"}


def hopping(name, N, graded=True):
    sites, bonds, nb = cluster(name)
    n = len(sites)
    pats = [frozenset(c) for c in itertools.combinations(range(n), N)]
    idx = {p: t for t, p in enumerate(pats)}
    H = np.zeros((len(pats), len(pats)), dtype=np.int64)
    for p in pats:
        for (i, j) in bonds:
            for a, b in ((i, j), (j, i)):
                if a in p and b not in p:
                    q = (p - {a}) | {b}
                    k = sum(1 for s in p if min(a, b) < s < max(a, b))
                    H[idx[q], idx[p]] += -((-1) ** k) if graded else -1
    return pats, idx, H


# Q(sqrt2): (a, b) = a + b sqrt2
def qadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def qsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def qmul(x, y):
    return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def qinv(x):
    d = x[0] * x[0] - 2 * x[1] * x[1]
    return (x[0] / d, -x[1] / d)


def qzero(x):
    return x[0] == 0 and x[1] == 0


def exact_kernel(H, E):
    """kernel of H - E over Q(sqrt2); returns list of basis vectors"""
    n = H.shape[0]
    A = [[(Fr(int(H[i, j])) - (E[0] if i == j else 0), (-E[1] if i == j else Fr(0))) for j in range(n)] for i in range(n)]
    piv = []
    r = 0
    for c in range(n):
        pr = next((i for i in range(r, n) if not qzero(A[i][c])), None)
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        inv = qinv(A[r][c])
        A[r] = [qmul(v, inv) for v in A[r]]
        for i in range(n):
            if i != r and not qzero(A[i][c]):
                f = A[i][c]
                A[i] = [qsub(a, qmul(f, b)) for a, b in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fc in free:
        v = [(Fr(0), Fr(0))] * n
        v[fc] = (Fr(1), Fr(0))
        for i, pc in enumerate(piv):
            v[pc] = (-A[i][fc][0], -A[i][fc][1])
        basis.append(v)
    return basis


ENERGY = {("2x3", 2): (Fr(-2), Fr(-1)), ("2x3", 3): (Fr(-1), Fr(-2)), ("cube", 4): (Fr(-6), Fr(0)), ("3x3", 3): (Fr(0), Fr(-4))}
ZEROS_NOTE = {
    ("2x3", 2): [{0, 3}, {1, 4}, {2, 5}],
    ("2x3", 3): [{0, 1, 2}, {3, 4, 5}],
    ("cube", 4): [{0, 1, 2, 3}, {4, 5, 6, 7}, {0, 1, 4, 5}, {2, 3, 6, 7}, {0, 2, 4, 6}, {1, 3, 5, 7}, {0, 1, 6, 7}, {2, 3, 4, 5},
                  {0, 2, 5, 7}, {1, 3, 4, 6}, {0, 3, 4, 7}, {1, 2, 5, 6}],
    ("3x3", 3): [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}],
}


def run_Z():
    print("=" * 78)
    print("Z  exact ground vectors over Q(sqrt 2)")
    data = {}
    for sec in SECTORS:
        name, N = sec
        pats, idx, H = hopping(name, N)
        E = ENERGY[sec]
        w = np.linalg.eigvalsh(H.astype(float))
        Ef = float(E[0]) + float(E[1]) * math.sqrt(2)
        basis = exact_kernel(H, E)
        v = basis[0] if len(basis) == 1 else None
        zeros = sorted(sorted(p) for p, a in zip(pats, v) if qzero(a)) if v else None
        signs = (sum(1 for a in v if not qzero(a) and float(a[0]) + float(a[1]) * math.sqrt(2) > 0),
                 sum(1 for a in v if not qzero(a) and float(a[0]) + float(a[1]) * math.sqrt(2) < 0),
                 sum(1 for a in v if qzero(a))) if v else None
        gap = w[1] - w[0]
        ok_e = abs(w[0] - Ef) < 1e-10 and len(basis) == 1 and gap >= 0.25 - 1e-12
        ok_z = zeros == sorted(sorted(z) for z in ZEROS_NOTE[sec])
        pu, iu, Hu = hopping(name, N, graded=False)
        wu, Vu = np.linalg.eigh(Hu.astype(float))
        g = Vu[:, 0] * np.sign(Vu[0, 0])
        perron = bool(np.all(g > 1e-12))
        data[sec] = (pats, idx, H, v, set(frozenset(z) for z in zeros) if zeros else set(), signs)
        print(f"  {LABEL[sec]}: dim {len(pats)}, E = {E[0]} + {E[1]}sqrt2 = {Ef:.10f} vs lowest float eigenvalue {w[0]:.10f}; "
              f"exact kernel dim {len(basis)}; gap {gap:.4f}; zeros {len(zeros) if zeros else None} match Theorem 1: {ok_z}; "
              f"signed counts (+,-,0) {signs}; ungraded ground vector strictly positive: {perron}")
        if not ok_e or not ok_z:
            hit(f"{LABEL[sec]}: energy/gap/zero set differs from Theorem 1")
        if not perron:
            hit(f"{LABEL[sec]}: the ungraded ground vector has a zero component")
    return data


def perm_sign(seq):
    s = 1
    seq = list(seq)
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                s = -s
    return s


def run_X(data):
    print("=" * 78)
    print("X  fixed-point character mechanism with the Jordan-Wigner sign")
    out = {}
    for sec in SECTORS:
        name, N = sec
        sites, bonds, nb = cluster(name)
        n = len(sites)
        bset = set(bonds)
        pats, idx, H, v, zeros, _ = data[sec]
        vf = [float(a[0]) + float(a[1]) * math.sqrt(2) for a in v]
        auts = [s for s in itertools.permutations(range(n))
                if all((min(s[i], s[j]), max(s[i], s[j])) in bset for i, j in bonds)]
        predicted = set()
        for s in auts:
            # character: v(s p) sgn = chi v(p) for any p with v(p) != 0
            p0 = next(p for p, a in zip(pats, vf) if abs(a) > 1e-9)
            sp_ = frozenset(s[i] for i in p0)
            sg0 = perm_sign([s[i] for i in sorted(p0)])
            chi = round(vf[idx[sp_]] * sg0 / vf[idx[p0]])
            for p in pats:
                if frozenset(s[i] for i in p) == p:
                    sg = perm_sign([s[i] for i in sorted(p)])
                    if chi * sg == -1:
                        predicted.add(p)
        got = len(predicted & zeros)
        out[sec] = (len(auts), got, len(zeros), len(predicted - zeros))
        print(f"  {LABEL[sec]}: {len(auts)} bond-preserving permutations; character-predicted zeros {got} of {len(zeros)} "
              f"(predicted non-zeros: {len(predicted - zeros)})")
    expect = {("2x3", 2): 3, ("2x3", 3): 0, ("cube", 4): 12, ("3x3", 3): 4}
    if any(out[s][1] != expect[s] or out[s][3] != 0 for s in SECTORS):
        hit(f"character-zero counts differ from Theorem 2: {dict((LABEL[s], out[s][1]) for s in SECTORS)}")
    return out


# ------------------------------------------------------------------------------------------ rules
def cls(conv, v, i, formed, pat, nb):
    rec = [j for j in nb[i] if j in formed]
    m = sum(1 for j in rec if j in pat)
    if conv == "unrec":
        return (v, len(rec), m)
    if conv == "bstate":                     # (v, u, e, m): unrecorded, recorded-empty, recorded-occupied in the window
        return (v, len(nb[i]) - len(rec), len(rec) - m, m)
    return (v, len(nb[i]) - len(rec), m)


def antichain_min(sets):
    sets = sorted(set(sets), key=lambda b: bin(b).count("1"))
    out = []
    for s in sets:
        if not any((o & s) == o for o in out):
            out.append(s)
    return out


def signatures(name, N, conv, pats, classidx):
    """for every pattern: the antichain of minimal class-bitmasks over all formation orders (DP over formed subsets)"""
    sites, bonds, nb = cluster(name)
    n = len(sites)
    out = {}
    for pat in pats:
        layer = {0: [0]}                                 # formed-set bitmask -> antichain of class masks
        for size in range(n):
            nxt = {}
            for S, ach in layer.items():
                formed = {i for i in range(n) if S >> i & 1}
                for i in range(n):
                    if S >> i & 1:
                        continue
                    c = cls(conv, 1 if i in pat else 0, i, formed, pat, nb)
                    if c not in classidx:
                        classidx[c] = len(classidx)
                    bit = 1 << classidx[c]
                    T = S | (1 << i)
                    nxt.setdefault(T, []).extend(a | bit for a in ach)
            layer = {T: antichain_min(v) for T, v in nxt.items()}
        out[pat] = layer[(1 << n) - 1]
    return out


def count_rules(constraints):
    """constraints: list of (antichain, is_zero).  Count F subset of used classes such that every zero pattern's
    antichain members all meet F and every nonzero pattern has a member disjoint from F.  Also forced/never masks."""
    used = 0
    for ach, _ in constraints:
        for s in ach:
            used |= s
    bits = [b for b in range(used.bit_length()) if used >> b & 1]
    # order variables by frequency
    freq = {b: sum(1 for ach, _ in constraints for s in ach if s >> b & 1) for b in bits}
    order = sorted(bits, key=lambda b: -freq[b])
    total = [0]
    forced = [used]
    never = [used]

    def status(Fb, Ab):
        """-1 violated, 0 open, 1 all decided"""
        decided = True
        for ach, is_zero in constraints:
            if is_zero:
                # realisable if some member entirely allowed -> violation; decided if every member hits F
                if any((s & ~Ab) == 0 for s in ach):
                    return -1
                if not all(s & Fb for s in ach):
                    decided = False
            else:
                if all(s & Fb for s in ach):
                    return -1
                if not any((s & ~Ab) == 0 for s in ach):
                    decided = False
        return 1 if decided else 0

    def rec(k, Fb, Ab):
        st = status(Fb, Ab)
        if st < 0:
            return
        if st == 1 or k == len(order):
            free = [b for b in order[k:]]
            total[0] += 1 << len(free)
            # forced: classes in every solution; never: classes in no solution
            freemask = sum(1 << b for b in free)
            forced[0] &= Fb                                  # free classes can be absent -> not forced
            never[0] &= ~(Fb | freemask)                     # free classes can be present -> not never
            return
        b = order[k]
        rec(k + 1, Fb | (1 << b), Ab)
        rec(k + 1, Fb, Ab | (1 << b))
    rec(0, 0, 0)
    return total[0], len(bits), (forced[0] if total[0] else 0), (never[0] if total[0] else 0), used


def names(mask, inv):
    return " ".join("".join(str(x) for x in inv[b]) for b in range(mask.bit_length()) if mask >> b & 1)


def run_R(data):
    print("=" * 78)
    print("R  sequential support rules: antichain DP + model counting")
    res = {}
    expect_fixed = {"unrec": {("2x3", 2): 476, ("2x3", 3): 201, ("cube", 4): 8750, ("3x3", 3): 421},
                    "empty": {("2x3", 2): 782, ("2x3", 3): 2607, ("cube", 4): 8750, ("3x3", 3): 1116}}
    expect_used = {"unrec": {("2x3", 2): 16, ("2x3", 3): 18, ("cube", 4): 20, ("3x3", 3): 26},
                   "empty": {("2x3", 2): 16, ("2x3", 3): 19, ("cube", 4): 20, ("3x3", 3): 26}}
    expect_joint = {"unrec": {("2x3N2", "cube", "3x3"): 160, ("2x3N2", "cube"): 1021, ("2x3N2", "3x3"): 384, ("cube", "3x3"): 189,
                              ("2x3N2", "2x3N3"): 0, ("2x3N2", "2x3N3", "cube", "3x3"): 0},
                    "empty": {("2x3N2", "2x3N3"): 39, ("2x3N2", "cube", "3x3"): 0, ("2x3N2", "2x3N3", "cube", "3x3"): 0}}
    key = {"2x3N2": ("2x3", 2), "2x3N3": ("2x3", 3), "cube": ("cube", 4), "3x3": ("3x3", 3)}
    for conv in ("unrec", "empty"):
        classidx = {}
        sigs = {}
        for sec in SECTORS:
            name, N = sec
            pats = data[sec][0]
            sigs[sec] = signatures(name, N, conv, pats, classidx)
        inv = {i: c for c, i in classidx.items()}
        cons = {sec: [(sigs[sec][p], p in data[sec][4]) for p in data[sec][0]] for sec in SECTORS}
        for sec in SECTORS:
            t0 = time.time()
            cnt, nused, fo, nv, used = count_rules(cons[sec])
            res[(conv, "fixed", sec)] = (cnt, nused, names(fo, inv), names(nv, inv))
            ok = cnt == expect_fixed[conv][sec] and nused == expect_used[conv][sec]
            print(f"  {conv:5s} {LABEL[sec]}: rules {cnt} (note {expect_fixed[conv][sec]}), used classes {nused} "
                  f"(note {expect_used[conv][sec]}); forced [{names(fo, inv)}]; never [{names(nv, inv)}]  ({time.time() - t0:.1f}s)")
            if not ok:
                hit(f"{conv} {LABEL[sec]}: fixed-N rule count {cnt} / used classes {nused} differ from Theorem 5")
        for combo, exp in expect_joint[conv].items():
            t0 = time.time()
            cs = []
            for kk in combo:
                cs += cons[key[kk]]
            cnt, nused, fo, nv, used = count_rules(cs)
            res[(conv, "joint", combo)] = (cnt, nused, names(fo, inv), names(nv, inv))
            print(f"  {conv:5s} joint {'+'.join(combo)}: rules {cnt} (note {exp}); used classes {nused}; forced [{names(fo, inv)}]; "
                  f"never [{names(nv, inv)}]  ({time.time() - t0:.1f}s)")
            if cnt != exp:
                if exp == 0 and ((conv == "unrec" and combo == ("2x3N2", "2x3N3")) or (conv == "empty" and combo == ("2x3N2", "cube", "3x3"))):
                    hit(f"falsifier fires: {conv} joint {'+'.join(combo)} admits {cnt} particle-number-blind rules")
                else:
                    hit(f"{conv} joint {'+'.join(combo)}: count {cnt} differs from Theorem 6 ({exp})")
    return res


def run_B(data):
    print("=" * 78)
    print("B  boundary-state class (v, u, e, m): full counts beyond the note's existence remark")
    classidx = {}
    cons = {}
    for sec in (("2x3", 2), ("2x3", 3)):
        name, N = sec
        sig = signatures(name, N, "bstate", data[sec][0], classidx)
        cons[sec] = [(sig[p], p in data[sec][4]) for p in data[sec][0]]
    pair, npair, _, _, _ = count_rules(cons[("2x3", 2)] + cons[("2x3", 3)])
    print(f"  2x3 N=2 + N=3 jointly: {pair} boundary-state rules over {npair} used classes (note: at least one found at cap one)")
    if pair < 1:
        hit("the boundary-state existence remark fails (no rule for the same-cluster pair)")
    return pair, npair


def main():
    t0 = time.time()
    data = run_Z()
    summary("Z exact Q(sqrt2) ground vectors: " + "; ".join(
        f"{LABEL[s]}: kernel dim 1, zeros {len(data[s][4])}, (+,-,0) {data[s][5]}" for s in SECTORS)
        + "; energies/gaps and ungraded Perron positivity as stated")
    xo = run_X(data)
    summary("X character mechanism: " + ", ".join(f"{LABEL[s]}: {xo[s][1]}/{xo[s][2]} (|Aut| {xo[s][0]})" for s in SECTORS))
    res = run_R(data)
    summary("R fixed-N counts (unrec/empty): " + "; ".join(
        f"{LABEL[s]}: {res[('unrec', 'fixed', s)][0]}/{res[('empty', 'fixed', s)][0]} "
        f"(used {res[('unrec', 'fixed', s)][1]}/{res[('empty', 'fixed', s)][1]})" for s in SECTORS))
    summary("R joint counts: " + "; ".join(f"{c} {'+'.join(k)}: {v[0]}" for (c, t, k), v in res.items() if t == "joint")
            + "; falsifiers 1 and 2 (unrec 2x3 pair, empty discriminator triple): "
            + f"{res[('unrec', 'joint', ('2x3N2', '2x3N3'))][0]} and {res[('empty', 'joint', ('2x3N2', 'cube', '3x3'))][0]} rules")
    bp, bnp = run_B(data)
    summary(f"B boundary-state class (beyond the note's existence remark): the same-cluster pair admits exactly {bp} rules over "
            f"{bnp} used classes")
    print("=" * 78)
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
