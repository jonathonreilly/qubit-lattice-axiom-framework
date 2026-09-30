"""Exact (Fraction) verification of an explicit Gibbs patch: a 2-rail ladder between two exogenous setting records.
Sites: A (content alpha=(tau,a)), rails (g1_k, g2_k) for k=1..K (K=1 is the plaquette A-g1-B-g2), B (content beta=(tau',b)).
Bonds (nearest neighbour only): s-A, A-g1_1, A-g2_1, g1_k-g1_{k+1}, g2_k-g2_{k+1}, g1_K-B, g2_K-B, B-t.
All weights are 0/1 (hard constraints = 'admissible possibilities'):
  f_s(alpha)      = [tau == s]                      (single-site weight with the neighbour s)
  W(alpha,g1_1)   = [g1_1 == a]
  W(alpha,g2_1)   = [g2_1 == a xor 1 xor tau]
  rails copy: [g1_{k+1} == g1_k], [g2_{k+1} == g2_k]
  W(beta,g1_K)    = [tau'==1 or b == g1_K]     ; b = g1 when tau'=0
  W(beta,g2_K)    = [tau'==0 or b == g2_K xor 1]; b = g2 xor 1 when tau'=1
  g_t(beta)       = [tau' == t]
Joint law given (s,t) = product of weights / Z(s,t): a single joint draw of the whole interior patch.
Claims checked: (1) CHSH = 4 exactly (PR box); (2) marginal of EVERY single site (incl. every rail site) is
independent of (s,t) except the two wing sites' own setting (A on s, B on t); (3) the joint law of the
cut pair (g1_k,g2_k) depends on s (total variation 1), i.e. cluster locality fails.
"""
from fractions import Fraction as Fr
from itertools import product
import sys

def run(K):
    # enumerate: A=(tau,a) ; rails g1[1..K], g2[1..K] ; B=(tau',b)
    res = {}
    for s in (0, 1):
        for t in (0, 1):
            wts = {}
            for tau, a in product((0, 1), repeat=2):
                if tau != s: continue
                g1 = [a]; g2 = [a ^ 1 ^ tau]
                # rails copy deterministically; enumerate only consistent configs (hard constraints)
                g1 = g1 * K; g2 = g2 * K
                for taup, b in product((0, 1), repeat=2):
                    if taup != t: continue
                    if taup == 0 and b != g1[-1]: continue
                    if taup == 1 and b != (g2[-1] ^ 1): continue
                    wts[((tau, a), tuple(g1), tuple(g2), (taup, b))] = Fr(1)
            Z = sum(wts.values())
            res[(s, t)] = {k: v / Z for k, v in wts.items()}
    return res

def check(K):
    res = run(K)
    def E(s, t):
        return sum(p * (1 if k[0][1] == 0 else -1) * (1 if k[3][1] == 0 else -1) for k, p in res[(s, t)].items())
    Es = {(s, t): E(s, t) for s in (0, 1) for t in (0, 1)}
    S = Es[0, 0] + Es[0, 1] + Es[1, 0] - Es[1, 1]
    # single-site marginals
    def marg(site):
        out = {}
        for st, law in res.items():
            m = {}
            for k, p in law.items():
                if site == "A": v = k[0]
                elif site == "B": v = k[3]
                elif site[0] == "g":
                    r, i = int(site[1]), int(site[2:]) - 1
                    v = (k[1] if r == 1 else k[2])[i]
                m[v] = m.get(v, 0) + p
            out[st] = m
        return out
    def dep(site, on):  # does the marginal change with s (on='s') or t (on='t')?
        m = marg(site)
        keys = set().union(*[set(x) for x in m.values()])
        bad = False
        for (s, t) in m:
            other = (1 - s, t) if on == "s" else (s, 1 - t)
            for v in keys:
                if m[(s, t)].get(v, 0) != m[other].get(v, 0): bad = True
        return bad
    rows = {"A": (dep("A", "s"), dep("A", "t")), "B": (dep("B", "s"), dep("B", "t"))}
    for k in range(1, K + 1):
        for r in (1, 2):
            rows[f"g{r}{k}"] = (dep(f"g{r}{k}", "s"), dep(f"g{r}{k}", "t"))
    # cut pair joint law
    def pair_law(k):
        out = {}
        for st, law in res.items():
            m = {}
            for kk, p in law.items():
                v = (kk[1][k - 1], kk[2][k - 1]); m[v] = m.get(v, 0) + p
            out[st] = m
        return out
    pl = pair_law(1)
    tv_s = max(sum(abs(pl[(0, t)].get(v, 0) - pl[(1, t)].get(v, 0)) for v in [(0,0),(0,1),(1,0),(1,1)]) / 2 for t in (0, 1))
    tv_t = max(sum(abs(pl[(s, 0)].get(v, 0) - pl[(s, 1)].get(v, 0)) for v in [(0,0),(0,1),(1,0),(1,1)]) / 2 for s in (0, 1))
    print(f"K={K} (sites: A,B + {2*K} rail sites; distance A-B = {K+1} bonds):")
    print("  E(s,t) =", {k: str(v) for k, v in Es.items()}, " CHSH S =", S)
    print("  marginal depends on (s,t)?  (site: on s, on t)")
    for k, v in rows.items(): print("    ", k, v)
    print(f"  cut pair (g1_1,g2_1) joint law: TV over s = {tv_s}, TV over t = {tv_t}")
    return S, rows, tv_s

if __name__ == "__main__":
    for K in (1, 2, 4, 8):
        check(K)
