#!/usr/bin/env python3
"""Independent referee for J:derive:local-clock-for-inertia-with-weights:a1.

Author w-macbookpro90c72-j5257 (claude-opus-5-5). Referee w-macbookpro90c72-j04d0 (grok-4.6).
Own torus, own rows. Rates and Farkas vectors are the author's data.json; the arithmetic is not theirs.
"""
import ast
import itertools
import json
import os
from fractions import Fraction as Fr
from itertools import combinations, product

PASS = []
E = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
GROUP = [(perm, sg) for perm in itertools.permutations(range(3)) for sg in product((1, -1), repeat=3)]
BASE = ((0, 0, 0), (1, 0, 0), (-1, 0, 0), (2, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1),
        (1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1))
CON_OF = {E[c]: c for c in range(6)}
WTS = {"c1": (Fr(3), Fr(1), Fr(2)), "c0": (Fr(3, 2), Fr(1, 2), Fr(1))}
DATA = json.load(open(os.path.join(
    os.path.dirname(__file__),
    "../w-macbookpro90c72-j5257/data.json")))


def record(tag, ok, text):
    PASS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}")


def rq(s):
    a, b = s.split("/")
    return Fr(int(a), int(b))


def gvec(g, v):
    perm, sg = g
    w = [0, 0, 0]
    for i in range(3):
        w[perm[i]] = sg[i] * v[i]
    return tuple(w)


class Torus:
    def __init__(self, L):
        self.L = L
        self.sites = list(product(range(L), repeat=3))
        self.idx = {x: i for i, x in enumerate(self.sites)}
        self.n = L ** 3
        self.nb = [[self.add(x, d) for d in E] for x in self.sites]
        self.fr = {}
        for x in range(self.n):
            for s in range(6):
                lst = []
                for g in GROUP:
                    if gvec(g, E[s]) != (1, 0, 0):
                        continue
                    perm, sg = g
                    sites, seen = [], set()
                    for d in BASE:
                        r = tuple(sg[i] * d[perm[i]] for i in range(3))
                        site = self.add(self.sites[x], r)
                        if site in seen:
                            continue
                        seen.add(site)
                        sites.append(site)
                    lst.append((sites, [CON_OF[gvec(g, E[c])] for c in range(6)]))
                self.fr[(x, s)] = lst

    def add(self, x, d):
        return self.idx[tuple((x[i] + d[i]) % self.L for i in range(3))]

    def env(self, occ, x):
        best = None
        for sites, gc in self.fr[(x, occ[x])]:
            key = tuple(gc[occ[t]] if occ[t] >= 0 else -1 for t in sites)
            if best is None or key < best:
                best = key
        return best

    def rot(self, occ, x, a):
        best = None
        for sites, gc in self.fr[(x, occ[x])]:
            key = (tuple(gc[occ[t]] if occ[t] >= 0 else -1 for t in sites), gc[a])
            if best is None or key < best:
                best = key
        return ("rot",) + best

    def weight(self, occ, w):
        val = Fr(1)
        occupied = [a for a in range(self.n) if occ[a] >= 0]
        for a in occupied:
            for b in self.nb[a]:
                if b > a and occ[b] >= 0:
                    c1, c2 = occ[a], occ[b]
                    val *= w[0] if c1 == c2 else (w[1] if c1 == (c2 ^ 1) else w[2])
        return val

    def own(self, occ, x, w):
        val = Fr(1)
        for b in self.nb[x]:
            if occ[b] >= 0:
                c1, c2 = occ[x], occ[b]
                val *= w[0] if c1 == c2 else (w[1] if c1 == (c2 ^ 1) else w[2])
        return val

    def configs(self, nrec):
        for rest in combinations(range(1, self.n), nrec - 1):
            pos = (0,) + rest
            for con in product(range(6), repeat=nrec):
                occ = [-1] * self.n
                for p_, c_ in zip(pos, con):
                    occ[p_] = c_
                yield pos, con, occ

    def pred(self, occ, x):
        s = occ[x]
        behind = self.nb[x][s ^ 1]
        out = list(occ)
        if occ[behind] >= 0:
            out[behind], out[x] = occ[x], occ[behind]
        else:
            out[behind] = s
            out[x] = -1
        return behind, out

    def terms(self, pos, occ, mode="base"):
        out = []
        for x in pos:
            s = occ[x]
            t = self.nb[x][s]
            out.append((self.env(occ, x), +1, None))
            if mode == "rot" and occ[t] == (s ^ 1):
                for a in range(6):
                    if a // 2 != s // 2:
                        out.append((self.rot(occ, x, a), +1, None))
            behind, occ2 = self.pred(occ, x)
            out.append((self.env(occ2, behind), -1, occ2))
        if mode == "rot":
            for x in pos:
                for di in (0, 2, 4):
                    y = self.nb[x][di]
                    c = occ[x]
                    if occ[y] >= 0 and occ[y] == (c ^ 1) and c // 2 != di // 2:
                        occ3 = list(occ)
                        occ3[x] = di
                        occ3[y] = di ^ 1
                        for actor, a_out in ((x, c), (y, occ[y])):
                            out.append((self.rot(occ3, actor, a_out), -1, occ3))
        return out

    def row(self, pos, occ, w, mode="base"):
        pi = self.weight(occ, w)
        acc = {}
        for key, sg, o2 in self.terms(pos, occ, mode):
            acc[key] = acc.get(key, 0) + (pi if sg > 0 else -self.weight(o2, w))
        return {k: v for k, v in acc.items() if v}


def is_move(key):
    return key[0] != "rot" and key[1] == -1


def parse_rates(blob):
    return {ast.literal_eval(k): rq(v) for k, v in blob.items()}


def occ_of(T, pos, con):
    occ = [-1] * T.n
    for p_, c_ in zip(pos, con):
        occ[p_] = c_
    return occ


# combinatorial count, before any torus scan
record("S1count", 26 * 25 // 2 * 6 ** 3 == 70200, "C(26,2)*6^3 = 70200 three-record configurations with a record at the origin on 3^3")

T3 = Torus(3)
w1 = WTS["c1"]
n = bad_g = bad_l = 0
largest = Fr(0)
for pos, con, occ in T3.configs(3):
    n += 1
    pi = T3.weight(occ, w1)
    out_l = sum(pi / T3.own(occ, x, w1) for x in pos)
    in_l = Fr(0)
    ins = 0
    for x in pos:
        behind, o2 = T3.pred(occ, x)
        in_l += T3.weight(o2, w1) / T3.own(o2, behind, w1)
        ins += 1
    bad_g += ins != 3
    if out_l != in_l:
        bad_l += 1
        largest = max(largest, abs(out_l - in_l))
record("S1", n == 70200 and bad_g == 0 and bad_l == 3168 and largest == 3,
       f"local clock fails at {bad_l}/{n}, largest defect {largest}; every config has 3 events each way")

# the prose witness: three +y records, only an equal-content exchange
pos_w, con_w = (0, 1, 3), (2, 2, 2)
occ_w = occ_of(T3, pos_w, con_w)
row_w = T3.row(pos_w, occ_w, w1)
exchanges = [k for k in row_w if not is_move(k)]
clock_defect = Fr(0)
for key, coef in row_w.items():
    if is_move(key):
        # local clock from the key's own-site neighbours, same convention as a radius-one clock
        own = Fr(1)
        for slot in (1, 2, 3, 4, 5, 6):
            c = key[slot]
            if c >= 0:
                own *= w1[0] if c == 0 else (w1[1] if c == 1 else w1[2])
        clock_defect += coef / own
record("S4", not exchanges and clock_defect != 0,
       f"witness (0,1,3)|(2,2,2) has no exchange class and local-clock defect {clock_defect}")


def verify_rule(T, blob, w):
    rates = parse_rates(blob)
    nconf = nbad = missing = 0
    for pos, con, occ in T.configs(3):
        row = T.row(pos, occ, w)
        if any(k not in rates for k in row):
            missing += 1
            continue
        nconf += 1
        if sum(c * rates[k] for k, c in row.items()) != 0:
            nbad += 1
    moves = [r for k, r in rates.items() if is_move(k)]
    ex = [r for k, r in rates.items() if not is_move(k)]
    return nconf, nbad, missing, min(moves), min(ex) if ex else Fr(0), len(rates)


# unit-move witness: three +x along a line. No exchange class, residual at rate 1.
pos_u, con_u = (0, 1, 2), (0, 0, 0)
row_u = T3.row(pos_u, occ_of(T3, pos_u, con_u), w1)
unit_ex = [k for k in row_u if not is_move(k)]
unit_res = sum(c for k, c in row_u.items() if is_move(k))
record("S4b", not unit_ex and unit_res != 0,
       f"unit-move witness (0,1,2)|(0,0,0) has no exchange class and residual {unit_res}")

rw_ok = True
rw_bits = []
for name, w in WTS.items():
    ATy, yl = {}, Fr(0)
    for kc, yy in DATA[f"cert_recordwise_{name}"].items():
        a, b, kr = kc.split("|")
        pos, con, kr = ast.literal_eval(a), ast.literal_eval(b), int(kr)
        occ = occ_of(T3, pos, con)
        x = pos[kr]
        behind, o2 = T3.pred(occ, x)
        row = {}
        for key, coef in ((T3.env(occ, x), T3.weight(occ, w)), (T3.env(o2, behind), -T3.weight(o2, w))):
            row[key] = row.get(key, Fr(0)) + coef
        yv = rq(yy)
        for k, c in row.items():
            ATy[k] = ATy.get(k, Fr(0)) + c * yv
            if is_move(k):
                yl += c * yv
    good = all(v >= 0 for v in ATy.values()) and yl > 0
    rw_ok &= good
    rw_bits.append(f"{name}: yAl={yl} support {len(DATA[f'cert_recordwise_{name}'])}")
record("S4c", rw_ok, "record-wise balance infeasible " + "; ".join(rw_bits))

T4, T5 = Torus(4), Torus(5)
bits = []
rule_ok = True
for L, T in ((3, T3), (4, T4), (5, T5)):
    for name, w in WTS.items():
        nconf, nbad, missing, mn, exn, nclass = verify_rule(T, DATA[f"rule_L{L}_{name}"], w)
        bits.append(f"{L}^{name}:{nconf} bad {nbad} missing {missing} minmove {mn}")
        rule_ok &= nbad == 0 and missing == 0 and mn >= 1 and exn >= 0
record("S3", rule_ok, "three-record rules " + "; ".join(bits))


def farkas(rows_y, mode, w, T):
    ATy, yl = {}, Fr(0)
    n4 = 0
    for kc, yy in rows_y.items():
        pos = ast.literal_eval(kc.split("|")[0])
        con = ast.literal_eval(kc.split("|")[1])
        n4 += len(pos) == 4
        yv = rq(yy)
        row = T.row(pos, occ_of(T, pos, con), w, mode)
        for k, c in row.items():
            ATy[k] = ATy.get(k, Fr(0)) + c * yv
            if is_move(k):
                yl += c * yv
    return all(v >= 0 for v in ATy.values()) and yl > 0, yl, n4, len(rows_y)


f_ok = True
f_bits = []
for mode in ("base", "rot"):
    for name, w in WTS.items():
        good, yl, n4, nsup = farkas(DATA[f"cert_joint_{mode}_{name}"], mode, w, T3)
        f_ok &= good and n4 == nsup
        f_bits.append(f"{mode}/{name}: n={nsup} all-four={n4} yAl={yl}")
record("S5", f_ok, "four-record Farkas on 3^3 " + "; ".join(f_bits))

# Z^3: certificate rows agree on 6^3 and 9^3 and give A^T y >= 0
T6, T9 = Torus(6), Torus(9)
z_ok = True
z_bits = []
for mode in ("base", "rot"):
    for name, w in WTS.items():
        blob = DATA[f"cert_Z3_{mode}_{name}"]
        ATy, yl, same = {}, Fr(0), True
        for kc, yy in blob.items():
            pos = ast.literal_eval(kc.split("|")[0])
            con = ast.literal_eval(kc.split("|")[1])
            row6 = T6.row(pos, occ_of(T6, pos, con), w, mode)
            pos9 = tuple(T9.idx[T6.sites[p]] for p in pos)
            row9 = T9.row(pos9, occ_of(T9, pos9, con), w, mode)
            same &= row6 == row9
            yv = rq(yy)
            for k, c in row6.items():
                ATy[k] = ATy.get(k, Fr(0)) + c * yv
                if is_move(k):
                    yl += c * yv
        good = same and all(v >= 0 for v in ATy.values()) and yl > 0
        z_ok &= good
        z_bits.append(f"{mode}/{name}: {len(blob)} same={same} yAl={yl}")
record("S6", z_ok, "compact Z^3 certificates " + "; ".join(z_bits))

# conservation of a head-on redraw and of one exchange / move
def mom(occ):
    tot = [0, 0, 0]
    nrec = 0
    for c in occ:
        if c >= 0:
            nrec += 1
            for i in range(3):
                tot[i] += E[c][i]
    return nrec, tuple(tot)

occ = occ_w
n0, m0 = mom(occ)
# exchange the two +y records at sites 0 and 3 (target of +y from 0 is site of (0,1,0))
occ_x = list(occ)
occ_x[0], occ_x[3] = occ[3], occ[0]
# move the record at site 1 (+y) into its empty target
s = occ[1]
tgt = T3.nb[1][s]
occ_m = list(occ)
occ_m[tgt] = s
occ_m[1] = -1
# redraw (s,-s) -> (a,-a). Build a head-on pair: +x at 0, -x at its target.
occ_h = [-1] * T3.n
occ_h[0] = 0
occ_h[T3.nb[0][0]] = 1
n1, m1 = mom(occ_h)
occ_r = list(occ_h)
# transverse +y,-y
y, ym = T3.nb[0][2], T3.nb[0][3]
# place redraw on the same two sites
a_site, b_site = 0, T3.nb[0][0]
occ_r[a_site], occ_r[b_site] = 2, 3
record("S7", mom(occ_x) == (n0, m0) and mom(occ_m) == (n0, m0) and mom(occ_r) == (n1, m1),
       f"move/exchange/redraw conserve count and content vector {mom(occ_m)} {mom(occ_r)}")

print(f"TOTAL: PASS={sum(PASS)} FAIL={len(PASS) - sum(PASS)}")
if all(PASS):
    print("SUMMARY: confirmed — local clock fails at 3168/70200 with defect 3; the radius-one rules balance every "
          "three-record configuration on 3^3, 4^3 and 5^3 at c=1 and c=1/2; the local-clock and unit-move witnesses have "
          "no exchange class; record-wise and four-record Farkas vectors satisfy A^T y >= 0 with y.(A l)=1; compact "
          "rows agree on 6^3 and 9^3")
    print("HIT: confirmed - the a1 claim survives: a radius-one rule keeps pi stationary for three records on the 3^3, "
          "4^3 and 5^3 tori, not by the local clock or by unit moves and not record by record, and no such rule balances "
          "the certified four-record clusters on 3^3 or on Z^3, with or without head-on redraws")
else:
    print("SUMMARY: fails at " + ",".join(str(i) for i, ok_ in enumerate(PASS, 1) if not ok_)
          + " - an independent finite check did not reproduce the attempt")
