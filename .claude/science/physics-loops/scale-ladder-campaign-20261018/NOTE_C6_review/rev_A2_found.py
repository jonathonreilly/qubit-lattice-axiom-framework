"""Re-verify the found ordering from scratch: BKSF algebra on all edge pairs at shared vertices, bare strings commute,
group of bare strings has no -I, identity prod kappa = sigma; then sign flips make uniform 1011 / 1111 the bare sector."""
import sys, pickle, random, math
sys.argv = [sys.argv[0], '3', '0']
exec(open('rev_A2.py').read().split("nconv = int")[0])
order = pickle.load(open('ordering_bare_consistent_L3.pkl', 'rb'))
assert all(sorted(order[v]) == sorted(inc[v]) for v in range(nV))
S = build(order)
# full anticommutation check on all pairs sharing a vertex, and a sample of disjoint pairs
def anti(A, B): return (bin(A[1] & B[2]).count('1') + bin(A[2] & B[1]).count('1')) % 2
ok = all(anti(S[a], S[b]) == 1 for v in range(nV) for a in inc[v] for b in inc[v] if a < b)
ends = [set(elist[k][:2]) for k in range(nE)]
for _ in range(20000):
    a, b = random.sample(range(nE), 2)
    if not (ends[a] & ends[b]): ok &= anti(S[a], S[b]) == 0
print("BKSF algebra:", ok)
label = list(range(nV))
kap, bare = loopdata(S, label)
allcomm = all(anti(bare[a], bare[b]) == 0 for a in range(nF) for b in range(a + 1, nF))
print("all bare loop strings commute:", allcomm)
sig = sigmas(bare)
print("identity prod kappa = sigma on all basis relations:", all(math.prod(kap[i] for i in range(nF) if (r >> i) & 1) == s for r, s in zip(rels, sig)))
print("#sigma=-1:", sum(s == -1 for s in sig), "; bare-+1 group contains -I:", contains_minus_I(bare))
print("kappa per type (#-1 / total):", {t: (sum(1 for (tt, _), k in zip(faces, kap) if tt == t and k == -1), sum(1 for tt, _ in faces if tt == t)) for t in TYPES})
# kappa is consistent, so it is the flux of a gauge field: find u (GF(2) solve) with prod_{e in C} u_e = kappa_C * F_target_C,
# then flipping S_e -> -S_e on {u_e = -1} makes the bare sector equal to F_target.
def solve(rhs):
    piv = {}
    for i, m in enumerate(fmask):
        x, b = m, rhs[i]
        while x:
            h = x.bit_length() - 1
            if h in piv: x ^= piv[h][0]; b ^= piv[h][1]
            else: piv[h] = (x, b); break
        if not x and b: return None
    sol = 0
    for h in sorted(piv):
        x, b = piv[h]
        rest = x & ~(1 << h)
        val = b ^ (bin(rest & sol).count('1') % 2)
        if val: sol |= 1 << h
    return sol
for name, bq in (('1011', (1, 0, 1, 1)), ('1111', (1, 1, 1, 1)), ('0000', (0, 0, 0, 0))):
    Ft = uniform(bq)
    rhs = [0 if kap[i] * Ft[i] == 1 else 1 for i in range(nF)]
    sol = solve(rhs)
    S2 = [((s[0] + 2) % 4, s[1], s[2]) if (sol >> k) & 1 else s for k, s in enumerate(S)]
    kap2, bare2 = loopdata(S2, label)
    print(f"target {name}: sign-flip set found: {sol is not None}; bare sector of flipped convention == target: {kap2 == Ft}; bare group -I: {contains_minus_I(bare2)}")
