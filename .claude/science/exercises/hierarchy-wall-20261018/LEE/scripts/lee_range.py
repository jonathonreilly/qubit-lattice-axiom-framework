"""POST-HOC: p_global(0.03%) for F0 versus the target range (not pre-registered)."""
import math, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lee_family as LF
mem = LF.family(LF.C0, [("MPl", LF.MPL)])
lnv = [math.log(m) for m, _ in mem]
w = math.log(1.0003)
for dec in (0.5, 1, 2, 3):
    lo, hi = math.log(LF.VOBS / 10**dec), math.log(LF.VOBS * 10**dec)
    print(f"targets in [v/10^{dec}, v*10^{dec}]: p_global(0.03%) = {LF.union_measure(lnv, w, lo, hi):.4f}")
