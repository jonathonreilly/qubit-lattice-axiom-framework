#!/usr/bin/env python3
"""Clock and rate: covariant exponential races, induced order laws, and what
finished records can and cannot see, exact and finite.

Wave C (clock-and-rate) of the TOE derivation campaign by underdetermination
witnesses.  Exact rational arithmetic throughout; exact probabilities; decimal displays may use floating point.

Declared objects
  * windows: the 2x3 rectangle (6 sites, 7 edges) and the 3x3 plane with the
    parity roles of the landed support-rule note (V = 4, L = 4, P = 1, each L
    in exactly two checks);
  * clocks: independent exponential clocks, one per unformed site, with a
    covariant rate law lambda(site | formed set, recorded values); the induced
    order law is the sequential race, P(next = s) = lambda(s)/sum over
    unformed sites, restarted by memorylessness after every formation;
  * rate laws: uniform lambda = 1; neighbour-count laws 1 + k, (1 + k)^2 and
    1/(1 + k) with k = number of formed in-window nearest neighbours; a
    value law 1 + (number of agreeing pairs among formed nearest-neighbour
    values), covariant under window rotations and the internal flip;
  * conditional rules on the binary alphabet {+1, -1}: the chain rule of the
    positive pair measure mu(v) proportional to 2^(number of agreeing edges)
    (conditions on all formed sites), and the nearest-neighbour rule
    r(a) proportional to 2^(number of formed neighbours with value a);
  * the plane hard-support rule of the support-rule note: any site may form next;
    draw a fair bit when no check closes, force the required bit when checks
    close, and fail on conflicting requirements; d(order) = number of L sites that form last within the union of
    their two checks; P(fully recorded | order) = 2^(-d).

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys

AUDIT_TIMEOUT_SEC = 900
from fractions import Fraction as Fr
from itertools import permutations, product

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


# ---------------------------------------------------------------- windows
def grid_window(rows, cols):
    sites = [(r, c) for r in range(rows) for c in range(cols)]
    idx = {s: i for i, s in enumerate(sites)}
    nbrs = []
    for (r, c) in sites:
        out = []
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (r + dr, c + dc) in idx:
                out.append(idx[(r + dr, c + dc)])
        nbrs.append(tuple(out))
    edges = sorted({tuple(sorted((i, j))) for i in range(len(sites)) for j in nbrs[i]})
    return sites, idx, nbrs, edges


S23, IDX23, NB23, ED23 = grid_window(2, 3)
N23 = len(S23)
S33, IDX33, NB33, ED33 = grid_window(3, 3)
N33 = len(S33)

# 3x3 parity roles as in the landed support-rule note: "VLPC"[(r % 2) + (c % 2)]
ROLE = ["VLPC"[(r % 2) + (c % 2)] for (r, c) in S33]
VS = [i for i, x in enumerate(ROLE) if x == "V"]
LS = [i for i, x in enumerate(ROLE) if x == "L"]
CHECKS = {v: tuple([v] + [u for u in NB33[v] if ROLE[u] == "L"]) for v in VS}
CHECKS_OF = {s: tuple(v for v in VS if s in CHECKS[v]) for s in range(N33)}
UNION = {l: tuple(sorted(set(m for v in CHECKS_OF[l] for m in CHECKS[v]))) for l in LS}
S_GAUSS = frozenset(p for p in product((0, 1), repeat=N33)
                    if all(sum(p[m] for m in CHECKS[v]) % 2 == 0 for v in VS))


# ---------------------------------------------------------------- rate laws
def lam_unif(s, formed, vals, nbrs):
    return Fr(1)


def lam_count(s, formed, vals, nbrs):
    return 1 + Fr(sum(1 for y in nbrs[s] if y in formed))


def lam_count_sq(s, formed, vals, nbrs):
    k = sum(1 for y in nbrs[s] if y in formed)
    return Fr((1 + k) * (1 + k))


def lam_inv(s, formed, vals, nbrs):
    return Fr(1, 1 + sum(1 for y in nbrs[s] if y in formed))


def lam_value(s, formed, vals, nbrs):
    rec = [vals[y] for y in nbrs[s] if y in formed]
    agree = sum(1 for i in range(len(rec)) for j in range(i + 1, len(rec)) if rec[i] == rec[j])
    return 1 + Fr(agree)


def order_prob(order, lam, nbrs, vals=None):
    """Exact probability of one formation order under the race with rate law lam.
    vals: full value assignment driving a value-dependent law (values of formed sites)."""
    n = len(order)
    formed = set()
    p = Fr(1)
    for s in order:
        tot = sum(lam(t, formed, vals, nbrs) for t in range(n) if t not in formed)
        p *= lam(s, formed, vals, nbrs) / tot
        formed.add(s)
    return p


# ---------------------------------------------------------------- section 1
print("== 1. Windows and induced order laws ==")
check("windows: 2x3 has 6 sites and 7 edges; 3x3 roles V=4, L=4, P=1, each L in two checks; |S_Gauss| = 32",
      N23 == 6 and len(ED23) == 7 and (len(VS), len(LS), ROLE.count("P")) == (4, 4, 1)
      and all(len(CHECKS_OF[l]) == 2 for l in LS) and len(S_GAUSS) == 32)
ALL_ORDERS = list(permutations(range(N23)))
probs_u = [order_prob(o, lam_unif, NB23) for o in ALL_ORDERS]
check("uniform rate: the race law is the uniform order law, every one of the 720 orders has mass 1/720",
      len(ALL_ORDERS) == 720 and min(probs_u) == max(probs_u) == Fr(1, 720) and sum(probs_u) == 1)
probs_c = [order_prob(o, lam_count, NB23) for o in ALL_ORDERS]
check("count rate 1 + k: the induced order law is normalised and is not exchangeable",
      sum(probs_c) == 1 and min(probs_c) < Fr(1, 720) < max(probs_c),
      "min " + str(min(probs_c)) + ", max " + str(max(probs_c)) + " against 1/720")
g23 = {IDX23[(r, c)]: IDX23[(1 - r, 2 - c)] for (r, c) in S23}
check("count rate: the order law is covariant under the 180-degree window rotation on 6 sampled orders",
      all(order_prob(tuple(g23[s] for s in o), lam_count, NB23) == order_prob(o, lam_count, NB23)
          for o in ALL_ORDERS[::137][:6]))
VFULL_P = tuple(1 for _ in range(N23))
VFULL_M = tuple(-1 if i % 2 else 1 for i in range(N23))
check("value rate: driven by any fixed full value pattern, the race masses sum to 1 over all 720 orders",
      sum(order_prob(o, lam_value, NB23, VFULL_P) for o in ALL_ORDERS) == 1
      and sum(order_prob(o, lam_value, NB23, VFULL_M) for o in ALL_ORDERS) == 1,
      "the race factors telescope: clocks spend no probability on values")

# ---------------------------------------------------------------- section 2
print()
print("== 2. Record-level invisibility for the chain rule of a positive measure ==")
MU_W = {v: Fr(2) ** sum(1 for i, j in ED23 if v[i] == v[j]) for v in product((1, -1), repeat=N23)}
Z_MU = sum(MU_W.values())
MU = {v: w / Z_MU for v, w in MU_W.items()}
_W_CACHE = {}


def W_part(part):
    """Total mu-weight of all completions of a partial value assignment."""
    if part in _W_CACHE:
        return _W_CACHE[part]
    unk = [i for i in range(N23) if part[i] is None]
    tot = Fr(0)
    for fill in product((1, -1), repeat=len(unk)):
        v = list(part)
        for i, b in zip(unk, fill):
            v[i] = b
        tot += MU_W[tuple(v)]
    _W_CACHE[part] = tot
    return tot


def r_chain(a, s, part):
    """Chain rule of mu: condition on every formed site."""
    return W_part(part[:s] + (a,) + part[s + 1:]) / W_part(part)


def r_nn(a, s, part):
    """Nearest-neighbour rule: r(a) proportional to 2^(formed neighbours with value a)."""
    ka = sum(1 for y in NB23[s] if part[y] == a)
    kb = sum(1 for y in NB23[s] if part[y] == -a)
    return Fr(2) ** ka / (Fr(2) ** ka + Fr(2) ** kb)


def finished_law(rule, lam):
    """Exact finished-record law of the race + rule process, by dynamic programming
    over partial value assignments (None = unformed)."""
    layer = {tuple([None] * N23): Fr(1)}
    for _ in range(N23):
        nxt = {}
        for part, mass in layer.items():
            formed = {i for i in range(N23) if part[i] is not None}
            unformed = [i for i in range(N23) if part[i] is None]
            tot = sum(lam(t, formed, part, NB23) for t in unformed)
            for s in unformed:
                race = lam(s, formed, part, NB23) / tot
                for a in (1, -1):
                    p = rule(a, s, part)
                    if p == 0:
                        continue
                    q = part[:s] + (a,) + part[s + 1:]
                    nxt[q] = nxt.get(q, Fr(0)) + mass * race * p
        layer = nxt
    return layer


def law_by_order(rule, order):
    """Finished law for one fixed formation order (no race)."""
    layer = {tuple([None] * N23): Fr(1)}
    for s in order:
        nxt = {}
        for part, mass in layer.items():
            for a in (1, -1):
                p = rule(a, s, part)
                if p == 0:
                    continue
                q = part[:s] + (a,) + part[s + 1:]
                nxt[q] = nxt.get(q, Fr(0)) + mass * p
        layer = nxt
    return layer


check("mu is a positive normalised pair measure, invariant under the flip and the 180-degree rotation",
      sum(MU.values()) == 1 and all(w > 0 for w in MU.values())
      and all(MU[v] == MU[tuple(-x for x in v)] for v in MU)
      and all(MU[v] == MU[tuple(v[g23[i]] for i in range(N23))] for v in MU))
ORDERS_3 = [tuple(range(N23)), tuple(reversed(range(N23))), (2, 0, 4, 5, 1, 3)]
check("the chain rule is order-blind: the finished law equals mu for three explicit orders, all 64 atoms",
      all(law_by_order(r_chain, o) == MU for o in ORDERS_3))
check("invisibility: under the chain rule the race law is mu for the count, value and inverse-count clocks",
      finished_law(r_chain, lam_count) == MU and finished_law(r_chain, lam_value) == MU
      and finished_law(r_chain, lam_inv) == MU,
      "no covariant rate law leaves any record trace when the conditional rule is order-blind")

print()
print("== 3. Record-level visibility for the nearest-neighbour rule ==")
L_U = finished_law(r_nn, lam_unif)
L_C = finished_law(r_nn, lam_count)
L_V = finished_law(r_nn, lam_value)


def tv(p, q):
    keys = set(p) | set(q)
    return sum(abs(p.get(k, Fr(0)) - q.get(k, Fr(0))) for k in keys) / 2


def e_agree(law):
    return sum(m * sum(1 for i, j in ED23 if v[i] == v[j]) for v, m in law.items())


check("the three race laws are normalised and flip-covariant (value clock included)",
      all(sum(L.values()) == 1 for L in (L_U, L_C, L_V))
      and all(L[v] == L[tuple(-x for x in v)] for L in (L_U, L_C, L_V) for v in L))
print(f"   E[agreeing edges]: uniform {e_agree(L_U)}, count {e_agree(L_C)}, value {e_agree(L_V)}, static mu {e_agree(MU)}")
print(f"   TV distances: unif-count {tv(L_U, L_C)}, unif-value {tv(L_U, L_V)}, count-value {tv(L_C, L_V)}")
check("clocks are visible: the count and value clocks shift the finished law of the NN rule (TV > 0)",
      (tv(L_U,L_C),tv(L_U,L_V),tv(L_C,L_V)) == (Fr(29995127,3429216000),Fr(201911,43740000),Fr(29140541,6429780000)))
check("the agreement statistic separates the clocks pairwise and from the static measure",
      tuple(e_agree(L) for L in (L_U,L_C,L_V,MU)) == (Fr(16780559,3645000),Fr(4956001733,1071630000),Fr(126083753,27337500),Fr(2696,561)))

# ---------------------------------------------------------------- section 4
print()
print("== 4. The plane hard-support rule: hole mass across clocks ==")


def is_double_closure(s, F):
    """Forming s with formed set F closes both checks of an L site."""
    return ROLE[s] == "L" and all(m in F or m == s for m in UNION[s])


def d_of_order(order):
    formed = set()
    d = 0
    for s in order:
        if is_double_closure(s, formed):
            d += 1
        formed.add(s)
    return d


def plane_d_hist(lam):
    """Exact distribution of d under the race with rate law lam (subset DP, 512 x 3 states)."""
    layer = {(frozenset(), 0): Fr(1)}
    for _ in range(N33):
        nxt = {}
        for (F, d), mass in layer.items():
            tot = sum(lam(t, F, None, NB33) for t in range(N33) if t not in F)
            for s in range(N33):
                if s in F:
                    continue
                race = lam(s, F, None, NB33) / tot
                key = (F | {s}, d + (1 if is_double_closure(s, F) else 0))
                nxt[key] = nxt.get(key, Fr(0)) + mass * race
        layer = nxt
    hist = {}
    for (F, d), mass in layer.items():
        hist[d] = hist.get(d, Fr(0)) + mass
    return hist


def plane_completion_mass(lam):
    """Second DP using the same closure identity: absorb the 1/2 compatibility coin at each double closure."""
    layer = {frozenset(): Fr(1)}
    for _ in range(N33):
        nxt = {}
        for F, mass in layer.items():
            tot = sum(lam(t, F, None, NB33) for t in range(N33) if t not in F)
            for s in range(N33):
                if s in F:
                    continue
                w = mass * lam(s, F, None, NB33) / tot
                if is_double_closure(s, F):
                    w /= 2
                key = F | {s}
                nxt[key] = nxt.get(key, Fr(0)) + w
        layer = nxt
    return sum(layer.values())


def hole_sim_all_coins(order):
    """All 512 coin vectors: closures force parities; conflicting double closure fails.
    Returns (number of fully recorded coin vectors, pattern -> multiplicity)."""
    nfull, pats = 0, {}
    for coins in product((0, 1), repeat=N33):
        vals, formed, ok = [None] * N33, set(), True
        for s in order:
            closing = [v for v in CHECKS_OF[s] if all(m in formed or m == s for m in CHECKS[v])]
            if not closing:
                vals[s] = coins[s]
            else:
                req = {(-sum(vals[m] for m in CHECKS[v] if m != s)) % 2 for v in closing}
                if len(req) > 1:
                    ok = False
                    break
                vals[s] = req.pop()
            formed.add(s)
        if ok:
            nfull += 1
            t = tuple(vals)
            pats[t] = pats.get(t, 0) + 1
    return nfull, pats


HIST_U = plane_d_hist(lam_unif)
E_U = sum(m / 2 ** d for d, m in HIST_U.items())
check("uniform clock: d-histogram (3/10, 3/5, 1/10), completion mass E[2^-d] = 5/8, matching the support-rule note",
      HIST_U == {0: Fr(3, 10), 1: Fr(3, 5), 2: Fr(1, 10)} and E_U == Fr(5, 8)
      and plane_completion_mass(lam_unif) == Fr(5, 8))
E_BY_LAW = {}
for name, lam in (("count", lam_count), ("count^2", lam_count_sq), ("1/(1+k)", lam_inv)):
    h = plane_d_hist(lam)
    e = sum(m / 2 ** d for d, m in h.items())
    ok_pair = (sum(h.values()) == 1 and plane_completion_mass(lam) == e)
    E_BY_LAW[name] = (e, ok_pair, h)
print("   completion masses: uniform 5/8 = 0.625; "
      + "; ".join(f"{k} {v[0]} = {float(v[0]):.6f}" for k, v in E_BY_LAW.items()))
check("count, count^2 and inverse-count clocks: histogram DP and absorbed-coin DP agree on the completion mass",
      all(v[1] for v in E_BY_LAW.values()))
check("the completion mass is clock-sensitive: all four covariant rate laws give different exact values",
      len({Fr(5, 8)} | {v[0] for v in E_BY_LAW.values()}) == 4,
      "the hole mass of an order-blind hard-support rule reads the clock")
g33 = {IDX33[(r, c)]: IDX33[(c, 2 - r)] for (r, c) in S33}
check("rate covariance on the plane: the count law is invariant under the 90-degree window rotation (samples)",
      all(lam_count(g33[s], frozenset(g33[t] for t in F), None, NB33) == lam_count(s, F, None, NB33)
          for s, F in ((0, frozenset((1, 3))), (4, frozenset((1, 5, 7))), (2, frozenset()), (7, frozenset((4, 6, 8))))))
O_D0 = tuple(LS + [s for s in range(N33) if s not in LS])
O_D1 = tuple([LS[3]] + [s for s in range(N33) if s not in (LS[0], LS[3])] + [LS[0]])
O_D2 = tuple([s for s in range(N33) if s not in (LS[0], LS[3])] + [LS[0], LS[3]])
check("explicit orders reach d = 0, 1, 2 (links early; one link last; two opposite links last)",
      d_of_order(O_D0) == 0 and d_of_order(O_D1) == 1 and d_of_order(O_D2) == 2)
ok_sim = True
for o in (O_D0, O_D1, O_D2):
    nf, pats = hole_sim_all_coins(o)
    d = d_of_order(o)
    ok_sim = ok_sim and nf == 512 // 2 ** d and frozenset(pats) == S_GAUSS and len(set(pats.values())) == 1
check("per order, over all 512 coins: completion fraction 2^-d, patterns exactly S_Gauss, uniform multiplicity",
      ok_sim,
      "conditional on completion the record law is uniform for every value-blind clock (mixture of uniforms)")


# ---------------------------------------------------------------- section 5
print()
print("== 5. Independent routes and bindings ==")


def two_step(rule, s1, a1, s2, a2, part):
    p1 = rule(a1, s1, part)
    q = part[:s1] + (a1,) + part[s1 + 1:]
    return p1 * rule(a2, s2, q)


PART0 = (1,) + tuple([None] * (N23 - 1))
check("exchange identity (formation-order block): the chain rule commutes on sampled pairs, the NN rule does not",
      all(two_step(r_chain, s1, a1, s2, a2, part) == two_step(r_chain, s2, a2, s1, a1, part)
          for part in (tuple([None] * N23), PART0)
          for (s1, a1, s2, a2) in ((1, -1, 4, -1), (1, 1, 4, -1), (2, 1, 5, 1)))
      and two_step(r_nn, 1, -1, 4, -1, PART0) != two_step(r_nn, 4, -1, 1, -1, PART0),
      "the order sensitivity that the clock reads is exactly the failed exchange identity")
check("invisibility extends to the count^2 clock as well",
      finished_law(r_chain, lam_count_sq) == MU)
L_U_DIRECT = {}
for o in ALL_ORDERS:
    for v, m in law_by_order(r_nn, o).items():
        L_U_DIRECT[v] = L_U_DIRECT.get(v, Fr(0)) + m
L_U_DIRECT = {v: m / 720 for v, m in L_U_DIRECT.items()}
check("independent route: the uniform-clock NN law equals the uniform mixture of all 720 fixed-order laws",
      L_U_DIRECT == L_U)
CNT_9F = {}
for perm in permutations(range(N33)):
    d = d_of_order(perm)
    CNT_9F[d] = CNT_9F.get(d, 0) + 1
check("independent route: direct enumeration of all 9! orders reproduces the d-counts 108864, 217728, 36288",
      CNT_9F == {0: 108864, 1: 217728, 2: 36288},
      "the support-rule note's histogram, recomputed from scratch")
E_C = E_BY_LAW["count"][0]
E_SQ = E_BY_LAW["count^2"][0]
E_IN = E_BY_LAW["1/(1+k)"][0]
ED_ALL = {n: sum(Fr(d) * m for d, m in v[2].items()) for n, v in E_BY_LAW.items()}
ED_ALL["uniform"] = sum(Fr(d) * m for d, m in HIST_U.items())
print("   E[d]: uniform " + str(ED_ALL["uniform"]) + "; count " + str(ED_ALL["count"])
      + "; count^2 " + str(ED_ALL["count^2"]) + "; 1/(1+k) " + str(ED_ALL["1/(1+k)"]))
check("eagerness ordering, exactly: count^2 > count > uniform > inverse-count in completion mass; E[d] = 4/5 uniform",
      E_SQ > E_C > Fr(5, 8) > E_IN and ED_ALL["uniform"] == Fr(4, 5)
      and ED_ALL["count^2"] < ED_ALL["count"] < Fr(4, 5) < ED_ALL["1/(1+k)"],
      "cluster-eager clocks complete checks before links can close them; frontier-averse clocks do the opposite")

print()
print('per_element: Exact finite arithmetic verifies the declared algebraic identities and explicit model comparisons; it does not select physical axioms.')
print('per_site: The supplied finite windows, alphabets and conditional rules fix the scope; other local laws and representations remain unclassified.')
print('per_mode: Analytic statements require the explicit assumptions and proofs in the note; finite sample checks alone do not establish a universal theorem.')
print('per_block: The fresh runner output certifies the implemented finite controls; historical author mutation tables are provenance rather than fresh review evidence.')
print('lattice_wide: No continuum limit, physical field identification, universal law selection or retained audit status is established by this finite certificate.')
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
