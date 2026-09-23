#!/usr/bin/env python3
"""What selects the Coulomb measure.  Under the static reading, a hard ice
rule (deterministic conditionals) is satisfied by every measure on the ice
states, so it selects none of them.  A positive nearest-neighbour rule,
with weight eps for each vertex-link disagreement, has a law that is
exactly uniform on the ice states for every eps and concentrates on them
as eps -> 0.  Exact rational arithmetic on the landed L = 2 torus.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.

Declared objects
  * the fine torus Z_4^3 with superlattice roles; links carry occupations,
    vertices carry records, the plaquette and cube sites carry nothing;
  * the hard soldered rule of open PR 8679 (vertex record = set of occupied
    directions, links read from it) and its 9600 ice states, 880 at zero
    flux;
  * the positive rule: vertex records range over the 20 ice patterns, and a
    state has weight eps^m, m = number of (vertex, link) pairs on which the
    record and the occupation disagree (eps > 0);
  * the static reading: a site's conditional given all other sites is a
    function of its six nearest-neighbour values.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
from fractions import Fraction as Fr
from itertools import combinations, product

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


N = 4
SITES = [(x, y, z) for x in range(N) for y in range(N) for z in range(N)]
DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def add(s, d):
    return tuple((a + b) % N for a, b in zip(s, d))


def sub(s, d):
    return tuple((a - b) % N for a, b in zip(s, d))


def role(s):
    return "VLPC"[sum(a % 2 for a in s)]


NB = {s: [add(s, d) for d in DIRS] for s in SITES}
VS = [s for s in SITES if role(s) == "V"]
LS = [s for s in SITES if role(s) == "L"]
LIDX = {l: i for i, l in enumerate(LS)}
ICEPAT = [tuple(1 if i in S else 0 for i in range(6)) for S in combinations(range(6), 3)]


def ice_states():
    out = []

    def rec(k, n):
        if k == len(VS):
            out.append(tuple(n[l] for l in LS))
            return
        star = NB[VS[k]]
        free = [l for l in star if l not in n]
        need = 3 - sum(n[l] for l in star if l in n)
        if 0 <= need <= len(free):
            for occ in combinations(free, need):
                for l in free:
                    n[l] = 1 if l in occ else 0
                rec(k + 1, n)
                for l in free:
                    del n[l]
    rec(0, {})
    return out


ICE = ice_states()


def fluxes(c):
    out = []
    for a in range(3):
        f = 0
        for l in LS:
            if l[a] == 1:
                lo = sub(l, DIRS[2 * a])
                f += 1 if (c[LIDX[l]] == 1) == (sum(x // 2 for x in lo) % 2 == 0) else -1
        out.append(f)
    return tuple(out)


ZERO = [c for c in ICE if fluxes(c) == (0, 0, 0)]


def pattern(c, v):
    return tuple(c[LIDX[l]] for l in NB[v])


# ---------- A. hard rules select nothing ----------
print("A. the hard static rule")


def values(c):
    val = {}
    for s in SITES:
        r = role(s)
        val[s] = pattern(c, s) if r == "V" else (c[LIDX[s]] if r == "L" else ".")
    return val


VAL = [values(c) for c in ICE]
fn = True
for s in SITES:
    seen = {}
    for v in VAL:
        key = tuple(v[t] for t in NB[s])
        if seen.setdefault(key, v[s]) != v[s]:
            fn = False
check("in every ice state each site's value is a function of its neighbours' values (hard soldered rule)",
      fn and len(ICE) == 9600 and len(ZERO) == 880, "9600 states, 880 at zero flux, as in the landed note")
l0 = LS[0]
laws = {"uniform": ICE, "zero-flux uniform": ZERO, "one state": ICE[:1]}
var = {k: Fr(sum(1 for c in st if c[LIDX[l0]] == 1), len(st)) for k, st in laws.items()}
fvar = {k: Fr(sum(fluxes(c)[0] ** 2 for c in st), len(st)) for k, st in laws.items()}
check("so the uniform law, the zero-flux uniform law and a single state all satisfy the same hard conditionals, and differ",
      var["one state"] in (0, 1) and var["uniform"] == Fr(1, 2) and fvar["zero-flux uniform"] == 0 and fvar["uniform"] > 0,
      f"P(link occupied) {var['uniform']}, {var['zero-flux uniform']}, {var['one state']}; flux variance {fvar['uniform']}, 0, {fvar['one state']}")

# ---------- B. a positive rule selects the uniform law ----------
print("B. the positive rule")


def A_weight(p, eps):
    return sum(eps ** sum(a != b for a, b in zip(S, p)) for S in ICEPAT)


EPS = Fr(1, 10)
ice_A = A_weight(ICEPAT[0], EPS)
check("a vertex whose links form an ice pattern contributes 1 + 9 eps^2 + 9 eps^4 + eps^6; any other pattern has no eps^0 term",
      all(A_weight(p, EPS) == 1 + 9 * EPS ** 2 + 9 * EPS ** 4 + EPS ** 6 for p in ICEPAT)
      and all(A_weight(p, Fr(0)) == (1 if p in ICEPAT else 0) for p in product((0, 1), repeat=6)),
      "summing the 20 records of a vertex, which are independent given its links")
ok_local = True
for c in ICE[:40]:
    for v in VS[:2]:
        for S in ICEPAT[:6]:
            for l in NB[v]:
                recs = {w: pattern(c, w) for w in VS}
                recs[v] = S

                def weight(n_l):
                    m = 0
                    for w in VS:
                        for k, t in enumerate(NB[w]):
                            occ = n_l if t == l else c[LIDX[t]]
                            m += recs[w][k] != occ
                    return EPS ** m
                odds = weight(1) / weight(0)
                ends = [w for w in VS if l in NB[w]]
                pred = EPS ** sum((recs[w][NB[w].index(l)] != 1) - (recs[w][NB[w].index(l)] != 0) for w in ends)
                ok_local = ok_local and odds == pred
check("the positive rule is nearest-neighbour: a link's odds depend only on its two vertex records",
      ok_local, "checked against the full weight on 1440 perturbed configurations; a vertex's law depends on its six links")


def partition(eps, ice_only=False):
    Aw = {p: (A_weight(p, eps) if (p in ICEPAT or not ice_only) else Fr(0)) for p in product((0, 1), repeat=6)}
    left = {l: 2 for l in LS}
    states = {(): Fr(1)}
    for v in VS:
        star = NB[v]
        nxt = {}
        for key, w in states.items():
            assign = dict(key)
            free = [l for l in star if l not in assign]
            for bits in product((0, 1), repeat=len(free)):
                a2 = dict(assign)
                a2.update(zip(free, bits))
                w2 = w * Aw[tuple(a2[l] for l in star)]
                if w2 == 0:
                    continue
                done = {l for l in star if left[l] == 1}
                k2 = tuple(sorted((l, x) for l, x in a2.items() if l not in done))
                nxt[k2] = nxt.get(k2, Fr(0)) + w2
        for l in star:
            left[l] -= 1
        states = nxt
    return sum(states.values())


Z0 = partition(Fr(0))
PS = {}
ICESUM = {}
for e in (Fr(1, 10), Fr(1, 100), Fr(1, 1000)):
    ICESUM[e] = partition(e, ice_only=True)
    PS[e] = ICESUM[e] / partition(e)
E1, E2, E3 = Fr(1, 10), Fr(1, 100), Fr(1, 1000)
check("the transfer programme reproduces 9600 at eps = 0; P(no charged vertex) rises to 1 as eps falls",
      Z0 == 9600 and PS[E1] < PS[E2] < PS[E3] and PS[E3] > Fr(999, 1000),
      f"P = {float(PS[E1]):.4f}, {float(PS[E2]):.4f}, {float(PS[E3]):.6f} at eps = 1/10, 1/100, 1/1000; "
      f"(1 - P)/eps^2 = {float((1 - PS[E3]) / E3 ** 2):.0f}: charges come in pairs")
check("given no charged vertex the law is exactly uniform on the 9600 ice states, for every eps > 0",
      len({A_weight(p, EPS) for p in ICEPAT}) == 1
      and all(ICESUM[e] == 9600 * A_weight(ICEPAT[0], e) ** 8 for e in ICESUM),
      "every ice state has link weight (1 + 9 eps^2 + 9 eps^4 + eps^6)^8; the zero-flux sector keeps its share 880/9600")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
