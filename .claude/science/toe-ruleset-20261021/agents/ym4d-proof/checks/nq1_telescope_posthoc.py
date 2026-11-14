#!/usr/bin/env python3
"""checks/nq1_telescope_posthoc.py -- POST-HOC check (written after check nq1's
result was seen, and labelled as such in NQ_CHECK.md).

It verifies, entrywise and exactly, the operator identity that Step 1 of
Theorem NQ-1 (NQ_CHECK.md section Q3) proves:

    Q^{(j)} = Q_str^{(j)} - d_j o sum_{i=0}^{j-1} ev^{(j-1-i)} o h o Q_str^{(i)}

at L = 3, d = 4, for j = 1 and j = 2, in all four link directions.  j = 1 is
input (i) itself; j = 2 is the first instance of the induction step, which is
uniform in j.  No pre-registered verdict attaches to this file; it is a
self-check of the proof's algebra, not a new result.  j = 3 is not run: two
4.1M-entry rows at once would exceed the brief's 1 GB budget.

Reuses the row machinery of nq1_qnorm.py unaltered.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nq1_qnorm import (D, DEN1, L, compose, h_pattern, pack, pdelta,  # noqa: E402
                       q_root_pattern, q_str_pattern, unpack)


def scale_add(acc, row, mult):
    for k, v in row.items():
        acc[k] = acc.get(k, 0) + mult * v


def main():
    qpats = {mu: q_root_pattern(mu) for mu in range(D)}
    spats = {mu: q_str_pattern(mu) for mu in range(D)}
    hp = h_pattern()
    ok = True
    for j in (1, 2):
        # SP[i][nu] = row of Q_str^{(i)} for the level-i link (0,nu), den DEN1^i
        SP = {0: {nu: {pack((0, 0, 0, 0), nu): 1} for nu in range(D)}}
        for i in range(1, j):
            SP[i] = {nu: compose(spats, i, nu, "Q_str^(%d)" % i) for nu in range(D)}
        for mu in range(D):
            lhs = compose(qpats, j, mu, "Q_root")
            acc = dict(compose(spats, j, mu, "Q_str"))
            # subtract the gauge part
            for i in range(j):
                # T_i at level-j site 0, over denominator DEN1^(i+1)
                ti = {}
                for key, coef in hp.items():
                    y, nu = unpack(key)
                    dk = pdelta(tuple((L ** i) * yc for yc in y))
                    for pk, w in SP[i][nu].items():
                        k2 = pk + dk
                        ti[k2] = ti.get(k2, 0) + coef * w
                mult = DEN1 ** (j - i - 1)
                # -(d_j T_i) = -(T_i at X=e_mu) + (T_i at X=0), far end at L^j e_mu
                far = [0] * D
                far[mu] = L ** j
                dkfar = pdelta(tuple(far))
                for k, v in ti.items():
                    acc[k + dkfar] = acc.get(k + dkfar, 0) - mult * v
                    acc[k] = acc.get(k, 0) + mult * v
            diff = dict(acc)
            for k, v in lhs.items():
                diff[k] = diff.get(k, 0) - v
            bad = sum(1 for v in diff.values() if v != 0)
            print("telescope j=%d mu=%d : %d entries differ  (lhs %d, rhs %d) -> %s"
                  % (j, mu, bad, len(lhs), sum(1 for v in acc.values() if v != 0),
                     "ok" if bad == 0 else "MISMATCH"))
            sys.stdout.flush()
            ok &= (bad == 0)
    print("POST-HOC telescope identity: %s" % ("ALL MATCH" if ok else "MISMATCH"))


if __name__ == "__main__":
    main()
