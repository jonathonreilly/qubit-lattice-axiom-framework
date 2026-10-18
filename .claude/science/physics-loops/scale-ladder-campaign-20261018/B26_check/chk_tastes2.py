"""Remainder of chk_tastes.py (part 1 timed out at 30 min): joint (R_L, A_1) with w_R in 8th roots, w_A in {+-1}
(A_1 alone admits only w = +-1, so a joint taste can have no other w_A); Rt alone, w in 8th roots."""
import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import chk_tastes_lib as T
from chk_tastes_lib import *
pre = {}
def tab2(Xa, Xb, wa_idx, wb_idx):
    out = {}
    for e in ES:
        out[e] = [(i, j) for i in wa_idx for j in wb_idx
                  if invertible_in_null(rows_for(Xa, e, WS[i]) + rows_for(Xb, e, WS[j]))[1]]
    return out
tRA = tab2(RLk, Aa(1), range(8), (0, 4))
for e in ES: print("  (R_L, A_1)", e, tRA[e])
check("joint (R_L, A_1) (w_R in 8th roots, w_A in {+-1}): some invertible taste for every e", all(tRA[e] for e in ES))
tRt = {e: [j for j in range(8) if invertible_in_null(rows_for(RTk, e, WS[j]))[1]] for e in ES}
check("Rt alone has tastes for every e (like R_L)", all(tRt[e] for e in ES), str(tRt))
print(f"\nTOTAL: PASS={P} FAIL={F}   [{time.time() - t0:.1f}s]")
