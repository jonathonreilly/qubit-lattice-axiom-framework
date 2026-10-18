#!/usr/bin/env python3
"""Fresh-context reviewer check for the C1 note (T2, T3, T4, T7, T9) by pure group theory / exact arithmetic.

Independent of the runner: no model, no lifts, no null spaces.  Inputs are only
  * O = 24 proper signed-permutation matrices;
  * det_K = A2 (for the real lift) on O, taken here as the sign of the S4 permutation of the 4 body diagonals
    (an independent definition of A2; the runner uses a class table);
  * the affine action on cube points: since k* is fixed by every g (little group O), g(k* + pi n) = k* + pi M_g n,
    so the doubler stabiliser is {M : M n = n mod 2} -- derived, not read from the runner;
  * the chirality pattern chi(k* + pi n) = s (-1)^|n| (numerical input of the note, both signs s).
T4 prediction: (H, chi) is selective iff chi != A2|H (forbidden at +-k*) and chi|H_n = A2|H_n for some doubler n.
This is the necessary condition; the runner's count additionally needs nonempty, generic on-site channels.
"""
import itertools
from fractions import Fraction as Fr
import numpy as np

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

O = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1: O.append(M)
key = lambda M: tuple(M.flatten())
IDX = {key(M): i for i, M in enumerate(O)}
MUL = [[IDX[key(O[a] @ O[b])] for b in range(24)] for a in range(24)]
E0 = IDX[key(np.eye(3, dtype=int))]

# A2 as sign of the permutation of the 4 body diagonals (up to sign)
DIAG = [np.array(v) for v in ((1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1))]
def diag_index(v):
    for i, d in enumerate(DIAG):
        if (v == d).all() or (v == -d).all(): return i
def perm_sign(p):
    s = 1; p = list(p)
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
    return s
A2 = [perm_sign([diag_index(O[g] @ d) for d in DIAG]) for g in range(24)]
check("A2 = sign of S4 action on body diagonals is a character, nontrivial, -1 on C4 (trace 1)",
      all(A2[MUL[a][b]] == A2[a] * A2[b] for a in range(24) for b in range(24)) and
      all(A2[g] == -1 for g in range(24) if np.trace(O[g]) == 1))

# all subgroups via closure of generator triples
def closure(gens):
    S = {E0} | set(gens); frontier = list(S)
    while frontier:
        new = []
        for a in frontier:
            for b in list(S):
                for c in (MUL[a][b], MUL[b][a]):
                    if c not in S: S.add(c); new.append(c)
        frontier = new
    return frozenset(S)
subs = set()
for r in range(0, 4):
    for gens in itertools.combinations(range(24), r): subs.add(closure(gens))
subs = sorted(subs, key=len)
check("O has exactly 30 subgroups", len(subs) == 30, f"orders {sorted(len(H) for H in subs)}")

def order(g):
    x, n = g, 1
    while x != E0: x = MUL[x][g]; n += 1
    return n
def characters(H):
    """all homomorphisms H -> C*, values as exponents mod 12 (exp(2 pi i a/12))."""
    H = sorted(H); out = []
    def rec(i, val):
        if i == len(H):
            if all((val[a] + val[b]) % 12 == val[MUL[a][b]] for a in H for b in H): out.append(dict(val))
            return
        h = H[i]
        if h in val: rec(i + 1, val); return
        o = order(h)
        for a in range(0, 12, 12 // o if 12 % o == 0 else 1):
            if (a * o) % 12: continue
            val2 = dict(val); val2[h] = a; okk = True
            # propagate powers
            x, p = h, a
            for _ in range(o):
                if x in val2 and val2[x] != p: okk = False; break
                val2[x] = p; x = MUL[x][h]; p = (p + a) % 12
            if not okk: continue
            # quick consistency on assigned products
            if all((val2[u] + val2[v]) % 12 == val2[MUL[u][v]] for u in val2 for v in val2 if MUL[u][v] in val2):
                rec(i + 1, val2)
    rec(0, {E0: 0})
    uniq = []
    for c in out:
        if c not in uniq: uniq.append(c)
    return uniq
a2exp = {g: (0 if A2[g] == 1 else 6) for g in range(24)}
DOUB = [n for n in itertools.product((0, 1), repeat=3) if 0 < sum(n) < 3]
def stab_n(H, n): return [g for g in H if tuple((O[g] @ np.array(n)) % 2) == n]

nchar_total = 0; selective = []; full_O_selective = []
for H in subs:
    chars = characters(H); nchar_total += len(chars)
    for c in chars:
        forb_star = any(c[g] != a2exp[g] for g in H)
        allowed = [n for n in DOUB if all(c[g] == a2exp[g] for g in stab_n(H, n))]
        if forb_star and allowed: selective.append((len(H), len(allowed), H, c))
        if len(H) == 24 and ((not forb_star) != bool(len(allowed) == 6)): full_O_selective.append(c)
print(f"   total (H, chi) pairs: {nchar_total}")
orders = sorted(set(s[0] for s in selective))
byorder = {o: sum(1 for s in selective if s[0] == o) for o in orders}
T_sel = [s for s in selective if s[0] == 12]
check("T4 (group-theory prediction) selective (H, chi): count 25, orders {2,3,4,8,12}, none for O",
      len(selective) == 25 and orders == [2, 3, 4, 8, 12] and not any(s[0] == 24 for s in selective),
      f"count {len(selective)}; by order {byorder}")
check("T4: for T exactly two selective characters, chi(C3) = omega, omega-bar, each allowing all six doublers",
      len(T_sel) == 2 and all(s[1] == 6 for s in T_sel) and
      sorted(s[3][[g for g in s[2] if np.trace(O[g]) == 0][0]] for s in T_sel) in ([4, 8],))
check("T3 under full O: A1 forbids all eight, A2 allows all eight (no selective full-O channel)",
      not full_O_selective and len(characters(subs[-1])) == 2)
# doubler stabiliser is D4 about the axis singled out by n
check("doubler little groups: |G_n| = 8 for each of the six doublers, containing exactly two C4 (trace 1)",
      all(len(stab_n(range(24), n)) == 8 and sum(np.trace(O[g]) == 1 for g in stab_n(range(24), n)) == 2 for n in DOUB))

# ---- T2: rotation-fixed vectors in R^3 / 2 pi Z^3, rational denominators up to 12 ----
fixed = []
for d in (1, 2, 3, 4, 6, 12):
    for q in itertools.product(range(2 * d), repeat=3):   # q / d in units of pi
        v = np.array(q)
        if all(tuple((M @ v) % (2 * d)) == q for M in O):
            fixed.append(tuple(Fr(x, d) for x in q))
fixed = sorted(set(fixed))
check("T2: O-fixed points of the torus at denominators <= 12 are exactly 0 and pi(1,1,1)",
      fixed == [(0, 0, 0), (1, 1, 1)], str(fixed))

# ---- T7: dipole bookkeeping in exact fractions of pi ----
kst = (Fr(1, 2), Fr(-1, 2), Fr(1, 2))
def K(n): return tuple(k + x for k, x in zip(kst, n))
def mod2(v): return tuple(x % 2 for x in v)
ok7 = True; tabs = {}
for s in (1, -1):
    chi = {n: s * (-1) ** sum(n) for n in itertools.product((0, 1), repeat=3)}
    orbs = {'k*': [(0, 0, 0)], '-k*': [(1, 1, 1)], 'A': [n for n in DOUB if sum(n) == 1], 'B': [n for n in DOUB if sum(n) == 2]}
    tab = {}
    for r in range(5):
        for combo in itertools.combinations(orbs, r):
            S = [n for o in combo for n in orbs[o]]
            net = sum(chi[n] for n in S)
            b = tuple(sum(chi[n] * K(n)[i] for n in S) for i in range(3))
            # representative independence: shift each node by a random 2 pi lattice vector
            rngv = np.random.default_rng(len(S) + 7 * r)
            b2 = tuple(sum(chi[n] * (K(n)[i] + 2 * int(rngv.integers(-2, 3))) for n in S) for i in range(3))
            if net == 0: ok7 &= mod2(b) == mod2(b2)
            tab['+'.join(combo) or 'empty'] = (net, mod2(b))
    ok7 &= tab['A+B'] == (0, (1, 1, 1)) and tab['k*+-k*'] == (0, (1, 1, 1)) and tab['k*+-k*+A+B'] == (0, (0, 0, 0))
    free = sorted(l for l, (net, b) in tab.items() if net == 0 and b == (0, 0, 0))
    netzero = sorted(l for l, (net, b) in tab.items() if net == 0)
    ok7 &= free == sorted(['empty', 'k*+-k*+A+B']) and netzero == sorted(['empty', 'k*+-k*', 'A+B', 'k*+-k*+A+B'])
    tabs[s] = tab
check("T7: b/pi mod 2: A+B -> (1,1,1), {+-k*} -> (1,1,1), all -> 0; net-zero subsets are exactly empty, {+-k*}, A+B, all; "
      "only empty and all are anomaly-free; representative-independent; either sign", ok7)

# ---- T9: jump on the plane k_z = pi/2 for the three node sets (exact) ----
def J(S, s):
    chi = {n: s * (-1) ** sum(n) for n in itertools.product((0, 1), repeat=3)}
    return sum(chi[n] for n in S if K(n)[2] % 2 == Fr(1, 2))
Jv = {s: (J([(0, 0, 0), (1, 1, 1)], s), J(DOUB, s), J(list(itertools.product((0, 1), repeat=3)), s)) for s in (1, -1)}
check("T9: jump at k_z = pi/2 is odd for {+-k*} only and for doublers only, 0 for all eight (C2x requires J = 2 nu(0) even)",
      all(a % 2 == 1 and b % 2 == 1 and c == 0 for a, b, c in Jv.values()), str(Jv))
# C2x affine map on k_z: k* fixed => theta = k* - M k*; z-component
C2x = np.diag([1, -1, -1]); th = tuple(k - x for k, x in zip(kst, C2x @ np.array(kst)))
check("T9: C2x fixing k* has affine shift with theta_z = pi (mod 2pi), so it maps slice k_z -> pi - k_z",
      th[2] % 2 == 1, f"theta/pi = {th}")
# T6: Q = 0 partners K <-> -K have opposite chirality; Q = pi p partner equal iff |p| odd
ok6 = True
for p in itertools.product((0, 1), repeat=3):
    for n in itertools.product((0, 1), repeat=3):
        partner = tuple((p[i] - n[i] + 1) % 2 for i in range(3))   # Q - k* - pi n = k* + pi(p - n + 1) mod 2pi
        ok6 &= ((-1) ** sum(n) == (-1) ** sum(partner)) == (sum(p) % 2 == 1)
check("T6/A19: partner chiralities under Q = pi p are equal iff |p| odd (Q = 0: opposite; Q = R: equal)", ok6)

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
