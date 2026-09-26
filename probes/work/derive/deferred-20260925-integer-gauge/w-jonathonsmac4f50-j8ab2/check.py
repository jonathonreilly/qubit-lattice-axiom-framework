#!/usr/bin/env python3
"""Box-free minimum moves of the landed tensor vector stencil (J:derive:deferred-20260925-integer-gauge:a1).

Stencil (landed tensor parent, as restated in the landed PR 9077/9095 notes on main):
    (Gp)_j(x) = p_jj(x+e_j) - p_jj(x) + sum_{i!=j} [p_ij(x) - p_ij(x-e_i)],   x in Z^3, p_ij = p_ji.
A move is a nonzero finite-support vector v with Gv = 0 (static charges).  All arithmetic is exact (int / Fraction / sympy).

A  encoding: doubled-coordinate rows use the six neighbours of the link site with coefficients +-1
B  generating functions: Row_j = sum_i u_i Q_ij with u_i = 1 - t_i, Q_jj = t_j^{-1} P_jj, Q_ij = P_ij
C  the named planar move is Airy(phi = monomial): Q_aa = u_b^2, Q_bb = u_a^2, Q_ab = -u_a u_b
D  proof identities (the algebraic proof itself is in ATTEMPT.md)
E  independent box-free exhaustive search: every connected support of size <= 12 through a lex-minimal anchor
F  consequences over Z: support >= 10, L1 >= 12, equality exactly the planar moves; unit-entry moves have support >= 14
G  the same leaves over Z_N, N = 2..13: minimum support and minimum cyclic step count (even-N cube preserved)
H  the order-12 amplitude A = 111150053/31850496 re-derived by exact recursion; no proper partial state is a move
"""
import itertools, sys, time
from fractions import Fraction
import sympy as sp

T0 = time.time()
FAIL = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""), flush=True)
    if not ok: FAIL.append(name)

# ---------------------------------------------------------------- lattice G in coarse coordinates (straight from the formula)
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
def vadd(a, b, s=1): return (a[0] + s*b[0], a[1] + s*b[1], a[2] + s*b[2])
def slot_key(i, j): return (min(i, j), max(i, j))
def G_apply(p):
    """p: dict {((i,j), x): int}; returns dict {(j, x): value} of nonzero rows."""
    rows = {}
    for ((i, j), x), val in p.items():
        if val == 0: continue
        if i == j:      # p_jj enters row j at x-e_j with +1 and row j at x with -1
            for r, s in (((j, vadd(x, E3[j], -1)), 1), ((j, x), -1)):
                rows[r] = rows.get(r, 0) + s*val
        else:           # p_ij enters rows j and i at x with +1, and at x+e_i (row j), x+e_j (row i) with -1
            for (row, shift) in ((j, i), (i, j)):
                rows[(row, x)] = rows.get((row, x), 0) + val
                y = vadd(x, E3[shift]); rows[(row, y)] = rows.get((row, y), 0) - val
    return {k: v for k, v in rows.items() if v != 0}

# ---------------------------------------------------------------- doubled coordinates
def dbl_of_slot(ij, x):
    i, j = ij
    y = (2*x[0], 2*x[1], 2*x[2])
    if i == j: return (y, i)
    return (vadd(vadd(y, E3[i]), E3[j]), -1)
def slot_of_dbl(sl):
    y, c = sl
    o = [k for k in range(3) if y[k] % 2]
    x = tuple((y[k] - (y[k] % 2)) // 2 for k in range(3))
    return ((c, c), x) if not o else ((o[0], o[1]), x)
def odd(y): return [k for k in range(3) if y[k] % 2]
def slot_rows(sl):
    y, c = sl
    o = odd(y)
    if not o: return [vadd(y, E3[c]), vadd(y, E3[c], -1)]
    return [vadd(y, E3[k], s) for k in o for s in (1, -1)]
def row_slots(r):
    d = odd(r)[0]
    return [((vadd(r, E3[k], s), d if k == d else -1), s) for k in range(3) for s in (1, -1)]
def row_of_dbl(r):
    d = odd(r)[0]
    return (d, tuple((r[k] - (r[k] % 2)) // 2 for k in range(3)))

print("== A  encoding")
okA = True
for j in range(3):
    for x in [(0, 0, 0), (1, -2, 3), (-1, 1, 0)]:
        for ij in [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]:
            sl = dbl_of_slot(ij, x)
            direct = G_apply({(ij, x): 1})
            viaD = {}
            for r in slot_rows(sl):
                coef = [s for t, s in row_slots(r) if t == sl]
                if len(coef) != 1: okA = False
                viaD[row_of_dbl(r)] = coef[0]
            if direct != viaD: okA = False
            if slot_of_dbl(sl) != (ij, x): okA = False
for r in [(1, 0, 0), (0, 3, 2), (4, -2, -1)]:
    rs = row_slots(r)
    if sorted(t[0] for t, _ in rs) != sorted(vadd(r, E3[k], s) for k in range(3) for s in (1, -1)): okA = False
check("A1 each row is the six neighbours of its link site, coefficients +-1; doubled encoding = formula", okA)

# ---------------------------------------------------------------- Laurent polynomials as dicts {exponent: int}
def L_add(*fs):
    out = {}
    for f in fs:
        for e, c in f.items(): out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c != 0}
def L_scale(f, a): return {e: a*c for e, c in f.items() if a*c != 0}
def L_shift(f, d): return {vadd(e, d): c for e, c in f.items()}
def L_u(f, i): return L_add(f, L_scale(L_shift(f, E3[i]), -1))          # (1 - t_i) f
def L_mono(e=(0, 0, 0), c=1): return {e: c}

def P_to_Q(p):
    Q = {}
    for ((i, j), x), val in p.items():
        if val == 0: continue
        e = x if i != j else vadd(x, E3[i], -1)       # Q_jj = t_j^{-1} P_jj
        Q.setdefault((i, j), {}); Q[(i, j)][e] = Q[(i, j)].get(e, 0) + val
    return Q
def Q_to_P(Q):
    p = {}
    for (i, j), f in Q.items():
        for e, c in f.items():
            if c == 0: continue
            x = e if i != j else vadd(e, E3[i])
            p[((i, j), x)] = p.get(((i, j), x), 0) + c
    return p
def Q_rows(Q):
    out = {}
    for j in range(3):
        terms = [L_u(Q.get(slot_key(i, j), {}), i) for i in range(3)]
        out[j] = L_add(*terms)
    return out

print("== B  generating functions")
import random
rng = random.Random(20260926)
okB = True
for trial in range(40):
    p = {}
    for _ in range(25):
        ij = slot_key(rng.randrange(3), rng.randrange(3))
        x = tuple(rng.randrange(-2, 3) for _ in range(3))
        p[(ij, x)] = p.get((ij, x), 0) + rng.randrange(-3, 4)
    direct = G_apply(p)
    R = Q_rows(P_to_Q(p))
    viaQ = {(j, e): c for j in range(3) for e, c in R[j].items() if c != 0}
    if direct != viaQ: okB = False
check("B1 (Gp)_j(x) = [t^x] sum_i (1-t_i) Q_ij on 40 random integer vectors", okB)

# ---------------------------------------------------------------- planar moves
def airy(a, b, phi):
    """Q_aa = u_b^2 phi, Q_bb = u_a^2 phi, Q_ab = -u_a u_b phi (others zero)."""
    return {(a, a): L_u(L_u(phi, b), b), (b, b): L_u(L_u(phi, a), a), slot_key(a, b): L_scale(L_u(L_u(phi, a), b), -1)}
def planar_p(a, b, c=(0, 0, 0)):
    """the landed named displacement around coarse vertex c."""
    ea, eb = E3[a], E3[b]
    p = {((a, a), c): -2, ((b, b), c): -2,
         ((a, a), vadd(c, eb)): 1, ((a, a), vadd(c, eb, -1)): 1, ((b, b), vadd(c, ea)): 1, ((b, b), vadd(c, ea, -1)): 1}
    ab = slot_key(a, b)
    for base, s in ((c, -1), (vadd(c, ea, -1), 1), (vadd(c, eb, -1), 1), (vadd(vadd(c, ea, -1), eb, -1), -1)):
        p[(ab, base)] = s
    return p
def clean(p): return {k: v for k, v in p.items() if v != 0}

print("== C  planar moves")
okC = True
for a, b in [(0, 1), (0, 2), (1, 2)]:
    c = (0, 0, 0)
    pp = planar_p(a, b, c)
    phi = L_mono(vadd(vadd(c, E3[a], -1), E3[b], -1))
    if clean(Q_to_P(airy(a, b, phi))) != clean(pp): okC = False
    if G_apply(pp): okC = False
    if len(clean(pp)) != 10 or sum(abs(v) for v in pp.values()) != 12: okC = False
    if len({dbl_of_slot(ij, x)[0] for (ij, x) in pp}) != 9: okC = False
check("C1 named planar move = Airy(monomial) in each plane; Gv=0; support 10 on 9 sites; L1 12", okC)

# ---------------------------------------------------------------- proof identities
print("== D  proof identities (symbolic)")
u1, u2, u3, phi, a_, b_, beta = sp.symbols("u1 u2 u3 phi a b beta")
U = [u1, u2, u3]
def rows_sym(Q):
    return [sp.expand(sum(U[i]*Q.get(slot_key(i, j), 0) for i in range(3))) for j in range(3)]
Qair = {(0, 0): u2**2*phi, (1, 1): u1**2*phi, (0, 1): -u1*u2*phi}
check("D1 Airy triple solves the planar rows identically", rows_sym(Qair) == [0, 0, 0])
Q0 = {(0, 1): u3*a_, (0, 2): -u2*a_, (1, 2): -u1*a_}
r0 = rows_sym(Q0)
check("D2 no diagonal: rows 1,2 solved, row 3 = -2 u1 u2 a (so a = 0 in characteristic 0)",
      r0[0] == 0 and r0[1] == 0 and sp.expand(r0[2] + 2*u1*u2*a_) == 0)
Q1 = {(0, 0): -2*u2*u3*beta, (0, 1): u1*u3*beta, (0, 2): u1*u2*beta, (1, 2): -u1**2*beta}
check("D3 one diagonal: the derived family solves all three rows", rows_sym(Q1) == [0, 0, 0])
Q1b = {(0, 0): sp.Symbol("Q11"), (0, 1): u3*b_, (0, 2): u2*b_, (1, 2): -u1*b_}
r1 = rows_sym(Q1b)
check("D4 one diagonal: rows 2,3 solved by (u3 b, u2 b, -u1 b); row 1 = u1 Q11 + 2 u2 u3 b",
      r1[1] == 0 and r1[2] == 0 and sp.expand(r1[0] - u1*sp.Symbol("Q11") - 2*u2*u3*b_) == 0)
t, A_, B_, m, n = sp.symbols("t A B m n")
f2 = A_*t**m + B_*t**n
sol = sp.solve([f2.subs(t, 1), sp.diff(f2, t).subs(t, 1)], [A_, B_], dict=True)
check("D5 a two-term Laurent polynomial with a double root at t=1 is zero when m != n", sol == [{A_: 0, B_: 0}], str(sol))
# the three-term/L1 facts used for integer vectors: three nonzero integers summing to 0 have L1 >= 4
check("D6 three nonzero integers with zero sum have L1 >= 4",
      min(abs(x) + abs(y) + abs(x + y) for x in range(-5, 6) for y in range(-5, 6) if x and y and x + y) == 4)

# ---------------------------------------------------------------- exhaustive box-free search
print("== E  box-free exhaustive search (connected supports through a lex-minimal anchor)")
def key(sl): return (sl[0], sl[1])
ANCHORS = [((0, 0, 0), 0), ((0, 0, 0), 1), ((0, 0, 0), 2), ((1, 1, 0), -1), ((1, 0, 1), -1), ((0, 1, 1), -1)]
def search(anchor, budget, leaves, stats):
    ak = key(anchor)
    def status(S, OUT):
        best = None
        for sl in S:
            for r in slot_rows(sl):
                cnt = 0; und = []
                for tt, _ in row_slots(r):
                    if tt in S: cnt += 1
                    elif tt in OUT or key(tt) < ak: pass
                    else: und.append(tt)
                if not und:
                    if cnt == 1: return True, None
                    continue
                pr = (0 if cnt == 1 else 1, len(und))
                if best is None or pr < best[0]: best = (pr, r, und, cnt)
        return False, best
    def rec(S, OUT):
        stats["nodes"] += 1
        dead, best = status(S, OUT)
        if dead: return
        if best is None:
            leaves.append(frozenset(S)); return
        _, r, und, cnt = best
        room = budget - len(S); nn = len(und)
        for mask in range(1 << nn):
            A = [und[i] for i in range(nn) if mask >> i & 1]
            if len(A) > room or cnt + len(A) == 1: continue
            rec(S | frozenset(A), OUT | frozenset(u for u in und if u not in A))
    rec(frozenset([anchor]), frozenset())

BUDGET = 12
leaves, stats = [], {"nodes": 0}
for an in ANCHORS:
    search(an, BUDGET, leaves, stats)
print(f"   budget {BUDGET}: {stats['nodes']} nodes, {len(leaves)} closed leaves, {time.time()-T0:.0f}s", flush=True)
def leaf_matrix(S):
    cols = sorted(S)
    rows = sorted({r for sl in S for r in slot_rows(sl)})
    idx = {c: i for i, c in enumerate(cols)}
    M = []
    for r in rows:
        v = [0]*len(cols)
        for tt, s in row_slots(r):
            if tt in idx: v[idx[tt]] = s
        M.append(v)
    return cols, M
def kernel_Q(M, ncol):
    A = [[Fraction(x) for x in row] for row in M]
    piv = []; rk = 0
    for c in range(ncol):
        pr = next((i for i in range(rk, len(A)) if A[i][c] != 0), None)
        if pr is None: continue
        A[rk], A[pr] = A[pr], A[rk]
        pv = A[rk][c]; A[rk] = [x / pv for x in A[rk]]
        for i in range(len(A)):
            if i != rk and A[i][c] != 0:
                f = A[i][c]; A[i] = [x - f*y for x, y in zip(A[i], A[rk])]
        piv.append(c); rk += 1
    free = [c for c in range(ncol) if c not in piv]
    basis = []
    for fcol in free:
        v = [Fraction(0)]*ncol; v[fcol] = Fraction(1)
        for i, pc in enumerate(piv): v[pc] = -A[i][fcol]
        basis.append(v)
    return basis
def primitive(v):
    from math import gcd
    den = 1
    for x in v: den = den*x.denominator // gcd(den, x.denominator)
    w = [int(x*den) for x in v]
    g = 0
    for x in w: g = gcd(g, abs(x))
    return [x // g for x in w]

# integer (rational) kernels of every leaf
qdef = []
for S in leaves:
    cols, M = leaf_matrix(S)
    B = kernel_Q(M, len(cols))
    if B: qdef.append((S, cols, B))
check("E1 no nonzero rational (hence integer or real) move has support <= 9",
      all(len(S) >= 10 for S, _, _ in qdef), f"{len(qdef)} rank-deficient leaves, sizes {sorted(len(S) for S,_,_ in qdef)}")
# identify them with the planar moves
def canon_dbl(vecmap):
    """translate so that the lex-minimal slot sits at the canonical anchor representative; returns frozenset of (slot, coef)."""
    mn = min(vecmap, key=key)
    y = mn[0]; sh = tuple(-2*((y[k] - (y[k] % 2)) // 2) for k in range(3))
    return frozenset(((vadd(sl[0], sh), sl[1]), c) for sl, c in vecmap.items())
planar_canon = set()
for a, b in [(0, 1), (0, 2), (1, 2)]:
    for sgn in (1, -1):
        pp = planar_p(a, b)
        planar_canon.add(canon_dbl({dbl_of_slot(ij, x): sgn*v for (ij, x), v in pp.items()}))
okE2 = True; detail = []
for S, cols, B in qdef:
    if len(B) != 1: okE2 = False
    v = primitive(B[0])
    vm = {cols[i]: v[i] for i in range(len(cols)) if v[i] != 0}
    if canon_dbl(vm) not in planar_canon: okE2 = False
    detail.append((len(S), len(vm), sum(abs(x) for x in v)))
check("E2 every rational move with connected support <= 12 is a multiple of a planar move (3 planes)", okE2 and len(qdef) == 3, str(detail))

print("== F  consequences over Z (proof in ATTEMPT.md; E is the independent confirmation)")
# any move with support <= 12 has connected components that are moves of support >= 10, so it is connected; E2 applies.
check("F1 minimum support of a nonzero integer move = 10, attained exactly by c*(planar move), c != 0", okE2)
check("F2 minimum L1 = 12 (L1 <= 12 forces support <= 12, hence c*planar with L1 = 12|c|); equality iff +-planar", okE2)
check("F3 unit-entry (qubit-step) moves: support >= 13 by E2 (planar has entries -2) and even L1 -> >= 14", okE2)

# ---------------------------------------------------------------- Z_N
print("== G  clock slots Z_N (same leaves; a Z_N move's minimal support is connected and passes the same row test)")
def smith(M):
    """returns (d, V) with U M V = diag(d) for unimodular U, V (V as list of columns)."""
    A = [row[:] for row in M]; m = len(A); n = len(A[0]) if m else 0
    V = [[int(i == j) for j in range(n)] for i in range(n)]
    def colop(c1, c2, f):  # col c1 -= f*col c2
        for r in range(m): A[r][c1] -= f*A[r][c2]
        for r in range(n): V[r][c1] -= f*V[r][c2]
    def colswap(c1, c2):
        for r in range(m): A[r][c1], A[r][c2] = A[r][c2], A[r][c1]
        for r in range(n): V[r][c1], V[r][c2] = V[r][c2], V[r][c1]
    d = []
    for k in range(min(m, n)):
        while True:
            nz = [(abs(A[i][j]), i, j) for i in range(k, m) for j in range(k, n) if A[i][j] != 0]
            if not nz: return d + [0]*(n - k), V
            _, pi, pj = min(nz)
            A[k], A[pi] = A[pi], A[k]; colswap(k, pj)
            done = True
            for i in range(k + 1, m):
                q = A[i][k] // A[k][k]
                A[i] = [x - q*y for x, y in zip(A[i], A[k])]
                if A[i][k] != 0: done = False
            for j in range(k + 1, n):
                q = A[k][j] // A[k][k]; colop(j, k, q)
                if A[k][j] != 0: done = False
            if not done: continue
            bad = [(i, j) for i in range(k + 1, m) for j in range(k + 1, n) if A[i][j] % A[k][k] != 0]
            if bad:
                i, _ = bad[0]; A[k] = [x + y for x, y in zip(A[k], A[i])]; continue
            d.append(abs(A[k][k])); break
    return d + [0]*(n - len(d)), V
from math import gcd
def zn_kernel(M, ncol, N):
    d, V = smith(M)
    gens = []
    ranges = []
    for i in range(ncol):
        g = gcd(d[i], N) if d[i] != 0 else N
        step = N // g
        ranges.append([step*k for k in range(g)])
    out = []
    for ys in itertools.product(*ranges):
        x = [sum(V[r][c]*ys[c] for c in range(ncol)) % N for r in range(ncol)]
        if any(x): out.append(x)
    return out
def cyc(x, N): return min(x % N, (-x) % N)
table = {}
for N in range(2, 14):
    best_supp, best_l1, at_l1 = None, None, []
    for S in leaves:
        cols, M = leaf_matrix(S)
        for x in zn_kernel(M, len(cols), N):
            # verify directly
            for row in M:
                assert sum(a*b for a, b in zip(row, x)) % N == 0
            s = sum(1 for v in x if v); l1 = sum(cyc(v, N) for v in x)
            best_supp = s if best_supp is None else min(best_supp, s)
            if best_l1 is None or l1 < best_l1: best_l1, at_l1 = l1, []
            if l1 == best_l1: at_l1.append(canon_dbl({cols[i]: x[i] for i in range(len(cols)) if x[i]}))
    kinds = []
    for mv in set(at_l1):
        n_face = sum(1 for sl, _ in mv if sl[1] == -1); n_diag = len(mv) - n_face
        kinds.append((len(mv), n_diag, n_face))
    table[N] = (best_supp, best_l1, sorted(set(kinds)), len(set(at_l1)))
    print(f"   N={N:2d}: min support {best_supp}, min cyclic steps {best_l1}, minimizers (support,diag,face) {sorted(set(kinds))} x{len(set(at_l1))}", flush=True)
# expectations
planar_mod2 = sum(1 for v in clean(planar_p(0, 1)).values() if v % 2)
check("G1 N=2: six-face cube is the minimum (support 6, 6 steps, the only minimizer); planar mod 2 has 8 slots",
      table[2][0] == 6 and table[2][1] == 6 and table[2][2] == [(6, 0, 6)] and table[2][3] == 1 and planar_mod2 == 8)
cube_N4 = table[4]
check("G2 N=4: minimum 12 steps shared by the planar moves and the half-period cube (2 on six faces)", table[4][1] == 12 and any(k == (6, 0, 6) for k in table[4][2]), str(table[4]))
odd_ok = all(table[N][0] == 10 for N in (3, 5, 7, 9, 11, 13))
check("G3 odd N: minimum support 10 (the integer value) for N = 3,5,7,9,11,13", odd_ok, str({N: table[N][:2] for N in (3,5,7,9,11,13)}))
check("G4 N=3: the planar move needs only 10 steps (-2 = +1 mod 3)", table[3][1] == 10, str(table[3]))
check("G5 N >= 5 odd and N = 6..13: minimum 12 steps (lifting lemma covers N >= 12)", all(table[N][1] == 12 for N in range(5, 14)), str({N: table[N][1] for N in range(5,14)}))

# every N at once: a leaf has a nonzero Z_N kernel iff an invariant is 0 or shares a prime with N
inv_primes = {}
for S in leaves:
    cols, M = leaf_matrix(S)
    d, _ = smith(M)
    ps = set()
    zero = any(x == 0 for x in d[:len(cols)])
    for x in d[:len(cols)]:
        if x > 1: ps |= set(sp.factorint(x))
    inv_primes.setdefault(len(S), set())
    inv_primes[len(S)] |= ps | ({"rank<cols"} if zero else set())
print("   primes dividing a Smith invariant (or rational rank deficiency), by leaf size:",
      {k: sorted(map(str, v)) for k, v in sorted(inv_primes.items())}, flush=True)
small = set().union(*[v for k, v in inv_primes.items() if k <= 9])
check("G6 all N: a Z_N move with support <= 9 exists iff N is even (only the prime 2 divides an invariant of a leaf of size <= 9)",
      small == {2}, str(sorted(map(str, small))))

# ---------------------------------------------------------------- effective-Hamiltonian amplitude
print("== H  order-12 amplitude (rotor slots, H0 = U sum_rows (Gv)^2, V = -h sum_s (X_s + X_s^dag))")
pp = clean(planar_p(0, 1))
slots = sorted(pp); tgt = [pp[s] for s in slots]
def syn(w):
    rows = G_apply({slots[i]: w[i] for i in range(len(w)) if w[i]})
    return sum(v*v for v in rows.values())
states = list(itertools.product(*[range(0, abs(tv) + 1) for tv in tgt]))
check("H1 monotone partial states form a 3*3*2^8 = 2304 box", len(states) == 2304)
def signed(k): return tuple(kk*(1 if tv > 0 else -1) for kk, tv in zip(k, tgt))
zero_syn = [k for k in states if syn(signed(k)) == 0]
check("H2 only the two endpoints have zero syndrome", sorted(zero_syn) == sorted([tuple(0 for _ in tgt), tuple(abs(tv) for tv in tgt)]))
F = {}
for k in sorted(states, key=sum):
    if sum(k) == 0: F[k] = Fraction(1); continue
    acc = Fraction(0)
    for i in range(len(k)):
        if k[i] > 0:
            prev = k[:i] + (k[i] - 1,) + k[i+1:]
            acc += F[prev]
    if sum(k) == 12: F[k] = acc
    else: F[k] = acc / syn(signed(k))
Aval = F[tuple(abs(tv) for tv in tgt)]
check("H3 A = sum over monotone paths of prod 1/|Gw|^2 = 111150053/31850496", Aval == Fraction(111150053, 31850496), str(Aval))

print(f"== done in {time.time()-T0:.0f}s")
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("SUMMARY: PROVED box-free: every nonzero finite-support integer move of the landed tensor stencil on Z^3 has support >= 10 "
          "and L1 >= 12, with equality exactly for the planar moves (algebraic proof + independent exhaustive connected-support search to size 12); "
          "rotor off-diagonal effective terms start at order 12 and are exactly the planar moves; unit-entry moves need >= 14 slots; "
          "Z_N: support <= 9 iff N even (every N); steps N=2 cube 6, N=3 planar 10, N=4 cube ties at 12, every other N 12")
    print("HIT box-free minimum move of the tensor stencil: support 10 / L1 12 exactly the planar pieces, no coefficient box, radius or anchor restriction")
