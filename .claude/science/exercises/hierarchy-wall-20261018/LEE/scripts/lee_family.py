"""LEE-1 part (i): look-elsewhere count for v_cand = M_Pl (7/8)^(1/4) alpha_LM^16.

Family fixed in ../PREREG.md before this script was written. Stdlib only.
"""
import math, random
from fractions import Fraction as F

MPL = 1.2209e19
MPL_RED = MPL / math.sqrt(8 * math.pi)
VOBS = 246.22
P = 0.5934
u0 = P ** 0.25
ab = 1 / (4 * math.pi)
aLM = ab / u0
asv = ab / u0 ** 2
VCAND = MPL * (7 / 8) ** 0.25 * aLM ** 16
delta0 = VCAND / VOBS - 1

# r-set
small = set()
for p in range(1, 5):
    for q in range(1, 5):
        small.add(F(p, q))
eta = {1 - F(1, 2 ** (s - 1)) for s in range(2, 7)}
R = sorted(small | eta | {1 / x for x in eta})
assert len(R) == 17, len(R)

def prefactors(R):
    out = []
    for r in R:
        for n in (1, 2, 4):
            val = float(r) ** (1.0 / n)
            if not any(abs(val / o[0] - 1) < 1e-12 for o in out):
                out.append((val, f"({r})^(1/{n})"))
    return out

PF = prefactors(R)

base = [("a_bare", ab), ("a_LM", aLM), ("a_s(v)", asv), ("u0", u0), ("<P>", P)]
C0 = base + [("a_bare/4pi", ab / (4 * math.pi)), ("a_LM/4pi", aLM / (4 * math.pi)),
             ("a_s(v)/4pi", asv / (4 * math.pi)), ("1-u0", 1 - u0), ("1-<P>", 1 - P)]
Ccore = base
Cuni = []
for nm, c in base:
    Cuni += [(nm, c), (nm + "/pi", c / math.pi), (nm + "/4pi", c / (4 * math.pi))]

def family(C, mpls):
    mem = []
    for mname, M in mpls:
        for pv, pn in PF:
            for cn, c in C:
                for k in range(1, 33):
                    mem.append((M * pv * c ** k, f"{mname} {pn} {cn}^{k}"))
    return mem

def column_check(C):
    mn = min(abs(math.log(c)) for _, c in C)
    return mn, mn > 2 * math.log(1.01)

def union_measure(lnvals, w, lo, hi):
    iv = sorted((x - w, x + w) for x in lnvals if x + w > lo and x - w < hi)
    tot = 0.0; cur_a = None; cur_b = None
    for a, b in iv:
        a = max(a, lo); b = min(b, hi)
        if cur_b is None or a > cur_b:
            if cur_b is not None:
                tot += cur_b - cur_a
            cur_a, cur_b = a, b
        else:
            cur_b = max(cur_b, b)
    if cur_b is not None:
        tot += cur_b - cur_a
    return tot / (hi - lo)

def analyse(name, mem, rng):
    N = len(mem)
    vals = [m for m, _ in mem]
    distinct = len({round(math.log(v), 11) for v in vals})
    lnv = [math.log(v) for v in vals]
    lo, hi = math.log(VOBS / 10), math.log(VOBS * 10)
    print(f"\n=== {name}: N = {N} members ({distinct} distinct values)")
    for tag, tol in (("0.03%", 3e-4), ("1%", 1e-2), ("|delta0|", abs(delta0))):
        hits = [(m, s) for m, s in mem if abs(m / VOBS - 1) <= tol]
        w = math.log(1 + tol)
        pg = union_measure(lnv, w, lo, hi)
        inrange = sum(1 for x in lnv if lo <= x <= hi)
        expn = inrange * 2 * w / (hi - lo)
        # Monte Carlo cross-check
        s = sorted(lnv); import bisect
        nmc = 200000; cnt = 0
        for _ in range(nmc):
            t = rng.uniform(lo, hi)
            i = bisect.bisect_left(s, t - w)
            if i < len(s) and s[i] <= t + w:
                cnt += 1
        print(f"  window {tag:9s}: N_hit = {len(hits):4d}  p_hit = {len(hits)/N:.3e}  "
              f"p_global(exact) = {pg:.4f}  p_global(MC) = {cnt/nmc:.4f}  E[#hits] = {expn:.4f}")
        if True:
            for m, s_ in sorted(hits, key=lambda h: abs(h[0] / VOBS - 1)):
                print(f"      {s_:40s} {m:10.4f} GeV  dev {100*(m/VOBS-1):+.4f}%")
    return N

def main():
    rng = random.Random(20261018)
    print(f"v_cand = {VCAND:.6f} GeV, delta0 = {delta0:+.6e}")
    print(f"prefactors: {len(PF)} distinct from {len(R)} rationals x 3 roots")
    for nm, C in (("F0", C0), ("F_core", Ccore), ("F_uniform", Cuni)):
        mn, ok = column_check(C)
        print(f"column check {nm}: min |ln c| = {mn:.4f} > 1% window width {2*math.log(1.01):.4f}: {ok}")
    analyse("F0 (decision family)", family(C0, [("MPl", MPL)]), rng)
    analyse("F_core", family(Ccore, [("MPl", MPL)]), rng)
    analyse("F_uniform", family(Cuni, [("MPl", MPL)]), rng)
    analyse("F0x2 (both M_Pl conventions)", family(C0, [("MPl", MPL), ("MPl_red", MPL_RED)]), rng)
    # per-column max hits check (proof check of p_hit <= 1/32)
    mem = family(C0, [("MPl", MPL)])
    cols = {}
    for m, s in mem:
        if abs(m / VOBS - 1) <= 1e-2:
            key = s.rsplit("^", 1)[0]
            cols[key] = cols.get(key, 0) + 1
    print("\nmax hits in one column (1% window, F0):", max(cols.values()) if cols else 0)

if __name__ == "__main__":
    main()
