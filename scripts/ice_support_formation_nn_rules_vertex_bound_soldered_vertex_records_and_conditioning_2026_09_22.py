#!/usr/bin/env python3
"""Ice support under nearest-neighbour formation: a 5/16 vertex bound, soldered
vertex records, unrecorded defects, sweeps, and conditional ice measures in the listed protocols.  Exact and finite.

Supplied conditional finite models; no physical formation law is inferred.  Exact rational arithmetic; no floating point.

Declared objects
  * the superlattice roles of the landed support-rule note in 3D: vertex
    sites V and link sites L; each V is the fine-lattice neighbour of its six
    links, and links are not neighbours of each other;
  * the ice support of the landed spin-half cubic-ice notes in occupation
    form: link records n in {0, 1}, exactly 3 of the 6 links of every vertex
    occupied;
  * the formation reading with the supplied unrecorded-site convention (open PR 8666): a
    site with no admissible possibility carries no record, and formation
    continues;
  * windows: one vertex with its 6 links; two vertices sharing a link (11
    links); four vertices around a plaquette in the xy-plane (24 links);
  * the soldered vertex-record rule: a vertex records one of the 20 ice
    configurations of its six links (3 occupied directions), uniformly among
    those consistent with its formed links; a link copies the occupation its
    formed vertices assign to it, takes a fair coin with none formed, and is
    unrecorded if two formed vertices disagree.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
from fractions import Fraction as Fr
from itertools import combinations, product
from math import comb

AUDIT_TIMEOUT_SEC = 120
RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
CONFIGS = [frozenset(c) for c in combinations(DIRS, 3)]
HALF = Fr(1, 2)


def neg(d):
    return tuple(-x for x in d)


print("== 1. One vertex: independent identical link draws have a 5/16 ice bound ==")
BOUND = max(comb(6, 3) * Fr(k, 64) ** 3 * (1 - Fr(k, 64)) ** 3 for k in range(65))
check("P(exactly 3 of 6 independent links occupied) = 20 p^3 (1-p)^3 <= 5/16, attained at p = 1/2 (grid of 65 p)",
      BOUND == Fr(5, 16) and comb(6, 3) * HALF ** 6 == Fr(5, 16) and len(CONFIGS) == 20,
      "link-first order: every link forms with no formed neighbour, the model stipulates independent identical draws")


def unsoldered_vertex_first(p_by_c, r0c):
    """Vertex records c first; direction-blind links then share one conditional p_c."""
    return sum(r0c[c] * comb(6, 3) * p ** 3 * (1 - p) ** 3 for c, p in p_by_c.items())


EX_U = unsoldered_vertex_first({0: Fr(1, 4), 1: Fr(3, 4)}, {0: HALF, 1: HALF})
GRID = [Fr(k, 8) for k in range(9)]
GRID_MAX = max(unsoldered_vertex_first({0: p0, 1: p1}, {0: q, 1: 1 - q}) for p0 in GRID for p1 in GRID for q in GRID)
check("unsoldered, vertex-first: given the vertex record the six links are exchangeable, so again P(ice) <= 5/16",
      EX_U == Fr(135, 1024) and EX_U < Fr(5, 16) and GRID_MAX == Fr(5, 16),
      "example p = 1/4 or 3/4 gives 135/1024; the maximum over 729 two-record rules is 5/16")


def solder_single(k):
    """Soldered vertex-record rule, one vertex: k links formed first (fair coins), then the vertex,
    then the rest copy. Returns P(vertex unrecorded)."""
    first = DIRS[:k]
    miss = Fr(0)
    for bits in product((0, 1), repeat=k):
        consistent = [c for c in CONFIGS if all((d in c) == bool(b) for d, b in zip(first, bits))]
        if not consistent:
            miss += HALF ** k
    return miss


HOLES = [solder_single(k) for k in range(7)]
check("soldered vertex records: the vertex is unrecorded with probability 0,0,0,0,1/8,3/8,11/16 when k = 0..6 links form first",
      HOLES == [0, 0, 0, 0, Fr(1, 8), Fr(3, 8), Fr(11, 16)],
      "vertex-first the links copy and the ice rule always holds; the order decides the defect probability")

print()
print("== 2. Two vertices sharing a link: defects move with the order ==")
SH = (1, 0, 0)
N_TWO = sum(comb(5, 3 - b) ** 2 for b in (0, 1))
def agrees(c1, c2):
    """Vertex 1's record and vertex 2's record assign the shared link the same occupation."""
    return (SH in c1) == (neg(SH) in c2)


agree = sum(1 for c1 in CONFIGS for c2 in CONFIGS if agrees(c1, c2))
check("vertex-first: the shared link is unrecorded exactly when the two vertex records disagree on it, 1/2",
      Fr(400 - agree, 400) == HALF and agree == 200 == N_TWO,
      "the 200 agreeing record pairs are exactly the 200 ice configurations of the 11-link window")
both = Fr(0)
LF_SURVIVORS = set()
for bits in product((0, 1), repeat=11):
    shared, rest1, rest2 = bits[0], bits[1:6], bits[6:11]
    if shared + sum(rest1) == 3 and shared + sum(rest2) == 3:
        both += HALF ** 11
        LF_SURVIVORS.add(bits)
check("link-first: both vertices recorded (both stars ice) with probability 25/256 = (5/16)^2",
      both == Fr(25, 256) and both * 2 ** 11 == N_TWO)
LINKS1 = [d for d in DIRS if d != SH]
LINKS2 = [d for d in DIRS if d != neg(SH)]
ICE_TWO = {bits for bits in product((0, 1), repeat=11)
           if bits[0] + sum(bits[1:6]) == 3 and bits[0] + sum(bits[6:11]) == 3}
VF = {}
for c1 in CONFIGS:
    for c2 in CONFIGS:
        if agrees(c1, c2):
            cfg = (int(SH in c1),) + tuple(int(d in c1) for d in LINKS1) + tuple(int(d in c2) for d in LINKS2)
            VF[cfg] = VF.get(cfg, Fr(0)) + Fr(1, 400)
ZV = sum(VF.values())
check("conditional on no unrecorded site, both orders give the uniform law 1/200 on the window's ice configurations",
      set(VF) == ICE_TWO and len(ICE_TWO) == 200 and all(m / ZV == Fr(1, 200) for m in VF.values())
      and LF_SURVIVORS == ICE_TWO and both * 2 ** 11 == len(ICE_TWO),
      "vertex-first: uniform on agreeing pairs; link-first: independent fair links conditioned on ice")

print()
print("== 3. A plaquette of four vertices: a sweep avoids defects but not bias ==")
V1, V2, V3, V4 = (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)
EXX, EYY = (1, 0, 0), (0, 1, 0)
sweep = {}
holes = Fr(0)
for c1 in CONFIGS:
    a, d = int(EXX in c1), int(EYY in c1)
    opts2 = [c for c in CONFIGS if int(neg(EXX) in c) == a]
    for c2 in opts2:
        b = int(EYY in c2)
        opts3 = [c for c in CONFIGS if int(neg(EYY) in c) == b]
        for c3 in opts3:
            c = int(neg(EXX) in c3)
            opts4 = [x for x in CONFIGS if int(EXX in x) == c and int(neg(EYY) in x) == d]
            p = Fr(1, 20) * Fr(1, len(opts2)) * Fr(1, len(opts3))
            if not opts4:
                holes += p
                continue
            for c4 in opts4:
                key = (c1, c2, c3, c4)
                sweep[key] = sweep.get(key, Fr(0)) + p / len(opts4)
N_PLAQ = sum(comb(4, 3 - a - d) * comb(4, 3 - a - b) * comb(4, 3 - b - c) * comb(4, 3 - c - d)
             for a, b, c, d in product((0, 1), repeat=4) if max(a + d, a + b, b + c, c + d) <= 3)
def consistent4(c1, c2, c3, c4):
    return ((EXX in c1) == (neg(EXX) in c2) and (EYY in c2) == (neg(EYY) in c3)
            and (neg(EXX) in c3) == (EXX in c4) and (neg(EYY) in c4) == (EYY in c1))


check("sweep order (each vertex after the links of its earlier neighbours): no unrecorded site, total mass 1",
      holes == 0 and sum(sweep.values()) == 1 and len(sweep) == N_PLAQ
      and all(consistent4(*k) for k in sweep),
      f"every one of the {N_PLAQ} ice configurations of the 20-link plaquette is reached")
check("but the sweep law is not uniform: masses 1/8000 and 1/12000 against the uniform 1/%d" % N_PLAQ,
      set(sweep.values()) == {Fr(1, 8000), Fr(1, 12000)} and Fr(1, N_PLAQ) not in set(sweep.values()),
      "the closing vertex has 4 or 6 consistent records, so its choice weights the configurations unevenly")
P_EQ_SWEEP = sum(m for (c1, c2, c3, c4), m in sweep.items() if int(EXX in c4) == int(neg(EYY) in c4))
P_EQ_UNIF = Fr(sum(comb(4, 3 - a - d) * comb(4, 3 - a - b) * comb(4, 3 - b - c) * comb(4, 3 - c - d)
                   for a, b, c, d in product((0, 1), repeat=4) if c == d), N_PLAQ)
check("a record statistic separates them: P(the two plaquette links at V4 agree) differs, sweep against uniform",
      P_EQ_SWEEP == Fr(62, 125) and P_EQ_UNIF == Fr(124, 313) and N_PLAQ == 10016,
      f"sweep {P_EQ_SWEEP}, uniform ice {P_EQ_UNIF}")

print()
print("per_element: checked the finite configurations and arithmetic controls explicitly enumerated above")
print("per_site: checked the declared finite-window local rules under their supplied sampling conventions")
print("per_mode: checked and not executed — no infinite-volume Fourier or spectral mode computation is performed")
print("per_block: checked only the listed finite windows and orders; proofs beyond those runs are source arguments")
print("lattice_wide: checked and not executed — no infinite-lattice formation process or physical completion is simulated")
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
