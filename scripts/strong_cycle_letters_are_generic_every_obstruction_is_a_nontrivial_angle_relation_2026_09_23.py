#!/usr/bin/env python3
"""Generic strong cycle angles with neighbour uniqueness in the supplied parameter space.

Genericity is relative to the supplied continuous angle parameterization, not a physical distribution, selection mechanism or tuning measure. For (U), collision requires simultaneous equality of five forms; the bad set is contained in the finite union used in the proof, not necessarily equal to it. Small primes can annihilate nonzero integer coefficient vectors. Strong retains its prior definition; (U) is additional.

See the companion note for proofs and exact execution scope.
"""
import itertools
import random
import sys

AUDIT_TIMEOUT_SEC = 900
import time

PASS = FAIL = 0
T0 = time.time()


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))


def vec(j, k):
    """angle c_{j,k} in the 9 free parameters c_{j,0}, c_{j,1}, c_{j,2}."""
    v = [0] * 9
    if k < 3:
        v[3 * j + k] = 1
    else:
        for kk in range(3):
            v[3 * j + kk] = -1
    return tuple(v)


def lin(*terms):
    """sum of coefficient * vector."""
    out = [0] * 9
    for a, v in terms:
        for i in range(9):
            out[i] += a * v[i]
    return tuple(out)


def canon(v):
    """a relation and its negative cut the same hyperplane."""
    for x in v:
        if x:
            return v if x > 0 else tuple(-y for y in v)
    return v


print("== A. Decoding ==")
check("the parametrisation: each cycle's four angle vectors sum to zero, and the free angles are unit vectors",
      all(not any(lin(*[(1, vec(j, k)) for k in range(4)])) for j in range(3))
      and all(sorted(vec(j, k)) == [0] * 8 + [1] for j in range(3) for k in range(3)))
signed = [(s, j, k) for j in range(3) for k in range(4) for s in (1, -1)]
dec_rel = set()
dec_zero = 0
for (s, j, k), (t, jj, kk) in itertools.combinations(signed, 2):
    r = lin((s, vec(j, k)), (-t, vec(jj, kk)))
    dec_zero += not any(r)
    dec_rel.add(canon(r))
single_zero = sum(1 for j in range(3) for k in range(4) if not any(vec(j, k)))
check("every coincidence of two signed angles, and every vanishing angle, is a nonzero relation",
      dec_zero == 0 and single_zero == 0 and len(dec_rel) == 135, f"{len(dec_rel)} decoding hyperplanes")
print()

print("== B. Squares ==")
sq_rel, bent_zero, straight_nonzero, nb, ns = set(), 0, 0, 0, 0
for A, B in itertools.permutations(range(3), 2):
    for X in range(3):
        for Y in range(3):
            if X == A or Y == B or X == Y:
                continue
            for p, q, r, u in itertools.product(range(4), repeat=4):
                for sa, sb, sc, se in itertools.product((1, -1), repeat=4):
                    rel = lin((sa, vec(A, p)), (sb, vec(X, q)), (-sc, vec(B, r)), (-se, vec(Y, u)))
                    straight = X == B and Y == A and q == r and u == p and sb == sc and se == sa
                    if straight:
                        ns += 1
                        straight_nonzero += any(rel)
                    else:
                        nb += 1
                        bent_zero += not any(rel)
                        sq_rel.add(canon(rel))
check("every non-straight square is a nonzero relation, and every straight square the zero relation",
      bent_zero == 0 and straight_nonzero == 0 and ns == 6 * 16 * 4 and len(sq_rel) == 3645 and nb == 73344,
      f"{nb} non-straight configurations on {len(sq_rel)} sign-normalized relation vectors")
print()

print("== C. (U) ==")
keys = set()
nstars = 0
for sig in itertools.permutations(range(3)):
    for sens in itertools.product((1, -1), repeat=3):
        for k in itertools.product(range(4), repeat=3):
            for dirs in itertools.product((1, -1), repeat=3):
                B = [lin((sens[i], vec(sig[i], k[i]))) for i in range(3)]
                F = [lin((sens[i], vec(sig[i], (k[i] + dirs[i]) % 4))) for i in range(3)]
                key = (lin((1, B[1]), (-1, B[0])), lin((1, B[2]), (-1, B[0]))) + tuple(lin((1, F[i]), (1, B[0])) for i in range(3))
                keys.add(key)
                nstars += 1
check("the 24576 covariant stars have pairwise distinct symbolic neighbour classes",
      nstars == 24576 and len(keys) == 24576, "a collision needs a nonzero relation among the angles")
print()

print("== D. Random letters modulo a prime ==")


def table(m, cyc):
    tab = {}
    for j, c in enumerate(cyc):
        for kk, g in enumerate(c):
            for s in (1, -1):
                rr = (s * g) % m
                if rr == 0 or rr in tab:
                    return None
                tab[rr] = (s, j, kk)
    return tab


def strong(m, cyc):
    if table(m, cyc) is None:
        return False
    for A, B in itertools.permutations(range(3), 2):
        for X in range(3):
            for Y in range(3):
                if X == A or Y == B or X == Y:
                    continue
                for p, q, r, u in itertools.product(range(4), repeat=4):
                    for sa, sb, sc, se in itertools.product((1, -1), repeat=4):
                        if (sa * cyc[A][p] + sb * cyc[X][q] - sc * cyc[B][r] - se * cyc[Y][u]) % m == 0:
                            if not (X == B and Y == A and q == r and u == p and sb == sc and se == sa):
                                return False
    seen = set()
    for sig in itertools.permutations(range(3)):
        for sens in itertools.product((1, -1), repeat=3):
            for k in itertools.product(range(4), repeat=3):
                for dirs in itertools.product((1, -1), repeat=3):
                    Bv = [(sens[i] * cyc[sig[i]][k[i]]) % m for i in range(3)]
                    Fv = [(sens[i] * cyc[sig[i]][(k[i] + dirs[i]) % 4]) % m for i in range(3)]
                    key = ((Bv[1] - Bv[0]) % m, (Bv[2] - Bv[0]) % m) + tuple((Fv[i] + Bv[0]) % m for i in range(3))
                    if key in seen:
                        return False
                    seen.add(key)
    return True


counts = {}
for m in (1009, 10007, 100003):
    rng = random.Random(m)
    n = 0
    for _ in range(60):
        cyc = []
        for _ in range(3):
            a = rng.sample(range(1, m), 3)
            cyc.append(tuple(a + [(-sum(a)) % m]))
        n += strong(m, tuple(cyc))
    counts[m] = n
H = len(dec_rel) + len(sq_rel)
check("seeded conditioned samples reproduce the declared strong-with-(U) counts",
      counts == {1009: 1, 10007: 34, 100003: 56},
      f"strong of 60: {counts[1009]}, {counts[10007]}, {counts[100003]} at m = 1009, 10007, 100003")
band = all(H / (4 * m) <= (60 - counts[m]) / 60 <= 4 * H / m for m in (10007, 100003))
check("at m = 10007 and 100003 the observed bad fraction lies within a factor 4 of H/m",
      band, f"H = {H} counted decoding/square relations only (U omitted); bad of 60: {60 - counts[10007]}, {60 - counts[100003]}; H/m = {H / 10007:.3f}, {H / 100003:.3f}")
print()
print(f"time {time.time() - T0:.0f} s")
print('per_element: Exact arithmetic tests the declared angle, star or linear-system objects; no physical qubit encoding is inferred.')
print('per_site: Site checks cover only the explicit finite boxes, tori and samples printed above; boundary freedoms remain as stated in the note.')
print('per_mode: Analytic mode or symmetry arguments are conditional source proofs; finite runner cases alone do not prove untested universality.')
print('per_block: This is one bounded support result in a supplied relational record model, with the controls and counts declared above.')
print('lattice_wide: No physical infinite-volume conclusion is inferred; any whole-lattice or all-size statement is limited to the explicit source theorem hypotheses.')
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
