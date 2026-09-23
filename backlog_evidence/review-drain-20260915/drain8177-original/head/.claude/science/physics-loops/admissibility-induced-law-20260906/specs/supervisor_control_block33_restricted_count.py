"""Kind-typed lift of the counted family with shape restrictions; the ceiling on epsilon_2 for a given budget exponent c.
Node kinds P (processed, arrow weight xP = t), A (amplified, arrow weight xA = eps2/t^c), S (seed, weight eps1).
Entry types: D (reached by a down step: the node is its parent's predecessor), U (reached by an up step: a successor whose arrow
points to the parent), F (reached by a fork), R (root).  Slots: own arrow (kinds P, A; not for entry U): 3 choices of predecessor,
child of entry D of any kind; up-children: successors whose arrows point here, entry U, kinds P or A; 3 positions minus 1 if entry D;
forks: 6 siblings minus 1 if entry F, weight yF = 1/t^3 per fork (paired with an extra seed).
Restriction 'R12': at nodes of kind P or A at most two up-children and at most one of kind P.  'none': the unrestricted count
(which must reproduce block 25/30's recursion: D = (1+xU)^2(1+3xD)(1+yF)^6 etc. with a single x when kinds are merged)."""
import sys
import numpy as np
from fractions import Fraction as F
def devs(p, q, r):
    p, q, r = F(p), F(q), F(r)
    return (1 - p**3/(p**3+q**3+4*r**3), 1 - p**2*q/(p*q*(p+q)+4*r**3), 1 - p**2*r/(r*(p**2+q**2)+r**2*(p+q)+2*r**3))
def iterate(xP, xA, eS, yF, restr, iters=4000, cap=1e12):
    # unknowns: for each entry e in D,U,F and kind k in P,A,S: generating function G[e][k] of the subtree hanging at such a node
    # (including the node's own weight: xP or xA for its arrow when it has one... we put the arrow weight on the edge instead:
    #  up-child of kind k contributes x_k * G[U][k]; down child (pred) contributes x_parent * G[D][kind]; fork child contributes yF * G[F][kind])
    G = {e: {k: 0.0 for k in "PAS"} for e in "DUFR"}      # least fixed point: iterate from the empty family
    prev = -1.0
    for it in range(iters):
        Gn = {e: {} for e in "DUFR"}
        Dsum = sum(G["D"][k] for k in "PAS")
        Fsum = sum(G["F"][k] for k in "PAS")
        UP, UA = xP * G["U"]["P"], xA * G["U"]["A"]
        for e in "DUFR":
            nup = 2 if e == "D" else 3
            nfork = 5 if e == "F" else 6
            for k in "PAS":
                if k == "S" and e == "U": Gn[e][k] = 0.0; continue
                own = 1.0
                if k != "S" and e != "U":
                    own = 3.0 * (xP if k == "P" else xA) * Dsum      # a processed or amplified node has exactly one arrow
                if restr == "R12" and k in "PA":
                    up = 1.0 + nup * (UP + UA) + (nup * (nup - 1) / 2) * (UA * UA + 2 * UP * UA)
                else:
                    up = (1.0 + UP + UA) ** nup
                fk = (1.0 + yF * Fsum) ** nfork
                w = eS if k == "S" else 1.0
                Gn[e][k] = w * own * up * fk
        G = Gn
        mx = max(max(v.values()) for v in G.values())
        if mx > cap: return None
        if it > 100 and it % 100 == 0 and mx > 0 and abs(mx - prev) < 1e-12 * mx: break
        prev = mx
    return G
def region(c, restr, p, q, r):
    d1, d2, d3 = devs(p, q, r); e1, e2 = float(d1), float(max(d2, d3))
    best = None
    for tn in range(20, 340):
        t = tn / 1000
        G = iterate(t, e2 / t**c, e1, 1.0 / t**3, restr)
        if G is None: continue
        R = G["R"]["P"] + G["R"]["A"] + G["R"]["S"]
        if best is None or R < best[1]: best = (t, R)
    return best
if __name__ == "__main__":
    print("sanity: unrestricted count at block 30's point (4165,1,2), c=2:", region(2, "none", 4165, 1, 2))
    print("sanity: unrestricted at (4150,1,2) c=2 (should fail):", region(2, "none", 4150, 1, 2))
    for c, restr in ((2, "none"), (2, "R12"), (1, "none"), (1, "R12")):
        for (q, r) in ((1, 2), (1, 1)):
            lo, hi = 20, 5000
            while lo < hi:
                mid = (lo + hi) // 2
                if region(c, restr, mid, q, r): hi = mid
                else: lo = mid + 1
            print(f"c={c} restriction={restr} line (p,{q},{r}): least p with a convergent count on the t-grid: {lo}  (t, R) = {region(c, restr, lo, q, r)}")
    
