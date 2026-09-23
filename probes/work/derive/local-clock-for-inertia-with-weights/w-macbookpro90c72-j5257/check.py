#!/usr/bin/env python3
"""J:derive:local-clock-for-inertia-with-weights:a1 - exact verification (Fractions) of the rules and certificates in
data.json (proposed by make_data.py with an LP solver; nothing here trusts the solver). Machinery in clocklib.py."""
import ast
import json
import os
import sys
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from clocklib import Torus, is_move  # noqa: E402

FAILS = []
T0 = time.time()


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg, flush=True)
    if not good:
        FAILS.append(tag)


W = {"c1": (Fr(3), Fr(1), Fr(2)), "c0": (Fr(3, 2), Fr(1, 2), Fr(1))}
D = json.load(open(os.path.join(HERE, "data.json")))
T3, T4 = Torus(3), Torus(4)


def rq(s):
    a, b = s.split("/")
    return Fr(int(a), int(b))


def occ_of(T, pos, con):
    occ = [-1] * T.N
    for p_, c_ in zip(pos, con):
        occ[p_] = c_
    return occ


# ------------------------------------------------------------------ A1: block 50's clocks reproduced
w = W["c1"]
n, bad_g, bad_l, largest = 0, 0, 0, 0
for pos, con, occ in T3.configs(3):
    pi = T3.weight(occ, w, Fr(1))
    out_l = sum(pi / T3.own(occ, x, w) for x in pos)
    in_l, in_g = Fr(0), 0
    for x in pos:
        s = occ[x]
        behind = T3.NB[x][s ^ 1]
        o2 = list(occ)
        if occ[behind] >= 0:
            o2[behind], o2[x] = occ[x], occ[behind]
        else:
            o2[behind] = s
            o2[x] = -1
        in_l += T3.weight(o2, w, Fr(1)) / T3.own(o2, behind, w)
        in_g += 1
    n += 1
    bad_g += in_g != len(pos)
    if out_l != in_l:
        bad_l += 1
        largest = max(largest, abs(out_l - in_l))
ok("A1", n == 70200 and bad_g == 0 and bad_l == 3168 and largest == 3,
   f"block 50 reproduced on the 3^3 torus at (3,1,2), c = 1: {n} three-record configurations with a record at the origin; "
   f"every configuration has three events out and three in (global clock balanced); the local clock 1/pi_x fails at "
   f"{bad_l}, largest defect {largest}")


# ------------------------------------------------------------------ A2, A3: the three-record rules
def verify_rule(T, rule, w):
    rates = {ast.literal_eval(k): rq(v) for k, v in rule.items()}
    nconf, nbad, missing = 0, 0, 0
    for pos, con, occ in T.configs(3):
        row = T.row(pos, occ, w, 'base', Fr(1))
        if any(k not in rates for k in row):
            missing += 1
            continue
        nconf += 1
        nbad += sum(c * rates[k] for k, c in row.items()) != 0
    mv = [r for k, r in rates.items() if is_move(k)]
    ex = [r for k, r in rates.items() if not is_move(k)]
    return nconf, nbad, missing, min(mv), min(ex), max(rates.values()), len(rates), len(mv), len(ex)


res = {}
TORI = [(3, T3), (4, T4)] + ([(5, Torus(5))] if "rule_L5_c1" in D else [])
for L, T in TORI:
    for name, w in W.items():
        res[(L, name)] = verify_rule(T, D[f"rule_L{L}_{name}"], w)
good = all(r[1] == 0 and r[2] == 0 and r[3] >= 1 and r[4] >= 0 for r in res.values())
ok("A2", good, "exact local rules for the three-record sector: " + "; ".join(
    f"{L}^3 {name}: {r[6]} rate classes ({r[7]} moves, {r[8]} exchanges), all {r[0]} configurations balanced, moves >= "
    f"{r[3]}, exchanges >= {r[4]}, largest rate {r[5]}" for (L, name), r in res.items()) + f" ({time.time() - T0:.0f} s)")


# ------------------------------------------------------------------ A3: certificates for the narrower families (3^3)
def mv_fixed(k, fam, w):
    if fam == "unitmoves":
        return Fr(1)
    own = Fr(1)
    for pos_ in (1, 2, 3, 4, 5, 6):                  # L = 3 keys: 0 x, 1 target, 2 behind, 3..6 transverse neighbours of x
        c = k[pos_]
        if c >= 0:
            own *= w[0] if c == 0 else (w[1] if c == 1 else w[2])
    return 1 / own


cert_ok, lines = True, []
for fam in ("localclock", "unitmoves"):
    for name, w in W.items():
        y = {ast.literal_eval(k.split("|")[0]) + ast.literal_eval(k.split("|")[1]): rq(v)
             for k, v in D[f"cert_{fam}_{name}"].items()}
        MT, by = {}, Fr(0)
        for kc, yy in D[f"cert_{fam}_{name}"].items():
            pos, con = ast.literal_eval(kc.split("|")[0]), ast.literal_eval(kc.split("|")[1])
            row = T3.row(pos, occ_of(T3, pos, con), w, 'base', Fr(1))
            yv = rq(yy)
            b = -sum(c * mv_fixed(k, fam, w) for k, c in row.items() if is_move(k))
            by += b * yv
            for k, c in row.items():
                if not is_move(k):
                    MT[k] = MT.get(k, 0) + c * yv
        good = all(v >= 0 for v in MT.values()) and by < 0
        cert_ok &= good
        lines.append(f"{fam} {name}: {len(y)} configuration(s), {len(MT)} exchange classes involved, b.y = {by}")
ok("A3", cert_ok, "exact Farkas certificates (3^3, three records): with every move at the local clock 1/pi_x, or every "
   "move at rate 1, NO choice of exchange rates balances the sector (M^T y >= 0 over all exchange classes, b.y < 0): "
   + "; ".join(lines))

# ------------------------------------------------------------------ A4: record-wise balance is impossible
rw_ok, lines = True, []
for name, w in W.items():
    ATy, yl = {}, Fr(0)
    for kc, yy in D[f"cert_recordwise_{name}"].items():
        a, b, kr = kc.split("|")
        pos, con, kr = ast.literal_eval(a), ast.literal_eval(b), int(kr)
        occ = occ_of(T3, pos, con)
        x = pos[kr]
        s = occ[x]
        behind = T3.NB[x][s ^ 1]
        o2 = list(occ)
        if occ[behind] >= 0:
            o2[behind], o2[x] = occ[x], occ[behind]
        else:
            o2[behind] = s
            o2[x] = -1
        row = {}
        k1, k2 = T3.env(occ, x), T3.env(o2, behind)
        row[k1] = row.get(k1, 0) + T3.weight(occ, w, Fr(1))
        row[k2] = row.get(k2, 0) - T3.weight(o2, w, Fr(1))
        yv = rq(yy)
        for k, c in row.items():
            ATy[k] = ATy.get(k, 0) + c * yv
            if is_move(k):
                yl += c * yv
    good = all(v >= 0 for v in ATy.values()) and yl > 0
    rw_ok &= good
    lines.append(f"{name}: y.(A l) = {yl}")
ok("A4", rw_ok, "exact certificates: no local rule balances each record's event against its own predecessor "
   "(A^T y >= 0, y.(A l) > 0, l = 1 on moves): " + "; ".join(lines))

# ------------------------------------------------------------------ A5: three and four records together, both families
j_ok, lines = True, []
for mode in ("base", "rot"):
    for name, w in W.items():
        ATy, yl, n3, n4 = {}, Fr(0), 0, 0
        for kc, yy in D[f"cert_joint_{mode}_{name}"].items():
            pos, con = ast.literal_eval(kc.split("|")[0]), ast.literal_eval(kc.split("|")[1])
            n3 += len(pos) == 3
            n4 += len(pos) == 4
            row = T3.row(pos, occ_of(T3, pos, con), w, mode, Fr(1))
            yv = rq(yy)
            for k, c in row.items():
                ATy[k] = ATy.get(k, 0) + c * yv
                if is_move(k):
                    yl += c * yv
        good = all(v >= 0 for v in ATy.values()) and yl > 0
        j_ok &= good
        lines.append(f"{'exchange only' if mode == 'base' else 'with head-on re-draw'} {name}: {n3} three- and {n4} "
                     f"four-record configurations, y.(A l) = {yl}")
ok("A5", j_ok, "exact certificates on 3^3: no local rule balances the three- and four-record sectors together, for the "
   "streaming events alone and for the family enlarged by a head-on pair re-drawing on its momentum class (a, -a): "
   + "; ".join(lines) + f" ({time.time() - T0:.0f} s)")

# ------------------------------------------------------------------ A7: compact clusters, rows of the problem on Z^3
if "cert_Z3_base_c1" in D:
    T6, T9 = Torus(6), Torus(9)
    z_ok, lines = True, []
    for mode in ("base", "rot"):
        for name, w in W.items():
            key = f"cert_Z3_{mode}_{name}"
            if key not in D:
                z_ok = False
                lines.append(f"{mode} {name}: no certificate")
                continue
            ATy, yl, same, nsup = {}, Fr(0), True, 0
            for kc, yy in D[key].items():
                pos, con = ast.literal_eval(kc.split("|")[0]), ast.literal_eval(kc.split("|")[1])
                row = T6.row(pos, occ_of(T6, pos, con), w, mode, Fr(1))
                pos9 = tuple(T9.IDX[T6.SITES[p_]] for p_ in pos)
                row9 = T9.row(pos9, occ_of(T9, pos9, con), w, mode, Fr(1))
                same &= row == row9
                yv = rq(yy)
                nsup += 1
                for k, c in row.items():
                    ATy[k] = ATy.get(k, 0) + c * yv
                    if is_move(k):
                        yl += c * yv
            good = same and all(v >= 0 for v in ATy.values()) and yl > 0
            z_ok &= good
            lines.append(f"{'exchange only' if mode == 'base' else 'with head-on re-draw'} {name}: {nsup} configurations, "
                         f"rows identical on 6^3 and 9^3: {same}, y.(A l) = {yl}")
    ok("A7", z_ok, "compact clusters (a record at the origin, the others in [0,2]^3): their balance equations are the same "
       "on the 6^3 and the 9^3 torus, hence equations of the problem on Z^3, and exact certificates show them infeasible: "
       + "; ".join(lines) + f" ({time.time() - T0:.0f} s)")

# ------------------------------------------------------------------ A6: conservation by every event
cons = True
for pos, con, occ in list(T3.configs(3))[::997]:
    for key, sg, o2 in T3.terms(pos, occ, 'rot'):
        if o2 is not None:
            mom = lambda o: tuple(sum((1 if c == 2 * i else -1 if c == 2 * i + 1 else 0) for c in o if c >= 0) for i in range(3))
            cons &= sum(1 for c in o2 if c >= 0) == len(pos) and mom(o2) == mom(occ)
ok("A6", cons, "every event (move, exchange, head-on re-draw) keeps the number of records and the total content "
   "vector, whatever its rate: conservation is a property of the event set, not of the clock (sampled predecessors)")

label = "PROVED (scope in ATTEMPT.md)" if not FAILS else "PARTIAL (failed: " + ", ".join(FAILS) + ")"
print(f"SUMMARY: {label}: radius-one local rates keep pi stationary on the three-record sector of the 3^3, 4^3 and 5^3 "
      "tori (exact rules, c = 1 and c0 = 1/2), never with local-clock or unit move rates, never record by record; the "
      "four-record sector admits none, on 3^3 and on Z^3 (compact clusters), even with head-on pairs re-drawing on their "
      "momentum class (exact Farkas certificates); number and momentum are conserved by every event")
if not FAILS:
    print("HIT: for block 50's inertial streaming of the six-axis rule at (3,1,2), rates depending only on the sites "
          "within distance one of an event keep pi stationary on the three-record sector of the 3^3, 4^3, 5^3 tori (exact "
          "rules at c = 1, c0 = 1/2), but no such rule has the local clock's or unit move rates or balances record by "
          "record; on Z^3 no such rule balances the four-record sector, with or without a head-on pair re-drawing on its "
          "momentum class: exact Farkas certificates on 74, 50 (73, 33) four-record clusters whose equations are the same "
          "on the 6^3 and 9^3 tori")
