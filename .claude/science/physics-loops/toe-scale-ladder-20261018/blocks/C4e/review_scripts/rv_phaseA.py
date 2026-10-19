"""Phase A: independent checks (i)-(vii) of C4e claims, reviewer implementation.
Usage: python3 rv_phaseA.py [section ...]   (sections: inv sparse_dense local u1 sym single pair triple quad)
Log: ../review_logs? -> written to review_scripts/logs/phaseA_<section>.txt
"""
import sys, os, random, itertools, time
import numpy as np
import rv_core as C
import rv_dense as Dn

HERE = os.path.dirname(os.path.abspath(__file__))
LOGD = os.path.join(HERE, 'logs')
os.makedirs(LOGD, exist_ok=True)
rng = random.Random(20261019)
nrng = np.random.default_rng(20261019)


def to_dense(c, L, shift=(0, 0, 0)):
    a = np.zeros(L ** 3, bool)
    for x in c:
        y = tuple((x[i] + shift[i]) % L for i in range(3))
        a[np.ravel_multi_index(y, (L, L, L))] = True
    return a


def from_dense(a, L, shift=(0, 0, 0)):
    idx = np.nonzero(a)[0]
    cs = np.array(np.unravel_index(idx, (L, L, L))).T
    return frozenset(tuple(int(v) - shift[i] for i, v in enumerate(r)) for r in cs)


def perm_index(L, M=None, t=(0, 0, 0)):
    """index map p such that (g c)[p[s]] = c[s]  for g: x -> M x + t mod L"""
    V = L ** 3
    co = np.array(np.unravel_index(np.arange(V), (L, L, L))).T
    if M is not None:
        co = co @ np.array(M).T
    co = (co + np.array(t)) % L
    return np.ravel_multi_index(co.T, (L, L, L))


def gact(a, p):
    b = np.zeros_like(a)
    b[p] = a
    return b


def sec_inv(ck):
    # sparse: all k<=4 configs in small boxes (exhaustive k<=3 in 3x3x3 box; k=4 exhaustive in 3^3)
    box = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
    for k in range(0, 5):
        n = 0
        bad = 0
        for comb in itertools.combinations(box, k):
            c = frozenset(comb)
            for f in (C.L1, C.L2):
                if f(f(c)) != c:
                    bad += 1
            if C.Uinv(C.U(c)) != c or C.U(C.Uinv(c)) != c:
                bad += 1
            n += 1
        ck(bad == 0, f"(i) sparse: L1^2=L2^2=id, U^-1U=UU^-1=id on all {n} k={k} configs in 3^3 box")
    # k=4 in 4^3 box random, and k up to 8 in 5^3 random
    for (k, B, ns) in [(4, 4, 20000), (6, 5, 5000), (8, 5, 5000)]:
        boxB = [(x, y, z) for x in range(B) for y in range(B) for z in range(B)]
        bad = 0
        for _ in range(ns):
            c = frozenset(rng.sample(boxB, k))
            for f in (C.L1, C.L2):
                if f(f(c)) != c:
                    bad += 1
            if C.Uinv(C.U(c)) != c:
                bad += 1
        ck(bad == 0, f"(i) sparse: involutions on {ns} random k={k} configs in {B}^3 box")
    # dense random densities
    for L in (8, 10, 12):
        D = Dn.Dyn(L)
        bad = 0
        ns = 0
        nact = 0
        for p in (0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8):
            for _ in range(40 if L < 12 else 15):
                c = nrng.random(L ** 3) < p
                for lay in (D.l1, D.l2):
                    c1, a = lay(c, return_active=True)
                    nact += len(a)
                    if not np.array_equal(lay(c1), c):
                        bad += 1
                if not np.array_equal(D.Uinv(D.U(c)), c):
                    bad += 1
                ns += 1
        ck(bad == 0, f"(i) dense L={L}: L1^2=L2^2=id and U^-1U=id on {ns} random configs, p in 0.05..0.8 (total active units {nact})")


def sec_sparse_dense(ck):
    L = 12
    D = Dn.Dyn(L)
    bad = 0
    n = 0
    boxB = [(x, y, z) for x in range(4) for y in range(4) for z in range(4)]
    for k in (2, 3, 4, 5, 6, 10, 20):
        for _ in range(300):
            c = frozenset(rng.sample(boxB, k))
            sh = (4, 4, 4)
            for fs, fd in ((C.L1, D.l1), (C.L2, D.l2), (C.U, D.U), (C.Uinv, D.Uinv)):
                if from_dense(fd(to_dense(c, L, sh)), L, sh) != fs(c):
                    bad += 1
            n += 1
    ck(bad == 0, f"sparse (Z^3) and dense (torus L=12) implementations agree on {n} random clusters (k=2..20), all four maps")


def sec_local(ck):
    for L in (10, 12):
        D = Dn.Dyn(L)
        ck(D.l1.radius == 3 and D.l2.radius == 3,
           f"(ii) L={L}: exact per-layer dependency radius from definition: L1={D.l1.radius}, L2={D.l2.radius} (claim 3)")
        co = D.l1.coords
        mx = {'L1': 0, 'L2': 0, 'U': 0, 'Uinv': 0}
        hist = {}
        ns = 0
        t0 = time.time()
        for p in (0.1, 0.2, 0.3, 0.4, 0.5):
            for _ in range(40 if L == 10 else 12):
                c = nrng.random(L ** 3) < p
                outs = {'L1': D.l1(c), 'L2': D.l2(c), 'U': D.U(c), 'Uinv': D.Uinv(c)}
                for _ in range(10):
                    y = nrng.integers(L ** 3)
                    c2 = c.copy()
                    c2[y] = ~c2[y]
                    for name, f in (('L1', D.l1), ('L2', D.l2), ('U', D.U), ('Uinv', D.Uinv)):
                        o2 = f(c2)
                        ch = np.nonzero(o2 != outs[name])[0]
                        ch = ch[ch != y]
                        if len(ch):
                            d = (co[ch] - co[y] + L // 2) % L - L // 2
                            r = int(np.abs(d).max(1).max())
                            mx[name] = max(mx[name], r)
                            if name == 'U':
                                hist[r] = hist.get(r, 0) + 1
                    ns += 1
        ck(mx['L1'] <= 3 and mx['L2'] <= 3 and mx['U'] <= 6 and mx['Uinv'] <= 6,
           f"(ii) L={L}: empirical max influence distance over {ns} flips: {mx} (bounds 3,3,6,6); U radius hist {dict(sorted(hist.items()))}; {time.time()-t0:.0f}s")
    # targeted lower bound search on U: sparse, small clusters, flip a far site
    best = 0
    wit = None
    boxB = [(x, y, z) for x in range(-3, 4) for y in range(-3, 4) for z in range(-3, 4)]
    for _ in range(30000):
        k = rng.randint(1, 6)
        c = frozenset(rng.sample(boxB, k))
        y = (rng.randint(-7, 7), rng.randint(-7, 7), rng.randint(-7, 7))
        c2 = c ^ {y}
        a, b = C.U(c), C.U(c2)
        diff = (a ^ b) - {y}
        if diff:
            r = max(C.cheb(z, y) for z in diff)
            if r > best:
                best, wit = r, (sorted(c), y)
    ck(best <= 6, f"(ii) sparse search, 30000 cluster+flip trials: max U influence distance found = {best} (witness {wit})")


def sec_u1(ck):
    D = Dn.Dyn(10)
    bad = 0
    pc = 0
    for p in np.linspace(0.02, 0.98, 25):
        for _ in range(8):
            c = nrng.random(1000) < p
            u = D.U(c)
            if u.sum() != c.sum():
                bad += 1
            # particle-hole: U C = C U
            if not np.array_equal(D.U(~c), ~u):
                pc += 1
    ck(bad == 0, "(iii) U(1): N conserved by U on 200 random torus configs (L=10)")
    ck(pc == 0, "(iv-aux) particle-hole: U(~c) = ~U(c) on 200 random torus configs (L=10)")
    # translation invariance
    bad = 0
    for _ in range(50):
        c = nrng.random(1000) < 0.3
        t = tuple(int(v) for v in nrng.integers(0, 10, 3))
        p = perm_index(10, None, t)
        if not np.array_equal(D.U(gact(c, p)), gact(D.U(c), p)):
            bad += 1
    ck(bad == 0, "TI: U commutes with random torus translations (50 configs, L=10)")


def sec_sym(ck):
    for L in (8, 10):
        D = Dn.Dyn(L)
        badT = 0
        oddfail = 0
        nodd = 0
        for M in C.T12:
            p = perm_index(L, M)
            for q in (0.1, 0.3, 0.5):
                for _ in range(6):
                    c = nrng.random(L ** 3) < q
                    if not np.array_equal(D.U(gact(c, p)), gact(D.U(c), p)):
                        badT += 1
                    if not np.array_equal(D.Uinv(gact(c, p)), gact(D.Uinv(c), p)):
                        badT += 1
        for M in C.ODD12:
            p = perm_index(L, M)
            for q in (0.1, 0.3, 0.5):
                for _ in range(3):
                    c = nrng.random(L ** 3) < q
                    nodd += 1
                    if not np.array_equal(D.U(gact(c, p)), gact(D.U(c), p)):
                        oddfail += 1
        ck(badT == 0, f"(iv) L={L}: U and U^-1 commute with all 12 R in T (site permutation about origin) on 216 random configs each")
        # first run demanded failure on every random config (reviewer test-design error, kept in
        # logs/phaseA_sym_firstrun_KEPT.txt): configs with no active units commute trivially.
        ck(oddfail > 0, f"(iv) L={L}: U fails to commute with odd R on {oddfail}/{nodd} random configs (>0 required)")
    # sparse k-sectors
    box = [(x, y, z) for x in range(-2, 3) for y in range(-2, 3) for z in range(-2, 3)]
    bad = 0
    for _ in range(3000):
        c = frozenset(rng.sample(box, rng.randint(1, 4)))
        for M in C.T12:
            if C.U(C.act(M, c)) != C.act(M, C.U(c)):
                bad += 1
    ck(bad == 0, "(iv) sparse: T-covariance on 3000 random k<=4 clusters x 12 R")
    # odd R on the face pair
    P = frozenset([(0, 0, 0), (1, 1, 0)])
    res = [C.U(C.act(M, P)) != C.act(M, C.U(P)) for M in C.ODD12]
    ck(all(res), f"(iv) odd R: U P_R != P_R U on pair {{0,e1+e2}} for {sum(res)}/12 odd R")
    # explicit: image of the pair under odd R moves with opposite velocity sign relation
    M = C.ODD12[0]
    ck.info(f"   example odd R={M}: U(R P)={sorted(C.U(C.act(M,P)))}  R U(P)={sorted(C.act(M,C.U(P)))}")
    # On-site action of even R: rotation about n => in fixed-N sector a phase e^{i theta (N - V/2)};
    # U is an N-conserving permutation, so it commutes with any function of N. Verified as (iii).
    # Odd R: P_R C (up to N-dependent phase). With U C = C U, covariance <=> U P_R = P_R U, which fails.
    # Also check O-covariance fails even allowing U P_R C = P_R C U directly on dense torus:
    D = Dn.Dyn(8)
    p = perm_index(8, C.ODD12[0])
    c = to_dense(P, 8, (3, 3, 3))
    lhs = D.U(~gact(c, p))
    rhs = ~gact(D.U(c), p)
    ck(not np.array_equal(lhs, rhs), "(iv) odd R with particle-hole (P_R C) also not a symmetry (pair config, L=8 torus)")


def sec_single(ck):
    ok = all(C.U(frozenset([x])) == frozenset([x]) and C.Uinv(frozenset([x])) == frozenset([x])
             for x in [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (3, -2, 5)])
    ck(ok, "(v) single magnons fixed by U and U^-1 (sparse)")
    D = Dn.Dyn(8)
    ok = True
    for s in range(512):
        c = np.zeros(512, bool)
        c[s] = True
        ok &= np.array_equal(D.U(c), c) and np.array_equal(D.Uinv(c), c)
    ck(ok, "(v) single magnons fixed at all 512 sites, torus L=8")
    # single holes (particle-hole) also fixed
    ok = True
    for s in range(0, 512, 7):
        c = np.ones(512, bool)
        c[s] = False
        ok &= np.array_equal(D.U(c), c)
    ck(ok, "(v-aux) single holes in full background fixed")


def face_v(rho):
    z = [i for i in range(3) if rho[i] == 0]
    if len(z) != 1 or any(abs(r) != 1 for i, r in enumerate(rho) if i != z[0]):
        return None
    a = z[0]
    b, c = [i for i in range(3) if i != a]
    v = [0, 0, 0]
    v[a] = rho[b] * rho[c]
    return tuple(v)


def sec_pair(ck):
    R = 13
    moving = {}
    static = 0
    other = []
    near_static = 0
    near_total = 0
    for rho in itertools.product(range(-R, R + 1), repeat=3):
        if rho <= (0, 0, 0):
            continue
        P = frozenset([(0, 0, 0), rho])
        img = C.U(P)
        v = face_v(rho)
        if max(abs(r) for r in rho) <= 2:
            near_total += 1
        if v is not None:
            exp = C.tr(P, v)
            if img == exp and C.Uinv(exp) == P:
                moving[rho] = v
            else:
                other.append((rho, sorted(img)))
        else:
            if img == P and C.Uinv(P) == P:
                static += 1
                if max(abs(r) for r in rho) <= 2:
                    near_static += 1
            else:
                other.append((rho, sorted(img)))
    ck(len(moving) == 6 and not other,
       f"(vi) all {(27**3-1)//2} pairs with |rho|<={R}: 6 face-diagonal relative positions move by v=rho_b rho_c e_a, {static} static, anomalies {other[:5]}")
    ck(near_total == 62 and near_static == 56, f"(vi) near pairs |rho|<=2: total {near_total}, static {near_static} (claim 62 = 6 dispersive + 56 flat)")
    for rho, v in sorted(moving.items()):
        ck.info(f"   rho={rho} -> v={v}")
    P = frozenset([(0, 0, 0), (1, 1, 0)])
    ck(C.U(P) == frozenset([(0, 0, 1), (1, 1, 1)]), "(vi) {0,e1+e2} -> {e3,(1,1,1)} exactly")
    ck(C.L1(P) == frozenset([(1, 0, 0), (0, 1, 0)]), "(vi) intermediate L1 image {e1,e2}")
    # long run
    c = P
    for n in range(50):
        c = C.U(c)
    ck(c == C.tr(P, (0, 0, 50)), "(vi) 50 ticks: pair displaced by 50 e3 (speed 1)")
    # glider on dense torus with finite-density? only isolated; check on torus L=10 wrap: period L
    D = Dn.Dyn(10)
    a = to_dense(P, 10)
    b = a.copy()
    for n in range(10):
        b = D.U(b)
    ck(np.array_equal(a, b), "(vi) torus L=10: glider returns after 10 ticks (wraps)")
    # pair in all orientations under T are images of each other (T acts transitively on 6 face orientations?)
    orbs = set(C.canon_T(frozenset([(0, 0, 0), rho])) for rho in moving)
    ck.info(f"   T-orbits among the 6 moving pair shapes: {len(orbs)}")


def connected(c, d=2):
    c = list(c)
    seen = {c[0]}
    st = [c[0]]
    while st:
        x = st.pop()
        for y in c:
            if y not in seen and C.cheb(x, y) <= d:
                seen.add(y)
                st.append(y)
    return len(seen) == len(c)


def diam(c):
    c = list(c)
    return max(C.cheb(a, b) for a in c for b in c)


def classify(c, nmax=200, split_d=14):
    c0 = c
    seen = {}
    cur = c
    for n in range(1, nmax + 1):
        cur = C.U(cur)
        if cur == c0:
            return ('static' if n == 1 else 'periodic', n)
        if C.normalize(cur) == C.normalize(c0):
            return ('rigid', n)
        if diam(cur) > split_d:
            return ('split', n)
    return ('undecided', nmax)


def sec_triple(ck):
    t0 = time.time()
    R = 2
    reps = set()
    rng3 = [(x, y, z) for x in range(-2 * R, 2 * R + 1) for y in range(-2 * R, 2 * R + 1) for z in range(-2 * R, 2 * R + 1)]
    near = [p for p in rng3 if p != (0, 0, 0) and max(map(abs, p)) <= 2 * R]
    for a, b in itertools.combinations(near, 2):
        c = frozenset([(0, 0, 0), a, b])
        if connected(c, R):
            reps.add(C.canon_T(c))
    n = len(reps)
    ck(n == 478, f"(vii) connected triples (Chebyshev-2 adjacency graph connected) modulo translations+T: {n} orbits (claim 478)")
    # also count Chebyshev-1 connected for info
    reps1 = set(r for r in reps if connected(r, 1))
    ck.info(f"   of which Chebyshev-1 connected: {len(reps1)}")
    counts = {}
    per = []
    for r in sorted(reps):
        cl, nn = classify(frozenset(r))
        counts[cl] = counts.get(cl, 0) + 1
        if cl == 'periodic':
            per.append((r, nn))
    ck(counts.get('static', 0) == 403 and counts.get('periodic', 0) == 6 and counts.get('split', 0) == 69
       and counts.get('rigid', 0) == 0,
       f"(vii) 3-magnon dynamics classes: {counts} (claim static 403, periodic 6, split 69, rigid 0); {time.time()-t0:.0f}s")
    for r, nn in per:
        ck.info(f"   periodic: {r} period {nn}")
    # pair meets single head-on: reflection
    P = frozenset([(0, 0, 0), (1, 1, 0)])
    res = []
    for h in range(3, 9):
        for sx, sy in [(0, 0), (1, 1), (1, 0), (0, 1)]:
            c = P | {(sx, sy, h)}
            cur = c
            for _ in range(3 * h + 10):
                cur = C.U(cur)
            single_ok = (sx, sy, h) in cur
            rest = sorted(cur - {(sx, sy, h)})
            res.append(((sx, sy, h), single_ok, rest))
    for r in res[:8]:
        ck.info(f"   pair {{0,e1+e2}} + single at {r[0]}: single still there: {r[1]}; others after 3h+10 ticks: {r[2]}")


def sec_quad(ck):
    # k=4: involution and T covariance, and pair-pair collisions
    box = [(x, y, z) for x in range(-2, 3) for y in range(-2, 3) for z in range(-2, 3)]
    bad = 0
    for _ in range(3000):
        c = frozenset(rng.sample(box, 4))
        if C.Uinv(C.U(c)) != c:
            bad += 1
        M = rng.choice(C.T12)
        if C.U(C.act(M, c)) != C.act(M, C.U(c)):
            bad += 1
    ck(bad == 0, "(i,iv) k=4: U^-1U=id and T-covariance on 3000 random 4-clusters")
    # head-on pairs
    P = frozenset([(0, 0, 0), (1, 1, 0)])
    Q = frozenset([(0, 0, 0), (1, -1, 0)])  # moves -e3
    out = []
    for h in range(4, 10):
        for dx, dy in [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (2, 0)]:
            c = P | C.tr(Q, (dx, dy + 1, h))  # shift so they don't overlap
            if len(c) != 4:
                continue
            cur = c
            T = 2 * h + 20
            for _ in range(T):
                cur = C.U(cur)
            # free motion prediction
            free = C.tr(P, (0, 0, T)) | C.tr(Q, (dx, dy + 1, h - T))
            zs = sorted(cur, key=lambda x: x[2])
            out.append(((dx, dy, h), cur == free, zs))
    npass = sum(1 for o in out if o[1])
    ck.info(f"   head-on pair-pair: {npass}/{len(out)} pass with no shift; e.g. {out[0]}")
    shifts = []
    for o in out:
        cur = o[2]
        # find two pairs: upper and lower halves
        hi = [x for x in cur if x[2] > 0]
        lo = [x for x in cur if x[2] <= 0]
        shifts.append((o[0], len(hi), len(lo)))
    ck.info(f"   (pairs after collision: counts above/below z=0) {shifts}")


SECS = {'inv': sec_inv, 'sparse_dense': sec_sparse_dense, 'local': sec_local, 'u1': sec_u1,
        'sym': sec_sym, 'single': sec_single, 'pair': sec_pair, 'triple': sec_triple, 'quad': sec_quad}

if __name__ == '__main__':
    secs = sys.argv[1:] or list(SECS)
    for s in secs:
        with open(os.path.join(LOGD, f'phaseA_{s}.txt'), 'w') as f:
            ck = C.Check(f)
            t0 = time.time()
            SECS[s](ck)
            ck.info(f"section {s} wall time {time.time()-t0:.0f}s")
            ck.total()
