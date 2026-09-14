#!/usr/bin/env python3
"""Handed-rule pseudo-scalar census and parity-odd record correlators (2026-09-13).

Exact finite arithmetic (Python ints, Fractions).  Possibility alphabet: the six
axis unit Bloch vectors.  Window: the seven-site nearest-neighbour cross of Z^3
(centre plus six arms).  Slots 0..5 = +x,-x,+y,-y,+z,-z.

S1 cubic group: 48 signed permutations (24 proper); slot, soldered, internal actions
S2 T = det[d_x,d_y,d_z] and D4 (alternating dot-product quartic): sign table
S3 census of lowest-degree pseudo-scalar invariants under three readings
S4 Burnside dimensions of handed rule terms; lowest handed degree per reading (DM lattice-curl term);
   explicit admissible rules W_0 (achiral) and W_X (handed), mirrors, positivity
S5 exact parity-odd record correlators on the seven-site window: centre-last, static, order mixture
S6 underdetermination witnesses per reading and the recorded separating clauses
Prints TOTAL: PASS=N FAIL=0.
"""
import random
import sys
from fractions import Fraction as Fr
from itertools import combinations, combinations_with_replacement, permutations, product

PASS = 0
FAIL = 0


class _Counting:
    """Counts bytes written to stdout so the runner can verify the 6000-byte ceiling itself."""
    def __init__(self, w): self.w, self.n = w, 0
    def write(self, t):
        self.n += len(t.encode())
        return self.w.write(t)
    def flush(self): return self.w.flush()

OUT = _Counting(sys.stdout)
sys.stdout = OUT


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + name + ((" " + detail) if detail else ""))


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


def sub(u, v):
    return (u[0] - v[0], u[1] - v[1], u[2] - v[2])


def det3(a, b, c):
    return (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def matvec(M, v):
    return tuple(M[i][0] * v[0] + M[i][1] * v[1] + M[i][2] * v[2] for i in range(3))


def detM(M):
    return det3(M[0], M[1], M[2])


# S1 ------------------------------------------------------------------------
G = []
for p in permutations(range(3)):
    for s in product((1, -1), repeat=3):
        M = [[0, 0, 0] for _ in range(3)]
        for i in range(3):
            M[i][p[i]] = s[i]
        G.append(tuple(tuple(r) for r in M))
PROPER = [M for M in G if detM(M) == 1]
IMPROPER = [M for M in G if detM(M) == -1]
SLOTVEC = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
SLOT_OF = {v: i for i, v in enumerate(SLOTVEC)}
PERM = {M: tuple(SLOT_OF[matvec(M, SLOTVEC[i])] for i in range(6)) for M in G}
CONJ = ((1, 0, 0), (0, -1, 0), (0, 0, 1))   # complex conjugation on the Bloch vector
INV = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
MIRX = ((-1, 0, 0), (0, 1, 0), (0, 0, 1))   # lattice mirror x -> -x


def act_slots(M, q):
    """Lattice operation on arm positions only (unsoldered): label q[i] moves to slot PERM[M][i]."""
    out = [None] * 6
    for i, j in enumerate(PERM[M]):
        out[j] = q[i]
    return tuple(out)


def act_soldered(M, q):
    """Lattice operation carrying the labels along (soldered)."""
    return tuple(matvec(M, v) for v in act_slots(M, q))


def act_internal(M, q):
    """Internal operation on labels only; positions fixed."""
    return tuple(matvec(M, v) for v in q)


def T_of(q):
    d = [sub(q[2 * a], q[2 * a + 1]) for a in range(3)]
    return det3(d[0], d[1], d[2])


def D4_of(q):
    """Alternating O_h sum of (q_{+x}.q_{+y})(q_{-x}.q_{+z}); odd under improper slot operations."""
    tot = 0
    for M in G:
        r = act_slots(M, q)
        tot += detM(M) * dot(r[0], r[2]) * dot(r[1], r[4])
    return tot


check("S1 cubic group has 48 elements, 24 proper and 24 improper",
      len(G) == 48 and len(PROPER) == 24 and len(IMPROPER) == 24)
check("S1 every slot action permutes the six arms", all(sorted(PERM[M]) == list(range(6)) for M in G))
check("S1 conjugation, x-mirror and inversion are improper and belong to the cubic group",
      all(detM(M) == -1 and M in PERM for M in (CONJ, MIRX, INV)))

# S2 ------------------------------------------------------------------------
LET = SLOTVEC                                   # six letters = six axis unit vectors
CONFIGS = list(product(range(6), repeat=6))    # 46656 arm configurations, lexicographic
NC = len(CONFIGS)
POW6 = [6 ** (5 - i) for i in range(6)]
LETPERM = {M: tuple(SLOT_OF[matvec(M, LET[l])] for l in range(6)) for M in G}
IDP = tuple(range(6))
DOT = [[dot(LET[a], LET[b]) for b in range(6)] for a in range(6)]

def vecs(c): return tuple(LET[x] for x in c)

def action_map(p, l):
    """Index map k -> k' of the joint action: labels permuted by l, then moved to slots by p."""
    w = [POW6[p[i]] for i in range(6)]
    return [l[c[0]]*w[0] + l[c[1]]*w[1] + l[c[2]]*w[2] + l[c[3]]*w[3] + l[c[4]]*w[4] + l[c[5]]*w[5]
            for c in CONFIGS]

T_ARR = [T_of(vecs(c)) for c in CONFIGS]
D4_TERMS = []
for M in G:
    p = PERM[M]; pinv = [0] * 6
    for i, j in enumerate(p): pinv[j] = i
    D4_TERMS.append((detM(M), pinv[0], pinv[2], pinv[1], pinv[4]))
def D4_fast(c):
    tot = 0
    for s, a, b, cc, d in D4_TERMS:
        tot += s * DOT[c[a]][c[b]] * DOT[c[cc]][c[d]]
    return tot
D4_ARR = [D4_fast(c) for c in CONFIGS]
def OMEGA_of(q):
    """Twist Omega = sum_a (q_{+a} x q_{-a}) . e_a  (needs the lattice axes: soldered reading only)."""
    tot = 0
    for a in range(3):
        u, w = q[2*a], q[2*a + 1]
        cr = (u[1]*w[2] - u[2]*w[1], u[2]*w[0] - u[0]*w[2], u[0]*w[1] - u[1]*w[0])
        tot += cr[a]
    return tot
OM_ARR = [OMEGA_of(vecs(c)) for c in CONFIGS]

rng = random.Random(20260913)
sample = [rng.randrange(NC) for _ in range(400)]
check("S2 fast D4 agrees with the alternating-sum definition on 400 samples",
      all(D4_fast(CONFIGS[k]) == D4_of(vecs(CONFIGS[k])) for k in sample))
check("S2 configuration index is consistent with the lexicographic enumeration",
      all(action_map(IDP, IDP)[k] == k for k in sample))

MAPS = {"slots": [(detM(M), action_map(PERM[M], IDP)) for M in G],
        "internal": [(detM(M), action_map(IDP, LETPERM[M])) for M in G],
        "soldered": [(detM(M), action_map(PERM[M], LETPERM[M])) for M in G]}

def grading_of(arr, maps):
    """'even' if invariant under all 48, 'odd' if it carries the det sign, else 'mixed'."""
    neg = [-x for x in arr]
    even = all([arr[j] for j in m] == arr for _, m in maps)
    odd = all([arr[j] for j in m] == (arr if s == 1 else neg) for s, m in maps)
    return "even" if even else ("odd" if odd else "mixed")

SIGN = {}
for nm, arr in (("T", T_ARR), ("D4", D4_ARR), ("Omega", OM_ARR)):
    for act in ("slots", "internal", "soldered"):
        SIGN[(nm, act)] = grading_of(arr, MAPS[act])
print("S2 sign table (grading under the 48 cubic operations, three actions):")
for nm in ("T", "D4", "Omega"):
    print(f"  {nm:5s} slots={SIGN[(nm,'slots')]:5s} internal={SIGN[(nm,'internal')]:5s} soldered={SIGN[(nm,'soldered')]}")
check("S2 T is odd under improper slot operations and odd under improper internal operations",
      SIGN[("T", "slots")] == "odd" and SIGN[("T", "internal")] == "odd")
check("S2 T is EVEN under every soldered cubic operation (a scalar in the soldered reading)",
      SIGN[("T", "soldered")] == "even")
check("S2 D4 is lattice-odd, internal-even and soldered-odd",
      SIGN[("D4", "slots")] == "odd" and SIGN[("D4", "internal")] == "even" and SIGN[("D4", "soldered")] == "odd")
check("S2 Omega is soldered-odd and carries no grading under slot-only or internal-only actions",
      SIGN[("Omega", "soldered")] == "odd" and SIGN[("Omega", "slots")] == "mixed" and SIGN[("Omega", "internal")] == "mixed")
check("S2 T, D4 and Omega are each nonzero on the axis alphabet",
      any(T_ARR) and any(D4_ARR) and any(OM_ARR))
TMAX = max(abs(x) for x in T_ARR); D4MAX = max(abs(x) for x in D4_ARR); OMMAX = max(abs(x) for x in OM_ARR)
print(f"S2 extreme values on the alphabet: max|T|={TMAX} max|D4|={D4MAX} max|Omega|={OMMAX}; "
      f"nonzero counts T={sum(1 for x in T_ARR if x)} D4={sum(1 for x in D4_ARR if x)} Omega={sum(1 for x in OM_ARR if x)}")

# S3 ------------------------------------------------------------------------
def proj_alt(arr, act):
    """Alternating projector sum_M det(M) f(act(M) q) as an integer array over all configurations."""
    out = [0] * NC
    for s, m in MAPS[act]:
        if s == 1:
            for k in range(NC): out[k] += arr[m[k]]
        else:
            for k in range(NC): out[k] -= arr[m[k]]
    return out

def rank_of(vectors):
    """Exact rank of integer vectors via the Gram matrix over Q."""
    n = len(vectors)
    if n == 0: return 0
    rows = [[Fr(sum(a * b for a, b in zip(vectors[i], vectors[j]))) for j in range(n)] for i in range(n)]
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, n) if rows[i][c] != 0), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(n):
            if i != r and rows[i][c] != 0:
                f = rows[i][c] / rows[r][c]
                rows[i] = [x - f * y for x, y in zip(rows[i], rows[r])]
        r += 1
    return r

def comp_map(M):
    """Component index a -> b where (M e_a) = +-e_b."""
    return tuple(next(b for b in range(3) if M[b][a] != 0) for a in range(3))

def orbit_reps(items, move):
    """One representative per orbit of `items` under the 48 operations (move(M, item) -> item)."""
    seen, reps = set(), []
    for it in items:
        if it in seen: continue
        reps.append(it)
        for M in G: seen.add(move(M, it))
    return reps

# families of arm-label monomials (internal-invariant families use dots and dets)
pairs = [(i, j) for i in range(6) for j in range(i + 1, 6)]
triples = list(combinations(range(6), 3))
pairpairs = list(combinations_with_replacement(pairs, 2))
def mv_pair(M, pr): return tuple(sorted(PERM[M][i] for i in pr))
def mv_triple(M, tr): return tuple(sorted(PERM[M][i] for i in tr))
def mv_pairpair(M, pp): return tuple(sorted(mv_pair(M, pr) for pr in pp))
dot_reps = orbit_reps(pairs, mv_pair)
det_reps = orbit_reps(triples, mv_triple)
dd_reps = orbit_reps(pairpairs, mv_pairpair)
def arr_dot(pr): return [DOT[c[pr[0]]][c[pr[1]]] for c in CONFIGS]
def arr_det(tr): return [det3(LET[c[tr[0]]], LET[c[tr[1]]], LET[c[tr[2]]]) for c in CONFIGS]
def arr_dd(pp):
    a, b = arr_dot(pp[0]), arr_dot(pp[1])
    return [x * y for x, y in zip(a, b)]
# soldered family: monomials in the 18 components, degree 1 and 2 (multisets of (slot, component))
mono1 = [((i, a),) for i in range(6) for a in range(3)]
mono2 = list(combinations_with_replacement([(i, a) for i in range(6) for a in range(3)], 2))
def mv_mono(M, mono):
    cm = comp_map(M)
    return tuple(sorted((PERM[M][i], cm[a]) for i, a in mono))
m1_reps = orbit_reps(mono1, mv_mono)
m2_reps = orbit_reps(mono2, mv_mono)
def arr_mono(mono):
    out = []
    for c in CONFIGS:
        v = 1
        for i, a in mono: v *= LET[c[i]][a]
        out.append(v)
    return out

P = {}   # projected families
P["so3_d2"] = [proj_alt(arr_dot(pr), "slots") for pr in dot_reps]
P["so3_d3"] = [proj_alt(arr_det(tr), "slots") for tr in det_reps]
P["so3_d4"] = [proj_alt(arr_dd(pp), "slots") for pp in dd_reps]
P["sol_d1"] = [proj_alt(arr_mono(m), "soldered") for m in m1_reps]
P["sol_d2"] = [proj_alt(arr_mono(m), "soldered") for m in m2_reps]
RANK = {k: rank_of(v) for k, v in P.items()}
RANK["o3_d2"] = RANK["so3_d2"]; RANK["o3_d4"] = RANK["so3_d4"]
# O(3) reading excludes every odd-degree label polynomial: -I (transpose) lies in the O(3) reading
NEG_I_ODD = all(grading_of(a, [(-1, action_map(IDP, LETPERM[INV]))] + [(1, action_map(IDP, IDP))]) == "odd"
                for a in (arr_det(tr) for tr in det_reps))
RANK["o3_d3"] = 0 if NEG_I_ODD else None
print(f"S3 orbit representatives: dots={len(dot_reps)} dets={len(det_reps)} dot.dot={len(dd_reps)} "
      f"soldered monomials d1={len(m1_reps)} d2={len(m2_reps)}")
print("S3 census, dimension of the lattice-odd (pseudo-scalar) span on the axis alphabet by degree:")
print(f"  unsoldered, internal SO(3) (dots+dets): d2={RANK['so3_d2']} d3={RANK['so3_d3']} d4={RANK['so3_d4']}")
print(f"  unsoldered, internal O(3) (dots only):  d2={RANK['o3_d2']} d3={RANK['o3_d3']} d4={RANK['o3_d4']}")
print(f"  soldered (all label components):        d1={RANK['sol_d1']} d2={RANK['sol_d2']}")

# coset parity: any function of at most two arm labels has vanishing alternating slot projection
def coset_parity_ok():
    for i in range(6):
        for j in range(6):
            tally = {}
            for M in G:
                key = (PERM[M][i], PERM[M][j])
                tally[key] = tally.get(key, 0) + detM(M)
            if any(tally.values()): return False
    return True
check("S3 coset parity: each ordered slot pair hit by equally many proper and improper ops",
      coset_parity_ok())
check("S3 unsoldered reading: no pseudo-scalar of degree <= 2 exists (SO(3) and O(3) families)",
      RANK["so3_d2"] == 0)
check("S3 unsoldered SO(3) reading: the lowest pseudo-scalar degree is 3 and the span is nonzero",
      RANK["so3_d3"] >= 1)
check("S3 T equals (1/6) of the alternating slot projection of det[q_+x, q_+y, q_+z]",
      proj_alt(arr_det((0, 2, 4)), "slots") == [6 * x for x in T_ARR])
check("S3 every det monomial is odd under -I: the O(3) reading has no degree-3 term",
      NEG_I_ODD)
check("S3 unsoldered O(3) reading: the lowest pseudo-scalar degree is 4 and D4 lies in that span",
      RANK["o3_d4"] >= 1 and rank_of(P["so3_d4"] + [D4_ARR]) == RANK["o3_d4"])
check("S3 soldered reading: no degree-1 pseudo-scalar; degree 2 is nonzero and contains Omega",
      RANK["sol_d1"] == 0 and RANK["sol_d2"] >= 1 and rank_of(P["sol_d2"] + [OM_ARR]) == RANK["sol_d2"])
check("S3 T is internally SO(3)-invariant and internally improper-odd; D4 is internally even",
      SIGN[("T", "internal")] == "odd" and SIGN[("D4", "internal")] == "even")
check("S3 Omega is not invariant under proper unsoldered slot rotations",
      any([OM_ARR[j] for j in m] != OM_ARR for s, m in MAPS["slots"] if s == 1))

# S4 ------------------------------------------------------------------------
# S4a Burnside census: dimensions of the invariant and the lattice-odd sectors of the function space
# on the six arms (6^6 configurations) and on the window with centre (6^7), for the three readings.
def cycles_of(p):
    seen, out = set(), []
    for i in range(6):
        if i in seen: continue
        n, j = 0, i
        while j not in seen:
            seen.add(j); j = p[j]; n += 1
        out.append(n)
    return out

def fix_count(sp, lp, with_centre):
    """Configurations fixed by (slot permutation sp, label permutation lp) = product over slot cycles
    of the number of labels fixed by lp^length; the centre is a length-1 cycle."""
    powers = [IDP]
    for _ in range(6): powers.append(tuple(lp[x] for x in powers[-1]))
    fixed = [sum(1 for l in range(6) if powers[n][l] == l) for n in range(7)]
    total = 1
    for n in cycles_of(sp): total *= fixed[n]
    return total * (fixed[1] if with_centre else 1)

def burnside(elements):
    """elements = (sign, slot perm, label perm); returns (inv6, odd6, inv7, odd7)."""
    n, acc = len(elements), [0, 0, 0, 0]
    for s, sp, lp in elements:
        f6, f7 = fix_count(sp, lp, False), fix_count(sp, lp, True)
        acc[0] += f6; acc[1] += s * f6; acc[2] += f7; acc[3] += s * f7
    assert all(a % n == 0 for a in acc), "Burnside sums must be divisible by the group order"
    return tuple(a // n for a in acc)

READINGS = {"unsoldered SO(3)": [(detM(M), PERM[M], LETPERM[R]) for M in G for R in PROPER],
            "unsoldered O(3)": [(detM(M), PERM[M], LETPERM[R]) for M in G for R in G],
            "soldered": [(detM(M), PERM[M], LETPERM[M]) for M in G]}
BURN = {k: burnside(v) for k, v in READINGS.items()}

def n_orbits(maps):
    seen, n = bytearray(NC), 0
    for k in range(NC):
        if seen[k]: continue
        n += 1
        for m in maps: seen[m[k]] = 1
    return n

def direct_inv_odd(act):
    full = n_orbits([m for s, m in MAPS[act]])
    return full, n_orbits([m for s, m in MAPS[act] if s == 1]) - full

DIRECT = {act: direct_inv_odd(act) for act in ("slots", "internal", "soldered")}
BURN_ONE = {"slots": burnside([(detM(M), PERM[M], IDP) for M in G]),
            "internal": burnside([(detM(M), IDP, LETPERM[M]) for M in G])}
print("S4a Burnside (inv6, odd6, inv7, odd7; handed rule terms = odd7-odd6, achiral = inv7-inv6):")
for k, (i6, o6, i7, o7) in BURN.items():
    print(f"  {k}: {i6} {o6} {i7} {o7} -> handed {o7 - o6}, achiral {i7 - i6}")
check("S4a Burnside agrees with direct orbit enumeration on the arms (three actions)",
      DIRECT["soldered"] == BURN["soldered"][:2] and DIRECT["slots"] == BURN_ONE["slots"][:2]
      and DIRECT["internal"] == BURN_ONE["internal"][:2])
check("S4a every reading admits handed rule terms (odd7 > odd6); soldered odd6 >= S3 rank",
      all(o7 > o6 for _, o6, _, o7 in BURN.values()) and BURN["soldered"][1] >= RANK["sol_d2"])

# S4b degree census of handed rule terms.  A rule term P(v, q) with sum_v P = 0 decomposes on the axis
# alphabet as sum_a v_a A_a(q) + sum_a v_a^2 B_a(q) with sum_a B_a = 0.  Unsoldered readings: v is inert
# under slot operations, so a handed term needs slot-odd A_a, B_a; the internal-covariant families of
# total degree <= 4 (cubic group, finite alphabet) are F1 q_i, F2 q_i x q_j (SO(3) only), F3 (q_i.q_j) q_k,
# F3' component triples (q_ia q_ja q_ka)_a, F4 axis-indicator pairs (q_ia q_ja)_a.
def cross(u, w): return (u[1]*w[2] - u[2]*w[1], u[2]*w[0] - u[0]*w[2], u[0]*w[1] - u[1]*w[0])
def arr_fn(f): return [f(vecs(c)) for c in CONFIGS]
def is_zero(arr): return not any(arr)
def mv_pk(M, pk): return (mv_pair(M, pk[0]), PERM[M][pk[1]])
def mv_tri(M, tr): return tuple(sorted(PERM[M][i] for i in tr))
pk_reps = orbit_reps([(pr, k) for pr in pairs for k in range(6)], mv_pk)
tri_reps = orbit_reps([t for t in combinations_with_replacement(range(6), 3) if len(set(t)) > 1], mv_tri)
pp_reps = orbit_reps([(i, j) for i in range(6) for j in range(i, 6)], mv_pair)
FAM = {}
FAM["F1 v.q_i (deg 2)"] = [arr_mono(((0, a),)) for a in range(3)]
FAM["F2 v.(q_i x q_j) (deg 3, SO(3))"] = [arr_fn(lambda q, i=i, j=j, a=a: cross(q[i], q[j])[a])
                                         for (i, j) in dot_reps for a in range(3)]
FAM["F3 v.q_k (q_i.q_j) (deg 4)"] = [arr_fn(lambda q, i=i, j=j, k=k, a=a: dot(q[i], q[j]) * q[k][a])
                                    for ((i, j), k) in pk_reps for a in range(3)]
FAM["F3' sum_a v_a q_ia q_ja q_ka (deg 4)"] = [arr_fn(lambda q, t=t, a=a: q[t[0]][a] * q[t[1]][a] * q[t[2]][a])
                                              for t in tri_reps for a in range(3)]
FAM["F4 sum_a v_a^2 q_ia q_ja (deg 4)"] = [arr_fn(lambda q, i=i, j=j, a=a: q[i][a] * q[j][a])
                                          for (i, j) in pp_reps for a in range(3)]
UNSOLD_ZERO = {k: all(is_zero(proj_alt(arr, "slots")) for arr in v) for k, v in FAM.items()}
S_ARR = [[sum(LET[x][a] for x in c) for c in CONFIGS] for a in range(3)]
TS = [[t * s for t, s in zip(T_ARR, S_ARR[a])] for a in range(3)]
DS = [[d * s for d, s in zip(D4_ARR, S_ARR[a])] for a in range(3)]
print("S4b unsoldered handed rule terms of total degree <= 4 (all families project to zero): "
      + ", ".join(f"{k.split()[0]}={'0' if z else 'NONZERO'}" for k, z in UNSOLD_ZERO.items()))
check("S4b unsoldered readings: no handed rule term of total degree <= 4",
      all(UNSOLD_ZERO.values()))
check("S4b unsoldered SO(3): T.(v.s) is a handed rule term of degree 5",
      all(grading_of(a, MAPS["slots"]) == "odd" for a in TS))
check("S4b unsoldered O(3): odd degree excluded by -I; D4.(v.s) is handed of degree 6",
      NEG_I_ODD and all(grading_of(a, MAPS["slots"]) == "odd" for a in DS)
      and all(grading_of(a, MAPS["internal"]) == "even" for a in [D4_ARR]))

# S4b soldered reading: v moves with the lattice (v -> Mv), so a handed v-linear term needs a vector
# field A(q) with A(g_M q) = det(M) M A(q) (pseudovector-covariant); the projector onto such fields is
# (PA)(q) = sum_M det(M) M^T A(g_M q).  A v-quadratic term needs B with sum_a B_a = 0 and
# B(g_M q) = det(M)|M| B(q); at arm degree 0 this is the coset-parity sum, which vanishes.
def proj_vec_component(b, arr):
    """Component arrays of P(e_b arr): (PA)_c[k] = sum_M det(M) M[b][c] arr[m_M[k]]."""
    out = [[0] * NC for _ in range(3)]
    for M, (s, m) in zip(G, MAPS["soldered"]):
        for c in range(3):
            w = s * M[b][c]
            if w == 0: continue
            row = out[c]
            for k in range(NC): row[k] += w * arr[m[k]]
    return out

SUM_DET_MT = [[sum(detM(M) * M[b][c] for M in G) for c in range(3)] for b in range(3)]
COSET_PARITY = [[sum(detM(M) for M in G if comp_map(M)[a] == b) for b in range(3)] for a in range(3)]
check("S4b soldered: no handed term of total degree <= 1 and no v^2-only degree-2 term",
      all(x == 0 for r in SUM_DET_MT for x in r) and all(x == 0 for r in COSET_PARITY for x in r))

def mv_iab(M, t):
    cm = comp_map(M)
    return (PERM[M][t[0]], cm[t[1]], cm[t[2]])
iab_reps = orbit_reps([(i, a, b) for i in range(6) for a in range(3) for b in range(3)], mv_iab)
VEC_PROJ = [proj_vec_component(b, arr_mono(((i, a),))) for (i, a, b) in iab_reps]
VEC_PROJ_FLAT = [comp[0] + comp[1] + comp[2] for comp in VEC_PROJ]
A_DM = [[sum(cross(SLOTVEC[i], q[i])[c] for i in range(6)) for q in map(vecs, CONFIGS)] for c in range(3)]
A_DM_FLAT = A_DM[0] + A_DM[1] + A_DM[2]
r_proj = rank_of([v for v in VEC_PROJ_FLAT if any(v)])
r_with = rank_of([v for v in VEC_PROJ_FLAT if any(v)] + [A_DM_FLAT])
dm_cov = all(A_DM[c][m[k]] == s * sum(M[c][e] * A_DM[e][k] for e in range(3))
             for M, (s, m) in zip(G, MAPS["soldered"]) for k in sample for c in range(3))
print(f"S4b soldered v-linear arm-degree-1 handed terms: {len(iab_reps)} orbit reps -> rank {r_proj}; "
      f"adding A_DM = sum_i r_i x q_i: rank {r_with}; max|A_DM| = {max(map(abs, A_DM_FLAT))}")
check("S4b soldered: degree-2 handed terms are one-dimensional, spanned by v.A_DM (lattice curl)",
      r_proj == 1 and r_with == 1 and any(A_DM_FLAT) and dm_cov)
P_DM_TAB = [[sum(LET[x][c] * A_DM[c][k] for c in range(3)) for x in range(6)] for k in range(NC)]
dm_window_ok = all(P_DM_TAB[m[k]][LETPERM[M][x]] == s * P_DM_TAB[k][x]
                   for M, (s, m) in zip(G, MAPS["soldered"]) for k in sample for x in range(6))
check("S4b soldered: v.A_DM is proper-invariant, improper-odd on the window, zero v-sum",
      dm_window_ok and all(sum(row) == 0 for row in P_DM_TAB))

# S4c rules.  Achiral base rule W_0(v|S) = (1/6)(1 + v.s_S/14), s_S = sum of the recorded arm vectors
# (uniform when no neighbour is recorded).  Handed rules W_X(v|q) = W_0 + eps_X P_X(v,q)/6 when all six
# arms are recorded, P_X = X(q) v.s for X in {T, D4, Omega} and P_DM = v.A_DM(q); eps_X = 1/E_X with
# E_X = 2(max|P_X| + 1) keeps every probability strictly positive.  Integer numerators over 84 E_X.
C_TAB = [[sum(LET[x][a] * S_ARR[a][k] for a in range(3)) for x in range(6)] for k in range(NC)]
P_TAB = {"T": [[T_ARR[k] * C_TAB[k][x] for x in range(6)] for k in range(NC)],
         "D4": [[D4_ARR[k] * C_TAB[k][x] for x in range(6)] for k in range(NC)],
         "Omega": [[OM_ARR[k] * C_TAB[k][x] for x in range(6)] for k in range(NC)],
         "DM": P_DM_TAB}
E_OF = {X: 2 * (max(abs(p) for row in tab for p in row) + 1) for X, tab in P_TAB.items()}

def rule_numerators(X, sign=1):
    """n_X(v|q) for all q, v; denominator 84*E_X (E=1 for the base rule X=None)."""
    if X is None:
        return [[14 + C_TAB[k][x] for x in range(6)] for k in range(NC)], 84
    E = E_OF[X]
    return [[14 * E + E * C_TAB[k][x] + 14 * sign * P_TAB[X][k][x] for x in range(6)] for k in range(NC)], 84 * E

RULES = {"W_0": rule_numerators(None)}
for X in P_TAB:
    RULES["W_" + X] = rule_numerators(X)
    RULES["W_-" + X] = rule_numerators(X, -1)
check("S4c every rule is normalised (sum_v = 1) on all 46656 arm configurations",
      all(all(sum(row) == den for row in tab) for tab, den in RULES.values()))
check("S4c every rule is strictly positive on all 279936 (v, q) pairs",
      all(min(min(row) for row in tab) > 0 for tab, _ in RULES.values()))
check("S4c every rule varies with the neighbour condition",
      all(len(set(map(tuple, tab))) > 1 for tab, _ in RULES.values()))
check("S4c base rule at one recorded neighbour, (14 + a.v)/84, is the law at s_S = a",
      all(min(14 + dot(LET[a], LET[x]) for a in range(6)) > 0
          and sum(14 + dot(LET[a], LET[x]) for a in range(6)) == 84 for x in range(6)))

def rule_grading(tab, act):
    """Behaviour of a 7-site rule table under the 48 operations of one action: invariant under proper ops
    and (even|odd|mixed) under improper ops; label perm for v is trivial in the slots action."""
    vperm = (lambda M: IDP) if act == "slots" else (lambda M: LETPERM[M])
    proper_ok, ev, od = True, True, True
    for M, (s, m) in zip(G, MAPS[act]):
        lp = vperm(M)
        same = all(tab[m[k]][lp[x]] == tab[k][x] for k in sample for x in range(6))
        if s == 1:
            proper_ok &= same
        else:
            ev &= same
            od &= all(tab[m[k]][lp[x]] == -tab[k][x] for k in sample for x in range(6))
    return proper_ok, ("even" if ev else "odd" if od else "mixed")

def handed_part(tab, den):
    """Odd numerators: n_X - n_0 * E (both over 84E)."""
    E = den // 84
    return [[tab[k][x] - E * (14 + C_TAB[k][x]) for x in range(6)] for k in range(NC)]

GR = {}
for X in P_TAB:
    tab, den = RULES["W_" + X]
    hp = handed_part(tab, den)
    GR[X] = {act: rule_grading(hp, act) for act in ("slots", "internal", "soldered")}
print("S4c handed parts (proper-covariant?/improper grading) for slots, internal, soldered: "
      + "; ".join(f"{X}: " + " ".join(f"{'cov' if ok else 'NOT'}/{g}" for ok, g in GR[X].values()) for X in GR))
base_cov = all(rule_grading(RULES["W_0"][0], act) == (True, "even") for act in ("slots", "internal", "soldered"))
check("S4c W_0 is covariant and mirror-even in every reading", base_cov)
check("S4c W_T: covariant, mirror-odd for unsoldered SO(3); mirror-even soldered",
      GR["T"]["slots"] == (True, "odd") and GR["T"]["internal"] == (True, "odd") and GR["T"]["soldered"] == (True, "even"))
check("S4c W_D4: covariant, mirror-odd for unsoldered O(3) and soldered",
      GR["D4"]["slots"] == (True, "odd") and GR["D4"]["internal"] == (True, "even") and GR["D4"]["soldered"] == (True, "odd"))
check("S4c W_Omega and W_DM: covariant and mirror-odd only in the soldered reading",
      GR["Omega"]["soldered"] == (True, "odd") and GR["DM"]["soldered"] == (True, "odd")
      and not GR["Omega"]["slots"][0] and not GR["DM"]["slots"][0])
def mirror_tab(tab, act):
    """(mirror W)(v|q) = W(M v | act_M q) for M = MIRX in the given action."""
    idx = G.index(MIRX)
    s, m = MAPS[act][idx]
    lp = IDP if act == "slots" else LETPERM[MIRX]
    return [[tab[m[k]][lp[x]] for x in range(6)] for k in range(NC)]
check("S4c mirror image of W_X is exactly W_-X (slot mirror: T, D4; soldered mirror: D4, Omega, DM)",
      mirror_tab(RULES["W_T"][0], "slots") == RULES["W_-T"][0]
      and mirror_tab(RULES["W_D4"][0], "slots") == RULES["W_-D4"][0]
      and all(mirror_tab(RULES["W_" + X][0], "soldered") == RULES["W_-" + X][0] for X in ("D4", "Omega", "DM"))
      and mirror_tab(RULES["W_T"][0], "soldered") == RULES["W_T"][0])

# S5 exact parity-odd record correlators on the seven-site window.  Formation laws: centre-last (arms
# form first with no recorded neighbour, hence uniform; the centre then forms under W_X with all six arms
# recorded); static (joint weight = product of all seven local conditionals); uniform mixture over
# formation orders (the arms recorded before the centre form a subset S; the handed term acts only when
# S is the full cross); centre-first (S empty).  All sums are exact integers over known denominators.
XS = list(P_TAB)
ARM_T = [[[dot(q[i], LET[x]) for i in range(6)] for x in range(6)] for q in map(vecs, CONFIGS)]
PROD = [[1] * 6 for _ in range(NC)]
for k in range(NC):
    for x in range(6):
        p = 1
        for t in ARM_T[k][x]: p *= 14 + t
        PROD[k][x] = p

def centre_last(tab, den, Y):
    return Fr(sum(tab[k][x] * P_TAB[Y][k][x] for k in range(NC) for x in range(6)), 6 ** 6 * den)

def static(tab, Y):
    num = sum(tab[k][x] * PROD[k][x] * P_TAB[Y][k][x] for k in range(NC) for x in range(6))
    Z = sum(tab[k][x] * PROD[k][x] for k in range(NC) for x in range(6))
    return Fr(num, Z)

def subset_numerator(S, Y):
    """Order class with arm subset S recorded before the centre (S != full cross): integer numerator."""
    tot = 0
    for k in range(NC):
        for x in range(6):
            w = 14 + sum(ARM_T[k][x][i] for i in S)
            for i in range(6):
                if i not in S: w *= 14 + ARM_T[k][x][i]
            tot += w * P_TAB[Y][k][x]
    return tot

CL = {X: {Y: centre_last(*RULES["W_" + X], Y) for Y in XS} for X in XS}
CLM = {X: centre_last(*RULES["W_-" + X], X) for X in XS}
CL0 = {Y: centre_last(*RULES["W_0"], Y) for Y in XS}
ST = {X: static(RULES["W_" + X][0], X) for X in XS}
STM = {X: static(RULES["W_-" + X][0], X) for X in XS}
ST0 = {Y: static(RULES["W_0"][0], Y) for Y in XS}
SUBSETS = [(), (0,), (0, 1, 2, 3, 4)]
SUB0 = all(subset_numerator(S, Y) == 0 for S in SUBSETS for Y in XS)
def even_stat(tab, den):
    return Fr(sum(tab[k][x] * C_TAB[k][x] for k in range(NC) for x in range(6)), 6 ** 6 * den)
EVEN_EQ = all(even_stat(*RULES["W_" + X]) == even_stat(*RULES["W_-" + X]) for X in XS)
print("S5 centre-last E[P_Y] under W_X (rows X, cols Y; T, D4, Omega, DM):")
for X in XS:
    print(f"  {X}: " + " ".join(str(CL[X][Y]) for Y in XS))
print("S5 static: " + " ".join(f"{X}={ST[X]}" for X in XS) + "; mixture=centre-last/7")
check("S5 W_0 leaves every parity-odd correlator at zero (centre-last and static)",
      all(v == 0 for v in CL0.values()) and all(v == 0 for v in ST0.values()))
check("S5 each handed rule leaves a positive trace in its own texture; its mirror negates it",
      all(CL[X][X] > 0 and CLM[X] == -CL[X][X] and ST[X] > 0 and STM[X] == -ST[X] for X in XS))
check("S5 T-row and T-column cross entries vanish (internal parity)",
      all(CL["T"][Y] == 0 and CL[Y]["T"] == 0 for Y in ("D4", "Omega", "DM")))
check("S5 order classes with an unrecorded arm carry no handed trace (S = empty, one, five arms)", SUB0)
check("S5 even statistic E[v.s] identical for W_X and W_-X", EVEN_EQ)

# S6 underdetermination witnesses.  In each reading the group is a set of (det, slot perm, letter perm)
# triples; a rule's handed part is classified on sampled configurations as covariant-handed (fixed by
# every proper element, negated by every improper one), achiral (fixed by all) or neither.
S6_SAMPLE = sample[:120]

def image_index(sp, lp, c):
    return sum(lp[c[i]] * POW6[sp[i]] for i in range(6))

def classify(X, elements):
    H = handed_part(*RULES["W_" + X])
    fixed = neg = True
    for s, sp, lp in elements:
        for k in S6_SAMPLE:
            k2 = image_index(sp, lp, CONFIGS[k])
            for x in range(6):
                a, b = H[k2][lp[x]], H[k][x]
                if s > 0:
                    if a != b: return "not covariant"
                else:
                    fixed = fixed and a == b
                    neg = neg and a == -b
    return "handed" if neg else ("achiral" if fixed else "mixed")

check("S6 sampled image index agrees with the soldered action map",
      all(image_index(PERM[M], LETPERM[M], CONFIGS[k]) == MAPS["soldered"][G.index(M)][1][k]
          for M in G[::5] for k in S6_SAMPLE))
CLASS = {r: {X: classify(X, els) for X in XS} for r, els in READINGS.items()}
WITNESS = {"unsoldered SO(3)": "T", "unsoldered O(3)": "D4", "soldered": "DM"}
for r in READINGS:
    print(f"S6 {r}: " + ", ".join(f"{X}={CLASS[r][X]}" for X in XS))
check("S6 witness pairs W_0/W_T (unsoldered SO(3)), W_0/W_D4 (O(3)), W_0/W_DM (soldered): covariant, "
      "differ on the handed trace, mirror rule negates it",
      all(CLASS[r][X] == "handed" and CL0[X] == 0 and CL[X][X] > 0 and CLM[X] == -CL[X][X]
          for r, X in WITNESS.items()))
check("S6 T: handed under unsoldered SO(3), not covariant under O(3), achiral when soldered",
      CLASS["soldered"]["T"] == "achiral" and CLASS["unsoldered O(3)"]["T"] == "not covariant"
      and CLASS["unsoldered SO(3)"]["T"] == "handed")
check("S6 D4 is handed in all three readings; Omega and DM are handed only when soldered",
      all(CLASS[r]["D4"] == "handed" for r in READINGS)
      and all(CLASS[r][X] == ("handed" if r == "soldered" else "not covariant")
              for r in READINGS for X in ("Omega", "DM")))
print("S6 separating clauses (recorded, no owner gate): SO(3) vs O(3); soldered vs unsoldered; parity fix")
check("S6 stdout stays under the 6000-byte ceiling", OUT.n < 5850, f"{OUT.n} bytes")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
