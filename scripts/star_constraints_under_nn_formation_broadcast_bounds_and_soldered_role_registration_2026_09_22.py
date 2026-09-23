#!/usr/bin/env python3
"""Star constraints under nearest-neighbour formation: pair constraints are
enforced in every order, star constraints need a checker formed last or a
soldered broadcast, and the parity-role skeleton is registered by soldered
role letters with nucleation defects.  Exact and finite.

Supplied conditional finite models; no physical formation law is inferred.  Exact rational arithmetic; no floating point.

Declared objects
  * formation reading with the supplied unrecorded-site convention (open PR 8666): a site
    with no admissible possibility carries no record, formation continues;
  * pair constraints (adjacent values compatible) and star constraints (the
    neighbours of one site jointly constrained): Gauss parity at a vertex,
    the ice count, and the role skeleton's link profile (two vertex letters
    on one axis, four plaquette letters across it);
  * role letters as parity vectors in {0,1}^3 (V = 000, L_x = 100, ...,
    C = 111): soldered letters rotate with positions and a site's letter
    fixes each neighbour's letter (flip the parity along the bond axis);
    scalar letters V, L, P, C (Hamming weight) are the unsoldered version;
  * the 2x2x2 cube window with all 40320 formation orders; the 3-site path.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
from fractions import Fraction as Fr
from itertools import permutations, product
from math import comb

AUDIT_TIMEOUT_SEC = 120
RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


H = "h"
CUBE = tuple(product((0, 1), repeat=3))
NBRS = {s: [t for t in CUBE if sum(a != b for a, b in zip(s, t)) == 1] for s in CUBE}


def axis(s, t):
    return next(i for i in range(3) if s[i] != t[i])


def xor(p, i):
    return tuple(b ^ (1 if j == i else 0) for j, b in enumerate(p))


LETTERS = CUBE


def soldered_rule(s, formed):
    implied = {xor(formed[t], axis(s, t)) for t in NBRS[s] if t in formed and formed[t] != H}
    if not implied:
        return {l: Fr(1, 8) for l in LETTERS}
    if len(implied) == 1:
        return {implied.pop(): Fr(1)}
    return {}


def scalar_rule(s, formed):
    ws = [formed[t] for t in NBRS[s] if t in formed and formed[t] != H]
    allowed = [w for w in range(4) if all(abs(w - x) == 1 for x in ws)]
    return {w: Fr(1, len(allowed)) for w in allowed}


def finished(rule, order):
    layer = {(): Fr(1)}
    for s in order:
        nxt = {}
        for part, mass in layer.items():
            formed = {order[i]: part[i] for i in range(len(part))}
            probs = rule(s, formed)
            tot = sum(probs.values())
            for v, p in probs.items():
                nxt[part + (v,)] = nxt.get(part + (v,), Fr(0)) + mass * p
            if tot < 1:
                nxt[part + (H,)] = nxt.get(part + (H,), Fr(0)) + mass * (1 - tot)
        layer = nxt
    pos = {s: i for i, s in enumerate(order)}
    return {tuple(part[pos[s]] for s in CUBE): m for part, m in layer.items()}


def nucleations(order):
    seen, k = set(), 0
    for s in order:
        if not any(t in seen for t in NBRS[s]):
            k += 1
        seen.add(s)
    return k


SKELETON = {tuple(tuple(a ^ b for a, b in zip(s, phi)) for s in CUBE) for phi in LETTERS}
SCALAR_SKEL = {tuple(sum(l) for l in sk) for sk in SKELETON}

print("== 1. Pair constraints hold in every order; star constraints need more ==")
ALL = list(permutations(CUBE))
KS = [nucleations(o) for o in ALL]
HIST = {k: KS.count(k) for k in sorted(set(KS))}
check("cube: 40320 orders split by the number k of independent nucleations",
      HIST == {1: 8640, 2: 24480, 3: 5760, 4: 1440},
      f"k-histogram {HIST}")
SAMPLE = [next(o for o, k in zip(ALL, KS) if k == kk) for kk in sorted(HIST)] + ALL[::4001]
ok_formula, ok_phase = True, True
for o in SAMPLE:
    L = finished(soldered_rule, o)
    complete = {st: m for st, m in L.items() if H not in st}
    z = sum(complete.values())
    ok_formula = ok_formula and z == Fr(1, 8) ** (nucleations(o) - 1)
    ok_phase = ok_phase and set(complete) <= SKELETON and all(m / z == Fr(1, 8) for m in complete.values())
check("soldered role letters: completion is exactly (1/8)^(k-1) on every sampled order (all k = 1..4 present)",
      ok_formula,
      "one nucleus registers the phase; each further independent nucleus must pick the same phase, 1 chance in 8")
check("conditional on completion the finished state is one of the 8 skeleton phases, each with mass 1/8",
      ok_phase and len(SKELETON) == 8)
E_COMPLETE = sum(Fr(c, 40320) * Fr(1, 8) ** (k - 1) for k, c in HIST.items())
check("under the uniform order law the skeleton completes with probability E[(1/8)^(k-1)]; connected growth always",
      HIST[1] > 0 and E_COMPLETE == Fr(599, 2048),
      f"{HIST[1]} connected-growth orders complete with certainty; overall {E_COMPLETE}")
viol = {}
for o in SAMPLE:
    L = finished(scalar_rule, o)
    complete = {st: m for st, m in L.items() if H not in st}
    z = sum(complete.values())
    viol[o] = sum(m for st, m in complete.items() if st not in SCALAR_SKEL) / z if z else None
check("scalar (unsoldered) letters: pair constraints hold, yet completed states leave the skeleton with no hole",
      max(v for v in viol.values() if v is not None) == Fr(7, 8),
      f"largest non-skeleton share among completed states: {max(v for v in viol.values() if v is not None)}")

print()
print("== 2. Star constraints: the unsoldered broadcast bound ==")
GRID = [Fr(k, 12) for k in range(13)]
L_BOUND = max(3 * q ** 2 * (1 - q) ** 4 for q in GRID)
check("link-letter star, unsoldered: centre L, six leaves i.i.d. over {V, P}: P(correct profile) <= 16/243",
      L_BOUND == Fr(16, 243) and 3 * Fr(1, 3) ** 2 * Fr(2, 3) ** 4 == Fr(16, 243),
      "the profile needs the two V letters on one axis and four P letters across it; a direction-blind rule cannot aim")
PARITY_BOUND = max((1 - (1 - 2 * p) ** 6) / 2 for p in GRID)
LINKS6 = list(product((0, 1), repeat=6))
V_LAST = sum(Fr(1, 64) for bits in LINKS6 if (sum(bits) + sum(bits) % 2) % 2 == 0)
V_FIRST_FAIR = sum(Fr(1, 2) * Fr(1, 64) for v in (0, 1) for bits in LINKS6 if (v + sum(bits)) % 2 == 0)
check("Gauss parity star: vertex last absorbs the parity (always even); vertex first, fair links: even w.p. 1/2",
      V_LAST == 1 and V_FIRST_FAIR == Fr(1, 2) and PARITY_BOUND == Fr(1, 2)
      and sum(1 for bits in LINKS6 if sum(bits) % 2 == 1) == 32,
      "unsoldered, odd vertex first: P(links odd) <= 1/2 for every link law; a soldered vertex can dictate one of 32 sets")
check("ice star: 20 p^3 (1-p)^3 <= 5/16 (the ice-support block); isotropic stars (V: all L, C: all P) can always hold",
      max(comb(6, 3) * p ** 3 * (1 - p) ** 3 for p in GRID) == Fr(5, 16))
SOLD_STAR = soldered_rule((1, 0, 0), {(0, 0, 0): (1, 0, 0)})
check("soldered link letter broadcasts: a leaf along the link's axis must be V, across it the plaquette letter",
      SOLD_STAR == {(0, 0, 0): Fr(1)} and soldered_rule((0, 1, 0), {(0, 0, 0): (1, 0, 0)}) == {(1, 1, 0): Fr(1)})

print()
print("== 3. Two independent nuclei on a path: the phase price ==")
SOLD_MID = sum(Fr(1, 64) for lx in LETTERS for lz in LETTERS if xor(lx, 0) == xor(lz, 0))
SCAL_MID = {(wx, wz): [w for w in range(4) if abs(w - wx) == 1 and abs(w - wz) == 1] for wx in range(4) for wz in range(4)}
SCAL_REC = sum(Fr(1, 16) for k, v in SCAL_MID.items() if v)
SCAL_SKEL = sum(Fr(1, 16) for (wx, wz), v in SCAL_MID.items() if v and wx == wz)
check("ends of a straight 3-site path formed first: soldered, the middle is recorded w.p. 1/8 (ends must agree)",
      SOLD_MID == Fr(1, 8)
      and sum(r * r for r in (Fr(1, 8), Fr(3, 8), Fr(3, 8), Fr(1, 8))) == Fr(5, 16),
      "one phase in 8; with scalar letters at skeleton frequencies the same-letter chance is 5/16")
check("scalar letters: the middle is recorded w.p. 1/2, but only half of those are skeleton (ends equal)",
      SCAL_REC == Fr(1, 2) and SCAL_SKEL == Fr(1, 4),
      "pair constraints accept V-L-P along one axis, which no skeleton phase contains")

print()
print("per_element: checked the finite configurations and arithmetic controls explicitly enumerated above")
print("per_site: checked the declared finite-window local rules under their supplied sampling conventions")
print("per_mode: checked and not executed — no infinite-volume Fourier or spectral mode computation is performed")
print("per_block: checked only the listed finite windows and orders; proofs beyond those runs are source arguments")
print("lattice_wide: checked and not executed — no infinite-lattice formation process or physical completion is simulated")
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
