"""Phase B reviewer checks. Usage: python3 rB_checks.py SECTION ; each section writes logs/SECTION.log.
Sections: inv, sectors, pairs, sym_random, radius, structure."""
import sys, os, time, itertools, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rlib import *
import rA_onsite_action as RA   # reviewer's own Phase-A lifts (prints its own log on import)

sec = sys.argv[1]
os.makedirs('logs', exist_ok=True)
logf = open(f'logs/{sec}.log', 'w')
PASS = FAIL = 0
def out(s): print(s); logf.write(s + '\n'); logf.flush()
def chk(name, ok):
    global PASS, FAIL
    ok = bool(ok); PASS += ok; FAIL += (not ok); out(('PASS ' if ok else 'FAIL ') + name)
O = group_O()
def coords(L, c): return [(i // (L*L), (i // L) % L, i % L) for i in np.nonzero(c)[0]]
def cfg(L, pts):
    c = np.zeros(L**3, np.uint8)
    for p in pts: c[((p[0] % L)*L + p[1] % L)*L + p[2] % L] = 1
    return c

# on-site lifts in occupation basis: index 1 = magnon = +n spin, index 0 = vacuum (-n)
def lifts():
    out = {}
    Vn = RA.V[:, ::-1]   # columns: (-n), (+n)  -> index 0 vacuum, 1 magnon
    for gi, M in enumerate(O):
        u = RA.lift(psign(M) * np.abs(M)); out[gi] = Vn.conj().T @ u @ Vn
    return out
UN = lifts()
def phase(gi, c):
    """phase of V_g |c> = phase * |g.c'>"""
    u = UN[gi]; N = int(c.sum()); V = c.size
    if psign(O[gi]) == 1: a, b = u[0, 0], u[1, 1]
    else: a, b = u[1, 0], u[0, 1]
    assert np.isclose(abs(a), 1) and np.isclose(abs(b), 1)
    return np.exp(1j*((V - N)*np.angle(a) + N*np.angle(b)))
def Vg(gi, P, c): return phase(gi, c), act(O[gi], P, c)
def Vg_inv(gi, P, d):
    M = O[gi]; Pinv = np.empty_like(P); Pinv[P] = np.arange(P.size)
    c = np.empty_like(d); c[:] = d[P]          # undo permutation
    if psign(M) == -1: c = 1 - c
    ph, d2 = Vg(gi, P, c); assert np.array_equal(d2, d)
    return np.conj(ph), c
def covariant(l1, l2, gi, P, c):
    """check V_g U V_g^dag |c> == U|c> (amplitude and phase)"""
    ph1, c0 = Vg_inv(gi, P, c)
    d = U(l1, l2, c0)
    ph2, e = Vg(gi, P, d)
    return np.array_equal(e, U(l1, l2, c)) and np.isclose(ph1*ph2, 1)

t0 = time.time()
if sec in ('inv', 'inv_more'):
    rng = np.random.default_rng(2026 if sec == 'inv' else 4242)
    MULT = 1 if sec == 'inv' else 5
    for L in ((8, 10, 12) if sec == 'inv' else (8,)):
        l1, l2 = build(L); V = L**3
        bad = 0; ncross = {'L1': 0, 'B': 0, 'A': 0}; ntest = 0
        configs = []
        for rho in (0.01, 0.02, 0.05, 0.1, 0.2, 0.35, 0.5, 0.65, 0.8, 0.9, 0.95, 0.98, 0.99):
            for _ in range(6): configs.append((rng.random(V) < rho).astype(np.uint8))
        # packed-candidate stress: empty / full / half-space / slab backgrounds, then plant many
        # random unit patterns (D or D' of random units, with their controls satisfied)
        pts = np.array(list(itertools.product(range(L), repeat=3)))
        for bg in ('empty', 'full', 'half', 'slab', 'random'):
            for rep in range(30*MULT):
                if bg == 'empty': c = np.zeros(V, np.uint8)
                elif bg == 'full': c = np.ones(V, np.uint8)
                elif bg == 'half': c = (pts[:, 2] < L//2).astype(np.uint8)
                elif bg == 'slab': c = ((pts[:, 2] >= 2) & (pts[:, 2] < 5)).astype(np.uint8)
                else: c = (rng.random(V) < rng.random()).astype(np.uint8)
                nplant = int(rng.integers(5, 60))
                for _ in range(nplant):
                    lay = l1 if rng.random() < 0.4 else l2
                    u = int(rng.integers(len(lay.units)))
                    st = lay.pat[u] if rng.random() < .5 else 1 - lay.pat[u]
                    c[lay.S[u]] = st
                    if lay.ctrl[u] == 1: c[lay.G[u]] = 0
                    if lay.ctrl[u] == 2: c[lay.G[u]] = 1
                configs.append(c)
        for c in configs:
            ntest += 1
            d, A1 = l1.apply(c, True); e, A2 = l2.apply(d, True)
            ncross['L1'] += len(A1)
            for u in A2: ncross['B' if l2.ctrl[u] == 1 else 'A'] += 1
            ok = (np.array_equal(l1.apply(d), c) and np.array_equal(l2.apply(e), d)
                  and np.array_equal(Uinv(l1, l2, e), c) and e.sum() == c.sum())
            # also each layer an involution on the *other* layer's output inputs
            ok &= np.array_equal(l2.apply(l2.apply(c)), c) and np.array_equal(l1.apply(l1.apply(e)), e)
            bad += (not ok)
        chk(f'L={L}: L1^2=L2^2=id, U^-1 U=id, N conserved on {ntest} configs (random densities + packed stress); crossings {ncross}', bad == 0)
        chk(f'L={L}: both L2 kinds and L1 actually crossed (>=50 each)', min(ncross.values()) >= 50)
        # multi-tick orbit reversibility
        bad = 0
        for c in configs[::7]:
            x = c.copy()
            for _ in range(6): x = U(l1, l2, x)
            for _ in range(6): x = Uinv(l1, l2, x)
            bad += not np.array_equal(x, c)
        chk(f'L={L}: U^-6 U^6 = id on {len(configs[::7])} configs', bad == 0)
        out(f'  [t={time.time()-t0:.0f}s]')

elif sec == 'sectors':
    # k<=4 magnons in the O-closed box [-1,1]^3 and their complements (k<=4 holes); L = 8
    L = 8; l1, l2 = build(L); V = L**3
    box = list(itertools.product((-1, 0, 1), repeat=3))
    S = []
    for k in range(0, 5):
        for sub in itertools.combinations(box, k):
            c = cfg(L, sub); S.append(c); S.append(1 - c)
    out(f'{len(S)} configs (k<=4 magnons in [-1,1]^3 and the complementary hole configs)')
    Umap = {}; bad_inv = 0; moved = 0
    for c in S:
        d = U(l1, l2, c); Umap[c.tobytes()] = d
        bad_inv += not (np.array_equal(Uinv(l1, l2, d), c) and np.array_equal(l1.apply(l1.apply(c)), c)
                        and np.array_equal(l2.apply(l2.apply(l1.apply(c))), l1.apply(c)) and d.sum() == c.sum())
        moved += not np.array_equal(d, c)
    chk(f'all {len(S)}: L1^2=id, L2^2=id (on L1 output), U^-1 U = id, N conserved; {moved} moved by U', bad_inv == 0)
    outs = {d.tobytes() for d in Umap.values()}
    chk('U injective on the set (bijectivity witness)', len(outs) == len(S))
    out(f'  [t={time.time()-t0:.0f}s]')
    Ps = [site_perm(M, L) for M in O]
    bad = 0; badph = 0
    for c in S:
        Uc = Umap[c.tobytes()]
        for gi, M in enumerate(O):
            ph_c, gc = Vg(gi, Ps[gi], c)
            Ugc = Umap.get(gc.tobytes())
            assert Ugc is not None
            ph_d, gUc = Vg(gi, Ps[gi], Uc)
            # V U |c> = ph_c U|gc>  must equal  U V|c>?  covariance: V_g U = U V_g
            if not np.array_equal(Ugc, gUc): bad += 1
            elif not np.isclose(ph_c, ph_d): badph += 1
    chk(f'covariance V_g U = U V_g for all 24 g in O (axis action, phases) on all {len(S)} configs: '
        f'{bad} config mismatches, {badph} phase mismatches', bad == 0 and badph == 0)
    # witnesses: pure permutation for odd R, and C, are NOT symmetries
    c = cfg(L, [(0,0,0), (1,1,0)])
    def perm(P, x):
        o = np.empty_like(x); o[P] = x; return o
    oddfail = sum(not np.array_equal(U(l1, l2, perm(Ps[gi], c)), perm(Ps[gi], U(l1, l2, c)))
                  for gi, M in enumerate(O) if psign(M) == -1)
    chk(f'witness: pure permutation pi_R fails for {oddfail}/12 odd R on {{0,e1+e2}}', oddfail == 12)
    cC = 1 - c
    chk('witness: [U, C] != 0 on {0,e1+e2}', not np.array_equal(U(l1, l2, cC), 1 - U(l1, l2, c)))
    # random k=3,4 magnon/hole configs in a larger window, direct covariance under all 24 g (both centres)
    rng = np.random.default_rng(7); bad = 0; n = 0
    Pc = [site_perm(M, L, (1,1,1)) for M in O]
    for rep in range(120):
        k = int(rng.integers(3, 5))
        pts = [tuple(int(v) for v in rng.integers(-2, 3, 3)) for _ in range(k)]
        c = cfg(L, pts)
        if rep % 2: c = 1 - c
        for gi in range(24):
            for P in (Ps[gi], Pc[gi]):
                n += 1; bad += not covariant(l1, l2, gi, P, c)
    chk(f'direct covariance (site- and cube-centred O) on {n} (config,g) pairs, k=3,4 in [-2,2]^3, magnons and holes', bad == 0)
    out(f'  [t={time.time()-t0:.0f}s]')

elif sec == 'pairs':
    for L in (8, 10, 12):
        l1, l2 = build(L); V = L**3
        R = L//2 - 1 if L > 8 else 4
        one = cfg(L, [(0,0,0)])
        chk(f'L={L}: single magnon fixed by U and U^-1', np.array_equal(U(l1, l2, one), one) and np.array_equal(Uinv(l1, l2, one), one))
        chk(f'L={L}: single hole fixed by U and U^-1', np.array_equal(U(l1, l2, 1-one), 1-one) and np.array_equal(Uinv(l1, l2, 1-one), 1-one))
        rels = [r for r in itertools.product(range(-R, R+1), repeat=3) if r != (0,0,0)]
        if L == 8: rels = [r for r in itertools.product(range(-3, 5), repeat=3) if r != (0,0,0)]  # whole torus
        bad_m = bad_h = 0; mv_m = mv_h = 0
        for r in rels:
            zero = [a for a in range(3) if r[a] == 0]
            face = (len(zero) == 1 and all(abs(r[a]) == 1 for a in range(3) if r[a] != 0))
            if face:
                a = zero[0]; b, cc = [x for x in range(3) if x != a]
                v = [0, 0, 0]; v[a] = r[b]*r[cc]
            c = cfg(L, [(0,0,0), r]); h = 1 - c
            for sgn, x0, isH in ((1, c, False), (-1, h, True)):
                x = x0.copy(); ok = True
                for tick in range(1, 4):
                    x = U(l1, l2, x)
                    if face:
                        sh = [sgn*v[i]*tick for i in range(3)]
                        exp = cfg(L, [tuple(sh), tuple(r[i] + sh[i] for i in range(3))])
                        if isH: exp = 1 - exp
                    else: exp = x0
                    ok &= np.array_equal(x, exp)
                if isH: bad_h += not ok; mv_h += face
                else: bad_m += not ok; mv_m += face
        chk(f'L={L}: all {len(rels)} magnon pairs: {mv_m} face relative vectors (= 6 unordered face-pair orientations x 2 labelings) glide by v=rho_b rho_c e_a at 1 site/tick for 3 ticks, rest static; {bad_m} mismatches', bad_m == 0 and mv_m == 12)
        chk(f'L={L}: all {len(rels)} hole pairs: {mv_h} face relative vectors glide by -v, rest static; {bad_h} mismatches', bad_h == 0 and mv_h == 12)
        out(f'  [t={time.time()-t0:.0f}s]')

elif sec == 'sym_random':
    rng = np.random.default_rng(99)
    for L in (8, 10, 12):
        l1, l2 = build(L); V = L**3
        Ps = [site_perm(M, L) for M in O]; Pc = [site_perm(M, L, (1,1,1)) for M in O]
        pts = np.array(list(itertools.product(range(L), repeat=3)))
        bad = 0; n = 0; crossings = 0
        nconf = 16 if L < 12 else 10
        for rep in range(nconf):
            kind = rep % 4
            if kind == 0: c = (rng.random(V) < rng.choice([0.03, 0.97])).astype(np.uint8)
            elif kind == 1: c = (rng.random(V) < rng.random()).astype(np.uint8)
            else:
                c = np.zeros(V, np.uint8) if kind == 2 else (pts[:, 0] < L//2).astype(np.uint8)
                for _ in range(40):
                    lay = l1 if rng.random() < 0.4 else l2
                    u = int(rng.integers(len(lay.units)))
                    c[lay.S[u]] = lay.pat[u] if rng.random() < .5 else 1 - lay.pat[u]
                    if lay.ctrl[u] == 1: c[lay.G[u]] = 0
                    if lay.ctrl[u] == 2: c[lay.G[u]] = 1
            crossings += int((U(l1, l2, c) != c).sum())
            for gi in range(24):
                for P in (Ps[gi], Pc[gi]):
                    n += 1; bad += not covariant(l1, l2, gi, P, c)
            # translation invariance
            t = tuple(int(x) for x in rng.integers(0, L, 3))
            Pt = (((pts[:, 0]+t[0]) % L)*L + (pts[:, 1]+t[1]) % L)*L + (pts[:, 2]+t[2]) % L
            ct = np.empty_like(c); ct[Pt] = c; Uc = U(l1, l2, c); Uct = np.empty_like(Uc); Uct[Pt] = Uc
            bad += not np.array_equal(U(l1, l2, ct), Uct)
        chk(f'L={L}: covariance under all 24 g (site+cube centred, phases) and a random translation on {nconf} finite-density/stress configs ({n} pairs; {crossings} changed sites)', bad == 0)
        out(f'  [t={time.time()-t0:.0f}s]')

elif sec == 'radius':
    L = 12; l1, l2 = build(L)
    def dist(i, j):
        a = np.array([i // (L*L), (i // L) % L, i % L]); b = np.array([j // (L*L), (j // L) % L, j % L])
        d = np.abs(a - b) % L; return int(np.max(np.minimum(d, L - d)))
    for name, lay in (('L1', l1), ('L2', l2)):
        x = 0; rad = 0
        units_x = [u for u in range(len(lay.units)) if x in lay.S[u]]
        for u in units_x:
            vs = [u] + [w for w in lay.N1[u] if w >= 0] + [w for w in lay.N2[u] if w >= 0]
            for v in vs:
                for s in list(lay.S[v]) + [g for g in lay.G[v] if g < lay.V]:
                    rad = max(rad, dist(x, s))
        chk(f'{name}: exact structural dependency radius = {rad} (claim 3)', rad == 3)
    # empirical single-flip influence
    rng = np.random.default_rng(5); V = L**3
    pts = np.array(list(itertools.product(range(L), repeat=3)))
    infl = {'L1': 0, 'L2': 0, 'U': 0}
    for rep in range(150):
        c = np.zeros(V, np.uint8) if rep % 3 == 0 else (np.ones(V, np.uint8) if rep % 3 == 1 else (rng.random(V) < rng.random()).astype(np.uint8))
        for _ in range(12):
            lay = l1 if rng.random() < 0.5 else l2
            u = int(rng.integers(len(lay.units)))
            c[lay.S[u]] = lay.pat[u] if rng.random() < .5 else 1 - lay.pat[u]
            if lay.ctrl[u] == 1: c[lay.G[u]] = 0
            if lay.ctrl[u] == 2: c[lay.G[u]] = 1
        y = int(rng.integers(V)); c2 = c.copy(); c2[y] ^= 1
        for name, f in (('L1', l1.apply), ('L2', l2.apply), ('U', lambda z: U(l1, l2, z))):
            dd = np.nonzero(f(c) ^ f(c2))[0]
            dd = [j for j in dd if j != y]
            if dd: infl[name] = max(infl[name], max(dist(y, j) for j in dd))
    out(f'empirical single-flip influence (150 trials, packed): {infl}')
    chk('empirical influence within proved bounds (L1,L2 <= 3, U <= 6)', infl['L1'] <= 3 and infl['L2'] <= 3 and infl['U'] <= 6)

elif sec == 'structure':
    # parity step: R in T maps B-units to B-units, odd R maps B<->A, with Gamma -> Gamma and {D,D'} -> {D,D'}
    T1, T2 = templates()
    def unitsets(t, p):
        tt = T2[t]
        S = [add(p, o) for o in tt['S']]
        D = frozenset(s for s, b in zip(S, tt['patD']) if b); Dp = frozenset(s for s, b in zip(S, tt['patD']) if not b)
        return tt['name'][0], frozenset(S), frozenset(add(p, o) for o in tt['G']), frozenset({D, Dp})
    allu = {}
    for t in range(6):
        for p in itertools.product(range(-3, 4), repeat=3):
            k, S, G, DD = unitsets(t, p); allu[(S, DD)] = (k, G)
    bad = 0; n = 0
    for M in O:
        for t in range(6):
            for p in itertools.product(range(-1, 2), repeat=3):
                k, S, G, DD = unitsets(t, p)
                f = lambda x: tuple(int(v) for v in M @ np.array(x))
                S2 = frozenset(map(f, S)); G2 = frozenset(map(f, G)); DD2 = frozenset(frozenset(map(f, d)) for d in DD)
                img = allu.get((S2, DD2)); n += 1
                if img is None: bad += 1; continue
                k2, Gimg = img
                want = k if psign(M) == 1 else ('A' if k == 'B' else 'B')
                bad += not (k2 == want and Gimg == G2)
    chk(f'parity step: T maps B->B, A->A; odd R maps B<->A; Gamma->Gamma; {{D,D\'}}->{{D,D\'}} ({n} unit images)', bad == 0)
    # squares: O maps plaquettes to plaquettes with diagonals to diagonals
    bad = 0
    sq = set()
    for t in range(3):
        for p in itertools.product(range(-3, 4), repeat=3):
            S = [add(p, o) for o in T1[t]['S']]
            sq.add(frozenset({frozenset(S[:2]), frozenset(S[2:])}))
    for M in O:
        f = lambda x: tuple(int(v) for v in M @ np.array(x))
        for t in range(3):
            for p in itertools.product(range(-1, 2), repeat=3):
                S = [add(p, o) for o in T1[t]['S']]
                img = frozenset({frozenset(map(f, S[:2])), frozenset(map(f, S[2:]))})
                bad += img not in sq
    chk('squares: every R in O maps square units to square units, diagonals to diagonals', bad == 0)
    # C-symmetry of the rule data: C maps candidacy 'Gamma empty' <-> 'Gamma full' and D <-> D'
    chk('complement of D within S is D\' for every template (crossing = XOR on S)',
        all(sorted(tt['patD']) == [0, 0, 1, 1] for tt in T1 + T2))

elif sec == 'sym_planted':
    # isolated planted units (spacing 4) on empty/full/half backgrounds + noise: many genuine crossings
    rng = np.random.default_rng(31)
    for L in (8, 12):
        l1, l2 = build(L); V = L**3
        Ps = [site_perm(M, L) for M in O]; Pc = [site_perm(M, L, (1,1,1)) for M in O]
        pts = np.array(list(itertools.product(range(L), repeat=3)))
        bad = 0; n = 0; cr = {'L1': 0, 'B': 0, 'A': 0}
        for rep in range(24 if L == 8 else 8):
            bg = rep % 3
            c = [np.zeros(V, np.uint8), np.ones(V, np.uint8), (pts[:, 1] < L//2).astype(np.uint8)][bg]
            for b in itertools.product(range(0, L, 4), repeat=3):
                lay = l1 if rng.random() < 0.3 else l2
                t = int(rng.integers(len(lay.units) // V))
                u = lay.uid[(t, b)]
                c[lay.S[u]] = lay.pat[u] if rng.random() < .5 else 1 - lay.pat[u]
                if lay.ctrl[u] == 1: c[lay.G[u]] = 0
                if lay.ctrl[u] == 2: c[lay.G[u]] = 1
            for _ in range(int(rng.integers(0, 4))): c[int(rng.integers(V))] ^= 1
            d, A1 = l1.apply(c, True); e, A2 = l2.apply(d, True); cr['L1'] += len(A1)
            for u in A2: cr['B' if l2.ctrl[u] == 1 else 'A'] += 1
            for gi in range(24):
                for P in (Ps[gi], Pc[gi]):
                    n += 1; bad += not covariant(l1, l2, gi, P, c)
        chk(f'L={L}: covariance under all 24 g (site+cube centred, phases) on planted configs ({n} pairs; crossings {cr})', bad == 0 and min(cr.values()) > 0)
        out(f'  [t={time.time()-t0:.0f}s]')

elif sec == 'influence':
    # targeted lower-bound search for the single-flip influence radius of U
    L = 12; l1, l2 = build(L); V = L**3; rng = np.random.default_rng(17)
    def dist(i, j):
        a = np.array([i // (L*L), (i // L) % L, i % L]); b = np.array([j // (L*L), (j // L) % L, j % L])
        d = np.abs(a - b) % L; return int(np.max(np.minimum(d, L - d)))
    best = {'L1': 0, 'L2': 0, 'U': 0}; ctr = l1.idx((6, 6, 6))
    for rep in range(int(sys.argv[2]) if len(sys.argv) > 2 else 600):
        c = [np.zeros(V, np.uint8), np.ones(V, np.uint8)][rep % 2].copy()
        for _ in range(int(rng.integers(1, 6))):
            lay = l1 if rng.random() < 0.5 else l2
            t = int(rng.integers(len(lay.units) // V))
            p = tuple(int(x) for x in 6 + rng.integers(-4, 5, 3)); u = lay.uid[(t, tuple(q % L for q in p))]
            c[lay.S[u]] = lay.pat[u] if rng.random() < .5 else 1 - lay.pat[u]
            if lay.ctrl[u] == 1: c[lay.G[u]] = 0
            if lay.ctrl[u] == 2: c[lay.G[u]] = 1
        base = {'L1': l1.apply(c), 'L2': l2.apply(c), 'U': U(l1, l2, c)}
        for y in rng.choice(np.nonzero(np.array([dist(ctr, j) <= 5 for j in range(V)]))[0], 30, replace=False):
            c2 = c.copy(); c2[y] ^= 1
            for name, f in (('L1', l1.apply), ('L2', l2.apply), ('U', lambda z: U(l1, l2, z))):
                dd = [j for j in np.nonzero(f(c2) ^ base[name])[0] if j != y]
                if dd: best[name] = max(best[name], max(dist(int(y), int(j)) for j in dd))
    out(f'targeted single-flip influence lower bounds: {best}')
    chk('influence lower bounds within proved upper bounds (L1, L2 <= 3; U <= 6)', best['L1'] <= 3 and best['L2'] <= 3 and best['U'] <= 6)

out(f'TOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]')
