#!/usr/bin/env python3
"""Order-blind formation with zeros and holes under the unsoldered reading:
never-failing rules are constant, strict order-blindness has an exact pair
form, and order-blind variation needs holes.  Exact and finite.

Supplied conditional finite models; no physical formation law is inferred.  Exact rational arithmetic; no floating point.

Declared objects
  * Z^3 windows: the 3-site bent path (a site with two perpendicular
    neighbours), the 4-site star, the 7-site cross, and the 8-site path;
  * sub-probability nearest-neighbour rules r(. | N): for each neighbour
    condition N (formed neighbours and their values) a vector of masses
    with sum <= 1; the deficit is the probability that formation fails at
    that step (a hole); a rule never fails when every sum is 1;
  * strict order-blindness: every formation order gives the same finished
    sub-law on completed configurations, including its total mass;
  * unsoldered covariance: rotating formed neighbours' positions with
    their values fixed leaves the rule unchanged, so a single formed
    neighbour's conditional is direction-free; the example rules are
    direction-blind (they see the multiset of formed values);
  * example rules on the binary alphabet {+1, -1} and the six-axis
    alphabet: copy-when-unanimous (never fails, has zeros), rejection
    exclusion (draw from the one-site law, fail if a formed neighbour holds
    the same value), forcing exclusion (take the opposite of unanimous
    formed neighbours, fail if they disagree).

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
from fractions import Fraction as Fr
from itertools import combinations, permutations, product

AUDIT_TIMEOUT_SEC = 120
RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


def vadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


EX, EY, EZ = (1, 0, 0), (0, 1, 0), (0, 0, 1)
DIRS = (EX, (-1, 0, 0), EY, (0, -1, 0), EZ, (0, 0, -1))
O0 = (0, 0, 0)
BENT = (O0, EX, EY)
STAR4 = (O0, EX, EY, EZ)
CROSS = (O0,) + DIRS


def nbr_values(site, formed):
    """Unsoldered: the multiset (sorted tuple) of formed neighbour values."""
    return tuple(sorted(formed[vadd(site, d)] for d in DIRS if vadd(site, d) in formed))


def sub_law(sites, alphabet, rule, order):
    """Exact finished sub-law of one order: dict config -> mass (failed histories dropped)."""
    layer = {(): Fr(1)}
    pos = {s: i for i, s in enumerate(order)}
    for s in order:
        nxt = {}
        for part, mass in layer.items():
            formed = {order[i]: part[i] for i in range(len(part))}
            probs = rule(nbr_values(s, formed))
            for a in alphabet:
                p = probs.get(a, Fr(0))
                if p:
                    nxt[part + (a,)] = nxt.get(part + (a,), Fr(0)) + mass * p
        layer = nxt
    out = {}
    for part, mass in layer.items():
        cfg = tuple(part[pos[s]] for s in sites)
        out[cfg] = out.get(cfg, Fr(0)) + mass
    return out


B2 = (1, -1)
HALF = Fr(1, 2)


def copy_unanimous(vals):
    if not vals or len(set(vals)) > 1:
        return {1: HALF, -1: HALF}
    return {vals[0]: Fr(1)}


print("== 1. Never-failing rules with zeros: constant, or order-sensitive ==")
check("copy-when-unanimous never fails, has zeros, and varies with its neighbour conditions",
      all(sum(copy_unanimous(v).values()) == 1 for v in ((), (1,), (-1,), (1, -1), (1, 1)))
      and copy_unanimous((1,)) == {1: Fr(1)} and copy_unanimous(()) == {1: HALF, -1: HALF})
RHO = {(b, a): copy_unanimous((a,)).get(b, Fr(0)) for a in B2 for b in B2}
E1 = sum(HALF * RHO[(1, a)] for a in B2)
E2 = sum(HALF * RHO[(1, a)] ** 2 for a in B2)
check("variance identity on the bent path: E[rho(+|.)] = 1/2 = r0(+) but E[rho(+|.)^2] = 1/2, not 1/4",
      E1 == HALF and E2 == HALF and E2 - E1 ** 2 == Fr(1, 4),
      "order-blindness would need two equal neighbours to give E[rho^2] = r0(+)^2; the gap is Var = 1/4")
L_LEAVES = sub_law(BENT, B2, copy_unanimous, (EX, EY, O0))
L_CENTRE = sub_law(BENT, B2, copy_unanimous, (O0, EX, EY))
P_DIFF = lambda L: sum(m for c, m in L.items() if c[1] != c[2])
check("so it is order-sensitive: leaves-first the two leaves differ with probability 1/2, centre-first never",
      P_DIFF(L_LEAVES) == HALF and P_DIFF(L_CENTRE) == 0
      and sum(L_LEAVES.values()) == 1 == sum(L_CENTRE.values()))


def rejection(alphabet):
    r0 = Fr(1, len(alphabet))

    def rule(vals):
        return {a: r0 for a in alphabet if a not in vals}
    return rule


def forcing_binary(vals):
    if not vals:
        return {1: HALF, -1: HALF}
    if len(set(vals)) > 1:
        return {}
    return {-vals[0]: Fr(1)}


print()
print("== 2. Holes: strict order-blindness has an exact pair form; forcing does not ==")
REJ2 = rejection(B2)
CROSS_ORDERS = list(permutations(CROSS))
REJ_LAWS = [sub_law(CROSS, B2, REJ2, o) for o in CROSS_ORDERS]
BASE = REJ_LAWS[0]
check("binary rejection exclusion on the 7-site cross: all 5040 orders give one sub-law, total mass 1/64",
      len(CROSS_ORDERS) == 5040 and all(L == BASE for L in REJ_LAWS) and sum(BASE.values()) == Fr(1, 64)
      and set(BASE.values()) == {Fr(1, 128)} and len(BASE) == 2,
      "two completed configurations (centre a, every leaf -a), each 1/128: clock-blind in how often and in what")
FORCE_Z = {sum(sub_law(CROSS, B2, forcing_binary, o).values()) for o in CROSS_ORDERS}
FORCE_COND = {tuple(sorted(sub_law(CROSS, B2, forcing_binary, o).values())) for o in CROSS_ORDERS[::97]}
check("forcing exclusion on the cross: the completion mass depends on the order, the completed law does not",
      min(FORCE_Z) == Fr(1, 32) and max(FORCE_Z) == 1 and len(FORCE_Z) > 2
      and all(len(set(v)) == 1 and len(v) == 2 for v in FORCE_COND),
      f"{len(FORCE_Z)} distinct completion masses from 1/32 (leaves first) to 1 (centre first)")
LAM = Fr(3, 4)


def soft_pair(vals):
    """Pair weights K(a, b) = (3/4)(1 + a b / 3): r(a | N) = r0(a) prod K(a, b)."""
    out = {}
    for a in B2:
        p = HALF
        for b in vals:
            p *= LAM * (1 + Fr(a * b, 3))
        out[a] = p
    return out


PARTIAL_MAPS = [vals for k in range(7) for vals in product(B2, repeat=k)]
check("pair form: rejection and soft rules equal r0(a) prod K(a, b_i) with symmetric K on all 127 value lists",
      all(REJ2(tuple(sorted(v))) == {a: HALF for a in B2 if all(a != b for b in v)} for v in PARTIAL_MAPS)
      and all(soft_pair(tuple(sorted(v)))[a] == HALF * __import__("math").prod([LAM * (1 + Fr(a * b, 3)) for b in v])
              for v in PARTIAL_MAPS for a in B2),
      "K_rej(a, b) = 1[a != b]; K_soft(a, b) = (3/4)(1 + ab/3) = K_soft(b, a)")
check("both are sub-probabilities on every neighbour condition; the soft rule's worst case (6 equal values) is 65/128",
      all(sum(REJ2(tuple(sorted(v))).values()) <= 1 for v in PARTIAL_MAPS)
      and max(sum(soft_pair(tuple(sorted(v))).values()) for v in PARTIAL_MAPS) == 1
      and sum(soft_pair((1,) * 6).values()) == Fr(65, 128))
K_FORCE = {(a, b): forcing_binary((a,)).get(b, Fr(0)) / HALF for a in B2 for b in B2}
check("forcing is not of pair form: its one-neighbour K = 2 1[a != b] would give mass 2 to two equal neighbours",
      K_FORCE[(1, -1)] == 2 and sum(HALF * K_FORCE[(a, 1)] ** 2 for a in B2) == 2)
SOFT_LAWS = [sub_law(CROSS, B2, soft_pair, o) for o in CROSS_ORDERS]
check("soft pair rule on the 7-site cross: all 5040 orders give one sub-law (strictly order-blind, and it varies)",
      all(L == SOFT_LAWS[0] for L in SOFT_LAWS) and soft_pair((1,)) != soft_pair(()),
      f"completion mass {sum(SOFT_LAWS[0].values())} = (3/4)^6, the same for every order")

print()
print("== 3. Completed records of order-blind hole rules: the static pair law returns ==")
PATH8 = tuple((0, 0, z) for z in range(8))
P8_ORDERS = [PATH8, tuple(reversed(PATH8)), PATH8[::2] + PATH8[1::2], (PATH8[3], PATH8[7], PATH8[0], PATH8[5], PATH8[1], PATH8[6], PATH8[2], PATH8[4])]
SOFT8 = [sub_law(PATH8, B2, soft_pair, o) for o in P8_ORDERS]
Z8 = sum(SOFT8[0].values())
MU_W = {c: Fr(2) ** sum(1 for i in range(7) if c[i] == c[i + 1]) for c in product(B2, repeat=8)}
MU = {c: w / sum(MU_W.values()) for c, w in MU_W.items()}
COND8 = {c: m / Z8 for c, m in SOFT8[0].items()}


def corr(law, i, j):
    return sum(m * c[i] * c[j] for c, m in law.items()) - sum(m * c[i] for c, m in law.items()) * sum(m * c[j] for c, m in law.items())


check("8-site path, four orders: one sub-law, completion (3/4)^7 = 2187/16384, completed law = the static pair measure",
      all(L == SOFT8[0] for L in SOFT8) and Z8 == Fr(2187, 16384) and COND8 == MU,
      "the nearest-neighbour pair measure 2^(agreeing bonds) is the completed-record law of an order-blind hole rule")
check("so its completed records correlate at every distance: c(0, d) = 3^-d for d = 1..7 (all means exactly 0)",
      all(corr(COND8, 0, d) == Fr(1, 3 ** d) for d in range(1, 8))
      and all(sum(m * c[i] for c, m in COND8.items()) == 0 for i in range(8)))
REJ8 = sub_law(PATH8, B2, REJ2, PATH8)
check("binary rejection on the 8-site path: completion 1/128, completed records the two staggered patterns",
      sum(REJ8.values()) == Fr(1, 128) and len(REJ8) == 2
      and all(c[i] == -c[i + 1] for c in REJ8 for i in range(7)) and corr({c: m * 128 for c, m in REJ8.items()}, 0, 7) == -1,
      "exact staggered order at every distance, with hole mass 127/128")
SIX = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
REJ6 = rejection(SIX)
BENT6 = [sub_law(BENT, SIX, REJ6, o) for o in permutations(BENT)]
STAR6 = [sub_law(STAR4, SIX, REJ6, o) for o in permutations(STAR4)]
ZS = sum(STAR6[0].values())
EQ_LEAVES = sum(m for c, m in STAR6[0].items() if c[1] == c[2]) / ZS
check("six-axis rejection (proper colourings): one sub-law for all orders of the bent path (6) and 4-site star (24)",
      all(L == BENT6[0] for L in BENT6) and all(L == STAR6[0] for L in STAR6)
      and ZS == Fr(125, 216) and EQ_LEAVES == Fr(1, 5),
      "star completion (5/6)^3; two leaves at distance 2 agree with probability 1/5, not 1/6")
P4 = tuple((0, 0, z) for z in range(4))
L6P = sub_law(P4, SIX, REJ6, P4)
Z6P = sum(L6P.values())
EQ2 = sum(m for c, m in L6P.items() if c[0] == c[2]) / Z6P
EQ3 = sum(m for c, m in L6P.items() if c[0] == c[3]) / Z6P
check("six-axis rejection on a 4-site path: agreement (1/6)(1 + 5(-1/5)^d) = 1/5 at d = 2, 4/25 at d = 3",
      EQ2 == Fr(1, 5) and EQ3 == Fr(4, 25) and Z6P == Fr(125, 216))

print()
print("per_element: checked the finite configurations and arithmetic controls explicitly enumerated above")
print("per_site: checked the declared finite-window local rules under their supplied sampling conventions")
print("per_mode: checked and not executed — no infinite-volume Fourier or spectral mode computation is performed")
print("per_block: checked only the listed finite windows and orders; proofs beyond those runs are source arguments")
print("lattice_wide: checked and not executed — no infinite-lattice formation process or physical completion is simulated")
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
