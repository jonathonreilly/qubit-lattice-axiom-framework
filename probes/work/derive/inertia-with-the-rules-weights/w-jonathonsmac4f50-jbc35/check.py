"""inertia-with-the-rules-weights, attempt a1 (w-jonathonsmac4f50-jbc35): checks.

Exact (fractions) for every finite claim; the linear-programming feasibility items are labelled NUMERIC.

Objects.  Six-axis contents (d and d^1 opposite); block 44's clause: a record streams along its content; an occupied target makes
the two records exchange contents; scattering re-draws an adjacent pair on its momentum class.  The law with vacancies (block 39):
mu(c) ~ z^n prod_{adjacent pairs} W(s_x, s_y), W = c0 omega, omega = p, q, r (equal, opposite, orthogonal), c0 = 6/(p+q+4r).
Departure clause: every streaming event of the record at x (move or exchange) has rate 1/W_hat(x), W_hat(x) = product of its pair
weights with its current neighbours; scattering is the heat bath on the momentum class with weights mu (detailed balance).
"""
import itertools
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inertial_weights as iw

RESULTS = []


def want(label, ok, detail=""):
    RESULTS.append((label, bool(ok)))
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail != "" else ""), flush=True)


E, M6 = iw.E, iw.M6
TRIPLES = [(5, 1, 2), (3, 1, 2), (7, 2, 1), (2, 1, 1)]
Wof = lambda t: iw.Wmat(*t, F(6, t[0] + t[1] + 4 * t[2]))

# ------------------------------------------------------------------ T0: conservation and covariance of the departure clause
ok = True
for t in TRIPLES:
    W = Wof(t)
    for n in (2, 3):
        cfgs = [{(0, 0, 0): 0, (1, 0, 0): 3}, {(0, 0, 0): 0, (0, 0, 1): 0, (0, 1, 0): 2}]
        for cfg in cfgs:
            if len(cfg) != n: continue
            P0 = tuple(sum(E[d][k] for d in cfg.values()) for k in range(3))
            for rate, new in iw.events(cfg, W, 4, "departure", F(1)):
                ok = ok and len(new) == n and tuple(sum(E[d][k] for d in new.values()) for k in range(3)) == P0 and rate > 0
want("T0 on sample two- and three-record configurations every event of the departure clause (moves, exchanges, heat-bath re-draws) "
     "conserves the number of records and the momentum with a positive rate (covariance is by construction: the rates are functions of "
     "rotation-invariant pair weights and of momentum classes, not checked here)", ok)

# ------------------------------------------------------------------ T1: two records - the departure clause keeps mu stationary, exactly
rows = []; ok = True
for t in TRIPLES:
    W = Wof(t)
    for (L, gamma) in ((3, F(0)), (3, F(1)), (4, F(1, 3))):
        cnt, bad, _, _ = iw.check(L, 2, W, "departure", gamma)
        ok = ok and not bad
        if t == TRIPLES[0]: rows.append(f"L={L} gamma={gamma}: {cnt} configurations, {len(bad)} unbalanced")
want("T1 two records: the departure clause keeps the law with vacancies stationary on every configuration of the 3^3 and 4^3 tori, "
     "with and without scattering, at four weight triples at their pinned scale", ok, "; ".join(rows))
cnt, bad, _, _ = iw.check(3, 2, Wof(TRIPLES[0]), "plain", F(0))
want("T1' block 44's plain clause (all rates 1) does not keep the law with vacancies stationary with two records on 3^3 at (5,1,2)",
     len(bad) > 0, f"{len(bad)} of {cnt} configurations unbalanced")

# ------------------------------------------------------------------ T2: three records - the exchange past a third record
W = Wof((5, 1, 2))
cnt, bad, inf, outf = iw.check(3, 3, W, "departure", F(0))
key = (((0, 0, 0), 0), ((0, 0, 1), 0), ((0, 1, 0), 2))
Weq, Wort = W[0][0], W[0][2]
want("T2 three records on 3^3 at (5,1,2): the departure clause leaves 34344 of 631800 configurations unbalanced; in the witness "
     "(+x at 000, +x at 001, +y at 010) the inflow is 1 + W_orth + 1 = 20/7 against the outflow 1 + W_orth + W_eq = 4: the exchange that "
     "brought +y to 010 switched the third record's bond from W_orth to W_eq, which no rate paid for",
     len(bad) == 34344 and cnt == 631800 and inf.get(key) == 2 + Wort and outf[key] == 1 + Wort + Weq and inf.get(key) == F(20, 7) and outf[key] == 4,
     f"in {inf.get(key)}, out {outf[key]}")


def defect(L, n, W, rule):
    cnt, bad, inf, outf = iw.check(L, n, W, rule, F(0))
    tot = sum(outf.values())
    return sum(abs(inf.get(k, 0) - v) for k, v in outf.items()) / tot


d2p, d2d = defect(3, 2, W, "plain"), defect(3, 2, W, "departure")
d3p, d3d = defect(3, 3, W, "plain"), defect(3, 3, W, "departure")
want("T3 the stationarity defect sum |inflow - outflow| / sum outflow of the law with vacancies on 3^3 at (5,1,2): plain clause 32/273 "
     "(two records) and 192896/1003977 (three); departure clause 0 and 176/20475 - the departure clause is exact for pairs and its "
     "three-record defect is 22 times smaller",
     (d2p, d2d, d3p, d3d) == (F(32, 273), F(0), F(192896, 1003977), F(176, 20475)),
     f"{d2p}, {d2d}, {d3p}, {d3d} = {float(d2p):.4f}, 0, {float(d3p):.4f}, {float(d3d):.5f}")

# ------------------------------------------------------------------ N1: global balance with local rates is feasible for three records
try:
    import numpy as np
    from scipy.optimize import linprog
    from scipy.sparse import coo_matrix, csr_matrix, hstack, identity
    import importlib.util
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location("lpfeas", os.path.join(here, "lp_feasibility.py"))
    lp = importlib.util.module_from_spec(spec); spec.loader.exec_module(lp)
    res_const = lp.solve((1, 1, 1)); res = lp.solve((5, 1, 2))
    want("N1 NUMERIC 4^3 torus, three records (140616 translation classes), move and exchange rates free per covariant environment "
         "within distance 1 of the event's two sites (630 classes; an isolated move at rate 1): the linear program for stationarity with "
         "all rates >= t has optimum t = 1 at constant weights (block 44's clause) and t = 0.217778 = 49/225 = 1/W_eq^2 at (5,1,2): "
         "strictly positive local rates exist",
         abs(res_const - 1) < 1e-6 and abs(res - 49 / 225) < 1e-5, f"t(1,1,1) = {res_const:.6f}, t(5,1,2) = {res:.6f}")
except ImportError as exc:
    want("N1 NUMERIC skipped (scipy missing)", False, str(exc))

npass = sum(1 for _, o in RESULTS if o)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("SUMMARY: PARTIAL the departure clause (stream at rate 1/(product of the mover's pair weights), block 44's exchange, heat-bath "
          "scattering on the momentum class) is covariant, conserves number and momentum, and keeps the law with vacancies stationary "
          "exactly for two records (every configuration of 3^3 and 4^3, four weight triples); no clause with record-by-record (pairwise) "
          "balance does so for three records unless omega is constant (an exchange displaces the passed record; proof in ATTEMPT.md); the "
          "departure clause's three-record defect is 176/20475 against 192896/1003977 for block 44's; and positive local rates within "
          "distance 1 that restore stationarity for three records exist on 3^3 and 4^3 (linear program, numeric), so no no-go at that level")
    print("HIT: pair-weight inertia: the departure clause (rate 1/W_hat of the mover) keeps the law with vacancies stationary exactly for "
          "two records, and record-by-record balance is impossible beyond two records unless omega is constant; three-record global balance "
          "is feasible with positive covariant range-1 rates (LP on 4^3, min rate 1/W_eq^2), so the no-go is only for pairwise balance")
