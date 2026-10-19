"""Common geometry for C4e (written from scratch; no code shared with C4d).

Sites: integer 3-tuples.  Chebyshev range r = 2.
T = 12 rotations: signed permutation matrices with even permutation and an even number of
minus signs (the axis-action vacuum stabiliser; it fixes the origin, so T x| Z^3 is generated
by these and translations).
Glider W_s (s = -1 is the task's convention {0,e1+e2} -> {e3,(1,1,1)}): a face-diagonal pair
{x, x+rho}, rho with one zero coordinate a, moves by v = -rho_b*rho_c*s*e_a; every other pair
(near or far) is fixed.
"""
import itertools

R_RANGE = 2

def _parity(p):
    return sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j]) % 2

TGROUP = [(p, sg) for p in itertools.permutations(range(3))
          for sg in itertools.product((1, -1), repeat=3)
          if _parity(p) == 0 and sum(s < 0 for s in sg) % 2 == 0]
assert len(TGROUP) == 12
OGROUP = [(p, sg) for p in itertools.permutations(range(3))
          for sg in itertools.product((1, -1), repeat=3)
          if (_parity(p) + sum(s < 0 for s in sg)) % 2 == 0]
assert len(OGROUP) == 24

def act(g, v):
    p, sg = g
    return (sg[0] * v[p[0]], sg[1] * v[p[1]], sg[2] * v[p[2]])

def add(a, b): return (a[0] + b[0], a[1] + b[1], a[2] + b[2])
def sub(a, b): return (a[0] - b[0], a[1] - b[1], a[2] - b[2])
def neg(a): return (-a[0], -a[1], -a[2])
def dist(a, b): return max(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))
def dset(z, S): return min(dist(z, y) for y in S)

def ball(c, r=R_RANGE):
    return [add(c, d) for d in itertools.product(range(-r, r + 1), repeat=3)]

def is_face(rho):
    return sorted(abs(c) for c in rho) == [0, 1, 1]

def glider_shift(x, y, s):
    """shift vector of the pair {x,y} under W_s (zero vector if the pair is not a face pair)"""
    rho = sub(y, x)
    if not is_face(rho):
        return (0, 0, 0)
    a = [i for i in range(3) if rho[i] == 0][0]
    b, c = [i for i in range(3) if i != a]
    e = [0, 0, 0]; e[a] = -rho[b] * rho[c] * s
    return tuple(e)

def W(pair, s, inverse=False):
    x, y = pair
    v = glider_shift(x, y, s)
    if inverse: v = neg(v)
    return frozenset((add(x, v), add(y, v)))

def F_small(S, s, inverse=False):
    """the (known) map on configurations of <= 2 magnons"""
    S = list(S)
    if len(S) <= 1: return frozenset(S)
    assert len(S) == 2
    return W(S, s, inverse)

def canon(S, G=TGROUP):
    """canonical representative of the T x| Z^3 orbit of a finite set"""
    best = None
    for g in G:
        im = [act(g, z) for z in S]
        m = min(im)
        key = tuple(sorted(sub(z, m) for z in im))
        if best is None or key < best: best = key
    return best

def stabiliser(S, G=TGROUP):
    S = frozenset(S); m0 = min(S); out = set()
    for g in G:
        im = [act(g, z) for z in S]
        t = sub(m0, min(im))
        if frozenset(add(z, t) for z in im) == S: out.add((g, t))
    return frozenset(out)
