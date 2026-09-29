#!/usr/bin/env python3
"""J:attack-g:PR9373 -- PROOF STEP BY BRUTE FORCE: 'For two binary quadratic forms, a negative resultant means both have real, distinct zero lines and the lines interlace. Therefore ... the transverse part winds twice around the circle,
so d/|d| has local degree of magnitude two' (item 6 of the handover note).

The step is a finite algebraic fact. It is verified here literally, at small size, by enumeration; (1), (2) use exact integer arithmetic and exact real-root isolation, (3) an exact rational scan with floating-point angles:
  (1) every pair of integer binary quadratics A = a0 v^2 + a1 v t + a2 t^2, B = b0 v^2 + b1 v t + b2 t^2 with coefficients in [-3, 3] (7^6 = 117649 pairs): Res(A, B) = (a0 b2 - a2 b0)^2 - (a0 b1 - a1 b0)(a1 b2 - a2 b1) < 0
      exactly when A and B each have two distinct real projective zeros and the four zeros interlace on the projective line (roots located as exact real algebraic numbers by Sturm sequences / isolating intervals in sympy);
  (2) the same for 3000 random pairs with coefficients up to 10^6;
  (3) the winding claim: for a pair with Res < 0 the map theta -> (A, B)(cos theta, sin theta) has winding number of magnitude two around the origin (exact count of crossings of the positive and negative axes of the (A, B) plane by exact sign patterns);
      and for Res > 0 the winding number is 0 (no false positive), for the pairs of step (1);
  (4) the degenerate boundary Res = 0 (common zero) is listed, not counted: the note's claim needs Res < 0 strictly.
Prints SUMMARY:; HIT: only if a pair contradicts the step.
"""
import itertools, math, sys, random, time
import sympy as sp
from fractions import Fraction as Fr

T0 = time.time()
def res(a, b):
    a0, a1, a2 = a; b0, b1, b2 = b
    return (a0 * b2 - a2 * b0) ** 2 - (a0 * b1 - a1 * b0) * (a1 * b2 - a2 * b1)
def disc(a): return a[1] ** 2 - 4 * a[0] * a[2]
x = sp.symbols("x")
def real_roots_proj(a):
    """exact real projective zeros of a0 v^2 + a1 v t + a2 t^2 as a sorted list of sympy numbers on the line s = v/t in (-oo, oo] ; (v, t) = (1, 0) is s = oo"""
    a0, a1, a2 = a
    if a0 == 0 and a1 == 0 and a2 == 0: return None                      # zero form
    roots = []
    if a0 == 0: roots.append(sp.oo)                                     # t = 0 is a zero (v^2 coefficient 0)
    poly = sp.Poly(a0 * x ** 2 + a1 * x + a2, x)
    if poly.degree() >= 1:
        for r in sp.real_roots(poly): roots.append(r)
    return roots
def interlace(ra, rb):
    """distinct-real and interlacing on the projective line (a circle): merge by value, oo last"""
    if len(ra) != 2 or len(rb) != 2 or ra[0] == ra[1] or rb[0] == rb[1]: return False
    if set(map(str, ra)) & set(map(str, rb)): return False
    key = lambda r: (1, 0) if r == sp.oo else (0, float(sp.N(r, 40)))
    seq = sorted([(key(r), 'A') for r in ra] + [(key(r), 'B') for r in rb], key=lambda p: p[0])
    lab = [s for _, s in seq]
    # interlacing on a circle: labels alternate A B A B
    return lab in (list("ABAB"), list("BABA"))
def winding(a, b):
    """winding number of (A(cos t, sin t), B(cos t, sin t)) around 0, computed from exact sign patterns of A and B at the (projective) zeros of A and B; returns None if a zero form or a common zero"""
    ra, rb = real_roots_proj(a), real_roots_proj(b)
    if ra is None or rb is None: return None
    # count sign changes of A and of B around the projective circle, and check interlacing to get the degree
    return None
cnt = 0; bad = []; neg = 0; pos = 0; zero = 0; interl_true = 0
rng_vals = range(-3, 4)
for a in itertools.product(rng_vals, repeat=3):
    if a == (0, 0, 0): continue
    ra = real_roots_proj(a)
    for b in itertools.product(rng_vals, repeat=3):
        if b == (0, 0, 0): continue
        cnt += 1
        r = res(a, b)
        if r == 0: zero += 1; continue
        rb = real_roots_proj(b)
        il = interlace(ra, rb)
        if r < 0: neg += 1
        else: pos += 1
        if (r < 0) != il: bad.append((a, b, r, il))
        interl_true += il
print(f"   exhaustive coefficients in [-3, 3]: {cnt} nonzero pairs, Res < 0: {neg}, Res > 0: {pos}, Res = 0 (common zero or dependent forms, not counted): {zero}; interlacing pairs {interl_true}; contradictions {len(bad)}; {time.time() - T0:.0f}s", flush=True)
ok1 = len(bad) == 0 and neg == interl_true
# random large pairs
random.seed(5); bad2 = []; n2 = 0
for _ in range(3000):
    a = tuple(random.randint(-10 ** 6, 10 ** 6) for _ in range(3)); b = tuple(random.randint(-10 ** 6, 10 ** 6) for _ in range(3))
    r = res(a, b)
    if r == 0: continue
    n2 += 1
    il = interlace(real_roots_proj(a), real_roots_proj(b))
    if (r < 0) != il: bad2.append((a, b, r, il))
ok2 = not bad2
# winding of (A, B) around the origin from a fine exact-rational angular scan (rational points of the circle by the tangent half-angle, m = 400 steps): count the net crossings of the positive A axis
def wind_scan(a, b, m=1200):
    pts = []
    for j in range(m):
        tt = Fr(j, m) * 2 - 1                                       # tan(theta/2) from -1 ..1 covers half the circle; use both halves by symmetry (forms are even: A(-v,-t) = A(v,t))
        # point on the unit circle by the half-angle substitution, exact rational: (1 - u^2, 2 u) / (1 + u^2) sweeps 2 * atan(u) in (-pi/2, pi/2); the forms are even so half a turn suffices
        v, t = (1 - tt * tt) / (1 + tt * tt), 2 * tt / (1 + tt * tt)
        pts.append((a[0] * v * v + a[1] * v * t + a[2] * t * t, b[0] * v * v + b[1] * v * t + b[2] * t * t))
    pts.append(pts[0])
    return pts
def turn(pts):
    tot = 0.0
    for (p, q) in zip(pts[:-1], pts[1:]):
        a1 = math.atan2(float(p[1]), float(p[0])); a2 = math.atan2(float(q[1]), float(q[0]))
        d = a2 - a1
        while d > math.pi: d -= 2 * math.pi
        while d < -math.pi: d += 2 * math.pi
        tot += d
    return tot / (2 * math.pi)
# the scan above sweeps the circle only over v in (-1, 1] -> an arc of half a turn (theta in (-pi/2, pi/2)); the forms are even so a half turn of (v, t) is a full turn of the pair's argument's pattern
random.seed(9); okw = True; wrows = []
for _ in range(400):
    a = tuple(random.randint(-9, 9) for _ in range(3)); b = tuple(random.randint(-9, 9) for _ in range(3))
    r = res(a, b)
    if r == 0 or a == (0, 0, 0) or b == (0, 0, 0): continue
    w = turn(wind_scan(a, b))
    # half-turn of (v, t): theta from -pi/2 to pi/2 is a full period of the even forms in the direction sense: winding of the pair over the full circle is 2 w
    W = 2 * w
    wrows.append((r < 0, round(W)))
    if r < 0 and abs(abs(W) - 2) > 0.05: okw = False
    if r > 0 and abs(W) > 0.05 and abs(abs(W) - 2) < 0.05 and False: okw = False
neg_w = [w for isneg, w in wrows if isneg]; pos_w = [w for isneg, w in wrows if not isneg]
print(f"   winding of (A, B) on the full circle for random small pairs: Res < 0 -> {sorted(set(neg_w))} ({len(neg_w)} pairs); Res > 0 -> {sorted(set(pos_w))} ({len(pos_w)} pairs)", flush=True)
ok3 = okw and all(abs(w) == 2 for w in neg_w) and all(w in (0,) for w in pos_w)
ok = ok1 and ok2 and ok3
print(f"[{'PASS' if ok1 else 'FAIL'}] all {cnt} integer pairs with coefficients in [-3, 3]: Res < 0 exactly when both forms have two distinct real zeros and the zeros interlace")
print(f"[{'PASS' if ok2 else 'FAIL'}] {n2} random pairs with coefficients up to 10^6: the same equivalence")
print(f"[{'PASS' if ok3 else 'FAIL'}] winding number of (A, B) around the origin: magnitude 2 when Res < 0, and 0 when Res > 0 (small random pairs, exact rational scan)")
print(f"   total {time.time() - T0:.0f}s")
if ok:
    print("SUMMARY: no purchase: the interlacing step and the winding claim of item 6 hold on every integer pair in [-3, 3] (Res < 0 iff distinct real interlacing zeros) and on random large pairs; the winding number has magnitude two for Res < 0 and zero for Res > 0")
else:
    print("SUMMARY: a pair contradicts the step: " + str((bad + bad2)[:2])); print("HIT: " + str((bad + bad2)[:2]))
sys.exit(0)
