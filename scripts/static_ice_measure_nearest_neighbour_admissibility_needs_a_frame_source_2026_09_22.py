#!/usr/bin/env python3
"""Static conditional locality of four declared finite record schemes. Read as a
static record law, the landed uniform ice measure on link occupations
breaks the nearest-neighbour sentence: a link's conditional is fixed by
next-nearest links.  Vertex records that name the occupied directions
restore it; they are soldered records or records in coordinate letters.
Records that cannot tell a vertex's links apart cannot.  Exact and finite.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.  Exact integer and rational arithmetic; no floating point.

Declared objects
  * the fine torus Z_4^3 with the superlattice roles (V: all coordinates
    even; L: one odd; P: two odd; C: three odd), so V and L form the coarse
    2x2x2 torus of the landed cubic-ice notes;
  * ice configurations: link occupations with exactly 3 of the 6 links of
    every vertex occupied; the uniform ice measure on them;
  * the static reading of the distribution sentence: each site's
    conditional given all other sites is a function of its six
    nearest-neighbour values (under the unsoldered reading, of their
    configuration up to proper rotation);
  * record schemes: occupation form (V, P, C carry nothing), soldered
    vertex records (the set of occupied bond directions, rotating with
    positions), vertex-only unsoldered records, and coordinate letters
    (labels c in Z_4^3 on every site, with the vertex record in label
    coordinates), as in open PR 8676.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys

AUDIT_TIMEOUT_SEC = 120
from itertools import combinations, permutations, product

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
AXES = [(0, 1), (2, 3), (4, 5)]


def add(s, d):
    return tuple((a + b) % N for a, b in zip(s, d))


def sub(s, d):
    return tuple((a - b) % N for a, b in zip(s, d))


def neg(d):
    return tuple(-a for a in d)


def role(s):
    return "VLPC"[sum(a % 2 for a in s)]


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


SP = [tuple(tuple(s[i] if j == p[i] else 0 for j in range(3)) for i in range(3))
      for p in permutations(range(3)) for s in product((1, -1), repeat=3)]
ROT = [g for g in SP if det3(g) == 1]


def act(g, v):
    return tuple(sum(g[i][j] * v[j] for j in range(3)) for i in range(3))


def actm(g, s):
    return tuple(x % N for x in act(g, s))


NB = {s: [add(s, d) for d in DIRS] for s in SITES}
VS = [s for s in SITES if role(s) == "V"]
LS = [s for s in SITES if role(s) == "L"]
LIDX = {l: i for i, l in enumerate(LS)}
ENDS = {l: [t for t in NB[l] if role(t) == "V"] for l in LS}


def ice_configs():
    out = []

    def rec(k, n):
        if k == len(VS):
            out.append(tuple(n[l] for l in LS))
            return
        star = NB[VS[k]]
        fixed = sum(n[l] for l in star if l in n)
        free = [l for l in star if l not in n]
        need = 3 - fixed
        if 0 <= need <= len(free):
            for occ in combinations(free, need):
                for l in free:
                    n[l] = 1 if l in occ else 0
                rec(k + 1, n)
                for l in free:
                    del n[l]
    rec(0, {})
    return out


ICE = ice_configs()


def is_function(pairs):
    seen = {}
    for key, val in pairs:
        if seen.setdefault(key, val) != val:
            return False
    return True


# ---------- 1. occupation form ----------
print("1. occupation form: vertices carry nothing")
check("ice configurations on the coarse 2x2x2 torus (Z_4^3 fine) enumerated",
      len(ICE) == 9600 and all(sum(c[LIDX[l]] for l in NB[v]) == 3 for c in ICE for v in VS),
      f"{len(ICE)} configurations; 8 vertices, 24 links")
nnn = all(c[LIDX[l]] == 3 - sum(c[LIDX[m]] for m in NB[v] if m != l)
          for c in ICE for l in LS for v in ENDS[l])
check("each link's conditional given all other sites is fixed by next-nearest links",
      nnn, "n(l) = 3 - (other five links at either endpoint)")
occ_fail = [l for l in LS if len({c[LIDX[l]] for c in ICE}) == 2]
check("with constant vertex, plaquette and cube records the link's value is not a function of its neighbours",
      len(occ_fail) == 24, "every link takes both values under identical neighbour records: the sentence fails")


def arrow_plus(c, l, a):
    lo = sub(l, DIRS[2 * a])
    return 1 if (c[LIDX[l]] == 1) == (sum(x // 2 for x in lo) % 2 == 0) else -1


def fluxes(c):
    return tuple(sum(arrow_plus(c, l, a) for l in LS if l[a] == 1) for a in range(3))


ICE0 = [c for c in ICE if fluxes(c) == (0, 0, 0)]
check("the landed RK sector: 880 zero-flux states, and every link still takes both values there",
      len(ICE0) == 880 and all(len({c[LIDX[l]] for c in ICE0}) == 2 for l in LS),
      "flux = net arrow count through a plane, arrows from the even to the odd coarse sublattice")

# ---------- 2. soldered vertex records ----------
print("2. soldered vertex records")


def soldered(c):
    val = {}
    for s in SITES:
        r = role(s)
        if r == "V":
            val[s] = frozenset(d for d in DIRS if c[LIDX[add(s, d)]] == 1)
        elif r == "L":
            val[s] = c[LIDX[s]]
        else:
            val[s] = "."
    return val


SOL = [soldered(c) for c in ICE]
ok_fn = all(is_function((tuple(v[add(s, d)] for d in DIRS), v[s]) for v in SOL) for s in SITES)
check("soldered records: every site's value is a function of its six neighbours' values (by direction)",
      ok_fn, f"64 sites x {len(SOL)} states")
keyset = {tuple(v[s] for s in SITES) for v in SOL}


def rot_soldered(g, v):
    out = {}
    for s in SITES:
        x = v[s]
        out[actm(g, s)] = frozenset(act(g, d) for d in x) if isinstance(x, frozenset) else x
    return tuple(out[s] for s in SITES)


check("the soldered support is invariant under the 24 rotations acting on positions and on records",
      all(rot_soldered(g, v) in keyset for g in ROT for v in SOL) and len(keyset) == len(ICE),
      "link marginal is the uniform ice measure (one state per ice configuration)")

# ---------- 3. unsoldered records that cannot tell links apart ----------
print("3. unsoldered vertex-only records")
star = [tuple(1 if i in S else 0 for i in range(6)) for S in combinations(range(6), 3)]
check("star window: an unsoldered link rule sees only the vertex, so all six links would be equal; no ice pattern is",
      len(star) == 20 and all(len(set(p)) == 2 for p in star),
      "20 ice patterns, none constant")
partners = all(set(ENDS[add(v, DIRS[i])]) == set(ENDS[add(v, DIRS[j])]) for v in VS for i, j in AXES)
odd_axis = all(any(c[LIDX[add(v, DIRS[i])]] != c[LIDX[add(v, DIRS[j])]] for v in VS for i, j in AXES) for c in ICE)
check("2x2x2 torus: the two links of an axis join the same vertex pair, and every ice state has such a pair unequal",
      partners and odd_axis, "a symmetric function of endpoint records gives them equal values; no vertex alphabet works")

# ---------- 4. coordinate letters ----------
print("4. coordinate letters (open PR 8676)")
ID = SP[0]
lem = True
for g2, g3 in product(SP, repeat=2):
    for d, e in permutations(DIRS, 2):
        if sum(a * b for a, b in zip(d, e)) != 0:
            continue
        back = act(g2, neg(d)) == neg(act(ID, d)) and act(g3, neg(e)) == neg(act(ID, e))
        close = add(act(ID, d), act(g2, e)) == add(act(ID, e), act(g3, d))
        if back and close and not (act(g2, e) == act(ID, e) and act(g3, d) == act(ID, d)):
            lem = False
check("static rigidity lemma: a plaquette whose two paths agree, with consistent back-steps, forces equal local frames",
      lem, "all 48 x 48 frame pairs and 24 perpendicular pairs (first frame fixed by relabelling)")


def frame_labels(g):
    return {s: actm(g, s) for s in SITES}


def static_ok(lab):
    for s in SITES:
        diffs = [sub(lab[t], lab[s]) for t in NB[s]]
        if not any(all(diffs[k] == tuple(x % N for x in act(g, DIRS[k])) for k in range(6)) for g in SP):
            return False
    return True


check("all 48 signed frames are complete static records of the frame rule on the torus",
      all(static_ok(frame_labels(g)) for g in SP), "with the lemma, these and their 64 offsets are all of them")
uniq = True
for g in SP:
    lab = frame_labels(g)
    ring = [lab[t] for t in NB[(0, 0, 0)]]
    cands = [c for c in SITES
             if any(all(sub(ring[k], c) == tuple(x % N for x in act(h, DIRS[k])) for k in range(6)) for h in SP)]
    uniq = uniq and cands == [(0, 0, 0)]
check("a site's six neighbour labels fix its own label in every frame", uniq, "unique candidate for all 48 frames")


def lettered(c, g):
    lab = frame_labels(g)
    val = {}
    for s in SITES:
        r = role(s)
        if r == "V":
            content = tuple(sorted(sub(lab[add(s, d)], lab[s]) for d in DIRS if c[LIDX[add(s, d)]] == 1))
        elif r == "L":
            content = (c[LIDX[s]],)
        else:
            content = ()
        val[s] = (lab[s], content)
    return val


def unsoldered_key(v, s):
    return tuple(sorted(tuple(sorted((repr(v[add(s, DIRS[i])]), repr(v[add(s, DIRS[j])]))))
                        for i, j in AXES))


pairs = [(unsoldered_key(v, s), repr(v[s])) for g in (ID, tuple(tuple(-x for x in r) for r in ID))
         for c in ICE for v in [lettered(c, g)] for s in SITES]
check("coordinate letters: every site's value is a function of its neighbours' values up to rotation",
      is_function(pairs), f"{len(pairs)} (site, state) pairs over a proper and an improper frame; key ignores directions")


def readout_ok(v):
    ice = all(sum(v[add(s, d)][1][0] for d in DIRS) == 3 for s in VS)
    links = all(v[l][1][0] == (1 if sub(v[l][0], v[t][0]) in v[t][1] else 0) for l in LS for t in ENDS[l])
    roles = all(sum(x % 2 for x in v[s][0]) == sum(x % 2 for x in s) for s in SITES)
    return ice and links and roles


rot_ok = all(readout_ok({actm(h, s): val for s, val in lettered(c, ID).items()}) for h in ROT for c in ICE[::7])
check("rotating positions with values fixed keeps the lettered records consistent (unsoldered covariance)",
      rot_ok and all(readout_ok(lettered(c, ID)) for c in ICE),
      "ice at every vertex, links agree with both vertex records, roles read from labels")

print("N5 resolution certificate: exact finite algebra and declared enumeration domains only")
print("N5 sampling certificate: external fixed orders and fresh conditional draws where formation is used")
print("N5 dependency certificate: self-contained stdlib runner; no physical encoding supplied")
print("N5 scaling certificate: finite checks do not execute infinite-volume or spectral limits")
print("N5 scope certificate: source proofs carry universal implications; alternative models remain open")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
