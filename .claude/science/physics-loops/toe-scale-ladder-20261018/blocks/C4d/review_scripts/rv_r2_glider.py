#!/usr/bin/env python3
"""Reviewer's independent check of the C4d range-2 face-diagonal glider claim.

W (pair walk, range r=2, group T): face-diagonal pairs {x, x+rho}, rho with one
zero coordinate a and nonzero b,c, are shifted by s*v*e_a with v = -rho_b*rho_c
(s = +1 or -1 selects the two gliders, |shift| = speed 1 or 2); every other near
pair is fixed.  Checks:
  (a) W is T x| Z^3 covariant (pure permutations), Lemma-K support at r=2, and a
      bijection on near pairs;
  (b) spectator conflicts: two distinct valid triples (p,w), dist(w,p)>r, whose
      images (Wp) u {w} coincide (this is exactly (S) for a phase-free monomial W),
      and likewise for W^{-1} ((S-dag));
  (c) control: the same glider at r=1 must produce conflicts (Theorem P1).
"""
import itertools
PASS = FAIL = 0
def check(name, ok, info=''):
    global PASS, FAIL
    PASS += ok; FAIL += (not ok)
    print(('PASS' if ok else 'FAIL') + ': ' + name + ('  ' + info if info else ''), flush=True)

def parity(p): return sum(1 for i in range(3) for j in range(i+1, 3) if p[i] > p[j]) % 2
T = [(p, sg) for p in itertools.permutations(range(3)) for sg in itertools.product((1, -1), repeat=3)
     if parity(p) == 0 and sum(s < 0 for s in sg) % 2 == 0]
assert len(T) == 12
def act(g, v): p, sg = g; return tuple(sg[i] * v[p[i]] for i in range(3))
def dist(a, b): return max(abs(a[i]-b[i]) for i in range(3))
def add(a, b): return tuple(a[i]+b[i] for i in range(3))
def sub(a, b): return tuple(a[i]-b[i] for i in range(3))
def ball(c, r): return [add(c, d) for d in itertools.product(range(-r, r+1), repeat=3)]

def make_W(s, speed, R):
    def is_face(rho): return sorted(abs(c) for c in rho) == [0, 1, 1]
    def W(p):
        x, y = p; rho = sub(y, x)
        if not is_face(rho): return p
        a = [i for i in range(3) if rho[i] == 0][0]
        b, c = [i for i in range(3) if i != a]
        v = -rho[b] * rho[c] * s * speed
        e = [0, 0, 0]; e[a] = v; e = tuple(e)
        return tuple(sorted((add(x, e), add(y, e))))
    return W

def run(s, speed, R, verbose=True):
    W = make_W(s, speed, R)
    O = (0, 0, 0)
    rhos = sorted({max(v, tuple(-c for c in v)) for v in ball(O, R) if v != O})
    base = [tuple(sorted((O, r))) for r in rhos]
    # (a) covariance, support, bijectivity
    cov = all(tuple(sorted(act(g, z) for z in W(p))) == W(tuple(sorted(act(g, z) for z in p)))
              for g in T for p in base)
    supp = all(dist(a, b) <= R for p in base for a in W(p) for b in p)
    region = [tuple(sorted((a, add(a, r)))) for a in ball(O, 3) for r in rhos]
    imgs = [W(p) for p in region]
    bij = len(set(imgs)) == len(imgs)
    Winv = {W(p): p for p in [tuple(sorted((a, add(a, r)))) for a in ball(O, 6) for r in rhos]}
    def Wi(q): return Winv[q]
    # (b) conflicts
    def conflicts(F):
        n = 0; ex = None
        for p1 in base:
            for w1 in ball(O, 2 * R + 2):
                if min(dist(w1, z) for z in p1) <= R: continue
                img = set(F(p1)) | {w1}
                # every other decomposition of img as valid (p2,w2) with w2 != w1
                for w2 in img:
                    if w2 == w1: continue
                    rest = tuple(sorted(img - {w2}))
                    # p2 must satisfy F(p2) = rest's pair part ... img = F(p2) u {w2}
                    q = rest
                    if dist(q[0], q[1]) > R: continue
                    p2 = Wi(q) if F is W else W(q)
                    if min(dist(w2, z) for z in p2) > R:
                        n += 1
                        if ex is None: ex = (p1, w1, p2, w2, tuple(sorted(img)))
        return n, ex
    n1, ex1 = conflicts(W)
    n2, ex2 = conflicts(Wi)
    if verbose:
        print('  r=%d s=%+d speed=%d: covariant=%s support=%s bijective=%s conflicts(S)=%d (S-dag)=%d' %
              (R, s, speed, cov, supp, bij, n1, n2))
        if ex1: print('    example (S) conflict:', ex1)
    return cov, supp, bij, n1, n2

ok = True
for s in (1, -1):
    c, su, b, n1, n2 = run(s, 1, 2)
    ok &= c and su and b and n1 == 0 and n2 == 0
check('r=2, speed-1 face gliders (both directions): covariant, Lemma-K, bijective, 0 spectator conflicts', ok)
bad = True
for s in (1, -1):
    c, su, b, n1, n2 = run(s, 2, 2)
    bad &= c and (n1 > 0 or n2 > 0)
check('r=2, speed-2 face gliders: spectator conflicts present', bad)
ctl = True
for s in (1, -1):
    c, su, b, n1, n2 = run(s, 1, 1)
    ctl &= c and su and (n1 > 0 or n2 > 0)
check('control r=1 speed-1 glider: covariant, Lemma-K support, but conflicts present', ctl)
print('TOTAL: PASS=%d FAIL=%d' % (PASS, FAIL))
