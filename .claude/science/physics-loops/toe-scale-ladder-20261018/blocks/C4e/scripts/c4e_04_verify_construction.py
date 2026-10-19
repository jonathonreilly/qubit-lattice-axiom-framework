#!/usr/bin/env python3
"""C4e-04: verification of the construction U = L2 o L1 (c4e_layers.py).

The load-bearing statement (L_i o L_i = id on every configuration, hence U is a reversible CA
and a QCA) is PROVED in NOTE.md (Lemma I).  This script checks the implementation and the
claimed properties:
  (1) L1, L2 involutions: exhaustive k<=3 (one magnon at origin, others in [-3,3]^3),
      exhaustive k=4 inside a 3x3x3 box, random finite configurations at densities 0.02..0.98;
  (2) translation covariance, number conservation;
  (3) T covariance (12 rotations about the origin) on random configurations;
  (4) O \\ T: fails as a pure site permutation, and fails with particle-hole (axis action, torus);
  (5) frozen singles; two-magnon sector = speed-1 face glider W_{s=-1}; all other pairs static;
  (6) range: exact dependency region (upper bound) and an empirical lower bound;
  (7) pair band.
"""
import sys, os, random, itertools, time
sys.path.insert(0, os.path.dirname(__file__))
from c4e_layers import Layer, U, CUBE
from c4e_common import TGROUP, OGROUP, act, glider_shift, add, sub, dist, is_face

PASS = FAIL = 0
def check(name, ok, info=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(('PASS' if ok else 'FAIL') + ': ' + name + (('  ' + info) if info else ''), flush=True)

t0 = time.time()
u = U(); L1, L2 = u.L1, u.L2
O = (0, 0, 0)
random.seed(20261019)

# (1) involutions -------------------------------------------------------------
box3 = [v for v in itertools.product(range(-3, 4), repeat=3) if v != O]
bad = n = 0
for k in (1, 2, 3):
    for rest in itertools.combinations(box3, k - 1):
        if k == 3 and rest[0] > rest[1]: continue
        c = frozenset((O,) + rest); n += 1
        for L in (L1, L2):
            if L.apply(L.apply(c)) != c: bad += 1
check('L1, L2 involutions on all k<=3 configs with a magnon at 0, others in [-3,3]^3', bad == 0,
      'configs=%d failures=%d (%.0fs)' % (n, bad, time.time() - t0))
cube27 = list(itertools.product(range(3), repeat=3))
bad = n = 0
for c in itertools.combinations(cube27, 4):
    c = frozenset(c); n += 1
    for L in (L1, L2):
        if L.apply(L.apply(c)) != c: bad += 1
check('L1, L2 involutions on all 4-magnon configs inside a 3x3x3 box', bad == 0,
      'configs=%d failures=%d (%.0fs)' % (n, bad, time.time() - t0))
bad = n = 0; nact = 0
for trial in range(1500):
    rho = random.choice([0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 0.98])
    side = random.choice([5, 6, 7])
    c = frozenset(z for z in itertools.product(range(side), repeat=3) if random.random() < rho)
    n += 1
    for L in (L1, L2):
        d, A = L.apply(c, return_active=True); nact += len(A)
        if L.apply(d) != c: bad += 1
    if u.inv(u(c)) != c: bad += 1
check('random finite configurations (densities 0.02-0.98): L_i^2 = id and U^-1 U = id', bad == 0,
      'configs=%d failures=%d, active units crossed in total=%d (%.0fs)' % (n, bad, nact, time.time() - t0))

# (2) translation covariance and conservation ---------------------------------
bad = 0
for trial in range(200):
    c = frozenset(z for z in itertools.product(range(5), repeat=3) if random.random() < 0.15)
    t = tuple(random.randint(-7, 7) for _ in range(3))
    ct = frozenset(add(z, t) for z in c)
    if u(ct) != frozenset(add(z, t) for z in u(c)) or len(u(c)) != len(c): bad += 1
check('translation covariance and magnon-number conservation (random)', bad == 0)

# (3) T covariance --------------------------------------------------------------
def gconf(g, c): return frozenset(act(g, z) for z in c)
badT = 0; badOdd = 0; oddwit = None
for trial in range(150):
    c = frozenset(z for z in itertools.product(range(-2, 3), repeat=3) if random.random() < random.choice([0.1, 0.2, 0.35]))
    Uc = u(c)
    for g in TGROUP:
        if u(gconf(g, c)) != gconf(g, Uc): badT += 1
for g in OGROUP:
    if g in TGROUP: continue
    P = frozenset({O, (1, 1, 0)})
    if u(gconf(g, P)) != gconf(g, u(P)):
        badOdd += 1; oddwit = oddwit or (g, sorted(gconf(g, P)), sorted(u(gconf(g, P))), sorted(gconf(g, u(P))))
check('T covariance: U(gc) = g U(c) for all 12 g in T (pure site permutations)', badT == 0, 'violations=%d' % badT)
print('  [phases] under the axis action even R act on-site by rotations about n, i.e. by e^{i theta_R N};'
      ' U conserves N, so these phases cancel exactly; T covariance is the permutation identity above.')
check('pure-permutation covariance FAILS for every R in O\\T (on the pair {0,e1+e2})', badOdd == 12,
      'example g=%s: U(gP)=%s but gU(P)=%s' % (oddwit[0], oddwit[2], oddwit[3]))
# axis action, odd R: site permutation composed with on-site particle-hole flip (torus L=8)
Lt = 8
def w8(z): return (z[0] % Lt, z[1] % Lt, z[2] % Lt)
ut = U(wrap=w8)
ALL = frozenset(itertools.product(range(Lt), repeat=3))
P = frozenset({O, (1, 1, 0)})
holes = ALL - P
lhs = ALL - ut(holes)              # positions of the holes after U
print('  [torus 8^3] two holes at {0,e1+e2} in the filled state move to %s; the two-magnon pair moves to %s'
      % (sorted(lhs), sorted(ut(P))))
# global particle-hole (complement) symmetry of each layer, random configurations on the torus
badC = 0
for trial in range(40):
    rho = random.choice([0.03, 0.1, 0.3, 0.5, 0.7, 0.9, 0.97])
    c = frozenset(z for z in ALL if random.random() < rho)
    if ut(ALL - c) != ALL - ut(c): badC += 1
check('U commutes with global particle-hole conjugation C (complement), 8^3 torus, random configs', badC == 0,
      'violations=%d (each layer is C-invariant: candidacy and crossing are complement-symmetric)' % badC)
print('  => for odd R the axis-action symbol is P_R C up to N-dependent phases; since UC = CU and U conserves N,')
print('     O covariance would require U P_R = P_R U for odd R, which fails (previous check). U is T- but not O-covariant.')
# (5) one- and two-magnon sectors ------------------------------------------------
ok1 = u(frozenset({O})) == frozenset({O}) and u.inv(frozenset({O})) == frozenset({O})
check('single magnons frozen (U and U^-1)', ok1)
badW = 0; nf = 0
for rho in itertools.product(range(-6, 7), repeat=3):
    if rho <= O: continue
    P = frozenset({O, rho}); v = glider_shift(O, rho, -1)
    want = frozenset({add(O, v), add(rho, v)})
    nf += is_face(rho)
    if u(P) != want: badW += 1
check('two-magnon sector: face pairs move by v(rho) (speed 1, s=-1 convention), all other pairs static',
      badW == 0, 'relative positions tested=%d (face=%d)' % (len([r for r in itertools.product(range(-6,7),repeat=3) if r > O]), nf))

# (6) range ------------------------------------------------------------------------
def dep_layer(L, x):
    R = set()
    for uu in L.units_at(x):
        for v in [uu] + list(L.N1(uu)) + list(L.N2(uu)):
            R |= L.sites(v)
    return R
r1 = max(dist(O, y) for y in dep_layer(L1, O))
r2 = max(dist(O, y) for y in dep_layer(L2, O))
D2 = dep_layer(L2, O)
DU = set()
for y in D2: DU |= {add(y, z) for z in dep_layer(L1, O)}
rU = max(dist(O, y) for y in DU)
# inverse U^-1 = L1 L2
D1 = dep_layer(L1, O); DUi = set()
for y in D1: DUi |= {add(y, z) for z in dep_layer(L2, O)}
rUi = max(dist(O, y) for y in DUi)
print('  dependency-region radii (upper bounds): L1 %d, L2 %d, U = L2 L1 %d, U^-1 = L1 L2 %d' % (r1, r2, rU, rUi))
# empirical lower bound: flip a site y, see which outputs change
maxd = 0; wit = None
for trial in range(3000):
    c = set(z for z in itertools.product(range(-3, 4), repeat=3) if random.random() < 0.12)
    y = tuple(random.randint(-6, 6) for _ in range(3))
    c2 = set(c) ^ {y}
    a, b = u(frozenset(c)), u(frozenset(c2))
    for x in (a ^ b):
        if x != y and dist(x, y) > maxd: maxd = dist(x, y); wit = (sorted(c), y, x)
print('  empirical: a single-site change at y altered U(c) at distance up to %d' % maxd)
check('range of U is finite: Chebyshev range <= %d (U) and <= %d (U^-1); empirical lower bound %d' % (rU, rUi, maxd),
      rU <= 6 and rUi <= 6 and maxd <= rU)

# (7) pair band ----------------------------------------------------------------------
print('  pair band: for each face orientation rho, U|P_x(rho)> = |P_{x+v(rho)}(rho)>, so with')
print('  |rho,K> = sum_x e^{iK.x}|P_x(rho)>:  U|rho,K> = e^{-iK.v(rho)}|rho,K>,  eps_rho(K) = -K.v(rho) mod 2pi,')
print('  group velocity d eps/dK = -v(rho)  (|v| = 1 site/tick along the face normal); 6 dispersive bands;')
print('  the 56 other near relative positions (62 with |rho|_inf <= 2 up to sign, minus 6 face) are static: flat bands.')
check('pair band dispersive with |v_g| = 1 (follows from the exact glider identity above)', badW == 0)
print('elapsed %.0fs' % (time.time() - t0))
print('TOTAL: PASS=%d FAIL=%d' % (PASS, FAIL))
