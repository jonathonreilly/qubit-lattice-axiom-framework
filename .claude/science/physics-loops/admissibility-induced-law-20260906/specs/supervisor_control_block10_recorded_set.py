"""Supervisor control, block 10: the recorded-set Gibbs theorem.
(1) k-th mixed differences of log Z_k (equivalently log K_k) at the vacuum +x, for k = 2..6, at (3,1,2), (5,2,4), (2,2,2):
    the k-body term of the canonical potential on a recorded set of size k is nonzero iff some k-th mixed difference is nonzero.
    Reported as an exact product ratio (the exponential of the alternating sum), != 1 iff nonzero.
(2) the plaquette (cycle4) formation law for the order a, b, c, d with d recording b and c (its two neighbors): the canonical
    (vacuum-normalized) potential by Möbius inversion of log mu over the 2^4 subsets, at (3,1,2): the pair term on the
    non-adjacent pair {b, c} is nonzero (so the law is not Markov for the cycle), and no term appears on the other non-edge {a, d}.
(3) the star (center x with three leaves, center formed last): the three-body term on the leaves is nonzero.
Exact arithmetic (fractions); the alternating sums are reported as ratios of products.
"""
from fractions import Fraction as F
from itertools import product, combinations
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[5] / "scripts"))
import importlib
run = importlib.import_module("admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_2026_09_15")
M = 6

def Zk(rule, vals):
    """Z_k(a_1..a_k) = sum_s prod_i phi(s, a_i) as an exact integer."""
    return sum(__import__("math").prod(rule.phi[s][a] for a in vals) for s in range(M))

def mixed_ratio(rule, vals):
    """exp(alternating sum over subsets S of {1..k} of (-1)^{k-|S|} log Z_k(v_S, vacuum elsewhere)) as an exact rational:
    numerator = product over S with (-1)^{k-|S|} = +1, denominator = product over the others."""
    k = len(vals)
    num, den = 1, 1
    for mask in range(1 << k):
        arg = [vals[i] if (mask >> i) & 1 else 0 for i in range(k)]
        z = Zk(rule, arg)
        if (k - bin(mask).count("1")) % 2 == 0:
            num *= z
        else:
            den *= z
    return F(num, den)

def main():
    print("=== (1) k-body irreducibility of log Z_k: a witness assignment per k (search over small alphabets), ratio != 1 means nonzero mixed difference")
    for tr in [(3, 1, 2), (5, 2, 4), (2, 2, 2)]:
        rule = run.Rule(tr)
        out = []
        for k in range(2, 7):
            found = None
            # search assignments over values in {-x, +y, +z, -y} (vacuum is +x = 0)
            for vals in product((1, 2, 4, 3), repeat=k):
                r = mixed_ratio(rule, vals)
                if r != 1:
                    found = (vals, r); break
            out.append((k, found))
        print(f"{tr}: " + "; ".join(f"k={k}: " + ("none (all searched ratios = 1)" if f is None else f"ratio {f[1]} at {[run.AXES[v] for v in f[0]]}") for k, f in out))
    print()
    print("=== (2) plaquette a-b, a-c, b-d, c-d; order (a, b, c, d): d records b and c; canonical potential by Möbius inversion at (3,1,2)")
    rule = run.Rule((3, 1, 2))
    sites = ["a", "b", "c", "d"]
    def mu(v):
        a, b, c, d = v
        return F(1, M) * rule.K[a][b] * rule.K[a][c] * rule.cond((b, c))[d]
    # log mu(v) = sum_{S subset} Phi_S(v_S) with Phi_S = 0 when any coordinate in S is the vacuum 0: Phi_S(v) = sum_{T subset S} (-1)^{|S-T|} log mu(v_T, 0 elsewhere)
    # report as ratios: exp(Phi_S) for the sets S = {b,c}, {a,d}, {a,b}, {a,b,c,d} at a witness v
    def phi_ratio(S, v):
        num, den = F(1), F(1)
        for r in range(len(S) + 1):
            for T in combinations(S, r):
                w = [0] * 4
                for i in T: w[i] = v[i]
                val = mu(tuple(w))
                if (len(S) - r) % 2 == 0: num *= val
                else: den *= val
        return num / den
    v = (1, 2, 4, 3)  # a=-x, b=+y, c=+z, d=-y
    for S, name in [((1, 2), "{b,c} non-adjacent (recorded together by d)"), ((0, 3), "{a,d} non-adjacent (never recorded together)"), ((0, 1), "{a,b} edge"), ((1, 3), "{b,d} edge"), ((0, 1, 2, 3), "{a,b,c,d}"), ((1, 2, 3), "{b,c,d}")]:
        print(f"  exp(Phi_{name}) at v = {phi_ratio(S, v)}  (1 means zero term)")
    # maximal over v for {a,d}: check it is 1 for all v
    all_ad_one = all(phi_ratio((0, 3), vv) == 1 for vv in product(range(M), repeat=4))
    print(f"  {{a,d}} term is zero on all 1296 configurations: {all_ad_one}")
    any_bc = any(phi_ratio((1, 2), vv) != 1 for vv in product(range(M), repeat=4))
    print(f"  {{b,c}} term nonzero for some configuration: {any_bc}")
    print()
    print("=== (3) star: center x formed last, recording its three leaves (l1, l2, l3): three-body term on the leaves at (3,1,2)")
    def mu_star(v):
        l1, l2, l3, x = v
        return F(1, M) ** 3 * rule.cond((l1, l2, l3))[x]
    def phi_ratio_star(S, v):
        num, den = F(1), F(1)
        for r in range(len(S) + 1):
            for T in combinations(S, r):
                w = [0] * 4
                for i in T: w[i] = v[i]
                val = mu_star(tuple(w))
                if (len(S) - r) % 2 == 0: num *= val
                else: den *= val
        return num / den
    any3 = None
    for vv in product(range(M), repeat=3):
        r = phi_ratio_star((0, 1, 2), vv + (0,))
        if r != 1: any3 = (vv, r); break
    print(f"  three-body term on the leaves nonzero: {any3 is not None}; witness {any3}")

if __name__ == "__main__":
    main()
