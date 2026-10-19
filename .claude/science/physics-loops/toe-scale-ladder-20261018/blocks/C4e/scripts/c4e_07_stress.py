#!/usr/bin/env python3
"""C4e-07: stress test of Lemma I near the activity thresholds.  Configurations are built from
many face-diagonal pairs (random orientation and parity, i.e. candidates of both layers) plus a
few singles, packed so that candidates sit at mutual distances 1..5, where conditions (b),(c)
switch.  Also runs U for 8 steps and checks U^-8 U^8 = id.  Counts how many units were active."""
import sys, os, random, itertools, time
sys.path.insert(0, os.path.dirname(__file__))
from c4e_layers import U
PASS = FAIL = 0
def check(name, ok, info=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(('PASS' if ok else 'FAIL') + ': ' + name + (('  ' + info) if info else ''), flush=True)
FACES = [r for r in itertools.product((-1, 0, 1), repeat=3) if sorted(map(abs, r)) == [0, 1, 1]]
u = U(); random.seed(99); t0 = time.time()
bad = 0; nact = 0; ncfg = 0
for trial in range(700):
    side = random.choice([6, 8, 10])
    npairs = random.randint(2, 7); c = set()
    for _ in range(npairs):
        x = tuple(random.randrange(side) for _ in range(3)); r = random.choice(FACES)
        c |= {x, (x[0] + r[0], x[1] + r[1], x[2] + r[2])}
    for _ in range(random.randint(0, 3)): c.add(tuple(random.randrange(side) for _ in range(3)))
    c = frozenset(c); ncfg += 1
    for L in (u.L1, u.L2):
        d, A = L.apply(c, return_active=True); nact += len(A)
        if L.apply(d) != c: bad += 1
    x = c
    for t in range(8): x = u(x)
    for t in range(8): x = u.inv(x)
    if x != c: bad += 1
check('stress configurations (2-7 face pairs + singles, packed): L_i^2 = id and U^-8 U^8 = id',
      bad == 0, 'configs=%d active-unit events=%d failures=%d (%.0fs)' % (ncfg, nact, bad, time.time() - t0))
print('TOTAL: PASS=%d FAIL=%d' % (PASS, FAIL))
