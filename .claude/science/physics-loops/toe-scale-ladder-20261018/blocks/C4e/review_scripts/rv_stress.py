"""Reviewer stress tests of Lemma I in the regime where it is load-bearing: several candidate units
close to each other (random tori have very few active units).
 (1) exhaustive: two face-diagonal pairs at all relative offsets in [-7,7]^3, all 6x6 shapes;
 (2) two face pairs + one extra magnon (random, 60000);
 (3) many face pairs packed in a box (random), U^n then U^-n.
"""
import os, itertools, random, time
import rv_core as C

HERE = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(HERE, 'logs', 'stress.txt'), 'w')
ck = C.Check(f)
rng = random.Random(11)
SH = []
for a, b in C.PLANES:
    for sgn in (1, -1):
        v = [0, 0, 0]; v[a] = 1; v[b] = sgn
        SH.append(tuple(v))
O = (0, 0, 0)
t0 = time.time()
bad = 0; n = 0; act1 = act2 = 0


def nact(c, kind):
    # count crossed sites / 4
    return len(c ^ C.layer(c, kind)) // 4


for s1 in SH:
    P1 = frozenset([O, s1])
    for s2 in SH:
        for t in itertools.product(range(-7, 8), repeat=3):
            P2 = frozenset([t, C.add(t, s2)])
            if P1 & P2:
                continue
            c = P1 | P2
            for kind in 'ST':
                c1 = C.layer(c, kind)
                if C.layer(c1, kind) != c:
                    bad += 1
            a1 = nact(c, 'S'); a2 = nact(c, 'T')
            act1 += a1 >= 2; act2 += a2 >= 2
            n += 1
ck(bad == 0, f"(1) exhaustive two face pairs, offsets [-7,7]^3: {n} configs, L1^2=L2^2=id; configs with 2 simultaneously active units: L1 {act1}, L2 {act2}; {time.time()-t0:.0f}s")

t0 = time.time()
bad = 0; n = 0; mult = 0
for _ in range(60000):
    s1, s2 = rng.choice(SH), rng.choice(SH)
    t = tuple(rng.randint(-5, 5) for _ in range(3))
    z = tuple(rng.randint(-4, 4) for _ in range(3))
    c = frozenset([O, s1, t, C.add(t, s2), z])
    for kind in 'ST':
        c1 = C.layer(c, kind)
        if C.layer(c1, kind) != c:
            bad += 1
        if nact(c, kind) >= 2:
            mult += 1
    if C.Uinv(C.U(c)) != c:
        bad += 1
    n += 1
ck(bad == 0, f"(2) two face pairs + one magnon, {n} random configs: involutions and U^-1U = id; layer applications with >=2 active units: {mult}; {time.time()-t0:.0f}s")

t0 = time.time()
bad = 0; tot_act = 0; n = 0
for trial in range(400):
    B = rng.randint(6, 10)
    npair = rng.randint(3, 12)
    c = set()
    for _ in range(npair):
        s = rng.choice(SH)
        x = tuple(rng.randint(0, B) for _ in range(3))
        c |= {x, C.add(x, s)}
    for _ in range(rng.randint(0, 4)):
        c.add(tuple(rng.randint(0, B) for _ in range(3)))
    c = frozenset(c)
    cur = c
    for _ in range(8):
        for kind in 'ST':
            tot_act += nact(cur, kind)
            nxt = C.layer(cur, kind)
            if C.layer(nxt, kind) != cur:
                bad += 1
            cur = nxt
    for _ in range(8):
        cur = C.Uinv(cur)
    if cur != c:
        bad += 1
    n += 1
ck(bad == 0, f"(3) {n} packed face-pair configs: L_i^2 = id at every step and U^-8 U^8 = id; active-unit crossings {tot_act}; {time.time()-t0:.0f}s")
ck.total()
