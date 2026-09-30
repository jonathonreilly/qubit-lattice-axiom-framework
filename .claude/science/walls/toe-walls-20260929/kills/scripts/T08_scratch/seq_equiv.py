"""Kill check 1: the attacker's 'co-formed' 2-rail ladder law equals, exactly, the law of an ordinary SEQUENTIAL
(adapted, one-site-at-a-time, nearest-neighbour, records-only) formation in the order s,t | A | rails | B, in which the
setting record s is an ANCESTOR of B's outcome.  That is the landed Thm 2(a) (b = a xor (s and t)) of the Bell-values note.
Also: the wing outcome law P(a,b|s,t) is identical to Thm 2(a)'s."""
from fractions import Fraction as Fr
from itertools import product
import sys
sys.path.insert(0, '../../attacks/T08_scratch')
import importlib.util
spec = importlib.util.spec_from_file_location("gg", "../../attacks/T08_scratch/gadget_gibbs_check.py")
# gadget_gibbs_check runs its prints at import; capture gibbs() by exec of its function only
src = open("../../attacks/T08_scratch/gadget_gibbs_check.py").read().split("for K in (1, 2, 3):")[0]
ns = {}; exec(src, ns); gibbs = ns["gibbs"]

def sequential(K, s, t):
    """s and t exogenous.  Step 1: A forms from neighbour s: content (tau,a), tau = copy of s, a a fair coin.
    Step 2: g1_1 forms from A (copy a), g2_1 forms from A (a xor 1 xor tau).  Step k: rails copy the previous rail site.
    Final: B forms from (g1_K, g2_K, t): tau'=t; b = g1_K if t=0 else g2_K xor 1."""
    law = {}
    for a in (0, 1):
        A = (s, a)
        g1 = [a] * K; g2 = [a ^ 1 ^ s] * K
        b = g1[-1] if t == 0 else (g2[-1] ^ 1)
        B = (t, b)
        law[(A, tuple(g1 + g2), B)] = Fr(1, 2)
    return law

for K in (1, 2, 3, 5):
    tv_max = 0
    for s in (0, 1):
        for t in (0, 1):
            g, _ = gibbs(K, s, t) if K <= 3 else (None, None)
            q = sequential(K, s, t)
            if g is not None:
                keys = set(g) | set(q)
                tv = sum(abs(g.get(k, 0) - q.get(k, 0)) for k in keys) / 2
                tv_max = max(tv_max, tv)
    # Thm 2(a): b = a xor (s and t), a fair
    ok2a = True
    for s in (0, 1):
        for t in (0, 1):
            q = sequential(K, s, t)
            for (A, R, B), p in q.items():
                if B[1] != A[1] ^ (s & t): ok2a = False
    print(f"K={K}: max TV(Gibbs 'co-formed' ladder, sequential chain) = {tv_max if K<=3 else 'n/a (Gibbs enumerated to K=3)'}; "
          f"outcome law = Thm 2(a) PR box b=a xor st: {ok2a}")
