#!/usr/bin/env python3
"""Formation unit: sequential single-site against joint covariant-set
formation with the joint law stated, exact and finite.

Wave C (formation-unit) of the TOE derivation campaign by underdetermination
witnesses.  Exact rational arithmetic throughout; no floating point.

Declared objects
  * windows: the 2x2x2 cube (8 sites, 12 edges), the 2x3 rectangle and the
    3x3 parity-role plane of the landed support-rule note;
  * units: single sites; the cube's two site-plus-all-in-window-neighbour
    units U0 = {000, 100, 010, 001} and U1 = {111, 011, 101, 110} (the
    in-window restriction of the proposed site-plus-six-neighbours unit,
    partitioning the window); the 2x3 site-plus-neighbours unit; plane
    partitions aligned and misaligned with the Gauss checks;
  * joint laws, each stated: PRODUCT FILL, every site of the forming unit
    draws from its conditional given the previously formed exterior alone,
    independently within the unit; BLOCK CHAIN, the forming unit draws its
    joint pattern from the conditional of the pair measure mu given all
    previously formed sites (unformed sites marginalised); GROUPED CHAIN,
    a fixed internal order within the unit conditioning on everything
    formed so far, which is a sequential process by construction;
  * conditional rules: the chain rule of mu proportional to 2^(agreeing
    edges) and the local nearest-neighbour rule r(a) proportional to
    2^(formed neighbours with value a), as in the clock-and-rate block;
  * the plane hard-support joint law: a forming unit draws uniformly from
    its patterns consistent with every check its formation completes,
    given the recorded exterior; no consistent pattern is a hole.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
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
def cube_window():
    sites = list(product((0, 1), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    nbrs = []
    for s in sites:
        out = []
        for d in range(3):
            t = list(s)
            t[d] ^= 1
            out.append(idx[tuple(t)])
        nbrs.append(tuple(out))
    edges = sorted({tuple(sorted((i, j))) for i in range(8) for j in nbrs[i]})
    return sites, idx, nbrs, edges


CS, CIDX, CNB, CED = cube_window()
NC = 8
U0 = frozenset([CIDX[(0, 0, 0)]] + list(CNB[CIDX[(0, 0, 0)]]))
U1 = frozenset(range(NC)) - U0


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


S23, I23, NB23, ED23 = grid_window(2, 3)
N23 = 6
S33, I33, NB33, ED33 = grid_window(3, 3)
N33 = 9
ROLE = ["VLPC"[(r % 2) + (c % 2)] for (r, c) in S33]
VS = [i for i, x in enumerate(ROLE) if x == "V"]
LS = [i for i, x in enumerate(ROLE) if x == "L"]
CHECKS = {v: tuple([v] + [u for u in NB33[v] if ROLE[u] == "L"]) for v in VS}
S_GAUSS = frozenset(p for p in product((0, 1), repeat=N33)
                    if all(sum(p[m] for m in CHECKS[v]) % 2 == 0 for v in VS))


# ---------------------------------------------------------------- rules on a window
def make_mu(n, edges):
    w = {v: Fr(2) ** sum(1 for i, j in edges if v[i] == v[j]) for v in product((1, -1), repeat=n)}
    z = sum(w.values())
    return w, {v: x / z for v, x in w.items()}


MUW_C, MU_C = make_mu(NC, CED)
MUW_23, MU_23 = make_mu(N23, ED23)


def make_W(n, muw):
    cache = {}

    def W(part):
        if part in cache:
            return cache[part]
        unk = [i for i in range(n) if part[i] is None]
        tot = Fr(0)
        for fill in product((1, -1), repeat=len(unk)):
            v = list(part)
            for i, b in zip(unk, fill):
                v[i] = b
            tot += muw[tuple(v)]
        cache[part] = tot
        return tot

    return W


W_C = make_W(NC, MUW_C)
W_23 = make_W(N23, MUW_23)


def r_chain(W):
    def r(a, s, part):
        return W(part[:s] + (a,) + part[s + 1:]) / W(part)
    return r


def r_nn(nbrs):
    def r(a, s, part):
        ka = sum(1 for y in nbrs[s] if part[y] == a)
        kb = sum(1 for y in nbrs[s] if part[y] == -a)
        return Fr(2) ** ka / (Fr(2) ** ka + Fr(2) ** kb)
    return r


RC_C, RN_C = r_chain(W_C), r_nn(CNB)
RC_23, RN_23 = r_chain(W_23), r_nn(NB23)


# ---------------------------------------------------------------- processes
def law_sequential_uniform(n, rule):
    """Finished law of the single-site process under the uniform order race."""
    layer = {tuple([None] * n): Fr(1)}
    for _ in range(n):
        nxt = {}
        for part, mass in layer.items():
            unformed = [i for i in range(n) if part[i] is None]
            for s in unformed:
                for a in (1, -1):
                    p = rule(a, s, part)
                    if p == 0:
                        continue
                    q = part[:s] + (a,) + part[s + 1:]
                    nxt[q] = nxt.get(q, Fr(0)) + mass * Fr(1, len(unformed)) * p
        layer = nxt
    return layer


def law_by_order(n, rule, order):
    layer = {tuple([None] * n): Fr(1)}
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


def law_product_fill(n, rule, units):
    """Joint PRODUCT FILL: unit sites draw independently from their conditional
    given the formed exterior alone (the pre-unit partial assignment)."""
    layer = {tuple([None] * n): Fr(1)}
    for unit in units:
        us = sorted(unit)
        nxt = {}
        for part, mass in layer.items():
            for fill in product((1, -1), repeat=len(us)):
                p = mass
                for s, a in zip(us, fill):
                    p *= rule(a, s, part)
                if p == 0:
                    continue
                q = list(part)
                for s, a in zip(us, fill):
                    q[s] = a
                q = tuple(q)
                nxt[q] = nxt.get(q, Fr(0)) + p
        layer = nxt
    return layer


def law_block_chain(n, W, units):
    """Joint BLOCK CHAIN: the unit draws its pattern from mu conditioned on all
    formed sites, unformed sites marginalised: weight W(part with unit) / W(part)."""
    layer = {tuple([None] * n): Fr(1)}
    for unit in units:
        us = sorted(unit)
        nxt = {}
        for part, mass in layer.items():
            base = W(part)
            for fill in product((1, -1), repeat=len(us)):
                q = list(part)
                for s, a in zip(us, fill):
                    q[s] = a
                q = tuple(q)
                p = mass * W(q) / base
                if p == 0:
                    continue
                nxt[q] = nxt.get(q, Fr(0)) + p
        layer = nxt
    return layer


def mix(laws):
    out = {}
    w = Fr(1, len(laws))
    for L in laws:
        for v, m in L.items():
            out[v] = out.get(v, Fr(0)) + w * m
    return out


def e_agree(law, edges):
    return sum(m * sum(1 for i, j in edges if v[i] == v[j]) for v, m in law.items())


def e_agree_on(law, edge_set):
    return sum(m * sum(1 for i, j in edge_set if v[i] == v[j]) for v, m in law.items())


# ---------------------------------------------------------------- section 1
print("== 1. Windows, units, and stated joint laws ==")
check("cube: 8 sites, 12 edges; U0 = site 000 plus its three neighbours; U0, U1 partition the window",
      NC == 8 and len(CED) == 12 and len(U0) == 4 and U1 == frozenset(range(8)) - U0
      and all(len(CNB[s]) == 3 for s in range(8)),
      "U1 is the antipodal site-plus-neighbours unit: the six-neighbour proposal restricted in window")
check("plane: roles V=4, L=4, P=1; |S_Gauss| = 32; 2x3: 6 sites, 7 edges",
      (len(VS), len(LS), ROLE.count("P")) == (4, 4, 1) and len(S_GAUSS) == 32 and len(ED23) == 7)
ANTIP = {CIDX[s]: CIDX[tuple(1 - x for x in s)] for s in CS}
check("the unit pair is covariant: the antipodal map swaps U0 and U1; the diagonal C3 preserves each",
      frozenset(ANTIP[s] for s in U0) == U1
      and frozenset(CIDX[(s[1], s[2], s[0])] for s in (CS[i] for i in U0)) == U0
      and frozenset(CIDX[(s[1], s[2], s[0])] for s in (CS[i] for i in U1)) == U1)

# ---------------------------------------------------------------- section 2
print()
print("== 2. Block-chain joints equal the chain rule: the unit is invisible ==")
FLIP_C = {v: tuple(-x for x in v) for v in MU_C}
check("mu on the cube: positive, normalised, invariant under the flip and the diagonal C3 rotation",
      sum(MU_C.values()) == 1 and all(m > 0 for m in MU_C.values())
      and all(MU_C[v] == MU_C[FLIP_C[v]] for v in MU_C)
      and all(MU_C[v] == MU_C[tuple(v[CIDX[(CS[i][1], CS[i][2], CS[i][0])]] for i in range(NC))] for v in MU_C))
check("single-site chain rule: the uniform race and two explicit orders all give exactly mu (256 atoms)",
      law_sequential_uniform(NC, RC_C) == MU_C
      and law_by_order(NC, RC_C, tuple(range(NC))) == MU_C
      and law_by_order(NC, RC_C, (7, 2, 5, 0, 3, 6, 1, 4)) == MU_C)
check("block chain over the covariant units: both unit orders give exactly mu on the cube",
      law_block_chain(NC, W_C, (U0, U1)) == MU_C and law_block_chain(NC, W_C, (U1, U0)) == MU_C,
      "the stated joint law equals the sequential law: the formation unit is invisible for chain content")
U23A = frozenset((1, 0, 2, 4))
U23B = frozenset((3, 5))
check("2x3 site-plus-neighbours unit: block chain equals mu in both unit orders (64 atoms)",
      law_block_chain(N23, W_23, (U23A, U23B)) == MU_23
      and law_block_chain(N23, W_23, (U23B, U23A)) == MU_23)

# ---------------------------------------------------------------- section 3
print()
print("== 3. Product-fill joints against sequential: the unit is visible ==")
L_SEQ = law_sequential_uniform(NC, RN_C)
L_P0 = law_product_fill(NC, RN_C, (U0, U1))
L_P1 = law_product_fill(NC, RN_C, (U1, U0))
L_PROD = mix([L_P0, L_P1])
GROUPED = tuple(sorted(U0)) + tuple(sorted(U1))
L_GRP = law_by_order(NC, RN_C, GROUPED)
check("the three laws are normalised and flip-covariant; the two product-fill unit orders are antipodal images",
      all(sum(L.values()) == 1 for L in (L_SEQ, L_PROD, L_GRP))
      and all(L[v] == L[FLIP_C[v]] for L in (L_SEQ, L_PROD, L_GRP) for v in L)
      and L_P1 == {tuple(v[ANTIP[i]] for i in range(NC)): m for v, m in L_P0.items()})
E_IN_U0 = [e for e in CED if e[0] in U0 and e[1] in U0]
E_CROSS = [e for e in CED if (e[0] in U0) != (e[1] in U0)]
check("cube edges split 3 + 6 + 3: inside U0, between the units, inside U1",
      len(E_IN_U0) == 3 and len(E_CROSS) == 6)
check("product fill erases intra-unit correlation: first-formed unit edges agree at exactly 1/2 each",
      e_agree_on(L_P0, E_IN_U0) == Fr(3, 2) and sum(1 for i, j in E_IN_U0) == 3,
      "under U0-first product fill the three U0 edges have iid fair endpoints")
EA = {"sequential": e_agree(L_SEQ, CED), "product": e_agree(L_PROD, CED),
      "grouped": e_agree(L_GRP, CED), "static mu": e_agree(MU_C, CED)}
print("   E[agreeing edges]: " + "; ".join(f"{k} {v} = {float(v):.5f}" for k, v in EA.items()))
check("the formation unit is visible for the local rule: sequential, product-fill and grouped laws differ",
      L_SEQ != L_PROD and L_SEQ != L_GRP and L_PROD != L_GRP and len(set(EA.values())) == 4,
      "the agreement statistic separates all three processes and the static measure")
check("sanity: none of the local-rule laws equals mu",
      L_SEQ != MU_C and L_PROD != MU_C and L_GRP != MU_C)

# ---------------------------------------------------------------- section 4
print()
print("== 4. The plane hard-support: the unit is a dial the hole mass reads ==")


def plane_unit_process(units):
    """Stated joint law: each forming unit draws uniformly from its patterns
    consistent with every check its formation completes, given the recorded
    exterior; a unit with no consistent pattern retires the history as a hole."""
    layer = {tuple([None] * N33): Fr(1)}
    hole = Fr(0)
    for unit in units:
        us = sorted(unit)
        nxt = {}
        for part, mass in layer.items():
            formed = {i for i in range(N33) if part[i] is not None}
            newly = formed | set(us)
            completed = [v for v in VS
                         if set(CHECKS[v]) <= newly and not set(CHECKS[v]) <= formed]
            cons = []
            for fill in product((0, 1), repeat=len(us)):
                q = list(part)
                for s, a in zip(us, fill):
                    q[s] = a
                if all(sum(q[m] for m in CHECKS[v]) % 2 == 0 for v in completed):
                    cons.append(tuple(q))
            if not cons:
                hole += mass
                continue
            w = mass / len(cons)
            for q in cons:
                nxt[q] = nxt.get(q, Fr(0)) + w
        layer = nxt
    return layer, hole


CHECKS_OF = {s: tuple(v for v in VS if s in CHECKS[v]) for s in range(N33)}
UNION = {l: tuple(sorted(set(m for v in CHECKS_OF[l] for m in CHECKS[v]))) for l in LS}


def singleton_completion_mass():
    """Uniform single-site race: absorbed-coin subset DP as in the clock-and-rate block."""
    layer = {frozenset(): Fr(1)}
    for _ in range(N33):
        nxt = {}
        for F, mass in layer.items():
            rest = [s for s in range(N33) if s not in F]
            for s in rest:
                w = mass / len(rest)
                if ROLE[s] == "L" and all(m in F or m == s for m in UNION[s]):
                    w /= 2
                key = F | {s}
                nxt[key] = nxt.get(key, Fr(0)) + w
        layer = nxt
    return sum(layer.values())


A_AL = frozenset((I33[(0, 0)], I33[(0, 1)], I33[(1, 0)], I33[(0, 2)], I33[(1, 2)]))
B_AL = frozenset(range(N33)) - A_AL
LAW_AB, HOLE_AB = plane_unit_process((A_AL, B_AL))
LAW_BA, HOLE_BA = plane_unit_process((B_AL, A_AL))
check("aligned two-unit partition (checks of the top corners, then the rest): no hole in either unit order",
      HOLE_AB == 0 and HOLE_BA == 0)
check("aligned partition: both unit orders give the uniform law on the Gauss set (32 atoms at 1/32)",
      frozenset(LAW_AB) == S_GAUSS and set(LAW_AB.values()) == {Fr(1, 32)}
      and frozenset(LAW_BA) == S_GAUSS and set(LAW_BA.values()) == {Fr(1, 32)})
LAW_FULL, HOLE_FULL = plane_unit_process((frozenset(range(N33)),))
check("the whole window as one glued unit: no hole, uniform law on the Gauss set",
      HOLE_FULL == 0 and frozenset(LAW_FULL) == S_GAUSS and set(LAW_FULL.values()) == {Fr(1, 32)})
L01 = I33[(0, 1)]
P11 = I33[(1, 1)]
A_MIS = frozenset(s for s in range(N33) if s not in (L01, P11))
LAW_MIS, HOLE_MIS = plane_unit_process((A_MIS, frozenset((P11,)), frozenset((L01,))))
check("misaligned partition (the shared link forms last, alone): hole mass exactly 1/2",
      HOLE_MIS == Fr(1, 2),
      "the lone last unit completes two checks with one variable: over-determined half the time")
check("misaligned partition, conditional on completion: still the uniform law on the Gauss set",
      frozenset(LAW_MIS) == S_GAUSS and set((m / (1 - HOLE_MIS) for m in LAW_MIS.values())) == {Fr(1, 32)})
E_SINGLE = singleton_completion_mass()
check("single-site units under the uniform race: completion mass 5/8, the support-rule and clock-rate value",
      E_SINGLE == Fr(5, 8))
check("the formation unit is a dial the hole mass reads: 1 (aligned or whole-window) > 5/8 (sites) > 1/2 (link last)",
      Fr(1) > E_SINGLE > Fr(1, 2),
      "while every completed-record law stays uniform on the Gauss set: units change how often, never what")

print()
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
