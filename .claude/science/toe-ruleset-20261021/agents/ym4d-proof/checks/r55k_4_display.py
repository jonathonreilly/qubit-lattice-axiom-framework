#!/usr/bin/env python3
# checks/r55k_4_display.py -- POST-HOC report-only arithmetic. Criteria: checks/r55k_4_criteria.md (written first).
import os
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, "r55k_1_const.py")).read().split('P("r55k_1_const.py')[0])
e1 = Fr("6.7e-40")
for lab, lo, hi in (("(a) loose", "8.8606e-46", "8.8607e-46"), ("(a) sharp", "6.1060e-45", "6.1061e-45"),
                    ("(b) loose", "3.6318e-44", "3.6319e-44"), ("(b) sharp", "5.7649e-44", "5.7650e-44")):
    v = 2 * LOG10(e1 / I(Fr(hi), Fr(lo)) ) if False else 2 * LOG10(I(e1 / Fr(hi), e1 / Fr(lo)))
    P("D1 %-10s energy shortfall at q=12 = %s" % (lab, SF(v, 4)))
KB = 150; acc = I.c(0)
for k in range(1, KB + 1): acc = acc + LOG(2 ** k - 1) / (2 ** k)
B8 = EXP(I(acc.lo, acc.hi + (LN2 * (KB + 2) / (2 ** KB)).hi) * 8)
lb = SQRT(6) * 64 * B8 * Fr("5.17814e5")
P("D2 sqrt6*64*B(8)*5.17814e5 = %s ; log10(lb/6.6494e10) = %s" % (S(lb, 6), SF(LOG10(lb / Fr("6.6494e10")), 4)))
verdict("D2 (sharp liminf bound exceeds the most lenient need)", lb.lo > Fr("6.6494e10"))
for x in ("1.9252e12", "2.5062e12", "3.1576e12", "7.7008e12", "2.0216e13"):
    P("D3 log10(%s/5.288348e12) = %s" % (x, SF(LOG10(Fr(x) / Fr("5.288348e12")), 4)))
